# Sistema de Gestión de Catálogo Web Full-Stack - Examen Final UISEK

## 1. Introducción del Proyecto
Este proyecto consiste en el diseño, desarrollo e implementación de una aplicación web full-stack desacoplada destinada a la gestión y visualización de un catálogo de películas, directores y vendedores. El sistema integra un Backend robusto basado en el framework Django (Django REST Framework) que actúa como proveedor de datos y servidor de autenticación bajo el estándar OAuth 2.0, y un Frontend ágil e interactivo desarrollado en React mediante Vite. La comunicación entre ambas capas se realiza de manera segura mediante peticiones asíncronas HTTP/HTTPS protegidas por tokens de acceso Bearer.

### Integrantes
* Andres [Nombre Completo]

### Carrera
Ingeniería en Informática

### Universidad
Universidad Internacional SEK (UISEK)

---

## 2. Objetivos del Proyecto

### Objetivo Académico
* Demostrar la capacidad práctica e intelectual para diseñar una arquitectura de software distribuida y desacoplada, aplicando patrones de diseño de software correctos.
* Implementar mecanismos rigurosos de seguridad y control de acceso utilizando el protocolo de autorización OAuth 2.0 a nivel de API REST.
* Consolidar habilidades en el manejo de bases de datos relacionales, persistencia de archivos multimedia y control de políticas de intercambio de recursos de origen cruzado (CORS).

### Expansión hacia un Modelo de Producción Profesional (Teoría de Escalabilidad)
Para transformar este prototipo académico en una plataforma lista para el mercado con alta disponibilidad, se contemplan los siguientes ejes de expansión:
1. **Desacoplamiento de Base de Datos y Almacenamiento:** Migrar el motor local SQLite a una base de datos relacional administrada de nivel empresarial (como PostgreSQL o Amazon RDS). Los archivos multimedia (pósteres y fotos) se trasladarían desde el disco local hacia un servicio de almacenamiento de objetos en la nube, como Amazon S3, distribuyéndolos mediante una red de entrega de contenido (CDN) como Cloudflare.
2. **Contenerización y Orquestación:** Empaquetar de manera independiente las aplicaciones de Frontend y Backend utilizando contenedores Docker. Esto garantizaría que el sistema se ejecute bajo las mismas variables y dependencias exactas en cualquier infraestructura, permitiendo su orquestación automatizada en clústeres mediante Kubernetes.
3. **Escalabilidad Horizontal e Infraestructura Serverless:** Desplegar el Backend detrás de un balanceador de carga (Nginx o AWS ALB) con auto-scaling para levantar instancias dinámicamente según la demanda. El Frontend de React se compilaría a archivos estáticos puros para ser servidos directamente desde infraestructuras Edge (como AWS Amplify, Vercel o Netlify), reduciendo la latencia de carga global a milisegundos.
4. **Seguridad y CI/CD:** Implementar HTTPS mandatorio mediante certificados SSL/TLS administrados, resguardar las credenciales sensibles y llaves maestras en administradores de secretos (como AWS Secrets Manager) e integrar flujos de Integración y Despliegue Continuos (CI/CD) automatizados mediante GitHub Actions.

---

## 3. Definición de la Arquitectura

El sistema implementa una **arquitectura desacoplada en capas**, aislando por completo la lógica de negocio y persistencia de datos (Backend) de la capa de presentación e interacción del usuario (Frontend). 

### Separación de Responsabilidades
* **Backend (Django):** Se encarga exclusivamente de procesar reglas de negocio, exponer los endpoints serializados en formato JSON, validar tokens criptográficos de autorización y gestionar el almacenamiento en la base de datos y archivos locales.
* **Frontend (React):** Se encarga de la interfaz gráfica del usuario, el manejo de rutas del lado del cliente, el almacenamiento temporal de las credenciales de sesión y el consumo asíncrono de los servicios expuestos por el Backend.

---

## 4. Estructura y Contenido de Carpetas

A continuación se detalla la jerarquía física del proyecto y la función técnica de cada módulo:

├── backend/                  # Directorio raíz del Backend (Django)│   ├── backend/              # Configuración global del proyecto de Django│   │   ├── settings.py       # Variables de entorno, APPS, Middlewares y seguridad│   │   ├── urls.py           # Enrutador principal del sistema (Admin, OAuth2)│   │   └── wsgi.py / asgi.py # Interfaces de pasarela para servidores web│   ├── catalog/              # Aplicación local encargada del catálogo de películas│   │   ├── migrations/       # Historial de cambios y mutaciones de la base de datos│   │   ├── models/           # Definición de las entidades (Pelicula, Director, Vendedor)│   │   ├── serializers/      # Lógica de transformación de Modelos a JSON (y viceversa)│   │   ├── views/            # Lógica de control y ViewSets que procesan las peticiones│   │   ├── admin.py          # Registro de modelos en el panel de administración nativo│   │   └── urls.py           # Enrutamiento específico del API de catálogo│   ├── media/                # Almacenamiento local de archivos multimedia (Pósteres/Fotos)│   ├── manage.py             # Utilidad de línea de comandos para la gestión del Backend│   └── requirements.txt      # Manifiesto de dependencias y librerías de Python│├── frontend/                 # Directorio raíz del Frontend (React + Vite)│   ├── public/               # Recursos estáticos globales abiertos (Favicon, SVGs)│   ├── src/                  # Código fuente ejecutable de la interfaz│   │   ├── assets/           # Imágenes y hojas de estilo base│   │   ├── App.jsx           # Componente raíz y lógica principal de la aplicación│   │   └── main.jsx          # Punto de entrada de renderizado de React en el DOM│   ├── index.html            # Lienzo HTML5 principal de la aplicación│   ├── package.json          # Manifiesto de dependencias de Node.js y scripts de ejecución│   └── vite.config.js        # Configuración del compilador y servidor de desarrollo Vite
---

