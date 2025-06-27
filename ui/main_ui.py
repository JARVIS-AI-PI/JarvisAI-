import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from voice.listener import listen
from voice.talker import speak
import jarvis

class JarvisUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis AI Assistant")
        self.root.geometry("320x240")
        self.root.configure(bg="black")

        self.chat_area = ScrolledText(root, wrap=tk.WORD, font=("Arial", 10), bg="#222", fg="white")
        self.chat_area.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        self.chat_area.insert(tk.END, "Jarvis is ready. Type or press mic.\n\n")
        self.chat_area.configure(state='disabled')

        self.input_box = tk.Entry(root, font=("Arial", 12))
        self.input_box.pack(padx=5, pady=5, fill=tk.X)
        self.input_box.bind("<Return>", self.on_enter)

        self.mic_button = tk.Button(root, text="🎙️", command=self.on_mic_click, font=("Arial", 12))
        self.mic_button.pack(pady=5)

    def on_enter(self, event=None):
        user_input = self.input_box.get()
        self.input_box.delete(0, tk.END)
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, f"You: {user_input}\n")
        self.chat_area.configure(state='disabled')

        response = jarvis_response(user_input)
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, f"Jarvis: {response}\n\n")
        self.chat_area.configure(state='disabled')
        self.chat_area.yview(tk.END)

    def on_mic_click(self):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, "🎤 Listening...\n")
        self.chat_area.configure(state='disabled')
        text = listen()
        self.input_box.insert(0, text)
        self.on_enter()

def jarvis_response(user_input):
    from jarvis import load_config, load_plugins
    config = load_config()
    plugins = load_plugins()

    for name, plugin in plugins.items():
        if hasattr(plugin, "can_handle") and plugin.can_handle(user_input):
            response = plugin.handle(user_input, config)
            if config.get("voice_mode", True):
                speak(response)
            return response

    return "I don't understand."

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisUI(root)
    root.mainloop()
