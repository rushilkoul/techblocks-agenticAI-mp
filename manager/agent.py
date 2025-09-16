from google.adk.agents import Agent,LoopAgent
from subagents.idea_analyzer.agent import idea_analyzer
from subagents.idea_evaluator.agent import  idea_evaluator

from subagents.theme_analyser.agent import theme_analyser
from subagents.drafter.agent import drafter
import os

# from subagents.ppt_head.agent import ppt_head
# from subagents.RoadMap_generator.agent import RoadMap_generator
# from subagents.ppt_worker_1.agent import ppt_worker_1
# from subagents.ppt_worker_2.agent import ppt_worker_2
# from subagents.ppt_worker_3.agent import ppt_worker_3
# from subagents.ppt_worker_4.agent import ppt_worker_4
# from subagents.ppt_worker_5.agent import ppt_worker_5
# from subagents.ppt_worker_6.agent import ppt_worker_6
# from subagents.ppt_worker_7.agent import ppt_worker_7
# from subagents.ppt_worker_8.agent import ppt_worker_8

# === Load manager instructions (optional) ===
BASE_DIR = os.path.dirname(__file__)
TXT_PATH = os.path.join(BASE_DIR, "manager.txt")

with open(TXT_PATH, "r", encoding="utf-8") as f:
    manager_instructions = f.read()

# from google.adk.agents import Agent

# logo_gen = Agent(
#     name="logo_gen",
#     model="gemini-2.5-flash-image-preview",
#     description="Generates creative hackathon/project logos from user descriptions.",
#     instruction="""
#     You are the **Logo Generator Agent**.

#     Your task:
#     - Take the user's description of a project, hackathon, or theme.
#     - Convert it into a clear, concise, and visually appealing logo design prompt.
#     - Use the image generation model to produce a professional-looking logo.
#     - Focus on clarity, simplicity, and aesthetics suitable for hackathon branding.

#     Always return:
#     1. A short explanation of the logo concept.
#     2. The generated logo image.
#     """,
# )

root_agent = Agent(
    
    name="Hack_Mate",
    model="gemini-2.0-flash",
    description="""
    You are **Hackmate**, the manager of the Hackathon Helper Assistant, built at IEEE TechBlocks 11.1.  
Your role is to oversee and coordinate the specialized sub-agents to help participants during hackathons.  
analyse user prompt and user transfer to agent only if needed 
"""
,
    instruction=manager_instructions,
    sub_agents=[
        theme_analyser,
        # logo_gen,
        LoopAgent(
            name="Idea_forge",
            description="Loop to suggest or refine ideas , output will be list of possible ideas with a brief explanation and techstack.",
            sub_agents=[idea_analyzer,idea_evaluator],
            max_iterations=2,
        ),
        drafter
    ]
    
    
)

