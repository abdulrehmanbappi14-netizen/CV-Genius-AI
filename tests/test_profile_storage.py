import tempfile
import unittest
from pathlib import Path

from cvgenius.models.cv_profile import CVProfile
from cvgenius.utils.profile_storage import load_profile, save_profile


class ProfileStorageTests(unittest.TestCase):
    def test_save_and_load_profile_round_trip(self):
        profile = CVProfile(
            full_name="Ada Lovelace",
            professional_title="Mathematician",
            email="ada@example.com",
            skills=["Mathematics", "Writing"],
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "profile.json"
            save_profile(profile, file_path)
            restored = load_profile(file_path)

        self.assertEqual(restored.full_name, profile.full_name)
        self.assertEqual(restored.professional_title, profile.professional_title)
        self.assertEqual(restored.email, profile.email)
        self.assertEqual(restored.skills, profile.skills)


if __name__ == "__main__":
    unittest.main()
