# Storage Contract: window.storage API

Both `itil-change-request` and `cab-review` skills MUST use this contract for all CR data operations.

## API

```javascript
// Read a key — returns { value: string } or null
await window.storage.get(key)

// Write a key — value must be a JSON string
await window.storage.set(key, jsonString)
```

## Keys

| Key Pattern | Value | Owner |
|-------------|-------|-------|
| `cr_index` | `JSON.stringify(string[])` — array of RFC IDs | Both skills (read/write) |
| `cr_{RFC-ID}` | `JSON.stringify(CR)` — full CR object | Both skills (read/write) |

## Invariants

1. Every ID in `cr_index` MUST have a corresponding `cr_{id}` record.
2. Every `cr_{id}` record MUST have its ID present in `cr_index` (except during deletion where index is updated first).
3. `updatedAt` MUST be set to `new Date().toISOString()` on every write to `cr_{id}`.
4. `cabHistory` is append-only — entries MUST NOT be modified or removed after creation.
5. Reads MUST handle `null` return (key does not exist) gracefully.

## Shared Functions

Both JSX artifacts MUST implement compatible versions of:

```javascript
// Read all CRs from storage
async function getCRs() {
  const idx = await window.storage.get("cr_index");
  if (!idx) return [];
  const ids = JSON.parse(idx.value);
  const out = [];
  for (const id of ids) {
    const r = await window.storage.get(`cr_${id}`);
    if (r) out.push(JSON.parse(r.value));
  }
  return out;
}

// Write a single CR (update index if new)
async function putCR(cr) {
  const saved = { ...cr, updatedAt: new Date().toISOString() };
  let ids = [];
  const idx = await window.storage.get("cr_index");
  if (idx) ids = JSON.parse(idx.value);
  if (!ids.includes(cr.id)) ids.push(cr.id);
  await window.storage.set("cr_index", JSON.stringify(ids));
  await window.storage.set(`cr_${cr.id}`, JSON.stringify(saved));
  return saved;
}

// Delete a CR (Draft only — caller must enforce)
async function deleteCR(id) {
  const idx = await window.storage.get("cr_index");
  if (!idx) return;
  const ids = JSON.parse(idx.value).filter(x => x !== id);
  await window.storage.set("cr_index", JSON.stringify(ids));
  // Note: window.storage may not support delete — overwrite with empty
}
```
