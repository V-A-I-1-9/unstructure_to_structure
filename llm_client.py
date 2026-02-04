import os
from groq import Groq

# Initialize Groq client safely
def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found. Please set it in environment or secrets.")

    return Groq(api_key=api_key)


def run_llm(system_prompt: str, user_input: str, temperature: float = 0.0) -> str:
    """
    Sends a prompt to Groq LLM and returns the raw response text.
    """
    client = get_groq_client()

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content.strip()
