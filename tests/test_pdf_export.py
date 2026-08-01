import tempfile
import unittest
from pathlib import Path

from pypdf import PdfReader

from cvgenius.models.cv_profile import CVProfile
from cvgenius.utils.exporter import export_profile_pdf


class PDFExportTests(unittest.TestCase):
    def test_pdf_export_generates_professional_resume_document(self):
        profile = CVProfile(
            full_name="Ada Lovelace",
            professional_title="Mathematician",
            email="ada@example.com",
            phone="555-0101",
            location="London",
            summary="Pioneer in computing.",
            skills=["Mathematics", "Research"],
            languages=["English"],
            template_name="classic",
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "resume.pdf"
            export_profile_pdf(profile, file_path)
            self.assertTrue(file_path.exists())
            self.assertGreater(file_path.stat().st_size, 0)

            reader = PdfReader(str(file_path))
            text = "\n".join(page.extract_text() or "" for page in reader.pages)

        self.assertIn("Ada Lovelace", text)
        self.assertIn("Mathematician", text)
        self.assertIn("Pioneer in computing.", text)
        self.assertIn("Skills", text)
        self.assertIn("Mathematics", text)

    def test_pdf_export_supports_multiple_templates(self):
        profile = CVProfile(
            full_name="Grace Hopper",
            professional_title="Computer Scientist",
            summary="Pioneer in compiler design.",
            template_name="modern",
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "modern_resume.pdf"
            export_profile_pdf(profile, file_path)
            self.assertTrue(file_path.exists())
            self.assertGreater(file_path.stat().st_size, 0)

            reader = PdfReader(str(file_path))
            text = "\n".join(page.extract_text() or "" for page in reader.pages)

        self.assertIn("Grace Hopper", text)
        self.assertIn("Computer Scientist", text)
        self.assertIn("Pioneer in compiler design.", text)


if __name__ == "__main__":
    unittest.main()
