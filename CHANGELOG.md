# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.9.0] - To Be Released

### Changed
- **Hardening**: Prepared codebase for production deployment.
    - **Backend**: Cleaned up `main.py` (removed unused imports/prints).
    - **Dependencies**: Standardized `requirements.txt` with essential packages only.
    - **Frontend**: Implemented robust error handling in `app.js` to distinguish between Network Errors (offline) and API Errors.
    - **Cleanup**: Removed debug `console.log` statements from client-side code.

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
