---
num: "00"
tipo: guia
kicker: "Guía del instructor"
archivo: "Tema00_Guia_del_instructor_CLT4BP"
titulo: "Guía del instructor: aplicar el mapa de ruta CLT4BP al curso de programación básica en C++"
corto: "Fases 1 a 3 del modelo"
lema: "Analizar a quién se enseña, diseñar para su memoria de trabajo, aplicar, medir… y volver a empezar si hace falta."
pasos_portada:
  - ["soporte", "Fase 1<br>Análisis"]
  - ["procedimental", "Fase 2<br>Diseño y desarrollo"]
  - ["tareas", "Rutas A y B<br>(Tomlinson)"]
  - ["evaluacion", "Fase 3<br>Aplicación y evaluación"]
  - ["protocolo", "Iterar si no se<br>cumplen objetivos"]
fuentes:
  - "Sandoval Medina, C. (2026). *Modelo de diseño instruccional «mapa de ruta CLT4BP» basado en la teoría de la carga cognitiva como apoyo en la enseñanza–aprendizaje de la programación*. Tesis doctoral, Universidad Autónoma de Aguascalientes. Caps. 4–7 y anexos A.1–A.7."
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Ediciones de la U / Ra-Ma."
  - "Lospinoso, J. (2019). *C++ Crash Course: A Fast-Paced Introduction*. No Starch Press."
glosario:
  - ["teoría de la carga cognitiva (TCC)", "cognitive load theory (CLT)", "Teoría que diseña la instrucción considerando los límites de la memoria de trabajo."]
  - ["memoria de trabajo", "working memory", "Memoria de capacidad y duración limitadas donde se procesa la información nueva."]
  - ["esquema", "schema", "Estructura de conocimiento en la memoria de largo plazo que agrupa muchos elementos en uno."]
  - ["carga intrínseca", "intrinsic load", "Carga debida a la complejidad propia del contenido (interactividad de elementos)."]
  - ["carga extrínseca", "extraneous load", "Carga causada por un diseño instruccional deficiente; debe reducirse."]
  - ["carga pertinente", "germane load", "Esfuerzo dedicado a construir esquemas; debe favorecerse."]
  - ["modelo 4C/ID", "four-component instructional design", "Modelo de van Merriënboer: tareas de aprendizaje, información de soporte, información procedimental y práctica de tareas parciales."]
  - ["diez pasos", "Ten Steps to Complex Learning", "Guía práctica para aplicar el modelo 4C/ID."]
  - ["instrucción diferenciada", "differentiated instruction (DI)", "Modelo de Tomlinson: adaptar contenido, proceso, producto y entorno a los estudiantes."]
  - ["modelo ARCS", "ARCS model", "Modelo motivacional de Keller: atención, relevancia, confianza y satisfacción."]
  - ["protocolo verbal", "verbal protocol / think-aloud", "Explicación en voz alta del CÓMO y el POR QUÉ de un experto al resolver un problema."]
  - ["desvanecimiento de guía", "guidance fading", "Retirar gradualmente la ayuda conforme crece la pericia."]
  - ["reversión de la experiencia", "expertise reversal", "Lo que ayuda a un novato puede estorbar a un estudiante avanzado."]
  - ["eficiencia mental", "mental efficiency", "Relación entre el desempeño y el esfuerzo mental invertido."]
---

# 1. Cómo usar este material {.guia}

Esta colección es el producto de las **Fases 1 y 2** del modelo instruccional **mapa de ruta CLT4BP** (*Cognitive Load Theory for Basic Programming*) aplicado a un curso completo de programación básica en C++, y una propuesta lista para la **Fase 3**. Consta de esta guía y de **17 cuadernillos**, uno por tema, que pueden usarse completos (un semestre) o por separado (un tema o una unidad), como prevé el modelo.

:::resumen | El mapa de ruta CLT4BP
```dot w="100%"
rankdir=TB; nodesep=0.3; ranksep=0.32; newrank=true;
node [fontsize=11.5, width=2.3];
subgraph cluster1 { label="FASE 1 · ANÁLISIS"; fontname="Inter Display"; fontsize=11; fontcolor="#1d4ed8"; style="rounded,filled"; fillcolor="#f8fbff"; color="#93c5fd";
  a1 [label="Objetivos de aprendizaje\ny métodos de evaluación\n(recall · comprehension)"];
  a2 [label="Entorno grupal:\nmotivación (MSLQ),\nprevios, estrategias"];
  a3 [label="Preselección de efectos\nde la TCC por tema"];
  d1 [shape=diamond, style="filled", fillcolor="#fff7ed", color="#c2410c", label="¿Previos\nheterogéneos?", fontsize=11, width=1.6];
  a1 -> a2 -> a3 -> d1;
}
subgraph cluster2 { label="FASE 2 · DISEÑO Y DESARROLLO"; fontname="Inter Display"; fontsize=11; fontcolor="#6d28d9"; style="rounded,filled"; fillcolor="#fbfaff"; color="#c4b5fd";
  b0 [label="Estrategias diferenciadas\n(Tomlinson)\nRuta A  ·  Ruta B", fillcolor="#ecfdf5", color="#059669"];
  b1 [label="Tareas de aprendizaje\n(ARCS · DI · efectos TCC)", fillcolor="#ecfdf5", color="#059669"];
  b2 [label="Información de soporte\n(ARCS · DI · efectos TCC)"];
  b3 [label="Información procedimental\n(isomórficos · guías ·\nprotocolos verbales)", fillcolor="#f5f3ff", color="#7c3aed"];
  b0 -> b1 -> b2 -> b3;
}
subgraph cluster3 { label="FASE 3 · APLICACIÓN Y EVALUACIÓN"; fontname="Inter Display"; fontsize=11; fontcolor="#be123c"; style="rounded,filled"; fillcolor="#fffafa"; color="#fda4af";
  c1 [label="Plan de implementación:\nsoporte → tareas\n(+ procedimental justo a tiempo)"];
  c2 [label="Evaluación: recall y\ncomprehension, carga cognitiva,\nCIS, IMMS, MSLQ final"];
  d2 [shape=diamond, style="filled", fillcolor="#fff7ed", color="#c2410c", label="¿Objetivos\ncumplidos?", fontsize=11, width=1.6];
  fin [label="Fin del ciclo", style="rounded,filled", fillcolor="#0f172a", fontcolor="#ffffff", color="#0f172a", width=1.4];
  it [label="Iterar: volver a la\nFase 1 o a la Fase 2", style="rounded,filled,dashed", fillcolor="#fff1f2", color="#be123c", fontcolor="#9f1239", width=1.7];
  c1 -> c2 -> d2;
  d2 -> fin [label=" sí"];
  d2 -> it [label=" no", color="#be123c", fontcolor="#be123c"];
  { rank=same; fin; it; }
}
{ rank=same; a1; b0; c1; }
a1 -> b0 -> c1 [style=invis];
d1 -> b0 [label=" sí", constraint=false];
d1 -> b1 [label=" no: una ruta", constraint=false];
b3 -> c1 [constraint=false];
```
*Basado en la Figura 4.3 y las Tablas 5.7, 5.9 y 5.10 de Sandoval Medina (2026).*
:::

