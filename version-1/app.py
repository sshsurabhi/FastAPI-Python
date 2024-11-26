from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List, Optional
from pydantic import BaseModel
import pandas as pd
import random
import logging

# Initialize app
app = FastAPI()

# Load dataset
data_file = "dataset/questions_en.xlsx"
questions_df = pd.read_excel(data_file)


# Drop rows with NaN or infinite values
questions_df = questions_df.replace([float('inf'), float('-inf')], float('nan')).dropna()
# Replace NaN with a default value (e.g., "unknown")
questions_df = questions_df.fillna({"use": "unknown", "subject": "unknown", "question": "unknown"})


# Basic auth
security = HTTPBasic()
users = {"alice": "wonderland", "bob": "builder", "clementine": "mandarine"}
admin_password = "4dm1N"

# Models
class Question(BaseModel):
    question: str
    subject: str
    correct: str
    use: str
    answerA: str
    answerB: str
    answerC: Optional[str] = None
    answerD: Optional[str] = None

class QuestionRequest(BaseModel):
    use: str
    subjects: List[str]
    count: int

# Verify user credentials
def verify_user(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username not in users or users[credentials.username] != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return credentials.username

def verify_admin(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != admin_password:
        raise HTTPException(status_code=403, detail="Admin access required")
    return credentials.username

@app.get("/")
def health_check():
    """Health check endpoint."""
    return {"status": "API is functional"}

@app.post("/get-questions/")
def get_questions(request: QuestionRequest, username: str = Depends(verify_user)):
    """Fetch random questions based on filters."""
    filtered_df = questions_df[
        (questions_df["use"] == request.use) &
        (questions_df["subject"].isin(request.subjects))
    ]
    if filtered_df.empty:
        raise HTTPException(status_code=404, detail="No questions found for the given criteria")
    
    # Randomize and select the requested count
    questions = filtered_df.sample(n=min(request.count, len(filtered_df))).to_dict(orient="records")
    return {"questions": questions}

@app.post("/add-question/")
def add_question(question: Question, username: str = Depends(verify_admin)):
    """Add a new question (admin-only)."""
    global questions_df
    new_question = pd.DataFrame([question.dict()])
    questions_df = pd.concat([questions_df, new_question], ignore_index=True)
    return {"status": "Question added successfully"}

@app.get("/questions/")
def list_questions(username: str = Depends(verify_admin)):
    """List all questions (admin-only)."""
    global questions_df
    if questions_df.empty:
        raise HTTPException(status_code=404, detail="No questions available")

    try:
        # Clean the DataFrame: Replace NaN/None values with empty strings or defaults
        clean_df = questions_df.fillna("").replace([float("inf"), float("-inf")], "")
        
        # Convert the cleaned DataFrame to JSON
        questions = clean_df.to_dict(orient="records")
        return {"questions": questions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing questions: {str(e)}")

@app.get("/debug/")
def debug_questions():
    """Check the questions DataFrame for invalid or out-of-range values."""
    global questions_df

    # Check for NaN or infinite values
    if questions_df.isnull().values.any():
        return {"error": "DataFrame contains NaN values"}
    if (questions_df.isin([float('inf'), float('-inf')])).any().any():
        return {"error": "DataFrame contains infinite values"}
    
    return {"questions": questions_df.to_dict(orient="records")}

