"""
LLM-based evaluation models and functions.
"""

from pydantic import BaseModel

from config import client
from prompts import PERSONA_NAME


class Evaluation(BaseModel):
    """
    Represents the evaluation result of an AI response.
    """

    is_acceptable: bool
    feedback: str


def build_evaluator_prompt(
    career_summary: str,
    linkedin_profile: str
) -> str:
    """
    Builds the system prompt for the response evaluator.
    """

    return f"""
You are an AI quality evaluator.

Your task is to determine whether the AI assistant's latest response is appropriate and accurate.

The assistant represents {PERSONA_NAME} on a personal portfolio website.

Evaluation Guidelines:
- Ensure the response is factually consistent with the supplied information.
- Ensure the response is professional and engaging.
- Reject responses that invent information.
- Reject responses that are misleading or inaccurate.
- If the answer appropriately admits missing information, consider that acceptable.

## Career Summary

{career_summary}

## LinkedIn Profile

{linkedin_profile}
"""


def build_evaluator_user_prompt(
    reply: str,
    message: str,
    history: list,
) -> str:
    """
    Creates the prompt containing the conversation
    for the evaluator model.
    """

    return f"""
Conversation History

{history}

Latest User Message

{message}

Latest Assistant Response

{reply}

Evaluate whether the assistant's latest response is acceptable.
Return whether it is acceptable and provide feedback.
"""


def evaluate(
    reply: str,
    message: str,
    history: list,
    career_summary: str,
    linkedin_profile: str,
) -> Evaluation:
    """
    Evaluates whether the AI response is acceptable.
    """

    system_prompt = build_evaluator_prompt(
        career_summary,
        linkedin_profile,
    )

    user_prompt = build_evaluator_user_prompt(
        reply,
        message,
        history,
    )

    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        response_format=Evaluation,
    )

    return response.choices[0].message.parsed