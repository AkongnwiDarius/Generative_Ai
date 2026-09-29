from langchain.agents import create_agent
from .models import create_model
from utils.tools import get_module_deadline, count_students_in_module
model = create_model()

agent=create_agent(
    model = model,
    tools = [get_module_deadline, count_students_in_module],
    system_prompt='You are an operations assistant for a coding bootcamp. Use tools to answer factual questions accurately'
)

result = agent.invoke({'messages': [{'role': 'user', 'content':'when is the CNN module due'}]})
print(result['messages'][-1].content)


#streamling the agent meaning giving the output as it is being generated 
for step in agent.stream({'messages': [{'role':'user','content':'how many students are in CNN'}]}):
    print(step)


