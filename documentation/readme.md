<div align="center">
  <img width="1568" height="479" alt="image" src="https://github.com/user-attachments/assets/0c822373-5963-4c93-9120-29a3657ddbb4" />
    <h1>INSTITUTO TECNOLÓGICO DE TIJUANA</h1>
    <br>
    <h3>INGENIERÍA EN SISTEMAS COMPUTACIONALES</h3>
    <br>
    <br>
    <br>
    <h2>PROYECTO FINAL: SISTEMAS programables</h2>
    <br>
    <h1>"PROLOGCUES: SISTEMA DE INFERENCIA DE PERFILES COGNITIVOS"</h1>
    <br>
    <br>
    <br>
    <p><strong>Desarrollado por:</strong><br>Corza Morales Ian Kurt <br>Angel Andres Castro Balbuena <br>Macedo Cruz Jennifer Nicole</p>
    <br>
    <p><strong>Fecha:</strong><br>Noviembre 2025</p>
</div>

---

## 1. Título del Proyecto
**Sistema Experto Híbrido (Python-Prolog) para la Detección Preliminar de Patrones Neurodivergentes.**

---

## 2. Planteamiento del Problema

En la actualidad, el acceso a diagnósticos psicológicos y neurológicos formales suele ser limitado debido a altos costos, largas listas de espera y la centralización de los servicios de salud. Esto lleva a muchas personas a buscar respuestas en internet mediante "quizzes" o cuestionarios web que carecen de rigor lógico, basándose meramente en condicionales simples o sumatorias arbitrarias.

El problema radica en la falta de herramientas accesibles que utilicen **Lógica de Primer Orden** para procesar síntomas y rasgos de comportamiento de manera estructurada. Existe una necesidad de cerrar la brecha entre la **Inteligencia Artificial Simbólica** (capaz de razonar sobre hechos y reglas) y las interfaces de usuario modernas, para ofrecer una herramienta de orientación que, sin sustituir al médico, provea un análisis preliminar más robusto que un test convencional.

---

## 3. Objetivos

### 3.1 Objetivo General
Desarrollar un Sistema Experto basado en reglas lógicas utilizando el lenguaje **Prolog**, integrado con una interfaz de usuario en **Python**, capaz de inferir la probabilidad de un perfil neurotípico o neurodivergente basándose en una base de conocimientos predefinida.

### 3.2 Objetivos Específicos
1.  **Diseñar la Base de Conocimientos:** Codificar hechos y reglas de inferencia en Prolog (`reglas_nd.pl`) que representen indicadores comunes de neurodivergencia (sensibilidad sensorial, función ejecutiva, etc.).
2.  **Implementar el Motor de Inferencia:** Configurar la comunicación bidireccional entre Python y el motor SWI-Prolog mediante la librería `pyswip`.
3.  **Desarrollar la Interfaz de Usuario (CLI):** Crear una experiencia de usuario interactiva y visualmente clara en la consola utilizando librerías de diseño como `rich` y `pyfiglet`.
4.  **Validar la Lógica:** Comprobar que el sistema sea capaz de discriminar entre perfiles basándose en la acumulación de hechos (evidencia) y umbrales lógicos definidos.

---

## 4. Hipótesis

Si se implementa un sistema que separe la lógica de decisión (Backend en Prolog) de la capa de interacción (Frontend en Python), entonces será posible crear una herramienta de diagnóstico preliminar que sea **escalable y modificable**.

Se plantea que, al utilizar un motor de inferencia lógica que cuente hechos dinámicamente (`findall/3`), el sistema podrá determinar con mayor precisión un perfil cognitivo basado en un umbral de síntomas, superando la rigidez de los algoritmos procedimentales tradicionales (`if-else` anidados) y demostrando la utilidad de la programación lógica en sistemas de apoyo a la toma de decisiones.

---

## 5. Metodología

Para el desarrollo de este proyecto se utilizó una metodología **Incremental Modular**, dividiendo el sistema en dos componentes principales que se comunican entre sí.

### 5.1 Herramientas y Tecnologías
* **Lenguaje Lógico:** Prolog (Motor SWI-Prolog). Utilizado para el razonamiento y almacenamiento de hechos temporales.
* **Lenguaje Anfitrión:** Python 3.12. Utilizado para el manejo de flujo, entrada/salida de datos y diseño.
* **Librerías Clave:**
    * `pyswip`: Puente de conexión Python-Prolog.
    * `rich`: Para el diseño de interfaz gráfica en terminal (TUI).
    * `pyfiglet`: Generación de arte ASCII para títulos.

### 5.2 Fases del Desarrollo

#### Fase 1: Ingeniería del Conocimiento (Prolog)
Se investigaron rasgos comunes asociados a la neurodivergencia (TEA/TDAH) y se tradujeron a sintaxis de Prolog. Se definieron predicados como `indicador(X)` para los hechos y reglas como `resultado(X)` que evalúan la cantidad de indicadores presentes en la memoria de trabajo.

#### Fase 2: Desarrollo del Motor (Backend)
Se instaló y configuró SWI-Prolog en el entorno de Windows, asegurando su presencia en las Variables de Entorno (PATH). Se creó el script de Python encargado de cargar el archivo `.pl`, inyectar los hechos (`assertz`) según las respuestas del usuario y realizar consultas (`query`) al motor.

#### Fase 3: Diseño de Interfaz (Frontend CLI)
Se implementó una interfaz de línea de comandos mejorada. Se sustituyeron los `print` básicos por paneles, colores y barras de progreso para mejorar la experiencia de usuario (UX), asegurando que el usuario entienda claramente que se trata de una simulación académica.

#### Fase 4: Pruebas e Integración
Se realizaron pruebas unitarias para verificar casos borde:
* Usuario con 0 síntomas -> Resultado: Neurotípico.
* Usuario con 10 síntomas -> Resultado: Neurodivergente.
* Manejo de errores si el motor Prolog no está instalado.

Esta arquitectura permite que, en el futuro, se puedan modificar las reglas médicas en el archivo Prolog sin necesidad de reescribir el código de la interfaz en Python.
