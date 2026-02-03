from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from app.database import jobs_collection
from app.services.resume_parser import extract_resume_text
from app.services.resume_scoring import calculate_resume_score
from app.services.job_fetcher import match_jobs

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/recommend")
async def recommend_jobs(file: UploadFile = File(...)):
    filename = file.filename
    file_ext = filename.split(".")[-1].lower()

    if file_ext not in ["pdf", "docx"]:
        raise HTTPException(status_code=400, detail="Only PDF or DOCX allowed")

    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    resume_text = extract_resume_text(file_path, file_ext)
    score_data = calculate_resume_score(resume_text)

    recommended_jobs = match_jobs(score_data["found_skills"])
    jobs_collection.insert_one({
    "skills_used": score_data["found_skills"],
    "results_count": len(recommended_jobs)
})

    return {
        "recommended_jobs": recommended_jobs[:10]
    }
