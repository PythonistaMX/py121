# Estructura del Curso py121: La Biblioteca Estándar a Fondo

## Enfoque

Curso intermedio-avanzado diseñado como puente hacia ingeniería de datos, CI/CD y desarrollo backend de alto rendimiento.

## Temario

### Módulo 1: Datos y Algoritmos (La base eficiente)

*Manipulación de datos en memoria y flujos de información.*

1. **01_colecciones_avanzadas.ipynb**
   * `collections`: `namedtuple`, `deque` (colas LIFO/FIFO), `Counter`, `defaultdict`.
2. **02_iteradores_y_generadores.ipynb**
   * Generadores avanzados y flujos de datos.
   * `yield` como entrada/salida: `send()`, `throw()`, `close()`.
   * Delegación con `yield from`. Expresiones generadoras vs Comprensiones.
3. **03_itertools_y_functools.ipynb**
   * Programación funcional pragmática.
   * `itertools`: Procesamiento de streams (`chain`, `zip_longest`) y combinatoria.
   * `functools`: Aplicación parcial (`partial`), caché (`lru_cache`), reducción (`reduce`) y decoradores (`wraps`).
4. **04_bytes_y_struct.ipynb**
   * Diferencia entre texto (`str`) y `bytes`. `bytearray`.
   * `struct`: Empaquetado y desempaquetado de datos binarios (C-structs). Reemplaza al obsoleto `array`.
5. **05_expresiones_regulares.ipynb**
    * Uso avanzado módulo `re`:  compilación, banderas, grupos con nombre y optimización de patrones.
6. **06_datos_csv_json.ipynb**
    * Manipulación eficiente de CSV y JSON. Dialectos, Encoders personalizados y técnicas de streaming.

### Módulo 2: Interacción con el Sistema (Infraestructura y CI/CD)

*Controlando el entorno donde corre el código.*

7. **07_sistema_y_argumentos.ipynb**
   * `sys`: `argv` (CLI basics), `exit` (códigos de retorno), `stdin`/`stdout`.
8. **08_variables_de_entorno.ipynb**
   * `os.environ`: Configuración de aplicaciones (The 12-Factor App). Seguridad y secretos.
9. **09_subprocesos_orquestacion.ipynb**
   * `subprocess`: Ejecución robusta de comandos externos. Captura de salidas y manejo de errores.
10. **10_pathlib_sistema_archivos.ipynb**
   * Manipulación de rutas orientada a objetos (vs `os.path`).

### Módulo 3: Robustez y Calidad

*Escribiendo código profesional.*

11. **11_recursos_y_contextlib.ipynb**
   * Gestores de contexto (`with`).
   * `contextlib`: `@contextmanager` y `ExitStack`.
12. **12_logging_avanzado.ipynb**
    * Jerarquías de loggers, handlers, formato JSON. Logs como interfaz de observabilidad.

### Módulo 4: Tiempo y Ejecución (Hacia la asincronía)

13. **13_datetime_moderno.ipynb**
    * Manejo de fechas con `zoneinfo` (sin `pytz`). Aritmética segura. `time.monotonic`.
14. **14_hilos_y_procesos.ipynb**
    * GIL, CPU-bound (`multiprocessing`) vs I/O-bound (`threading`).
15. **15_futuros_y_ejecutores.ipynb**
    * `concurrent.futures`: abstracción moderna (`ThreadPoolExecutor`, `ProcessPoolExecutor`).

### Módulo 5: AsyncIO (La joya de la corona)

*Donde convergen los generadores, recursos y concurrencia.*

16. **16_fundamentos_asyncio.ipynb**
    * Multitarea cooperativa. `async`/`await`. Event Loop.
17. **17_gestion_tareas_async.ipynb**
    * `create_task`, `gather`, `wait_for` (timeouts), cancelación.
18. **18_sincronizacion_asincrona.ipynb**
    * `asyncio.Lock`, `asyncio.Queue` (Productor-Consumidor async).
19. **19_contextvars_y_conclusiones.ipynb**
    * `contextvars`: Estado local en contextos asíncronos (request-ids, tracing).
