# Biblioteca Estándar de Python (Py121)

[Python](https://www.python.org/) [Codespaces](https://github.com/features/codespaces) [License](LICENSE)

> Estado: ✅ Curso Activo | Nivel: Intermedio

Este repositorio contiene el material oficial del curso Py121, enfocado en dominar la **Biblioteca Estándar de Python** para construir aplicaciones robustas, eficientes y escalables. Es la continuación de [Py111](https://github.com/PythonistaMX/py111) y el paso previo a estructuras de datos complejas.

> **⚠️ Nota Importante:** Este repositorio ha sido actualizado en 2026 con contenido moderno (Python 3.12+). Si buscas el material original, puedes encontrarlo en la rama [legacy](../../tree/legacy).

## 🗺️ Ruta de Aprendizaje

Este curso forma parte de la serie **Fundamentos de Python (py1xx)**:

| Curso | Título | Estado |
| :---: | :--- | :--- |
| **py101** | Introducción a Python 3 | Prerrequisito |
| **py111** | POO con Python 3 | Prerrequisito |
| **py121** | Biblioteca estándar de Python | ✅ **Este curso** |
| **py131** | Estructuras de Datos y Algoritmia | Siguiente paso |
| **py141** | Automatización y Extracción de Datos | Aplicación práctica |

## 🚀 Acerca del Curso

Un programa diseñado para servir como puente hacia la ingeniería de datos, desarrollo backend de alto rendimiento y orquestación de sistemas. Al completarlo serás capaz de:

*   **Manipular datos eficientemente** utilizando colecciones avanzadas, iteradores y formatos binarios.
*   **Interactuar con el sistema operativo**, gestionando archivos, procesos y variables de entorno.
*   **Escribir código robusto** mediante logging avanzado y gestión segura de recursos.
*   **Dominar la concurrencia y el paralelismo** con hilos, procesos y futuros.
*   **Implementar programación asíncrona** moderna utilizando `asyncio`.

## 📅 Temario y Estructura

El contenido está dividido en cuadernos (notebooks) progresivos:

### 📚 Contenidos

*   `01` - [Colecciones Avanzadas](01_colecciones_avanzadas.ipynb)
*   `02` - [Iteradores y Generadores](02_iteradores_y_generadores.ipynb)
*   `03` - [Itertools y Functools](03_itertools_y_functools.ipynb)
*   `04` - [Bytes y Struct](04_bytes_y_struct.ipynb)
*   `05` - [Expresiones Regulares](05_expresiones_regulares.ipynb)
*   `06` - [Datos CSV y JSON](06_datos_csv_json.ipynb)
*   `07` - [Sistema y Argumentos](07_sistema_y_argumentos.ipynb)
*   `08` - [Variables de Entorno](08_variables_de_entorno.ipynb)
*   `09` - [Subprocesos y Orquestación](09_subprocesos_orquestacion.ipynb)
*   `10` - [Pathlib y Sistema de Archivos](10_pathlib_sistema_archivos.ipynb)
*   `11` - [Recursos y Contextlib](11_recursos_y_contextlib.ipynb)
*   `12` - [Logging Avanzado](12_logging_avanzado.ipynb)
*   `13` - [Datetime Moderno](13_datetime_moderno.ipynb)
*   `14` - [Hilos y Procesos](14_hilos_y_procesos.ipynb)
*   `15` - [Futuros y Ejecutores](15_futuros_y_ejecutores.ipynb)
*   `16` - [Fundamentos de AsyncIO](16_fundamentos_asyncio.ipynb)
*   `17` - [Gestión de Tareas Async](17_gestion_tareas_async.ipynb)
*   `18` - [Sincronización Asíncrona](18_sincronizacion_asincrona.ipynb)
*   `19` - [Contextvars y Conclusiones](19_contextvars_y_conclusiones.ipynb)

## 🛠️ Instalación y Uso

¡Olvídate de configurar entornos locales complejos! Este repositorio está configurado para **GitHub Codespaces**.

1.  Haz clic en el botón **"Code"** (verde) arriba a la derecha.
2.  Ve a la pestaña **"Codespaces"**.
3.  Haz clic en **"Create codespace on main"**.

El entorno se iniciará automáticamente con Python 3 y todas las extensiones necesarias listas para usar.

### Ejecución Local (Opcional)

Si prefieres trabajar en tu máquina:

1.  **Clonar el repositorio**
    ```bash
    git clone https://github.com/PythonistaMX/py121.git
    cd py121
    ```

2.  **Crear entorno virtual (Recomendado)**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Iniciar Jupyter**
    ```bash
    # (Asegúrate de tener jupyter instalado o instálalo con pip install jupyterlab)
    jupyter lab
    ```

## 📝 Licencia

Este material es desarrollado y mantenido por **José Luis Chiquete Valdivieso**.

Este proyecto está bajo la licencia **Creative Commons Atribución 4.0 Internacional (CC-BY 4.0)**.

Eres libre de:

*   ✅ **Compartir** el material en cualquier medio o formato
*   ✅ **Adaptar**, remezclar y crear contenido derivado
*   ✅ **Usar** con fines comerciales

Con la condición de:

*   📌 **Atribución**: Debes dar crédito apropiado, proporcionar un enlace a la licencia e indicar si se han realizado cambios.

Véase el archivo [LICENSE](LICENSE) para los términos completos.
