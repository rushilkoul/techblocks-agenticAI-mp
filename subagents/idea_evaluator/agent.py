from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
import os
# === Load manager instructions (optional) ===
# BASE_DIR = os.path.dirname(__file__)
# TXT_PATH = os.path.join(BASE_DIR, "theme_analyser.txt")

# with open(TXT_PATH, "r", encoding="utf-8") as f:
#     instructions = f.read()


idea_evaluator_instructions = """
Your role is to critically evaluate an analyzed hackathon idea based on a defined set of criteria.
You will receive a structured breakdown of an idea. Your task is to score it and provide a final verdict.

Use the following criteria for your evaluation, scoring each from 1 (poor) to 10 (excellent):
1.  **Innovation & Originality:** How unique or novel is this concept?
2.  **Technical Feasibility:** How practical is it to build a working prototype during the hackathon?
3.  **Impact & Value:** How significant is the problem it solves and how valuable is the proposed solution?
4.  **Theme Alignment:** How well does the idea align with the hackathon's central theme?

After scoring, provide a summary of the idea's main strengths and weaknesses.
Conclude with a single, clear recommendation: 'PROCEED', 'REVISE', or 'REJECT'.
"""

# === Break Instruction for the loop ===
idea_evaluator_break_instruction = "If the final recommendation is 'PROCEED' or 'REJECT', the evaluation is complete and the goal is met. Stop the loop."


# === Agent Definition: idea_evaluator ===
idea_evaluator = Agent(
    name="idea_evaluator",
    model="gemini-2.0-flash",
    description="Evaluates analyzed hackathon ideas based on innovation, feasibility, and impact.",
    instruction=idea_evaluator_instructions,
   
)