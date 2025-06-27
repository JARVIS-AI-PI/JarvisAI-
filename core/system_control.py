import os
import subprocess
from core.guardian_mode import warn_if_risky

def run_command(text):
    warning = warn_if_risky(text)
    if warning:
        return warning

    try:
        output = subprocess.check_output(text, shell=True, stderr=subprocess.STDOUT, timeout=10)
        return output.decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        return f"❌ Error: {e.output.decode('utf-8')}"
    except Exception as ex:
        return f"⚠️ Exception: {str(ex)}"
