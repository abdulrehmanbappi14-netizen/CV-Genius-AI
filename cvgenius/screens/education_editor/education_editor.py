from pathlib import Path

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from cvgenius.models.cv_profile import CVProfile, EducationEntry

Builder.load_file(__file__.replace(".py", ".kv"))


class EducationEditorScreen(Screen):
    """Specialized editor for a resume's education entries."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.profile = CVProfile()

    def set_profile(self, profile: CVProfile) -> None:
        self.profile = profile

    def sync_profile_to_fields(self) -> None:
        if "education_text" in self.ids:
            self.ids.education_text.text = "\n".join(
                f"{item.institution} | {item.degree} | {item.years} | {item.details}".strip()
                for item in self.profile.education
            )

    def sync_fields_to_profile(self) -> None:
        if "education_text" in self.ids:
            self.profile.education = [
                EducationEntry(institution=line.strip(), degree="", years="", details="")
                for line in self.ids.education_text.text.splitlines()
                if line.strip()
            ]

    def save_profile(self, file_path: str | Path) -> None:
        self.sync_fields_to_profile()
        self.profile.save_to_file(file_path)

    def back_to_profile_editor(self) -> None:
        manager = self.manager
        if manager is not None:
            manager.current = "profile_editor"
