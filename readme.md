

# Hackmate  
### Your AI-Powered Multi-Agent Hackathon Assistant 🚀  

![Hackathon](https://img.shields.io/badge/Event-IEEE%20Techblocks%2011.1-blue.svg)  
![Framework](https://img.shields.io/badge/Framework-Google%20ADK-orange.svg)  
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)  

Hackmate is a **multi-agent AI system** built with the Google Agent Development Kit (ADK) to supercharge your hackathon workflow.  
It automates the **entire pre-development lifecycle** — from analyzing the theme and brainstorming innovative ideas to drafting a project roadmap and generating a full presentation deck.  

Instead of spending hours on planning and slides, let Hackmate’s AI agents handle it while you focus on **building and coding your solution.** 💻🔥  

---

## ⚡ Getting Started  

Follow these steps to set up and run Hackmate on your local machine.  

### ✅ Prerequisites  
- **Python** (3.9 or higher)  
- **Git** (for cloning) *or* you can download the project ZIP from GitHub  

---

### 📥 Step 1: Get the Code  

You have **two options**:  

**Option A – Clone with Git:**  
```sh
git clone https://github.com/your-username/hackmate.git
cd hackmate

Option B – Download ZIP:

Go to the GitHub repository.

Click on Code → Download ZIP.

Extract the ZIP and open the folder in your terminal:


cd hackmate


---

🛠️ Step 2: Create and Activate a Virtual Environment

It’s best practice to use a virtual environment to isolate dependencies.

For macOS / Linux:

python3 -m venv venv
source venv/bin/activate

For Windows:

python -m venv venv
.\venv\Scripts\activate

If successful, your terminal will show (venv) at the beginning of the line.


---

📦 Step 3: Install Dependencies

Install all required Python libraries from requirements.txt:

pip install -r requirements.txt


---

🔑 Step 4: Configure Environment Variables

1. Create a new file named .env in the project root.


2. Copy contents from .env.example (if available) or add your own.



Example:

# .env file
API_KEY="YOUR_SECRET_API_KEY_HERE"


---

🚀 Step 5: Launch Hackmate

Run the following command to start Hackmate:

adk web

Open your browser at the URL provided (usually http://127.0.0.1:8080) to start using Hackmate! 🎉


---

🤖 System Architecture & Agents

Hackmate uses a multi-agent architecture with a central Manager Agent that coordinates everything.


---

🧠 Manager Agent

Acts as the brain of Hackmate.

Interprets the user’s request.

Maintains the project state.

Delegates tasks to specialized agents.



---

🔍 Phase 1: Ideation & Analysis (Sequential)

1. Theme Analyzer

Deeply analyzes the hackathon theme.

Identifies concepts, user personas, pain points, existing solutions, and ethical considerations.



2. Idea Forge (loop with two sub-agents):

Idea Analyzer: Generates diverse and creative ideas.

Idea Evaluator: Scores ideas based on feasibility, innovation, and impact.

Provides a ranked shortlist of best ideas.





---

🏗️ Phase 2: Planning & Presentation (Parallel Execution)

Once you select an idea, two agents start working in parallel:

Drafter Agent

Creates your development roadmap.

Outputs include:

✅ Tech stack suggestions

✅ Feature breakdown

✅ Milestones & timelines

✅ API/data source recommendations



PPT Head Agent

Supervises 8 parallel worker agents (ppt_worker_1 … ppt_worker_8).

Each worker creates one part of a standard hackathon pitch deck.

Final output = a complete presentation deck.


Slide Outputs:

Title, team, tagline

Problem statement & impact

Proposed solution & features

Technical architecture

Market analysis & audience

Business/monetization model

Scalability & future scope

Visuals & demo flow



---

🗂️ Text-Based Flowchart

Here’s how Hackmate’s flow looks in text format:

User Input (Hackathon Theme)
        │
        ▼
 Manager Agent
        │
        ├── Phase 1 (Sequential)
        │       ├── Theme Analyzer
        │       ▼
        │   Idea Forge (loop)
        │       ├── Idea Analyzer
        │       └── Idea Evaluator
        │
        └── Phase 2 (Parallel)
                ├── Drafter Agent ──► Roadmap, Tech Stack, Milestones
                └── PPT Head Agent ─► Supervises 8 Workers ─► Full Presentation


---

🎯 Why Hackmate?

⏱️ Save time on planning and slides

🤝 Collaborate smarter with AI-generated roadmaps

⚡ Accelerate innovation with fast idea iteration

📊 Pitch-ready decks created in minutes



---

📌 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Bhai ab seedha isko `README.md` me daal aur tera project ekdum **pro level hackathon ready** lagega 🚀🔥  

Chaahta hai main ek **“Demo” section** bhi dal dun (jisme tu GIF/screenshot add karega) taaki aur attractive lage?

