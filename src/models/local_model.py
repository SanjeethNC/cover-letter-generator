from transformers import pipeline
import torch

class HFModelWrapper:
    def __init__(self, model_name: str):
        self.pipeline = pipeline(
            "text2text-generation",
            model=model_name,
            tokenizer=model_name,
            device=0 if torch.cuda.is_available() else -1
        )

    def __call__(self, prompt, max_length=600, **kwargs):
        result = self.pipeline(prompt, max_length=max_length, do_sample=True)
        return [{"generated_text": result[0]["generated_text"]}]
