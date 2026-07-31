import unittest

from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from cvgenius.models.cv_profile import CVProfile
from cvgenius.screens.profile_editor.profile_editor import ProfileEditorScreen
from cvgenius.screens.template_preview.template_preview import TemplatePreviewScreen


class DummyApp(MDApp):
    pass


class ProfileEditorScreenTests(unittest.TestCase):
    def test_profile_editor_screen_uses_cv_profile_model(self):
        app = DummyApp()
        screen = ProfileEditorScreen(name="profile_editor")

        self.assertIsInstance(screen.profile, CVProfile)
        self.assertEqual(screen.profile.full_name, "")
        self.assertEqual(screen.profile.experiences, [])
        self.assertEqual(screen.profile.education, [])
        self.assertEqual(screen.profile.skills, [])
        self.assertEqual(screen.profile.languages, [])
        self.assertEqual(screen.profile.certifications, [])

    def test_profile_editor_can_pass_current_profile_to_preview_screen(self):
        app = DummyApp()
        manager = ScreenManager()
        editor = ProfileEditorScreen(name="profile_editor")
        preview = TemplatePreviewScreen(name="template_preview")

        manager.add_widget(editor)
        manager.add_widget(preview)

        editor.profile = CVProfile(
            full_name="Ada Lovelace",
            professional_title="Mathematician",
            summary="Pioneer in computing.",
            template_name="classic",
        )

        editor.preview_resume()

        self.assertEqual(preview.profile.full_name, "Ada Lovelace")
        self.assertEqual(preview.profile.professional_title, "Mathematician")
        self.assertEqual(preview.profile.template_name, "classic")
        self.assertEqual(manager.current, "template_preview")


if __name__ == "__main__":
    unittest.main()
