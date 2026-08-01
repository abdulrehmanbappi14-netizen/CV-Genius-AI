import unittest

from cvgenius.models.cv_profile import CVProfile
from cvgenius.utils.ai_assistant import AIService, MockAIProvider, generate_summary_suggestion


class AIAssistantTests(unittest.TestCase):
    def test_generate_summary_suggestion_uses_known_profile_fields(self):
        profile = CVProfile(
            full_name="Ada Lovelace",
            professional_title="Mathematician",
            skills=["Mathematics", "Writing", "Research"],
        )

        suggestion = generate_summary_suggestion(profile)

        self.assertIn("Ada Lovelace", suggestion)
        self.assertIn("Mathematician", suggestion)
        self.assertIn("Mathematics", suggestion)

    def test_ai_service_returns_provider_ready_mock_responses(self):
        profile = CVProfile(
            full_name="Grace Hopper",
            professional_title="Computer Scientist",
            skills=["Compiler Design", "Leadership"],
            summary="Pioneer in compiler design.",
        )

        service = AIService(provider=MockAIProvider())

        improve_result = service.improve_resume(profile)
        summary_result = service.generate_summary(profile)
        skills_result = service.suggest_skills(profile)
        quality_result = service.check_quality(profile)

        self.assertIn("Coming Soon", improve_result)
        self.assertIn("Coming Soon", summary_result)
        self.assertIn("Coming Soon", skills_result)
        self.assertIn("Coming Soon", quality_result)


if __name__ == "__main__":
    unittest.main()
