import streamlit as st
import subprocess

st.set_page_config(page_title="Local Chat - Ollama", page_icon="🤖")
st.title("💬 Chat with Gemma 2B - Locally via Ollama")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

prompt = st.chat_input("Ask something...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Thinking..."):
        # Call Ollama CLI and get output
        result = subprocess.run(
            ["ollama", "run", "gemma:2b"],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        reply = result.stdout.decode()

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
