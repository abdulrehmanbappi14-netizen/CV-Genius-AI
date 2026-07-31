from __future__ import annotations

import json
from pathlib import Path

from cvgenius.models.cv_profile import CVProfile


def save_profile(profile: CVProfile, file_path: str | Path) -> None:
    path = Path(file_path)
    path.write_text(json.dumps(profile.to_dict(), indent=2), encoding="utf-8")


def load_profile(file_path: str | Path) -> CVProfile:
    path = Path(file_path)
    data = json.loads(path.read_text(encoding="utf-8"))
    return CVProfile.from_dict(data)