## 1.1 Anatomía de cada cuadernillo

Todos los temas tienen la misma estructura, para que estudiantes e instructor sepan siempre dónde encontrar cada cosa (esto reduce la carga extrínseca de «orientarse» en el material):

| Sección del PDF | Elemento del modelo CLT4BP | Contenido | Quién la usa |
|---|---|---|---|
| **Portada** | Mapa de ruta | Número, título, lema, rutas A/B y fuentes del tema. | Todos |
| **0. Ficha de diseño instruccional** | Fases 1, 2 y 3 | Objetivos por ruta (cf. Tabla 5.14), métodos de evaluación, efectos de la TCC por componente (cf. Tablas 5.6 y 5.15), matriz Tomlinson × 4C/ID (Tabla 5.8) y plan de implementación (Tabla 5.10). | Instructor |
| **1. Información de soporte** | Componente 4C/ID | Analogía, pregunta para pensar, relevancia (ARCS), conceptos uno por uno, actividad de movimiento humano, ejemplo resuelto y mapa del tema. | Estudiantes (antes de las tareas) |
| **2. Información procedimental** | Componente 4C/ID | Tarjetas de sintaxis, guía de preguntas de rutina, errores frecuentes y ejemplos isomórficos. | Estudiantes (durante las tareas) |
| **3. Tareas de aprendizaje** | Componente 4C/ID | 8 o 9 tareas con desvanecimiento de guía, marcadas por ruta. | Estudiantes |
| **4. Protocolo verbal** | Información procedimental | Guion segmentado de un experto (CÓMO y POR QUÉ) para grabar o leer en voz alta. | Instructor → estudiantes |
| **5. Evaluación** | Fase 3 | Recall test, comprehension test y autorregistro con escala de esfuerzo mental. | Instructor / estudiantes |
| **Glosario y Anexo** | — | Términos español–inglés (para leer el *C++ Crash Course*) y soluciones de tareas y evaluación. | Todos |

## 1.2 Convenciones visuales

<div class="leyenda">
<div style="--c:var(--sop)"><b>Azul · Información de soporte</b>Modelos mentales y conceptos; se presenta antes de las tareas y queda disponible.</div>
<div style="--c:var(--pro)"><b>Violeta · Información procedimental</b>Reglas «cómo se hace», consultadas justo a tiempo.</div>
<div style="--c:var(--tar)"><b>Verde · Tareas de aprendizaje</b>De menor a mayor complejidad, con ayuda que se desvanece.</div>
<div style="--c:var(--pv)"><b>Naranja · Protocolo verbal</b>Razonamiento experto en voz alta, en segmentos.</div>
<div style="--c:var(--ev)"><b>Rosa · Evaluación</b>Recall test, comprehension test y autorregistro.</div>
<div style="--c:var(--fi)"><b>Gris · Ficha del instructor</b>Decisiones de diseño de las Fases 1–3.</div>
</div>

- **Rutas.** {{A}} tareas para estudiantes **sin** conocimientos previos del tema; {{B}} para estudiantes **con** conocimientos previos; {{AB}} para ambos.
- **Efectos de la TCC** (clasificación de la Tabla 4.2 de la tesis): <span class="ef ef-n">Ejemplo resuelto</span> naranja = efecto para **nuevos conocimientos**; <span class="ef ef-r">Autoexplicación</span> violeta = efecto para **reforzar conocimientos previos**; <span class="ef ef-x">Movimiento humano</span> gris = aplicable a **ambos** (movimiento humano y autogestión). Cada recuadro y cada tarea indica los efectos que aplica.
- **ARCS.** La etiqueta {{arcs:Relevancia}} señala dónde se trabaja explícitamente una categoría motivacional de Keller.
- **Protocolos.** Las etiquetas {{como}} y {{porque}} separan el procedimiento de su justificación.

Así se ven los recuadros de código. Todo programa con salida fue **compilado y ejecutado** con g++ al generar el material, de modo que las salidas y los mensajes de error que aparecen son reales:

<div class="cols">
<div>

```cpp run stdin="7" title="ejemplo.cpp"
#include <iostream>
using namespace std;
int main()
{
    int n;
    cout << "Numero: ";       //> Anotación al margen
    cin >> n;
    cout << "Cuadrado: " << n * n << "\n";
    return 0;
}
```
*En la consola, el texto resaltado es lo que teclea el usuario.*

</div>
<div>

```cpp blank title="por_completar.cpp"
int doble(int x)
{
    return __1__;   // 1: completa
}
```
*Problema por completar: los huecos numerados se resuelven en el Anexo.*

```cpp err
int main()
{
    int total = 5;
    return totl;
}
```
*Mensaje real del compilador (abreviado).*

</div>
</div>

## 1.3 Fuentes y alcance

