from pathlib import Path

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from cvgenius.models.cv_profile import (
    CVProfile,
    CertificationEntry,
    EducationEntry,
    ExperienceEntry,
    ProjectEntry,
)
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
        self.ids.template_name.text = self.profile.template_name
        self.ids.skills.text = ", ".join(self.profile.skills)
        self.ids.languages.text = ", ".join(self.profile.languages)
        self.ids.experience.text = "\n".join(
            f"{item.role} - {item.company} ({item.years}) :: {item.details}".strip()
            for item in self.profile.experiences
        )
        self.ids.education.text = "\n".join(
            f"{item.institution} - {item.degree} ({item.years}) :: {item.details}".strip()
            for item in self.profile.education
        )
        self.ids.projects.text = "\n".join(
            f"{item.name} :: {item.description}".strip() for item in self.profile.projects
        )
        self.ids.certifications.text = "\n".join(
            f"{item.name} - {item.issuer} ({item.year})".strip()
            for item in self.profile.certifications
        )
        self.ids.achievements.text = "\n".join(self.profile.achievements)

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
        self.profile.template_name = self.ids.template_name.text
        self.profile.skills = [item.strip() for item in self.ids.skills.text.split(",") if item.strip()]
        self.profile.languages = [item.strip() for item in self.ids.languages.text.split(",") if item.strip()]

        self.profile.experiences = [
            ExperienceEntry(role=line.strip(), details="")
            for line in self.ids.experience.text.splitlines()
            if line.strip()
        ]
        self.profile.education = [
            EducationEntry(institution=line.strip(), details="")
            for line in self.ids.education.text.splitlines()
            if line.strip()
        ]
        self.profile.projects = [
            ProjectEntry(name=line.strip(), description="")
            for line in self.ids.projects.text.splitlines()
            if line.strip()
        ]
        self.profile.certifications = [
            CertificationEntry(name=line.strip(), issuer="", year="")
            for line in self.ids.certifications.text.splitlines()
            if line.strip()
        ]
        self.profile.achievements = [
            line.strip() for line in self.ids.achievements.text.splitlines() if line.strip()
        ]

    def save_profile(self, file_path: str | Path) -> None:
        self.sync_fields_to_profile()
        save_profile(self.profile, file_path)

    def load_profile(self, file_path: str | Path) -> None:
        self.profile = load_profile(file_path)
        self.sync_profile_to_fields()
