"""
Core AI agent responsible for handling conversations.
"""

from config import client
from knowledge import load_linkedin_profile, load_summary
from prompts import build_system_prompt
from evaluator import evaluate
from tools import TOOLS, handle_tool_calls


class PersonalAgent:
    """
    AI agent responsible for answering questions
    about the portfolio owner.
    """

    def __init__(self):
        # Load knowledge
        self.career_summary = load_summary("data/summary.txt")
        self.linkedin_profile = load_linkedin_profile("data/linkedin.pdf")

        # Build system prompt
        self.system_prompt = build_system_prompt(
            self.career_summary,
            self.linkedin_profile,
        )

    def chat(
        self,
        message: str,
        history: list,
    ) -> str:
        """
        Handles the conversation with the user,
        including OpenAI tool calling and response evaluation.
        """

        messages = (
            [{"role": "system", "content": self.system_prompt}]
            + history
            + [{"role": "user", "content": message}]
        )

        while True:

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                tools=TOOLS,
            )
            print(response.choices[0].finish_reason)
            print(response.choices[0].message.tool_calls)

            assistant_message = response.choices[0].message

            # -----------------------------
            # Handle Tool Calls
            # -----------------------------
            if assistant_message.tool_calls:

                messages.append(assistant_message)

                tool_results = handle_tool_calls(
                    assistant_message.tool_calls
                )

                messages.extend(tool_results)

                continue

            reply = assistant_message.content

            # -----------------------------
            # Evaluate the reply
            # -----------------------------
            evaluation = evaluate(
                reply=reply,
                message=message,
                history=history,
                career_summary=self.career_summary,
                linkedin_profile=self.linkedin_profile,
            )

            if evaluation.is_acceptable:
                return reply

            return self.rerun(
                reply,
                message,
                history,
                evaluation.feedback,
            )

    def rerun(
        self,
        reply: str,
        message: str,
        history: list,
        feedback: str,
    ) -> str:
        """
        Regenerates a response after evaluation failure.
        """

        retry_prompt = self.system_prompt
        retry_prompt += "\n\n## Previous response rejected\n"
        retry_prompt += f"\nRejected response:\n{reply}\n"
        retry_prompt += f"\nEvaluator feedback:\n{feedback}\n"

        messages = (
            [{"role": "system", "content": retry_prompt}]
            + history
            + [{"role": "user", "content": message}]
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )

        return response.choices[0].message.content