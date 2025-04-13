# Cover Letter Generator using Generative AI

This is a web-based application that generates personalized cover letters using large language models (LLMs). It allows users to upload their resume and a job description, choose between a short or long tone, and select the backend model (local or cloud-hosted) to generate a tailored output.

---

## Objective

The goal of this project is to make the job application process more efficient by automating cover letter creation using state-of-the-art generative AI. This tool helps users draft high-quality, job-specific letters in seconds.

---

## Features

- Upload your Resume and Job Description in plain text or PDF
- Choose model: Groq (LLaMA 3.3 70B) or local (Flan-T5-Large)
- Select tone: Short or Long
- Generate cover letters instantly
- Hosted on Hugging Face Spaces

---

## Project Structure

```
cover-letter-generator/
├── app.py
├── requirements.txt
├── .streamlit/
│   └── secrets.toml
└── src/
    ├── models/
    │   ├── groq_model.py
    │   └── local_model.py
    ├── prompts/
    │   ├── groq_prompt.py
    │   └── flan_prompt.py
    ├── model_selector.py
    ├── data_processing.py
    └── cover_letter_generator.py
```

---

## ⚙️ How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/your-username/cover-letter-generator.git
cd cover-letter-generator
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Add your Groq API key in `.streamlit/secrets.toml`
```toml
groq_api_key = "your_groq_api_key"
```

5. Launch the app
```bash
streamlit run app.py
```

---

## Models Used

| Model            | Hosted On      | Notes                          |
|------------------|----------------|--------------------------------|
| Flan-T5-Large    | Local Runtime  | Lightweight backup model       |
| LLaMA 3.3 70B    | Groq Cloud API | High-speed, high-quality model |

---

## Model Performance

| Model           | Short Output | Long Output   |
|-----------------|--------------|---------------|
| LLaMA 3.3 70B   | ~2.5 sec     | ~2.8 sec      |
| Flan-T5-Large   | ~35 sec      | ~2 mins       |

*LLaMA 3.3 70B produced significantly better, more human-sounding responses.*

---

## Future Enhancements

- Add tone, style, and length customization options
- Include keyword-based filtering
- Improve UI/UX for mobile devices
- Host on AWS/GCP for faster local model inference

---

## Live App

Try it here on [Hugging Face Spaces](https://huggingface.co/spaces/sanjeethnc/cover-letter-generator-ds552)

---

## License

This project was built as part of the DS552 - Generative AI course at Worcester Polytechnic Institute.
