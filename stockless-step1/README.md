# StockLess — Steps 1 and 2 redesign + workspace background

Targets **`HansYap/StockLess`** (the live app behind `stockless.pages.dev`), not the Figma Make
prototype. I checked first: the wording PDF's strings — *"What data can StockLess use?"*,
*"Drop your CSV file here"*, *"Finishing up"*, *"Use sample file"* — all live in
`frontend/src/screens/UploadScreen.tsx`, so that's where the changes go.

## What's in here

| File | What it is |
| --- | --- |
| `steps-1-2-redesign.patch` | all seven file changes, 632 lines, +192 / −102 |
| `WorkspaceDecor.tsx` | the new component on its own, if you'd rather copy it in by hand |
| `../StockLess-Step1-Upload.html` | a static preview of the result — double-click to open |

Apply it:

```sh
git checkout -b step1-upload-redesign
git apply step1-upload-redesign.patch
npm run dev
```

## The wording changes

Everything below comes from *Homepage and Step Suggestion UI Wording.pdf*.

| Where | Before | After |
| --- | --- | --- |
| Section heading | What data can StockLess use? | 🌱 **What do you need to get started?** |
| Intro | (listed every attribute up front) | Start with the three required attributes. Optional attributes unlock additional insights. |
| Lede | — | Required data is enough to get started. Optional data unlocks deeper insights. |
| Attribute 02 label | Product identifier | **Product identification** |
| Attribute 02 desc | — | Choose one of the accepted formats to keep products and pack sizes separate. |
| Accepted forms | (3 loosely-worded options) | 1. SKU, barcode or product code · 2. Product name + pack size |
| File limits | (split across two lines) | .CSV · Up to 10 MiB · 100,000 rows · Comma, semicolon or tab separated |
| Privacy headline | — | **Your data stays on your device.** |
| Privacy body | — | Your CSV is processed directly in this browser. Your sales rows and product identifiers are not uploaded to an AI or API service. |
| Final phase label | Finishing up | **You're one step closer to less waste.** |
| Final phase subline | (generic progress text) | Your data is ready. Let's see what your store actually needs. |

Plus one thing the PDF implies rather than spells out: a **value chain** under the drop zone —
Sales data → Demand insights → Smarter restocking → 🌱 Less waste. It answers *"why am I uploading
this?"* at the exact moment someone hesitates over the button.

The two backend strings moved too, because the UI reads them from there rather than hard-coding:
`field-registry.ts` (`coreDescription`, `PRIVACY_NOTICE.beforeUpload`) and `capabilities.ts`
(the product-identification label, description and accepted forms).

## The background

`WorkspaceDecor.tsx` brings the homepage artwork into the app — same waves, leaves and dot grids,
same colours sampled from your mockup (`#EDF7E9`, `#DCEFD8`, `#B8DFBE`, dots `#9CC9A0`).

Three deliberate differences from the homepage version, because this is a working screen rather
than a marketing page:

- **It's quieter.** Lower opacities, fewer leaves, no basket. You're meant to read the screen, not
  look at the background.
- **It's pinned to the viewport** (`position: fixed`), so it doesn't stretch and repeat as the
  upload progresses and the page grows.
- **The centre column is cleared.** A radial wash of `--page` sits over the middle at full opacity
  and fades out at the margins, so no artwork ever passes under text — the same rule as the
  homepage.

It's hidden below 900px. On a phone the content column already fills the screen, so the artwork
would only ever sit *behind* text, which is the thing you didn't want.

It mounts as the first child of `.frame` in `AppShell.tsx`, so every screen in the workspace gets
it — not just Step 1. One line in `styles.css` lifts every other child of `.frame` above it:

```css
.frame > *:not(.ws-decor){position:relative;z-index:1}
```

## Typography — the app now uses the homepage's scale

The workspace was set a notch below the marketing site: body copy at 13px, descriptions at 11px,
labels at 10px, against the homepage's 15 / 12 / 11. Side by side they read as two different
products, and on the Upload screen — which is nothing *but* wording — it just read as small.

