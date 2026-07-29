# Dashboard Grok Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `dashboard-grok/index.html` that loads predictions listed in `dashboard-grok/manifest.json` (from read-only `input/`), scores them against live Yahoo QQQ OHLC, and renders project-wide ranks, accuracy, heatmap (medals + Overall), and date detail.

**Architecture:** Client-only page fetches manifest → prediction JSONs → Yahoo QQQ daily bars; pure JS scoring; CI regenerates manifest on `input/` pushes (excluding `manifest.json` itself).

**Tech Stack:** Static HTML/CSS/JS, Python 3 manifest script, GitHub Actions, Yahoo chart API (CORS fallback via `api.allorigins.win`).

## Global Constraints

- Neutral: `|return%| < 0.01` → excluded from accuracy/weight
- Pre-market → `(close_D - open_D) / open_D`; intraday → `(open_next - close_D) / close_D`
- Weight: correct `+|r|*100`, wrong `-|r|*100`
- Columns = every `engine/model` (project-wide, not 3 silos)
- Heatmap medals 🥇🥈🥉 per row; bottom row Overall
- Light airy theme; `dashboard-grok/index.html` (Lora, `#FAFAFA`, `#16A34A`)
- Do not modify existing gainer-story dashboards

---

### Task 1: Manifest generator + tests

**Files:**
- Create: `scripts/generate-input-manifest.py`
- Create: `tests/test_generate_input_manifest.py`
- Create: `input/manifest.json` (generated)

**Produces:** CLI that writes `{ "generated_at", "files": ["input/..."] }` sorted; excludes `manifest.json`.

- [x] **Step 1:** Write pytest covering scan, exclude manifest, path shape
- [x] **Step 2:** Implement script; run tests; generate real `input/manifest.json`
- [ ] **Step 3:** Commit when user asks (skip unless requested)

### Task 2: GitHub Action

**Files:**
- Create: `.github/workflows/update-input-manifest.yml`

**Produces:** On push to `input/**` excluding `input/manifest.json`, regenerate and commit manifest + QQQ OHLC cache.

- [x] **Step 1:** Add workflow with path filters + bot commit

### Task 3: Dashboard page

**Files:**
- Create: `dashboard-grok.html` (evolve from mockup patterns in `dashboard-grok-mockup.html`)
- Create: `scripts/fetch-qqq-ohlc.py` + `input/qqq-ohlc.json` (Yahoo CORS fallback)

**Produces:** Full live dashboard per spec §§4–7, 10.

- [x] **Step 1:** Load manifest + predictions (concurrency 12) + dedupe latest timestamp
- [x] **Step 2:** Fetch Yahoo QQQ OHLC (+ proxies); fallback to `input/qqq-ohlc.json`
- [x] **Step 3:** Score, aggregate per column, rank
- [x] **Step 4:** Render leaderboard, accuracy table, heatmap (medals + Overall), date detail
- [x] **Step 5:** Empty/error states; light theme + 2–3 motions
- [x] **Step 6:** Smoke-check locally (python -m http.server) against real input/

### Task 4: Verify acceptance

- [x] Manifest lists ~326 files; dashboard loads columns ≈12
- [x] Heatmap rows = date×session newest-first + Overall
- [x] Pending intraday without next open excluded from scores
