import os
import google.generativeai as genai

# Set your working Google API key and configure the API
os.environ["GOOGLE_API_KEY"] = ""
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List available models and print them
print("Available models:")
for m in genai.list_models():
    print(f"- {m.name}")
