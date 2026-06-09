"""
reminder_bot.py — your first automation 🤖

Day 6 "try it": make something happen AUTOMATICALLY, without you clicking Run.

This little program posts a homework reminder into the shared #automations
channel on Discord — and @mentions YOU so you get pinged. Once it works,
you'll Publish it as a Scheduled Deployment so it fires before class every
time, on its own. THAT is automation: code that does a real thing in the
world while you're not even looking.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SET IT UP (about 5 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Your instructor will share a webhook URL for the #automations channel.
     • In Replit, open the Tools panel  →  Secrets
     • New secret →  key:  DISCORD_WEBHOOK_URL    value: (paste the URL)

2. Get your Discord user ID so the bot can @mention you:
     • In Discord: Settings  →  App Settings  →  Advanced  →  toggle Developer Mode ON
     • Back in the server, right-click your own name  →  "Copy User ID"
     • In Replit, add another Secret →  key:  DISCORD_USER_ID    value: (paste your ID)

3. Click Run. Check #automations — your reminder should appear and ping you! 🎉

4. Make it automatic:  Publish  →  Scheduled Deployment
     • Run command:  python3 day-06/reminder_bot.py
     • Schedule: before class (for example, weekdays at 10:30 AM)
   Now it pings the channel on its own, even with your browser closed.

Scheduling feels fiddly? No stress — just clicking Run still fires it, and that
still counts: you made code do a real thing automatically. That's the whole idea.
"""

import os
import json
import urllib.request

# The reminder you want to send. Change this to anything you like!
REMINDER = (
    "📚 Heads up — AI Builders Camp class starts soon! "
    "Bring your project and a question you're stuck on. See you there! 🚀"
)

# ─────────────────────────────────────────────────────────────────────────────
# BONUS: make the reminder fresh and fun EVERY time, using the AI you already know.
# Flip this to True and ask_ai() will write a new reminder on each run.
# ─────────────────────────────────────────────────────────────────────────────
USE_AI = False


def build_message():
    """Return the text to post — either your fixed reminder or an AI-written one."""
    if USE_AI:
        from ai_helper import ask_ai
        return ask_ai(
            "Write a short, upbeat one-line reminder that AI Builders Camp class "
            "starts soon. Include one emoji. Keep it under 25 words.",
            system_prompt="You are a hype friend sending fun class reminders to teenagers.",
        )
    return REMINDER


def send_to_discord(message):
    """Post a message to the shared #automations channel using the class webhook."""
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("No DISCORD_WEBHOOK_URL secret found yet.")
        print("Your instructor will share this URL — paste it into Tools → Secrets.")
        print("See the setup steps at the top of this file.")
        return

    # If the student set their Discord user ID, prepend an @mention so they get pinged.
    user_id = os.environ.get("DISCORD_USER_ID")
    if user_id:
        message = f"<@{user_id}> {message}"
    else:
        print("Tip: add a DISCORD_USER_ID secret so the bot @mentions you!")
        print("(Discord → Settings → Advanced → Developer Mode, then right-click your name → Copy User ID)")

    data = json.dumps({"content": message}).encode("utf-8")
    request = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json"},
    )
    urllib.request.urlopen(request)
    print("Sent to Discord! Go check #automations. ✅")


if __name__ == "__main__":
    send_to_discord(build_message())
