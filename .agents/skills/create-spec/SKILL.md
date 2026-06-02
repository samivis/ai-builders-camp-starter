# Create Spec

Guide the student through writing a tech spec for their project, then scaffold the project structure from it — architecture only, no feature code yet.

## When to use

When the student is on Day 2, picks a project idea, or says "use the create-spec skill" / "help me write my spec" / "set up my project."

## Replit rules
- For AI calls: use `ask_ai()` from `ai_helper.py`. Do NOT create a new OpenAI client or ask the student for an API key — Replit Managed AI is already wired up.
- For packages: add them to `requirements.txt` (Replit installs automatically). Do not instruct the student to run `pip install` in a terminal.
- For external services (Discord, Google Sheets, Gmail, Notion, etc.): use Replit **Connectors** (one-click OAuth in the Tools panel). Never ask the student for raw API keys.
- Keep the app simple: main logic in `main.py`, pages in `templates/`, styles in `static/`. Don't add new entry-point files or a build step.

## Workflow

### Step 1 — Pick one idea
Ask the student which of their 3 project ideas (from the Day 1 worksheets) they want to build. If they're unsure, ask: "What's one thing you do every week that's annoying and repetitive?" Pick ONE. Do not let them build all three.

### Step 2 — Write the spec with them
Copy `day-02/spec-template.md` to the project root as `spec.md`. Fill it in by asking the student each question — do not write it for them silently:
- One-sentence summary: "[Name] helps [who] do [what] by [how]."
- The problem: who has it, why it matters. Push back if the answer is vague ("helps people do things better" is not allowed — get specific, like "10th graders studying for AP History").
- How it works: input → what the AI does → output.
- APIs and tools needed: AI is already handled. Note any extras (Discord, email, calendar).
- What the user sees (frontend) and what happens behind the scenes (backend).

### Step 3 — Set up any extra tools
Most projects only need AI, which is already wired through `ai_helper.py`. If the spec calls for an external service, set up the matching Replit Connector. Do not ask for API keys.

### Step 4 — Scaffold from the spec
Create the project skeleton: the files, routes, templates, and `requirements.txt` entries the spec implies. Build the structure ONLY — no feature code. Think "the frame of a house before the walls." Then run it and confirm it loads.

### Done when
- [ ] `spec.md` exists in the project root and is specific (no vague problem statements)
- [ ] Any extra tools the spec needs are connected via Replit Connectors
- [ ] The scaffolded project runs (green screen) with structure in place but no feature code yet
