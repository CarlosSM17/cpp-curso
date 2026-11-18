---
num: "01"
archivo: "Tema01_Estructura_programa_y_compilacion"
titulo: "Estructura de un programa en C y cadena de compilación"
corto: "Estructura y compilación"
lema: "Del texto que escribes al programa que se ejecuta: anatomía de un programa en C y el viaje que hace hasta convertirse en ejecutable."
duracion: "4 h · 2 sesiones de 2 h"
previos: "Ninguno (tema de entrada). Uso básico de la computadora y de un editor de texto."
fuentes:
  - "Kernighan, B. W. y Ritchie, D. M. (1988). *The C Programming Language* (2.ª ed.). Prentice Hall. Cap. 1 «A Tutorial Introduction»: §1.1 Getting Started."
  - "Seacord, R. C. (2020). *Effective C: An Introduction to Professional C Programming*. No Starch Press. Cap. 1 «Getting Started with C»: Developing Your First C Program, Compiling and Running Your Program."
  - "King, K. N. (2008). *C Programming: A Modern Approach* (2.ª ed.). W. W. Norton. Cap. 2 «C Fundamentals»: Writing a Simple Program, The General Form of a Simple Program, Comments."
objetivos:
  A:
    - "Identificar las partes de un programa básico en C: comentarios, directivas `#include`, función `main`, bloque `{ }`, sentencias y `return 0;`."
    - "Escribir, compilar y ejecutar programas que muestren texto en pantalla con `printf`, `\\n` y `\\t`."
    - "Describir con sus palabras las fases de edición, preprocesamiento, compilación, enlace y ejecución."
    - "Distinguir errores de compilación, de enlace, de ejecución y de lógica, y corregir los errores de sintaxis más comunes."
  B:
    - "Explicar qué recibe y qué produce cada fase de la cadena de compilación (`.c`, `.o/.obj`, `.exe`)."
    - "Interpretar mensajes de gcc con el formato `archivo:línea:columna` y corregir varios errores encadenados empezando por el primero."
    - "Explicar por qué un prototipo sin definición produce un error de **enlace** y no de compilación."
    - "Comparar la salida con formato mediante `printf` y la salida directa de cadenas con `puts`, ambas de `<stdio.h>`."
