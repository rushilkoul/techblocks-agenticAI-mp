from google.adk.agents import Agent
import os

BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "RoadMap_generator.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    roadmap_instructions = f.read()

RoadMap_generator = Agent(
    name="RoadMap_generator",
    model="gemini-2.0-flash",
    description="Generates a step-by-step roadmap for implementing the user’s hackathon project.",
    instruction=roadmap_instructions,
)
