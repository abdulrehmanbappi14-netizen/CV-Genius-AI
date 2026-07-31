from __future__ import annotations

from pathlib import Path

from cvgenius.models.cv_profile import CVProfile


def export_profile_text(profile: CVProfile, file_path: str | Path) -> None:
    path = Path(file_path)
    preview = profile.render_preview()
    path.write_text(preview, encoding="utf-8")
