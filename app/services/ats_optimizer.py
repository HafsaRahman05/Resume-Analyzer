ACTION_VERBS = {
    "worked on": "developed",
    "responsible for": "managed",
    "helped": "assisted",
    "made": "created",
    "did": "executed"
}

ATS_SECTIONS = [
    "SKILLS",
    "EXPERIENCE",
    "PROJECTS",
    "EDUCATION",
    "CERTIFICATIONS"
]


def improve_action_verbs(text: str) -> str:
    for weak, strong in ACTION_VERBS.items():
        text = text.replace(weak, strong)
    return text


def add_missing_skills(text: str, missing_skills: list) -> str:
    if not missing_skills:
        return text

    skills_section = "\n\nSKILLS\n" + ", ".join(missing_skills[:8])
    return text + skills_section


def format_for_ats(text: str) -> str:
    formatted = text.upper()
    for section in ATS_SECTIONS:
        if section not in formatted:
            formatted += f"\n\n{section}\n"
    return formatted


def optimize_resume(resume_text: str, missing_skills: list):
    optimized = resume_text.lower()
    optimized = improve_action_verbs(optimized)
    optimized = add_missing_skills(optimized, missing_skills)
    optimized = format_for_ats(optimized)

    return optimized
