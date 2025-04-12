# src/data_processing.py

import pdfplumber
import docx2txt
import re

def extract_text_from_file(file, file_type: str) -> str:
    """
    Extract text from an uploaded file.
    Supported types: 'pdf', 'docx', 'txt'.
    """
    try:
        if file_type == "pdf":
            with pdfplumber.open(file) as pdf:
                return "\n".join([page.extract_text() or "" for page in pdf.pages])

        elif file_type == "docx":
            return docx2txt.process(file)

        elif file_type == "txt":
            return file.read().decode("utf-8", errors="ignore")

        else:
            return ""
    except Exception as e:
        return ""

def clean_text(text: str) -> str:
    """
    Clean up raw text: normalize whitespace, strip weird characters.
    """
    text = re.sub(r"\s+", " ", text)  # collapse multiple spaces/newlines
    text = re.sub(r"•", "-", text)    # convert bullets to dashes
    return text.strip()

def format_block(text: str, label: str, max_length: int = 1200) -> str:
    """
    Prepares a labeled text block for the LLM prompt.
    """
    return f"\n## {label} ##\n{text[:max_length].strip()}\n"

def truncate_text(text: str, max_tokens: int = 200) -> str:
    return " ".join(text.split()[:max_tokens])
