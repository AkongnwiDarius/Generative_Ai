from http.client import responses
from urllib import response

from .models import create_model
from config import QWEN

model = create_model(QWEN)
# response = model.invoke('who is the first lady of the united states of america')
# print(response.content)

# for chunk in model.stream('who is the GOAt of football'):
#     print(f' {chunk.content}', flush=True , end='')

message_batches = [
    'wht do they call black americans nigros',
    'who was the first president of cameroon',
    'who started world war 2'
]

responses = model.batch(message_batches)

for r in responses:
    print(r.text)