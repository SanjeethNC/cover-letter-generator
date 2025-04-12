from .models.local_model import HFModelWrapper
from .models.groq_model import GroqModelWrapper
import streamlit as st



GROQ_MODEL_NAME = "llama-3.3-70b-versatile"
HF_MODEL_NAME = "google/flan-t5-large"

def load_model(model_name: str):
    if model_name == GROQ_MODEL_NAME:
        api_key = st.secrets["groq_api_key"]
        return GroqModelWrapper(api_key=api_key, model=GROQ_MODEL_NAME)
    elif model_name == HF_MODEL_NAME:
        return HFModelWrapper(model_name=HF_MODEL_NAME)
    else:
        raise ValueError(f"Unsupported model: {model_name}")
