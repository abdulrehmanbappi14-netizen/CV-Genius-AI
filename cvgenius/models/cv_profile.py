from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import List


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
    skills: List[str] = field(default_factory=list)
    experiences: List[ExperienceEntry] = field(default_factory=list)
    education: List[EducationEntry] = field(default_factory=list)
    projects: List[ProjectEntry] = field(default_factory=list)
    certifications: List[CertificationEntry] = field(default_factory=list)
    languages: List[str] = field(default_factory=list)
    achievements: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)

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
            skills=list(data.get("skills", [])),
            experiences=experiences,
            education=education,
            projects=projects,
            certifications=certifications,
            languages=list(data.get("languages", [])),
            achievements=list(data.get("achievements", [])),
        )
