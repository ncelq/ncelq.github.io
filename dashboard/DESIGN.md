---
version: alpha
name: Signal Arena
description: Light-theme QQQ prediction scoreboard — project-wide rank across folder/model columns with accuracy, backtest, and battle heatmap.
colors:
  primary: "#16A34A"
  primary-deep: "#15803D"
  primary-soft: "#DCFCE7"
  primary-wash: "#F0FDF4"
  primary-bright: "#10B981"
  primary-mint: "#22C55E"
  secondary: "#64748B"
  secondary-soft: "#94A3B8"
  tertiary: "#E11D48"
  tertiary-bright: "#F43F5E"
  tertiary-soft: "#FFE4E6"
  tertiary-wash: "#FFF1F2"
  neutral: "#FAFAFA"
  surface: "#FFFFFF"
  on-surface: "#0F172A"
  on-surface-soft: "#334155"
  border: "#E2E8F0"
  border-soft: "#F1F5F9"
  surface-muted: "#F8FAFC"
  amber: "#D97706"
  amber-soft: "#FEF3C7"
  amber-wash: "#FFFBEB"
  amber-ink: "#92400E"
  error-ink: "#9F1239"
  podium-gold-border: "#F59E0B"
  podium-gold-wash: "#FFFBEB"
  tag-crash-bg: "#FFE0A3"
  tag-crash-ink: "#78350F"
  tag-llm-bg: "#DDD6FE"
  tag-llm-ink: "#4C1D95"
  tag-ppx-bg: "#BAE6FD"
  tag-ppx-ink: "#0C4A6E"
  threat-high-bg: "#FFEDD5"
  threat-high-ink: "#C2410C"
  heatmap-flat: "#CBD5E1"
typography:
  eyebrow:
    fontFamily: Source Sans 3
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.16em
  headline-display:
    fontFamily: Lora
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Lora
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Lora
    fontSize: 22.5px
    fontWeight: 700
    lineHeight: 1.2
  score-display:
    fontFamily: Lora
    fontSize: 43px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: -0.02em
  body-lg:
    fontFamily: Source Sans 3
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
  body-md:
    fontFamily: Source Sans 3
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
  body-sm:
    fontFamily: Source Sans 3
    fontSize: 12.5px
    fontWeight: 600
    lineHeight: 1.45
  label-lg:
    fontFamily: Source Sans 3
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
  label-md:
    fontFamily: Source Sans 3
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.07em
  label-sm:
    fontFamily: Source Sans 3
    fontSize: 11px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0.04em
  table-body:
    fontFamily: Source Sans 3
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
rounded:
  xs: 3px
  sm: 5px
  md: 6px
  lg: 12px
  xl: 18px
  full: 99px
spacing:
  xs: 4px
  sm: 8px
  md: 14px
  lg: 18px
  xl: 28px
  section: 44px
  gutter: 14px
  page-x: 22px
  page-y: 28px
  content-max: 1220px
components:
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-lg}"
  eyebrow:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary-deep}"
    typography: "{typography.eyebrow}"
  status-banner:
    backgroundColor: "{colors.amber-wash}"
    textColor: "{colors.amber-ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 12px
  status-banner-error:
    backgroundColor: "{colors.tertiary-wash}"
    textColor: "{colors.error-ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 12px
  meta-chip:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 5px
  meta-chip-value:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-deep}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 5px
  kpi-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.xl}"
    padding: 18px
  kpi-card-up:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-deep}"
    typography: "{typography.score-display}"
    rounded: "{rounded.xl}"
    padding: 18px
  kpi-card-down:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.tertiary}"
    typography: "{typography.score-display}"
    rounded: "{rounded.xl}"
    padding: 18px
  threat-chip-low:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.primary-deep}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 2px
  threat-chip-moderate:
    backgroundColor: "{colors.amber-soft}"
    textColor: "{colors.amber-ink}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 2px
  threat-chip-high:
    backgroundColor: "{colors.threat-high-bg}"
    textColor: "{colors.threat-high-ink}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 2px
  threat-chip-critical:
    backgroundColor: "{colors.tertiary-soft}"
    textColor: "{colors.error-ink}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 2px
  podium-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.xl}"
    padding: 18px
  podium-card-first:
    backgroundColor: "{colors.podium-gold-wash}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.xl}"
    padding: 26px
  table-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.table-body}"
    rounded: "{rounded.xl}"
    padding: 0px
  table-header:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.secondary}"
    typography: "{typography.label-md}"
    padding: 12px
  table-row-total:
    backgroundColor: "{colors.primary-wash}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-lg}"
    padding: 10px
  pipeline-tag-crash:
    backgroundColor: "{colors.tag-crash-bg}"
    textColor: "{colors.tag-crash-ink}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.md}"
    padding: 2.5px
  pipeline-tag-llm:
    backgroundColor: "{colors.tag-llm-bg}"
    textColor: "{colors.tag-llm-ink}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.md}"
    padding: 2.5px
  pipeline-tag-ppx:
    backgroundColor: "{colors.tag-ppx-bg}"
    textColor: "{colors.tag-ppx-ink}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.md}"
    padding: 2.5px
  accuracy-bar:
    backgroundColor: "{colors.primary-mint}"
    rounded: "{rounded.full}"
    height: 5px
  heatmap-cell:
    backgroundColor: "{colors.border-soft}"
    rounded: "{rounded.sm}"
    size: 27px
  heatmap-ok:
    backgroundColor: "{colors.primary-bright}"
  heatmap-bad:
    backgroundColor: "{colors.tertiary-bright}"
  heatmap-flat:
    backgroundColor: "{colors.heatmap-flat}"
