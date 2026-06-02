# Design Spec

Turn the student's design references into a formal `design-spec.md` — the look-and-feel half of their project that pairs with `spec.md`.

## When to use

When the student is on Day 4, has gathered references in `day-03/design/references/`, or says "use the design-spec skill" / "make my design spec."

## Replit rules
- Keep the app simple: main logic in `main.py`, pages in `templates/`, styles in `static/`. Don't add new entry-point files or a build step.
- This skill produces a document only — it does NOT build the app. Building happens in the build-v1 skill on Day 4.

## Workflow

### Step 1 — Look at the references
Read every file in `day-03/design/references/` (screenshots, palettes, font picks, links). If the folder is empty or nearly empty, stop and ask the student to add references first — the references ARE the taste; without them the result is AI slop.

### Step 2 — Draft the spec from the template
Use `day-03/design-spec-template.md` as the structure. Create `design-spec.md` in the project root and fill in every section:
- **Vibe in 3 words**
- **Color palette** — 4–5 colors with hex codes; for each, name its role and which reference it came from
- **Typography** — a heading font and a body font from Google Fonts, with the CSS import link, tied to a reference
- **Tone & voice** — plus 3 real microcopy lines (button label, empty state, error message)
- **Visual direction** — 2–4 sentences referencing specific images ("Based on your Spotify screenshot, ...")
- **Component styles** — buttons, cards, inputs
- **Anti-slop list** — things to avoid (generic blue gradients, "Welcome to your dashboard" headers)

Every choice must trace back to a reference. No generic suggestions.

### Step 3 — Review and iterate
Show the student the draft. If something is off, take their feedback ("the palette is too bright — more muted like the [app] screenshot") and update the spec.

### Done when
- [ ] `design-spec.md` exists in the project root
- [ ] Every color, font, and style choice traces to a reference in `day-03/design/references/`
- [ ] The anti-slop list is filled in
- [ ] The student is happy with the vibe (no app built yet — that's build-v1)