:::nota | Sobre los libros base
- **Betancourt y Polanco (2021)** organiza el temario (capítulos 1 a 13: estructura del lenguaje, secuenciales, selectivas, repetitivas, arreglos, matrices, funciones, recursividad, cadenas, estructuras, archivos y POO). El archivo disponible para este trabajo contenía el **índice y los capítulos 1 y 2**; de los capítulos 3 a 13 se tomó la **estructura temática del índice** (las secciones se citan en cada cuadernillo) y los ejemplos y ejercicios de esos temas son **originales**, alineados con ella.
- **Lospinoso (2019)** aporta el enfoque moderno de C++ (inicialización con llaves, `enum class`, referencias, `nullptr`, ciclo de vida de los objetos, *streams*). Se tomaron solo sus capítulos de **programación básica**; quedan fuera los temas avanzados (herencia, plantillas, excepciones, biblioteca estándar en profundidad, concurrencia).
- **La tesis** aporta el modelo y numerosos ejemplos que se reutilizan: la analogía de las casas y direcciones (punteros), la estructura `Empleado`/`Fecha` (estructuras anidadas), la secuencia de desvanecimiento de guía para ciclos, la solución libre de ordenamiento, el cuadrado mágico colaborativo y el manejo de archivos del segundo piloto.
:::

:::tip | Entorno técnico recomendado
Cualquier compilador moderno de C++ (g++, clang o MSVC) con un IDE que tenga **depurador** (Code::Blocks, Visual Studio Code, Dev-C++, CLion u otro), porque varias tareas piden observar variables paso a paso. Los programas se verificaron con `g++ -std=c++20 -Wall -Wextra`.
:::

# 2. Mapa de temas y prerrequisitos {.guia}

```dot w="100%"
rankdir=TB; nodesep=0.25; ranksep=0.42; newrank=true;
node [width=1.55, fontsize=11.5];
subgraph cluster_b1 { label="Bloque I · Fundamentos"; fontname="Inter Display"; fontsize=11; color="#93c5fd"; style="rounded"; fontcolor="#1d4ed8";
  t01 [label="01 Estructura\ny compilación"]; t02 [label="02 Tipos,\nvariables y E/S"]; t03 [label="03 Operadores\ny secuencia"]; t04 [label="04 if, if-else\ny anidados"]; t05 [label="05 switch\ny menús"]; }
subgraph cluster_b2 { label="Bloque II · Repetición y arreglos"; fontname="Inter Display"; fontsize=11; color="#6ee7b7"; style="rounded"; fontcolor="#047857";
  node [fillcolor="#ecfdf5", color="#059669"];
  t06 [label="06 while, do-while\ny for"]; t07 [label="07 Ciclos anidados,\nbreak y continue"]; t08 [label="08 Arreglos\n(vectores)"]; t09 [label="09 Matrices"]; }
subgraph cluster_b3 { label="Bloque III · Modularidad y datos"; fontname="Inter Display"; fontsize=11; color="#c4b5fd"; style="rounded"; fontcolor="#6d28d9";
  node [fillcolor="#f5f3ff", color="#7c3aed"];
  t10 [label="10 Funciones"]; t11 [label="11 Recursividad"]; t12 [label="12 Cadenas"]; t13 [label="13 Estructuras\ny enumeraciones"]; }
subgraph cluster_b4 { label="Bloque IV · Memoria, archivos y objetos"; fontname="Inter Display"; fontsize=11; color="#fdba74"; style="rounded"; fontcolor="#c2410c";
  node [fillcolor="#fff7ed", color="#c2410c"];
  t14 [label="14 Punteros\ny referencias"]; t15 [label="15 Memoria\ndinámica"]; t16 [label="16 Archivos\nde texto"]; t17 [label="17 Clases\ny objetos"]; }
{ rank=same; t01; t02; t03; t04; t05; }
{ rank=same; t06; t07; t08; t09; }
{ rank=same; t10; t11; t12; t13; }
{ rank=same; t14; t15; t16; t17; }
t01 -> t06 -> t10 -> t14 [style=invis, weight=20];
t02 -> t07 -> t11 -> t15 [style=invis, weight=20];
t03 -> t08 -> t12 -> t16 [style=invis, weight=20];
t04 -> t09 -> t13 -> t17 [style=invis, weight=20];
t01 -> t02 -> t03 -> t04 -> t05;
t06 -> t07 -> t08 -> t09;
t10 -> t11 [constraint=false]; t10 -> t12 [constraint=false]; t12 -> t13;
t14 -> t15; t13 -> t14 [constraint=false]; t13 -> t16 [constraint=false]; t14 -> t17 [constraint=false];
t04 -> t06 [constraint=false]; t08 -> t10 [constraint=false];
```
*Cada flecha indica un prerrequisito directo; la ficha de cada tema detalla todos sus conocimientos previos. Los temas 11 (recursividad) y 16 (archivos) pueden moverse dentro de su bloque sin romper la secuencia.*

## 2.1 Formato de objetivos de aprendizaje (Tabla 5.1, completado para el curso)

