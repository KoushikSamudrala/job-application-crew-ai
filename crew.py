"""Crew orchestration: wire agents and tasks together and run the crew."""

from crewai import Crew

from agents import (
    create_researcher,
    create_profiler,
    create_resume_strategist,
    create_interview_preparer,
)
from tasks import (
    create_research_task,
    create_profile_task,
    create_resume_strategy_task,
    create_interview_prep_task,
)


def build_crew() -> Crew:
    """Instantiate all agents and tasks, then return a configured Crew."""
    # --- Agents ---
    researcher = create_researcher()
    profiler = create_profiler()
    resume_strategist = create_resume_strategist()
    interview_preparer = create_interview_preparer()

    # --- Tasks (order matters for context dependencies) ---
    research_task = create_research_task(researcher)
    profile_task = create_profile_task(profiler)
    resume_task = create_resume_strategy_task(resume_strategist, research_task, profile_task)
    interview_task = create_interview_prep_task(
        interview_preparer, research_task, profile_task, resume_task
    )

    return Crew(
        agents=[researcher, profiler, resume_strategist, interview_preparer],
        tasks=[research_task, profile_task, resume_task, interview_task],
        verbose=True,
    )


def run_crew(job_posting_url: str, github_url: str, personal_writeup: str) -> dict:
    """Build and kick off the crew with provided inputs."""
    crew = build_crew()
    inputs = {
        "job_posting_url": job_posting_url,
        "github_url": github_url,
        "personal_writeup": personal_writeup,
    }
    result = crew.kickoff(inputs=inputs)
    return result
