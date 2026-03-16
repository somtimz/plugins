"""Document reader for the RAG ingestion pipeline."""
import os

import pypdf
import pypdf.errors
import docx
from docx import Document

# Expose as a bare module-level name so tests can patch ``lib.reader.PdfReader``.
PdfReader = pypdf.PdfReader


class UnreadableError(Exception):
    pass


class EmptyDocumentError(Exception):
    pass


class FileSizeLimitError(Exception):
    pass


def read_document(path: str, max_file_size_mb: int) -> str:
    """Read a document from *path* and return its text content.

    Parameters
    ----------
    path:
        Absolute or relative path to the file.
    max_file_size_mb:
        Maximum allowed file size in megabytes.  Files larger than this
        limit are rejected before being opened.

    Returns
    -------
    str
        The full text content of the document.

    Raises
    ------
    FileSizeLimitError
        If the file exceeds *max_file_size_mb*.
    UnreadableError
        If the file format is unsupported or the file cannot be parsed.
    EmptyDocumentError
        If the file contains no extractable text.
    FileNotFoundError
        If *path* does not exist (propagated naturally).
    """
    size_bytes = os.path.getsize(path)
    if size_bytes > max_file_size_mb * 1024 * 1024:
        raise FileSizeLimitError(
            f"File {path!r} exceeds {max_file_size_mb} MB limit "
            f"({size_bytes / 1024 / 1024:.1f} MB)"
        )

    ext = os.path.splitext(path)[1].lower()

    if ext in (".txt", ".md"):
        with open(path, encoding="utf-8") as fh:
            content = fh.read()
        if not content.strip():
            raise EmptyDocumentError(f"Document {path!r} is empty.")
        return content

    if ext == ".pdf":
        try:
            reader = PdfReader(path)
        except pypdf.errors.PdfReadError as exc:
            raise UnreadableError(str(exc)) from exc
        pages_text = [page.extract_text() or "" for page in reader.pages]
        text = "\n".join(pages_text)
        if not text.strip():
            raise EmptyDocumentError(f"PDF {path!r} contains no extractable text.")
        return text

    if ext == ".docx":
        doc = Document(path)
        text = "\n".join(p.text for p in doc.paragraphs)
        if not text.strip():
            raise EmptyDocumentError(f"Document {path!r} is empty.")
        return text

    if ext == ".doc":
        raise UnreadableError(
            "Legacy .doc format is not supported. Convert to .docx first."
        )

    raise UnreadableError(f"Unsupported file format: {ext!r}")
