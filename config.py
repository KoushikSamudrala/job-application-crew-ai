"""Configuration and environment setup for the Job Application Crew."""

import os
import warnings
from dotenv import load_dotenv

warnings.filterwarnings("ignore")
load_dotenv()


def validate_env():
    """Validate required environment variables are set."""
    required_keys = ["OPENAI_API_KEY", "SERPER_API_KEY"]
    missing = [k for k in required_keys if not os.getenv(k)]
    if missing:
        raise EnvironmentError(
            f"Missing required environment variables: {missing}\n"
            "Please copy .env.example to .env and fill in your API keys."
        )


# Model config — swap to Gemini or Claude here if needed
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME", "gpt-4-turbo")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY", "")

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
RESUME_PATH = os.path.join(DATA_DIR, "sample_resume.md")

os.makedirs(OUTPUT_DIR, exist_ok=True)
