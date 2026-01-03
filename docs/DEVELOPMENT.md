# Guía de Desarrollo - Agro-Solver

Este documento define los estándares técnicos, estructura del proyecto y reglas de contribución para **Agro-Solver**.

## 1. Principios de Ingeniería
- **Clean Code**: Priorizamos la legibilidad sobre la optimización prematura.
- **DRY (Don't Repeat Yourself)**: Abstrae lógica repetitiva.
- **KISS (Keep It Simple, Stupid)**: Soluciones simples y elegantes.

## 2. Stack Tecnológico

### Backend
- **Lenguaje**: Python 3.10+
- **Framework**: FastAPI
- **Gestión de Paquetes**: Pip / Requirements.txt
- **Linter/Formatter**: Black, Flake8, Isort

### Frontend
- **Lenguaje**: JavaScript (Vanilla / ES6+)
- **Estilos**: CSS3 (Modular / Variables CSS)
- **Bundler**: Vite (Opcional si crece la complejidad)

## 3. Estructura del Proyecto
```
Agro-Solver/
├── backend/            # API REST (FastAPI)
│   ├── app/            # Código fuente de la aplicación
│   ├── tests/          # Tests unitarios e integración
│   └── requirements.txt
├── frontend/           # Cliente Web
│   ├── src/            # Código fuente JS/CSS
│   └── index.html      # Punto de entrada
├── docs/               # Documentación adicional
├── .gitignore
├── LICENSE
├── README.md
└── DEVELOPMENT.md
```

## 4. Flujo de Git y Versionamiento

### Conventional Commits
Es **OBLIGATORIO** usar Conventional Commits:
- `feat`: Nuevas características.
- `fix`: Corrección de bugs.
- `docs`: Cambios en documentación.
- `style`: Formato (espacios, comas, etc).
- `refactor`: Refactorización de código sin cambiar lógica.
- `test`: Añadir o corregir tests.
- `chore`: Tareas de mantenimiento, build, herramientas.

**Ejemplo:** `feat(auth): add jwt login endpoint`

### Ramas
- `main`: Producción (estable).
- `develop`: Desarrollo (integración).
- `feature/nombre-feature`: Nuevas funcionalidades.
- `fix/nombre-bug`: Corrección de errores.

## 5. setup Inicial
1. Clonar repositorio.
2. Backend: `pip install -r backend/requirements.txt`
3. Frontend: Servir `index.html` localmente.

---
**Lead Software Architect** - Agro-Solver Team
