from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from app.database import resumes_collection
from app.services.resume_parser import extract_resume_text
from app.services.resume_scoring import calculate_resume_score
from app.services.ats_optimizer import optimize_resume


router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    filename = file.filename
    file_ext = filename.split(".")[-1].lower()

    if file_ext not in ["pdf", "docx"]:
        raise HTTPException(status_code=400, detail="Only PDF or DOCX files allowed")

    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        resume_text = extract_resume_text(file_path, file_ext)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "filename": filename,
        "extracted_text": resume_text[:3000]  # limit output
    }

@router.post("/score")
async def score_resume(file: UploadFile = File(...)):
    filename = file.filename
    file_ext = filename.split(".")[-1].lower()
    

    if file_ext not in ["pdf", "docx"]:
        raise HTTPException(status_code=400, detail="Only PDF or DOCX allowed")

    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    resume_text = extract_resume_text(file_path, file_ext)
    score_data = calculate_resume_score(resume_text)
    resumes_collection.insert_one({
    "filename": filename,
    "score": score_data
})

    return {
        "filename": filename,
        "resume_score": score_data
    }

@router.post("/optimize")
async def optimize_resume_api(file: UploadFile = File(...)):
    filename = file.filename
    file_ext = filename.split(".")[-1].lower()

    if file_ext not in ["pdf", "docx"]:
        raise HTTPException(status_code=400, detail="Only PDF or DOCX allowed")

    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    resume_text = extract_resume_text(file_path, file_ext)
    score_data = calculate_resume_score(resume_text)

    optimized_resume = optimize_resume(
        resume_text,
        score_data["missing_skills"]
    )

    return {
        "filename": filename,
        "optimized_resume": optimized_resume[:4000]
    }
