"""Configuration and environment setup for the Job Application Crew.

LLM     : Groq  — llama3-70b-8192  (via langchain_groq / CrewAI LLM wrapper)
Search  : Tavily
Scraping: ScrapeWebsiteTool
"""

import os
import warnings
from dotenv import load_dotenv
from langchain_groq import ChatGroq

warnings.filterwarnings("ignore")
load_dotenv()


def validate_env():
    """Validate that all required environment variables are present."""
    required_keys = ["GROQ_API_KEY", "TAVILY_API_KEY"]
    missing = [k for k in required_keys if not os.getenv(k)]
    if missing:
        raise EnvironmentError(
            f"Missing required environment variables: {missing}\n"
            "Please copy .env.example to .env and fill in your API keys."
        )


# ── LLM ──────────────────────────────────────────────────────────────────────
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

# Shared LLM instance — imported by agents
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=GROQ_MODEL,
    temperature=0.3,
)

# ── Search ────────────────────────────────────────────────────────────────────
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY", "")

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
RESUME_PATH = os.path.join(DATA_DIR, "sample_resume.md")

os.makedirs(OUTPUT_DIR, exist_ok=True)