efectos:
  soporte:
    - ["Elementos aislados", "La anatomía del programa se presenta pieza por pieza (main → printf → \\n/\\t → comentarios → delimitadores) antes del programa completo."]
    - ["Atención dividida", "Código anotado línea por línea: la explicación está pegada a cada línea, no en un párrafo aparte."]
    - ["Ejemplo resuelto", "Tarjeta de bienvenida: algoritmo → pseudocódigo → C comentado → salida real."]
    - ["Modalidad", "El diagrama de la cadena de compilación se acompaña con el guion narrado del protocolo verbal (audio breve)."]
  procedimental:
    - ["Variabilidad", "Errores frecuentes mostrados en contextos distintos, con el mensaje real de gcc."]
    - ["Redundancia", "La tarjeta de sintaxis evita repetir teoría: solo plantillas y reglas mínimas para consultar."]
    - ["Autoexplicación", "Preguntas «¿por qué falla?» antes de mostrar cada corrección."]
  tareas:
    - ["Ejemplo resuelto", "T1: cartel resuelto + problema gemelo."]
    - ["Problema por completar", "T2 con pistas; T3 sin pistas y con más huecos."]
    - ["Desvanecimiento de guía", "Secuencia T1 → T2 → T3 → T4 (de resuelto a convencional)."]
    - ["Solución libre", "T5: dibujar una figura con todas las formas de salida en C que conozcas."]
    - ["Autoexplicación", "T6: encontrar, explicar y corregir errores en el programa de un compañero."]
    - ["Imaginación", "T7 (Ruta B): imaginar el viaje de un programa por la cadena antes de compilarlo."]
    - ["Memoria colectiva de trabajo", "T8: la cadena de compilación en vivo, por equipos heterogéneos."]
    - ["Movimiento humano", "T8: cada integrante representa una fase y «mueve» el programa físicamente."]
    - ["Autogestión", "T9: rediseñar una explicación mal diseñada aplicando los efectos de la TCC."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Conceptos aislados con ejemplos resueltos y código anotado; uso de compilador en línea para no instalar nada."
    B: "Lectura de la sección completa como repaso; foco en el error de enlace y la comparación `printf` vs `puts`."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 en orden, en pares con un estudiante de Ruta B como apoyo; el instructor retira la ayuda gradualmente."
    B: "T3, T6, T7 y T9 de forma autónoma; actúan como «copilotos» en la T8."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Programa «tarjeta de presentación» (T4) funcionando."
    B: "Un programa con tres errores sembrados (uno de cada tipo) para que otro equipo lo depure."
  Entorno:
    comp: "Información procedimental"
    A: "IDE o compilador en línea, con la tarjeta de sintaxis impresa a un lado."
    B: "Terminal con `gcc -Wall -Wextra`; lectura directa de mensajes del compilador."
plan:
  - ["Apertura", "Soporte", "Analogía de la receta y pregunta «¿cómo entiende la computadora tu texto?». Mostrar software o sistemas escritos en C (relevancia).", "10 min"]
  - ["Desarrollo", "Soporte + protocolo", "Conceptos 1 a 5 (uno a la vez), anatomía anotada, cadena de compilación narrada y ejemplo resuelto 1.5.", "60 min"]
  - ["Práctica guiada", "Tareas + procedimental", "Ruta A: T1 → T2 → T3. Ruta B: T3, T6, T7. Tarjeta de sintaxis a la vista.", "60 min"]
  - ["Práctica colaborativa", "Tareas", "T8 por equipos heterogéneos (4 integrantes).", "30 min"]
  - ["Autónoma y cierre", "Tareas + evaluación", "T4 (todos), T5 (A), T9 (B); recall test, comprehension test y autorregistro.", "80 min"]
glosario:
  - ["código fuente", "source code", "Texto del programa escrito en C (archivo `.c`)."]
  - ["compilador", "compiler", "Programa que traduce el código fuente a código objeto (lenguaje máquina)."]
  - ["preprocesador", "preprocessor", "Fase previa que procesa las directivas `#` (por ejemplo, copia el contenido de `<stdio.h>`)."]
  - ["enlazador", "linker", "Une los archivos objeto con las bibliotecas estándar y produce el ejecutable."]
  - ["archivo objeto", "object file", "Resultado de compilar un `.c` (`.o` en gcc, `.obj` en Visual Studio)."]
  - ["ejecutable", "executable", "Archivo que el sistema operativo puede ejecutar (`.exe` en Windows)."]
  - ["cadena de herramientas", "tool chain", "Conjunto preprocesador + compilador + enlazador."]
  - ["sentencia / instrucción", "statement", "Unidad de acción del programa; en C termina en `;`."]
  - ["directiva", "directive", "Instrucción para el preprocesador; empieza con `#`."]
  - ["archivo de cabecera", "header file", "Archivo con declaraciones de funciones listo para incluirse (p. ej., `<stdio.h>`)."]
  - ["salida estándar", "standard output", "`stdout`: canal por el que `printf` envía texto a la pantalla."]
  - ["literal de cadena", "string literal", "Texto entre comillas dobles, como `\"Hola\"`."]
  - ["secuencia de escape", "escape sequence", "Combinación con `\\` que representa un carácter especial: `\\n`, `\\t`."]
  - ["argumento", "argument", "Valor que se pasa entre paréntesis a una función, como `\"Hola\\n\"` en `printf(\"Hola\\n\")`."]
  - ["punto de entrada", "entry point", "Lugar donde inicia la ejecución: la función `main`."]
  - ["error de compilación", "compile-time error", "Error detectado al traducir (sintaxis, funciones no declaradas)."]
  - ["error de enlace", "link-time error", "Error detectado al unir piezas (función declarada pero no definida)."]
  - ["error en tiempo de ejecución", "runtime error", "Error que aparece cuando el programa ya se está ejecutando."]
  - ["depurador", "debugger", "Herramienta para ejecutar paso a paso e inspeccionar el programa (GDB, LLDB, Visual Studio)."]
---

# 1. Información de soporte {.soporte}

:::analogia | Un programa es una receta… para un cocinero muy literal
Imagina una receta de cocina. Primero dice **qué ingredientes necesitas**, después da **pasos en orden** y cada paso termina con un punto. El cocinero no improvisa: si la receta dice «agrega sal» pero nunca dijiste qué es la sal, se detiene.

Un programa en C funciona igual: las **bibliotecas** (archivos de cabecera) son los ingredientes, las **sentencias** son los pasos (cada una termina en `;`) y la computadora es el cocinero literal. Hay un detalle: el cocinero no lee español ni C, solo **lenguaje máquina** (ceros y unos). Por eso necesitamos un **traductor**: el compilador.
:::

:::pregunta
Antes de seguir, piensa 30 segundos: **¿cómo crees que la computadora «entiende» lo que escribes en C si solo maneja ceros y unos?** Anota tu idea; al final de la sección 1.5 la comparas con lo que realmente pasa.

{{lineas:2}}
:::

:::relevancia | ¿Por qué y para qué aprender esto?
C está detrás del núcleo de Linux y de buena parte de Windows y macOS, del intérprete de Python, de bases de datos como SQLite y PostgreSQL, de Git y del firmware de microcontroladores en lavadoras, automóviles y placas de robótica. Todos esos programas, por grandes que sean, tienen la misma estructura básica que vas a aprender hoy: **un `main`, sentencias en orden y una cadena de compilación que los convierte en ejecutables**. Además, C++, Java, C# y JavaScript tomaron su sintaxis de C, así que lo que aprendas aquí te servirá en casi cualquier lenguaje. Dominar esto te permite leer cualquier programa en C y entender los mensajes de error, que es la habilidad que más tiempo ahorra a un programador. {{arcs:Relevancia}}
:::

## 1.1 Las piezas, una por una

Un programa tiene varias piezas que interactúan. Para no saturar tu memoria de trabajo, las verás **aisladas**, una a la vez; al final las juntamos. {{ef:Elementos aislados}}

:::concepto | 1 | El programa más pequeño: la función `main` | Elementos aislados, Atención dividida
Todo programa en C empieza a ejecutarse en una función llamada **`main`**. Es el **punto de entrada**.

```c check
int main(void)     //> `int`: main devuelve un número entero al sistema operativo
{                  //> `{` abre el **bloque** de instrucciones de main
    return 0;      //> `return 0;` termina el programa e informa «todo salió bien»
}                  //> `}` cierra el bloque
```

Este programa compila y se ejecuta… pero no hace nada visible. Para «ver» algo necesitamos la siguiente pieza.
:::

:::concepto | 2 | Mostrar texto: `#include <stdio.h>` y `printf` | Elementos aislados, Atención dividida
Para escribir en pantalla usamos la función `printf` (*print formatted*), declarada en el archivo de cabecera estándar `<stdio.h>` (*standard input/output*). La línea `#include` le pide al preprocesador que copie esa cabecera dentro de tu programa.

```c run
#include <stdio.h>             //> Directiva: trae la biblioteca de entrada/salida estándar
int main(void)
{
    printf("Hola, mundo");     //> `printf` imprime en la pantalla el literal de cadena entre paréntesis
    return 0;                  //> Termina el programa e informa «todo salió bien»
}
```

- El texto entre comillas dobles (`"Hola, mundo"`) es un **literal de cadena**: se muestra tal cual.
- Los paréntesis `( )` en `printf(...)` encierran el **argumento** que le pasamos a la función para que lo imprima.
- En C estándar, `int main(void)` indica explícitamente que `main` no recibe argumentos (también verás `int main()`).
:::

:::concepto | 3 | Saltos de línea y tabuladores: `\n` y `\t` | Elementos aislados, Atención dividida
`printf` no cambia de renglón por sí solo. Para controlar el formato se usan **secuencias de escape**: una barra invertida `\` seguida de una letra dentro de las comillas.

```c run
#include <stdio.h>
int main(void)
{
    printf("Linea 1");             //> Sin salto: lo siguiente queda pegado
    printf(" (sigue)\n");          //> `\n` = salto de línea dentro del texto
    printf("Linea 2\n");
    printf("Nombre:\tAna\n");      //> `\t` = tabulador: alinea en columnas
    printf("Edad:\t17\n");
    return 0;
}
```

:::nota | ¿Por qué `printf` lleva una «f» al final?
La *f* viene de *formatted* (con formato). Además de imprimir texto fijo, en el Tema 02 usarás `printf` con **especificadores de formato** (como `%d` o `%f`) para mostrar números y variables. También existe `puts("Hola");`, que imprime una cadena y agrega automáticamente un salto de línea al final.
:::
:::

:::concepto | 4 | Comentarios: notas para humanos | Elementos aislados
El compilador **ignora** los comentarios; sirven para explicar el código a otras personas (¡y a ti en el futuro!).

```c run
#include <stdio.h>
/* Comentario de bloque:
   puede ocupar varias lineas.
   Autor: equipo 3, Programacion basica */
int main(void)
{
    printf("Los comentarios no se muestran\n");  // comentario de una linea
    return 0;
}
```
:::

:::concepto | 5 | Reglas de escritura (delimitadores) | Elementos aislados
| Símbolo | Para qué sirve | Ejemplo |
|---|---|---|
| `;` | Termina una sentencia | `return 0;` |
| `{ }` | Abren y cierran un bloque | cuerpo de `main` |
| `( )` | Encierran parámetros o argumentos de una función | `main(void)`, `printf("Hola")` |
| `" "` | Delimitan un literal de cadena | `"Hola"` |
| `< >` | Encierran el nombre de una cabecera estándar | `#include <stdio.h>` |
| `//`, `/* */` | Comentarios | `// nota` |

Además: **C distingue mayúsculas de minúsculas** (`Main` ≠ `main`, `Printf` ≠ `printf`) y los espacios y saltos de línea extra no importan al compilador, pero sí a quien lee tu código: **indenta** el contenido de cada bloque.
:::

## 1.2 Todas las piezas juntas: anatomía de un programa

Ahora que conoces cada pieza por separado, mira cómo interactúan en un programa completo. La explicación de cada línea está **integrada a su derecha** para que no tengas que ir y venir entre texto y código. {{ef:Atención dividida}}

```c run title="anatomia.c"
// Programa: saludo de bienvenida                 //> **Comentario**: describe el programa
// Curso: Programacion basica en C                //> El compilador lo ignora
#include <stdio.h>                                //> **Directiva** del preprocesador: incluye la cabecera de E/S
                                                  //> Línea en blanco: solo legibilidad
int main(void)                                    //> **Función principal**: aquí inicia la ejecución
{                                                 //> Inicio del bloque de `main`
    printf("Bienvenido a C\n");                   //> **Sentencia**: llamada a `printf`; termina en `;`
    printf("Hoy aprendes la estructura\n");       //> Las sentencias se ejecutan en orden, de arriba abajo
    return 0;                                     //> Devuelve 0 al sistema: «terminó sin problemas»
}                                                 //> Fin del bloque (y del programa)
```

## 1.3 Del texto al ejecutable: la cadena de compilación

Tu archivo `.c` es solo texto. Para que la computadora lo ejecute, pasa por una **cadena de herramientas** (*tool chain*). Sigue el diagrama de izquierda a derecha: arriba están las fases y abajo lo que cada una produce.

```dot caption="Figura 1. Cadena de compilación: arriba las fases, abajo lo que cada una produce." w="92%"
rankdir=LR; nodesep=0.3; ranksep=0.45;
@file(src, "bienvenida.c\ncódigo fuente")
@proc(pre, "1. Preprocesador\ncopia <stdio.h>,\nquita comentarios")
@file(exp, "código\nexpandido")
@proc(comp, "2. Compilador\nrevisa sintaxis,\ntraduce a máquina")
@file(obj, "bienvenida.o\ncódigo objeto")
@proc(link, "3. Enlazador\nune tu código\ncon bibliotecas")
@term(exe, "bienvenida.exe\nejecutable")
@io(run, "4. Ejecución\nel SO corre main")
src -> pre -> comp -> link -> run;
pre -> exp [style=dashed, arrowhead=none]; comp -> obj [style=dashed, arrowhead=none]; link -> exe [style=dashed, arrowhead=none];
{rank=same; pre; exp;} {rank=same; comp; obj;} {rank=same; link; exe;}
```

| Fase | Qué recibe | Qué hace | Qué produce |
|---|---|---|---|
| Edición | Tus ideas | Escribes el programa en un editor o IDE | `nombre.c` (código fuente) |
| Preprocesamiento | `nombre.c` | Ejecuta las directivas `#` (copia `<stdio.h>`), elimina comentarios | Código fuente expandido (temporal) |
| Compilación | Código expandido | Verifica reglas del lenguaje y traduce a lenguaje máquina | `nombre.o` / `nombre.obj` (código objeto) |
| Enlace | Código objeto + bibliotecas | Une todas las piezas y verifica que cada función usada exista | `nombre.exe` (ejecutable) |
| Ejecución | Ejecutable | El sistema operativo lo carga en memoria y ejecuta `main` | La salida en pantalla |

Con el compilador **gcc** (MinGW en Windows, Linux) todo se hace con un comando; en Code::Blocks o Visual Studio, con el botón «Compilar y ejecutar»:

```console title="Terminal: compilar y ejecutar con gcc"
$ gcc bienvenida.c -o bienvenida        # preprocesa, compila y enlaza
$ ./bienvenida                          # en Windows: bienvenida.exe
Bienvenido a C
Hoy aprendes la estructura
```

## 1.4 ¿En qué fase aparece cada error?

Los errores se clasifican según **la fase** en la que se detectan. Mira cómo se «enganchan» a la cadena:

```dot caption="Figura 2. Tipos de error según la fase en que se detectan." w="78%"
rankdir=TB; nodesep=0.5; ranksep=0.28;
@proc(c, "Compilación")
@proc(l, "Enlace")
@proc(e, "Ejecución")
@hl(r, "Resultado en pantalla")
c -> l -> e -> r;
@note(ec, "Error de COMPILACIÓN: falta ;  ·  función no declarada  ·  Printf en vez de printf")
@note(el, "Error de ENLACE: función usada pero no definida  ·  Main en vez de main")
@note(ee, "Error de EJECUCIÓN: el programa se detiene (división entre cero, memoria)")
@note(er, "Error de LÓGICA: compila y corre, pero el resultado es incorrecto")
c -> ec [style=dotted, arrowhead=none]; l -> el [style=dotted, arrowhead=none];
e -> ee [style=dotted, arrowhead=none]; r -> er [style=dotted, arrowhead=none];
{rank=same; c; ec;} {rank=same; l; el;} {rank=same; e; ee;} {rank=same; r; er;}
```

:::def | Regla de oro de la depuración
El compilador reporta los errores como **`archivo:línea:columna: error: mensaje`**. Corrige **siempre el primer error** y vuelve a compilar: muchos errores posteriores son consecuencia del primero.
:::

## 1.5 Ejemplo resuelto: tarjeta de bienvenida

:::ejemplo | Ejemplo resuelto · Tarjeta de bienvenida al curso | Ejemplo resuelto, Atención dividida
**Problema.** Escribir un programa que muestre una tarjeta de bienvenida con un borde, el nombre del curso y dos datos alineados con tabuladores.

**A. Algoritmo** (qué hacer, en lenguaje natural)

1. Mostrar el borde superior.
2. Mostrar el título del curso.
3. Mostrar los datos «Lenguaje» y «Sesiones» alineados.
4. Mostrar el borde inferior.

**B. Pseudocódigo** (en PSeInt)

```pseudo
Algoritmo TarjetaBienvenida
    Escribir "+-------------------------------+"
    Escribir "|  PROGRAMACION BASICA EN C     |"
    Escribir "|  Lenguaje: C     Sesiones: 2  |"
    Escribir "+-------------------------------+"
FinAlgoritmo
```

**C. Código en C** (cada paso del algoritmo es una o más sentencias)

```c run title="tarjeta.c"
// Tarjeta de bienvenida                           //> Comentario: propósito del programa
#include <stdio.h>                                 //> Paso 0: «ingredientes» (cabecera de E/S)
int main(void)
{
    printf("+-------------------------------+\n");  //> Paso 1: borde superior
    printf("|  PROGRAMACION BASICA EN C     |\n");  //> Paso 2: título
    printf("|  Lenguaje:\tC\t\t|\n");               //> Paso 3: `\t` alinea los datos en columnas
    printf("|  Sesiones:\t2\t\t|\n");
    printf("+-------------------------------+\n");  //> Paso 4: borde inferior
    return 0;                                       //> Fin exitoso
}
```

**D. Verificación.** La salida coincide con lo planeado en el algoritmo: cuatro partes, en el mismo orden en que se escribieron las sentencias (estructura **secuencial**).
:::

:::pregunta | Vuelve a tu respuesta inicial
¿Tu idea de cómo la computadora «entiende» C se parece a la cadena preprocesador → compilador → enlazador? ¿Qué cambiarías? {{arcs:Confianza}}
:::

:::resumen | Mapa del tema
```dot
rankdir=TB; nodesep=0.25; ranksep=0.3;
@term(p, "Programa en C")
@proc(f, "Archivo .c")
@proc(d, "Directivas #include")
@proc(m, "main(void): punto de entrada")
@proc(s, "Sentencias ; en orden")
@proc(o, "printf(\"texto\")  \\n  \\t  puts")
@proc(cm, "Comentarios // /* */")
@sub(cad, "Cadena de compilación:\npreprocesar → compilar → enlazar → ejecutar")
@hl(err, "Errores: compilación · enlace\nejecución · lógica")
p -> f; f -> d; f -> m; f -> cm; m -> s; s -> o; f -> cad; cad -> err;
```
:::

# 2. Información procedimental {.procedimental}

Esta sección es tu **caja de herramientas**: no hay que memorizarla, hay que **consultarla** mientras resuelves las tareas.

:::sintaxis | Tarjeta de sintaxis 2.1 · Plantilla de todo programa
```c check title="plantilla.c"
#include <stdio.h>

int main(void)
{
    // tus sentencias aqui
    return 0;
}
```

| Quiero… | Escribo | Resultado |
|---|---|---|
| Mostrar texto | `printf("Hola");` | `Hola` |
| Mostrar y saltar de línea | `printf("Hola\n");` o `puts("Hola");` | `Hola` + nuevo renglón |
| Mostrar varias partes seguidas | `printf("A"); printf("B"); printf("C\n");` | `ABC` |
| Alinear en columnas | `printf("Dato:\tvalor\n");` | `Dato:   valor` |
| Mostrar comillas, barra o % | `printf("Dijo \"hola\" \\ 100%%");` | `Dijo "hola" \ 100%` |
| Comentar una línea | `// nota` | (se ignora) |
| Comentar un bloque | `/* varias lineas */` | (se ignora) |
| Compilar (gcc) | `gcc prog.c -o prog` | crea `prog` (`prog.exe` en Windows) |
| Compilar con avisos | `gcc -Wall -Wextra prog.c -o prog` | muestra advertencias útiles |
:::

:::checklist | Guía de preguntas de rutina 2.2 · Antes de compilar, pregúntate…
<ul class="checks">
<li>¿Incluí <code>#include &lt;stdio.h&gt;</code> al inicio del archivo?</li>
<li>¿<code>main</code> está escrita en minúsculas y tiene paréntesis: <code>int main(void)</code>?</li>
<li>¿Cada <code>{</code> tiene su <code>}</code>? (Indentar ayuda a verlo.)</li>
<li>¿Cada sentencia termina en <code>;</code>? (Las líneas <code>#include</code>, <code>int main(void)</code>, <code>{</code> y <code>}</code> <b>no</b> llevan <code>;</code>.)</li>
<li>¿Cada texto abre y cierra comillas dobles <code>" "</code> dentro de los paréntesis de <code>printf(...)</code>?</li>
<li>Si hay errores: ¿leí el <b>primero</b> y fui a la línea y columna que indica?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 · Lee el mensaje, encuentra la causa | Variabilidad, Autoexplicación
Antes de leer la corrección, intenta explicar **por qué** falla cada programa.

**a) Falta el punto y coma.** El compilador solo lo nota cuando lee la palabra *siguiente* (`return`); por eso el mensaje dice *before 'return'*. gcc señala el lugar exacto donde falta, al final de la línea 4, y hasta dibuja el `;` debajo; otros compiladores marcan la línea siguiente.

```c err
#include <stdio.h>
int main(void)
{
    printf("Hola")
    return 0;
}
```
*Corrección:* `printf("Hola");` — el mensaje *expected ';' before 'return'* dice que falta `;` **antes** de `return`.

**b) Mayúscula donde no va.** `Printf` no existe; C distingue mayúsculas.

