from pydantic import BaseModel, Field
from .models import create_model
from config import QWEN

model = create_model()

#creating the blueprint for our output for our model
class Player(BaseModel):
    name: str = Field(description="The name of the player")
    age: int = Field(description="The age of the player")
    club: str = Field(description="The club the player belongs to")
    nationality: str = Field(description="The nationality of the player")
    national_flag: str = Field(description="The national flag of the player as an emoji")

class TopTen(BaseModel):
    opinion: str = Field(description="the opinion of the model about the top ten footballers of all time")
    players: list[Player] = Field(description="A list of the top ten footballers of all time")

structured_model = model.with_structured_output(TopTen)
results = structured_model.invoke("the top ten footballers of all time")
# print(results)

#.model_dump() prints the models ouput in a dictionary format
print(results.model_dump())

# print(f'the players name is {results.name}')
# print(f'the players age is {results.age}')
