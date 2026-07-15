# 🎓 Examen Final - Aplicación Web Full-Stack UISEK

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-REST-darkgreen?style=for-the-badge&logo=django)
![React](https://img.shields.io/badge/React-18-61dafb?style=for-the-badge&logo=react)
![License](https://img.shields.io/badge/License-Academic-orange?style=for-the-badge)

**Una aplicación web Full-Stack moderna con autenticación OAuth 2.0 y gestión de catálogos**

</div>

---

## 📖 Descripción

Este proyecto corresponde al **examen final de Desarrollo Web** de la Universidad Internacional SEK (UISEK). 

Consiste en una aplicación web Full-Stack que integra un backend robusto con una interfaz moderna y responsiva. La aplicación implementa una **arquitectura cliente-servidor** donde:

- 🔧 **Django** funciona exclusivamente como **API REST**
- ⚛️ **React** consume los servicios expuestos para ofrecer una **interfaz moderna e interactiva**
- 🔐 **OAuth 2.0** proporciona autenticación segura
- 📊 **SQLite** almacena los datos de forma segura

---

## 🎯 Objetivo

Desarrollar una aplicación web Full-Stack que demuestre el dominio de:

| 📚 Concepto | ✅ Implementado |
|---|---|
| Desarrollo de APIs REST | ✓ GET, POST, PUT, PATCH, DELETE |
| React & Componentes | ✓ Interfaz reactiva y modular |
| OAuth 2.0 | ✓ Autenticación segura |
| Consumo de APIs | ✓ Integración cliente-servidor |
| Arquitectura Cliente-Servidor | ✓ Separación de responsabilidades |
| Control de versiones | ✓ Git & GitHub |

---

## 🛠️ Tecnologías utilizadas

### 🔙 Backend

```
┌─────────────────────────────────────┐
│      Django REST Framework          │
├─────────────────────────────────────┤
│  • Django ORM                       │
│  • OAuth 2.0 Integration            │
│  • Serializers & Validators         │
│  • Authentication & Permissions     │
└─────────────────────────────────────┘
         ↓
    SQLite Database
```

### 🎨 Frontend

```
┌─────────────────────────────────────┐
│        React + Vite                 │
├─────────────────────────────────────┤
│  • Material UI Components           │
│  • Axios para HTTP Requests         │
│  • State Management                 │
│  • Responsive Design                │
└─────────────────────────────────────┘
```

### 🔧 Herramientas

- **Control de versiones**: Git & GitHub
- **Testing de APIs**: Postman
- **Editor**: VS Code (recomendado)

---

## 📚 Características principales

### 🔐 Autenticación

- ✅ Inicio de sesión mediante **OAuth 2.0**
- ✅ Protección de endpoints
- ✅ Manejo seguro de tokens de acceso
- ✅ Cierre de sesión

### 📊 Gestión de datos (CRUD)

- ✅ **Crear** registros
- ✅ **Leer** información
- ✅ **Actualizar** registros
- ✅ **Eliminar** registros

### 🌐 API REST

```
GET    /api/items/          → Listar todos los registros
POST   /api/items/          → Crear nuevo registro
GET    /api/items/{id}/     → Obtener un registro específico
PUT    /api/items/{id}/     → Actualizar completo
PATCH  /api/items/{id}/     → Actualización parcial
DELETE /api/items/{id}/     → Eliminar registro
```

---

## 📂 Estructura del proyecto

```
examen-final-UISEK/
│
├── 📁 backend/                    # Django REST API
│   ├── 📁 apps/
│   │   └── 📁 catalog/
│   │       ├── models.py          # Definición de modelos
│   │       ├── serializers.py     # Serializadores
│   │       ├── views.py           # Vistas API
│   │       └── urls.py            # Rutas
│   ├── 📁 api/
│   │   └── settings.py            # Configuración Django
│   ├── manage.py
│   └── requirements.txt
│
├── 📁 frontend/                   # React App
│   ├── 📁 src/
│   │   ├── 📁 components/         # Componentes React
│   │   ├── 📁 pages/              # Páginas
│   │   ├── 📁 services/           # Servicios API
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── 📁 public/
│   ├── package.json
│   └── vite.config.js
│
└── README.md                       # Este archivo
```

---

## 🚀 Instalación rápida

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/sebastianrubio-cpu/examen-final.-aplicacion-web-full-stack-UISEK.git
cd examen-final.-aplicacion-web-full-stack-UISEK
```

### 2️⃣ Configurar el Backend

```bash
# Navegar a la carpeta backend
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor Django
python manage.py runserver
```

El backend estará disponible en `http://localhost:8000`

### 3️⃣ Configurar el Frontend

```bash
# En otra terminal, navegar a frontend
cd frontend

# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev
```

El frontend estará disponible en `http://localhost:5173`

---

## 📬 Endpoints de la API

### Autenticación

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/auth/login/` | Iniciar sesión |
| `POST` | `/api/auth/logout/` | Cerrar sesión |
| `POST` | `/api/auth/token/refresh/` | Refrescar token |

### Catálogo

| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/items/` | Listar todos | ✓ |
| `POST` | `/api/items/` | Crear nuevo | ✓ |
| `GET` | `/api/items/{id}/` | Obtener uno | ✓ |
| `PUT` | `/api/items/{id}/` | Actualizar | ✓ |
| `PATCH` | `/api/items/{id}/` | Actualizar parcial | ✓ |
| `DELETE` | `/api/items/{id}/` | Eliminar | ✓ |

---

## 🔐 Seguridad

La aplicación implementa múltiples capas de seguridad:

```
🔒 OAuth 2.0 Authentication
    ↓
🔑 JWT Tokens (Access & Refresh)
    ↓
🛡️ CORS Configuration
    ↓
✅ HTTPS (en producción)
    ↓
🔐 Encrypted Passwords (bcrypt)
```

**⚠️ Nota**: Los endpoints protegidos requieren un Access Token válido en el header:

```
Authorization: Bearer {access_token}
```

---

## 🧪 Pruebas con Postman

Se incluye una colección de Postman con:

- ✅ Flujo completo de autenticación
- ✅ CRUD completo
- ✅ Variables de entorno preconfiguradas
- ✅ Ejemplos de request y response
- ✅ Endpoints protegidos

**Ubicación**: `/postman/coleccion.json`

---

## 📋 Requisitos del sistema

| Requisito | Versión mínima |
|-----------|-----------------|
| Node.js | 16.x |
| npm | 7.x |
| Python | 3.8+ |
| Django | 4.0+ |
| Git | 2.x |

---

## 📊 Composición del código

```
Python   ███████░░░░░░░░ 53.5%
CSS      ████░░░░░░░░░░░ 24.9%
JavaScript ███░░░░░░░░░░░ 19.8%
HTML     ░░░░░░░░░░░░░░░  1.8%
```

---

## 📖 Comandos útiles

### Backend

```bash
# Crear superuser
python manage.py createsuperuser

# Acceder a shell interactivo
python manage.py shell

# Ver migraciones
python manage.py showmigrations

# Crear nueva app
python manage.py startapp nombre_app
```

### Frontend

```bash
# Compilar para producción
npm run build

# Preview de build
npm run preview

# Linting
npm run lint
```

---

## 🎓 Conceptos aplicados

- ✅ Arquitectura REST
- ✅ Principios SOLID
- ✅ MVC Pattern (Backend)
- ✅ Component-Based Design (Frontend)
- ✅ DRY (Don't Repeat Yourself)
- ✅ Separación de responsabilidades
- ✅ Versionado semántico
- ✅ Documentación clara

---

## 📧 Contacto & Contribuciones

Este es un proyecto académico de la **Universidad Internacional SEK (UISEK)**.

**Estudiantes**:
- Nombre del estudiante 1
- Nombre del estudiante 2

---

## 📄 Licencia

```
© 2024 Proyecto desarrollado con fines académicos
Universidad Internacional SEK (UISEK)
Asignatura: Desarrollo Web
```

<div align="center">

**Hecho con ❤️ para UISEK**

[⬆ Volver arriba](#examen-final---aplicación-web-full-stack-uisek)

</div>