| Tema | Objetivo de aprendizaje general | Temas a completar | Duración | Fuentes adicionales de consulta |
|---|---|---|---|---|
| **01** | Escribir, compilar y ejecutar un programa en C++ y explicar su estructura. | `main`, `#include`, `cout`, comentarios, compilación y tipos de error. | 4 h | Betancourt y Polanco, cap. 1 · Lospinoso, cap. 1 |
| **02** | Declarar variables y constantes de tipos fundamentales y realizar entrada/salida. | Tipos, identificadores, `const`, `cin`, `getline`, formato de salida. | 4 h | B&P, cap. 1 · L, caps. 1–2 |
| **03** | Construir expresiones y resolver problemas con estructura secuencial. | Operadores, precedencia, conversiones, `<cmath>`, secuencia E–P–S. | 4 h | B&P, caps. 1–2 · L, cap. 7 |
| **04** | Resolver problemas de decisión con `if`, `if-else` y decisiones anidadas. | Condiciones simples y compuestas, escaleras `else if`, validación. | 4 h | B&P, cap. 3 · L, caps. 1, 7, 8 |
| **05** | Resolver selección múltiple con `switch` y construir menús. | `case`, `break`, `default`, caída de casos, `enum class`. | 3 h | B&P, cap. 4 · L, caps. 2, 8 |
| **06** | Resolver problemas repetitivos con `while`, `do-while` y `for`. | Contadores, acumuladores, centinelas, validación con ciclos. | 6 h | B&P, cap. 5 · L, caps. 2, 8 |
| **07** | Resolver problemas con ciclos anidados y control de flujo. | Patrones, tablas, `break`, `continue`, banderas. | 4 h | B&P, cap. 5 · L, cap. 8 |
| **08** | Almacenar y procesar colecciones con arreglos unidimensionales. | Declaración, recorrido, búsqueda, máximos, ordenamiento. | 6 h | B&P, cap. 6 · L, caps. 2, 13 |
| **09** | Procesar datos tabulares con matrices. | Recorridos por filas y columnas, diagonales, operaciones. | 5 h | B&P, cap. 7 · L, cap. 2 |
| **10** | Descomponer problemas en funciones reutilizables. | Parámetros por valor y referencia, retorno, ámbito, sobrecarga. | 6 h | B&P, cap. 8 · L, caps. 1, 3, 4, 9 |
| **11** | Resolver problemas con funciones recursivas. | Caso base, caso recursivo, pila de llamadas, recursión vs. iteración. | 4 h | B&P, cap. 9 · L, cap. 4 |
| **12** | Manipular texto con arreglos de `char` y `std::string`. | Lectura, recorrido, búsqueda, comparación, conversión. | 5 h | B&P, cap. 10 · L, caps. 2, 15 |
| **13** | Modelar registros con estructuras y enumeraciones. | `struct`, anidamiento, arreglos de estructuras, `enum class`. | 5 h | B&P, cap. 11 · L, caps. 2, 8 |
| **14** | Usar punteros y referencias para acceder a datos de forma indirecta. | `&`, `*`, `->`, aritmética de punteros, paso por puntero. | 6 h | B&P, caps. 1, 8 · L, cap. 3 |
| **15** | Gestionar memoria dinámica de forma segura. | `new`/`delete`, arreglos dinámicos, fugas, punteros colgantes. | 5 h | L, caps. 3–4 · tesis, §5.4 |
| **16** | Hacer persistentes los datos con archivos de texto. | `ifstream`, `ofstream`, modos, lectura por línea, actualización. | 5 h | B&P, cap. 12 · L, cap. 16 |
| **17** | Modelar entidades con clases y objetos. | Atributos, métodos, encapsulamiento, constructores, destructor. | 6 h | B&P, cap. 13 · L, caps. 2–4 |

*B&P = Betancourt y Polanco (2021); L = Lospinoso (2019). Total: 82 h de instrucción.*

# 3. Fase 1 · Análisis {.guia}

## 3.1 Objetivos y métodos de evaluación

Los objetivos de cada tema están redactados **por ruta** en la ficha del cuadernillo (sección 0.1), siguiendo la matriz de objetivos y métodos de evaluación por nivel del estudio piloto (Tabla 5.14). Los instrumentos del modelo son:

| Instrumento | Mide | Cuándo | Formato | Dónde |
|---|---|---|---|---|
| **Recall test** | Conocimiento declarativo (conceptos, sintaxis, definiciones). | Inicio del tema (diagnóstico) y final (desempeño). | 10 reactivos breves. | Sección 5.1 de cada tema |
| **Comprehension test** | Conocimiento procedimental y transferencia (predecir, corregir, desarrollar). | Final del tema. | 3–4 problemas. | Sección 5.2 de cada tema |
| **MSLQ** (Pintrich et al., 1991) | Motivación (31 ítems) y estrategias de aprendizaje (50 ítems). | Inicio y final del curso. | Likert 1–7. | Anexo A.1 de la tesis |
| **CIS** (Keller, 2010) | Percepción de **cómo enseña el instructor** (ARCS). | Final del curso o de la unidad. | 34 ítems, Likert 1–5. | Anexo A.4 |
| **IMMS** (Keller, 2010) | Reacción motivacional al **material** (ARCS). | Final del curso o de la unidad. | 36 ítems, Likert 1–5. | Anexo A.5 |
| **Encuesta de carga cognitiva** (Morrison et al., 2014) | Carga intrínseca (ítems 1–3), extrínseca (4–6) y pertinente (7–10). | Al cerrar cada bloque de temas. | 10 ítems, escala 0–10. | Anexo A.7 |
| **Autorregistro** (escala de Paas, 1992) | Esfuerzo mental percibido por tema. | Final de cada tema. | Escala 1–9. | Sección 5.3 de cada tema |

## 3.2 Entorno grupal

:::checklist | Guía de preguntas de rutina 3.2 · Diagnóstico del grupo
<ul class="checks">
<li><b>Motivación.</b> Aplica la sección de motivación del MSLQ en la primera sesión. Explica para qué sirve y promete retroalimentación individual: así se fomentan el interés y la honestidad en las respuestas. Registra los resultados en la Tabla 5.3.</li>
<li><b>Estrategias cognitivas y metacognitivas.</b> Aplica la sección de estrategias del MSLQ y registra cada subescala en la Tabla 5.4. Si casi nadie usa estrategias metacognitivas (como ocurrió en el piloto, Tabla 5.13), da peso al autorregistro y a las tareas de autoexplicación.</li>
<li><b>Conocimientos previos.</b> Aplica la prueba diagnóstica (sección 3.3) y, al iniciar cada bloque, el recall test del primer tema del bloque. Clasifica a cada estudiante en «con previos» (Ruta B) o «sin previos» (Ruta A).</li>
<li><b>Resumen.</b> Concentra todo en la Tabla 5.5 y redacta un diagnóstico de cuatro renglones como el de la Tabla 5.13 (motivación, estrategias cognitivas, metacognitivas y previos).</li>
<li><b>Decisión de rutas.</b> Si el grupo es heterogéneo en conocimientos previos, usa las dos rutas; si es homogéneo, sigue una sola ruta (la que corresponda) comenzando directamente por las tareas de aprendizaje. Aun con un grupo homogéneo, puedes diferenciar si lo consideras útil: el proceso no se afecta.</li>
</ul>
:::

