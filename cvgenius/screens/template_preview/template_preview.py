from pathlib import Path

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from cvgenius.models.cv_profile import CVProfile

Builder.load_file(__file__.replace(".py", ".kv"))


class TemplatePreviewScreen(Screen):
    """Minimal preview screen for a CV profile."""

    def __init__(self, **kwargs):
        self.profile = CVProfile()
        super().__init__(**kwargs)

    def get_preview_text(self) -> str:
        if not hasattr(self, "profile"):
            self.profile = CVProfile()
        return self.profile.render_preview()

    def export_preview_to_file(self, file_path: str | Path) -> None:
        path = Path(file_path)
        path.write_text(self.get_preview_text(), encoding="utf-8")
