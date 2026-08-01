from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file(__file__.replace(".py", ".kv"))


class HomeScreen(Screen):
    """Dashboard-style landing screen for the CV builder.

    The home screen now acts as the entry point into the profile editor
    and preview flow, providing a minimal but real navigation surface
    for the growing app.
    """

    def open_profile_editor(self) -> None:
        manager = self.manager
        if manager is not None:
            manager.current = "profile_editor"

    def open_template_preview(self) -> None:
        manager = self.manager
        if manager is not None:
            manager.current = "template_preview"
