def build_flan_prompt(resume_block: str, jd_block: str) -> str:
    return f"""
You are a helpful career assistant writing a cover letter on behalf of a candidate.

Instructions:
- Write the letter from the candidate’s point of view.
- Tailor it to the specific role described in the job description.
- Only mention experiences, skills, or technologies present in the candidate’s resume.
- Start with "Dear Hiring Manager,"
- Highlight how the candidate’s background aligns with the job's requirements.
- End the letter professionally with a polite thank you.

Candidate's Resume:
{resume_block}

Job Description (target role):
{jd_block}

Please write the full cover letter below:
"""
