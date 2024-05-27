import streamlit as st   

import os 
os.environ['GOOGLE_API_KEY'] = "API_KEY"

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.schema import (
AIMessage, HumanMessage, SystemMessage
)

st.header("Hey, Im your CHATGPT")

# Initialize session state for storing messages if not already present
if 'sessionMessages' not in st.session_state:
    st.session_state.sessionMessages = [
        SystemMessage(content="You are a roaster assistant")
    ]

# Function to load answer from the language model
def load_answer(question):
    st.session_state.sessionMessages.append(HumanMessage(content=question))
    assistant_answer = chat(st.session_state.sessionMessages)
    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))
    return assistant_answer.content

# Function to get user input
def get_text():
    input_text = st.text_input('You: ', key='input')
    return input_text

# Initialize the chat model
chat = ChatGoogleGenerativeAI(model='gemini-pro')

# Get user input
user_input = get_text()
submit = st.button('Generate')

# If generate button is clicked, load the answer
if submit and user_input:
    result = load_answer(user_input)
    st.header('Result')
    st.write(result)