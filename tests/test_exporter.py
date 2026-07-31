import tempfile
import unittest
from pathlib import Path

from cvgenius.models.cv_profile import CVProfile
from cvgenius.utils.exporter import export_profile_text


class ExporterTests(unittest.TestCase):
    def test_export_profile_text_writes_resume_content(self):
        profile = CVProfile(
            full_name="Ada Lovelace",
            professional_title="Mathematician",
            summary="Pioneer in computing.",
            skills=["Mathematics", "Research"],
            template_name="classic",
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "resume.txt"
            export_profile_text(profile, file_path)
            content = file_path.read_text(encoding="utf-8")

        self.assertIn("Ada Lovelace", content)
        self.assertIn("Mathematician", content)
        self.assertIn("Pioneer in computing.", content)
        self.assertIn("Classic Resume", content)


if __name__ == "__main__":
    unittest.main()
