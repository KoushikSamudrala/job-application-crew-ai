"""Resume Strategist agent definition."""

from crewai import Agent
from tools.custom_tools import scrape_tool, search_tool, read_resume, semantic_search_resume


def create_resume_strategist() -> Agent:
    """Returns the Resume Strategist for Engineers agent."""
    return Agent(
        role="Resume Strategist for Engineers",
        goal="Find all the best ways to make a resume stand out in the job market.",
        tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
        verbose=True,
        backstory=(
            "With a strategic mind and an eye for detail, you excel at refining "
            "resumes to highlight the most relevant skills and experiences, ensuring "
            "they resonate perfectly with the job's requirements."
        ),
    )
