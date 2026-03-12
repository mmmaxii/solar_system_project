# Proyecto: Alke Web Base - Sistema Solar Interactivo

Este repositorio contiene el código fuente correspondiente al proyecto del Módulo 6: Desarrollo Web con Django - Fundamentos, desarrollado como parte de las asignaciones de Alke Solutions.

El proyecto consiste en una aplicación web dinámica construida sobre el framework Django. Su propósito es demostrar la comprensión práctica de la arquitectura modelo-vista-plantilla (MVT), la configuración de rutas, y la correcta integración de archivos estáticos y renderizado del lado del cliente.

## Estructura del Proyecto e Implementación de Requerimientos

El desarrollo cumple con las siguientes especificaciones técnicas establecidas en la rúbrica de evaluación:

### 1. Configuración del Proyecto Django
Se configuró un entorno virtual aislado y se inicializó un proyecto base funcional en Django. El entorno de desarrollo principal utilizado fue Visual Studio Code. El proyecto puede ejecutarse localmente sin errores utilizando el servidor de pruebas integrado de Django.

### 2. Estructura y Aplicaciones
El proyecto cuenta con una aplicación principal orientada a la visualización de los cuerpos celestes del sistema solar. Esta aplicación ha sido debidamente registrada en el arreglo `INSTALLED_APPS` dentro del archivo de configuración global `settings.py`, respetando la separación de responsabilidades y la estructura de directorios recomendada por el framework.

### 3. Vistas y Rutas
Se implementó un sistema de enrutamiento adecuado:
- **Rutas (URLs):** Se configuraron rutas tanto a nivel principal del proyecto como a nivel de la aplicación, permitiendo la navegación fluida entre la página de inicio (sistema solar general) y las vistas detalladas (por ejemplo, la vista del Sol).
- **Vistas:** El archivo `views.py` contiene la lógica para manejar las peticiones HTTP y retornar las respuestas y plantillas correspondientes a cada ruta solicitada.

### 4. Templates y Archivos Estáticos
La capa de presentación integra múltiples tecnologías para ofrecer una experiencia interactiva:
- **Templates HTML:** Integración del sistema de plantillas de Django, haciendo uso de etiquetas como `{% url %}` y `{% static %}` para referenciar recursos de forma dinámica.
- **Archivos Estáticos (CSS y JS):** 
  - Archivos locales organizados estructuradamente en la carpeta `static/` dedicada de la aplicación.
  - Implementación de hojas de estilo modernas utilizando técnicas de diseño de interfaz avanzadas (como Glassmorphism) y disposiciones dinámicas de contenido que reaccionan al desplazamiento de la página.
- **Renderizado 3D:** Integración del lado del cliente con la biblioteca `Three.js` (cargada a través de CDN) para renderizar modelos 3D interactivos, utilizando de texturas mapeadas localmente.

## Instrucciones de Ejecución

Para iniciar el proyecto en un entorno local, se deben seguir los siguientes pasos desde la terminal, situándose en la raíz del repositorio:

1. Crear y activar el entorno virtual (recomendado):
   ```bash
   python -m venv venv
   
   # En Windows:
   .\venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

2. Instalar las dependencias necesarias:
   ```bash
   pip install django
   ```

3. Navegar al directorio de trabajo del proyecto y ejecutar el servidor de desarrollo:
   ```bash
   cd solar_system
   python manage.py runserver
   ```

El proyecto estará disponible para su visualización en el navegador a través de la dirección local: `http://127.0.0.1:8000/`.
