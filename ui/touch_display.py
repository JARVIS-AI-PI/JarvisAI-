import tkinter as tk
from tkinter import scrolledtext
from jarvis import respond_to
from voice.talker import speak

def start_ui():
    root = tk.Tk()
    root.title("Jarvis AI Assistant")
    root.attributes('-fullscreen', True)

    frame = tk.Frame(root, bg="black")
    frame.pack(fill=tk.BOTH, expand=True)

    display = scrolledtext.ScrolledText(frame, bg="black", fg="lime", font=("Courier", 12))
    display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    display.insert(tk.END, "🤖 Jarvis is ready. Type your command below.\n\n")
    display.configure(state='disabled')

    entry = tk.Entry(frame, bg="gray15", fg="white", font=("Courier", 14))
    entry.pack(fill=tk.X, padx=10, pady=10)

    def on_enter(event=None):
        user_input = entry.get()
        entry.delete(0, tk.END)
        if not user_input.strip():
            return
        display.configure(state='normal')
        display.insert(tk.END, f"🧑 You: {user_input}\n")
        response = respond_to(user_input)
        display.insert(tk.END, f"🤖 Jarvis: {response}\n\n")
        speak(response)
        display.configure(state='disabled')
        display.yview(tk.END)

    entry.bind("<Return>", on_enter)

    root.bind("<Escape>", lambda e: root.destroy())
    root.mainloop()