```c err
#include <stdio.h>
int main(void)
{
    Printf("Hola\n");
    return 0;
}
```
*Corrección:* `printf`. *Implicit declaration of function* significa «usas una función que nunca se declaró»; gcc incluso pregunta *did you mean 'printf'?*. (Con versiones de gcc anteriores a la 14 esto es solo una advertencia y el error aparece después, en el enlace: *undefined reference to `Printf`*.)

**c) Olvidar la cabecera.** Sin `#include <stdio.h>`, el compilador no conoce la declaración de `printf`.

```c err
int main(void)
{
    printf("Hola\n");
    return 0;
}
```
*Corrección:* agregar `#include <stdio.h>` al inicio. Observa que gcc sugiere la solución en el mensaje (*include '`<stdio.h>`' or provide a declaration of 'printf'*).

**d) Comillas sin cerrar.**

```c err
#include <stdio.h>
int main(void)
{
    printf("Hola\n);
    return 0;
}
```
*Corrección:* cerrar la cadena antes del paréntesis: `printf("Hola\n");`.

**e) `Main` con mayúscula: ¡error de enlace!** El archivo **compila** (no hay errores de sintaxis), pero el **enlazador** no encuentra la función `main` que todo programa necesita.

```c err
#include <stdio.h>
int Main(void)
{
    printf("Hola\n");
    return 0;
}
```
*Corrección:* `int main(void)`. Si el mensaje menciona **`ld`** o ***undefined reference***, el problema está en la fase de **enlace**.
:::