`styles.css` now declares the homepage's type tokens and every size in the file is set from them:

```css
--text-page-title:36px; --text-lead:18px;  --text-section-head:20px;
--text-body:15px;       --text-secondary:13px; --text-description:12px;
--text-eyebrow:11px;    --text-label:10px;
```

| Was | Now | Where you'll notice it |
| --- | --- | --- |
| 13px, 14px | **15px** | attribute descriptions, drop-zone copy, privacy body, card subheads |
| 12px | **13px** | file limits, pills, step labels, session status |
| 11px | **12px** | the value chain, accepted-format chips, fine print |
| 10px | **11px** | uppercase micro-labels |
| 9px | **10px** | the smallest badges |

Headings didn't move — 20px section heads, 18px ledes and the 36px page title already matched the
homepage. Hard-coded pixel line-heights (`line-height:18.85px` and friends) became ratios, so they
follow the size instead of fighting it.

The same pass ran over `homepage.css`, lifting its small reading copy to the same scale: benefit and
step paragraphs, the food-waste statistics, comparison table, SDG caption, sources line and footer.
**The miniature app demo in the hero is deliberately untouched** — it's a scaled-down screenshot, and
enlarging its type would break both the illusion and its layout.

### One bug fixed along the way

`.sl-story` and `.sl-impact` are two-column grids whose children had no `min-width:0`, so the shop
photo overflowed the page by ~12px at 1440 and the text column blew past the viewport by 135px on a
phone. That's on the live site today, before any of these changes — the bigger statistics text just
made it more obvious. One line fixes it:

```css
.sl-story>*,.sl-impact>*{min-width:0}
```

All three widths (1440 / 1280 / 390) now scroll clean.

## Step 2 — Map columns

Checked against the live site first (`stockless.pages.dev/#workspace` with a file loaded), then
revised against *Homepage and Step Suggestion UI Wording* and Iteration 3's E1 stories.

### Wording

| Where | Before | After |
| --- | --- | --- |
| Eyebrow | Confirm what your columns mean | **Make sure StockLess understands your data** |
| Heading | We found likely matches. Check them before continuing. | **We found your data. Let's make sure it's right.** |
| Lede | Your original file is not changed. Mapping only tells StockLess how to interpret it… | Review the suggested column matches before continuing. Your original file won't be changed. |
| Banner | Sample data loaded. | Sample data loaded — **review the mappings before continuing.** |
| Bulk button | Looks well, next step | **Confirm all and continue →** |
| Identity heading | How should products be kept separate? | **How should StockLess identify each product?** |
| Identity lede | Pick one path and confirm it. This choice is recorded as evidence… | Choose the format that keeps different products and pack sizes separate. |
| Format 1 | One code column | ① One code column — *SKU, barcode or product code* |
| Format 2 | Product name together with pack size | ② Product name + pack size |
| Final CTA | Run readiness check → | **Check my data →** |

### Colour now means something

The PDF's point was that green was doing every job. It now carries one:

- **Sage** `#EDF3EE` / `#3F7A5D` / `#D8E6DA` — confirmed
- **Amber** — needs attention (the sample-data banner, unconfirmed matches)
- **Red** — error

Once every field is confirmed and nothing is blocking, a quiet line appears above the table:
*✓ Your data is ready to analyse.*

### The dark panel is gone

`This file unlocks` was a near-black teal block listing capabilities, with a
`LOCKED UNTIL ITERATION 3` group still in it — during iteration 3. Two things pointed the same way:
the PDF asked for a sage card, and **US1.5a** says the feature-unlock presentation is replaced.

It's now a sage card carrying guidance instead of an inventory: *🌱 How to check your data* with the
four numbered steps, then *Keep products separated* with the two identity formats, then the privacy
note.

**This removes a visible feature**, so it's worth a look before merging. The "what can my data
support" question doesn't disappear — it's US1.5a's subject and belongs on Step 3 (Check readiness),
where it can be answered properly rather than as a locked list. The immediate "what's missing"
answer is still on this screen, in the `Still needed:` line beside the button.

