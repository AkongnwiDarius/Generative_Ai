import re

from pydantic import BaseModel, Field
from .chain import model, announcement
from .prompt_boot import prompt

result = announcement.invoke({
    'tone': 'SEED AI Bootcamp students',
    'audience': 'Urgent',
    'announcement_details': 'Bootcamp starts this friday'
})

class Announcement(BaseModel):
    tone: str = Field(description='{result}')
    audience: str = Field(description='{result}')
    announcement_details: str = Field(description='{result}')


structured_model = model.with_structured_output(Announcement)
results = structured_model.invoke('{result}')
print(results.model_dump())