---

# Signal Arena · DESIGN.md

Visual identity for `dashboard/index.html` — a client-only QQQ signal scoreboard.

## Overview

Signal Arena is a **calm trading scoreboard**: light, airy, and data-first. It should feel like a precise research desk — not a neon terminal, not a marketing landing page.

Brand personality: confident green for “correct / up / hold-aligned,” restrained slate for structure, and rose only for losses and wrong calls. Display type (Lora) carries hierarchy; Source Sans 3 carries the numbers and labels.

Emotional target: clarity under density. Every section has one job. Motion is a soft entrance (`rise`) and light card lift on hover — never decorative noise.

Audience: traders and model operators comparing folder/model columns across accuracy, excess PnL, and day-by-day battle outcomes.

## Colors

The palette is cool neutrals with a single **Forest Signal Green** accent, plus a mirrored rose for downside.

- **Primary (#16A34A):** Forest Signal Green — brand accent and large positive display scores (HOLD / up / correct). Prefer **primary-deep** for small UI text that must meet WCAG AA on white.
- **Primary deep (#15803D):** Darker green for meta chip values, eyebrow emphasis, and AA-safe green labels.
- **Primary soft / wash (#DCFCE7 / #F0FDF4):** Soft green washes for KPI “up” card gradients, table subtotals/totals, and row hover tint.
- **Primary bright / mint (#10B981 / #22C55E):** Heatmap “ok/up” cells and accuracy-bar gradients.
- **Secondary (#64748B):** Slate for supporting copy, section subtitles, table headers, and pipeline tag fallbacks.
- **Secondary soft (#94A3B8):** Faint slate for heatmap column labels and empty/N/A states — decorative, not body copy.
- **Tertiary (#E11D48):** Rose for wrong calls, negative scores, SELL-aligned losses, and error banners.
- **Tertiary soft / wash (#FFE4E6 / #FFF1F2):** Soft rose fills for KPI “down” card gradients and error status.
- **Neutral (#FAFAFA):** Page canvas — slightly off pure white so white panels read as surfaces.
- **Surface (#FFFFFF):** Cards, tables, podium tiles, meta chips.
- **On-surface (#0F172A):** Primary ink for headlines and body.
- **On-surface soft (#334155):** Secondary ink for meta and row labels.
- **Border (#E2E8F0 / #F1F5F9):** Structural hairlines; soft variant for row dividers and empty heatmap cells.
- **Amber family:** Warning banners and moderate threat chips only — never as a brand accent. Gold podium border (`#F59E0B`) is a first-place cue, not a semantic up/down color.
- **Pipeline tags:** Distinct pastel chips — Crash (amber), LLM (violet), PPX (sky) — so engines stay scannable without competing with green/rose semantics.

Semantic rule: green = correct / up / positive excess; rose = wrong / down / negative; slate = structure; amber = caution only.

## Typography

Two families only: **Lora** (display/headlines/scores) and **Source Sans 3** (UI, tables, labels).

- **Eyebrow:** Source Sans 3 Bold, uppercase, wide tracking — brand wordmark “Signal Arena” in primary green.
- **Headline display:** Lora Bold for the page H1; responsive clamp ~2.1–3.1rem; tight tracking.
- **Headline lg:** Lora Bold for section titles (~2rem).
- **Score display:** Lora Bold for KPI values and podium scores — the largest numeric voice on the page.
- **Body:** Source Sans 3 at 18px / 1.55 for page chrome; 15px muted for subtitles.
- **Labels:** Uppercase tracked labels for table headers and pipeline tags; compact 11px pills for threat/session chips.
- **Tables:** Source Sans 3 at 16px; pipe rows are heavier, uppercase, slate.

Do not introduce a third font. Prefer tabular-feeling numeric density via weight and color, not monospace.

## Layout

Fixed-max-width content column (**1220px**) centered with **22px** horizontal page padding and **28px** top padding. Vertical rhythm: **44px** between major sections; **14–18px** inside cards and grids.

Structure (top → bottom, one job each):

1. Status banner (conditional)
2. Hero — brand eyebrow, H1, one supporting sentence, meta chips
3. Latest signals — responsive KPI card grid (`auto-fit`, min ~260px)
4. Accuracy Summary — 3-column podium, then scrollable table
5. Backtest Simulation — same podium + table pattern
6. Battle Heatmap — horizontal-scroll grid of engine × date cells

At ≤860px, podium collapses to a single column. Tables and heatmap scroll horizontally inside rounded shells — never shrink columns until illegible.

Spacing scale is roughly 4 / 8 / 14 / 18 / 28 / 44 — favor these over arbitrary gaps.

## Elevation & Depth

Depth is **soft and green-tinted**, not heavy Material-style layers.

- Default surface: white panel + 1px border (`#E2E8F0`) + light dual shadow (`0 1px 2px` slate + `0 10px 28px` green wash).
- Hover lift: translateY(-2px to -3px) + stronger shadow; used on KPI cards, podium tiles, and table wraps.
- First-place podium: gold-tinted border/wash and warmer shadow — the only special elevation cue beyond hover.
- Hierarchy otherwise comes from typography scale, green/rose semantics, and section spacing — not stacked z-index theater.

No glassmorphism, no glow rings, no multi-layer dark shadows.

## Shapes

Shape language is **rounded editorial**: large radii for containers, tighter radii for atoms.

- **xl (18px):** KPI cards, podium tiles, table shells, heatmap wrap.
- **lg (12px):** Status banners.
- **md (6px):** Pipeline tags.
- **sm (5px):** Heatmap cells.
- **full (99px):** Meta chips, threat/session pills, accuracy bars.

Corners stay consistent within a component family. Prefer continuous white surfaces with borders over nested inset cards.

## Components

### Status banner
Inline page alert above the hero. Amber wash for informational/fallback notices; rose wash for hard errors. Compact bold copy; rounded-lg; single border.

### Meta chips
Pill row under the hero subtitle. White surface, hairline border, soft shadow. Values in primary-deep; labels in on-surface-soft.

### KPI signal cards
Latest-signal atoms. White base with a 3px top gradient rail (neutral / green / rose by direction). Up/down variants tint the lower half with soft green or rose washes — decorative only; score text sits on white. Large Lora signal word; pipeline + threat pills; model name bold; catalyst as muted body.

### Podium
Left-to-right rank order (1st · 2nd · 3rd). Three cards; first place taller with gold wash and gold border. Medal emoji, Lora name, uppercase pipeline tag, Lora score colored by sign, muted accuracy line.

### Tables
White scroll shell with border hairline. Uppercase muted headers on surface-muted. Pipe rows are slate uppercase; subtotals wash green; grand total stronger green wash + thicker top border. Row hover uses a faint green tint. Positive/negative numbers use primary/tertiary at bold weight. Inline accuracy bars are green gradient capsules.

### Pipeline tags
Uppercase chips — Crash / LLM / PPX pastel pairs as listed in tokens. Unknown engines fall back to border-soft + secondary.

### Battle heatmap
27×27 cells, 5px radius. Each cell splits into pre-market (upper-left triangle) and intraday (lower-right). Colors: emerald = correct/up, rose = wrong/down, slate = flat, striped amber = pending, transparent = none. Vertical column labels in secondary-soft; date row labels with medals where ranked.

## Do's and Don'ts

- Do keep the page light (`#FAFAFA` canvas, white panels) — this is not a dark trading terminal.
- Do use Forest Signal Green as the only brand accent; reserve rose strictly for negative/wrong states.
- Do set section titles and big scores in Lora; keep tables and chrome in Source Sans 3.
- Do preserve one-job sections: hero → latest → accuracy → backtest → heatmap.
- Do load QQQ prices from `qqq-ohlc.json` only (no live Yahoo fetch in the browser).
- Do use primary-deep (or on-surface) for small green labels; reserve bright primary for large display scores and fills.
- Don't introduce purple-indigo marketing gradients, cream/terracotta heritage themes, or broadsheet dense column layouts.
- Don't nest cards inside cards or wrap the hero in a bordered panel.
- Don't put stats strips, schedules, or secondary marketing blocks in the first viewport — only brand, H1, one sentence, meta chips.
- Don't use glow effects, neon accents, or emoji outside established medals/pipeline cues.
- Don't flatten semantic color: a green wrong-call or rose win breaks the scoreboard grammar.
- Don't mix sharp and fully rounded corners on the same component family without reason.
- Do maintain WCAG AA contrast for body text on white/soft washes; prefer `#0F172A` on `#FFFFFF` / `#FAFAFA`.

