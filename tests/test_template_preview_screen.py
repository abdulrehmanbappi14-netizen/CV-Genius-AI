import unittest

from kivymd.app import MDApp

from cvgenius.models.cv_profile import CVProfile
from cvgenius.screens.template_preview.template_preview import TemplatePreviewScreen


class DummyApp(MDApp):
    pass


class TemplatePreviewScreenTests(unittest.TestCase):
    def test_preview_screen_gets_preview_text_from_profile(self):
        app = DummyApp()
        profile = CVProfile(
            full_name="Ada Lovelace",
            professional_title="Mathematician",
            summary="Pioneer in computing.",
            skills=["Mathematics", "Research"],
            template_name="classic",
        )

        screen = TemplatePreviewScreen(name="template_preview")
        screen.profile = profile

        self.assertIn("Ada Lovelace", screen.get_preview_text())
        self.assertIn("Classic Resume", screen.get_preview_text())
        self.assertIn("Pioneer in computing.", screen.get_preview_text())

    def test_preview_screen_refreshes_visible_preview_text(self):
        app = DummyApp()
        screen = TemplatePreviewScreen(name="template_preview")
        screen.profile = CVProfile(
            full_name="Grace Hopper",
            professional_title="Computer Scientist",
            summary="Pioneer in compiler design.",
            skills=["Algorithms", "Leadership"],
            template_name="modern",
        )

        screen.refresh_preview()

        self.assertIn("Grace Hopper", screen.ids.preview_text.text)
        self.assertIn("Modern Resume", screen.ids.preview_text.text)
        self.assertIn("Pioneer in compiler design.", screen.ids.preview_text.text)


if __name__ == "__main__":
    unittest.main()
