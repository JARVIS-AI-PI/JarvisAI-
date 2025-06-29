# 📁 JarvisAI/plugins/edu_tools.py

from chatgpt import ask_chatgpt

def define_word(word):
    return ask_chatgpt(f"Define the word: {word}")

def explain_concept(concept):
    return ask_chatgpt(f"Explain: {concept}")

def summarize_text(text):
    return ask_chatgpt(f"Summarize: {text}")

def spell_word(word):
    return " ".join(list(word.upper()))

def run():
    print("📚 Educational Tools Plugin Started")
    while True:
        cmd = input("Ask (or 'exit'): ").lower()
        if cmd.startswith("define"):
            word = cmd.replace("define", "").strip()
            print("📖", define_word(word))
        elif cmd.startswith("explain"):
            topic = cmd.replace("explain", "").strip()
            print("🧠", explain_concept(topic))
        elif cmd.startswith("summarize"):
            txt = cmd.replace("summarize", "").strip()
            print("✂️", summarize_text(txt))
        elif cmd.startswith("spell"):
            word = cmd.replace("spell", "").strip()
            print("🔤", spell_word(word))
        elif cmd == "exit":
            break
        else:
            print("❓ Use: define / explain / summarize / spell / exit")
