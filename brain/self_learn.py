import json
import os

LEARN_DB = "brain/learned.json"

if not os.path.exists(LEARN_DB):
    with open(LEARN_DB, "w") as f:
        json.dump({}, f)

def learn(question, answer):
    with open(LEARN_DB, "r") as f:
        data = json.load(f)
    data[question.lower()] = answer
    with open(LEARN_DB, "w") as f:
        json.dump(data, f, indent=2)

def try_learned(question):
    with open(LEARN_DB, "r") as f:
        data = json.load(f)
    return data.get(question.lower(), None)
