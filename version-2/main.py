from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
import pandas as pd
import random

app = FastAPI()
security = HTTPBasic()

# User Database
USER_DB = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine"
}

# Admin Password
ADMIN_PASSWORD = "4dm1N"

# Reading the questions from the Excel file
questions_df = pd.read_excel('questions.xlsx')  # Adjusted this line to read from Excel
print(questions_df.head())  # Print first few rows to verify

class Question(BaseModel):
    question: str
    subject: str
    correct: str
    use: str
    answerA: str
    answerB: str
    answerC: str
    answerD: str


def fake_decode_token(credentials: HTTPBasicCredentials):
    if credentials.username in USER_DB and USER_DB[credentials.username] == credentials.password:
        return credentials.username
    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/")
async def read_root():
    return {"message": "Welcome to the MCQ API"}

# Load questions
questions_df = pd.read_excel('questions.xlsx')
print(questions_df.head())  # Check the contents

@app.get("/questions/")
async def get_questions(use: str, subject: str, number: int = Query(..., ge=5, le=20), 
                        credentials: HTTPBasicCredentials = Depends(security)):
    fake_decode_token(credentials)

    # Filtering the DataFrame for matching entries
    filtered_questions = questions_df[
        (questions_df['use'].str.lower() == use.lower()) &
        (questions_df['subject'].str.lower() == subject.lower())
    ]

    if filtered_questions.empty:
        raise HTTPException(status_code=404, detail="No questions found")

    selected_questions = filtered_questions.sample(n=min(number, len(filtered_questions)), random_state=1)

    return selected_questions.to_dict(orient='records')


@app.get("/questions/")
async def get_questions(use: str, subject: str, number: int = Query(..., ge=5, le=20), 
                        credentials: HTTPBasicCredentials = Depends(security)):
    fake_decode_token(credentials)
    
    filtered_questions = questions_df[
        (questions_df['use'] == use) & (questions_df['subject'] == subject)
    ]

    if filtered_questions.empty:
        raise HTTPException(status_code=404, detail="No questions found")

    selected_questions = filtered_questions.sample(n=min(number, len(filtered_questions)), random_state=1)

    return selected_questions.to_dict(orient='records')


@app.post("/questions/")
async def create_question(question: Question, credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != ADMIN_PASSWORD:
        raise HTTPException(status_code=403, detail="Not authorized to create a question")

    # Append new question to the CSV or Database
    # In a real application, save it to the database or modify the DataFrame as necessary
    new_question = question.dict()
    print("New question would be stored:", new_question)
    
    return {"msg": "Question created"}


@app.get("/verify/")
async def verify_api():
    return {"status": "API is functional!"}