:::tip | Acentos y eñes en la consola de Windows
Si escribes `printf("Programación");` puede que la consola de Windows muestre símbolos raros. Por eso en este material los **mensajes** se escriben sin acentos (los comentarios sí pueden llevarlos). Si quieres usarlos, ejecuta `chcp 65001` en la terminal antes de correr el programa o guarda el archivo en UTF-8 y configura tu IDE.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · El mismo patrón, otro contexto | Variabilidad
El patrón «planear la salida → una sentencia por renglón → verificar» sirve para cualquier texto con formato. Aquí, un boleto de cine:

```c run title="boleto.c"
#include <stdio.h>
int main(void)
{
    printf("=== CINEMA C ===\n");             //> Encabezado
    printf("Pelicula:\tEl Compilador\n");      //> `\t` alinea las columnas
    printf("Sala:\t\t4\n");                    //> Dos `\t` porque «Sala:» es más corto
    printf("Asiento:\tF-12\n");
    printf("================\n");
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

Resuélvelas **en orden**. Cada tarea te da un poco menos de ayuda que la anterior: es el **desvanecimiento de guía**. Mantén la sección 2 a la vista. {{ef:Desvanecimiento de guía}}

:::tarea A | T1. Cartel de evento escolar: estudia el ejemplo y resuelve su gemelo | 20 min | Ejemplo resuelto, Variabilidad
**Contexto.** El club de robótica te pidió un programa que muestre en la pantalla del laboratorio el cartel de su próximo evento.

**¿Por qué y para qué?** Casi todos los programas comienzan mostrando información con formato; es la base para menús, reportes y tickets. {{arcs:Relevancia}}

**Paso 1 · Estudia este ejemplo resuelto** (lee cada anotación de la derecha):

```c run title="cartel_robotica.c"
#include <stdio.h>
int main(void)
{
    printf("******************************\n");  //> Borde superior: 30 asteriscos
    printf("*   TORNEO DE ROBOTICA 2026  *\n");  //> Título centrado a mano con espacios (30 caracteres)
    printf("******************************\n");
    printf("Fecha:\t15 de noviembre\n");          //> `\t` separa etiqueta y dato
    printf("Lugar:\tLaboratorio 3\n");
    printf("Hora:\t10:00\n");
    return 0;
}
```

**Paso 2 · Ahora tú (problema gemelo).** Escribe `cartel_feria.c` para la **Feria de Ciencias**: mismo formato (borde, título, tres datos alineados), con fecha *20 de noviembre*, lugar *Patio central* y hora *09:30*.

**Resultado esperado:** un cartel idéntico en estructura al del ejemplo, con los datos nuevos.

:::checkpoint
¿Tu programa compila al primer intento? Si no, usa la guía 2.2. ¿Los tres datos quedaron alineados? {{arcs:Confianza}}
:::

:::solucion | T1
```c run title="cartel_feria.c"
#include <stdio.h>
int main(void)
{
    printf("******************************\n");
    printf("*     FERIA DE CIENCIAS      *\n");
    printf("******************************\n");
    printf("Fecha:\t20 de noviembre\n");
    printf("Lugar:\tPatio central\n");
    printf("Hora:\t09:30\n");
    return 0;
}
```
:::
:::

:::tarea A | T2. Ticket de la cafetería (completa con pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** La cafetería de la escuela necesita imprimir un ticket de ejemplo para probar su nueva impresora.

**¿Por qué y para qué?** Los tickets usan columnas alineadas: el mismo principio de los reportes de cualquier sistema de ventas.

Completa los huecos {{c:1}} a {{c:5}}. Las pistas están en los comentarios.

```c blank title="ticket.c"
#include __1__                         // 1: cabecera para usar printf
int __2__(void)                        // 2: punto de entrada del programa
{
    printf("CAFETERIA ESCOLAR__3__");  // 3: secuencia de escape para saltar de linea
    printf("Producto\tPrecio\n");
    printf("Torta__4__$35\n");         // 4: dos tabuladores para alinear en columna
    printf("Agua\t\t$15\n");
    printf("TOTAL\t\t$50\n")__5__      // 5: lo que termina toda sentencia
    return 0;
}
```

**Resultado esperado:**

```console title="Salida esperada"
CAFETERIA ESCOLAR
Producto	Precio
Torta		$35
Agua		$15
TOTAL		$50
```

:::solucion | T2
{{c:1}} `<stdio.h>` · {{c:2}} `main` · {{c:3}} `\n` · {{c:4}} `\t\t` · {{c:5}} `;`

```c run title="ticket.c"
#include <stdio.h>
int main(void)
{
    printf("CAFETERIA ESCOLAR\n");
    printf("Producto\tPrecio\n");
    printf("Torta\t\t$35\n");
    printf("Agua\t\t$15\n");
    printf("TOTAL\t\t$50\n");
    return 0;
}
```
:::
:::

:::tarea AB | T3. Menú de un videojuego (completa sin pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Estás programando la pantalla de inicio de un videojuego de consola. **¿Para qué?** Todo juego empieza con un menú; después aprenderás a leer la opción del jugador (Tema 05).

Ahora hay más huecos y **ninguna pista**. Usa la tarjeta 2.1.

```c blank title="menu_juego.c"
__1__ <stdio.h>
__2__ main(void)
__3__
    printf("==========================\n");
    printf("     LA CRIPTA DEL BIT\n");
    printf("==========================\n")__4__
    printf("1.\tNueva partida\n");
    printf("2.\tContinuar\n");
    __5__("3.\tSalir\n");
    __6__ 0;
