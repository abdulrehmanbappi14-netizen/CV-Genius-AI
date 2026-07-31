from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import List

from cvgenius.data.templates.template_registry import get_template


@dataclass
class ExperienceEntry:
    role: str = ""
    company: str = ""
    location: str = ""
    years: str = ""
    details: str = ""


@dataclass
class EducationEntry:
    institution: str = ""
    degree: str = ""
    field_of_study: str = ""
    years: str = ""
    details: str = ""


@dataclass
class ProjectEntry:
    name: str = ""
    description: str = ""
    technologies: List[str] = field(default_factory=list)
    link: str = ""


@dataclass
class CertificationEntry:
    name: str = ""
    issuer: str = ""
    year: str = ""


@dataclass
class CVProfile:
    full_name: str = ""
    professional_title: str = ""
    email: str = ""
    phone: str = ""
    location: str = ""
    website: str = ""
    linkedin: str = ""
    github: str = ""
    summary: str = ""
    template_name: str = ""
    skills: List[str] = field(default_factory=list)
    experiences: List[ExperienceEntry] = field(default_factory=list)
    education: List[EducationEntry] = field(default_factory=list)
    projects: List[ProjectEntry] = field(default_factory=list)
    certifications: List[CertificationEntry] = field(default_factory=list)
    languages: List[str] = field(default_factory=list)
    achievements: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)

    def render_preview(self) -> str:
        skill_text = ", ".join(self.skills) if self.skills else "No skills listed"
        language_text = ", ".join(self.languages) if self.languages else "No languages listed"
        experience_text = "\n".join(
            [
                f"- {entry.role} at {entry.company} ({entry.years})"
                + (f" — {entry.details}" if entry.details else "")
                for entry in self.experiences
            ]
        ) or "No experience listed"
        education_text = "\n".join(
            [
                f"- {entry.institution} — {entry.degree} ({entry.years})"
                + (f" — {entry.details}" if entry.details else "")
                for entry in self.education
            ]
        ) or "No education listed"
        project_text = "\n".join(
            [
                f"- {entry.name}: {entry.description}"
                + (f" | Technologies: {', '.join(entry.technologies)}" if entry.technologies else "")
                + (f" | Link: {entry.link}" if entry.link else "")
                for entry in self.projects
            ]
        ) or "No projects listed"
        certification_text = "\n".join(
            [
                f"- {entry.name} — {entry.issuer} ({entry.year})"
                for entry in self.certifications
            ]
        ) or "No certifications listed"
        achievement_text = "\n".join(
            [f"- {achievement}" for achievement in self.achievements]
        ) or "No achievements listed"
        contact_lines = [
            f"Email: {self.email}" if self.email else None,
            f"Phone: {self.phone}" if self.phone else None,
            f"Location: {self.location}" if self.location else None,
            f"Website: {self.website}" if self.website else None,
            f"LinkedIn: {self.linkedin}" if self.linkedin else None,
            f"GitHub: {self.github}" if self.github else None,
        ]
        contact_text = "\n".join(line for line in contact_lines if line)

        template_key = self.template_name or "classic"

        try:
            template_label = get_template(template_key).label
        except KeyError:
            template_label = template_key

        return "\n".join(
            [
                f"Template: {template_label}",
                f"Name: {self.full_name or 'Unknown'}",
                f"Title: {self.professional_title or 'Professional'}",
                f"Summary: {self.summary or 'No summary available'}",
                f"Contact:\n{contact_text or 'No contact information provided'}",
                f"Skills: {skill_text}",
                f"Languages: {language_text}",
                f"Experience:\n{experience_text}",
                f"Education:\n{education_text}",
                f"Projects:\n{project_text}",
                f"Certifications:\n{certification_text}",
                f"Achievements:\n{achievement_text}",
            ]
        )

    def save_to_file(self, file_path: str | Path) -> None:
        path = Path(file_path)
        path.write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")

    @classmethod
    def from_dict(cls, data: dict) -> "CVProfile":
        experiences = [ExperienceEntry(**entry) for entry in data.get("experiences", [])]
        education = [EducationEntry(**entry) for entry in data.get("education", [])]
        projects = [ProjectEntry(**entry) for entry in data.get("projects", [])]
        certifications = [CertificationEntry(**entry) for entry in data.get("certifications", [])]

        return cls(
            full_name=data.get("full_name", ""),
            professional_title=data.get("professional_title", ""),
            email=data.get("email", ""),
            phone=data.get("phone", ""),
            location=data.get("location", ""),
            website=data.get("website", ""),
            linkedin=data.get("linkedin", ""),
            github=data.get("github", ""),
            summary=data.get("summary", ""),
            template_name=data.get("template_name", ""),
            skills=list(data.get("skills", [])),
            experiences=experiences,
            education=education,
            projects=projects,
            certifications=certifications,
            languages=list(data.get("languages", [])),
            achievements=list(data.get("achievements", [])),
        )

    @classmethod
    def load_from_file(cls, file_path: str | Path) -> "CVProfile":
        path = Path(file_path)
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls.from_dict(data)
