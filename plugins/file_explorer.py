import os

def list_files(path="."):
    try:
        items = os.listdir(path)
        print(f"📂 Contents of {os.path.abspath(path)}:")
        for item in items:
            print(" -", item)
    except Exception as e:
        print(f"[❌ Error] {e}")

def search_file(filename, root="."):
    matches = []
    for dirpath, _, files in os.walk(root):
        if filename in files:
            matches.append(os.path.join(dirpath, filename))
    return matches

def delete_file(filepath):
    try:
        os.remove(filepath)
        print(f"🗑️ Deleted: {filepath}")
    except Exception as e:
        print(f"[❌ Error] {e}")

def rename_file(old, new):
    try:
        os.rename(old, new)
        print(f"🔁 Renamed: {old} ➜ {new}")
    except Exception as e:
        print(f"[❌ Error] {e}")

def run():
    print("🗂️ File Explorer Plugin Started")
    while True:
        command = input("File command (or 'exit'): ").lower()
        if "list" in command:
            folder = command.replace("list", "").strip() or "."
            list_files(folder)
        elif "find" in command or "search" in command:
            filename = command.replace("find", "").replace("search", "").strip()
            results = search_file(filename)
            if results:
                print("📁 Found:")
                for r in results:
                    print(" -", r)
            else:
                print("❌ File not found.")
        elif "delete" in command:
            filename = command.replace("delete", "").strip()
            delete_file(filename)
        elif "rename" in command:
            parts = command.replace("rename", "").strip().split(" to ")
            if len(parts) == 2:
                rename_file(parts[0].strip(), parts[1].strip())
            else:
                print("⚠️ Usage: rename old.txt to new.txt")
        elif "exit" in command:
            print("👋 Exiting File Explorer.")
            break
        else:
            print("❓ Unknown command. Try: list, find, delete, rename.")
