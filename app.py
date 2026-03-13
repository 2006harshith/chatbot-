import streamlit as st
from groq import Groq
from ai.intent_classifier import predict_intent
# AI client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Personality prompt
SYSTEM_PROMPT = """
You are a helpful conversational AI assistant.

Your behavior:
- Explain concepts simply and clearly.
- Break complex ideas into steps.
- Be concise but complete.
- Use examples when helpful.
- Maintain a friendly conversational tone.
- Use context from previous messages.
- Avoid unnecessary jargon.
- Ask clarifying questions when needed.
- Focus on helping the user learn, not just giving answers.
"""
st.title('Hash')
# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# Chat input
user_input = st.chat_input("Type a message...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Detect intent
    intent = predict_intent(user_input)

    if intent == "greeting":
        reply = "Hello! How can I help you today?"

    elif intent == "goodbye":
        reply = "Goodbye! Have a great day."

    elif intent == "gratitude":
        reply = "You're welcome!"

    else:
        # fallback to LLM
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *st.session_state.messages
            ]
        )

        reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)