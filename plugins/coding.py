def can_handle(text):
    keywords = ["write code", "generate code", "make python", "create html"]
    return any(kw in text.lower() for kw in keywords)

def handle(text, config):
    if "python" in text.lower():
        code = "def greet(name):\n    return f'Hello, {name}!'\n\nprint(greet('Jarvis'))"
        filename = "generated_code.py"

    elif "html" in text.lower():
        code = "<!DOCTYPE html>\n<html>\n<head><title>Jarvis Page</title></head>\n<body>\n<h1>Hello from Jarvis</h1>\n</body>\n</html>"
        filename = "generated_page.html"

    else:
        return "Please specify which language: Python or HTML."

    try:
        with open(filename, "w") as f:
            f.write(code)
        return f"Code generated and saved to {filename}"
    except Exception as e:
        return f"Error writing code: {e}"
