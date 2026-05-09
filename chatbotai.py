from dotenv import load_dotenv

from openai import OpenAI
import streamlit as st

load_dotenv()

client = OpenAI()
initial_message =[
     {"role": "system", "content": "Your are a trip planner in Kerala. You are an expert in Kerala Tourism, locations, food,events, etc. You are able to guid users to plan their vation to Kerala. You should respond professionally. Response shouldn't 200 words"},
        {
            "role": "assistant",
            "content": "hello, I am Rayees Ai bot trip Assistant, your expert trip planner. How can I help you?"
        }
]

def get_response_from_llm(messages):
    completion = client.chat.completions.create(
    model="whisper-1",
    messages= messages
    )
    return completion.choices[0].message.content

if "messages" not in st.session_state:
    st.session_state.messages = initial_message
st.title("Kerala Trip Assistant ")
for messages in st.session_state.messages:
    if messages['role'] != "system":
        with st.chat_message(messages["role"]):
            st.markdown(messages["content"])


user_message = st.chat_input("Ask your plans")
if user_message:
    new_message = {
        "role":"user",
        "content":user_message
    }
    st.session_state.messages.append(new_message)
    with st.chat_message(new_message["role"]):
        st.markdown(new_message['content'])
    response = get_response_from_llm(st.session_state.messages)
    if response:
        response_message = {
        "role":"assistant",
        "content":response
        }
        st.session_state.messages.append(response_message)
        with st.chat_message(response_message['role']):
            st.markdown(response_message["content"])
            
        
