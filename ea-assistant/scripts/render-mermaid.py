#!/usr/bin/env python3
"""
render-mermaid.py — render Mermaid (.mmd) files to images using mermaid-cli (mmdc)

Usage:
    # Render a single file
    python ea-assistant/scripts/render-mermaid.py diagrams/my-diagram.mmd

    # Render all .mmd files in a directory
    python ea-assistant/scripts/render-mermaid.py EA-projects/my-engagement/diagrams/

    # Render with options
    python ea-assistant/scripts/render-mermaid.py diagrams/ --format svg --theme dark

    # Dry run (show what would be rendered, no output written)
    python ea-assistant/scripts/render-mermaid.py diagrams/ --dry-run

Options:
    --format   png | svg | pdf   (default: png)
    --theme    default | dark | forest | neutral | base   (default: default)
    --bg       Background colour: transparent | white | #rrggbb   (default: white)
    --width    Output width in pixels for PNG (default: 1920)
    --scale    Scale factor for PNG (default: 2, gives high-DPI output)
    --out-dir  Directory for output files (default: same directory as input)
    --dry-run  Show what would be rendered without running mmdc
    --mmdc     Path to mmdc binary (auto-detected if not specified)

Prerequisites:
    npm install -g @mermaid-js/mermaid-cli
    — OR —
    npx @mermaid-js/mermaid-cli (used automatically as fallback)
"""

import sys
import os
import shutil
import subprocess
import argparse
from pathlib import Path


# ---------------------------------------------------------------------------
# mmdc detection
# ---------------------------------------------------------------------------

def find_mmdc(explicit_path: str | None = None) -> tuple[list[str], str]:
    """
    Return (command_prefix, description) for invoking mmdc.
    Tries: explicit path → PATH binary → npx fallback.
    Raises RuntimeError if nothing is available.
    """
    if explicit_path:
        p = Path(explicit_path)
        if p.is_file():
            return [str(p)], f"explicit: {p}"
        raise RuntimeError(f"mmdc not found at specified path: {explicit_path}")

    # Check PATH
    mmdc_bin = shutil.which("mmdc")
    if mmdc_bin:
        return [mmdc_bin], f"PATH: {mmdc_bin}"

    # Check common npm global locations
    candidates = [
        Path.home() / ".npm-global" / "bin" / "mmdc",
        Path.home() / "node_modules" / ".bin" / "mmdc",
        Path("/usr/local/bin/mmdc"),
        Path("/usr/bin/mmdc"),
    ]
    # Windows
    candidates += [
        Path.home() / "AppData" / "Roaming" / "npm" / "mmdc.cmd",
        Path.home() / "AppData" / "Roaming" / "npm" / "mmdc",
    ]
    for c in candidates:
        if c.exists():
            return [str(c)], f"found: {c}"

    # npx fallback — available if node/npm is installed
    npx_bin = shutil.which("npx")
    if npx_bin:
        return [npx_bin, "-y", "@mermaid-js/mermaid-cli"], "npx fallback (will download on first run)"

    raise RuntimeError(
        "mermaid-cli (mmdc) not found.\n"
        "Install it with:  npm install -g @mermaid-js/mermaid-cli\n"
        "Or ensure 'npx' is on PATH for automatic download."
    )


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_file(
    input_path: Path,
    output_path: Path,
    cmd_prefix: list[str],
    fmt: str,
    theme: str,
    bg: str,
    width: int,
    scale: int,
    dry_run: bool,
) -> tuple[bool, str]:
    """
    Render a single .mmd file. Returns (success, message).
    """
    cmd = cmd_prefix + [
        "-i", str(input_path),
        "-o", str(output_path),
        "-t", theme,
        "-b", bg,
        "-w", str(width),
        "-s", str(scale),
    ]

    if dry_run:
        return True, f"  DRY    {input_path.name} → {output_path.name}"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode == 0:
            size_kb = output_path.stat().st_size // 1024 if output_path.exists() else 0
            return True, f"  OK     {input_path.name} → {output_path.name} ({size_kb} KB)"
        else:
            err = (result.stderr or result.stdout or "unknown error").strip()
            # Truncate long errors
            if len(err) > 200:
                err = err[:200] + "…"
            return False, f"  FAIL   {input_path.name} — {err}"
    except subprocess.TimeoutExpired:
        return False, f"  TIMEOUT {input_path.name} — mmdc took > 60 s"
    except FileNotFoundError as e:
        return False, f"  ERROR  {input_path.name} — {e}"


def collect_inputs(target: Path) -> list[Path]:
    """Return list of .mmd files from a file or directory."""
    if target.is_file():
        if target.suffix != ".mmd":
            raise ValueError(f"Input file must have .mmd extension: {target}")
        return [target]
    if target.is_dir():
        files = sorted(target.glob("*.mmd"))
        if not files:
            raise ValueError(f"No .mmd files found in: {target}")
        return files
    raise ValueError(f"Input path does not exist: {target}")


def output_path_for(input_path: Path, out_dir: Path | None, fmt: str) -> Path:
    base = out_dir if out_dir else input_path.parent
    return base / (input_path.stem + "." + fmt)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render Mermaid (.mmd) files to images using mermaid-cli (mmdc)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("input", help="A .mmd file or a directory containing .mmd files")
    parser.add_argument("--format", choices=["png", "svg", "pdf"], default="png",
                        help="Output format (default: png)")
    parser.add_argument("--theme", choices=["default", "dark", "forest", "neutral", "base"],
                        default="default", help="Mermaid theme (default: default)")
    parser.add_argument("--bg", default="white",
                        help="Background colour: transparent, white, or #rrggbb (default: white)")
    parser.add_argument("--width", type=int, default=1920,
                        help="Output width in pixels for PNG (default: 1920)")
    parser.add_argument("--scale", type=int, default=2,
                        help="Scale factor for PNG — 2 = high-DPI (default: 2)")
    parser.add_argument("--out-dir", default=None,
                        help="Directory for output files (default: same as input)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be rendered without running mmdc")
    parser.add_argument("--mmdc", default=None,
                        help="Explicit path to mmdc binary")

    args = parser.parse_args()

    # Resolve paths
    input_path = Path(args.input).resolve()
    out_dir = Path(args.out_dir).resolve() if args.out_dir else None

    # Collect input files
    try:
        inputs = collect_inputs(input_path)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    # Find mmdc
    try:
        cmd_prefix, cmd_desc = find_mmdc(args.mmdc)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    # Print header
    print(f"render-mermaid.py — {len(inputs)} file(s) → {args.format.upper()}")
    print(f"mmdc   : {cmd_desc}")
    print(f"theme  : {args.theme}  bg: {args.bg}  width: {args.width}px  scale: {args.scale}x")
    if args.dry_run:
        print("mode   : DRY RUN — no files will be written")
    print()

    # Render
    results = []
    for f in inputs:
        out = output_path_for(f, out_dir, args.format)
        ok, msg = render_file(
            f, out, cmd_prefix,
            args.format, args.theme, args.bg,
            args.width, args.scale,
            args.dry_run,
        )
        results.append((ok, msg))
        print(msg)

    # Summary
    ok_count = sum(1 for ok, _ in results if ok)
    fail_count = len(results) - ok_count
    print()
    if args.dry_run:
        print(f"Summary: {ok_count} would be rendered")
    else:
        print(f"Summary: {ok_count} rendered, {fail_count} failed")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
