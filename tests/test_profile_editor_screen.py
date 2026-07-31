import unittest

from kivymd.app import MDApp

from cvgenius.models.cv_profile import CVProfile
from cvgenius.screens.profile_editor.profile_editor import ProfileEditorScreen


class DummyApp(MDApp):
    pass


class ProfileEditorScreenTests(unittest.TestCase):
    def test_profile_editor_screen_uses_cv_profile_model(self):
        app = DummyApp()
        screen = ProfileEditorScreen(name="profile_editor")

        self.assertIsInstance(screen.profile, CVProfile)
        self.assertEqual(screen.profile.full_name, "")


if __name__ == "__main__":
    unittest.main()
