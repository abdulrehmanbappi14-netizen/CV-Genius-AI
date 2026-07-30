from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file(__file__.replace(".py", ".kv"))


class HomeScreen(Screen):
    """Landing screen shown when the app opens. Placeholder for Day 1 -
    this proves the Kivy/KivyMD toolchain and screen-loading pattern
    work end-to-end before any real CV-builder features are added."""
    pass
