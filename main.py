from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from cvgenius.screens.home.home_screen import HomeScreen
from cvgenius.screens.profile_editor.profile_editor import ProfileEditorScreen


class CVGeniusApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        screen_manager = ScreenManager()
        screen_manager.add_widget(HomeScreen(name="home"))
        screen_manager.add_widget(ProfileEditorScreen(name="profile_editor"))
        return screen_manager


if __name__ == "__main__":
    CVGeniusApp().run()
