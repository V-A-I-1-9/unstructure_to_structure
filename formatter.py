import json


def try_parse_json(text: str):
    """
    Safely tries to parse JSON from LLM output.
    Returns dict if successful, else None.
    """
    try:
        return json.loads(text)
    except Exception:
        return None


def format_as_pretty_json(text: str) -> str:
    parsed = try_parse_json(text)
    if parsed:
        return json.dumps(parsed, indent=2)
    return text


def format_as_bullets(text: str) -> str:
    parsed = try_parse_json(text)

    if not parsed:
        return text

    bullets = []
    for key, value in parsed.items():
        if isinstance(value, list):
            bullets.append(f"{key}:")
            for item in value:
                if isinstance(item, dict):
                    bullets.append(f"  - " + ", ".join(f"{k}: {v}" for k, v in item.items()))
                else:
                    bullets.append(f"  - {item}")
        else:
            bullets.append(f"{key}: {value}")

    return "\n".join(bullets)


def format_as_markdown(text: str) -> str:
    parsed = try_parse_json(text)

    if not parsed:
        return text

    md = []
    for key, value in parsed.items():
        md.append(f"## {key.replace('_', ' ').title()}")
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    md.append("- " + ", ".join(f"**{k}**: {v}" for k, v in item.items()))
                else:
                    md.append(f"- {item}")
        else:
            md.append(str(value))

    return "\n".join(md)


def format_output(text: str, output_format: str) -> str:
    """
    Main formatter dispatcher.
    """
    output_format = output_format.lower()

    if output_format == "json":
        return format_as_pretty_json(text)

    if output_format == "bullet points":
        return format_as_bullets(text)

    if output_format == "markdown":
        return format_as_markdown(text)

    return text
