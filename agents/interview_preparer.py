"""Interview Preparer agent definition."""

from crewai import Agent
from tools.custom_tools import scrape_tool, search_tool, read_resume, semantic_search_resume


def create_interview_preparer() -> Agent:
    """Returns the Engineering Interview Preparer agent."""
    return Agent(
        role="Engineering Interview Preparer",
        goal=(
            "Create interview questions and talking points "
            "based on the resume and job requirements."
        ),
        tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
        verbose=True,
        backstory=(
            "Your role is crucial in anticipating the dynamics of interviews. "
            "With your ability to formulate key questions and talking points, "
            "you prepare candidates for success, ensuring they can confidently "
            "address all aspects of the job they are applying for."
        ),
    )
