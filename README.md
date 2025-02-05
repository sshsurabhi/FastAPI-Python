--- 
# FastAPI Questionnaire API 
### (Refer Version-1, Version-2 for better understanding)
## Overview

This project implements a FastAPI-based API designed for a questionnaire application, enabling users to generate multiple-choice questions (MCQs) based on selected categories and test types. Utilizing a structured dataset, the API enables secure access, random question retrieval, and admin functionalities for managing questions.

## Key Features

1. **Randomized Question Retrieval:**
   - Users can select a test type and multiple categories to generate MCQs in sets of 5, 10, or 20 questions, delivered in a randomized order for varied quiz experiences.

2. **User Authentication:**
   - Basic authentication is implemented to ensure that only authorized users can access the API using usernames and passwords. The current user credentials are:
     - `alice`: `wonderland`
     - `bob`: `builder`
     - `clementine`: `mandarine`

3. **Admin Capabilities:**
   - An admin endpoint allows an admin user to create new questions. The admin username and password for this functionality are:
     - Username: `admin`
     - Password: `4dm1N`

4. **Health Check Endpoint:**
   - A dedicated endpoint is available to verify the API’s operational status.

5. **Error Handling and Documentation:**
   - The API is extensively documented for ease of use and includes error responses for various incorrect usages.

## Dataset

The questions are sourced from an Excel file located [here](https://dst-de.s3.eu-west-3.amazonaws.com/fastapi_en/questions_en.xlsx). Each question includes fields such as `question`, `subject`, `correct`, `use`, and multiple possible answers. 

To explore the dataset, you can download it using the following command:

```bash
wget https://dst-de.s3.eu-west-3.amazonaws.com/fastapi_en/questions_en.xlsx
```

*Note: Ensure you have the `openpyxl` package installed to read Excel files.*

## Requirements

You can find the list of required Python libraries in the `requirements.txt` file.

## Usage

1. Clone the repository to your local environment.
2. Install the necessary libraries with:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```
4. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Conclusion

This FastAPI implementation offers a robust foundation for creating a dynamic questionnaire application, showcasing FastAPI's capabilities in handling asynchronous requests, user authentication, and generating structured API documentation effortlessly.

--- 
