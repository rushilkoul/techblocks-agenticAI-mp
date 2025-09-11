from google.adk.agents import Agent,ParallelAgent,LoopAgent,llm_agent
from subagents.idea_analyzer.agent import idea_analyzer
from subagents.idea_evaluator.agent import  idea_evaluator

from subagents.theme_analyser.agent import theme_analyser
from subagents.drafter.agent import drafter


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

# # === Load manager instructions (optional) ===
# BASE_DIR = os.path.dirname(__file__)
# TXT_PATH = os.path.join(BASE_DIR, "manager.txt")

# with open(TXT_PATH, "r", encoding="utf-8") as f:
#     manager_instructions = f.read()


# root_agent = Agent(
#     name="Hack_Mate",
#     model="gemini-2.0-flash",
#     description="You are The manager of a hackathon  helping agent your task is to simple help to choose right agent and switch between agents ",
#     instruction=manager_instructions,
#     # sub_agents=[
#     #     theme_analyser,
#     #     LoopAgent(
#     #         name="Idea_forge",
#     #         description="Loop to suggest or refine ideas , output will be list of possible ideas with a brief explanation and techstack.",
#     #         sub_agents=[idea_analyzer,idea_evaluator],
#     #         max_iterations=2,
#     #     ),
#     #     drafter
#     # ]
    
    
# )


root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - stock_analyst
    - funny_nerd

    You also have access to the following tools:
    - news_analyst
    - get_current_time
    """,
    # sub_agents=[stock_analyst, funny_nerd,Weather_agent,Movie_agent],
    # tools=[
    #     AgentTool(news_analyst),
    #     get_current_time,
    # ],
    
)