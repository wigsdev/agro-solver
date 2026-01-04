# Agro-Tech 🌾

![Status](https://img.shields.io/badge/Status-Stable%20v2.0.0-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Tech](https://img.shields.io/badge/Stack-FastAPI%20%7C%20Jinja2-orange?style=for-the-badge)

> **Inteligencia Digital para el Campo.**

**Agro-Tech** (anteriormente Agro-Solver) es un portal integral de servicios agronómicos diseñado para optimizar la toma de decisiones mediante tecnología accesible.

## 📋 Tabla de Contenidos
- [Descripción del Problema](#-descripción-del-problema)
- [Arquitectura (v2.0.0)](#-arquitectura-v200-mvc)
- [Stack Tecnológico](#-stack-tecnológico)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Contribuir](#-contribuir)

## 🧐 Descripción del Problema
La agricultura moderna requiere más que cálculos aislados; necesita un ecosistema de información. Agro-Tech centraliza herramientas de cálculo, contenido educativo y análisis de datos en una sola plataforma web unificada.

## 🏗 Arquitectura (v2.0.0: MVC)
El proyecto ha evolucionado de una API REST simple a una arquitectura **Server-Side Rendering (SSR)** para mejorar el SEO y la extensibilidad.
- **Modelos**: Pydantic (`backend/schemas.py`).
- **Vistas (Templates)**: Jinja2 HTML (`templates/`).
- **Controlador**: FastAPI Routing (`backend/main.py`).

## 🛠 Stack Tecnológico

**Backend & Rendering**
- Python 3.11+
- FastAPI (High performance API)
- **Jinja2** (Template Engine)
- Pydantic (Data Validation)

**Frontend (Assets)**
- HTML5 Semántico
- CSS3 (Variables & Mobile First)
- Vanilla JS (ES6+)

**DevOps**
- Render (PaaS Deployment)
- Infrastructure as Code (`render.yaml`)

## 🛠️ Instalación

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/Agro-Solver.git
    cd Agro-Solver
    ```

2.  **Configurar entorno virtual (Backend):**
    ```bash
    python -m venv backend/venv
    # Windows
    .\backend\venv\Scripts\activate
    # Linux/Mac
    source backend/venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Uso

   .\venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   
   # Instalar dependencias
   pip install -r backend/requirements.txt
   
   # Ejecutar Servidor (Dev)
   uvicorn backend.main:app --reload
   
   # Ejecutar Tests
   pytest backend/tests
   ```

3. **Frontend Setup**
   Simplemente abre el archivo `frontend/index.html` en tu navegador.
   
## 🚀 Uso

1.  **Iniciar el Servidor:**
    ```bash
    uvicorn backend.main:app --reload
    ```
2.  **Navegar al Portal:**
    - Abre `http://127.0.0.1:8000` en tu navegador.
    - **Inicio**: Landing page con proposición de valor.
    - **Herramientas**: Catálogo de calculadoras (/tools).
    - **Blog**: Artículos técnicos (/blog).

---
**Status:** Stable v2.0.0 (Agro-Tech)

## 🗺 Roadmap

- [ ] **Fase 1**: Arquitectura Base y Definición de API.
- [ ] **Fase 2**: Módulo de Gestión de Cultivos (CRUD básico).
- [ ] **Fase 3**: Integración de Datos Climáticos.
- [ ] **Fase 4**: Dashboard Analítico y Reportes.

## 🤝 Contribuir
Consulta [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) para conocer las normas de contribución y estándares de código de este proyecto.

## 📚 Documentación Técnica
- [Fórmulas Agronómicas](docs/AGRONOMY.md): Detalles matemáticos de los cálculos.

## 📄 Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
