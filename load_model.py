import google.generativeai as genai
import os

def load_llm() -> genai.GenerativeModel:
   
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    gemini_model = genai.GenerativeModel('gemini-2.0-flash')
    
    return gemini_model