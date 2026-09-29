from tools.image_gen import generate_image
from tools.voice import text_to_speech
# from tools.websearch import TavilySearch



# result = generate_image('a boy riding a bicycle')
# print(result)

voice_response = text_to_speech.invoke({"text" : "Please give advice to a young man studying AI"})

# Print the tool's response/audio output
print(voice_response["messages"][-1].content)

# INCORRECT:
# text_to_speech.invoke({"messages": [("user", "Hello")]})

# CORRECT:
result = text_to_speech.invoke({"text": "Advice a young man to study AI"})
print(result)