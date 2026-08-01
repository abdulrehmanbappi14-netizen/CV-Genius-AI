import unittest

from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from cvgenius.models.cv_profile import CVProfile, ExperienceEntry, EducationEntry, ProjectEntry
from cvgenius.screens.education_editor.education_editor import EducationEditorScreen
from cvgenius.screens.experience_editor.experience_editor import ExperienceEditorScreen
from cvgenius.screens.profile_editor.profile_editor import ProfileEditorScreen
from cvgenius.screens.skills_editor.skills_editor import SkillsEditorScreen


class DummyApp(MDApp):
    pass


class StructuredEditorFlowTests(unittest.TestCase):
    def test_profile_editor_can_open_specialized_editors(self):
        app = DummyApp()
        manager = ScreenManager()
        editor = ProfileEditorScreen(name="profile_editor")
        experience_editor = ExperienceEditorScreen(name="experience_editor")
        education_editor = EducationEditorScreen(name="education_editor")
        skills_editor = SkillsEditorScreen(name="skills_editor")

        manager.add_widget(editor)
        manager.add_widget(experience_editor)
        manager.add_widget(education_editor)
        manager.add_widget(skills_editor)

        editor.profile = CVProfile(
            full_name="Ada Lovelace",
            skills=["Python", "Kivy"],
            experiences=[ExperienceEntry(role="Engineer", company="Analytical Engines", years="1842")],
            education=[EducationEntry(institution="University of London", degree="Mathematics", years="1833")],
            projects=[ProjectEntry(name="Analytical Engine", description="Computing machine prototype")],
        )

        editor.open_experience_editor()
        self.assertEqual(manager.current, "experience_editor")
        self.assertEqual(experience_editor.profile.full_name, "Ada Lovelace")
        self.assertEqual(experience_editor.profile.experiences[0].role, "Engineer")

        editor.open_education_editor()
        self.assertEqual(manager.current, "education_editor")
        self.assertEqual(education_editor.profile.education[0].institution, "University of London")

        editor.open_skills_editor()
        self.assertEqual(manager.current, "skills_editor")
        self.assertEqual(skills_editor.profile.skills, ["Python", "Kivy"])


if __name__ == "__main__":
    unittest.main()
