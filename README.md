# AI Builders Camp — Starter Template

Welcome to camp. This is your starting point. In two weeks, you'll turn it into a real, deployed AI app that lives at your own link — something you can put on a résumé or a college app.

**Instructor:** Samidha Visai · **Ages:** 13–17 · **Format:** 8 sessions over 2 weeks

---

## Before Camp — do this at home (5 steps, ~15 minutes)

These are just **accounts and verification** — no forking, no importing, no coding. On Day 1, the instructor walks everyone through the project setup together live.

---

### Step 1 — Create your Replit account & upgrade to Core (3 min)

AI calls cost credits, and Replit Core gives you the credits you need.

1. Go to [replit.com](https://replit.com) and sign up
2. Replit often offers **Core when you sign up** — if you see that prompt, just upgrade right there
3. Otherwise, click your **profile photo** → **Upgrade to Core**
4. Follow the steps — you'll need a parent's help if you're under 18 (it's the only paid step, ~$20/month, cancel anytime)

> **Already on Core?** Skip to Step 2.

---

### Step 2 — Turn on AI in a warm-up Repl (3 min, one-time)

Replit requires a **one-time phone verification** before it turns on managed AI. We do it now (with a parent nearby) so Day 1 is smooth. This only happens **once per account** — after this, AI works in every project.

1. In Replit, click **+ Create Repl** → **Blank Repl** → name it anything (e.g. `warm-up`) → **Create**
2. Click the **Agent** button (top right, looks like a sparkle or chat icon)
3. Type exactly this:
   > `Please set up Replit AI so my app can make AI calls.`
4. The Agent will show you an **OpenAI integration** to approve — click **Approve** (not Dismiss!)
5. ⚠️ **Replit will ask you to verify your phone number** — this is the one-time account check. A parent's phone is fine; Replit only texts once.
6. Wait for Agent to finish — it will say the app is ready
7. You can delete the warm-up Repl — its job is done

> If you accidentally click **Dismiss** on the integration popup, just type the same message again and approve it the second time.

---

### Step 3 — Create a GitHub account (2 min)

You need a free GitHub account to save your code and build your portfolio.

