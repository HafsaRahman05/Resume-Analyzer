import requests


REMOTIVE_API = "https://remotive.com/api/remote-jobs"


def fetch_jobs():
    response = requests.get(REMOTIVE_API)
    data = response.json()
    return data.get("jobs", [])


def match_jobs(resume_skills: list):
    jobs = fetch_jobs()
    matched_jobs = []

    for job in jobs[:50]:  # limit for performance
        description = job["description"].lower()
        title = job["title"]

        match_count = sum(skill in description for skill in resume_skills)
        match_percent = int((match_count / max(len(resume_skills), 1)) * 100)

        if match_percent > 20:
            matched_jobs.append({
                "title": title,
                "company": job["company_name"],
                "location": job["candidate_required_location"],
                "url": job["url"],
                "match_percent": match_percent
            })

    return sorted(matched_jobs, key=lambda x: x["match_percent"], reverse=True)
