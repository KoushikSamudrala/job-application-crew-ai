"""Tech Job Researcher agent definition."""

from crewai import Agent
from tools.custom_tools import scrape_tool, search_tool


def create_researcher() -> Agent:
    """Returns the Tech Job Researcher agent."""
    return Agent(
        role="Tech Job Researcher",
        goal=(
            "Make sure to do amazing analysis on job postings "
            "to help job applicants stand out."
        ),
        tools=[scrape_tool, search_tool],
        verbose=True,
        backstory=(
            "As a Job Researcher, your prowess in navigating and extracting "
            "critical information from job postings is unmatched. Your skills "
            "help pinpoint the necessary qualifications and skills sought by "
            "employers, forming the foundation for effective application tailoring."
        ),
    )
