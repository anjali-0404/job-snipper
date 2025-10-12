"""
Version Manager & A/B Testing
Track multiple resume versions and analyze which performs best.
"""

import json
from datetime import datetime
from typing import Dict, List, Any, Optional


class VersionManager:
    """Manage resume versions and track performance."""

    def __init__(self):
        self.versions = []

    def create_version(
        self,
        resume_text: str,
        version_name: str,
        settings: Dict[str, Any],
        notes: str = "",
    ) -> Dict[str, Any]:
        """
        Create a new resume version.

        Args:
            resume_text: Resume content
            version_name: Name for this version
            settings: Settings used to generate this version
            notes: Optional notes about this version

        Returns:
            Version metadata
        """
        version = {
            "id": len(self.versions) + 1,
            "name": version_name,
            "content": resume_text,
            "settings": settings,
            "notes": notes,
            "created_at": datetime.now().isoformat(),
            "stats": {
                "word_count": len(resume_text.split()),
                "char_count": len(resume_text),
                "line_count": len(resume_text.split("\n")),
            },
            "performance": {
                "applications": 0,
                "interviews": 0,
                "responses": 0,
                "rejections": 0,
                "offers": 0,
            },
            "scores": {"ats_score": 0, "match_score": 0, "quality_score": 0},
        }

        self.versions.append(version)
        return version

    def update_performance(
        self, version_id: int, metric: str, increment: int = 1
    ) -> Dict[str, Any]:
        """
        Update performance metrics for a version.

        Args:
            version_id: Version ID
            metric: Metric to update (applications, interviews, etc.)
            increment: Amount to increment by

        Returns:
            Updated version data
        """
        for version in self.versions:
            if version["id"] == version_id:
                if metric in version["performance"]:
                    version["performance"][metric] += increment
                return version

        return None

    def update_scores(
        self,
        version_id: int,
        ats_score: float = None,
        match_score: float = None,
        quality_score: float = None,
    ) -> Dict[str, Any]:
        """
        Update scores for a version.

        Args:
            version_id: Version ID
            ats_score: ATS compatibility score
            match_score: Job match score
            quality_score: Overall quality score

        Returns:
            Updated version data
        """
        for version in self.versions:
            if version["id"] == version_id:
                if ats_score is not None:
                    version["scores"]["ats_score"] = ats_score
                if match_score is not None:
                    version["scores"]["match_score"] = match_score
                if quality_score is not None:
                    version["scores"]["quality_score"] = quality_score
                return version

        return None

    def get_version(self, version_id: int) -> Optional[Dict[str, Any]]:
        """Get a specific version by ID."""
        for version in self.versions:
            if version["id"] == version_id:
                return version
        return None

    def list_versions(self) -> List[Dict[str, Any]]:
        """List all versions."""
        return self.versions

    def compare_versions(self, version_id1: int, version_id2: int) -> Dict[str, Any]:
        """
        Compare two resume versions.

        Args:
            version_id1: First version ID
            version_id2: Second version ID

        Returns:
            Comparison results
        """
        v1 = self.get_version(version_id1)
        v2 = self.get_version(version_id2)

        if not v1 or not v2:
            return {"error": "One or both versions not found"}

        # Calculate conversion rates
        v1_conversion = (
            (v1["performance"]["interviews"] / v1["performance"]["applications"] * 100)
            if v1["performance"]["applications"] > 0
            else 0
        )
        v2_conversion = (
            (v2["performance"]["interviews"] / v2["performance"]["applications"] * 100)
            if v2["performance"]["applications"] > 0
            else 0
        )

        v1_offer_rate = (
            (v1["performance"]["offers"] / v1["performance"]["applications"] * 100)
            if v1["performance"]["applications"] > 0
            else 0
        )
        v2_offer_rate = (
            (v2["performance"]["offers"] / v2["performance"]["applications"] * 100)
            if v2["performance"]["applications"] > 0
            else 0
        )

        comparison = {
            "version1": {
                "id": v1["id"],
                "name": v1["name"],
                "performance": v1["performance"],
                "scores": v1["scores"],
                "conversion_rate": round(v1_conversion, 1),
                "offer_rate": round(v1_offer_rate, 1),
            },
            "version2": {
                "id": v2["id"],
                "name": v2["name"],
                "performance": v2["performance"],
                "scores": v2["scores"],
                "conversion_rate": round(v2_conversion, 1),
                "offer_rate": round(v2_offer_rate, 1),
            },
            "winner": None,
            "differences": {},
        }

        # Determine winner based on conversion rates
        if v1_conversion > v2_conversion:
            comparison["winner"] = v1["name"]
        elif v2_conversion > v1_conversion:
            comparison["winner"] = v2["name"]
        else:
            comparison["winner"] = "Tie"

        # Calculate differences
        comparison["differences"] = {
            "word_count": v2["stats"]["word_count"] - v1["stats"]["word_count"],
            "interviews": v2["performance"]["interviews"]
            - v1["performance"]["interviews"],
            "conversion_rate": round(v2_conversion - v1_conversion, 1),
            "offer_rate": round(v2_offer_rate - v1_offer_rate, 1),
            "ats_score": round(
                v2["scores"]["ats_score"] - v1["scores"]["ats_score"], 1
            ),
        }

        return comparison

    def get_performance_analytics(self) -> Dict[str, Any]:
        """
        Get overall performance analytics across all versions.

        Returns:
            Analytics data
        """
        if not self.versions:
            return {"error": "No versions to analyze"}

        total_apps = sum(v["performance"]["applications"] for v in self.versions)
        total_interviews = sum(v["performance"]["interviews"] for v in self.versions)
        total_offers = sum(v["performance"]["offers"] for v in self.versions)

        overall_conversion = (
            (total_interviews / total_apps * 100) if total_apps > 0 else 0
        )
        overall_offer_rate = (total_offers / total_apps * 100) if total_apps > 0 else 0

        # Find best performing version
        best_version = max(
            self.versions,
            key=lambda v: (
                v["performance"]["interviews"] / v["performance"]["applications"] * 100
            )
            if v["performance"]["applications"] > 0
            else 0,
        )

        # Find highest scored version
        highest_scored = max(self.versions, key=lambda v: v["scores"]["quality_score"])

        analytics = {
            "total_versions": len(self.versions),
            "total_applications": total_apps,
            "total_interviews": total_interviews,
            "total_offers": total_offers,
            "overall_conversion_rate": round(overall_conversion, 1),
            "overall_offer_rate": round(overall_offer_rate, 1),
            "best_performing_version": {
                "id": best_version["id"],
                "name": best_version["name"],
                "conversion_rate": round(
                    (
                        best_version["performance"]["interviews"]
                        / best_version["performance"]["applications"]
                        * 100
                    )
                    if best_version["performance"]["applications"] > 0
                    else 0,
                    1,
                ),
            },
            "highest_scored_version": {
                "id": highest_scored["id"],
                "name": highest_scored["name"],
                "quality_score": highest_scored["scores"]["quality_score"],
            },
            "version_comparison": [],
        }

        # Add per-version breakdown
        for v in self.versions:
            conv_rate = (
                (
                    v["performance"]["interviews"]
                    / v["performance"]["applications"]
                    * 100
                )
                if v["performance"]["applications"] > 0
                else 0
            )
            analytics["version_comparison"].append(
                {
                    "id": v["id"],
                    "name": v["name"],
                    "applications": v["performance"]["applications"],
                    "interviews": v["performance"]["interviews"],
                    "conversion_rate": round(conv_rate, 1),
                    "quality_score": v["scores"]["quality_score"],
                }
            )

        return analytics

    def export_versions(self, filename: str = "resume_versions.json"):
        """Export all versions to JSON file."""
        with open(filename, "w") as f:
            json.dump(self.versions, f, indent=2)

    def import_versions(self, filename: str = "resume_versions.json"):
        """Import versions from JSON file."""
        try:
            with open(filename, "r") as f:
                self.versions = json.load(f)
        except FileNotFoundError:
            pass

    def delete_version(self, version_id: int) -> bool:
        """Delete a specific version."""
        self.versions = [v for v in self.versions if v["id"] != version_id]
        return True

    def get_recommendations(self) -> List[str]:
        """Get recommendations based on version performance."""
        if len(self.versions) < 2:
            return ["Create more versions to enable A/B testing and recommendations"]

        analytics = self.get_performance_analytics()
        recommendations = []

        best_version = analytics["best_performing_version"]
        best_v_data = self.get_version(best_version["id"])

        recommendations.append(
            f"🏆 Best performing version: '{best_version['name']}' "
            f"with {best_version['conversion_rate']}% conversion rate"
        )

        # Analyze what made it successful
        if best_v_data:
            settings = best_v_data["settings"]
            recommendations.append(
                f"✅ Successful settings: Tone={settings.get('tone', 'N/A')}, "
                f"Focus={settings.get('focus', 'N/A')}"
            )

        # Compare with worst
        worst_version = min(
            self.versions,
            key=lambda v: (
                v["performance"]["interviews"] / v["performance"]["applications"] * 100
            )
            if v["performance"]["applications"] > 0
            else 0,
        )

        if worst_version["id"] != best_version["id"]:
            recommendations.append(
                f"⚠️ Lowest performing: '{worst_version['name']}' - "
                f"consider updating or removing this version"
            )

        # Overall insights
        if analytics["overall_conversion_rate"] < 10:
            recommendations.append(
                "💡 Conversion rate is low. Consider:\n"
                "  - Adding more quantifiable achievements\n"
                "  - Improving keyword optimization\n"
                "  - Tailoring to specific job descriptions"
            )

        return recommendations
