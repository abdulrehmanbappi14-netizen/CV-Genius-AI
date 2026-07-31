from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from cvgenius.models.cv_profile import CVProfile

Builder.load_file(__file__.replace(".py", ".kv"))


class ProfileEditorScreen(Screen):
    """Minimal profile editor screen used for Stage 2.

    The screen holds a single `CVProfile` instance that will later be
    populated from form fields and used for preview/export workflows.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.profile = CVProfile()
