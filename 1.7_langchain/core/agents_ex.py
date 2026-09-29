from langchain.agents import create_agent
from streamlit import user
from .models import create_model
from utils.tool_ex import module_deadline_lookup, student_count_lookup, prerequisite, session_module_lookup

model = create_model()
agent = create_agent(
    model = model,
    tools = [module_deadline_lookup, student_count_lookup, prerequisite, session_module_lookup],
    system_prompt='You are an operations assistant for a University. Use tools to answer factual questions accurately'
)

result = agent.invoke({'messages': [{'role':'user', 'content':'can a student who has not finished Computer Architechture start Statistics, and how many students are already in Statistics'}]})
print(result['messages'][-1].content)


