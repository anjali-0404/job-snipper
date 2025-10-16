from typing import List, Any, Dict, Optional
from langchain.agents import Tool, AgentExecutor
from langchain.memory import ConversationBufferMemory

import os
import sys
from dotenv import load_dotenv

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.llm_utils import generate_text

load_dotenv()


class MultiModelLLMWrapper:
    """Multi-model LLM wrapper exposing .call(prompt) interface for LangChain compatibility."""

    def __init__(self, temperature: float = 0.0, max_tokens: int = 2048, preferred_provider: str = None):
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.preferred_provider = preferred_provider

    def call(self, prompt: str) -> str:
        """Generate text using multi-model LLM with automatic fallback."""
        try:
            return generate_text(
                prompt,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                preferred_provider=self.preferred_provider
            )
        except Exception as e:
            raise RuntimeError(f"Multi-model LLM generation failed: {e}")


def make_gemini_llm(
    temperature: float = 0.0, model_name: Optional[str] = None
) -> MultiModelLLMWrapper:
    """
    Return a MultiModelLLMWrapper instance (maintains backward compatibility).
    Note: model_name is deprecated - use preferred_provider instead.
    """
    # Map old model names to providers for backward compatibility
    provider = None
    if model_name:
        if "gemini" in model_name.lower():
            provider = "gemini"
        elif "gpt" in model_name.lower():
            provider = "openai"
        elif "claude" in model_name.lower():
            provider = "anthropic"
    
    return MultiModelLLMWrapper(temperature=temperature, preferred_provider=provider)


def make_tools_from_funcs(funcs: List[Dict[str, Any]]):
    """Build LangChain Tool objects from a list of dicts.

    Expected input: [{"name": "Parser", "func": parse_resume, "description": "..."}, ...]
    """
    tools = []
    for f in funcs:
        tools.append(
            Tool(name=f["name"], func=f["func"], description=f.get("description", ""))
        )
    return tools


def make_executor_from_tools(
    tools: List[Tool],
    agent_type: str = "chat-zero-shot-react-description",
    memory: Optional[ConversationBufferMemory] = None,
    llm=None,
    verbose: bool = True,
):
    """Create an AgentExecutor bound to the provided tools.

    - memory: optional LangChain memory object
    - llm: optional model to power the agent's inner reasoning (must expose `.call(prompt)`)
    """
    if llm is None:
        llm = make_gemini_llm()

    # AgentExecutor.from_tools will construct a default agent of given type internally
    # We create executor with provided LLM (the agent will use it for planning)
    try:
        executor = AgentExecutor.from_tools(
            tools=tools,
            agent=agent_type,
            memory=memory,
            llm=llm,
            verbose=verbose,
        )
        return executor
    except Exception as e:
        print("Failed to create AgentExecutor:", e)
        # Try fallback: create executor without memory
        try:
            executor = AgentExecutor.from_tools(
                tools=tools,
                agent=agent_type,
                llm=llm,
                verbose=verbose,
            )
            return executor
        except Exception as e2:
            raise RuntimeError(
                f"Could not create LangChain AgentExecutor: {e2}"
            ) from e2


def make_conversation_memory(
    mem_key: str = "chat_history", return_messages: bool = True
):
    """Create a simple conversation buffer memory instance."""
    return ConversationBufferMemory(memory_key=mem_key, return_messages=return_messages)
