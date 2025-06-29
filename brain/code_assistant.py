import os
import openai

def set_api_key(key):
    openai.api_key = key

def generate_code(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Write Python code for: {prompt}"}],
            temperature=0.5,
            max_tokens=500
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

def explain_code(code):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Explain this Python code:\n{code}"}],
            temperature=0.3,
            max_tokens=500
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

def fix_code(code):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Fix this broken Python code:\n{code}"}],
            temperature=0.3,
            max_tokens=500
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"
