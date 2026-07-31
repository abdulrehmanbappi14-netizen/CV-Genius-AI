import unittest

from cvgenius.models.cv_profile import (
    CVProfile,
    CertificationEntry,
    ExperienceEntry,
    ProjectEntry,
)


class CVProfileTests(unittest.TestCase):
    def test_profile_stores_basic_fields(self):
        profile = CVProfile(
            full_name="Ada Lovelace",
            professional_title="Mathematician",
            email="ada@example.com",
            phone="+123456789",
            website="https://ada.example",
            linkedin="https://linkedin.com/in/ada",
            github="https://github.com/ada",
            summary="Mathematician and writer.",
        )

        self.assertEqual(profile.full_name, "Ada Lovelace")
        self.assertEqual(profile.professional_title, "Mathematician")
        self.assertEqual(profile.email, "ada@example.com")
        self.assertEqual(profile.phone, "+123456789")
        self.assertEqual(profile.website, "https://ada.example")
        self.assertEqual(profile.linkedin, "https://linkedin.com/in/ada")
        self.assertEqual(profile.github, "https://github.com/ada")
        self.assertEqual(profile.summary, "Mathematician and writer.")

    def test_profile_can_add_experience(self):
        profile = CVProfile(full_name="Ada Lovelace")
        profile.experiences.append(
            ExperienceEntry(role="Analyst", company="Analytical Engine Co.", years="1843")
        )

        self.assertEqual(len(profile.experiences), 1)
        self.assertEqual(profile.experiences[0].role, "Analyst")

    def test_profile_can_add_projects_and_certifications(self):
        profile = CVProfile(full_name="Ada Lovelace")
        profile.projects.append(
            ProjectEntry(
                name="Analytical Engine Notes",
                description="Research notes for early computation.",
                technologies=["Math", "Writing"],
                link="https://example.com/project",
            )
        )
        profile.certifications.append(
            CertificationEntry(name="Advanced Computation", issuer="Royal Society", year="1843")
        )

        self.assertEqual(len(profile.projects), 1)
        self.assertEqual(profile.projects[0].name, "Analytical Engine Notes")
        self.assertEqual(len(profile.certifications), 1)
        self.assertEqual(profile.certifications[0].issuer, "Royal Society")

    def test_profile_can_round_trip_to_dict(self):
        profile = CVProfile(
            full_name="Ada Lovelace",
            email="ada@example.com",
            skills=["Mathematics", "Writing"],
            languages=["English", "French"],
            achievements=["First published algorithm"],
        )

        payload = profile.to_dict()
        restored = CVProfile.from_dict(payload)

        self.assertEqual(restored.full_name, profile.full_name)
        self.assertEqual(restored.email, profile.email)
        self.assertEqual(restored.skills, profile.skills)
        self.assertEqual(restored.languages, profile.languages)
        self.assertEqual(restored.achievements, profile.achievements)


if __name__ == "__main__":
    unittest.main()
