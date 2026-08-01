from pathlib import Path

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from cvgenius.models.cv_profile import CVProfile

Builder.load_file(__file__.replace(".py", ".kv"))


class SkillsEditorScreen(Screen):
    """Specialized editor for a resume's skills list."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.profile = CVProfile()

    def set_profile(self, profile: CVProfile) -> None:
        self.profile = profile

    def sync_profile_to_fields(self) -> None:
        if "skills_text" in self.ids:
            self.ids.skills_text.text = ", ".join(self.profile.skills)

    def sync_fields_to_profile(self) -> None:
        if "skills_text" in self.ids:
            self.profile.skills = [
                item.strip()
                for item in self.ids.skills_text.text.split(",")
                if item.strip()
            ]

    def save_profile(self, file_path: str | Path) -> None:
        self.sync_fields_to_profile()
        self.profile.save_to_file(file_path)

    def back_to_profile_editor(self) -> None:
        manager = self.manager
        if manager is not None:
            manager.current = "profile_editor"
