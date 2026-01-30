# Staged AI Content Workflow (Draft-First, Human-in-the-Loop)

This workflow is designed to safely take you from **data → plan → briefs → AI drafts → WordPress drafts**, while minimizing the risk of overwriting existing content.

**Principle:** Nothing touches WordPress until you explicitly approve it, **one piece at a time**.

---

## Stage 0: Prerequisites

- **WordPress access** working (app password; REST API access).
- **Data access** (as available): GSC + GA4 + DataForSEO + crawl export (e.g., Screaming Frog).
- **Repo convention**: commit the *inputs* and *reviewable outputs* (briefs, trackers, review packets). Never commit secrets.

---

## Stage 1: Baseline + Target Selection (Safe)

Goal: establish a baseline and pick monthly targets (e.g., 5 new + 5 updates).

- Run benchmark tooling (GSC/GA4/DataForSEO where possible).
- Create a monthly plan (targets, intent, rough word counts, internal link targets).

**Checkpoint:** you can explain *why* each piece exists and what it should accomplish.

---

## Stage 2: Generate Briefs (Safe)

Briefs are your “contract” with the generator.

Each brief should include:
- Title + slug
- Target keyword + intent
- Word count target
- Required H2 outline
- FAQs (if required)
- Internal link targets (preferred as URLs; slug as fallback)
- Tables (if required)
- Key points / constraints (what must be included / avoided)

**Checkpoint:** you can hand the brief to a human writer and they could execute it.

---

## Stage 3: Generate Content Locally (Safe)

Goal: AI generates content **to local files only** (no WordPress).

Recommended outputs per piece:
- `article.html` (renderable review asset)
- `meta.txt` (meta title + meta description + keyword)
- `bundle.json` (single source of truth: HTML + meta + FAQ + tables + metrics)
- `checklist.md` (validation results + human spot-check prompts)

**Checkpoint:** content is readable, meets word count, and has no obvious hallucinations.

---

## Stage 4: Validation Gates (Safe)

Before anything is published, run strict validations (see `docs/AI_CONTENT_QUALITY_GATES.md`).

**Checkpoint:** failures are fixed locally (regenerate/revise) until PASS.

---

## Stage 5: Updates Require Diffs + Backups (Safe)

For any update to an existing post/page:

- Fetch the current content (read-only).
- Generate a **before/after diff**.
- Save a **backup** of the original JSON payload.

**Checkpoint:** you can clearly see what changes and you approve them.

---

## Stage 6: Dry-Run Publish (Safe)

Simulate the API calls that would be made:
- endpoints
- payloads
- which items are create vs update

**Checkpoint:** the payloads match what you intend (especially for updates).

---

## Stage 7: Publish ONE Piece to WordPress (Draft-Only)

Publish a single piece with explicit confirmation:
- New content: verify slug does **not** already exist.
- Updates: verify backups exist; apply the approved change strategy.
- Always publish as **draft** first.
- Log every action to an **audit log**.

**Checkpoint:** you review the WordPress draft URL in the editor.

---

## Stage 8: Repeat (One-at-a-Time), Then Promote Drafts Later

Once you’ve reviewed the drafts, you can:
- keep as drafts for stakeholder review
- or promote to publish in a separate, explicit step

**Checkpoint:** drafts are ready; publishing live is a deliberate decision, not a side effect.

