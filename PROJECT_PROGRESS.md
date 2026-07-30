# CV Genius AI — Project Progress

_Last updated: 2026-07-31 (Day 1)_

This file is the single source of truth for where this project stands.
If you're picking this back up after days away, read this top to bottom
before touching code.

---

## 1. What this project is

**CV Genius AI** — an Android CV & Resume Builder app, built step by step
using Python, VS Code, GitHub, and Git.

- **UI framework:** Kivy + KivyMD (Material Design widgets on top of
  Kivy — chosen because it's the most common, best-documented path for a
  pure-Python Android app, and KivyMD's form/card widgets fit a
  CV-builder UI well).
- **Android packaging:** Buildozer (builds the Kivy app into an
  installable `.apk`). Buildozer's Android build step only runs on
  Linux/macOS/WSL — desktop development and testing happens directly on
  Windows via `python main.py`, and packaging to APK is a separate later
  step once there's something worth packaging.

This is a **brand new project** — started 2026-07-31, right after
wrapping up (and pausing) work on the separate `AI_Bitcoin_Trading_App`
project. That project is unrelated and untouched by this one.

## 2. Project layout on disk

```
C:\Users\Acer User\Downloads\CV-Genius-AI\
├── main.py                          ← app entry point (creates CVGeniusApp(MDApp), loads HomeScreen)
├── cvgenius\                        ← main Python package
│   ├── __init__.py
│   ├── screens\                     ← one subfolder per app screen
│   │   ├── __init__.py
│   │   └── home\
│   │       ├── __init__.py
│   │       ├── home_screen.py       ← HomeScreen(Screen) - Day 1 placeholder screen
│   │       └── home_screen.kv       ← KV layout for HomeScreen (MDBoxLayout + 2 MDLabels)
│   ├── widgets\__init__.py          ← empty - reusable custom widgets go here later
│   ├── models\__init__.py           ← empty - CV data models (Experience, Education, etc.) go here later
│   ├── utils\__init__.py            ← empty - helpers (PDF export, storage, etc.) go here later
│   └── data\templates\.gitkeep      ← empty - CV template definitions go here later
├── assets\
│   ├── images\.gitkeep              ← empty - also needs presplash.png eventually (see §7)
│   ├── fonts\.gitkeep               ← empty
│   └── icons\.gitkeep               ← empty - also needs icon.png eventually (see §7)
├── tests\__init__.py                ← empty test package, no tests written yet
├── docs\                            ← empty, reserved for future design notes
├── buildozer.spec                   ← Android packaging config (title/package/requirements set; icon+presplash paths point to files that don't exist yet)
├── requirements.txt                 ← kivy>=2.3.1, kivymd>=1.2.0 (buildozer commented out - install separately in WSL/Linux, not the Windows venv)
├── .gitignore                       ← Python/Kivy/Buildozer/VS Code/OS entries
├── README.md                        ← setup instructions, project layout, status
└── PROJECT_PROGRESS.md              ← this file
```

## 3. What's implemented so far (Day 1)

- Full folder skeleton created (see §2) — organized so screens, widgets,
  models, utils, and data templates each have an obvious home as the app
  grows, without over-building anything not needed yet.
- `main.py`: a minimal `CVGeniusApp(MDApp)` that sets a blue/light
  KivyMD theme and shows a single `HomeScreen` via `ScreenManager`.
- `HomeScreen`: a placeholder screen (`cvgenius/screens/home/`) that
  just proves the Kivy + KivyMD + `.kv`-file-loading pattern works
  end-to-end — it shows "CV Genius AI" as a title label and a subtitle
  confirming the skeleton is running. **No CV-builder functionality
  exists yet** — this is intentionally just scaffolding, per the
  "step by step" approach.
- `buildozer.spec` written by hand (Buildozer isn't installed yet, so
  this wasn't generated via `buildozer init` — it follows the standard
  template): app title "CV Genius AI", package
  `org.cvgenius.cvgeniusai`, portrait orientation, Kivy 2.3.1 + KivyMD
  1.2.0 pinned as requirements, Android API 34 / minAPI 24.
- `requirements.txt`, `.gitignore`, `README.md` written.

**Nothing has been run yet** — `main.py` has not been executed
successfully because of the environment blockers in §4. The code has
been written carefully to match standard Kivy/KivyMD patterns but has
**not been visually verified to actually launch a window**. Treat it as
unverified until §9 step 1 is done.

## 4. Environment findings (important — read before installing anything)

Checked on 2026-07-31, this machine:

- **Git was not installed** (not on PATH, not in `C:\Program Files\Git`,
  not in `%LOCALAPPDATA%\Programs\Git`). `git init` could not be run
  until this was fixed.
- **Only Python 3.14.6 was installed** (checked via `py --list` — no
  3.11/3.12/3.13 available). Kivy's latest PyPI release (2.3.1) has
  **no prebuilt wheel for Python 3.14** — confirmed by running
  `pip install kivy==2.3.1 --dry-run`, which fell back to building from
  source and **failed while installing its own build dependencies**
  (setuptools/wheel/packaging build backend step errored out). Kivy is
  simply too new-Python-incompatible right now; this is a Kivy/PyPI
  ecosystem lag issue, not something fixable by changing this project's
  code.
