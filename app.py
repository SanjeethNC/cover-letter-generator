# app.py
import streamlit as st
from src.data_processing import extract_text_from_file, clean_text, format_block, truncate_text
from src.cover_letter_generator import generate_cover_letter
from src.model_selector import load_model

def is_valid_text(text, min_words=30):
    return len(text.split()) >= min_words and not any(
        bad in text.lower() for bad in ["&mdash", ".doc", ".pdf", "file.doc", "cleaver agreement"]
    )

def main():
    st.set_page_config(page_title="Cover Letter Generator", layout="wide")

    st.markdown("<h1 style='margin-bottom: 1rem;'>AI-Powered Cover Letter Generator</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style='font-size: 16px; color: #555;'>Upload your resume and job description, choose a model, and generate a professional, ATS-optimized cover letter.</p>
        <hr style='margin-top: 10px; margin-bottom: 25px;'/>
        """,
        unsafe_allow_html=True
    )

    # Two-column layout
    left, right = st.columns([1, 1.5], gap="large")

    with left:
        st.subheader("Input")

        model_name = st.selectbox("Choose a Model", [
            "llama-3.3-70b-versatile",
            "google/flan-t5-large"
        ])

        resume_file = st.file_uploader("Upload Your Resume", type=["pdf", "docx", "txt"])
        jd_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])

        generate_clicked = st.button("Generate Cover Letter")

    with right:
        st.subheader("Output")
        if generate_clicked:
            if resume_file is None or jd_file is None:
                st.error("Please upload both files.")
                return

            resume_type = resume_file.name.split(".")[-1].lower()
            jd_type = jd_file.name.split(".")[-1].lower()

            with st.spinner("Reading and cleaning files..."):
                resume_text = clean_text(extract_text_from_file(resume_file, resume_type))
                jd_text = clean_text(extract_text_from_file(jd_file, jd_type))

            if not is_valid_text(resume_text) or not is_valid_text(jd_text):
                st.error("One or both files do not contain valid resume or job description content.")
                return

            resume_block = format_block(truncate_text(resume_text, 200), "RESUME")
            jd_block = format_block(truncate_text(jd_text, 200), "JOB DESCRIPTION")

            with st.spinner("Loading model..."):
                text_generator = load_model(model_name)

            with st.spinner("Generating cover letter..."):
                cover_letter = generate_cover_letter(text_generator, resume_block, jd_block, model_name=model_name)

            st.success("Cover Letter Generated")
            st.text_area("Generated Cover Letter", cover_letter, height=400)

            st.download_button(
                label="Download Cover Letter",
                data=cover_letter,
                file_name="cover_letter.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()
