"""Research task: extract job requirements from a posting URL."""

from crewai import Task
from crewai import Agent


def create_research_task(researcher: Agent) -> Task:
    """Returns the job research task assigned to the Researcher agent."""
    return Task(
        description=(
            "Analyze the job posting URL provided ({job_posting_url}) to extract "
            "key skills, experiences, and qualifications required. Use the tools "
            "to gather content and identify and categorize the requirements."
        ),
        expected_output=(
            "A structured list of job requirements, including necessary "
            "skills, qualifications, and experiences."
        ),
        agent=researcher,
        async_execution=True,
    )
