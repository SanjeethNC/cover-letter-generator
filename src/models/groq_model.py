try:
    from groq import Groq
except ImportError:
    Groq = None

class GroqModelWrapper:
    def __init__(self, api_key: str, model: str):
        if Groq is None:
            raise ImportError("groq package not installed.")
        self.client = Groq(api_key=api_key)
        self.model = model

    def __call__(self, prompt, max_length=300, temperature=0.7, top_p=0.95, repetition_penalty=1.25, **kwargs):
        messages = [{"role": "user", "content": prompt}]
        response = self.client.chat.completions.create(
            messages=messages,
            model=self.model,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_length
        )
        return [{"generated_text": response.choices[0].message.content}]
