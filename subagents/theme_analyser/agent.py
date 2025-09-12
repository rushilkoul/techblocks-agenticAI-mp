from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
import os
# === Load manager instructions (optional) ===
BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "theme_analyser.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    instructions = f.read()

theme_analyser = Agent(
    name="theme_analyser",
    model="gemini-2.0-flash",
    description="Analyzes hackathon themes and ensures they are relevant, engaging, and impactful.",
    instruction= instructions
    
)
