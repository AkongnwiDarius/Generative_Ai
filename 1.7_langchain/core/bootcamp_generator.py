from html import parser
from itertools import chain
from .models import create_model
from config import QWEN
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#creating our model and our parser
model = create_model()
parser = StrOutputParser()

#the prompt and input 
prompt = ChatPromptTemplate.from_messages([
    ('system','write an announcement for {audience} with {tones} and details {announcement_details}'),
    ('human', '{announcement_details}')
])

# audience = input('Enter the audience: ')
# tones = ['formal', 'friendly', 'urgent']
# announcement_details = input('Enter the announcement details: ')

chain = prompt | model | parser
result = chain.invoke({
    'audience': 'SEED AI Bootcamp students',
     'tones': 'Formal',
     'announcement_details':'Bootcamp starts this friday'
})

print(result)