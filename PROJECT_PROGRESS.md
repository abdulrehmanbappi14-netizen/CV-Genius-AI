# CV Genius AI — Project Progress

_Last updated: 2026-08-01_

This file is the single source of truth for where this project stands.
If you're picking this back up after days away, read this top to bottom
before touching code.

## Current checkpoint (2026-08-01)

The verified checkpoint now includes Phase 4: template selection and
live resume preview. The profile editor can now surface the built-in
resume templates from the registry and let the user pick a template
for the current `CVProfile`. The preview screen remains synchronized
with the current profile data so the selected template label and the
rendered preview text update from one shared source of truth.

Implementation details:
- `ProfileEditorScreen` now exposes `get_template_choices()` and
  `apply_template_choice()` to read from the registry and update the
  current profile's `template_name` field.
- The editor UI now offers template action buttons for the built-in
  `classic` and `modern` templates.
- A helper method `update_preview_from_profile()` keeps the preview
  route consistent and avoids duplicating the screen handoff logic.
- The preview flow remains tied to the same `CVProfile` object so the
  active selection and live preview are always in sync.

Verification evidence:
- `python -m unittest tests.test_template_selection -v` → 1 test run, OK
- `python -m unittest discover -v` → 20 tests run, OK

This feature completes the Phase 4 roadmap milestone without changing
its architectural direction: the model stays central, the preview stays
in sync, and the UI remains incremental rather than over-built.

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

- **`main.py` is verified working** (2026-07-31): launched via
  `.venv\Scripts\python.exe main.py`, log ended with
  `[INFO] [Base] Start application main loop` and no errors/tracebacks
  — the KivyMD window opens, GL/SDL2 initialize correctly (Intel UHD
  Graphics 620, OpenGL 4.6), and `HomeScreen`'s `.kv` layout loads
  without issue. Process was stopped intentionally afterward (it's a
  GUI event loop that runs until closed).

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
- **Fix applied and confirmed working:** installed both via `winget`
  (user chose this option explicitly):
  - `winget install --id Git.Git -e --accept-package-agreements --accept-source-agreements --silent`
    → **Git 2.55.0.3** installed and confirmed working (`git --version`).
  - `winget install --id Python.Python.3.12 -e --accept-package-agreements --accept-source-agreements --silent`
    → **Python 3.12.10** installed and confirmed working (`py -3.12 --version`).
  - **Gotcha hit during setup:** right after a winget install, `git`/`py
    -3.12` were still "not recognized" in already-open terminal
    sessions — PATH is only re-read by newly-started processes, not
    picked up by a shell that was already running. Opening a fresh
    terminal (or, in a pinch, manually reloading
    `$env:Path` from
    `[System.Environment]::GetEnvironmentVariable("Path","Machine")` +
    `...("Path","User")` in PowerShell) fixes it. If `git`/`python`
    seem missing right after installing them, this is almost certainly
    why — try a fresh terminal before assuming the install failed.
- **Why Python 3.12 specifically:** it's a recent, stable release with
  mature Kivy wheel support. The system's Python 3.14 remains installed
  and unchanged (still the default for `python`/`py` outside this
  project) — this project's `.venv` was built explicitly with
  `py -3.12 -m venv .venv` and must keep being used via that venv, not
  system Python.

## 5. Bug fixes completed

None needed — `main.py` ran successfully on the first attempt once the
environment (§4) was fixed. No code defects found yet, since no real
feature code exists yet either.

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

Git repository: **initialized**, first commit made —
`f7893e4 Initial project skeleton: Kivy/KivyMD app structure` (19 files,
on branch `master`). Local git identity was set to
`Abdul Rehman <abdulrehmanbappi13@gmail.com>` (a reasonable guess from
the account email — change with `git config user.name`/`user.email` if
a different name is preferred).

Also created (not tracked by git — see `.gitignore`):
- `.venv\` — Python 3.12 virtual environment with Kivy 2.3.1 + KivyMD
  1.2.0 installed (see §4).

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
- GitHub: only local git exists so far. No GitHub remote repository has
  been created or connected yet — that needs the user to create the repo
  on github.com (or provide `gh` CLI access) and decide on visibility
  (public/private) before a remote push happens.
- KivyMD 1.2.0 (pinned in `requirements.txt`/`buildozer.spec`) logs a
  deprecation warning on startup: "Version 1.2.0 is deprecated... Use
  KivyMD version 2.0.0 from the master branch". 1.2.0 was still used
  deliberately since it's the latest stable PyPI release (2.0.0 is only
  available as an unreleased install-from-git master branch) — revisit
  this tradeoff later if KivyMD 2.0 has a stable PyPI release by the
  time real feature work starts.

## 8. Current project status

- Full folder/file skeleton exists, matches standard Kivy/KivyMD project
  conventions, and **is verified working**: `main.py` launches a KivyMD
  window showing the placeholder `HomeScreen` with no errors (§3, §5).
- Git repo initialized locally with one commit (§6). **No GitHub remote
  connected yet.**
- Dev environment is fully set up: Git 2.55.0, Python 3.12.10, and a
  `.venv` with Kivy 2.3.1 + KivyMD 1.2.0 installed and confirmed working
  (§4, §6).
- No CV-builder features implemented — this is scaffolding only, by
  design, per the "step by step" approach.
- VS Code has **not** been opened/configured for this project yet in
  this session (no way to verify that from a terminal-only session) —
  first item in §9.

## 9. Exact next task to continue

1. **Open the project in VS Code and select the right interpreter:**
   open the `CV-Genius-AI` folder in VS Code, then Ctrl+Shift+P →
   "Python: Select Interpreter" → pick
   `.venv\Scripts\python.exe` (Python 3.12.10) so IntelliSense/linting
   and the integrated terminal both use the correct environment. Install
   the "kivy-lang" extension if `.kv` syntax highlighting is wanted.
2. **Connect to GitHub:** create a new empty repository on github.com
   named `CV-Genius-AI` (confirm with the user: public or private, and
   under which GitHub account), then from the project folder:
   ```
   git remote add origin <the repo URL>
   git branch -M main
   git push -u origin main
   ```
3. **Only after 1–2 are done**, start actual feature work. The natural
   first real feature is a `cvgenius/models/cv_profile.py` data model
   (name, contact info, a list of experience entries, education,
   skills) plus a first real form screen to capture it — but confirm
   this with the user before starting, since they may want a different
   first slice (e.g. template selection UI first, or PDF export first).
4. **Remember the venv activation step** every new terminal session
   before running anything: `.venv\Scripts\activate` (or just call
   `.venv\Scripts\python.exe`/`.venv\Scripts\pip.exe` directly, which is
   what was used during this session's verification and doesn't depend
   on activation state).