### Iteration 3 stories covered

- **US1.4** — confirm all matches together or edit individually. The bulk confirm already existed;
  it now says what it does.
- **US1.6** — the identity conflict alert already explains clashes between names, codes and pack
  sizes; the format choice above it is now numbered and in plain language.
- **US1.5a** — the unlock presentation is replaced, as above.

### One bug fixed

The `Suggested — please check` pill is `white-space: nowrap`, which is right everywhere else but
made it overflow the narrow status column in the mapping table. It wraps there now, and the column
is 23% rather than 20%.

## Naming: one vocabulary across all three surfaces

The same four steps had three different names depending on where you were standing. Worse, the live
homepage described a *different workflow* — "Prepare it with StockLess" merged mapping and readiness
into one step, and "Understand your demand" added a step the app doesn't have.

|  | Step 1 | Step 2 | Step 3 | Step 4 |
| --- | --- | --- | --- | --- |
| **Homepages** (both) | Upload your sales data | Map your columns | Check your data is ready | Plan your purchases |
| **App stepper** | Upload | Map columns | Check readiness | Plan purchases |

The app's labels are canonical, since they're what a user sees on every screen. Both homepages and
the prototype's placeholder screens now match, in all three languages.

**Watch this when you edit live copy.** `frontend/src/i18n/messages.ts` is keyed by the English
string, so changing a caption silently drops its Malay and Chinese back to English. New entries are
in for all seven changed strings.

## The stepper cultivates: 🌱 → 🌿 → 🪴 → 🌳

Steps not yet reached are desaturated; the current one is full colour and slightly larger. The
glyphs are `aria-hidden` and the dots still carry the number and the tick, so nothing depends on
seeing an emoji.

The metaphor is bonsai rather than bamboo, and the distinction matters: retailers aren't trying to
*grow* inventory, they're trying to shape it. A plant that only gets bigger quietly argues for more
stock, which is the opposite of what StockLess is for.

**One thing to verify on real devices.** 🪴 is a newer emoji than the other three and renders
inconsistently — fine on recent macOS, iOS and Android, but it can show as a blank box on older
Windows and some Android builds. If it boxes anywhere, 🍃 is the safe swap, or draw all four as
small SVGs and stop depending on system emoji fonts.

## Step 2 — the rest of it

- Field descriptions moved into `?` tooltips, so the mapping table scans instead of reading as
  prose. `aria-label` carries the same text.
- Every field description rewritten in plain language: "The current product-level stock snapshot;
  repeated values are not summed" became "How much you have on the shelf right now."
- Preview values de-duplicated and dates formatted — a stock-count column repeated one date five
  times, which said nothing five times. Now `12 Sep 2026`.
- The identity cards **are** the control now (a `radiogroup` with `aria-checked`), rather than a
  small button inside a large card that did nothing when clicked.
- "Suggested — please check" → "Please confirm"; "✓ Confirmed" → "✓ Selected" on the format choice,
  because selecting a format isn't the same as confirming a mapping.
- The unlock panel came back as a light teal box, inverted: one row per missing column with what it
  unlocks, and columns that unlock the same things merged. Seven repeating items became two rows.

## Two things to know before you merge

**This is the team repo, not your fork.** The patch applies cleanly to `HansYap/StockLess` as of
today, but it'll need a PR rather than a direct push.

**I couldn't run `npm run build`** — the sandbox blocks the npm registry, so dependencies won't
install. I syntax-checked all five changed source files with esbuild instead (all clean) and rendered both
the preview and the homepage from the repo's own stylesheets, checking for overflow at 1440, 1280
and 390px.
The one thing nobody has verified is a full type-check. Run it once locally before you open the PR.

## Still open from the I3 plan

- Are the I2 verdicts (*High risk / Needs review / Looks balanced / Cannot judge*) the same thing
  as the I3 groups (*Order Needed / Check Your Order / Looks Balanced / Need More Data*), or a
  layer above them? Step 4's wording depends on the answer.
- Screens 2–4 (column matching, data check, results) haven't been touched yet.
