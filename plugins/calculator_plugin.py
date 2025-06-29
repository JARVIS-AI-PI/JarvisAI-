import re
import math

def safe_eval(expr):
    # Safely evaluate math expressions
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    code = compile(expr, "<string>", "eval")
    for name in code.co_names:
        if name not in allowed_names:
            raise NameError(f"Use of '{name}' not allowed.")
    return eval(code, {"__builtins__": {}}, allowed_names)

def extract_expression(text):
    # Remove command words and extract numbers/expressions
    text = text.lower()
    triggers = ["calculate", "what is", "evaluate", "solve", "how much is"]
    for trigger in triggers:
        if trigger in text:
            text = text.replace(trigger, "")
    return text.strip()

def run():
    print("🧮 Calculator Plugin Started.")
    try:
        user_input = input("Enter math expression (or say it): ")
        expr = extract_expression(user_input)
        result = safe_eval(expr)
        print(f"🧠 Answer: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")