:::cuidado | Criterio sugerido para asignar rutas
La tesis plantea solo dos caminos (sí/no). Como criterio inicial, ajustable por el instructor: **Ruta B** si el estudiante obtiene **70 o más** sobre 100 en el diagnóstico; **Ruta A** en otro caso. Considera al grupo **heterogéneo** cuando ambos perfiles reúnen al menos una quinta parte del grupo, o cuando una prueba estadística muestra diferencias significativas entre ellos. La asignación **no es permanente**: se revisa al inicio de cada bloque, porque un estudiante puede pasar de A a B (efecto de reversión de la experiencia).
:::

## 3.3 Prueba diagnóstica de entrada (Bloques I y II)

:::recall | Parte 1 · Recall (4 puntos cada reactivo · 40 puntos)
1. ¿Cuál es la función por la que empieza a ejecutarse todo programa en C++?
2. ¿Qué tipo de dato usarías para guardar el precio 3.75? ¿Y para guardar una letra?
3. ¿Qué hace la instrucción `cin >> edad;`?
4. ¿Cuánto vale la expresión `17 % 5`? ¿Y `7 / 2` si ambos son enteros?
5. ¿Qué diferencia hay entre `=` y `==`?
6. ¿Cuántas veces se repite el cuerpo de `for (int i = 0; i < 4; i++)`?
7. ¿Qué diferencia hay entre `while` y `do-while`?
8. En el arreglo `int a[5];`, ¿cuál es el índice del primer elemento? ¿Y del último?
9. ¿Qué significa que una función sea `void`?
10. Verdadero o falso: dentro de un `switch`, si se omite `break`, la ejecución continúa con el siguiente `case`.
:::

:::compr | Parte 2 · Comprehension (15 puntos cada problema · 60 puntos)
**P1. Predice la salida.**

```cpp check title="diag_p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int suma = 0;
    for (int i = 1; i <= 6; i++)
    {
        if (i % 2 == 0)
            suma += i;
        else
            cout << i << " ";
    }
    cout << "| " << suma << "\n";
    return 0;
}
```

**P2. Encuentra y corrige los errores** (hay tres):

```cpp blank title="diag_p2.cpp"
#include <iostream>
using namespace std;
int main()
{
    int calif
    cout << "Calificacion: ";
    cin >> calif;
    if (calif = 10)
        cout << "Excelente\n";
    else if (calif >= 6)
        cout << "Aprobado\n"
    else
        cout << "Reprobado\n";
    return 0;
}
```

**P3. Desarrolla** un programa que lea 5 números enteros y muestre el mayor y el promedio.

**P4. Rastrea** el arreglo: ¿qué contiene `v` al terminar?

```cpp check title="diag_p4.cpp"
#include <iostream>
using namespace std;
int main()
{
    int v[5] = {4, 1, 3, 5, 2};
    for (int i = 0; i < 4; i++)
        if (v[i] > v[i + 1])
        {
            int t = v[i];
            v[i] = v[i + 1];
            v[i + 1] = t;
        }
    for (int x : v) cout << x << " ";
    cout << "\n";
    return 0;
}
```
:::

:::solucion | Prueba diagnóstica · Parte 1
1 `main` · 2 `double` (o `float`); `char` · 3 Lee un valor del teclado y lo guarda en la variable `edad` · 4 `2`; `3` (división entera) · 5 `=` asigna un valor; `==` compara si dos valores son iguales · 6 4 veces (i = 0, 1, 2, 3) · 7 `while` evalúa la condición antes de entrar (puede no ejecutarse nunca); `do-while` la evalúa al final (se ejecuta al menos una vez) · 8 `0`; `4` · 9 Que no devuelve ningún valor · 10 Verdadero.
:::

:::solucion | Prueba diagnóstica · Parte 2
**P1.** Imprime los impares y acumula los pares (2 + 4 + 6 = 12):

```cpp run title="diag_p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int suma = 0;
    for (int i = 1; i <= 6; i++)
    {
        if (i % 2 == 0)
            suma += i;
        else
            cout << i << " ";
    }
    cout << "| " << suma << "\n";
    return 0;
}
```

**P2.** (1) Falta `;` en `int calif;`. (2) `if (calif = 10)` asigna en vez de comparar: `if (calif == 10)`. (3) Falta `;` después de `"Aprobado\n"`.

**P3.** Una solución:

```cpp run stdin="8\n15\n3\n12\n7" title="diag_p3.cpp"
#include <iostream>
using namespace std;
int main()
{
    int n, mayor = 0, suma = 0;
    for (int i = 1; i <= 5; i++)
    {
        cout << "Numero " << i << ": ";
        cin >> n;
        if (i == 1 || n > mayor) mayor = n;
        suma += n;
    }
    cout << "Mayor: " << mayor << "\nPromedio: " << suma / 5.0 << "\n";
    return 0;
}
```
*Criterio:* lectura en ciclo (4 pts), mayor correcto incluso con negativos (4), acumulador (3), promedio con división real (4).

**P4.** Es una pasada del método de la burbuja: el mayor (5) «sube» al final.

```cpp run title="diag_p4.cpp"
#include <iostream>
using namespace std;
int main()
{
    int v[5] = {4, 1, 3, 5, 2};
    for (int i = 0; i < 4; i++)
        if (v[i] > v[i + 1])
        {
            int t = v[i];
            v[i] = v[i + 1];
            v[i + 1] = t;
        }
    for (int x : v) cout << x << " ";
    cout << "\n";
    return 0;
}
```
**Uso del resultado:** quien domina las partes que corresponden a un bloque (reactivos 1–5 y P1–P2 para el Bloque I; 6–10 y P3–P4 para el Bloque II) puede seguir la Ruta B en ese bloque.
:::

