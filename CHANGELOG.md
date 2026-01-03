# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
