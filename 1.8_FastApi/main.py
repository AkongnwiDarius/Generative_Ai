from fastapi import FastAPI, HTTPException
from sqlalchemy import Update 

app = FastAPI()

# First end point 
@app.get('/')  #Explanation?
def hellos():
    return 'Hello AI engineers'  # data returned in form of a string 


#Returning in form of a dictionary 
@app.get('/hello')
def index():
    return {'Data':{'Name':"Darius", 'email':'dariuskincaid161@gamil.com', 'FavMeal':'Koki'}}


# How this can be used in AI apps 
# agents, llms, prompt templates, chains and much more 
@app.get('/get-response')
def get_ai_response():
    return{'data': 'This endpoint can be used to get response from AI models', 'Final response':'Ai response'}


# Path parameters
# Getting info from the user
@app.get('/sentiment/{text}')
def analyze_sentiment(text):
    if text == '':
        return {'data':'No text provided'}
    else:
        # perform sentiment analysis on the text and return the result 
        # use one of the hugging face models to do sentiment analysis 
        return{'Text':text, 'sentiment':'positive'}


# Another example of path parameter
@app.get('/model-response/{model_id}')
def model_response(model_id:int):
    models = {1:'gpt2', 2:'gpt3', 3:'gpt-5', 4:'gpt-6', 5:'gpt-7'}
    get_model = models.get(model_id, 'not found')
    return{
        'id':model_id,
        'model_name':get_model
    }


# query parameters 
@app.get('/bloq')
def indexs(limit:int, published:bool):
    if published:
        return {'data':f'{limit} published blogs from DB'}
    else: 
        return {'data':f'{limit} blogs from DB'}


# query parameters exrecise 
models = ['gpt', 'gemini', 'llama']

@app.get('/response')
def generate_response(prompt:str, model:str):
    if model in models:
        return{
            'data': 'This is your reponse',
            'model': model,
            'prompt': prompt
        }
    else:
        return {
            'data': 'no model found'
        }


# Request Body 
# Pydantic
from typing import Optional
from pydantic import BaseModel

#first class structured or blueprint
class HelloRequest(BaseModel): #This is like the blue print or skeleton of how we want the request body to be
    name:str
    email:str
    age:int

#first post endpoint 
@app.post('/hello')
def hello(request:HelloRequest):
    return {'data':f'Hello {request.name}, your email is {request.email} and your are {request.age} years old.'}


#second class or blueprint
class StudentRequest(BaseModel):
    name:str
    email:str
    age:int
    course:Optional[str]='Ai fundamentals'  # optional is gotten from typing and the ai fundematals is just the default string to be plavced if none is selected but can still be empty without the equal to 

#second post endpoint
@app.post('/student')
def student(request:StudentRequest):
    return{'data':f'Helo {request.name}, your email is {request.email}, you are {request.age} years old and you are enrolled in the {request.course} course'}


# this in memory store is for learning only: its data resets whenever the app restarts
students:dict[int, StudentRequest]={}
next_student_id=1

@app.post('/students', status_code =201)
def create_student(request: StudentRequest):
    """Create a student; post sends a new record to the collection"""
    global next_student_id
    student_id=next_student_id
    next_student_id+=1
    students[student_id]=request
    return {'id': student_id, **request.model_dump()}


# REST APi
# first get endpoint 
@app.get('/students/{student_id}')
def get_student(student_id:int):
    """Read one student by ID; the ID is part of the URL path"""
    student_record=students.get(student_id)
    if student_record is None:
        raise HTTPException(status_code=404, detail='Student not found')
    return {'id':student_id, **student_record.model_dump()}


# PUT  endpoint 
@app.put('/students/{student_id}')
def replace_students(student_id:int, request:StudentRequest):
    """Replace every student Filed; PUT expecta the complete record"""
    if student_id not in students:
        raise HTTPException(status_code=404, detail='student not found')
    students[student_id]=request
    return {'id':student_id, **request.model_dump()}


# PATCH endpoint 
class StudentPatch(BaseModel):
    # optional; fields let PATCH callers send only the values they ant to change 
    name:Optional[str]=None
    email:Optional[str]=None
    age:Optional[int]=None
    course:Optional[str]=None

@app.patch('/students/{student_id}')
def patch_students(student_id:int, request:StudentPatch):
    """Change only fields send by the caller; PATCH keeps all other values"""
    student_record=students.get(student_id)
    if student_record is None:
        raise HTTPException(status_code=404, detail='Student not found')
    updated_fields=request.model_dump(exclude_unset=True)
    updated_record=student_record.model_copy(update=updated_fields)
    students[student_id] = updated_record
    return {'id': student_id, **updated_record.model_dump()}

# DELETE endpoint
@app.delete('/students/{student_id})', status_code=404)
def delete_student(student_id:int):
    """Delete one student; DELETE succeeds without returning a response body"""
    if student_id not in students:
        raise HTTPException(status_code=404, detail='Student not found')
    del students[student_id]