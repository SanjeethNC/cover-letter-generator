# src/cover_letter_generator.py
from .prompts.flan_prompt import build_flan_prompt
from .prompts.groq_prompt import build_groq_prompt


def generate_cover_letter(
    text_generator,
    resume_block: str,
    jd_block: str,
    max_length: int = 900,
    model_name: str = None
) -> str:
    """
    Generates a structured, high-quality cover letter using the selected LLM model.
    """
    if model_name == "google/flan-t5-large":
        prompt = build_flan_prompt(resume_block, jd_block)
    else:
        prompt = build_groq_prompt(resume_block, jd_block)

    outputs = text_generator(
        prompt,
        max_length=max_length,
        min_length=350,
        temperature=0.65,
        top_p=0.95,
        repetition_penalty=1.15,
        do_sample=True,
        num_return_sequences=1
    )

    return outputs[0]["generated_text"]
