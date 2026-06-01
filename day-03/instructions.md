# Day 3 — Design + Build

**Duration:** 60 min build + 60 min optional office hours · **Theme:** AI can build you anything. Make sure it builds something that looks like YOU.

---

## Today's goal

Create a design doc from your references. Then give Replit Agent both your tech spec (from Day 2) and your design doc — and have it build v1 of your app with intentional design from the start.

---

## The one idea you need

**AI slop** is what happens when you let an AI build your app's design with zero direction: generic blue gradients, rounded cards, "Welcome to Your Dashboard" headers. It looks finished but it says nothing about you or your users.

The fix: **give the AI specific design references instead of letting it guess.** A folder of screenshots, palettes, and fonts you like is worth more than 100 words of description.

---

## The design reference workflow

1. **Gather inspo** — you started this in Day 2 homework
2. **Feed it to Replit Agent** — use the pre-written prompt
3. **Agent creates your design doc** — palette, fonts, tone, visual direction
4. **Agent builds v1** — using your tech spec AND your design doc together

---

## Step 1 — Finish your design references (15 min)

Check your `day-03/design/references/` folder. You should have 5–10 items from homework. If not, gather them now:

**Color palette** — go to [Coolors.co](https://coolors.co). Hit spacebar to generate palettes. Click a color to lock it. When you find one you like, screenshot it and save to your references folder. Give yourself **5 minutes max** — the rabbit hole is real.

**Fonts** — go to [Google Fonts](https://fonts.google.com). Pick one font for headings and one for body text. Screenshot your picks. Good starter pairs: DM Sans + Playfair Display, Space Mono + Inter, Fraunces + DM Sans.

**Design explorations** — go to [Variant](https://variant.com). Type what you're building, scroll through the generated designs, screenshot the ones that match the vibe you want.

**Real app screenshots** — open 2–3 apps you actually use and love the design of. Screenshot them. Write one sentence about what you like: "Spotify: dark bg, bright green accents, clean cards."

**Pinterest** (optional) — search "[your app type] UI design" and save a few pins.

Post in Discord: *"My design vibe is ___"* with one reference image.

---

## Step 2 — Create your design doc (10 min)

Make sure all your references are in `day-03/design/references/`. Then open `day-03/design/AGENT-PROMPT.md` — it has a pre-written prompt you can paste directly into Replit Agent.

The prompt tells Agent to:
- Look at everything in your references folder
- Create a `design-doc.md` with your color palette, fonts, tone, and visual direction
- Reference your specific images to explain why it chose each element

Review what Agent creates. Does it match your vibe? If not, tell it: *"The palette is too bright — I want something more muted like the Spotify screenshot"* or *"Change the heading font to [font name]."*

Save the final `design-doc.md` in your project root, next to your `spec.md`.

> ✅ Green light: you have a design doc that matches your references and you'd be proud to show someone.

---

## Step 3 — Build v1 with design (20 min)

Now the magic. Tell Replit Agent:

> "I have two reference docs for my project:
> 1. My tech spec: [paste path to spec.md or paste contents]
> 2. My design doc: [paste path to design-doc.md or paste contents]
>
> Build the first version of my app following both documents. The app should work (based on the spec) and look intentional (based on the design doc). Start with the main screen and one core feature."

Let Agent build. Click **Run**. You should see an app that:
- Actually does something (the core feature from your spec)
- Looks like YOUR design choices, not generic AI defaults

If something looks off, iterate: *"The buttons don't match my design doc — they should be [color] with [style]."*

---

## Step 4 — Push to GitHub

This is the day you push to GitHub if you haven't yet.

In the Replit Git panel:
- Commit message: `"Day 3: v1 with design — spec + design doc + working app"`
- Click **Push**

> ✅ Ship proof: screenshot of your running app + one sentence about your design choices in `#day-3-ships`.

---

## Optional office hours (60 min)

Stay if you want:
- **Peer review pairs:** swap with another student. Give 3 observations: "this looks intentional," "this looks like slop," "I'd change this."
- **Design iteration:** refine your design doc and have Agent apply changes
- **Feature polish:** iterate on your core feature

---

## Checkpoint

Before you leave today:
- [ ] Design references gathered (5–10 items)
- [ ] Design doc created from references
- [ ] v1 built with both spec and design doc
- [ ] App runs and looks intentional
- [ ] Pushed to GitHub

---

## Homework

Use your app **3 times** before Day 4. Write down:
- One thing that's **annoying about the output** (the AI response, the feature behavior)
- One thing that **looks off about the design** (a color, a font, spacing, a label)

Come to Day 4 ready to say both. We're adding intelligence next — chaining AI steps to make your tool feel like it's actually thinking.

---

## You now know

- What AI slop is and exactly why it happens
- How to gather design references that give an AI agent real taste
- How to create a design doc from references using Replit Agent
- That giving the AI specific references beats letting it guess every time
- How to have Replit Agent build from both a tech spec and a design doc
