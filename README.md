# py121: La Biblioteca Estándar de Python a Fondo

> **⚠️ Nota Importante:** Este repositorio ha sido actualizado en 2026 con contenido moderno (Python 3.12+). Si buscas el material original, puedes encontrarlo en la rama [legacy](../../tree/legacy).

Este curso está diseñado como un puente hacia la ingeniería de datos, CI/CD y desarrollo backend de alto rendimiento, explorando a fondo la biblioteca estándar de Python.

## Temario

### Módulo 1: Datos y Algoritmos (La base eficiente)
*Manipulación de datos en memoria y flujos de información.*
* Colecciones avanzadas
* Iteradores y generadores
* Itertools y flujos
* Bytes y struct
* Expresiones Regulares
* Formatos de Intercambio (CSV y JSON)

### Módulo 2: Interacción con el Sistema
*Controlando el entorno donde corre el código.*
* Sistema y argumentos
* Variables de entorno
* Subprocesos y orquestación
* Pathlib y sistema de archivos

### Módulo 3: Robustez y Calidad
*Escribiendo código profesional.*
* Recursos y contextlib
* Logging avanzado

### Módulo 4: Tiempo y Ejecución
*Hacia la asincronía.*
* Datetime moderno
* Hilos y procesos
* Futuros y ejecutores

### Módulo 5: AsyncIO
*La joya de la corona.*
* Fundamentos de AsyncIO
* Gestión de tareas Async
* Sincronización asíncrona
* Contextvars y conclusiones

## Configuración del Entorno de Desarrollo

Puedes seguir este curso utilizando Docker, GitHub Codespaces o Visual Studio Code con Dev Containers.

### Opción A: GitHub Codespaces (Recomendado en la nube)
1. Haz clic en el botón de **Code** en el repositorio de GitHub.
2. Selecciona la pestaña **Codespaces**.
3. Haz clic en **Create codespace on master**.
4. El entorno se configurará automáticamente con todas las dependencias necesarias.

### Opción B: VS Code con Dev Containers (Local)
Requisitos: Docker Desktop y VS Code con la extensión "Dev Containers" instalada.

1. Clona este repositorio.
2. Abre la carpeta en VS Code.
3. Cuando aparezca la notificación "Reopen in Container", haz clic en ella. O abre la paleta de comandos (F1) y selecciona **Dev Containers: Reopen in Container**.
4. VS Code construirá la imagen de Docker y configurará el entorno.

### Opción C: Ejecución Local
Requisitos: Python 3.10 o superior.

1. Clona el repositorio.
2. Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias (si las hubiera):
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta Jupyter Lab o abre los notebooks en VS Code.

## Nota sobre Versiones Anteriores (Legacy)

El material original de este curso (versión introductoria a minería de datos y data wrangling) ha sido movido a una rama dedicada para preservación histórica.

Si buscas el material antiguo, puedes acceder a él cambiando a la rama `legacy`:

```bash
git checkout legacy
```

O seleccionando la rama "legacy" en el selector de ramas de GitHub.
