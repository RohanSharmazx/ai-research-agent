🤖 AI Research Agent

An AI-powered research assistant that takes a question, searches the web for relevant information, and turns the findings into a structured research report with sources.

I built this project to understand how AI agents work beyond simple chatbots — especially how multiple LLM-powered steps can work together to plan, search, write, evaluate, and improve research.

💡 What does it do?

You give the agent a research question such as:

What skills will be important for CSE students graduating in 2028?

The agent then:

🧠 Plans the research
🔍 Searches the web for relevant information
✍️ Writes a structured report
🔎 Evaluates the research
🔄 Performs additional research when needed
📚 Returns the sources used

The goal isn't simply to generate an answer. The goal is to create a small research workflow where the agent can decide whether the available research is sufficient or whether it needs to investigate further.

---

🏗️ How It Works

The application uses a LangGraph workflow to coordinate multiple stages of the research process.

                    User Question
                         │
                         ▼
                    🧠 Planner
                         │
                         ▼
                    🔍 Search
                         │
                         ▼
                    ✍️ Writer
                         │
                         ▼
                   🔎 Evaluator
                         │
                  ┌──────┴──────┐
                  │             │
             More Research   Satisfied
                  │             │
                  ▼             ▼
               Planner      Final Report
                  │
                  └──────► ...

The evaluator can send the workflow back to the Planner when more research is needed, allowing the agent to perform another research cycle before producing the final report.


### Research Flow

**Planner**

Breaks the user's question down and creates a search query.

**Search**

Searches the web and collects relevant results.

**Writer**

Uses the research results to generate a structured report.

**Evaluator**

Checks the generated research and determines whether another research iteration is required.

If more research is needed, the workflow goes back to the **Planner**.

---

## ✨ Features

* 🧠 Multi-step AI research workflow
* 🔍 Web search integration
* 🔄 Iterative research using an evaluator
* 📝 Structured AI-generated reports
* 📚 Source listing
* 📖 Markdown rendering
* ⚡ FastAPI backend
* 🌐 Web-based frontend
* ⏳ Loading state while research is running
* 📱 Responsive frontend design
* 🧩 Modular LangGraph architecture

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* LangGraph
* LangChain
* Pydantic
* Uvicorn

### AI & Research

* Large Language Model
* Web search
* LangGraph agent workflow

### Frontend

* HTML
* CSS
* JavaScript
* Marked.js

### Development

* VS Code
* Git
* GitHub

---

## 📁 Project Structure

```text
Research Agent/
│
├── main.py
├── graph.py
├── state.py
│
├── nodes/
│   ├── planner.py
│   ├── search.py
│   ├── writer.py
│   └── evaluator.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-research-agent.git
```

```bash
cd ai-research-agent
```

---

## 2. Create a virtual environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure your API keys

Create a `.env` file in the project directory.

```env
YOUR_API_KEY=your_api_key_here
```

Use the environment variable names expected by your implementation.


---

## 5. Start the application

From the directory containing `main.py`:

```bash
uvicorn main:app --reload
```

You should see something similar to:

```text
Uvicorn running on http://127.0.0.1:8000
```

Open the application in your browser:

```text
http://127.0.0.1:8000
```

---

# 🖥️ Using the Agent

Enter a question into the research box.

For example:

```text
What are the most important skills for AI engineers in 2028?
```

Then click:

**🔍 Research**

The agent will execute its research workflow and return:

* A structured report
* Analysis and findings
* Sources used during the research

---

# 📊 Example

### Question

```text
Why are quantum computers difficult to build?
```

### Workflow

```text
Question
   ↓
Planner
   ↓
Web Search
   ↓
Research Results
   ↓
Writer
   ↓
Evaluator
   ↓
Final Report
```

If the evaluator determines that more research is required:

```text
Evaluator
    ↓
More research needed
    ↓
Planner
    ↓
Search
    ↓
Writer
    ↓
Evaluator
```

---

# 🎯 Why I Built This

I wanted to understand how AI agents are actually built rather than only using existing AI applications.

While building this project, I worked with:

* LangGraph state management
* Agent workflows
* Conditional graph execution
* Web search
* LLM-based report generation
* Evaluation loops
* FastAPI APIs
* Frontend/backend integration
* Markdown rendering
* Async web application concepts

The project is also intentionally a work in progress. I'm using it to learn by building, testing, breaking, and improving the system.

---

# 🔮 Roadmap

The current version is a working **v1**.

There are several areas I plan to improve.

## Research Quality

* [ ] Better source credibility scoring
* [ ] Source deduplication
* [ ] Better citation formatting
* [ ] Claim verification
* [ ] Better handling of conflicting sources
* [ ] Primary-source prioritization

## Agent Improvements

* [ ] Better research planning
* [ ] Parallel web searches
* [ ] More reliable evaluator
* [ ] Faster research execution
* [ ] Better error handling
* [ ] Improved context management

## User Experience

* [ ] Real-time research progress
* [ ] Research history
* [ ] Better source previews
* [ ] Report export
* [ ] Improved mobile experience
* [ ] More polished UI

## Future Ideas

* [ ] Research history and saved reports
* [ ] Multiple research modes
* [ ] User authentication
* [ ] PDF report generation
* [ ] Source credibility indicators
* [ ] Citation verification

---

# ⚠️ Current Limitations

This is currently a learning/portfolio project and should **not** be treated as an authoritative source of truth.

The quality of the final report depends on:

* The quality of search results
* The quality of retrieved sources
* The LLM's interpretation of those sources
* The research workflow
* The evaluator's decisions

AI-generated research can still contain mistakes.

For important topics, always verify the final answer against the original sources provided by the agent.

---

# 🔐 Security

API keys and other sensitive information should never be committed to the repository.

Use environment variables:

```env
YOUR_API_KEY=your_api_key_here
```

and keep `.env` in `.gitignore`.

If you accidentally expose an API key on GitHub, **revoke/rotate it immediately**.

---

# 📌 Project Status

**Version:** `v1.0`

The core research workflow and web application are working.

Current capabilities include:

* Multi-agent research workflow
* Web search
* Report generation
* Research evaluation
* Source extraction
* FastAPI backend
* HTML/CSS/JavaScript frontend

The project is actively being improved, with future work focused mainly on **research quality, citations, source evaluation, performance, and user experience**.

---

# 🧠 What I Learned

Building this project helped me understand that an AI application isn't just an LLM call.

A useful AI system requires multiple pieces working together:

```text
User Interface
      ↓
API
      ↓
Agent Workflow
      ↓
Search / Tools
      ↓
LLM
      ↓
Evaluation
      ↓
Final Response
```

This project was my hands-on exploration of that architecture.

---

# 👨‍💻 About

Built as a hands-on project while learning:

**AI Agents → LangGraph → LLM Applications → FastAPI → Full-Stack AI Development**

I'm continuing to improve the project as I learn more about AI agents, retrieval, evaluation, and production AI systems.

---

# ⭐ Feedback

If you find the project interesting, feel free to explore the code and suggest improvements.

If you find it useful, consider giving the repository a ⭐.

---
