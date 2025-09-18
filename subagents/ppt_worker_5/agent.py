from google.adk.agents import Agent
import os
from .tools.ppt_tool import add_slide
BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "ppt_worker_5.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    worker_instructions = f.read()

ppt_worker_5 = Agent(
    name="ppt_worker_5",
    model="gemini-2.0-flash",
    description="Generates business model slide.",
    instruction=worker_instructions,
    tools=[add_slide]
)
