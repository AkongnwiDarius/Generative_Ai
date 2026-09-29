import streamlit as st 
from langchain_core.messages import HumanMessage, AIMessage
from core.chain1 import get_chat_chain

st.set_page_config(page_title='Football Chat Bot', page_icon='🤖⚽')
st.header('Football Chat Bot🤖⚽')
with st.sidebar:
    st.title("Persona")
    persona = st.selectbox(
        "Choose a Persona:",
        ["Encouraging tactician", "football medical doctor", "football player"]
    )

#run the streamlit by running app.py in the langchain folder
chain = get_chat_chain()

if 'history' not in st.session_state:
    st.session_state.history = []

    
    # (AIMessage('message'), HumanMessage('message'))

for msg in st.session_state.history:
    role='user' if isinstance(msg, HumanMessage) else 'assistant'
    with st.chat_message(role):
        st.markdown(msg.content)

#what if there is an input 
user_input = st.chat_input('Ask your question...')

if user_input:
    st.session_state.history.append(HumanMessage(content=user_input))
    with st.chat_message('user'):
        st.markdown(user_input)

    with st.chat_message('assistant'):
        with st.spinner('Thinking...'):
            full_reply = st.write_stream(
                chain.stream({'input': user_input, 'history': st.session_state.history[:-1],'persona': persona})
        )
            st.session_state.history.append(AIMessage(content=full_reply))

