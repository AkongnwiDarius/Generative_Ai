# get the model in and makes sure it works 
from itertools import chain

from .models import create_model
from config import QWEN
model = create_model(QWEN)
# we are going to be using something called: chatprompt template to create a prompt template
from langchain_core.prompts import ChatPromptTemplate

# a good example of prompt template 
# describe this (football players) in one sentence 
# given this (data) about this school, answer related questions ask by the user 



prompt_template = ChatPromptTemplate.from_messages(
    [
        #system message : a message given to the model in order for it to determine how to respond to users 
        #human message : a message given to the model by the user of the app
        ('system', 'please in one sentence describe this {football_player} and give a brief history of his career and also provide a list of his achievements in football'),
        ('human', '{question}' ),
    ]
)

football_player = input('enter the name of the football player:')
question = input('Enter the question you want to ask bout the football player:')

chain = prompt_template | model 
result = chain.invoke({
    'football_player':football_player,
    'question':question
})

print(result.content)