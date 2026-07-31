import unittest

from cvgenius.models.cv_profile import CVProfile


class TemplatePreviewTests(unittest.TestCase):
    def test_profile_preview_uses_template_name_and_sections(self):
        profile = CVProfile(
            full_name="Ada Lovelace",
            professional_title="Mathematician",
            summary="Pioneer in computing.",
            skills=["Mathematics", "Research"],
            template_name="classic",
        )

        preview = profile.render_preview()

        self.assertIn("Ada Lovelace", preview)
        self.assertIn("Classic Resume", preview)
        self.assertIn("Pioneer in computing.", preview)
        self.assertIn("Mathematics", preview)


if __name__ == "__main__":
    unittest.main()
