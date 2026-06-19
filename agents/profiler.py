"""Personal Profiler agent — uses Groq LLM + Tavily search + resume tools."""

from crewai import Agent
from config import llm
from tools.custom_tools import scrape_tool, search_tool, read_resume, semantic_search_resume


def create_profiler() -> Agent:
    """Returns the Personal Profiler for Engineers agent."""
    return Agent(
        role="Personal Profiler for Engineers",
        goal=(
            "Do incredible research on job applicants "
            "to help them stand out in the job market."
        ),
        tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
        llm=llm,
        verbose=True,
        backstory=(
            "Equipped with analytical prowess, you dissect and synthesize "
            "information from diverse sources to craft comprehensive personal "
            "and professional profiles, laying the groundwork for personalized "
            "resume enhancements."
        ),
    )
