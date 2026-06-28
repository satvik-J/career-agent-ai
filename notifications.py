"""
Notification utilities for the Personal AI Agent.
"""

import requests

from config import (
    PUSHOVER_TOKEN,
    PUSHOVER_URL,
    PUSHOVER_USER,
)


def push(message: str) -> None:
    """
    Sends a notification using the Pushover API.
    """

    print(f"Pushover Notification: {message}")

    payload = {
        "user": PUSHOVER_USER,
        "token": PUSHOVER_TOKEN,
        "message": message,
    }

    requests.post(
        PUSHOVER_URL,
        data=payload,
        timeout=10,
    )