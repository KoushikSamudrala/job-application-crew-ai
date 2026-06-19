"""Interview prep task: generate interview questions and talking points."""

from crewai import Task
from crewai import Agent
from config import OUTPUT_DIR
import os


def create_interview_prep_task(
    interview_preparer: Agent,
    research_task: Task,
    profile_task: Task,
    resume_strategy_task: Task,
) -> Task:
    """Returns the interview prep task assigned to the Interview Preparer agent."""
    return Task(
        description=(
            "Create a set of potential interview questions and talking points "
            "based on the tailored resume and job requirements. Utilize tools "
            "to generate relevant questions and discussion points. Make sure to "
            "use these questions and talking points to help the candidate highlight "
            "the main points of the resume and how it matches the job posting."
        ),
        expected_output=(
            "A document containing key questions and talking points that the "
            "candidate should prepare for the initial interview."
        ),
        output_file=os.path.join(OUTPUT_DIR, "interview_materials.md"),
        context=[research_task, profile_task, resume_strategy_task],
        agent=interview_preparer,
    )