1. Go to [github.com/signup](https://github.com/signup)
2. Sign up with your email (13+ required)
3. Pick a username you'd put on a college application
4. Verify the email

> **Already have a GitHub account?** Just sign in and you're done.

---

### Step 4 — Join Discord and check Zoom (2 min)

1. Join the camp Discord at [discord.gg/DK3CCuSge](https://discord.gg/DK3CCuSge) — create an account if you don't have one
2. Go to [zoom.us/test](https://zoom.us/test) on your camp laptop and confirm audio + camera work

---

## Day 1 — in class, live together

The instructor shares their screen and walks through these steps. Campers follow along. If anyone gets stuck, they raise their hand and the instructor helps right there.

---

### Step 1 — Fork this repo to your own GitHub (2 min)

1. Make sure you're signed in to **GitHub** at [github.com](https://github.com)
2. Open this repo: `github.com/samivis/ai-builders-camp-starter`
3. Click **Fork** (top right)
4. In the **Repository name** box, name it after yourself so the instructor can tell projects apart — for example `maya-ai-builders-camp` or `jordan-ai-camp`
5. Click **Create fork**
6. You now have your own copy at `github.com/YOUR-USERNAME/maya-ai-builders-camp`

---

### Step 2 — Import your fork into Replit (2 min)

1. In Replit, click **+ Create Repl** → **Import from GitHub**
2. Paste **your fork's** URL: `https://github.com/YOUR-USERNAME/maya-ai-builders-camp`
3. Click **Import from GitHub** — Replit will set everything up

> ✅ Your Replit is now linked to **your own** GitHub repo. When you push, it goes to your repo — not the original template.

---

### Step 3 — Turn on AI in the starter (1 min)

The phone verification was already done at home (Step 2 above). In class, just approve the integration card.

1. Click the **Agent** button (top right)
2. Type exactly this:
   > `Please set up Replit AI so my app can make AI calls.`
3. Click **Approve** on the **OpenAI integration** card (not Dismiss!)
4. Wait for Agent to finish

---

### Step 4 — Run your app and test AI (2 min)

1. Click the green **Run** button at the top
2. The **Explain Anything** app opens in the preview window (right side)
3. Type a topic like `black holes` and click **Explain it →**
4. You should get a real AI answer — not an error message

> ❌ **Still seeing "AI isn't connected yet"?** Ask the Agent again. The error message in the app tells you exactly what to paste if the keys didn't save the first time.

---

### Step 5 — Save your work to GitHub (2 min)

The easiest, most reliable way to back up your code is to let the **Agent** do it.

1. Open the **Agent** panel (top right)
2. Type exactly:
   > `Please push my code to GitHub.`
3. If a **Connect GitHub** card pops up, click **Connect GitHub** and authorize — this happens once, then the Agent remembers it
4. The Agent saves everything to your repo and tells you when it's done

> ✅ Go to `github.com/YOUR-USERNAME/maya-ai-builders-camp` — you should see your files there. That's your code, saved and backed up. From now on, just ask the Agent *"push my latest changes"* anytime.

---

### Step 6 — Invite your instructor (1 min)

**On Replit:**
- Click **Invite** (top right, next to **Publish**) → in the **email** box type `sami.v.95@gmail.com` → click **Invite**

**On GitHub:**
- Go to your repo → **Settings** → **Collaborators** → **Add people** → search `samivis`

---

### Step 7 — Introduce yourself in Discord (1 min)

Post in **#general**:

> Hey everyone! I'm [your name] and I'm set up for AI Builders Camp! My Replit is [username] and my GitHub is [github-username]. Ready to build! 🚀

---

## Day 1 — Make it yours (first customization)

Open `main.py` and change the `SYSTEM_PROMPT` line — one line change, totally different tool:

```python
SYSTEM_PROMPT = "You explain any topic like a hyped sports announcer calling the play-by-play."
```

Run it and try it out. That's yours now.

---

## How this template is organized

```
main.py              ← YOUR APP. The Run button runs this. You grow it all camp.
templates/index.html ← what your app looks like (the web page)
static/style.css     ← your app's colors and styling
ai_helper.py         ← your shortcut to AI. Just import ask_ai and use it.
replit.md            ← tells your Replit Agent about the project (reads automatically)
.agents/skills/      ← guided workflows your Agent knows how to follow

examples/            ← three finished mini-apps to read for ideas
```

You build ONE app across all of camp — it lives in `main.py` and gets better every day.

---

## Using AI in your code

Anywhere in your Python code, you can do this:

```python
from ai_helper import ask_ai

answer = ask_ai("Write a haiku about pizza")
print(answer)
```

Want to change the AI's personality? Pass a `system_prompt`:

```python
answer = ask_ai(
    "Tell me about the moon",
    system_prompt="You are a pirate who loves astronomy."
)
```

---

## The 8 days

| Day | You build |
|---|---|
| 1 | Your first AI tool + your code saved to GitHub |
| 2 | A tech spec + scaffolded project, ready to design |
| 3 | Design references — your app's visual identity starts here |
| 4 | A design spec + working v1, built from your specs |
| 5 | Midpoint demo + feature direction for week 2 |
| 6 | Automation — a scheduled job, bot, or recurring task |
| 7 | Ethics review + GTM plan + final polish |
| 8 | Demo Day 🎉 |

---

## Stuck? Three things to try

1. **Ask the Agent.** It can see your code. Describe what's wrong in plain English.
2. **Read the error message.** It usually says which file and line broke.
3. **Post in Discord** at [discord.gg/DK3CCuSge](https://discord.gg/DK3CCuSge). Someone's probably hit the same thing.

You've got this. Let's build.
