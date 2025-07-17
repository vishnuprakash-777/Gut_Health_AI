# streamlit_app.py

import streamlit as st
from rag_gut_health import get_rag_chain

# Configure the page
st.set_page_config(
    page_title="Gut Health Coach",
    page_icon="🦠",
    layout="centered"
)

st.title("🦠 Your Personal Gut Health Coach")

# Intro (display once)
if "intro_displayed" not in st.session_state:
    st.markdown(
        """
        Hi there! I'm your gut health coach 🤗  
        Ask me anything about digestion, bloating, probiotics, SIBO, food sensitivities, and more.
        
        Type your question below to begin the conversation. 🌱
        """
    )
    st.session_state.intro_displayed = True

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box at the bottom
with st.container():
    user_input = st.chat_input("Ask your gut health question...")

# Process user input
if user_input:
    # Display user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get response
    with st.spinner("Thinking..."):
        chain = get_rag_chain()
        response = chain.run(user_input)

    # Display assistant message
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# Display conversation
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(msg["content"])
