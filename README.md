# 🤖 Job Application Crew AI

A production-grade **multi-agent AI system** built with [CrewAI](https://github.com/joaomdmoura/crewAI) that automates the end-to-end job application tailoring process. Four specialized AI agents collaborate to analyze job postings, build candidate profiles, optimize resumes, and generate targeted interview preparation materials.

> **Stack:** Groq `llama3-70b-8192` · Tavily Search · CrewAI · LangChain

---

## 🧠 Architecture Overview

```
job-application-crew-ai/
├── agents/
│   ├── researcher.py          # Tech Job Researcher agent
│   ├── profiler.py            # Personal Profiler agent
│   ├── resume_strategist.py   # Resume Strategist agent
│   └── interview_preparer.py  # Interview Preparer agent
├── tasks/
│   ├── research_task.py       # Job posting analysis task
│   ├── profile_task.py        # Candidate profiling task
│   ├── resume_strategy_task.py# Resume tailoring task
│   └── interview_prep_task.py # Interview materials task
├── tools/
│   └── custom_tools.py        # Tavily search + scrape + resume tools
├── outputs/                   # Generated artifacts (gitignored)
├── data/
│   └── sample_resume.md       # Candidate resume input
├── crew.py                    # Crew orchestration entry point
├── main.py                    # CLI runner
├── config.py                  # LLM + env + path configuration
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🤖 Agents

| Agent | Role | Tools |
|-------|------|-------|
| **Researcher** | Extracts key skills & qualifications from job postings | Tavily, ScrapeWebsite |
| **Profiler** | Builds a comprehensive candidate profile | Tavily, ScrapeWebsite, FileRead, MDXSearch |
| **Resume Strategist** | Tailors resume to match job requirements | Tavily, ScrapeWebsite, FileRead, MDXSearch |
| **Interview Preparer** | Generates interview questions & talking points | Tavily, ScrapeWebsite, FileRead, MDXSearch |

---

## ⚙️ Task Flow

```
[research_task] ──┐
                  ├──▶ [resume_strategy_task] ──▶ [interview_prep_task]
[profile_task]  ──┘
```

`research_task` and `profile_task` run in **parallel** (async). Their outputs feed sequentially into the resume and interview tasks.

---

## 🚀 Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/KoushikSamudrala/job-application-crew-ai.git
cd job-application-crew-ai
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
cp .env.example .env
# Fill in your GROQ_API_KEY and TAVILY_API_KEY
```

| Variable | Source | Notes |
|----------|--------|-------|
| `GROQ_API_KEY` | [console.groq.com](https://console.groq.com) | Free tier available |
| `GROQ_MODEL` | — | Defaults to `llama3-70b-8192` |
| `TAVILY_API_KEY` | [app.tavily.com](https://app.tavily.com) | Free tier available |

### 5. Add your resume
Replace `data/sample_resume.md` with your own resume in Markdown format.

### 6. Run the crew
```bash
python main.py \
  --job-url "https://jobs.example.com/posting" \
  --github-url "https://github.com/KoushikSamudrala" \
  --writeup "Brief personal summary about yourself"
```

Outputs are saved to `outputs/tailored_resume.md` and `outputs/interview_materials.md`.

---

## 📦 Tech Stack

| Component | Library / Service |
|-----------|------------------|
| Multi-agent orchestration | [CrewAI](https://github.com/joaomdmoura/crewAI) `0.28.8` |
| LLM | [Groq](https://groq.com) — `llama3-70b-8192` |
| LLM integration | `langchain_groq` |
| Web search | [Tavily](https://tavily.com) via `TavilySearchResults` |
| Web scraping | `ScrapeWebsiteTool` (crewai_tools) |
| Resume tools | `FileReadTool`, `MDXSearchTool` (crewai_tools) |
| Config management | `python-dotenv` |

---

## 📁 Output Files

| File | Description |
|------|-------------|
| `outputs/tailored_resume.md` | Resume optimized for the target job posting |
| `outputs/interview_materials.md` | Interview questions & talking points |

---

## 🧩 Extending the Project

- **Swap LLM**: Edit `config.py` — change `ChatGroq` to `ChatGoogleGenerativeAI` (Gemini) or `ChatOpenAI`
- **Change Groq model**: Set `GROQ_MODEL=mixtral-8x7b-32768` (or any Groq-supported model) in `.env`
- **Add agents**: Create a new file in `agents/` and register in `crew.py`
- **Add tasks**: Create a new file in `tasks/` and add to the Crew task list
- **Custom tools**: Extend `tools/custom_tools.py` with new CrewAI tools

---

## 🙋 Author

**Koushik Samudrala** — [GitHub](https://github.com/KoushikSamudrala)

Built as part of an ongoing portfolio in **Generative AI**, **Multi-Agent Systems**, and **LLM-based Automation**.
