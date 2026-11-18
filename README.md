# Programación básica en C · curso interactivo CLT4BP

Curso web de programación básica en C (C17) diseñado con el modelo instruccional **mapa de ruta CLT4BP** (Sandoval Medina, 2026): 17 temas organizados en 4 bloques, cada uno con los cinco pasos del modelo (información de soporte, información procedimental, tareas de aprendizaje, protocolo verbal y evaluación), dos rutas según los conocimientos previos y una guía docente.


## Qué incluye

| Página | Para qué sirve |
|---|---|
| `index.html` | Mapa de ruta del curso: cada tema es una parada; las vías A y B se iluminan según la ruta elegida y las paradas se rellenan con el avance. |
| `diagnostico.html` | Diagnóstico por bloque (8 reactivos, calificación automática). Con 70 % o más sugiere la Ruta B; con menos, la Ruta A. |
| `tema-01.html` … `tema-17.html` | Los cinco pasos del tema, glosario, fuentes y ficha docente. Problemas por completar con calificación inmediata, programas con salida real («Ejecutar»), enlace a Compiler Explorer para editar y ejecutar, soluciones plegadas, recall test y comprehension test con autoevaluación, autorregistro con la escala de esfuerzo mental. |
| `progreso.html` | Avance por tema, gráfica de desempeño contra esfuerzo mental, encuesta de carga cognitiva por bloque (anexo A.7 de la tesis) y exportación del progreso en JSON o CSV. |
| `glosario.html` | Los 213 términos bilingües de los 17 temas, con búsqueda. |
| `guia.html` | Guía docente: cómo aplicar las tres fases del modelo, formatos de registro y enlaces a las fichas y a los PDF. |
| `pdf/` | Los 18 cuadernillos en PDF (versión imprimible, con todas las soluciones). |

El progreso de cada alumno se guarda **solo en su navegador** (`localStorage`). No hay servidor ni cuentas; para entregar resultados al docente, el alumno descarga el JSON o el CSV desde «Mi progreso».




Estructura:

```
docs/          sitio publicado (lo genera engine/web.py; no editar a mano)
temas/         contenido fuente de los 17 temas y la guía (00_guia.md)
engine/
  render.py    motor común: Markdown → HTML, compilación y ejecución con gcc, PDF
  echo_stdin.c eco de la entrada en las salidas (solo al generar el material)
  asan_check.py  ejecuta los programas de un tema con AddressSanitizer y UBSan
  Dockerfile   entorno reproducible para regenerar (GCC 14, make, Graphviz, Chromium)
  web.py       generador del sitio web
  web_diag.py  reactivos del diagnóstico (se verifican compilándolos)
  diagrams.py  diagramas SVG (memoria, arreglos, pila, Graphviz)
  web/         CSS, JavaScript y fuentes del sitio
```

## Notas

- **Compiler Explorer.** El botón «Probar en Compiler Explorer» abre el programa en godbolt.org (GCC 14.2, `-std=c17 -Wall -Wextra`) con los datos de entrada del ejemplo; en los problemas por completar lleva lo que el alumno escribió en los huecos. Los programas del Tema 16 que leen archivos y los del Tema 17, formados por varios archivos, se deben probar en la computadora del alumno.
- **Fuentes tipográficas.** Overpass, Overpass Mono e Inter (SIL Open Font License) y DejaVu Sans Mono (licencia Bitstream Vera) están incluidas en `docs/assets/fonts/`; ver `LICENCIAS.txt`.

## Créditos

- Modelo instruccional: Sandoval Medina, C. (2026). *Mapa de ruta CLT4BP*. Tesis doctoral, Universidad Autónoma de Aguascalientes.
- Fuentes del temario: King, K. N. (2008). *C Programming: A Modern Approach* (2.ª ed.). W. W. Norton. Kernighan, B. W. y Ritchie, D. M. (1988). *The C Programming Language* (2.ª ed.). Prentice Hall. Seacord, R. C. (2020). *Effective C*. No Starch Press.
- Ejercicios del Tema 03 adaptados a C de: Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Ediciones de la U / Ra-Ma.
