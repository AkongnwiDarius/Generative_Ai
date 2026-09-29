from html import parser
from itertools import chain
from .models import create_model
from config import QWEN
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#importing our model and our parser
model = create_model(QWEN)
parser = StrOutputParser()

#the message and input
prompt = ChatPromptTemplate.from_messages([
    ('system', 'please a give a one-paragraphed explanation for {topic} and should target audience of {audience}'),
    ('human', '{topic}')
])

topic = input('Enter the topic you want to learn about:')
audience = input('Enter the audience level you want :')

chain = prompt | model | parser
result = chain.invoke({
    'topic': topic,
    'audience': audience
})
print(result)

