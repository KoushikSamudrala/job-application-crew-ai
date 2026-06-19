"""Profile task: compile a comprehensive candidate profile."""

from crewai import Task
from crewai import Agent


def create_profile_task(profiler: Agent) -> Task:
    """Returns the profiling task assigned to the Profiler agent."""
    return Task(
        description=(
            "Compile a detailed personal and professional profile using the GitHub "
            "({github_url}) URL and personal write-up ({personal_writeup}). "
            "Utilize tools to extract and synthesize information from these sources."
        ),
        expected_output=(
            "A comprehensive profile document that includes skills, project "
            "experiences, contributions, interests, and communication style."
        ),
        agent=profiler,
        async_execution=True,
    )
