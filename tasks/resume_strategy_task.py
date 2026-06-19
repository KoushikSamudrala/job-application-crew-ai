"""Resume strategy task: tailor the resume to match job requirements."""

from crewai import Task
from crewai import Agent
from config import OUTPUT_DIR
import os


def create_resume_strategy_task(
    resume_strategist: Agent,
    research_task: Task,
    profile_task: Task,
) -> Task:
    """Returns the resume strategy task assigned to the Resume Strategist agent."""
    return Task(
        description=(
            "Using the profile and job requirements obtained from previous tasks, "
            "tailor the resume to highlight the most relevant areas. Employ tools "
            "to adjust and enhance the resume content. Make sure this is the best "
            "resume ever but don't make up any information. Update every section, "
            "including the initial summary, work experience, skills, and education — "
            "all to better reflect the candidate's abilities and how it matches the "
            "job posting."
        ),
        expected_output=(
            "An updated resume that effectively highlights the candidate's "
            "qualifications and experiences relevant to the job."
        ),
        output_file=os.path.join(OUTPUT_DIR, "tailored_resume.md"),
        context=[research_task, profile_task],
        agent=resume_strategist,
    )
