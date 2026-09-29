from langchain_core.tools import tool
from langchain_tavily import TavilySearch
from config import DEFAULT_MODEL, TAVILY
from dotenv import load_dotenv

load_dotenv()

web_search = TavilySearch(
    max_results = 5,
    topic = 'general',
)
result = web_search.invoke({'query': 'latest news on AI regulation in Africa'})
print(result)


# @tool
# def websearch(query:str) -> str:
#     """ Search the web for information using tavily search"""
#     TavilySearch(
#         max_results = 5,
#         topic = 'general',
#     )

# result = websearch.invoke({'query': 'who is the GOAT of football as of 2026'})
# print(result)