__7__
```

**Resultado esperado:** el menú con las tres opciones numeradas y alineadas.

:::solucion | T3
{{c:1}} `#include` · {{c:2}} `int` · {{c:3}} `{` · {{c:4}} `;` · {{c:5}} `printf` · {{c:6}} `return` · {{c:7}} `}`

```c run title="menu_juego.c"
#include <stdio.h>
int main(void)
{
    printf("==========================\n");
    printf("     LA CRIPTA DEL BIT\n");
    printf("==========================\n");
    printf("1.\tNueva partida\n");
    printf("2.\tContinuar\n");
    printf("3.\tSalir\n");
    return 0;
}
```
:::
:::

:::tarea AB | T4. Tu tarjeta de presentación (problema convencional) | 30 min | Variabilidad, Desvanecimiento de guía
**Contexto.** En la primera semana de clases cada estudiante presenta una «tarjeta digital». **¿Para qué?** Es tu primer programa completo, escrito desde cero, sin código de apoyo.

**Requisitos:**

1. Un comentario de bloque con tu nombre y la fecha.
2. Un borde superior e inferior.
3. Al menos cuatro datos alineados con `\t` (nombre, carrera o grado, lenguaje favorito, un pasatiempo).
4. Una frase final entre comillas dobles (usa `\"`).
5. Debe compilar sin errores ni advertencias con `gcc -Wall -Wextra`.

