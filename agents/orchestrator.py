from langchain.agents import Tool, AgentExecutor
from agents.parser_agent import parse_resume
from agents.scoring_agent import score_resume
from agents.matcher_agent import match_resume
from agents.rewrite_agent import rewrite_resume_agent
from agents.coverletter_agent import generate_coverletter
from agents.project_agent import suggest_projects_agent
from agents.jobsearch_agent import search_jobs_agent

tools = [
    Tool(name="Parser", func=parse_resume, description="Parse resume files"),
    Tool(name="Scorer", func=score_resume, description="Score resume completeness"),
    Tool(name="Matcher", func=match_resume, description="Match resume vs job description"),
    Tool(name="Rewriter", func=rewrite_resume_agent, description="Rewrite resume bullets"),
    Tool(name="CoverLetter", func=generate_coverletter, description="Generate cover letter"),
    Tool(name="ProjectSuggester", func=suggest_projects_agent, description="Suggest projects"),
    Tool(name="JobSearch", func=search_jobs_agent, description="Search jobs based on JD")
]

executor = AgentExecutor.from_tools(
    tools=tools,
    agent="chat-zero-shot-react-description",
    verbose=True
)
