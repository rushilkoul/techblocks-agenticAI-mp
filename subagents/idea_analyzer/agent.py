from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
import os
# === Load manager instructions (optional) ===
# BASE_DIR = os.path.dirname(__file__)
# TXT_PATH = os.path.join(BASE_DIR, "theme_analyser.txt")

# with open(TXT_PATH, "r", encoding="utf-8") as f:
#     instructions = f.read()

# === Instructions for the Idea Analyzer ===
idea_analyzer_instructions = """
Your primary role is to dissect and analyze a given hackathon idea.
You must not evaluate or judge the idea's quality. Your task is to simply break it down into its constituent parts for the evaluator.

Follow these steps meticulously:
1.  **Problem Statement:** Clearly identify and articulate the core problem the idea intends to solve.
2.  **Proposed Solution:** Describe the main functionality of the proposed solution.
3.  **Target Audience:** Define who the intended users or beneficiaries of this solution are.
4.  **Key Features:** List the 3-5 most critical features required for a minimum viable product (MVP).
5.  **Technical Stack (Optional):** If mentioned, list the potential technologies (languages, frameworks, APIs).

Present your final analysis in a structured, easy-to-read markdown format.
"""


idea_analyzer = Agent(
    name="idea_analyzer",
    model="gemini-2.0-flash",
    description="Analyzes and breaks down hackathon ideas into their core components like problem, solution, and features.",
    instruction=idea_analyzer_instructions,
    output_key="idea"
    
)