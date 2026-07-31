from pathlib import Path

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from cvgenius.models.cv_profile import CVProfile
from cvgenius.utils.profile_storage import load_profile, save_profile

Builder.load_file(__file__.replace(".py", ".kv"))


class ProfileEditorScreen(Screen):
    """Minimal profile editor screen used for Stage 2.

    The screen holds a single `CVProfile` instance that will later be
    populated from form fields and used for preview/export workflows.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.profile = CVProfile()

    def sync_profile_to_fields(self) -> None:
        self.ids.full_name.text = self.profile.full_name
        self.ids.professional_title.text = self.profile.professional_title
        self.ids.email.text = self.profile.email
        self.ids.phone.text = self.profile.phone
        self.ids.location.text = self.profile.location
        self.ids.website.text = self.profile.website
        self.ids.linkedin.text = self.profile.linkedin
        self.ids.github.text = self.profile.github
        self.ids.summary.text = self.profile.summary
        self.ids.skills.text = ", ".join(self.profile.skills)
        self.ids.languages.text = ", ".join(self.profile.languages)

    def sync_fields_to_profile(self) -> None:
        self.profile.full_name = self.ids.full_name.text
        self.profile.professional_title = self.ids.professional_title.text
        self.profile.email = self.ids.email.text
        self.profile.phone = self.ids.phone.text
        self.profile.location = self.ids.location.text
        self.profile.website = self.ids.website.text
        self.profile.linkedin = self.ids.linkedin.text
        self.profile.github = self.ids.github.text
        self.profile.summary = self.ids.summary.text
        self.profile.skills = [item.strip() for item in self.ids.skills.text.split(",") if item.strip()]
        self.profile.languages = [item.strip() for item in self.ids.languages.text.split(",") if item.strip()]

    def save_profile(self, file_path: str | Path) -> None:
        self.sync_fields_to_profile()
        save_profile(self.profile, file_path)

    def load_profile(self, file_path: str | Path) -> None:
        self.profile = load_profile(file_path)
        self.sync_profile_to_fields()
