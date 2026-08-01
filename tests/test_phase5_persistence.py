import tempfile
import unittest
from pathlib import Path

from kivymd.app import MDApp

from cvgenius.screens.profile_editor.profile_editor import ProfileEditorScreen
from cvgenius.utils.exporter import export_profile_text


class DummyApp(MDApp):
    pass


class Phase5PersistenceTests(unittest.TestCase):
    def test_profile_editor_can_import_and_export_profile_workflow(self):
        app = DummyApp()
        screen = ProfileEditorScreen(name="profile_editor")
        screen.profile.full_name = "Ada Lovelace"
        screen.profile.professional_title = "Mathematician"
        screen.profile.summary = "Pioneer in computing."
        screen.profile.skills = ["Mathematics"]
        screen.profile.template_name = "classic"
        screen.sync_profile_to_fields()

        with tempfile.TemporaryDirectory() as tmp_dir:
            json_path = Path(tmp_dir) / "profile.json"
            text_path = Path(tmp_dir) / "profile.txt"

            screen.save_profile(json_path)
            screen.import_profile(json_path)
            screen.export_profile(text_path)
            exported = text_path.read_text(encoding="utf-8")

        self.assertEqual(screen.profile.full_name, "Ada Lovelace")
        self.assertEqual(screen.profile.professional_title, "Mathematician")
        self.assertEqual(screen.profile.template_name, "classic")
        self.assertIn("Ada Lovelace", exported)
        self.assertIn("Classic Resume", exported)


if __name__ == "__main__":
    unittest.main()