## 3.4 Preselección de efectos por tema (Tabla 5.6, completada)

La ficha de cada tema (sección 0.3) detalla **cómo** se aplica cada efecto. Este es el resumen del curso:

| Tema | Efectos a aplicar (además de los comunes) | Herramientas / estrategias de aplicación |
|---|---|---|
| **Todos** | <span class="ef ef-n">Ejemplo resuelto</span> <span class="ef ef-n">Problema por completar</span> <span class="ef ef-n">Elementos aislados</span> <span class="ef ef-n">Atención dividida</span> <span class="ef ef-n">Variabilidad</span> <span class="ef ef-r">Autoexplicación</span> <span class="ef ef-r">Imaginación</span> <span class="ef ef-r">Solución libre</span> <span class="ef ef-r">Memoria colectiva de trabajo</span> <span class="ef ef-r">Desvanecimiento de guía</span> | Código anotado al margen, diagramas integrados con el código, tareas T1–T8 con desvanecimiento, reto colaborativo final. |
| **01** | <span class="ef ef-n">Modalidad</span> <span class="ef ef-n">Redundancia</span> <span class="ef ef-x">Autogestión</span> <span class="ef ef-x">Movimiento humano</span> | Diagrama de compilación con guion narrado; tarjeta de sintaxis sin repetir teoría; «La hoja viaja por el salón»; T9: rediseñar una explicación mal diseñada. |
| **02** | <span class="ef ef-n">Redundancia</span> <span class="ef ef-x">Movimiento humano</span> | Tarjeta de sintaxis que resume sin repetir; «Casilleros humanos». |
| **03** | <span class="ef ef-x">Movimiento humano</span> | «Árbol de expresión humano» para la precedencia de operadores. |
| **04** | <span class="ef ef-x">Movimiento humano</span> | «Diagrama de flujo en el piso». |
| **05** | <span class="ef ef-x">Movimiento humano</span> | «El switch humano». |
| **06** | <span class="ef ef-x">Autogestión</span> <span class="ef ef-x">Movimiento humano</span> | Secuencia de desvanecimiento de la tesis (pares → factorial → Fibonacci → tabla); «Vueltas a la pista»; T9: rediseñar una explicación de `for`. |
| **07** | <span class="ef ef-n">Interactividad de elementos</span> <span class="ef ef-x">Movimiento humano</span> | Plantilla «una fila = un ciclo interno + salto de línea»; «El reloj humano». |
| **08** | <span class="ef ef-x">Autogestión</span> <span class="ef ef-x">Movimiento humano</span> | «Burbuja humana»; T9: rediseñar el material de la burbuja (tesis, §6.1.17). |
| **09** | <span class="ef ef-n">Interactividad de elementos</span> <span class="ef ef-x">Movimiento humano</span> | Plantillas separadas para filas, columnas y diagonales; «Matriz humana». |
| **10** | <span class="ef ef-x">Movimiento humano</span> | «La llamada telefónica» (pila de llamadas). |
| **11** | <span class="ef ef-x">Movimiento humano</span> | «¿Cuántos hay detrás de ti?» (llamadas recursivas). |
| **12** | <span class="ef ef-x">Movimiento humano</span> | «La cadena humana». |
| **13** | <span class="ef ef-x">Movimiento humano</span> | «Fichas humanas» (estructuras anidadas). |
| **14** | <span class="ef ef-n">Modalidad</span> <span class="ef ef-x">Autogestión</span> <span class="ef ef-x">Movimiento humano</span> | Analogía de casas y direcciones; diagramas de memoria con guion narrado; «Notas y casas»; cada estudiante dibuja su propio diagrama de memoria. |
| **15** | <span class="ef ef-n">Modalidad</span> | Guion narrado sobre los diagramas de pila y montón. |
| **16** | — | Contenido de cada archivo mostrado junto al programa que lo lee o escribe (atención dividida). |
| **17** | <span class="ef ef-x">Movimiento humano</span> | «Objetos humanos» con atributos privados. |

*Efectos que se aplican en el diseño y no como actividad: <span class="ef ef-n">Información transitoria</span> (los protocolos verbales se entregan también por escrito y en segmentos breves) y <span class="ef ef-r">Reversión de la experiencia</span> (la Ruta B omite ejemplos resueltos y problemas por completar).*

# 4. Fase 2 · Diseño y desarrollo {.guia}

## 4.1 Cómo se construyó cada componente

| Componente 4C/ID | Recomendaciones del marco de trabajo (Tabla 5.9) | Cómo aparecen en los cuadernillos |
|---|---|---|
| **Tareas de aprendizaje** | Dificultad creciente, escenarios auténticos, establecer el POR QUÉ y el PARA QUÉ; ARCS y estrategias diferenciadas. | Cada tarea abre con un **contexto** realista (tienda, cine, laboratorio, videojuego). La secuencia típica se muestra abajo. |
| **Información de soporte** | Seleccionar la información relevante, elegir herramientas de entrega, contenido accesible; ARCS, DI y efectos de la TCC. | Analogía + pregunta para pensar (atención) + relevancia; conceptos **uno por uno** con código y diagrama integrados; ejemplo resuelto en pasos (análisis → algoritmo → código → verificación). |
| **Información procedimental** | Ejemplos isomórficos, guías de preguntas de rutina, mapas y tablas de sintaxis; protocolos verbales del instructor o de un desarrollador profesional (CÓMO y POR QUÉ, en video o audio). | Tarjetas de sintaxis, listas de verificación, errores frecuentes con el mensaje real del compilador y un ejemplo isomórfico; protocolo verbal segmentado en la sección 4. |

