import os
import shutil

def list_files(directory="."):
    try:
        return os.listdir(directory)
    except Exception as e:
        return [f"Error: {e}"]

def read_file(filepath):
    try:
        with open(filepath, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

def write_file(filepath, content):
    try:
        with open(filepath, "w") as f:
            f.write(content)
        return f"File '{filepath}' written successfully."
    except Exception as e:
        return f"Error: {e}"

def delete_file(filepath):
    try:
        os.remove(filepath)
        return f"File '{filepath}' deleted."
    except Exception as e:
        return f"Error: {e}"

def rename_file(old, new):
    try:
        os.rename(old, new)
        return f"Renamed '{old}' to '{new}'."
    except Exception as e:
        return f"Error: {e}"

def move_file(src, dst):
    try:
        shutil.move(src, dst)
        return f"Moved '{src}' to '{dst}'."
    except Exception as e:
        return f"Error: {e}"
