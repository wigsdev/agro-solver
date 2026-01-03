# Agro-Solver 🌾

![Status](https://img.shields.io/badge/Status-In%20Development-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Tech](https://img.shields.io/badge/Stack-FastAPI%20%7C%20VanillaJS-green?style=for-the-badge)

> **Soluciones Agrícolas Inteligentes impulsadas por Ingeniería de Software.**

Agro-Solver es una plataforma integral diseñada para optimizar la toma de decisiones en el sector agrícola mediante análisis de datos, gestión de cultivos y automatización de procesos.

## 📋 Tabla de Contenidos
- [Descripción del Problema](#-descripción-del-problema)
- [Stack Tecnológico](#-stack-tecnológico)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Roadmap](#-roadmap)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

## 🧐 Descripción del Problema
La agricultura moderna enfrenta desafíos complejos: variabilidad climática, gestión ineficiente de recursos y falta de digitalización en procesos clave. Agro-Solver busca resolver estos problemas centralizando la información y proveyendo herramientas analíticas accesibles y potentes.

## 🛠 Stack Tecnológico

**Backend**
- Python 3.11+
- FastAPI (High performance API)
- Pydantic (Data Validation)

**Frontend**
- HTML5 / CSS3 Moderno
- JavaScript (ES6+ Vanilla)

**DevOps & Tools**
- Git & GitHub Actions
- Docker (Planned)

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
    pip install -r backend/requirements.txt
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
   
   > **Nota**: Asegúrate de que el backend esté corriendo en el puerto 8000. Si cambias el puerto, actualiza `frontend/config.js`.

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
