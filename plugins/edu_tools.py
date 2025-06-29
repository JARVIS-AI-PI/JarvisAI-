from brain.chatgpt import ask_chatgpt

def define_word(word):
    return ask_chatgpt(f"Define the word: {word}")

def explain_concept(concept):
    return ask_chatgpt(f"Explain: {concept}")

def summarize_text(text):
    return ask_chatgpt(f"Summarize: {text}")

def spell_word(word):
    return " ".join([ch.upper() for ch in word])

def run():
    print("📚 Educational Tools Plugin Started")
    while True:
        command = input("Ask (or 'exit'): ").lower()
        
        if "define" in command:
            word = command.replace("define", "").strip()
            print("📖", define_word(word))

        elif "explain" in command:
            topic = command.replace("explain", "").strip()
            print("🧠", explain_concept(topic))

        elif "summarize" in command:
            text = command.replace("summarize", "").strip()
            print("✂️", summarize_text(text))

        elif "spell" in command:
            word = command.replace("spell", "").strip()
            print("🔤", spell_word(word))

        elif "exit" in command:
            print("👋 Exiting Edu Tools.")
            break

        else:
            print("❓ Unknown command. Try: define, explain, summarize, spell.")
