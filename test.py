import os
import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
prompt = input("Enter a prompt")

response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=7)
print(response)

