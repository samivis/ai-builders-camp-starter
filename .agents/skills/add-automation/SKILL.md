# Add Automation

Add one working automation to the student's app — a scheduled job, a bot command, or a recurring task.

## When to use

When the student is on Day 6, or says "use the add-automation skill" / "make my app do something automatically" / "add a bot."

## Replit rules
- For AI calls: use `ask_ai()` from `ai_helper.py`. Do NOT create a new OpenAI client or ask the student for an API key — Replit Managed AI is already wired up.
- For packages: add them to `requirements.txt` (Replit installs automatically). Do not instruct the student to run `pip install` in a terminal.
- For external services (Discord, Google Sheets, Gmail, Notion, etc.): use Replit **Connectors** (one-click OAuth in the Tools panel). Never ask the student for raw API keys.
- For scheduled/recurring work: use a Replit **Scheduled Deployment**, not a cron file.
- Do NOT explain the agent loop, tool-calling, or how automation works under the hood. The concept is "your app can do things automatically" — the student describes what they want; you build it.

## Workflow

### Step 1 — Pick one automation
Ask the student what they want to automate. Steer them to one of three shapes:
- **Scheduled job** — runs on a timer (e.g., "post a reminder every day at 4pm")
- **Bot** — responds to an event or command (e.g., a Discord command)
- **Recurring task** — checks something regularly and acts on it

### Step 2 — Connect any external service
If the automation touches Discord, Google Sheets, Gmail, etc., set up the matching Replit Connector (one-click OAuth in the Tools panel). Start this early — OAuth can take a few minutes. Never ask for raw API keys.

### Step 3 — Build it
Build the automation in the student's project. Keep it small and focused on one real thing.

### Step 4 — Schedule it (if it runs on a timer)
For a scheduled job, set it up as a Replit **Scheduled Deployment** so it runs even when the browser is closed. Mention that scheduled deployments use deployment credits.

### Step 5 — Test it
Make the automation fire at least once so the student sees it work. If a service connection gets messy, fall back to a manual Run-button trigger — that still proves the concept.

### Done when
- [ ] One automation is built (scheduled job, bot command, or recurring task)
- [ ] Any external service is connected via a Replit Connector
- [ ] The automation has fired at least once and the student saw it work
