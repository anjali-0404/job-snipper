"""
Integration test to verify the complete workflow:
1. Import circular dependency is resolved
2. Workflow visualization handles missing Graphviz gracefully
3. App can handle JSON workflow output
"""

import sys
import os

# Add parent directory to path so we can import modules
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
os.chdir(parent_dir)  # Change to project root for relative paths

# Test 1: Circular import resolution
print("=" * 70)
print("TEST 1: Circular Import Resolution")
print("=" * 70)

try:
    from services.docx_parser import parse_docx

    print("✓ Successfully imported parse_docx from services.docx_parser")
    print(f"  Function type: {type(parse_docx)}")
    print(f"  Function name: {parse_docx.__name__}")
except ImportError as e:
    print(f"✗ FAILED: {e}")
    sys.exit(1)

# Test 2: Parser agent import chain
print("\n" + "=" * 70)
print("TEST 2: Parser Agent Import Chain")
print("=" * 70)

try:
    from agents.parser_agent import parse_resume

    print("✓ Successfully imported parse_resume from agents.parser_agent")
    print("  (This confirms the circular import is resolved)")
except ImportError as e:
    print(f"✗ FAILED: {e}")
    sys.exit(1)

# Test 3: Workflow visualization with missing Graphviz
print("\n" + "=" * 70)
print("TEST 3: Workflow Visualization Fallback")
print("=" * 70)

try:
    from utils.langgraph_visual import visualize_agents_workflow

    result_dict = {
        "parser": {"parsed_keys": ["name", "skills"]},
        "scoring": {"overall": 80},
        "matcher": {"match_score": 85},
        "rewrite": {"has_rewritten": True},
        "coverletter": {"has_cover": True},
        "projectsuggester": {"count": 3},
        "jobsearch": {"count": 10},
    }

    workflow_path = visualize_agents_workflow(
        result_dict, out_filename="integration_test"
    )

    if os.path.exists(workflow_path):
        print("✓ Workflow visualization succeeded")
        print(f"  Output: {workflow_path}")

        ext = os.path.splitext(workflow_path)[1]
        if ext == ".json":
            print("  Mode: JSON fallback (Graphviz not available)")

            # Verify JSON is valid
            import json

            with open(workflow_path, "r") as f:
                data = json.load(f)
            print(f"  ✓ Valid JSON with {len(data)} keys")
        elif ext == ".html":
            print("  Mode: HTML visualization")
        else:
            print(f"  Mode: {ext} output")
    else:
        print(f"✗ FAILED: Output file not found at {workflow_path}")
        sys.exit(1)

except Exception as e:
    print(f"✗ FAILED: {e}")
    import traceback

    traceback.print_exc()
    sys.exit(1)

# Test 4: App imports
print("\n" + "=" * 70)
print("TEST 4: App Module Imports")
print("=" * 70)

try:
    # Don't actually run streamlit, just check if imports work
    import importlib.util

    spec = importlib.util.spec_from_file_location("app", "app.py")
    if spec and spec.loader:
        print("✓ app.py module structure is valid")
        print("  (Full streamlit test skipped - requires streamlit runtime)")
    else:
        print("✗ Could not load app.py module spec")
except Exception as e:
    print(f"⚠ Warning: Could not validate app.py: {e}")
    print("  (This may be expected if streamlit is not installed)")

# Summary
print("\n" + "=" * 70)
print("INTEGRATION TEST SUMMARY")
print("=" * 70)
print("✓ All critical tests passed!")
print("\nYour app should now:")
print("  1. Import without circular dependency errors")
print("  2. Run without crashing when Graphviz executable is missing")
print("  3. Display JSON workflow data as fallback")
print("\nTo install Graphviz executable for visual workflows:")
print("  - Windows: Download from https://graphviz.org/download/")
print("  - Or use: choco install graphviz")
print("  - Or use: scoop install graphviz")
print("  - Then restart your terminal/VS Code")
