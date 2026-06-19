"""CrewAI tool wrappers for the Job Application Crew.

Search  : TavilySearchResults (replaces SerperDev)
Scraping: ScrapeWebsiteTool
Resume  : FileReadTool + MDXSearchTool
"""

from langchain_community.tools.tavily_search import TavilySearchResults
from crewai_tools import (
    FileReadTool,
    ScrapeWebsiteTool,
    MDXSearchTool,
)
from config import RESUME_PATH

# Web search via Tavily API (replaces SerperDev)
search_tool = TavilySearchResults(
    max_results=5,
    search_depth="advanced",
    include_answer=True,
)

# Scrape raw content from a job posting URL
scrape_tool = ScrapeWebsiteTool()

# Read the candidate's resume file
read_resume = FileReadTool(file_path=RESUME_PATH)

# Semantic search over the resume using MDX
semantic_search_resume = MDXSearchTool(mdx=RESUME_PATH)
