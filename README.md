# 🤖 Job Application Crew AI

A production-grade **multi-agent AI system** built with [CrewAI](https://github.com/joaomdmoura/crewAI) that automates the end-to-end job application tailoring process. Four specialized AI agents collaborate to analyze job postings, build candidate profiles, optimize resumes, and generate targeted interview preparation materials.

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
│   └── custom_tools.py        # CrewAI tool wrappers
├── outputs/                   # Generated artifacts (gitignored)
├── data/
│   └── sample_resume.md       # Sample resume input file
├── crew.py                    # Crew orchestration entry point
├── main.py                    # CLI runner
├── config.py                  # Configuration and environment setup
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🤖 Agents

| Agent | Role | Tools |
|-------|------|-------|
| **Researcher** | Extracts key skills & qualifications from job postings | SerperDev, ScrapeWebsite |
| **Profiler** | Builds a comprehensive candidate profile | SerperDev, ScrapeWebsite, FileRead, MDXSearch |
| **Resume Strategist** | Tailors resume to match job requirements | SerperDev, ScrapeWebsite, FileRead, MDXSearch |
| **Interview Preparer** | Generates interview questions & talking points | SerperDev, ScrapeWebsite, FileRead, MDXSearch |

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
# Fill in your API keys in .env
```

### 5. Add your resume
Replace `data/sample_resume.md` with your own resume in Markdown format.

### 6. Run the crew
```bash
python main.py \
  --job-url "https://jobs.example.com/posting" \
  --github-url "https://github.com/your-username" \
  --writeup "Brief personal summary about yourself"
```

Outputs are saved to `outputs/tailored_resume.md` and `outputs/interview_materials.md`.

---

## 🔑 Environment Variables

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL_NAME=gpt-4-turbo
SERPER_API_KEY=your_serper_api_key
```

> **Tip:** You can swap OpenAI for Google Gemini by updating `config.py` to use `langchain_google_genai`.

---

## 📦 Tech Stack

- **[CrewAI](https://github.com/joaomdmoura/crewAI)** — Multi-agent orchestration framework
- **[LangChain Community](https://github.com/langchain-ai/langchain)** — LLM tooling & integrations
- **SerperDev API** — Real-time web search
- **ScrapeWebsite Tool** — Job posting content extraction
- **MDXSearch Tool** — Semantic resume search
- **Python-dotenv** — Environment configuration

---

## 📁 Output Files

| File | Description |
|------|-------------|
| `outputs/tailored_resume.md` | Resume optimized for the target job posting |
| `outputs/interview_materials.md` | Interview questions & talking points |

---

## 🧩 Extending the Project

- **Swap LLM**: Edit `config.py` to use Gemini, Claude, or any LangChain-compatible model
- **Add agents**: Create a new file in `agents/` and register in `crew.py`
- **Add tasks**: Create a new file in `tasks/` and add to the Crew task list
- **Custom tools**: Extend `tools/custom_tools.py` with new CrewAI tools

---

## 🙋 Author

**Koushik Samudrala** — [GitHub](https://github.com/KoushikSamudrala)

Built as part of an ongoing portfolio in **Generative AI**, **Multi-Agent Systems**, and **LLM-based Automation**.
