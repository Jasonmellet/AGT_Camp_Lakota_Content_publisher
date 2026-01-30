# AI Content Quality Gates (Minimum Bar)

These gates exist to prevent low-quality drafts from reaching WordPress and to reduce “manual cleanup” time.

Treat failures as **hard stops**: revise/regenerate locally until PASS.

---

## Required gates

### Word count (strict)
- Must land within **±5%** of target.
- Rationale: ensures predictable depth and avoids “thin content” or bloated drafts.

### Metadata correctness
- Meta title: **≤ 60 characters**
- Meta description: **≤ 160 characters**
- Target keyword included in both (case-insensitive).
- Avoid stale years (e.g. “2024”) unless the brief explicitly calls for a dated page.

### Internal links (real links, not placeholders)
- Minimum **5 real internal links** for long-form content.
- If briefs provide internal link targets, ensure the final HTML contains **resolved URLs**.\n+- Zero unresolved placeholders (e.g. `{{link:...}}`).

### Required structure present
- H2 outline covered (don’t skip planned sections).
- If brief requires FAQ: FAQ section exists and answers are substantive.
- If brief requires tables: at least one valid HTML table exists for each required table.

### Readability (AIOSEO-inspired)
These are pragmatic targets for blog content that must be “skim-friendly”:
- Long sentences: **≤ 25%** of sentences exceed 20 words
- Flesch reading ease: **≥ 55** (heuristic; enough to avoid “very difficult”)
- Transition words: **≥ 20%** of sentences contain a transition word/phrase

---

## Recommended human spot-checks

- Verify claims are factual (no invented stats or regulations).
- Ensure the intro matches the search intent.
- Scan each H2: substantive, not fluff.
- Confirm internal links point to the correct pages and make sense in context.
- Confirm CTA placement is appropriate and non-spammy.

---

## If a draft fails gates

- **Word count off**: tighten/expand while preserving the outline and FAQs.
- **Meta fails**: rewrite meta, keep keyword inclusion, keep it human.\n+- **Links missing**: add links naturally inside relevant sections (not a link-dump).
- **Readability low**: shorten sentences, use simpler phrasing, add transitions, increase headings/lists.

