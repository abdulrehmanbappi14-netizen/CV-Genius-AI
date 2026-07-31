import unittest

from kivymd.app import MDApp

from cvgenius.models.cv_profile import CVProfile
from cvgenius.screens.profile_editor.profile_editor import ProfileEditorScreen


class DummyApp(MDApp):
    pass


class ProfileEditorBindingTests(unittest.TestCase):
    def test_profile_editor_syncs_text_fields_into_profile(self):
        app = DummyApp()
        screen = ProfileEditorScreen(name="profile_editor")

        screen.profile = CVProfile(
            full_name="Ada Lovelace",
            professional_title="Mathematician",
            email="ada@example.com",
            location="London",
            summary="Pioneer in computing.",
            skills=["Mathematics"],
            languages=["English"],
        )

        screen.sync_profile_to_fields()

        self.assertEqual(screen.ids.full_name.text, "Ada Lovelace")
        self.assertEqual(screen.ids.email.text, "ada@example.com")
        self.assertEqual(screen.ids.location.text, "London")
        self.assertEqual(screen.ids.summary.text, "Pioneer in computing.")
        self.assertEqual(screen.ids.skills.text, "Mathematics")
        self.assertEqual(screen.ids.languages.text, "English")


if __name__ == "__main__":
    unittest.main()
