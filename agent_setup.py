# agent_setup.py
import os
from dotenv import load_dotenv
from langchain.agents import create_react_agent, AgentExecutor
from langchain.chat_models import init_chat_model
from tools import tools
from prompt_template import prompt

# Load environment variables
load_dotenv()

# Initialize model
llm = init_chat_model("google_genai:gemini-2.0-flash")

# Create agent
custom_agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# Create executor
agent_executor = AgentExecutor(
    agent=custom_agent,
    tools=tools,
    verbose=False,
    handle_parsing_errors=False
)

def run_agent(query: str):
    """Run the custom calculator agent."""
    try:
        result = agent_executor.invoke({"input": query})
        return result["output"]
    except Exception as e:
        return f"Error: {e}"


# while True:
#     user_ques = input("Enter: ")
#     if user_ques.lower() in ["exit", "quit"]:
#         break
#     print("AI:", run_agent(user_ques))

