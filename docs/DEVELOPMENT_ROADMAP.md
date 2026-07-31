# CV-Genius-AI Development Roadmap

## 1. Project analysis summary

CV-Genius-AI is currently a verified Kivy/KivyMD application skeleton, not a feature-complete CV builder. The codebase already proves that:

- the app launches successfully from `main.py`
- the `HomeScreen` loads correctly from a `.kv` file
- the package layout follows the standard Kivy screen-per-folder structure

The app is therefore in a good starting state for incremental feature development. The right next step is to build one coherent slice at a time, with the first slice centered on a real CV data model and editable form screens.

---

## 2. Existing project structure and what each folder/file is for

### Root-level files

- `main.py`
  - Application entry point.
  - Creates the `CVGeniusApp` subclass of `MDApp`.
  - Sets the theme style and registers the initial `HomeScreen`.

- `requirements.txt`
  - Declares Python dependencies for the desktop development environment.
  - Currently pins Kivy and KivyMD.

- `buildozer.spec`
  - Buildozer packaging configuration for Android APK generation.
  - Contains app identity, Android SDK/API settings, and package requirements.

- `README.md`
  - High-level project description, environment setup, and usage notes.

- `PROJECT_PROGRESS.md`
  - The source-of-truth progress log and environment notes.
  - Documents what has been completed and what remains.

- `.gitignore`
  - Ignores virtual environments, build artifacts, cache files, and OS/editor noise.

### Application package

- `cvgenius/`
  - Main Python package for the app logic.

- `cvgenius/__init__.py`
  - Package marker file.

### Screens

- `cvgenius/screens/`
  - Dedicated folder for all app screens.
  - Each screen should live in its own folder with a matching `.py` and `.kv` file.

- `cvgenius/screens/home/`
  - Placeholder home screen for the first working app shell.

- `cvgenius/screens/home/home_screen.py`
  - Defines the `HomeScreen` class.
  - Loads the matching `home_screen.kv` layout file.

- `cvgenius/screens/home/home_screen.kv`
  - KV layout for the placeholder landing screen.

- `cvgenius/screens/__init__.py`
  - Package marker for the screens module.

### Reusable UI components

- `cvgenius/widgets/`
  - Future home for reusable Kivy/KivyMD custom widgets.

- `cvgenius/widgets/__init__.py`
  - Package marker file.

### Data models

- `cvgenius/models/`
  - Future home for CV data structures such as personal info, work experience, education, skills, and templates.

- `cvgenius/models/__init__.py`
  - Package marker file.

### Utilities

- `cvgenius/utils/`
  - Future home for cross-cutting helpers such as file persistence, PDF export, validation, and formatting utilities.

- `cvgenius/utils/__init__.py`
  - Package marker file.

### Data templates

- `cvgenius/data/templates/`
  - Reserved for CV template definitions and layout assets.

### Assets

- `assets/`
  - Static app resources.

- `assets/images/`
  - App images, splash artwork, and preview visuals.

- `assets/fonts/`
  - Custom fonts if needed.

- `assets/icons/`
  - App icons and launch/icon-related assets.

### Tests and docs

- `tests/`
  - Automated test suite location.

- `tests/__init__.py`
  - Test package marker.

- `docs/`
  - Project documentation and product planning files.

---

## 3. Current state of the codebase

### What is already working

1. The Python environment has been set up and verified.
2. The Kivy/KivyMD app can be launched via `main.py`.
3. The screen loading pattern is proven and stable.
4. The repository has a valid initial package structure for future feature expansion.

### What is not implemented yet

- Real CV profile creation flow
- Experience/education form screens
- Resume template selection
- PDF export
- Local storage or data persistence
- AI-powered content generation
- APK packaging verification

---

## 4. Recommended development roadmap

### Phase 0 — Stabilize the project foundation

Goal: ensure the app is clean, consistent, and ready for feature work.

Planned tasks:

