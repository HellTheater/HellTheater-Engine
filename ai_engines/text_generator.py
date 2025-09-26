from transformers import pipeline

class TextGenerator:
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt2")

    def generate(self, prompt, max_length=100):
        result = self.generator(prompt, max_length=max_length, num_return_sequences=1)
        return result[0]["generated_text"]
