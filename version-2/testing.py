import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8000"

response = requests.get(
    f"{BASE_URL}/questions/?use=MCQ&subject=math&number=5",  # Use valid parameters found in the Excel file
    auth=HTTPBasicAuth("alice", "wonderland")
)

print(response.json())

# # Test creating a question (admin role)
# response = requests.post(
#     f"{BASE_URL}/questions/",
#     json={"question": "What is 2+2?", "subject": "math", "correct": "4", "use": "MCQ", "answerA": "3", "answerB": "4", "answerC": "5", "answerD": "6"},
#     auth=HTTPBasicAuth("admin", "4dm1N")
# )
# print(response.json())