import json
import os

THEME_FILE = "ui/theme.json"

default_themes = {
    "dark": {
        "bg": "#000000",
        "fg": "#00FF00",
        "font": "Consolas"
    },
    "light": {
        "bg": "#FFFFFF",
        "fg": "#000000",
        "font": "Consolas"
    },
    "hacker": {
        "bg": "#101010",
        "fg": "#00FF00",
        "font": "Courier"
    }
}

def load_theme():
    if not os.path.exists(THEME_FILE):
        save_theme("dark")
    with open(THEME_FILE, "r") as f:
        return json.load(f)

def save_theme(name):
    if name not in default_themes:
        name = "dark"
    with open(THEME_FILE, "w") as f:
        json.dump(default_themes[name], f)

def apply_theme(widget, theme):
    widget.configure(bg=theme["bg"], fg=theme["fg"], font=(theme["font"], 12))