```dot w="100%"
rankdir=LR; nodesep=0.12; ranksep=0.22;
node [fontsize=10.5, width=1.0, margin="0.08,0.05", fillcolor="#ecfdf5", color="#059669"];
t1 [label="T1\nEjemplo resuelto\n+ gemelo", fillcolor="#d1fae5"];
t2 [label="T2\nPor completar\ncon pistas"];
t3 [label="T3\nPor completar\nsin pistas"];
t4 [label="T4\nProblema\nconvencional"];
t5 [label="T5\nSolución\nlibre"];
t6 [label="T6\nAutoexplicación\n(código con errores)"];
t7 [label="T7\nImaginación\n(sin ejecutar)"];
t8 [label="T8\nReto\ncolaborativo", fillcolor="#a7f3d0"];
t1 -> t2 -> t3 -> t4 -> t5 -> t6 -> t7 -> t8;
```
*Secuencia típica de tareas: la guía se desvanece de izquierda a derecha. La Ruta A recorre T1 → T4 con apoyo del instructor; la Ruta B inicia en T3 o T4 y trabaja T5–T7 de forma autónoma; ambas se reúnen en T8 con equipos de niveles mezclados.*

## 4.2 Motivación: el modelo ARCS en el material

| Categoría | Subcomponente (Tablas 5.11 y 5.12) | Dónde se aplica en los cuadernillos |
|---|---|---|
| **Atención** | Entusiasmo perceptivo; por indagación; variabilidad. | Analogía inicial y recuadro «Pregunta para pensar»; diagramas; contextos variados en cada tarea. |
| **Relevancia** | Orientación a objetivos; concordancia de motivos; familiaridad. | Recuadro «¿Por qué y para qué?» con usos reales (videojuegos, bancos, sensores); problemas de la vida cotidiana. |
| **Confianza** | Requisitos de aprendizaje; oportunidades de éxito; control personal. | Objetivos explícitos por ruta; ejemplos resueltos y problemas por completar antes de la práctica autónoma; soluciones en el anexo. |
| **Satisfacción** | Refuerzo intrínseco; recompensa extrínseca; equidad. | Programas que funcionan y se prueban con valores extremos; autorregistro; mensajes del compilador explicados como oportunidad de mejora. |

## 4.3 Instrucción diferenciada (Tabla 5.8)

Cada ficha incluye su **matriz Tomlinson × 4C/ID** ya completada. El criterio general del curso:

| Elemento | Ruta A · sin conocimientos previos | Ruta B · con conocimientos previos |
|---|---|---|
| **Contenido** | Conceptos esenciales, uno por uno. | Conceptos esenciales más extensiones marcadas «Ruta B» (buenas prácticas, casos límite, C++ moderno). |
| **Proceso** | Ejemplos resueltos → problemas por completar → problema convencional, con el instructor cerca. | Autoexplicación, imaginación y solución libre de forma autónoma; papel de «arquitecto» en el reto colaborativo. |
| **Producto** | Un programa funcional y bien probado del contexto de la tarea T4. | Un programa más abierto o integrador (T5 o T8). |
| **Entorno** | Tarjetas de sintaxis impresas, depurador paso a paso, trabajo en parejas. | Proyecto en el IDE, consulta del *C++ Crash Course* en inglés, trabajo individual y luego en equipo. |

## 4.4 Protocolos verbales: cómo grabarlos

:::checklist | Guía de preguntas de rutina 4.4 · Grabar un protocolo verbal
<ul class="checks">
<li>Usa el guion de la sección 4 del tema: resuelve un problema <b>isomórfico</b> a las tareas, no una de ellas.</li>
<li>Graba un segmento por paso (de 30 a 60 s cada uno): así se evita la <b>información transitoria</b> y el estudiante puede volver a cada segmento.</li>
<li>Di siempre el <b>CÓMO</b> y el <b>POR QUÉ</b>; incluye un error típico y cómo lo detectas.</li>
<li>Muestra en pantalla solo lo que narras (modalidad): código y diagrama, sin repetir en texto lo que dices (redundancia).</li>
<li>Si lo graba un desarrollador profesional, pídele que se centre en el proceso y el razonamiento, no en el resultado.</li>
<li>Entrega el guion escrito junto con el video o audio.</li>
</ul>
:::

# 5. Fase 3 · Aplicación y evaluación {.guia}

## 5.1 Plan de implementación de una sesión típica

| Momento | Componente | Qué hace el instructor | Ruta A | Ruta B |
|---|---|---|---|---|
| **Apertura** (10 min) | Soporte | Presenta un ejemplo real y la «Pregunta para pensar» (¿cómo crees que funciona?). | Todo el grupo | Todo el grupo |
| **Soporte** (30–40 min) | Soporte | Conceptos uno por uno, actividad de movimiento humano, ejemplo resuelto. El material queda disponible todo el tema. | Atiende todo | Puede saltar a conceptos «Ruta B» |
| **Tareas** (50–60 min) | Tareas + procedimental | Acompaña a la Ruta A y retira la ayuda gradualmente; la información procedimental se usa «justo a tiempo». | T1 → T4 | T3/T4 → T5–T7 |
| **Protocolo verbal** | Procedimental | Se reproduce antes del primer problema convencional (T4) o cuando varios estudiantes se atascan. | Sí | Opcional |
| **Cierre** (10 min) | Evaluación | Autorregistro con escala de esfuerzo mental; dudas para la siguiente sesión. | Sí | Sí |

## 5.2 Cronograma sugerido (16 semanas · 6 h por semana)

| Semana | Temas | Instrumentos de evaluación |
|---|---|---|
| **1** | Fase 1 (2 h) · 01 Estructura y compilación | MSLQ inicial, prueba diagnóstica, recall de 01 como diagnóstico |
| **2–4** | 02 Tipos y E/S · 03 Operadores · 04 if · 05 switch | Recall y comprehension de cada tema · encuesta de carga cognitiva (fin del Bloque I) |
| **4–8** | 06 Ciclos · 07 Ciclos anidados · 08 Arreglos · 09 Matrices | Diagnóstico del Bloque II · tests por tema · carga cognitiva (fin del Bloque II) |
| **8–11** | 10 Funciones · 11 Recursividad · 12 Cadenas · 13 Estructuras | Diagnóstico del Bloque III · tests por tema · carga cognitiva (fin del Bloque III) |
| **11–15** | 14 Punteros · 15 Memoria dinámica · 16 Archivos · 17 Clases | Diagnóstico del Bloque IV · tests por tema · carga cognitiva (fin del Bloque IV) |
| **16** | Cierre y revisión de resultados | CIS, IMMS, MSLQ final · decisión de iterar (sección 5.4) |

