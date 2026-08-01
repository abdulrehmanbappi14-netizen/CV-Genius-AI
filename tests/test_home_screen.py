import unittest

from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from cvgenius.screens.home.home_screen import HomeScreen
from cvgenius.screens.profile_editor.profile_editor import ProfileEditorScreen


class DummyApp(MDApp):
    pass


class HomeScreenTests(unittest.TestCase):
    def test_home_screen_can_navigate_to_profile_editor(self):
        app = DummyApp()
        manager = ScreenManager()
        home = HomeScreen(name="home")
        editor = ProfileEditorScreen(name="profile_editor")

        manager.add_widget(home)
        manager.add_widget(editor)
        manager.current = "home"

        home.open_profile_editor()

        self.assertEqual(manager.current, "profile_editor")


if __name__ == "__main__":
    unittest.main()
