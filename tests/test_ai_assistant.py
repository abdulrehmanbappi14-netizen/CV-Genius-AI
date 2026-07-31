import unittest

from cvgenius.models.cv_profile import CVProfile
from cvgenius.utils.ai_assistant import generate_summary_suggestion


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


if __name__ == "__main__":
    unittest.main()
