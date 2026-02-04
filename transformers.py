from llm_client import run_llm
from utils import normalize_text
from prompts import (
    ACTION_PLAN_PROMPT,
    PROJECT_BLUEPRINT_PROMPT,
    CHECKLIST_PROMPT,
    MULTI_FORMAT_PROMPT
)


# Messy Text → Action Plan
def generate_action_plan(user_text: str) -> str:
    output = run_llm(
        system_prompt=ACTION_PLAN_PROMPT,
        user_input=user_text,
        temperature=0.0
    )
    return normalize_text(output)

# Problem Statement → Project Blueprint
def generate_project_blueprint(problem_text: str) -> str:
    output = run_llm(
        system_prompt=PROJECT_BLUEPRINT_PROMPT,
        user_input=problem_text,
        temperature=0.0
    )
    return normalize_text(output)

# Requirements → Checklist Generator
def generate_checklist(requirements_text: str) -> str:
    output = run_llm(
        system_prompt=CHECKLIST_PROMPT,
        user_input=requirements_text,
        temperature=0.0
    )
    return normalize_text(output)

# Text → Multiple Formats
def generate_formatted_output(user_text: str, output_format: str) -> str:
    formatted_input = f"""
Text:
{user_text}

Format:
{output_format}
"""
    output = run_llm(
        system_prompt=MULTI_FORMAT_PROMPT,
        user_input=formatted_input,
        temperature=0.0
    )
    return normalize_text(output)
