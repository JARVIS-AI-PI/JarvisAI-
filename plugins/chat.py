def can_handle(text):
    return True  # Always allow fallback if online plugin fails

def handle(text, config):
    responses = {
        "hi": "Hello! (offline mode)",
        "hello": "Hi there! (offline)",
        "what is your name": "I am Jarvis, operating in offline mode.",
        "how are you": "I'm fully operational even offline.",
        "bye": "Goodbye! See you again."
    }

    for key in responses:
        if key in text.lower():
            return responses[key]

    return "I'm in offline mode. Limited functions are available."
