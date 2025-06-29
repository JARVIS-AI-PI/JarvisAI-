import os
import shutil

BACKUP_DIR = "brain/backups"

if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

def backup_file(filepath):
    filename = os.path.basename(filepath)
    backup_path = os.path.join(BACKUP_DIR, filename)
    shutil.copy2(filepath, backup_path)
    return backup_path

def update_file(filepath, old_text, new_text):
    if not os.path.exists(filepath):
        return f"File '{filepath}' not found."

    try:
        backup_path = backup_file(filepath)

        with open(filepath, "r") as f:
            content = f.read()

        if old_text not in content:
            return f"Original text not found in file."

        updated = content.replace(old_text, new_text)

        with open(filepath, "w") as f:
            f.write(updated)

        return f"✅ Updated '{filepath}'. Backup saved at '{backup_path}'"
    except Exception as e:
        return f"Error: {e}"
