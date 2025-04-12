def build_groq_prompt(resume_block: str, jd_block: str) -> str:
    return f"""
You are a highly intelligent AI career assistant helping a job applicant craft an outstanding, tailored cover letter that increases their chances of getting hired.

The cover letter must be written from the perspective of the applicant and should highlight how their background aligns with the job description.

---

### OBJECTIVE
Generate a professional, ATS-optimized, and recruiter-friendly cover letter that:
- Clearly states the candidate's interest in the role and company
- Highlights relevant skills, experience, or achievements that match the job description
- Feels personalized, not templated
- Is written in fluent, formal business English
- Avoids vague, generic phrases like "I am writing to apply for"
- Demonstrates an understanding of the company’s focus and values if mentioned
- Concludes confidently and warmly

---

### FORMAT INSTRUCTIONS
- Start with "Dear Hiring Manager,"
- Use 3–4 meaningful paragraphs, not a giant wall of text
- End with "Sincerely," followed by the candidate’s name (which you must infer from the resume)

---

### DO NOT:
- Copy large parts of the resume or job description verbatim
- Repeat the same sentence pattern multiple times
- Make up degrees, companies, or skills that aren't present

---

### CONTEXT FOR GENERATION

Below is the candidate’s resume followed by the full job description.

{resume_block}

{jd_block}

---

### BEGIN COVER LETTER
Write a complete cover letter from the candidate’s perspective, addressing the role based on the information above:
"""
