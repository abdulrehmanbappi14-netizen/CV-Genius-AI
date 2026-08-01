# CV Genius AI

An Android CV & Resume Builder app, built with Python (Kivy + KivyMD) and
packaged for Android with Buildozer.

## Status

✅ Feature-complete CV builder foundation verified in the current repo state.
The app now includes the shared profile model, editor navigation, template
selection, persistence/import-export, PDF export, and a provider-ready AI
abstraction with mock placeholder actions. See `PROJECT_PROGRESS.md` for
full implementation trail and the current Android packaging handoff.

## Tech stack

- **Kivy** — cross-platform Python UI framework (renders the app window,
  handles touch/input, runs the same on desktop and Android).
- **KivyMD** — Material Design widget library on top of Kivy (buttons,
  text fields, cards — the form-heavy UI a CV builder needs).
- **Buildozer** — packages the Kivy app into an installable Android APK.
  Buildozer's Android build step only runs on Linux/macOS/WSL, not native
  Windows — desktop runs (`python main.py`) work fine on Windows during
  development.

## Project layout

```
CV-Genius-AI/
├── main.py                     # app entry point
├── cvgenius/                   # main Python package
│   ├── screens/                # one subfolder per app screen (.py + matching .kv)
│   ├── widgets/                # reusable custom widgets
│   ├── models/                 # CV data models (future: Experience, Education, etc.)
│   ├── utils/                  # helpers (PDF export, storage, etc.)
│   └── data/templates/         # CV template definitions (future)
├── assets/                     # images, fonts, icons
├── tests/                      # test suite
├── buildozer.spec              # Android packaging config
├── requirements.txt
└── PROJECT_PROGRESS.md         # detailed build log - read this first
```

## Setup (Windows dev environment)

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

See `PROJECT_PROGRESS.md` for known setup caveats (Python version
compatibility with Kivy wheels) before running the above.

## Building the Android APK

The repo now includes a release-ready `buildozer.spec` baseline and
Android icon/splash assets. A real APK/AAB build still needs to be run in
Linux/macOS/WSL with Buildozer installed so the final Android packaging
pipeline can be verified end-to-end.
