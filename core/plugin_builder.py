import os

PLUGIN_DIR = "plugins"

def create_plugin(name, trigger_phrase, response_text):
    plugin_name = name.lower().replace(" ", "_")
    filename = f"{plugin_name}.py"
    filepath = os.path.join(PLUGIN_DIR, filename)

    if os.path.exists(filepath):
        return f"A plugin named '{plugin_name}' already exists."

    plugin_code = f'''
def can_handle(text):
    return "{trigger_phrase.lower()}" in text.lower()

def handle(text, config):
    return "{response_text}"
'''

    try:
        with open(filepath, "w") as f:
            f.write(plugin_code.strip())
        return f"Plugin '{plugin_name}' created successfully."
    except Exception as e:
        return f"Error creating plugin: {e}"
