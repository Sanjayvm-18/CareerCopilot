from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # This loads your .env file

client = OpenAI()  # Now uses the key from .env



def get_resume_feedback(resume_text: str) -> str:
    prompt = f"""
    You are a career advisor. Review the following resume text:

    {resume_text}

    1. What are the strengths?
    2. What are 3 areas of improvements?
    3. Estimate an ATS score out of 10.
    4. Suggest improvements for formatting, tone, and relevance.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=700
    )
    return response.choices[0].message.content