# from itertools import chain
# from .models import create_model
# from config import QWEN
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# model = create_model(QWEN)
# parser = StrOutputParser()


# # prompt_template -> model -> convert_to_string

# prompt = ChatPromptTemplate.from_messages([
#     ('system', 'you are a concise teaching assistant, answer in {max_sentence} sentences'),
#     ('human', '{question}')
# ])

# chain = prompt | model | parser
# result = chain.invoke({
#     'max_sentence':5,
#     'question': 'what is the difference between CNN and ANN'
# })

# print(result)

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


chat_prompt = ChatPromptTemplate([
    ('system','you are a helpful Ai. adopt the following persona and tone throughout the conversation: {persona}'),
    (MessagesPlaceholder('history')),
    ('human','{input}')
])
