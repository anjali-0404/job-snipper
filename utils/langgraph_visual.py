"""
Workflow visualization helper.
Tries to use 'langgraph' if available; otherwise falls back to graphviz to render
an HTML/SVG file that can be embedded in Streamlit.
"""

import os
import json
from typing import Dict, Any

# Attempt to import langgraph
try:
    from langgraph import Graph, Node  # type: ignore

    HAS_LANGGRAPH = True
except Exception:
    HAS_LANGGRAPH = False


OUT_DIR = os.getenv("WORKFLOW_OUT_DIR", "data/visuals")
os.makedirs(OUT_DIR, exist_ok=True)


def visualize_agents_workflow(
    result_dict: Dict[str, Any], out_filename: str = "workflow_graph"
):
    """
    Create a workflow visualization from a result dictionary describing pipeline outputs.
    - If langgraph is installed, use it.
    - Otherwise render a Graphviz digraph to SVG/HTML for embedding.
    Returns path to generated HTML file (or SVG).
    """
    if HAS_LANGGRAPH:
        # Build LangGraph object (simple metadata)
        g = Graph(title="AI Resume Assistant Workflow")
        nodes = {}
        order = [
            "Parser",
            "Scoring",
            "Matcher",
            "Rewrite",
            "CoverLetter",
            "ProjectSuggester",
            "JobSearch",
        ]
        for n in order:
            node = Node(n)
            # attach metadata if available
            meta_key = n.lower()
            if meta_key in result_dict:
                node.metadata = {"summary": str(result_dict.get(meta_key))}
            g.add_node(node)
            nodes[n] = node
        # Add edges in logical order
        edges = [
            ("Parser", "Scoring"),
            ("Scoring", "Matcher"),
            ("Matcher", "Rewrite"),
            ("Rewrite", "CoverLetter"),
            ("Rewrite", "ProjectSuggester"),
            ("Rewrite", "JobSearch"),
        ]
        for a, b in edges:
            g.add_edge(nodes[a], nodes[b])
        out_path = os.path.join(OUT_DIR, f"{out_filename}.html")
        g.render(out_path)
        return out_path

  
    # no visualization libs available: produce basic JSON file
    out_path = os.path.join(OUT_DIR, f"{out_filename}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result_dict, f, indent=2)
    return out_path
