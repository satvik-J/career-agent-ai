"""
Tools available to the AI agent.
"""

import json

from notifications import push


def record_user_details(
    email: str,
    name: str = "Name not provided",
    notes: str = "Not provided",
) -> dict:
    """
    Records a potential contact and sends a notification.
    """

    push(
        f"New lead received!\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Notes: {notes}"
    )

    return {
        "status": "success",
        "message": "User details recorded successfully.",
    }


def record_unknown_question(question: str) -> dict:
    """
    Records a question the AI could not answer.
    """

    push(f"Unknown question received:\n{question}")

    return {
        "status": "success",
        "message": "Question recorded successfully.",
    }


record_user_details_schema = {
    "name": "record_user_details",
    "description": (
        "Record contact information when a user wants to get in touch."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "The user's email address.",
            },
            "name": {
                "type": "string",
                "description": "The user's name, if provided.",
            },
            "notes": {
                "type": "string",
                "description": (
                    "Additional notes about the conversation."
                ),
            },
        },
        "required": ["email"],
        "additionalProperties": False,
    },
}


record_unknown_question_schema = {
    "name": "record_unknown_question",
    "description": (
        "Record questions that the AI assistant could not answer."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": (
                    "The question the AI could not answer."
                ),
            },
        },
        "required": ["question"],
        "additionalProperties": False,
    },
}


TOOLS = [
    {
        "type": "function",
        "function": record_user_details_schema,
    },
    {
        "type": "function",
        "function": record_unknown_question_schema,
    },
]
TOOL_FUNCTIONS = {
    "record_user_details": record_user_details,
    "record_unknown_question": record_unknown_question,
}

def handle_tool_calls(tool_calls: list) -> list:
    """
    Executes tool calls requested by the LLM.
    """

    results = []

    for tool_call in tool_calls:

        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print(f"Executing tool: {tool_name}")

        tool = TOOL_FUNCTIONS.get(tool_name)

        if tool:
            result = tool(**arguments)
        else:
            result = {
                "status": "error",
                "message": f"Unknown tool: {tool_name}",
            }

        results.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result),
            }
        )

    return results