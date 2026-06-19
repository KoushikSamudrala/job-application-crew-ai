"""CrewAI tool wrappers for the Job Application Crew."""

from crewai_tools import (
    FileReadTool,
    ScrapeWebsiteTool,
    MDXSearchTool,
    SerperDevTool,
)
from config import RESUME_PATH

# Web search via Serper API
search_tool = SerperDevTool()

# Scrape raw content from a job posting URL
scrape_tool = ScrapeWebsiteTool()

# Read the candidate's resume file
read_resume = FileReadTool(file_path=RESUME_PATH)

# Semantic search over the resume using MDX
semantic_search_resume = MDXSearchTool(mdx=RESUME_PATH)
