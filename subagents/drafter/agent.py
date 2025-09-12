from google.adk.agents import Agent, ParallelAgent
import os

# === Load drafter instructions ===
BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "drafter.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    drafter_instructions = f.read()

# Import sub-agents
from subagents.RoadMap_generator.agent import RoadMap_generator
from subagents.ppt_head.agent import ppt_head

# === Drafter Agent ===
drafter = ParallelAgent(
    name="drafter",
    # model="gemini-2.0-flash",
    description="""
    Drafter agent documents the user’s idea into actionable formats.
    It runs parallel agents to generate:
    - A roadmap of the project
    - A draft PowerPoint presentation structure
    """,
    # instruction=drafter_instructions,
    sub_agents=[
        RoadMap_generator,
        ppt_head
    ]
)
