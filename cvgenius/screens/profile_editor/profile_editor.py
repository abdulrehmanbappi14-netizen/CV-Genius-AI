from pathlib import Path

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from cvgenius.data.templates.template_registry import get_available_templates, get_template
from cvgenius.models.cv_profile import (
    CVProfile,
    CertificationEntry,
    EducationEntry,
    ExperienceEntry,
    ProjectEntry,
)
from cvgenius.utils.exporter import export_profile_text
from cvgenius.utils.profile_storage import load_profile, save_profile

Builder.load_file(__file__.replace(".py", ".kv"))


class ProfileEditorScreen(Screen):
    """Profile editor screen for CV data entry and preview orchestration.

    The screen holds a single `CVProfile` instance that is populated from
    form fields and used for preview/export workflows. Phase 4 adds a
    simple template-selection pathway so the chosen template can drive
    the live preview output.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.profile = CVProfile()

    def get_template_choices(self):
        return get_available_templates()

    def apply_template_choice(self, template_name: str) -> None:
        if template_name in {item.name for item in self.get_template_choices()}:
            self.profile.template_name = template_name
            if "template_name" in self.ids:
                self.ids.template_name.text = template_name
            self.sync_fields_to_profile()

    def update_preview_from_profile(self) -> None:
        manager = self.manager
        if manager is not None:
            preview_screen = manager.get_screen("template_preview")
            preview_screen.profile = self.profile
            preview_screen.refresh_preview()
            manager.current = "template_preview"

    def sync_profile_to_fields(self) -> None:
        if "full_name" in self.ids:
            self.ids.full_name.text = self.profile.full_name
        if "professional_title" in self.ids:
            self.ids.professional_title.text = self.profile.professional_title
        if "email" in self.ids:
            self.ids.email.text = self.profile.email
        if "phone" in self.ids:
            self.ids.phone.text = self.profile.phone
        if "location" in self.ids:
            self.ids.location.text = self.profile.location
        if "website" in self.ids:
            self.ids.website.text = self.profile.website
        if "linkedin" in self.ids:
            self.ids.linkedin.text = self.profile.linkedin
        if "github" in self.ids:
            self.ids.github.text = self.profile.github
        if "summary" in self.ids:
            self.ids.summary.text = self.profile.summary
        if "template_name" in self.ids:
            self.ids.template_name.text = self.profile.template_name
        if "skills" in self.ids:
            self.ids.skills.text = ", ".join(self.profile.skills)
        if "languages" in self.ids:
            self.ids.languages.text = ", ".join(self.profile.languages)
        if "experience" in self.ids:
            self.ids.experience.text = "\n".join(
                f"{item.role} - {item.company} ({item.years}) :: {item.details}".strip()
                for item in self.profile.experiences
            )
        if "education" in self.ids:
            self.ids.education.text = "\n".join(
                f"{item.institution} - {item.degree} ({item.years}) :: {item.details}".strip()
                for item in self.profile.education
            )
        if "projects" in self.ids:
            self.ids.projects.text = "\n".join(
                f"{item.name} :: {item.description}".strip() for item in self.profile.projects
            )
        if "certifications" in self.ids:
            self.ids.certifications.text = "\n".join(
                f"{item.name} - {item.issuer} ({item.year})".strip()
                for item in self.profile.certifications
            )
        if "achievements" in self.ids:
            self.ids.achievements.text = "\n".join(self.profile.achievements)

    def sync_fields_to_profile(self) -> None:
        if "full_name" in self.ids:
            self.profile.full_name = self.ids.full_name.text
        if "professional_title" in self.ids:
            self.profile.professional_title = self.ids.professional_title.text
        if "email" in self.ids:
            self.profile.email = self.ids.email.text
        if "phone" in self.ids:
            self.profile.phone = self.ids.phone.text
        if "location" in self.ids:
            self.profile.location = self.ids.location.text
        if "website" in self.ids:
            self.profile.website = self.ids.website.text
        if "linkedin" in self.ids:
            self.profile.linkedin = self.ids.linkedin.text
        if "github" in self.ids:
            self.profile.github = self.ids.github.text
        if "summary" in self.ids:
            self.profile.summary = self.ids.summary.text
        if "template_name" in self.ids:
            self.profile.template_name = self.ids.template_name.text
        if "skills" in self.ids:
            self.profile.skills = [item.strip() for item in self.ids.skills.text.split(",") if item.strip()]
        if "languages" in self.ids:
            self.profile.languages = [item.strip() for item in self.ids.languages.text.split(",") if item.strip()]
        if "experience" in self.ids:
            self.profile.experiences = [
                ExperienceEntry(role=line.strip(), details="")
                for line in self.ids.experience.text.splitlines()
                if line.strip()
            ]
        if "education" in self.ids:
            self.profile.education = [
                EducationEntry(institution=line.strip(), details="")
                for line in self.ids.education.text.splitlines()
                if line.strip()
            ]
        if "projects" in self.ids:
            self.profile.projects = [
                ProjectEntry(name=line.strip(), description="")
                for line in self.ids.projects.text.splitlines()
                if line.strip()
            ]
        if "certifications" in self.ids:
            self.profile.certifications = [
                CertificationEntry(name=line.strip(), issuer="", year="")
                for line in self.ids.certifications.text.splitlines()
                if line.strip()
            ]
        if "achievements" in self.ids:
            self.profile.achievements = [
                line.strip() for line in self.ids.achievements.text.splitlines() if line.strip()
            ]

    def save_profile(self, file_path: str | Path) -> None:
        self.sync_fields_to_profile()
        save_profile(self.profile, file_path)

    def import_profile(self, file_path: str | Path) -> None:
        self.profile = load_profile(file_path)
        self.sync_profile_to_fields()

    def export_profile(self, file_path: str | Path) -> None:
        self.sync_fields_to_profile()
        export_profile_text(self.profile, file_path)

    def preview_resume(self) -> None:
        manager = self.manager
        if manager is not None:
            syncable_fields = (
                "full_name",
                "professional_title",
                "email",
                "phone",
                "location",
                "website",
                "linkedin",
                "github",
                "summary",
                "template_name",
                "skills",
                "languages",
                "experience",
                "education",
                "projects",
                "certifications",
                "achievements",
            )
            has_field_text = any(
                getattr(self.ids.get(field), "text", "")
                for field in syncable_fields
                if field in self.ids
            )
            if has_field_text:
                self.sync_fields_to_profile()

            self.update_preview_from_profile()

    def load_profile(self, file_path: str | Path) -> None:
        self.profile = load_profile(file_path)
        self.sync_profile_to_fields()

    def _has_any_field_text(self) -> bool:
        syncable_fields = (
            "full_name",
            "professional_title",
            "email",
            "phone",
            "location",
            "website",
            "linkedin",
            "github",
            "summary",
            "template_name",
            "skills",
            "languages",
            "experience",
            "education",
            "projects",
            "certifications",
            "achievements",
        )
        return any(
            bool(getattr(self.ids.get(field), "text", ""))
            for field in syncable_fields
            if field in self.ids
        )

    def open_experience_editor(self) -> None:
        manager = self.manager
        if manager is not None:
            if self._has_any_field_text():
                self.sync_fields_to_profile()
            experience_screen = manager.get_screen("experience_editor")
            experience_screen.set_profile(self.profile)
            experience_screen.sync_profile_to_fields()
            manager.current = "experience_editor"

    def open_education_editor(self) -> None:
        manager = self.manager
        if manager is not None:
            if self._has_any_field_text():
                self.sync_fields_to_profile()
            education_screen = manager.get_screen("education_editor")
            education_screen.set_profile(self.profile)
            education_screen.sync_profile_to_fields()
            manager.current = "education_editor"

    def open_skills_editor(self) -> None:
        manager = self.manager
        if manager is not None:
            if self._has_any_field_text():
                self.sync_fields_to_profile()
            skills_screen = manager.get_screen("skills_editor")
            skills_screen.set_profile(self.profile)
            skills_screen.sync_profile_to_fields()
            manager.current = "skills_editor"
