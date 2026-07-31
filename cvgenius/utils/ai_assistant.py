from __future__ import annotations

from cvgenius.models.cv_profile import CVProfile


def generate_summary_suggestion(profile: CVProfile) -> str:
    """Generate a deterministic summary suggestion from known profile fields.

    This helper keeps the AI slice intentionally small and model-driven:
    it does not call external APIs and does not alter the UI or export code.
    """
    skill_text = ", ".join(profile.skills[:3]) if profile.skills else "strong communication"
    title = profile.professional_title or "professional"

    return (
        f"{profile.full_name or 'Experienced professional'} is a {title} with a strong "
        f"foundation in {skill_text}."
    )
