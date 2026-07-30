# CV Genius AI

An Android CV & Resume Builder app, built with Python (Kivy + KivyMD) and
packaged for Android with Buildozer.

## Status

🚧 Project skeleton only — no CV-builder features implemented yet. See
`PROJECT_PROGRESS.md` for the detailed build log and the exact next task.

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

Requires Buildozer on Linux/macOS/WSL (not covered yet — see
`PROJECT_PROGRESS.md` next-task section).
