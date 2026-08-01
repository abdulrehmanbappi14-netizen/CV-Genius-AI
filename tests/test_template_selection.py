import unittest

from kivymd.app import MDApp

from cvgenius.data.templates.template_registry import get_available_templates
from cvgenius.screens.profile_editor.profile_editor import ProfileEditorScreen


class DummyApp(MDApp):
    pass


class TemplateSelectionTests(unittest.TestCase):
    def test_profile_editor_returns_registry_template_choices(self):
        app = DummyApp()
        screen = ProfileEditorScreen(name="profile_editor")

        choices = screen.get_template_choices()

        self.assertEqual(
            [item.name for item in choices],
            [item.name for item in get_available_templates()],
        )


if __name__ == "__main__":
    unittest.main()
