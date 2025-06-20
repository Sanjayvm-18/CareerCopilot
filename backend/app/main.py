# backend/app/main.py

# from fastapi import FastAPI, UploadFile, File
# from app.services.pdf_parser import extract_text_from_pdf
# from app.services.gpt_client import get_resume_feedback

# app = FastAPI()

# @app.post("/analyze-resume/")
# async def analyze_resume(file: UploadFile = File(...)):
#     content = await file.read()
#     resume_text = extract_text_from_pdf(content)
#     feedback = get_resume_feedback(resume_text)
#     return {"feedback": feedback}


# backend/app/main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware  # Import CORS
from app.services.pdf_parser import extract_text_from_pdf
from app.services.gpt_client import get_resume_feedback

app = FastAPI()

# Enable CORS for React frontend (default React port 3000)
origins = [
    "http://localhost:3000",  # React frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-resume/")
async def analyze_resume(file: UploadFile = File(...)):
    content = await file.read()
    resume_text = extract_text_from_pdf(content)
    feedback = get_resume_feedback(resume_text)
    return {"feedback": feedback}

