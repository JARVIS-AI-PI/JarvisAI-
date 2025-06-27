def can_handle(text):
    return "edit" in text.lower() and ".py" in text.lower()

def handle(text, config):
    try:
        parts = text.split("edit")
        if len(parts) < 2:
            return "Please mention the file name to edit."

        filename = parts[1].strip()
        if not filename.endswith(".py"):
            return "Only Python files can be edited."

        print(f"Opening {filename} for editing...")
        lines = []
        print("Type your new code line by line. Type 'SAVE' to save and exit.")
        while True:
            line = input(">>> ")
            if line.strip().upper() == "SAVE":
                break
            lines.append(line)

        with open(filename, "w") as f:
            f.write("\n".join(lines))

        return f"{filename} updated successfully."
    except Exception as e:
        return f"Editing failed: {e}"
