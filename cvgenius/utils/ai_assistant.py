from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from cvgenius.models.cv_profile import CVProfile


class AIProvider(Protocol):
    """Provider interface for future AI backends.

    The contract is intentionally small so OpenAI, Claude, Gemini, or
    any other provider can be plugged in later without changing the rest
    of the application.
    """

    def improve_resume(self, profile: CVProfile) -> str:
        ...

    def generate_summary(self, profile: CVProfile) -> str:
        ...

    def suggest_skills(self, profile: CVProfile) -> str:
        ...

    def check_quality(self, profile: CVProfile) -> str:
        ...


@dataclass
class MockAIProvider:
    """Local placeholder provider that returns deterministic "Coming Soon" responses.

    This keeps the Phase 7 architecture future-proof without making any
    external network calls.
    """

    provider_name: str = "mock"

    def improve_resume(self, profile: CVProfile) -> str:
        return (
            f"Coming Soon: AI Resume Improvement for {profile.full_name or 'this profile'} "
            f"is not yet connected to a live provider."
        )

    def generate_summary(self, profile: CVProfile) -> str:
        return (
            f"Coming Soon: professional summary generation for {profile.full_name or 'this profile'} "
            f"will be provided by the selected AI provider later."
        )

    def suggest_skills(self, profile: CVProfile) -> str:
        return (
            f"Coming Soon: better skills suggestions for {profile.full_name or 'this profile'} "
            f"will be plugged in once a live AI provider is chosen."
        )

    def check_quality(self, profile: CVProfile) -> str:
        return (
            f"Coming Soon: resume quality checks for {profile.full_name or 'this profile'} "
            f"will be provided by the selected AI provider later."
        )


class AIService:
    """Application-facing service that abstracts away the provider implementation."""

    def __init__(self, provider: AIProvider | MockAIProvider | None = None) -> None:
        self.provider = provider or MockAIProvider()

    def improve_resume(self, profile: CVProfile) -> str:
        return self.provider.improve_resume(profile)

    def generate_summary(self, profile: CVProfile) -> str:
        return self.provider.generate_summary(profile)

    def suggest_skills(self, profile: CVProfile) -> str:
        return self.provider.suggest_skills(profile)

    def check_quality(self, profile: CVProfile) -> str:
        return self.provider.check_quality(profile)


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
