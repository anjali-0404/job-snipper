"""
Test script to verify workflow visualization handles missing Graphviz executable gracefully.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.langgraph_visual import visualize_agents_workflow

# Simulate the result_dict from app.py
result_dict = {
    "parser": {"parsed_keys": ["name", "email", "skills"]},
    "scoring": {"overall": 75, "subscores": {"skills": 80, "experience": 70}},
    "matcher": {"match_score": 85, "matched_skills": ["Python", "JavaScript"]},
    "rewrite": {"has_rewritten": True},
    "coverletter": {"has_cover": True},
    "projectsuggester": {"count": 3},
    "jobsearch": {"count": 10},
}

print("Testing workflow visualization with sample data...")
print("-" * 60)

try:
    workflow_path = visualize_agents_workflow(result_dict, out_filename="test_workflow")
    print(f"\n✓ Success! Workflow output saved to: {workflow_path}")

    # Check if file exists
    if os.path.exists(workflow_path):
        print(f"✓ File verified: {workflow_path}")

        # Show file extension to see if it's HTML, SVG, or JSON
        ext = os.path.splitext(workflow_path)[1]
        if ext == ".json":
            print("  → Fallback mode: JSON output (Graphviz executable not available)")
        elif ext in [".html", ".svg"]:
            print(f"  → Visualization mode: {ext.upper()} output generated")
    else:
        print(f"✗ Warning: File not found at {workflow_path}")

except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback

    traceback.print_exc()
    sys.exit(1)

print("\nTest completed successfully!")
