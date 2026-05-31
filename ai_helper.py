"""
ai_helper.py — your shortcut to AI.

You don't need an OpenAI account or an API key. Replit's Managed AI gives your
app access to powerful AI models, and the cost comes out of your Replit credits.

Every day of camp, you'll import the `ask_ai` function from this file:

    from ai_helper import ask_ai
    answer = ask_ai("Explain black holes")
    print(answer)

You almost never need to edit this file. Just use it.
"""

import os
from openai import OpenAI

# These two values are set up automatically by Replit when AI is connected.
# You never type a key. You never see a key. Replit handles it.
BASE_URL = os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL")
API_KEY = os.environ.get("AI_INTEGRATIONS_OPENAI_API_KEY")

# Which AI model to use.
#
# The OpenAI-compatible API requires a model name — you can't leave it blank.
# This default works well for camp, but students are encouraged to try others.
#
# To change it:
#   • Edit the string below (students can do this freely in their own Repl), OR
#   • Set a Replit Secret called REPLIT_AI_MODEL to override it without touching code
#     (handy for the instructor to swap the whole class to a newer model)
#
# The Replit Agent / coding assistant you talk to in the IDE picks its OWN model
# automatically — this setting only controls calls your *app* makes to the AI.
MODEL = os.environ.get("REPLIT_AI_MODEL", "gpt-4o-mini")


def ai_is_connected():
    """True if Replit AI is set up and ready to go."""
    return bool(BASE_URL) and bool(API_KEY)


def ask_ai(prompt, system_prompt="You are a helpful, friendly assistant."):
    """
    Send a prompt to the AI and get the response back as text.

    prompt        = the question or input from your user
    system_prompt = the AI's personality / instructions (this is where the magic is —
                    change it to change how your tool behaves!)
    """
    if not ai_is_connected():
        return (
            "AI isn't connected yet. Open the Agent panel (top right) and say:\n"
            "'Please set up Replit AI so my app can make AI calls.'\n"
            "Then run your app again."
        )

    client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        max_completion_tokens=8192,
    )

    return response.choices[0].message.content
