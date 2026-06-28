import gradio as gr

from agent import PersonalAgent

agent = PersonalAgent()

demo = gr.ChatInterface(
    fn=agent.chat,
    type="messages",
    title="CareerAgent_AI",
    description="Ask me about my education, projects, skills and experience."
)

demo.launch()