**Resultado esperado (ejemplo):**

```console title="Ejemplo de salida"
################################
Nombre:     Ana Lopez
Grado:      2o semestre
Lenguaje:   C
Pasatiempo: videojuegos
"Aprender a programar es aprender a pensar"
################################
```

:::reto | Reto extra
Dibuja tu inicial en grande con asteriscos debajo de la tarjeta (arte ASCII). {{arcs:Satisfacción}}
:::

:::solucion | T4
Hay muchas soluciones correctas; esta es una posible:

```c run title="tarjeta_presentacion.c"
/* Tarjeta de presentacion
   Autora: Ana Lopez
   Fecha: agosto 2026 */
#include <stdio.h>
int main(void)
{
    printf("################################\n");
    printf("Nombre:\t\tAna Lopez\n");
    printf("Grado:\t\t2o semestre\n");
    printf("Lenguaje:\tC\n");
    printf("Pasatiempo:\tvideojuegos\n");
    printf("\"Aprender a programar es aprender a pensar\"\n");
    printf("################################\n");
    return 0;
}
```
:::
:::

:::tarea A | T5. Una figura, muchas soluciones (solución libre) | 20 min | Solución libre, Variabilidad
**Contexto.** Necesitas mostrar este triángulo en pantalla:

```console title="Figura a mostrar"
*
**
***
****
```

**Tarea de solución libre:** no hay una única respuesta. **Escribe todas las versiones del programa que se te ocurran** para producir exactamente la misma figura. Por ejemplo: un `printf` por renglón, un solo `printf` con varios `\n`, usando `puts` (que añade el salto de línea automáticamente), dividiendo una sentencia en varias líneas… Compara tus versiones: ¿cuál es más fácil de leer?, ¿cuál es más corta?

:::solucion | T5
Algunas de las soluciones posibles (todas producen la misma salida):

```c run title="version1_un_printf_por_linea.c"
#include <stdio.h>
int main(void)
{
    printf("*\n");
    printf("**\n");
    printf("***\n");
    printf("****\n");
    return 0;
}
```

```c run title="version2_un_solo_printf.c"
#include <stdio.h>
int main(void)
{
    printf("*\n**\n***\n****\n");
    return 0;
}
```

```c run title="version3_puts.c"
#include <stdio.h>
int main(void)
{
    puts("*");
    puts("**");
    puts("***");
    puts("****");
    return 0;
}
```

```c run title="version4_varias_lineas.c"
#include <stdio.h>
int main(void)
{
    printf("*\n"
           "**\n"
           "***\n"
           "****\n");
    return 0;
}
```
La versión 1 es la más legible; la 2, la más corta; la 3 usa `puts` (*put string*), que imprime una cadena y agrega el `\n` por ti; la 4 muestra que una sentencia puede ocupar varias líneas (el `;` marca el final, no el salto de línea) y que C une las cadenas escritas una junto a otra.
:::
:::

