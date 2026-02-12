# Estructura del Curso py121: La Biblioteca Estándar a Fondo

## Enfoque

Curso intermedio-avanzado diseñado como puente hacia ingeniería de datos, CI/CD y desarrollo backend de alto rendimiento.

## Temario

### Módulo 1: Datos y Algoritmos (La base eficiente)

*Manipulación de datos en memoria y flujos de información.*

1. **01_colecciones_avanzadas.ipynb**
   * `collections`: `namedtuple`, `deque` (colas LIFO/FIFO), `Counter`, `defaultdict`.
2. **02_iteradores_y_generadores.ipynb**
   * Generadores, `yield`, `yield from` y el protocolo iterador. La base para entender corrutinas.
3. **03_itertools_y_flujos.ipynb**
   * Procesamiento de streams: `chain`, `zip_longest`, combinatoria (`product`, `permutations`).
4. **04_bytes_y_struct.ipynb**
   * Diferencia entre texto (`str`) y `bytes`. `bytearray`.
   * `struct`: Empaquetado y desempaquetado de datos binarios (C-structs). Reemplaza al obsoleto `array`.

### Módulo 2: Interacción con el Sistema (Infraestructura y CI/CD)

*Controlando el entorno donde corre el código.*

5. **05_sistema_y_argumentos.ipynb**
   * `sys`: `argv` (CLI basics), `exit` (códigos de retorno), `stdin`/`stdout`.
6. **06_variables_de_entorno.ipynb**
   * `os.environ`: Configuración de aplicaciones (The 12-Factor App). Seguridad y secretos.
7. **07_subprocesos_orquestacion.ipynb**
   * `subprocess`: Ejecución robusta de comandos externos. Captura de salidas y manejo de errores.
8. **08_pathlib_sistema_archivos.ipynb**
   * Manipulación de rutas orientada a objetos (vs `os.path`).

### Módulo 3: Robustez y Calidad

*Escribiendo código profesional.*

9. **09_recursos_y_contextlib.ipynb**
   * Gestores de contexto (`with`).
   * `contextlib`: `@contextmanager` y `ExitStack`.
10. **10_logging_avanzado.ipynb**
    * Jerarquías de loggers, handlers, formato JSON. Logs como interfaz de observabilidad.

### Módulo 4: Tiempo y Ejecución (Hacia la asincronía)

11. **11_datetime_moderno.ipynb**
    * Manejo de fechas con `zoneinfo` (sin `pytz`). Aritmética segura. `time.monotonic`.
12. **12_hilos_y_procesos.ipynb**
    * GIL, CPU-bound (`multiprocessing`) vs I/O-bound (`threading`).
13. **13_futuros_y_ejecutores.ipynb**
    * `concurrent.futures`: abstracción moderna (`ThreadPoolExecutor`, `ProcessPoolExecutor`).

### Módulo 5: AsyncIO (La joya de la corona)

*Donde convergen los generadores, recursos y concurrencia.*

14. **14_fundamentos_asyncio.ipynb**
    * Multitarea cooperativa. `async`/`await`. Event Loop.
15. **15_gestion_tareas_async.ipynb**
    * `create_task`, `gather`, `wait_for` (timeouts), cancelación.
16. **16_sincronizacion_asincrona.ipynb**
    * `asyncio.Lock`, `asyncio.Queue` (Productor-Consumidor async).
17. **17_contextvars_y_conclusiones.ipynb**
    * `contextvars`: Estado local en contextos asíncronos (request-ids, tracing).
