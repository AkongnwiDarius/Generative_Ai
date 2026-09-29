from pydantic import BaseModel, Field
from .models import create_model
from config import QWEN

model = create_model()


class CourseFeedback(BaseModel):
    sentiment: str = Field( description="positive, negative, neutral")
    key_points: list[str] = Field(description='key points extracted')
    suggested_actions: str = Field(description='points suggested to be taken')
    original_text: str = Field(description='the original input text')

#creating our build feedbacl classifier
def build_feedback_classifier():
    structured_model = model.with_structured_output(CourseFeedback)
    return structured_model

classifier = build_feedback_classifier()

#creating our feedback 

feedbacks = ['the lecturer explains concepts very clearly and the examples are excellent',
             'the lessons are confusing and we need more examples',
             'the course content is difficult to follow and the teaching needs improvement',
             'the course is okay but some concepts could be explained better',
             'i really enjoyed the course and found the practical exercise very useful']

for feedback in feedbacks:
    result = classifier.invoke(feedback)
print(result)
    

 