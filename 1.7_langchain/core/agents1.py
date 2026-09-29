

import warnings

# Suppress the deprecation warning in 1.2.11
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langgraph.prebuilt import create_react_agent
from core.models import create_model
from tools.image_gen import generate_image
from tools.websearch import web_search
from tools.voice import text_to_speech

SYSTEM_PROMPT = """You are a helpful multimodal assistant with tools for image generation, web search, text-to-speech.
Only call a tool when a request genuinely needs it:
- generate image: only when the user explicitly asks you to create, draw or visualize something 
- web search: only for current events, recent news, or facts you wouldn't reliably know 
- text to speech: only when the user explicitly asks for audio or spoken output 

For everything else, greetings, general knowledge, explanations, conversations answer directly without calling any tool.
"""

def build_multimodal_agent():
    model = create_model()
    tools = [generate_image, web_search, text_to_speech]
    
    # Passing system prompt via prompt= (or state_modifier=)
    return create_react_agent(model, tools, prompt=SYSTEM_PROMPT)

agent = build_multimodal_agent()

# Image generation
# result = agent.invoke({"messages": [("user", "generate an image of messi")]})
# print(result["messages"][-1].content)


# Web search
# result = agent.invoke({ 'messages': [('user','give me latest news on SpaceX')]})
# print(result['messages'][-1].content)