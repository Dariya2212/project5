import json


def load_transactions(json_path):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            operations = json.load(f)
    except (json.JSONDecodeError, TypeError, KeyError, ValueError):
        return []
    return operations