## 5. Instrucciones de Ejecución

### Prerrequisitos del Sistema
Antes de iniciar, asegúrese de contar con los siguientes entornos instalados globalmente en la máquina:
* Python (Versión recomendada: **3.12.x**)
* Node.js (Versión recomendada: **18.x** o superior) junto con su gestor de paquetes `npm`.

### Configuración e Inicio del Backend (Django)

1. Navegue al directorio raíz del backend:
   ```bash
   cd backend
Genere un entorno virtual aislado para evitar colisiones de dependencias:Bash# En Windows
py -3.12 -m venv .venv
# En macOS/Linux
python3.12 -m venv .venv
Active el entorno virtual:Bash# En Windows (PowerShell)
.venv\Scripts\activate
# En Windows (CMD Tradicional)
.venv\Scripts\activate.bat
# En macOS/Linux
source .venv/bin/activate
Instale los módulos obligatorios definidos en el manifiesto de manera limpia:Bashpip install --no-cache-dir -r requirements.txt
Realice las migraciones de esquemas para estructurar la base de datos relacional:Bashpython manage.py makemigrations
python manage.py migrate
Genere la credencial del administrador supremo del sistema (Superusuario):Bashpython manage.py createsuperuser
Inicialice el servidor web de desarrollo:Bashpython manage.py runserver
El servidor quedará a la escucha en la dirección: http://127.0.0.1:8000/Configuración e Inicio del Frontend (React + Vite)En una nueva pestaña de la terminal, navegue al directorio raíz del frontend:Bashcd frontend
Instale los paquetes y dependencias del ecosistema Node.js:Bashnpm install
Ejecute el servidor de desarrollo local del cliente:Bashnpm run dev
La interfaz de usuario quedará disponible en la dirección: http://localhost:5173/Rutas Excluidas del Control de Versiones (.gitignore)Se han excluido de forma explícita del repositorio de Git los archivos y directorios que comprometen la portabilidad o la seguridad del sistema:Carpetas de entornos virtuales (.venv/, env/)Residuos de precompilación de Python (__pycache__/, *.pyc)Base de datos local volátil (db.sqlite3)Directorio local de subida de imágenes de usuarios (media/)Carpeta de módulos de Node.js en el frontend (node_modules/)Archivos temporales de compilación de producción (dist/)6. Rúbrica de Evaluación UtilizadaCriterio de EvaluaciónDescripciónPuntaje MáximoCalificación ObtenidaTotal/7. Recomendaciones Observadas de parte del EstudianteAislamiento Estricto de Entornos: Al desplgar este proyecto en los equipos de los laboratorios de la universidad, se recomienda enfáticamente eliminar cualquier carpeta .venv preexistente o directorios __pycache__ heredados, ya que las variaciones de versión de los intérpretes locales de Python bloquean la correcta inicialización del sistema.Control de Restricciones del Sistema Operativo: En entornos Windows corporativos o universitarios, PowerShell suele bloquear la ejecución de los scripts de activación. Se sugiere realizar las gestiones desde la consola clásica de Símbolo del Sistema (cmd.exe) o modificar la política de ejecución de manera temporal en la sesión abierta mediante comandos bypass.Verificación de Librerías Nativas: Asegurarse de compilar e instalar dependencias con extensiones binarias de C (como Pillow y cryptography) utilizando el flag --no-cache-dir, evitando así que el gestor de paquetes arrastre binarios corruptos alojados en el almacenamiento compartido de la estación de trabajo.8. ConclusionesÉxito del Enfoque Desacoplado: La arquitectura basada en servicios e interfaces independientes demostró ser una solución óptima para el desarrollo moderno, permitiendo que modificaciones de diseño en la interfaz gráfica no alteren de ningún modo la integridad o reglas lógicas configuradas en el servidor.Solidez en Seguridad Criptográfica: La incorporación de django-oauth-toolkit acoplada con las políticas restrictivas de Django REST Framework provee un control de accesos de estándar profesional, limitando eficazmente el consumo de recursos sensibles a clientes que demuestren de forma transparente su autenticidad.Preparación Teórica de Despliegue: Aunque el sistema opera adecuadamente bajo entornos simulados locales (localhost) y almacenamiento SQLite, el diseño modular del backend y la portabilidad del frontend facilitan una transición directa hacia la nube bajo arquitecturas escalables horizontales y entornos automatizados de producción.