:::tarea B | T6. ¿Puedes ayudar a tu compañero? (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
**Contexto.** Un compañero escribió este programa para mostrar el horario del laboratorio, pero no compila. Te pide ayuda porque no entiende los mensajes del compilador.

```c blank title="horario_con_errores.c"
int main(void)
{
    Printf("HORARIO DE LABORATORIO\n");
    printf("Lunes:\t\t8:00 - 10:00\n")
    printf("Miercoles:\t12:00 - 14:00\n;
    printf("Viernes:\t9:00 - 11:00\n");
    return 0;
}
```

1. Encuentra **los cuatro errores**.
2. Para cada uno, **explica con tus palabras** por qué es un error y qué fase lo detecta.
3. Escribe la versión corregida y compílala.

{{lineas:4}}

:::solucion | T6
1. Falta `#include <stdio.h>` al inicio: sin la cabecera, `printf` no está declarada (**compilación**).
2. `Printf` con mayúscula (línea 3): C distingue mayúsculas; esa función no existe (**compilación**).
3. Falta `;` al final de la línea 4 (**compilación**; gcc lo descubre al leer el `printf` de la línea 5).
4. Comillas sin cerrar en la línea 5: `"...\n;` debe ser `"...\n");` (**compilación**).

```c run title="horario.c"
#include <stdio.h>
int main(void)
{
    printf("HORARIO DE LABORATORIO\n");
    printf("Lunes:\t\t8:00 - 10:00\n");
    printf("Miercoles:\t12:00 - 14:00\n");
    printf("Viernes:\t9:00 - 11:00\n");
    return 0;
}
```
:::
:::

:::tarea B | T7. Imagina el viaje del programa (imaginación) | 15 min | Imaginación
**Contexto.** Este programa declara una función `saludar` (adelanto del Tema 10) pero nunca la define.

```c blank title="viaje.c"
#include <stdio.h>
void saludar(void);          // prototipo: "existe una funcion saludar"
int main(void)
{
    // comentario que desaparece
    saludar();
    return 0;
}
```

**Sin compilarlo**, imagina el recorrido por la cadena de la Figura 1 y responde:

1. ¿Qué le hace el **preprocesador** a las líneas 1 y 5?
2. ¿El **compilador** encuentra algún error? ¿Por qué sí o por qué no?
3. ¿Qué ocurre en el **enlazador**? Escribe el mensaje que esperas ver.
4. Ahora compílalo y compara tu predicción con el mensaje real.

{{lineas:4}}

:::solucion | T7
1. Sustituye la línea 1 por el contenido de `<stdio.h>` y elimina el comentario de la línea 5.
2. No: la línea 2 (prototipo) le promete al compilador que `saludar` existe, así que la llamada de la línea 6 es válida sintácticamente.
3. El enlazador busca la **definición** de `saludar` para unirla con `main` y no la encuentra:

```c err
#include <stdio.h>
void saludar(void);
int main(void)
{
    saludar();
    return 0;
}
```
Se corrige agregando la definición: `void saludar(void) { printf("Hola\n"); }`.
:::
:::

:::tarea AB | T8. La cadena de compilación en vivo (reto colaborativo) | 30 min | Memoria colectiva de trabajo, Movimiento humano
:::colab | Organización
**Equipos de 4, heterogéneos** (al menos un integrante de Ruta B). Roles: **Programador**, **Preprocesador**, **Compilador**, **Enlazador**. Cada integrante procesa solo su parte: así la carga del problema se reparte entre cuatro memorias de trabajo.
:::

:::movimiento | La hoja viaja por el salón
1. El **Programador** escribe en una hoja un programa corto (5–8 líneas) que use `printf` y **una función** declarada con prototipo.
2. Entrega la hoja (físicamente) al **Preprocesador**, que tacha los comentarios y pega una tarjeta que dice «contenido de stdio.h» sobre cada `#include`.
3. El **Compilador** revisa línea por línea: `;`, llaves, comillas, paréntesis, mayúsculas. Si encuentra un error, marca `línea:columna` y devuelve la hoja al Programador.
4. El **Enlazador** verifica que cada función llamada tenga una definición. Si falta, escribe *undefined reference*.
5. Si la hoja pasa todas las fases, el equipo la escribe en la computadora y la ejecuta. Luego **rotan roles**.
:::

**Producto del equipo:** escriban un programa con **un error de compilación, uno de enlace y uno de lógica** y entréguenlo a otro equipo para que lo depure y explique cada error.

:::solucion | T8
Ejemplo de programa con un error de cada tipo (para el equipo que depura):

- **Compilación:** falta `;` en un `printf`.
- **Enlace:** se llama a `void despedir(void);` que solo tiene prototipo.
- **Lógica:** el programa debe mostrar «Hoy es lunes» y muestra «Hoy es martes» (compila y corre, pero el resultado es incorrecto).

La depuración se hace en ese orden: primero el compilador, luego el enlazador y, por último, la comparación de la salida con lo esperado.
:::
:::

:::tarea B | T9. Mejora este material (autogestión) | 20 min | Autogestión, Atención dividida, Redundancia
**Contexto.** Un sitio web explica el «Hola mundo» en C así:

:::autog | Material original (mal diseñado)
*El programa comienza con una directiva al preprocesador que incluye la biblioteca estándar de entrada y salida, después se declara la función principal que no recibe parámetros y devuelve un entero, y dentro de su bloque se llama a la función de impresión con formato pasándole como argumento la cadena literal Hola mundo seguida de un salto de línea, y finalmente se devuelve cero. El programa comienza con una directiva al preprocesador…* (el párrafo se repite debajo del código, y el código aparece dos páginas después).
:::

Identifica sus problemas de diseño (atención dividida, redundancia, texto excesivo) y **rediséñalo**: código a la izquierda y una explicación breve pegada a cada línea, sin repetir información. Compara tu versión con la solución.

:::solucion | T9
Problemas: (1) el texto está **separado** del código (atención dividida), (2) el párrafo se **repite** (redundancia), (3) un solo bloque de texto largo sin señalizar qué parte del código explica. Rediseño:

```c run title="hola_redisenado.c"
#include <stdio.h>             //> Trae `printf` (cabecera de E/S estándar)
int main(void)                 //> Aquí empieza la ejecución
{
    printf("Hola mundo\n");    //> Muestra el texto en pantalla y salta de línea
    return 0;                  //> Termina: «todo bien»
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Una experta resuelve un problema nuevo pensando en voz alta | Modalidad, Ejemplo resuelto
*Guion para narración en audio (≈ 3 min). Para evitar el efecto de **información transitoria**, grábalo en 4 segmentos cortos que el estudiante pueda pausar y repetir, mostrando en pantalla el código mientras se escucha (sin el texto del guion, para no generar **redundancia**).*

**Problema:** «Mostrar el recibo de una papelería con tres productos y el total, alineado en columnas».

**Segmento 1 — Planear antes de teclear.** {{como}} Primero dibujo en papel cómo quiero que se vea la salida: un encabezado, tres renglones de producto y precio, y el total. {{porque}} Si no sé qué quiero ver, no sé qué sentencias escribir; cada renglón de la salida será una llamada a `printf`.

**Segmento 2 — Esqueleto y primera compilación.** {{como}} Escribo la plantilla: `#include <stdio.h>`, `int main(void)`, llaves y `return 0;`. Compilo **ya**, aunque no haga nada. {{porque}} Si hay un error ahora, sé que está en cinco líneas y no en cincuenta.

**Segmento 3 — Agregar de a poco.** {{como}} Agrego el encabezado y compilo; luego los productos con `\t` entre nombre y precio. Veo que «Cuaderno» desalinea la columna porque es más largo, así que a los nombres cortos les pongo dos `\t`. {{porque}} El tabulador salta a la siguiente columna fija (cada 8 caracteres); los textos de distinta longitud necesitan distinto número de saltos.

**Segmento 4 — Leer el error, no adivinarlo.** {{como}} Al compilar aparece `recibo.c:7:28: error: expected ';' before 'printf'`. Voy a la línea **7**, columna 28: justo después del paréntesis de cierre falta el `;`. {{porque}} El compilador solo lo nota al leer el `printf` de la línea 8 (por eso dice *before 'printf'*), pero gcc me señala dónde debe ir. Corrijo, compilo y comparo la salida con mi dibujo inicial.

```c run title="recibo.c"
#include <stdio.h>
int main(void)
{
    printf("PAPELERIA EL LAPIZ\n");
    printf("Producto\tPrecio\n");
    printf("Cuaderno\t$40\n");
    printf("Lapiz\t\t$8\n");
    printf("Goma\t\t$6\n");
    printf("TOTAL\t\t$54\n");
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo (10 reactivos)
1. ¿Cuál es el punto de entrada de todo programa en C?
   a) `inicio()` · b) `main()` · c) `#include` · d) `printf`
2. ¿Qué archivo de cabecera debe incluirse para usar `printf`?
   a) `<string.h>` · b) `<math.h>` · c) `<stdio.h>` · d) `<stdlib.h>`
