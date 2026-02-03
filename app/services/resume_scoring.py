import re

# Basic skill database (you can expand later)
SKILLS_DB = [
    "python", "java", "c++", "sql", "fastapi", "django",
    "machine learning", "nlp", "html", "css", "javascript",
    "react", "node", "mongodb", "postgresql", "aws", "docker"
]

EDUCATION_KEYWORDS = ["bachelor", "master", "degree", "b.tech", "m.tech", "phd"]

ATS_KEYWORDS = [
    "experience", "skills", "projects", "education",
    "certification", "responsibilities", "achievements"
]


def calculate_resume_score(resume_text: str):
    text = resume_text.lower()

    # -------- SKILLS SCORE (30) --------
    found_skills = [skill for skill in SKILLS_DB if skill in text]
    skills_score = min(len(found_skills) * 3, 30)

    # -------- EXPERIENCE SCORE (25) --------
    years = re.findall(r'(\d+)\+?\s+years?', text)
    if years:
        experience_score = min(int(years[0]) * 5, 25)
    else:
        experience_score = 10  # default

    # -------- EDUCATION SCORE (15) --------
    edu_score = 15 if any(word in text for word in EDUCATION_KEYWORDS) else 5

    # -------- ATS SCORE (30) --------
    ats_found = sum(1 for word in ATS_KEYWORDS if word in text)
    ats_score = min(ats_found * 5, 30)

    total_score = skills_score + experience_score + edu_score + ats_score

    return {
        "total_score": total_score,
        "skills_score": skills_score,
        "experience_score": experience_score,
        "education_score": edu_score,
        "ats_score": ats_score,
        "found_skills": found_skills,
        "missing_skills": list(set(SKILLS_DB) - set(found_skills))
    }
