import os
import shutil
import subprocess

EXCLUDE = ["config.json", "learn_data.json"]
VALID_EXTENSIONS = [".py", ".json", ".js", ".css"]

def update_from_github(repo_url="https://github.com/YOUR_USERNAME/JarvisAI.git", branch="main"):
    try:
        print("📦 Cloning latest version from GitHub...")
        if os.path.exists("update_tmp"):
            shutil.rmtree("update_tmp")
        subprocess.run(["git", "clone", "-b", branch, repo_url, "update_tmp"], check=True)

        apply_updates("update_tmp")
        shutil.rmtree("update_tmp")
        return "✅ Jarvis updated from GitHub."
    except Exception as e:
        return f"❌ Update failed: {e}"

def update_from_local(folder_path):
    if not os.path.exists(folder_path):
        return "❌ Local folder not found."

    try:
        apply_updates(folder_path)
        return "✅ Jarvis updated from local folder."
    except Exception as e:
        return f"❌ Local update failed: {e}"

def apply_updates(source_dir):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if any(file.endswith(ext) for ext in VALID_EXTENSIONS) and file not in EXCLUDE:
                src = os.path.join(root, file)
                rel_path = os.path.relpath(src, source_dir)
                dst = os.path.join(os.getcwd(), rel_path)

                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
                print(f"🔁 Updated: {rel_path}")
