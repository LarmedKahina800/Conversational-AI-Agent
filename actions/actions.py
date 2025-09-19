# Project: AI Conversational Agent
# File: actions.py
# In this file I implemented a custom Rasa action that talks to Ollama.
# I wanted my chatbot to be smart and answer general questions,
# so I used subprocess to call the Ollama LLM (llama3 model).


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import subprocess
import sys

# Ensure UTF-8 encoding (on Windows I had issues with special characters in output)

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


class ActionAskOllama(Action):
    def name(self) -> Text:
        # I give my action a name that I can call from domain.yml and rules.yml
        return "action_ask_ollama"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        # Get last user message
        user_message = tracker.latest_message.get("text", "")

        # I use a slot to store conversation history (to add context to answers)
        history = tracker.get_slot("conversation_history") or []

        # Keep last 3 turns only (to avoid huge prompts)
        context_text = ""
        for turn in history[-3:]:
            context_text += f"User: {turn['user']}\nBot: {turn['bot']}\n"

        # Append current user input
        prompt = context_text + f"User: {user_message}\nBot:"

        try:
            # Call Ollama (I used llama3 model). Timeout is big because it can take time.
            result = subprocess.run(
                ["ollama", "run", "llama3", prompt],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=9000,
            )
            
            # If Ollama returns text, I use it, else I fallback to stderr
            answer = result.stdout.strip() if result.stdout else result.stderr.strip()
            if not answer:
                answer = "Sorry, I didn't get any response from Ollama."

        except subprocess.TimeoutExpired:
            answer = "⚠️ Ollama took too long to respond. Please try again."
        except Exception as e:
            answer = f"Sorry, I couldn't get an answer. Error: {e}"

        #  Save history (I keep last 5 exchanges only)
        history.append({"user": user_message, "bot": answer})
        history = history[-5:]  # keep last 5

        # Send the answer to the user
        dispatcher.utter_message(text=answer)

        # Update slot with new history
        return [SlotSet("conversation_history", history)]






