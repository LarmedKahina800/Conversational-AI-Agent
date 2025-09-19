# 🎓 AI Conversational Agent (Student Project)

This is a chatbot project I built as part of my learning journey.  
It uses **Rasa** for natural language understanding and dialogue management, and integrates with **Ollama** (running LLaMA locally) to answer general knowledge questions.

---

##  Features

The chatbot can:
- Greet users and respond to small talk (hello, goodbye, mood).
- Handle predefined conversation flows (happy/sad paths).
- Answer open-ended questions by calling **Ollama** (e.g. *“What is quantum physics?”*, *“Translate hello to French”*).
- Work inside a simple web interface with a floating chat widget.

---

##  Tech Stack

- **Python** 3.8.10  
- **Rasa** 3.6.21
- **Rasa SDK** 3.6.2 (for custom actions)  
- **Ollama** 0.11.11 (local LLM engine)  
- **HTML/CSS/JavaScript** (frontend chat widget)  

---

##  Project Structure

```

ai-conversational-agent/
│── actions/actions.py          # My custom action (calls Ollama with user question)
│── domain.yml          # Intents, responses, slots
│── data/nlu.yml        # Example sentences for training
│── data/rules.yml      # Rules for simple cases
│── data/stories.yml    # Stories (sample conversations)
│── config.yml          # Pipeline + policies
│── credentials.yml     # Channels (REST, SocketIO)
│── endpoints.yml       # Action server config
│── requirements.txt    # Python packages I used
│── Web/index.html          # My web chat widget

````

---

##  How to Run

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/ai-conversational-agent.git
   cd ai-conversational-agent
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv chatbot_env
   ./chatbot_env/Scripts/activate   

   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model**

   ```bash
   rasa train
   ```

5. **Start Rasa server**

   ```bash
   rasa run --enable-api --cors "*"
   ```

6. **Start Action server**

   ```bash
   rasa run actions
   ```

7. **Open the chatbot UI**
   Just double-click **index.html** and start chatting 🎉

---

##  Example Conversations

## Chatbot Interface

Here is a screenshot of the chatbot in action:

![Chatbot Screenshot](Images\Screenshot1.png)


---

##  What I Learned

* Training intents and entities in Rasa.
* Writing custom actions in Python to connect with external tools (Ollama).
* Managing conversation history with slots.
* Creating a web chat interface with HTML, CSS, and JavaScript.



