"""
Professional workflow visualization using matplotlib.
Creates beautiful, modern visualizations with a clean design aesthetic.
"""

import os
import json
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from typing import Dict, Any

# Try to import seaborn, but don't fail if not available
try:
    import seaborn as sns
    SEABORN_AVAILABLE = True
    # Set professional styling
    sns.set_style("whitegrid")
except ImportError:
    SEABORN_AVAILABLE = False
    # Use matplotlib default styling
    plt.style.use('default')
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Segoe UI", "Arial", "DejaVu Sans"]
plt.rcParams["font.size"] = 10
plt.rcParams["axes.labelsize"] = 11
plt.rcParams["axes.titlesize"] = 13
plt.rcParams["xtick.labelsize"] = 9
plt.rcParams["ytick.labelsize"] = 9
plt.rcParams["legend.fontsize"] = 10
plt.rcParams["figure.titlesize"] = 14

# Professional color palette
COLORS = {
    "primary": "#2E86AB",  # Professional blue
    "secondary": "#A23B72",  # Accent purple
    "success": "#06A77D",  # Green
    "warning": "#F18F01",  # Orange
    "danger": "#C73E1D",  # Red
    "light": "#F4F4F9",  # Light gray
    "dark": "#2D3142",  # Dark gray
    "text": "#333333",  # Text color
}

OUT_DIR = os.getenv("WORKFLOW_OUT_DIR", "data/visuals")
os.makedirs(OUT_DIR, exist_ok=True)


