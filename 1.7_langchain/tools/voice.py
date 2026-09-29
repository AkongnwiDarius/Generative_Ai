from dotenv import load_dotenv
from httpx import request
from langchain_core.tools import tool 
import requests 
import os 

load_dotenv()
API_KEY = os.environ['YARNGPT_API_KEY']
API_URL = 'https://yarngpt.ai/api/v1/tts'
#why because yarn is an extenral service not given to us by langcahin 

@tool
def text_to_speech(text:str, voice:str='Emma', response_format:str='mp3')->str:
    """Generate Nigerain Accented Speech via the YarnGPT hosted API. Return path to audio file"""
    headers = {'Authorization':f'Bearer {API_KEY}'}

    payload = {
        'text': text,
        'voice' : voice,
        'response_format' : response_format
    }
    response = requests.post(API_URL, headers=headers, json=payload, stream=True, timeout=60)
    if response.status_code!=200:
        raise RuntimeError(f'YarnGPT API error {response.text}')

    #if we have something back 
    os.makedirs('generated_audio', exist_ok=True)
    path = f'generated_audio/oyput.{response_format}'
    with open(path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return path 