- **Fix applied:** user chose to install both via `winget` (see §6 for
  exact outcome/versions once confirmed — update this section after
  installs finish if picking this up mid-setup).
  - `winget install --id Git.Git -e --accept-package-agreements --accept-source-agreements --silent`
  - `winget install --id Python.Python.3.12 -e --accept-package-agreements --accept-source-agreements --silent`
- **Why Python 3.12 specifically:** it's a recent, stable release with
  mature Kivy wheel support, while staying close to current. Do **not**
  use the system's Python 3.14 for this project's virtual environment —
  create the venv with `py -3.12 -m venv .venv` explicitly (see §9).

## 5. Bug fixes completed

None yet — no code has been run yet, so nothing to fix. (See §3 —
`main.py` is unverified.)

## 6. Files created or modified so far

| File | Change |
|---|---|
| `main.py` | Created — KivyMD app entry point. |
| `cvgenius/__init__.py`, `cvgenius/screens/__init__.py`, `cvgenius/screens/home/__init__.py`, `cvgenius/widgets/__init__.py`, `cvgenius/models/__init__.py`, `cvgenius/utils/__init__.py` | Created — empty package markers. |
| `cvgenius/screens/home/home_screen.py` | Created — `HomeScreen(Screen)` placeholder, loads matching `.kv`. |
| `cvgenius/screens/home/home_screen.kv` | Created — KV layout for `HomeScreen`. |
| `cvgenius/data/templates/.gitkeep`, `assets/images/.gitkeep`, `assets/fonts/.gitkeep`, `assets/icons/.gitkeep` | Created — placeholders so git tracks these otherwise-empty folders. |
| `tests/__init__.py` | Created — empty test package. |
| `requirements.txt` | Created. |
| `buildozer.spec` | Created (hand-written, not `buildozer init`-generated — Buildozer isn't installed on this machine yet). |
| `.gitignore` | Created. |
| `README.md` | Created. |
| `PROJECT_PROGRESS.md` | Created (this file). |

Git repository: **not yet initialized as of the start of this file** —
update this line once `git init` + first commit is done (see §9 step 2).

## 7. Known gaps / things to be aware of (not bugs, just context)

- `buildozer.spec` references `assets/icons/icon.png` and
  `assets/images/presplash.png` for the app icon and splash screen —
  **neither file exists yet**. Buildozer will warn/use defaults until
  real icon/presplash images are added. Not urgent until an actual APK
  build is attempted.
- `home_screen.py` loads its `.kv` file via
  `Builder.load_file(__file__.replace(".py", ".kv"))` — a simple,
  explicit pattern that works because the `.py` and `.kv` files sit
  side by side with matching names. If more screens are added, keep
  following this same one-folder-per-screen, matching-filename pattern
  for consistency.
- No actual CV-builder features exist yet: no data model for CV content
  (name/experience/education/skills), no form screens, no PDF export,
  no local storage/persistence. All of that is future work, to be built
  incrementally per the user's "step by step" instruction — resist the
  urge to scaffold all of it at once.
- GitHub: only local git is being set up in this session. No GitHub
  remote repository has been created or connected yet — that needs the
  user to create the repo on github.com (or provide `gh` CLI access) and
  decide on visibility (public/private) before a remote push happens.

## 8. Current project status

- Full folder/file skeleton exists and is believed structurally correct
  for a standard Kivy/KivyMD project, but **`main.py` has not yet been
  successfully run/verified** — blocked on environment setup (§4).
- Git/Python 3.12 install via winget was chosen and kicked off this
  session — confirm completion and actual versions before trusting this
  section; update once verified.
- No GitHub remote connected yet.
- No CV-builder features implemented — this is scaffolding only.

## 9. Exact next task to continue

1. **Verify the winget installs actually completed successfully:**
   `git --version` and `py -3.12 --version` (or `python --version` after
   reopening the terminal so PATH picks up the new installs — a fresh
   terminal/VS Code window is usually required after installing Git or
   Python via winget). If either is still missing, finish installing it
   manually before continuing.
2. **Initialize git and make the first commit:**
   ```
   cd "C:\Users\Acer User\Downloads\CV-Genius-AI"
   git init
   git add .
   git commit -m "Initial project skeleton: Kivy/KivyMD app structure"
   ```
3. **Create a Python 3.12 virtual environment and install dependencies**
   (do NOT use the system Python 3.14 — see §4 for why):
   ```
   py -3.12 -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. **Run the app for the first time and visually confirm it launches:**
   ```
   python main.py
   ```
   Expect a window showing "CV Genius AI" and the subtitle text. If it
   fails, capture the exact traceback before attempting any fix.
5. **Connect to GitHub:** create a new empty repository on github.com
   named `CV-Genius-AI` (ask the user whether it should be public or
   private, and under which GitHub account), then:
   ```
   git remote add origin <the repo URL>
   git branch -M main
   git push -u origin main
   ```
6. **Set up VS Code for this project:** open the `CV-Genius-AI` folder
   in VS Code, select the `.venv` Python 3.12 interpreter (Ctrl+Shift+P
   → "Python: Select Interpreter"), and confirm the Kivy language
   support/linting is comfortable to work with (install the "kivy-lang"
   VS Code extension if `.kv` syntax highlighting is wanted).
7. **Only after 1–6 are done and verified**, start actual feature work:
   the natural first real feature is a `models/cv_profile.py` data model
   (name, contact info, a list of experience entries, education,
   skills) plus a first real form screen to capture it — but confirm
   this with the user before starting, since they may want a different
   first slice (e.g. template selection UI first, or PDF export first).
