# What to Commit vs Ignore (Recommended)

The goal is for each client repo to be the **auditable source of truth** for strategy + execution, without leaking secrets.

---

## Always ignore (never commit)

- `.env` and any credential files
- Google service account JSON files (or any keys)
- API tokens / passwords
- Any vendor exports that contain PII

---

## Recommended to commit (high leverage)

### Planning + tracking
- Monthly allocations and trackers (CSV/MD)\n+- Benchmark summaries (CSV/MD)\n+- Execution checklists and progress trackers\n+
### Briefs (source of truth)
- JSON briefs for each content item\n+- A monthly `_index.json` / manifest\n+
### Generated outputs (only if you want full reproducibility)
- Review packets (`article.html`, `meta.txt`, `checklist.md`, `bundle.json`)\n+- Generation reports (pass/fail summaries)\n+
### Publishing safety
- Audit logs (every publish/update action)\n+- Backups/diffs for updates (especially if you ever update existing pages)\n+
---

## Optional / case-by-case

- Large crawls (Screaming Frog exports): commit if you explicitly want them versioned; otherwise keep them local or store in Drive.\n+- Raw third-party exports: prefer storing the “cleaned” / normalized version that you actually use for decisions.\n+
---

## Why commit these artifacts?

- Makes work reviewable (by you, a client, or future you).
- Makes executions reproducible.
- Prevents loss after machine changes or hard resets.
- Creates a paper trail for safety (what changed, when, and why).

