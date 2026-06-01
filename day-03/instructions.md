# Day 3 — Design Spec

  **Duration:** 60 min design sprint + 60 min optional office hours · **Theme:** References beat adjectives. Give the AI taste — on paper — before it builds.

  ---

  ## Today's goal

  Gather design references, then turn them into a **design spec** (`design-spec.md`): your palette, typography, tone, and component styles. You will **not** build the app today — that's Day 4. Today you leave with two specs sitting side by side in your repo: `spec.md` (what it does) and `design-spec.md` (how it looks).

  ---

  ## The one idea you need

  **AI slop** is what happens when you let an AI design your app with zero direction: generic blue gradients, rounded cards, "Welcome to Your Dashboard" headers. It looks finished but it says nothing about you or your users.

  The fix: **give the AI specific design references instead of letting it guess.** A folder of screenshots, palettes, and fonts you like is worth more than 100 words of description. Those references become your design spec.

  ---

  ## The design spec workflow

  1. **Gather inspo** — you started this in Day 2 homework
  2. **Feed it to Replit Agent** — use the pre-written prompt
  3. **Agent writes your design spec** — palette, fonts, tone, visual direction, component styles

  That's where you stop today. No building. On Day 4 you hand your **tech spec + design spec** to an agent and it builds v1.

  ---

  ## Step 1 — Finish your design references (15 min)

  Check your `day-03/design/references/` folder. You should have 5–10 items from homework. If not, gather them now:

  **Color palette** — go to [Coolors.co](https://coolors.co). Hit spacebar to generate palettes. Click a color to lock it. When you find one you like, screenshot it and save it to your references folder. Give yourself **5 minutes max** — the rabbit hole is real.

  **Fonts** — go to [Google Fonts](https://fonts.google.com). Pick one font for headings and one for body text. Screenshot your picks. Good starter pairs: DM Sans + Playfair Display, Space Mono + Inter, Fraunces + DM Sans.

  **Design explorations** — go to [Variant](https://variant.com). Type what you're building, scroll through the generated designs, screenshot the ones that match the vibe you want.

  **Real app screenshots** — open 2–3 apps you actually use and love the design of. Screenshot them. Write one sentence about what you like: "Spotify: dark bg, bright green accents, clean cards."

  **Pinterest** (optional) — search "[your app type] UI design" and save a few pins.

  Post in Discord: *"My design vibe is ___"* with one reference image.

  ---

  ## Step 2 — Generate your design spec (15 min)

  Make sure all your references are in `day-03/design/references/`. Then open `day-03/design/AGENT-PROMPT.md` — it has a pre-written prompt you can paste directly into Replit Agent.

  The prompt tells Agent to:
  - Look at everything in your references folder
  - Create a `design-spec.md` with your color palette, fonts, tone, visual direction, and component styles
  - Reference your specific images to explain why it chose each element

  Prefer to draft it yourself? Use `day-03/design-spec-template.md` and fill it in by hand.

  Review what Agent creates. Does it match your vibe? If not, tell it: *"The palette is too bright — I want something more muted like the Spotify screenshot"* or *"Change the heading font to [font name]."*

  > ✅ Green light: you have a `design-spec.md` where every choice traces back to a reference, and you'd be proud to explain why it looks like this.

  ---

  ## Step 3 — Pair your two specs (10 min)

  Your app will be built from **two** documents. Make sure they live together in your project root:

  - `spec.md` — what it does (from Day 2)
  - `design-spec.md` — how it looks (today)

  Siblings. Best friends. Do not lose them — on Day 4 you hand both to the agent and that's how your v1 gets built.

  ---

  ## Step 4 — Push to GitHub

  This is the day you push to GitHub if you haven't yet.

  In the Replit Git panel:
  - Commit message: `"Day 3: design spec"`
  - Click **Push**

  > ✅ Ship proof: post your design vibe (one line) + a reference screenshot in `#lesson-3`.

  ---

  ## Make it yours (optional)

  Sharpen your design spec. Pick one:
  - Add **component states** — what a button looks like on hover, disabled
  - Write **3 real microcopy lines** in your app's voice (a button, an empty state, an error)
  - Name your palette colors by **job**, not hex ("action green," not "#3DDC84")
  - Add a **"don't do this"** list of slop the agent should avoid

  ---

  ## Optional office hours (60 min)

  Stay if you want:
  - **Peer review pairs:** swap design specs. Give 3 observations: "this looks intentional," "this is a slop risk," "I'd change this."
  - **Reference hunting:** fill gaps in your references folder
  - **Tone polish:** tighten your microcopy and "don't do this" list

  ---

  ## Checkpoint

  Before you leave today:
  - [ ] Design references gathered (5–10 items)
  - [ ] `design-spec.md` created from references
  - [ ] Every design choice traces back to a reference
  - [ ] `spec.md` AND `design-spec.md` both in your project root
  - [ ] Pushed to GitHub

  ---

  ## Homework

  Lock your **two specs** before Day 4 — that's when an AI agent builds your v1 from them:

  - Re-read your **design spec** — does every choice trace back to a reference?
  - Confirm `spec.md` **and** `design-spec.md` are both in your repo and pushed

  The better your specs, the better your v1. Garbage in, garbage out — great specs in, great app out.

  ---

  ## You now know

  - What AI slop is and exactly why it happens
  - How to gather design references that give an AI agent real taste
  - How to turn references into a **design spec** using `AGENT-PROMPT.md`
  - That giving the AI specific references beats letting it guess every time
  - Why you write the design spec **before** anything gets built
  