from utils.tool_ex import student_count_lookup, prerequisite, module_deadline_lookup, session_module_lookup
from .models import create_model
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

tools = [module_deadline_lookup, student_count_lookup, prerequisite, session_module_lookup]

llm = create_model().bind_tools(tools)
# print(llm)

tools_by_name = {t.name: t for t in tools}
messages = [HumanMessage('how many students are in the statistics course and when is the deadline for submission')]

ai_response = llm.invoke(messages) #what happens in this first invoke

messages.append(ai_response)


for tool in ai_response.tool_calls:
    tool_fn = tools_by_name[tool['name']]
    result = tool_fn.invoke(tool['args'])
    # print(f'tool result is: {result}')
    messages.append(ToolMessage(content=result, tool_call_id=tool['id']))


final = llm.invoke(messages)
print(final.content)