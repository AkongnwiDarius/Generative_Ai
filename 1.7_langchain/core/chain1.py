import streamlit as st 
# @st.cache_resources  # helps store api calls temporary 
from langchain_core.output_parsers import StrOutputParser
from .models import create_model
from .prompt import chat_prompt
from config import QWEN

parser = StrOutputParser()

@st.cache_resource
def get_chat_chain():
    model = create_model()
    return chat_prompt | model | parser