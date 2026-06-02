# Ethics Review

Review the student's own app for real ethics issues and write up findings with concrete, doable fixes.

## When to use

When the student is on Day 7, or says "use the ethics-review skill" / "check my app for ethics issues."

## Replit rules
- For AI calls: use `ask_ai()` from `ai_helper.py`. Do NOT create a new OpenAI client or ask the student for an API key — Replit Managed AI is already wired up.
- Keep the app simple: main logic in `main.py`, pages in `templates/`, styles in `static/`. Don't add new entry-point files or a build step.

## Workflow

### Step 1 — Read the app
Read the student's app code (`main.py`, `templates/`, and any helpers). Understand what data the user gives it and where that data goes.

### Step 2 — Evaluate five areas
Assess the app honestly across these five areas. Make it specific to THIS app, not generic:
- **Privacy** — what user data is sent to the AI, and does the user know?
- **Bias** — could the app treat different users differently or unfairly?
- **Security** — could someone trick the AI (prompt injection) or misuse the app?
- **Content safety** — could the AI output something harmful?
- **Transparency** — does the user know they're talking to AI?

### Step 3 — Write the review
Create `ethics-review.md` in the project root. For each of the five areas: a one-line finding for this app, and at least one concrete recommendation the student could actually do.

### Step 4 — Discuss and apply quick fixes
Walk the student through the findings. Ask "what surprised you?" If they want a quick fix (e.g., add an "AI-generated" label for transparency), apply it.

### Done when
- [ ] `ethics-review.md` exists in the project root
- [ ] All five areas (privacy, bias, security, content safety, transparency) are covered specifically for this app
- [ ] At least one concrete, doable recommendation is included
