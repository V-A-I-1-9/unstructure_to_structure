import json


def is_text_empty(text: str) -> bool:
    """
    Checks if user input is empty or whitespace.
    """
    return not text or not text.strip()


def safe_json_load(text: str):
    """
    Safely attempts to load JSON from text.
    Returns dict if valid, else None.
    """
    try:
        return json.loads(text)
    except Exception:
        return None


def validate_required_keys(parsed_json: dict, required_keys: list) -> bool:
    """
    Checks if required keys exist in parsed JSON.
    """
    if not parsed_json:
        return False

    return all(key in parsed_json for key in required_keys)

def normalize_text(text: str) -> str:
    """
    Normalizes common Unicode characters to plain text.
    """
    if not text:
        return text

    replacements = {
        "\u2013": "-",  # en-dash
        "\u2014": "-",  # em-dash
        "\u2018": "'",  # left single quote
        "\u2019": "'",  # right single quote
        "\u201c": '"',  # left double quote
        "\u201d": '"',  # right double quote
    }

    for unicode_char, replacement in replacements.items():
        text = text.replace(unicode_char, replacement)

    return text
