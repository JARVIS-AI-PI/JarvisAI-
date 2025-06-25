import openai
import socket
import os

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53))
        return True
    except:
        return False

def get_api_key():
    if os.path.exists("openai.key"):
        with open("openai.key", "r") as f:
            return f.read().strip()
    return None

def can_handle(text):
    return True

def handle(text, config):
    if not is_connected():
        return "No internet. Switching to offline fallback."

    api_key = get_api_key()
    if not api_key:
        return "API key not found. Please create a file called 'openai.key' with your OpenAI API key."

    try:
        openai.api_key = api_key

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Jarvis, a smart AI assistant."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error using ChatGPT: {str(e)}"
