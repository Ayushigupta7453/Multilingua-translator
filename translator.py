import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)

# models = genai.list_models()
# for m in models:
#     print(m.name)


# Load the model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")


def translate_text(text, target_language):
    prompt = (
        f"Translate the following text into {target_language}:\n\n"
        f"'{text}'\n\n"
        "Only return the translated text, without explanations."
    )
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"
