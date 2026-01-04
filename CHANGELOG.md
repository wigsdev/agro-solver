# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-01-04

> **Feature Release:** Added instant Unit Converter tool logic on client-side.

### Added
- **Module**: Unit Converter Tool (`/tools/converter`).
    - Surfaces: Ha, Acres, Manzanas, m², Tareas.
    - Weights: Ton, Quintal (qq), Kg, Lb.
    - **Client-Side Engine**: Zero-latency conversion using `converter.js`.
    - **UI**: Tabbed interface for category switching.

## [2.0.0] - 2026-01-04

> **Major Refactor: Agro-Tech Portal.** Transformed into a multi-page content platform.

### Changed
- **Branding**: Rebranded from 'Agro-Solver' to **'Agro-Tech'**. New visual identity (Deep Green/Slate).
- **Architecture**: Migrated from Static Frontend to **Jinja2 Server-Side Rendering**.
    - Moved HTML to `/templates` and Assets to `/static`.
    - Implemented `base.html` for layout inheritance.
- **Features**:
    - Added **Home Page** (Landing).
    - Added **Tools Hub** (Catalog).
    - Added **Blog** Section.

## [1.0.0] - 2026-01-03

> **First Stable Release.** Core Seed Density Calculator is fully operational.

### Added
- **Backlog**: Created `TODO.md` with future roadmap (Login, SQLite, Docker).

### Changed
- **Refactoring**: Final code polish and removal of development artifacts.

## [0.9.0] - 2026-01-03

## [0.3.0] - 2026-01-03

### Changed
- **UI/UX**: Complete overhaul of the frontend interface.
    - Implemented **Mobile-First** design using `style.css`.
    - Defined agricultural color palette (Green #2E7D32, Earth #795548).
    - Added styled cards for calculator and results.
    - Improved visual feedback for success/error states.
- **Localization**: Translated all system documentation and code comments to **Spanish**.
    - `backend/main.py` docstrings.
    - `backend/schemas.py` descriptions.
    - `frontend/app.js` logic comments.

## [0.2.0] - 2026-01-03

### Added
- **Agronomy**: Implemented Density Calculator Module.
    - Support for **Square/Rectangular** planting systems.
    - Support for **Triangular (Tresbolillo)** planting systems (+15% efficiency).
- **Backend**:
    - `POST /api/density` endpoint with logic for both systems.
    - Pydantic schemas in `backend/schemas.py` using Enums.
- **Frontend**:
    - Calculator Card Component in `index.html`.
    - Dynamic calculation logic in `app.js`.
- **Docs**:
    - Created `docs/` directory.
    - Added `docs/AGRONOMY.md` explaining mathematical formulas.
    - Moved `DEVELOPMENT.md` to `docs/`.

## [0.1.0] - 2026-01-03

### Added
- **Backend**:
    - Initialized FastAPI application (`main.py`).
    - Added `GET /` root endpoint returning API status.
    - Configured CORS middleware (currently allowing `*` for development).
    - Added `requirements.txt` with strict dependency pinning.
    - Added unit tests with `pytest` (`tests/test_main.py`).
- **Frontend**:
    - Created basic HTML5 structure (`index.html`).
    - Implemented logic (`app.js`) to fetch API status.
    - Added configuration file (`config.js`) for environment variables.
- **Documentation**:
    - Initialized `CHANGELOG.md`.
    - Updated `README.md` with execution instructions.