*Con otra carga horaria, conserva el orden de los bloques y la proporción de tiempo entre soporte (≈ 30 %) y tareas (≈ 60 %).*

## 5.3 Registro y análisis de resultados

- **Desempeño:** registra recall y comprehension de cada estudiante (Tabla 5.2) y compara con el diagnóstico (y, si existe, con un grupo de control) para identificar diferencias estadísticamente significativas.
- **Carga cognitiva:** promedia los ítems 1–3 (intrínseca), 4–6 (extrínseca) y 7–10 (pertinente) por bloque. Junto con el desempeño, permite estimar la **eficiencia mental** del material.
- **Motivación y percepción:** compara el MSLQ inicial y el final; analiza el CIS (enseñanza) y el IMMS (material) por categoría ARCS.

## 5.4 Revisión de resultados: ¿iterar?

Si se cumplen los objetivos, el ciclo termina. Si no, el modelo indica **regresar a la Fase 1 o 2** según los hallazgos:

| Si observas… | Regresa a… | Ajuste sugerido |
|---|---|---|
| Recall bajo, comprehension aceptable | Fase 2 · soporte | Reforzar conceptos con más ejemplos resueltos y glosario; repasar el mapa del tema. |
| Recall aceptable, comprehension baja | Fase 2 · tareas | Más problemas por completar y ejemplos isomórficos; desvanecer la guía más despacio. |
| Carga **extrínseca** alta (ítems 4–6) | Fase 2 · diseño | Revisar atención dividida, redundancia y claridad de instrucciones; segmentar los protocolos verbales. |
| Carga **intrínseca** alta (ítems 1–3) con bajo desempeño | Fase 2 · secuencia | Aplicar elementos aislados con más pasos intermedios; revisar prerrequisitos. |
| Carga **pertinente** baja (ítems 7–10) | Fase 2 · tareas | Más autoexplicación, imaginación y variabilidad (sobre todo para la Ruta B). |
| Ruta B aburrida o Ruta A frustrada | Fase 1 · rutas | Reasignar estudiantes; recalibrar el criterio de 70 puntos. |
| Motivación (MSLQ, IMMS) a la baja | Fase 2 · ARCS | Contextos más cercanos al grupo, retos con elección del tema, retroalimentación inmediata. |

# 6. Formatos para el instructor {.guia}

*Plantillas en blanco de la Fase 1 (Sandoval Medina, 2026, Tablas 5.1–5.6 y 5.8). Pueden fotocopiarse o reproducirse en una hoja de cálculo.*

**Tabla 5.2 · Registro de resultados de las pruebas finales de desempeño** (tema: ____________________)

{{plantilla:12:ID|Ruta|Recall test inicial · calificación|Recall test final · calificación|Comprehension test final · calificación|Esfuerzo mental (1–9)}}

**Tabla 5.3 · Registro de indicadores de motivación y autoeficacia** (MSLQ, escala 1–7)

{{plantilla:12:ID|Orientación intrínseca|Orientación extrínseca|Valor de la tarea|Autoeficacia|Ansiedad|Promedio}}

**Tabla 5.4 · Estrategias cognitivas, metacognitivas y manejo de recursos** (MSLQ, escala 1–7)

{{plantilla:12:ID|Cog. · Repetición|Cog. · Elaboración|Cog. · Organización|Metacog. · Control de la comprensión|Rec. · Gestión del tiempo y estudio|Rec. · Regulación del esfuerzo|Rec. · Búsqueda de ayuda|Rec. · Entorno de aprendizaje}}

**Tabla 5.5 · Resumen estadístico de variables de aprendizaje y motivación** (grupo: ____________)

{{plantilla:3:Dato|Motivación (promedio)|Previos: sí|Previos: no|Cognitivas (1–3)|Metacognitivas: sí|Metacognitivas: no|Recursos (1–4)}}

**Tabla 5.13 · Resumen de diagnóstico del entorno grupal**

{{plantilla:4:Dimensión de análisis (motivación · estrategias cognitivas · metacognitivas · conocimientos previos)|Resultados del grupo}}

**Tabla 5.8 · Matriz de planificación: instrucción diferenciada y modelo 4C/ID** (tema: ____________)

{{plantilla:4:Elemento (contenido · proceso · producto · entorno)|Tema(s)|Componente 4C/ID|Con previos (Ruta B)|Sin previos (Ruta A)}}

**Tabla 5.6 · Plan de aplicación de efectos de la carga cognitiva por tema** (para temas nuevos)

{{plantilla:5:Tema|Efecto(s) a aplicar|Herramientas / estrategias de aplicación}}

## Referencias de los instrumentos y del marco teórico

- Keller, J. M. (2010). *Motivational design for learning and performance: The ARCS model approach*. Springer. (CIS e IMMS.)
- Morrison, B. B., Dorn, B. y Guzdial, M. (2014). Measuring cognitive load in introductory CS: Adaptation of an instrument. En *Proceedings of the Tenth Annual Conference on International Computing Education Research (ICER '14)* (pp. 131–138). ACM.
- Paas, F. (1992). Training strategies for attaining transfer of problem-solving skill in statistics: A cognitive-load approach. *Journal of Educational Psychology, 84*(4), 429–434.
- Pintrich, P. R., Smith, D. A. F., García, T. y McKeachie, W. J. (1991). *A manual for the use of the Motivated Strategies for Learning Questionnaire (MSLQ)*. University of Michigan.
- Sweller, J., van Merriënboer, J. J. G. y Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*, 261–292.
- Tomlinson, C. A. (2017). *How to differentiate instruction in academically diverse classrooms* (3.ª ed.). ASCD.
- van Merriënboer, J. J. G. y Kirschner, P. A. (2018). *Ten steps to complex learning* (3.ª ed.). Routledge.
