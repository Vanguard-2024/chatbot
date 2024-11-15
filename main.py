
from langchain_groq import ChatGroq

import streamlit as st 
import os
from langchain.schema import HumanMessage
llm = ChatGroq(api_key="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", model="llama3-70b-8192")


st.title('Ask Real360')
if 'messages' not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])    

prompt = st.chat_input('Pass Your Prompt here')

if prompt:
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role':'user','content':prompt})
    response = llm.invoke([HumanMessage(content=prompt)], max_tokens=400, temperature=0.7)
    st.chat_message('assistant').markdown(prompt)
    st.session_state.messages.append({
        'role':'assistant','content':response.content
    })
    
    
    
    
    

    

    
    