# Add Automation

Add one working automation to the student's app — a scheduled job, a bot command, or a recurring task.

## When to use

When the student is on Day 6, or says "use the add-automation skill" / "make my app do something automatically" / "add a bot" / "set up the homework reminder."

## Quick guided path: Discord homework reminder (the default Day 6 exercise)

If the student just wants the fast, everyone-can-do-it automation, use the ready-made starter file `day-06/reminder_bot.py`. It posts a message to the shared `#automations` channel on Discord using a **webhook** the instructor pre-created — no bot token, no OAuth, no new packages. Everyone's bots post to the same channel. Walk them through it:
1. **Store the webhook URL** the instructor shared as a Secret named `DISCORD_WEBHOOK_URL` (Tools → Secrets). Never put the URL in code.
2. **Get their Discord user ID** so the bot @mentions them: Discord Settings → App Settings → Advanced → toggle Developer Mode ON, then right-click their own name → Copy User ID. Store it as a Secret named `DISCORD_USER_ID`.
3. **Run it** (`day-06/reminder_bot.py`) and confirm the message appears in `#automations` with an @mention that pings them.
4. **Schedule it** as a Replit Scheduled Deployment with run command `python3 day-06/reminder_bot.py`, set to fire before class. Mention scheduled deployments use deployment credits.
5. **Bonus:** flip `USE_AI = True` in the file so `ask_ai()` writes a fresh reminder each run — connecting the AI they already know to automation.
Rescue path: if scheduling is fiddly, just clicking Run fires it — that still proves the concept.

Students who'd rather automate their OWN app instead of the reminder exercise: use the general workflow below.

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
