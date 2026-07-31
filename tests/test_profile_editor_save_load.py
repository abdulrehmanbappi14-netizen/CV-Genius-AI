import tempfile
import unittest
from pathlib import Path

from kivymd.app import MDApp

from cvgenius.screens.profile_editor.profile_editor import ProfileEditorScreen


class DummyApp(MDApp):
    pass


class ProfileEditorSaveLoadTests(unittest.TestCase):
    def test_screen_can_save_and_load_profile_from_file(self):
        app = DummyApp()
        screen = ProfileEditorScreen(name="profile_editor")

        screen.profile.full_name = "Ada Lovelace"
        screen.profile.email = "ada@example.com"
        screen.profile.location = "London"
        screen.profile.summary = "Pioneer in computing."
        screen.profile.skills = ["Mathematics"]
        screen.profile.languages = ["English"]

        screen.sync_profile_to_fields()

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "resume.json"
            screen.save_profile(file_path)
            screen.load_profile(file_path)

        self.assertEqual(screen.profile.full_name, "Ada Lovelace")
        self.assertEqual(screen.profile.email, "ada@example.com")
        self.assertEqual(screen.profile.location, "London")
        self.assertEqual(screen.profile.summary, "Pioneer in computing.")
        self.assertEqual(screen.profile.skills, ["Mathematics"])
        self.assertEqual(screen.profile.languages, ["English"])


if __name__ == "__main__":
    unittest.main()
