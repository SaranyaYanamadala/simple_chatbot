import streamlit as st
import google.generativeai as genai

API_key = "AIzaSyA1G168bJfFFdzBKv8Z4vmyWLP9mAtOZIg"
genai.configure(api_key = API_key)
model = genai.GenerativeModel("gemini-1.5-flash")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("🤖 Chatbot - Your AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if promt := st.chat_input("Say something....") :
  ## Add user message to the chat history
  st.session_state.messages.append({"role" : "user", "content" : prompt})
  with st.chat_message("user") :
    st.markdown(prompt)

  response = st.session_state.chat.send_message(prompt)

  st.session_state.messages.append({"role" : "assistant", "content" : response.text})
  with st.chat_message("assistant") :
    st.markdown(response.text)
