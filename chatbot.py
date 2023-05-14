import streamlit as st
from rwkv_chat import RWKV_CHAT

chat = RWKV_CHAT()

st.title('RWKV Chatbot')

conversation = st.empty()
response = st.empty()

user_input = st.text_input('You:')
if user_input: 
    for response_line in chat.get_response(user_input):
        response.write(f'Bot: {response_line}\n\n')
    conversation.write(f'You: {user_input}\nBot: {response.text}\n\n') 