3. ¿Qué símbolo marca el final de una sentencia? \_\_\_\_\_
4. Relaciona cada fase con lo que produce: (1) Preprocesamiento, (2) Compilación, (3) Enlace.
   a) Ejecutable · b) Código fuente expandido · c) Código objeto
5. Verdadero o falso: `Printf` y `printf` son el mismo nombre para el compilador.
6. ¿Qué hace la secuencia de escape `\t`?
7. ¿Cómo se escribe un comentario que ocupa varias líneas?
8. El mensaje *undefined reference to main* aparece en la fase de:
   a) edición · b) preprocesamiento · c) compilación · d) enlace
9. ¿Qué significa `return 0;` al final de `main`?
10. Explica en una oración la diferencia entre un error de **sintaxis** y un error de **lógica**.
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida** exacta (marca con ⏎ los saltos de línea):

```c check title="p1.c"
#include <stdio.h>
int main(void)
{
    printf("Uno");
    printf("Dos\n");
    printf("Tres\nCuatro\n\n");
    printf("Fin");
    return 0;
}
```

**P2. Corrige** el programa (tiene tres errores) y explica en qué fase se detecta cada uno:

```c blank title="p2.c"
#include <stdio.h>
int main(void)
{
    printf("Prueba de errores\n")
    printf("Linea dos\n);
    return 0;
```

**P3. Ordena las líneas** para formar un programa válido que muestre `Listo`:
`}` · `return 0;` · `#include <stdio.h>` · `{` · `int main(void)` · `printf("Listo\n");`

**P4. Escribe un programa** que muestre tu horario de clases de un día con tres materias, una por renglón, con la hora y la materia alineadas por `\t`, y un comentario de bloque con tu nombre.
:::

:::registro | 5.3 Autorregistro
Marca lo que ya puedes hacer:
<ul class="checks">
<li>Escribo la plantilla de un programa en C sin mirar la tarjeta.</li>
<li>Uso <code>printf</code>, <code>puts</code>, <code>\n</code> y <code>\t</code> para dar formato a la salida.</li>
<li>Explico qué hace cada fase de la cadena de compilación.</li>
<li>Leo un mensaje de error y voy a la línea y columna correctas.</li>
</ul>
**¿Cuánto esfuerzo mental te exigió este tema?** (escala de Paas, 1 = muy, muy bajo · 9 = muy, muy alto)
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 b · 2 c · 3 `;` · 4 (1)-b, (2)-c, (3)-a · 5 Falso · 6 Inserta un tabulador (salta a la siguiente columna) · 7 Entre `/*` y `*/` · 8 d · 9 Termina `main` e informa al sistema operativo que el programa finalizó correctamente · 10 Un error de sintaxis viola las reglas del lenguaje y lo detecta el compilador; un error de lógica compila y se ejecuta, pero produce un resultado incorrecto.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** Salida real:

```c run title="p1.c"
#include <stdio.h>
int main(void)
{
    printf("Uno");
    printf("Dos\n");
    printf("Tres\nCuatro\n\n");
    printf("Fin");
    return 0;
}
```

**P2.** (1) Falta `;` después de `printf("Prueba de errores\n")` — compilación. (2) Comillas sin cerrar en `"Linea dos\n);` — compilación. (3) Falta la llave de cierre `}` de `main` — compilación.

**P3.** `#include <stdio.h>` → `int main(void)` → `{` → `printf("Listo\n");` → `return 0;` → `}`.

**P4.** Ejemplo:

```c run title="horario.c"
/* Horario del lunes
   Autor: Luis Perez */
#include <stdio.h>
int main(void)
{
    printf("07:00\tMatematicas\n");
    printf("09:00\tProgramacion\n");
    printf("11:00\tFisica\n");
    return 0;
}
```
:::
