from typing import List, Any, Dict, Optional
from langchain.agents import Tool, AgentExecutor
from langchain.memory import ConversationBufferMemory

import os
from dotenv import load_dotenv

load_dotenv()


# Gemini SDK (optional) — we handle absence gracefully in calling modules
try:
    from google.ai import generativelanguage as genai
    from google.ai.generativelanguage import types as gl_types
    from google.api_core.client_options import ClientOptions

    # create a client lazily in the wrapper if the user provides an API key
    _GENAI_CLIENT = None
    _HAS_GENAI = True
except Exception:
    genai = None
    _GENAI_CLIENT = None
    _HAS_GENAI = False

# Default model; change this constant to point to another Gemini model if needed.
MODEL = os.getenv("GENAI_MODEL", "models/gemini-2.5-flash")


class GeminiWrapper:
    """Thin wrapper exposing .call(prompt) similar to LangChain's ChatOpenAI."""

    def __init__(self, model: str = MODEL, temperature: float = 0.0):
        self.model = model
        self.temperature = temperature

    def call(self, prompt: str) -> str:
        # Initialize client on first use (allows module import without installed SDK)
        if not _HAS_GENAI:
            raise RuntimeError("google-ai-generativelanguage SDK not available")

        global _GENAI_CLIENT
        if _GENAI_CLIENT is None:
            # try to pick up API key from env if available
            api_key = os.getenv("GOOGLE_API_KEY")
            client_opts = None
            if api_key:
                client_opts = ClientOptions(api_key=api_key)
            # Use the TextServiceClient exposed on the generativelanguage module
            _GENAI_CLIENT = genai.TextServiceClient(client_options=client_opts)
        request = gl_types.GenerateTextRequest(
            model=self.model,
            prompt=gl_types.TextPrompt(text=prompt),
            temperature=self.temperature,
        )

        resp = _GENAI_CLIENT.generate_text(request=request)
        if hasattr(resp, "candidates") and resp.candidates:
            return "\n".join([c.output for c in resp.candidates])
        return str(resp)


def make_gemini_llm(
    temperature: float = 0.0, model_name: Optional[str] = None
) -> GeminiWrapper:
    """Return a GeminiWrapper instance (wrap creation for reuse)."""
    model = model_name or MODEL
    return GeminiWrapper(model=model, temperature=temperature)


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
