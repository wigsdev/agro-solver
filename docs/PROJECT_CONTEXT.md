# 🚀 Project Name: AGRO-SOLVER (MVP)

## 1. Executive Summary & Vision
**Agro-Solver** is a specialized Micro-SaaS web application designed for agronomists and technical farmers.
**The core problem:** Field calculations (like seed density or fertilizer mixing) are currently done manually or in complex Excel sheets that are hard to use on mobile devices in the field.
**The Solution:** A mobile-first, fast, and precise web tool to perform these calculations instantly.
**Ultimate Goal:** Deploy a functional, monetizable product to production (Live URL) that serves as a lead generation tool for agricultural inputs.

## 2. Strategic Objectives

### A. Business Objectives (Priority #1)
1.  **Speed to Market:** The site must be deployed and accessible via a public URL (Render/Railway) immediately upon completion of v1.0.0.
2.  **User Experience (UX):** The interface must be "Field-Ready". This means large buttons, high contrast for sunlight visibility, and zero fluff.
3.  **Monetization Foundation:** The architecture must allow for future insertion of affiliate links or "Premium Features" (like PDF export) without rewriting the core.

### B. Technical Objectives (Priority #2)
1.  **Stack Compliance:** Strict adherence to the learning path:
    * **Backend:** Python (FastAPI) - for mathematical robustness.
    * **Frontend:** Vanilla JavaScript (ES6+), HTML5, CSS3 - to master the basics before frameworks.
2.  **Code Quality:** Code must be modular, commented for educational purposes, and follow PEP8 (Python) standards.
3.  **Scalability:** Separate Backend (API) from Frontend (Client) to allow future migration to React or mobile apps.

## 3. Scope of Work (MVP - v1.0.0)

**Included Features:**
* **Seed Density Calculator Module:**
    * **Input:** Row Distance (m), Plant Distance (m).
    * **Validation:** Must reject negative numbers or zero.
    * **Output:** Plants per Hectare (visual card).
* **Connectivity:** Robust error handling for poor network conditions (common in agriculture).
* **Architecture:** RESTful API endpoints.

**Excluded (For Future Versions):**
* User Authentication (Login/Signup).
* Database Persistence (History).
* Payment Gateways.

## 4. Technical Constraints & Rules
1.  **Mobile First:** All CSS must be written for mobile screens first, then adapted for desktop.
2.  **No "Magic":** Do not use heavy libraries for simple tasks. Use native Python/JS functions where possible.
3.  **Documentation:** All major functions must have docstrings explaining the logic.
4.  **Language:**
    * **Code/Variables:** English (e.g., `calculate_density`).
    * **User Interface:** Spanish (Target market is Latin America).

## 5. Deployment Strategy
* **Version Control:** GitHub (Main branch is always production-ready).
* **Infrastructure:** PaaS (Render or Railway).
* **CI/CD:** Manual push to main triggers deployment.

---
**Note to Agent:** efficient execution and error-free code are prioritized over complex abstractions. The goal is a working product NOW.