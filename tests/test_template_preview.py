import unittest

from cvgenius.models.cv_profile import (
    CVProfile,
    CertificationEntry,
    EducationEntry,
    ExperienceEntry,
    ProjectEntry,
)


class TemplatePreviewTests(unittest.TestCase):
    def test_profile_preview_uses_template_name_and_sections(self):
        profile = CVProfile(
            full_name="Ada Lovelace",
            professional_title="Mathematician",
            summary="Pioneer in computing.",
            skills=["Mathematics", "Research"],
            languages=["English", "French"],
            template_name="classic",
            experiences=[
                ExperienceEntry(
                    role="Analyst",
                    company="Analytical Engine Co.",
                    years="1843",
                    details="Published early computational notes.",
                )
            ],
            education=[
                EducationEntry(
                    institution="Royal Society Academy",
                    degree="Advanced Study",
                    years="1842",
                    details="Focused on mathematics and computation.",
                )
            ],
            projects=[
                ProjectEntry(
                    name="Analytical Engine Notes",
                    description="Research notes for early computation.",
                    technologies=["Math", "Writing"],
                )
            ],
            certifications=[
                CertificationEntry(name="Advanced Computation", issuer="Royal Society", year="1843")
            ],
            achievements=["First published algorithm"],
        )

        preview = profile.render_preview()

        self.assertIn("Ada Lovelace", preview)
        self.assertIn("Classic Resume", preview)
        self.assertIn("Pioneer in computing.", preview)
        self.assertIn("Mathematics", preview)
        self.assertIn("English", preview)
        self.assertIn("Analyst", preview)
        self.assertIn("Royal Society Academy", preview)
        self.assertIn("Analytical Engine Notes", preview)
        self.assertIn("Advanced Computation", preview)
        self.assertIn("First published algorithm", preview)


if __name__ == "__main__":
    unittest.main()