- select the correct Python interpreter in VS Code
- keep using the `.venv` for all local development
- confirm the app opens cleanly on Windows desktop before every feature increment
- establish a simple testing baseline for the screen layer

Deliverable:

- a stable dev setup and a reproducible launch path

### Phase 1 — Build the core data model

Goal: define the actual information the app will manage.

Suggested first module:

- `cvgenius/models/cv_profile.py`

Suggested model content:

- personal details
- contact information
- summary/objective
- work experience list
- education list
- skills list
- optional achievements or projects

Deliverable:

- a typed, testable CV profile model that can be edited across screens and persisted later

### Phase 2 — Create the first real user flow

Goal: let a user enter a CV profile through an actual form screen.

Recommended first screen sequence:

1. `HomeScreen` becomes the dashboard
2. `ProfileEditorScreen` for name/contact details
3. `ExperienceEditorScreen` for work history
4. `EducationEditorScreen` for academic history
5. `SkillsEditorScreen` for technical or soft skills

Deliverable:

- a fully usable first-time data-entry workflow

### Phase 3 — Add form navigation and state management

Goal: connect screens together with consistent transitions.

Planned improvements:

- a `ScreenManager`-driven navigation flow
- navigation buttons and back/next logic
- simple screen-to-screen state passing
- data validation on required fields

Deliverable:

- a coherent, navigable application flow rather than isolated forms

### Phase 4 — Template selection and resume preview

Goal: make the app feel like a CV builder rather than a data form.

Planned tasks:

- define template metadata
- create a preview screen or card layout
- support at least one basic template style
- allow switching between templates

Deliverable:

- a previewable resume layout based on the collected profile data

### Phase 5 — Persistence and import/export

Goal: give the user a safe way to keep work.

Planned tasks:

- save CV data locally in JSON
- reload saved profiles
- add import/export support for backup or data transfer
- optionally prepare for PDF generation later

Deliverable:

- persistent CV editing sessions with restore capability

### Phase 6 — Export and professional output

Goal: turn the app into a real resume generator.

Suggested output choices:

- PDF export
- print-ready formatting
- template-specific layout rendering

Deliverable:

- an exportable resume document from the completed profile

### Phase 7 — AI-assisted enhancements

Goal: move from static form-building into intelligent resume assistance.

Possible AI features:

- auto-generate summary statements
- rewrite bullet points
- recommend skill wording
- tailor CV content toward a job description

Deliverable:

- an assistant layer that improves content quality without disturbing the core editing model

### Phase 8 — Android packaging and release preparation

Goal: prepare the app for APK distribution.

Planned tasks:

- add icon and splash assets
- verify Buildozer configuration
- test packaging under Linux/WSL
- finalize app metadata and permissions

Deliverable:

- a releasable Android build workflow

---

## 5. Recommended implementation order

The safest order is:

1. `cv_profile.py` model
2. home/dashboard redesign
3. profile editor screen
4. experience/education/skills screens
5. preview/template screen
6. local persistence
7. export
8. AI enhancement layer
9. Android packaging

This order keeps the project focused on one real user outcome: entering CV data and generating a usable output.

---

## 6. Suggested directory growth plan

As the app expands, keep the following structure consistent:

- `cvgenius/screens/` for app pages
- `cvgenius/widgets/` for reusable UI pieces
- `cvgenius/models/` for plain Python data objects
- `cvgenius/utils/` for persistence/export/helpers
- `cvgenius/data/templates/` for template definitions and theme assets

Avoid over-scaffolding. Add modules only when the next feature needs them.

---

## 7. Recommended first implementation slice

The best first slice is:

- `cvgenius/models/cv_profile.py`
- one profile form screen
- one screen manager flow
- a save/load mechanism for a single profile

This gives the app a real product identity without creating too much architectural burden too early.

---

## 8. Approval checkpoint

No feature code should be written until the roadmap above is approved.

Once approved, the next step will be to implement the first slice in a small, testable sequence using the existing app shell.
