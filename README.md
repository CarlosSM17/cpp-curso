# Programación básica en C++ · curso interactivo CLT4BP

Curso web de programación básica en C++ diseñado con el modelo instruccional **mapa de ruta CLT4BP** (Sandoval Medina, 2026): 17 temas organizados en 4 bloques, cada uno con los cinco pasos del modelo (información de soporte, información procedimental, tareas de aprendizaje, protocolo verbal y evaluación), dos rutas según los conocimientos previos y una guía docente.

El sitio es estático (HTML, CSS y JavaScript sin dependencias externas) y está listo para **GitHub Pages**.

## Qué incluye

| Página | Para qué sirve |
|---|---|
| `index.html` | Mapa de ruta del curso: cada tema es una parada; las vías A y B se iluminan según la ruta elegida y las paradas se rellenan con el avance. |
| `diagnostico.html` | Diagnóstico por bloque (8 reactivos, calificación automática). Con 70 % o más sugiere la Ruta B; con menos, la Ruta A. |
| `tema-01.html` … `tema-17.html` | Los cinco pasos del tema, glosario, fuentes y ficha docente. Problemas por completar con calificación inmediata, programas con salida real («Ejecutar»), enlace a Compiler Explorer para editar y ejecutar, soluciones plegadas, recall test y comprehension test con autoevaluación, autorregistro con la escala de esfuerzo mental. |
| `progreso.html` | Avance por tema, gráfica de desempeño contra esfuerzo mental, encuesta de carga cognitiva por bloque (anexo A.7 de la tesis) y exportación del progreso en JSON o CSV. |
| `glosario.html` | Los 216 términos bilingües de los 17 temas, con búsqueda. |
| `guia.html` | Guía docente: cómo aplicar las tres fases del modelo, formatos de registro y enlaces a las fichas y a los PDF. |
| `pdf/` | Los 18 cuadernillos en PDF (versión imprimible, con todas las soluciones). |

El progreso de cada alumno se guarda **solo en su navegador** (`localStorage`). No hay servidor ni cuentas; para entregar resultados al docente, el alumno descarga el JSON o el CSV desde «Mi progreso».

## Publicar en GitHub Pages

1. Crea un repositorio en GitHub (por ejemplo, `curso-cpp-clt4bp`) y sube esta carpeta completa:

   ```bash
   git init
   git add .
   git commit -m "Curso interactivo de programación básica en C++ (CLT4BP)"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/curso-cpp-clt4bp.git
   git push -u origin main
   ```

2. En el repositorio: **Settings → Pages → Build and deployment**. En *Source* elige **Deploy from a branch**; en *Branch*, **main** y la carpeta **/docs**. Guarda.
3. En uno o dos minutos el curso queda en `https://TU_USUARIO.github.io/curso-cpp-clt4bp/`.

El archivo `docs/.nojekyll` evita que GitHub procese el sitio con Jekyll.

### Probarlo en tu computadora

```bash
python3 -m http.server 8000 --directory docs
```

y abre `http://localhost:8000`. (También funciona abriendo `docs/index.html` directamente, pero algunos navegadores limitan el guardado del progreso en archivos locales.)

## Modificar el contenido y regenerar el sitio

El contenido de cada tema está en `temas/NN_*.md` (Markdown con directivas propias: cajas `:::concepto`, `:::tarea`, `:::solucion`, bloques ```` ```cpp run ```` que se compilan y ejecutan, diagramas `dot`, etc.). El generador vuelve a compilar con g++ cada programa que cambió, así que las salidas mostradas siempre son reales.

Requisitos: Python 3.12 o superior, `g++` (C++20), Graphviz (`dot`) y los paquetes `markdown`, `pyyaml` y `pygments`.

```bash
pip install markdown pyyaml pygments
python3 engine/web.py              # regenera docs/
```

Para regenerar un cuadernillo PDF (requiere además `playwright` con Chromium y `pypdf`):

```bash
python3 engine/render.py temas/08_vectores.md   # escribe out/Tema08_….pdf
python3 engine/web.py                           # copia los PDF de out/ a docs/pdf/
```

Estructura:

```
docs/          sitio publicado (lo genera engine/web.py; no editar a mano)
temas/         contenido fuente de los 17 temas y la guía (00_guia.md)
engine/
  render.py    motor común: Markdown → HTML, compilación y ejecución con g++, PDF
  web.py       generador del sitio web
  web_diag.py  reactivos del diagnóstico (se verifican compilándolos)
  diagrams.py  diagramas SVG (memoria, arreglos, pila, Graphviz)
  web/         CSS, JavaScript y fuentes del sitio
```

## Notas

- **Compiler Explorer.** El botón «Probar en Compiler Explorer» abre el programa en godbolt.org (GCC 13.2, `-std=c++20`) con los datos de entrada del ejemplo; en los problemas por completar lleva lo que el alumno escribió en los huecos. Los programas del Tema 16 que leen archivos se deben probar en la computadora del alumno.
- **Fuentes tipográficas.** Overpass, Overpass Mono e Inter (SIL Open Font License) y DejaVu Sans Mono (licencia Bitstream Vera) están incluidas en `docs/assets/fonts/`; ver `LICENCIAS.txt`.

## Créditos

- Modelo instruccional: Sandoval Medina, C. (2026). *Mapa de ruta CLT4BP*. Tesis doctoral, Universidad Autónoma de Aguascalientes.
- Fuentes del temario: Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Ediciones de la U / Ra-Ma. Lospinoso, J. (2019). *C++ Crash Course*. No Starch Press.
