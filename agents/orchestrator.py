"""
Orchestrator Agent - Coordinates all resume processing agents
"""

try:
    from langchain.agents import Tool, AgentExecutor, create_react_agent
    from langchain_core.prompts import PromptTemplate
    LANGCHAIN_AVAILABLE = True
except ImportError:
    LANGCHAIN_AVAILABLE = False

from agents.parser_agent import parse_resume
from agents.scoring_agent import score_resume
from agents.matcher_agent import match_resume
from agents.rewrite_agent import rewrite_resume_agent
from agents.coverletter_agent import generate_coverletter
from agents.project_agent import suggest_projects_agent
from agents.jobsearch_agent import search_jobs_agent

# Define tools
tools = [
    {
        "name": "Parser",
        "func": parse_resume,
        "description": "Parse resume files to extract structured information"
    },
    {
        "name": "Scorer",
        "func": score_resume,
        "description": "Score resume completeness and quality"
    },
    {
        "name": "Matcher",
        "func": match_resume,
        "description": "Match resume against job description"
    },
    {
        "name": "Rewriter",
        "func": rewrite_resume_agent,
        "description": "Rewrite and optimize resume bullets"
    },
    {
        "name": "CoverLetter",
        "func": generate_coverletter,
        "description": "Generate tailored cover letter"
    },
    {
        "name": "ProjectSuggester",
        "func": suggest_projects_agent,
        "description": "Suggest relevant projects based on skills"
    },
    {
        "name": "JobSearch",
        "func": search_jobs_agent,
        "description": "Search for jobs based on job description"
    }
]

# Create executor only if LangChain is available
executor = None

if LANGCHAIN_AVAILABLE:
    try:
        langchain_tools = [
            Tool(
                name=tool["name"],
                func=tool["func"],
                description=tool["description"]
            )
            for tool in tools
        ]
        
        # Note: from_tools is deprecated, using modern approach
        # Executor will be created on-demand with proper LLM
        executor = None  # Set to None for now, will be initialized when needed
    except Exception as e:
        print(f"Warning: Could not create agent executor: {e}")
        executor = None


def get_tool_by_name(tool_name: str):
    """Get a tool function by its name"""
    for tool in tools:
        if tool["name"].lower() == tool_name.lower():
            return tool["func"]
    return None


def orchestrate_workflow(workflow_steps: list):
    """
    Orchestrate a workflow by executing tools in sequence
    
    Args:
        workflow_steps: List of tool names to execute in order
        
    Returns:
        Results from each step
    """
    results = {}
    
    for step in workflow_steps:
        tool_func = get_tool_by_name(step)
        if tool_func:
            try:
                # Execute the tool (actual parameters would be passed from context)
                results[step] = {"status": "ready", "func": tool_func}
            except Exception as e:
                results[step] = {"status": "error", "error": str(e)}
        else:
            results[step] = {"status": "not_found"}
    
    return results