def create_workflow_diagram(
    result_dict: Dict[str, Any], out_filename: str = "workflow_graph"
) -> str:
    """
    Create a professional workflow diagram using matplotlib.
    Returns path to the saved PNG file.
    """

    # Define workflow nodes and their positions
    nodes = [
        {"name": "Parser", "pos": (1, 5), "key": "parser"},
        {"name": "Scoring", "pos": (3, 5), "key": "scoring"},
        {"name": "Matcher", "pos": (5, 5), "key": "matcher"},
        {"name": "Rewrite", "pos": (7, 5), "key": "rewrite"},
        {"name": "Cover Letter", "pos": (7, 3), "key": "coverletter"},
        {"name": "Projects", "pos": (9, 5), "key": "projectsuggester"},
        {"name": "Job Search", "pos": (9, 3), "key": "jobsearch"},
    ]

    # Define edges
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (3, 6)]

    # Create figure with professional styling
    fig, ax = plt.subplots(figsize=(14, 6), facecolor="white")
    ax.set_xlim(0, 10)
    ax.set_ylim(2, 6)
    ax.axis("off")

    # Draw edges with arrows
    for start_idx, end_idx in edges:
        start = nodes[start_idx]["pos"]
        end = nodes[end_idx]["pos"]

        arrow = FancyArrowPatch(
            start,
            end,
            arrowstyle="->,head_width=0.4,head_length=0.8",
            color=COLORS["primary"],
            linewidth=2,
            alpha=0.7,
            zorder=1,
        )
        ax.add_patch(arrow)

    # Draw nodes
    for node in nodes:
        x, y = node["pos"]
        name = node["name"]
        key = node["key"]

        # Get status from result_dict
        has_data = key in result_dict and result_dict[key]

        # Choose color based on status
        if has_data:
            box_color = COLORS["success"]
            text_color = "white"
        else:
            box_color = COLORS["light"]
            text_color = COLORS["text"]

        # Draw fancy box
        fancy_box = FancyBboxPatch(
            (x - 0.4, y - 0.25),
            0.8,
            0.5,
            boxstyle="round,pad=0.05",
            facecolor=box_color,
            edgecolor=COLORS["primary"],
            linewidth=2,
            zorder=2,
        )
        ax.add_patch(fancy_box)

        # Add text
        ax.text(
            x,
            y,
            name,
            ha="center",
            va="center",
            fontsize=10,
            fontweight="bold",
            color=text_color,
            zorder=3,
        )

        # Add status indicator
        if has_data:
            # Add checkmark
            ax.text(
                x + 0.35,
                y + 0.2,
                "✓",
                ha="center",
                va="center",
                fontsize=12,
                color="white",
                fontweight="bold",
                zorder=4,
            )

    # Add title
    fig.suptitle(
        "AI Resume Assistant Workflow",
        fontsize=16,
        fontweight="bold",
        color=COLORS["dark"],
        y=0.98,
    )

    # Add subtitle
    completed_count = sum(
        1 for node in nodes if node["key"] in result_dict and result_dict[node["key"]]
    )
    ax.text(
        5,
        2.3,
        f"Pipeline Status: {completed_count}/{len(nodes)} stages completed",
        ha="center",
        va="center",
        fontsize=11,
        color=COLORS["text"],
        style="italic",
    )

    plt.tight_layout()

    # Save the figure
    out_path = os.path.join(OUT_DIR, f"{out_filename}.png")
    plt.savefig(out_path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close()

    return out_path


def create_score_visualization(
    subscores: Dict[str, float],
    overall_score: float,
    out_filename: str = "score_visual",
) -> str:
    """
    Create a professional score visualization with radar chart and bar chart.
    """
    if not subscores:
        subscores = {"Overall": overall_score}

    fig = plt.figure(figsize=(14, 6), facecolor="white")

    # Create radar chart
    ax1 = fig.add_subplot(121, projection="polar")

    categories = list(subscores.keys())
    values = list(subscores.values())

    # Complete the circle for plotting values (categories labels reuse via set_xticklabels)
    values_plot = values + [values[0]]

    # Convert to radians
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles_plot = angles + [angles[0]]

    # Plot
    ax1.plot(
        angles_plot,
        values_plot,
        "o-",
        linewidth=2,
        color=COLORS["primary"],
        label="Your Score",
    )
    ax1.fill(angles_plot, values_plot, alpha=0.25, color=COLORS["primary"])

    # Add reference circle for 80% (good score)
    ax1.plot(
        angles_plot,
        [80] * len(angles_plot),
        "--",
        linewidth=1,
        color=COLORS["success"],
        alpha=0.5,
        label="Target (80)",
    )

    ax1.set_xticks(angles)
    ax1.set_xticklabels(categories, size=10)
    ax1.set_ylim(0, 100)
    ax1.set_yticks([20, 40, 60, 80, 100])
    ax1.set_yticklabels(["20", "40", "60", "80", "100"], size=9)
    ax1.set_title(
        "Score Breakdown", pad=20, fontsize=13, fontweight="bold", color=COLORS["dark"]
    )
    ax1.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    ax1.grid(True, linestyle="--", alpha=0.7)

    # Create bar chart
    ax2 = fig.add_subplot(122)

    # Sort by score
    sorted_items = sorted(subscores.items(), key=lambda x: x[1], reverse=True)
    categories_sorted = [item[0] for item in sorted_items]
    values_sorted = [item[1] for item in sorted_items]

    # Color bars based on score
    colors = []
    for val in values_sorted:
        if val >= 80:
            colors.append(COLORS["success"])
        elif val >= 60:
            colors.append(COLORS["warning"])
        else:
            colors.append(COLORS["danger"])

    bars = ax2.barh(categories_sorted, values_sorted, color=colors, alpha=0.8)

    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, values_sorted)):
        ax2.text(val + 1, i, f"{val:.0f}", va="center", fontsize=10, fontweight="bold")

    ax2.set_xlim(0, 105)
    ax2.set_xlabel("Score", fontsize=11, fontweight="bold")
    ax2.set_title(
        "Performance by Category", fontsize=13, fontweight="bold", color=COLORS["dark"]
    )
    ax2.grid(axis="x", linestyle="--", alpha=0.3)

    # Add overall score indicator
    fig.text(
        0.5,
        0.02,
        f"Overall Score: {overall_score:.0f}/100",
        ha="center",
        fontsize=14,
        fontweight="bold",
        color=COLORS["primary"],
        bbox=dict(boxstyle="round", facecolor=COLORS["light"], alpha=0.8),
    )

    plt.tight_layout(rect=[0, 0.04, 1, 1])

    # Save
    out_path = os.path.join(OUT_DIR, f"{out_filename}.png")
    plt.savefig(out_path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close()

    return out_path


def create_skill_match_visualization(
    matched_skills: list,
    missing_skills: list,
    match_score: float,
    out_filename: str = "skill_match",
) -> str:
    """
    Create visualization for skill matching analysis.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), facecolor="white")

    # Pie chart for match distribution
    if matched_skills or missing_skills:
        matched_count = len(matched_skills)
        missing_count = len(missing_skills)

        sizes = [matched_count, missing_count]
        labels = [f"Matched\n({matched_count})", f"Missing\n({missing_count})"]
        colors = [COLORS["success"], COLORS["danger"]]
        explode = (0.05, 0.05)

        ax1.pie(
            sizes,
            explode=explode,
            labels=labels,
            colors=colors,
            autopct="%1.1f%%",
            shadow=True,
            startangle=90,
            textprops={"fontsize": 11, "fontweight": "bold"},
        )
        ax1.set_title(
            "Skill Coverage",
            fontsize=13,
            fontweight="bold",
            pad=20,
            color=COLORS["dark"],
        )
    else:
        ax1.text(
            0.5,
            0.5,
            "No skill data available",
            ha="center",
            va="center",
            fontsize=12,
            color=COLORS["text"],
        )
        ax1.axis("off")

    # Match score gauge
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis("off")

    # Draw gauge background
    theta = np.linspace(0, np.pi, 100)
    r = 4
    x_bg = 5 + r * np.cos(theta)
    y_bg = 2 + r * np.sin(theta)
    ax2.plot(x_bg, y_bg, color=COLORS["light"], linewidth=15, solid_capstyle="round")

    # Draw score arc
    score_theta = np.linspace(0, np.pi * (match_score / 100), 100)
    x_score = 5 + r * np.cos(score_theta)
    y_score = 2 + r * np.sin(score_theta)

    # Color based on score
    if match_score >= 80:
        score_color = COLORS["success"]
    elif match_score >= 60:
        score_color = COLORS["warning"]
    else:
        score_color = COLORS["danger"]

    ax2.plot(x_score, y_score, color=score_color, linewidth=15, solid_capstyle="round")

    # Add score text
    ax2.text(
        5,
        2,
        f"{match_score:.0f}%",
        ha="center",
        va="center",
        fontsize=32,
        fontweight="bold",
        color=score_color,
    )
    ax2.text(
        5,
        0.5,
        "Match Score",
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold",
        color=COLORS["text"],
    )

    # Add markers
    ax2.text(1, 2, "0", ha="center", va="center", fontsize=10, color=COLORS["text"])
    ax2.text(9, 2, "100", ha="center", va="center", fontsize=10, color=COLORS["text"])
    ax2.text(
        5,
        6.5,
        "JOB MATCH ANALYSIS",
        ha="center",
        va="center",
        fontsize=14,
        fontweight="bold",
        color=COLORS["dark"],
    )

    plt.tight_layout()

    # Save
    out_path = os.path.join(OUT_DIR, f"{out_filename}.png")
    plt.savefig(out_path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close()

    return out_path


def visualize_agents_workflow(
    result_dict: Dict[str, Any], out_filename: str = "workflow_graph"
) -> str:
    """
    Main function to create workflow visualization.
    Backwards compatible with the old graphviz-based function.
    """
    try:
        return create_workflow_diagram(result_dict, out_filename)
    except Exception as e:
        print(f"Workflow visualization failed: {e}")
        # Fallback to JSON
        out_path = os.path.join(OUT_DIR, f"{out_filename}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(result_dict, f, indent=2)
        return out_path
