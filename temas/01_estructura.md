---
num: "01"
archivo: "Tema01_Estructura_programa_y_compilacion"
titulo: "Estructura de un programa en C++ y cadena de compilación"
corto: "Estructura y compilación"
lema: "Del texto que escribes al programa que se ejecuta: anatomía de un programa y el viaje que hace hasta convertirse en ejecutable."
duracion: "4 h · 2 sesiones de 2 h"
previos: "Ninguno (tema de entrada). Uso básico de la computadora y de un editor de texto."
fuentes:
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Ediciones de la U / Ra-Ma. Cap. 1: §1.1 Características, §1.2.1 Instrucciones, §1.2.3 Bibliotecas, §1.2.6 Comentarios, §1.2.7 Delimitadores, §1.3 Fases de la ejecución, §1.4 Tipos de errores, §1.5 Ejemplo de un programa."
  - "Lospinoso, J. (2019). *C++ Crash Course*. No Starch Press. Cap. 1 «Up and Running»: The Structure of a Basic C++ Program, The Compiler Tool Chain, Comments, Debugging."
objetivos:
  A:
    - "Identificar las partes de un programa básico: comentarios, directivas `#include`, función `main`, bloque `{ }`, sentencias y `return 0;`."
    - "Escribir, compilar y ejecutar programas que muestren texto en pantalla con `cout`, `\\n`, `endl` y `\\t`."
    - "Describir con sus palabras las fases de edición, preprocesamiento, compilación, enlace y ejecución."
    - "Distinguir errores de compilación, de enlace, de ejecución y de lógica, y corregir los errores de sintaxis más comunes."
  B:
    - "Explicar qué recibe y qué produce cada fase de la cadena de compilación (`.cpp`, `.o/.obj`, `.exe`)."
    - "Interpretar mensajes de g++ con el formato `archivo:línea:columna` y corregir varios errores encadenados empezando por el primero."
    - "Explicar por qué un prototipo sin definición produce un error de **enlace** y no de compilación."
    - "Comparar la salida con `cout` (C++) y con `printf` (C), como la usa el *C++ Crash Course*."
efectos:
  soporte:
    - ["Elementos aislados", "La anatomía del programa se presenta pieza por pieza (main → cout → using → \\n/\\t → comentarios) antes del programa completo."]
    - ["Atención dividida", "Código anotado línea por línea: la explicación está pegada a cada línea, no en un párrafo aparte."]
    - ["Ejemplo resuelto", "Tarjeta de bienvenida: algoritmo → pseudocódigo → C++ comentado → salida real."]
    - ["Modalidad", "El diagrama de la cadena de compilación se acompaña con el guion narrado del protocolo verbal (audio breve)."]
  procedimental:
    - ["Variabilidad", "Errores frecuentes mostrados en contextos distintos, con el mensaje real de g++."]
    - ["Redundancia", "La tarjeta de sintaxis evita repetir teoría: solo plantillas y reglas mínimas para consultar."]
    - ["Autoexplicación", "Preguntas «¿por qué falla?» antes de mostrar cada corrección."]
  tareas:
    - ["Ejemplo resuelto", "T1: cartel resuelto + problema gemelo."]
    - ["Problema por completar", "T2 con pistas; T3 sin pistas y con más huecos."]
    - ["Desvanecimiento de guía", "Secuencia T1 → T2 → T3 → T4 (de resuelto a convencional)."]
    - ["Solución libre", "T5: dibujar una figura con todas las formas de salida que conozcas."]
    - ["Autoexplicación", "T6: encontrar, explicar y corregir errores en el programa de un compañero."]
    - ["Imaginación", "T7 (Ruta B): imaginar el viaje de un programa por la cadena antes de compilarlo."]
    - ["Memoria colectiva de trabajo", "T8: la cadena de compilación en vivo, por equipos heterogéneos."]
    - ["Movimiento humano", "T8: cada integrante representa una fase y «mueve» el programa físicamente."]
    - ["Autogestión", "T9: rediseñar una explicación mal diseñada aplicando los efectos de la TCC."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Conceptos aislados con ejemplos resueltos y código anotado; uso de compilador en línea para no instalar nada."
    B: "Lectura de la sección completa como repaso; foco en el error de enlace y la comparación `cout` vs `printf`."
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
    B: "Terminal con `g++ -Wall`; lectura directa de mensajes del compilador."
plan:
  - ["Apertura", "Soporte", "Analogía de la receta y pregunta «¿cómo entiende la computadora tu texto?». Mostrar un juego hecho en C++ (relevancia).", "10 min"]
  - ["Desarrollo", "Soporte + protocolo", "Conceptos 1 a 6 (uno a la vez), anatomía anotada, cadena de compilación narrada y ejemplo resuelto 1.6.", "60 min"]
  - ["Práctica guiada", "Tareas + procedimental", "Ruta A: T1 → T2 → T3. Ruta B: T3, T6, T7. Tarjeta de sintaxis a la vista.", "60 min"]
  - ["Práctica colaborativa", "Tareas", "T8 por equipos heterogéneos (4 integrantes).", "30 min"]
  - ["Autónoma y cierre", "Tareas + evaluación", "T4 (todos), T5 (A), T9 (B); recall test, comprehension test y autorregistro.", "80 min"]
glosario:
  - ["código fuente", "source code", "Texto del programa escrito en C++ (archivo `.cpp`)."]
  - ["compilador", "compiler", "Programa que traduce el código fuente a código objeto (lenguaje máquina)."]
  - ["preprocesador", "preprocessor", "Fase previa que procesa las directivas `#` (por ejemplo, copia el contenido de `<iostream>`)."]
  - ["enlazador", "linker", "Une los archivos objeto con las bibliotecas y produce el ejecutable."]
  - ["archivo objeto", "object file", "Resultado de compilar un `.cpp` (`.o` en g++, `.obj` en Visual Studio)."]
  - ["ejecutable", "executable", "Archivo que el sistema operativo puede ejecutar (`.exe` en Windows)."]
  - ["cadena de herramientas", "tool chain", "Conjunto preprocesador + compilador + enlazador."]
  - ["sentencia / instrucción", "statement", "Unidad de acción del programa; en C++ termina en `;`."]
  - ["directiva", "directive", "Instrucción para el preprocesador; empieza con `#`."]
  - ["biblioteca", "library", "Código ya escrito que se incorpora al programa (p. ej., `<iostream>`)."]
  - ["flujo de salida", "output stream", "`cout`: canal por el que el programa envía texto a la pantalla."]
  - ["literal de cadena", "string literal", "Texto entre comillas dobles, como `\"Hola\"`."]
  - ["secuencia de escape", "escape sequence", "Combinación con `\\` que representa un carácter especial: `\\n`, `\\t`."]
  - ["espacio de nombres", "namespace", "Agrupación de nombres; la biblioteca estándar vive en `std`."]
  - ["punto de entrada", "entry point", "Lugar donde inicia la ejecución: la función `main`."]
  - ["error de compilación", "compile-time error", "Error detectado al traducir (sintaxis, nombres no declarados)."]
  - ["error de enlace", "link-time error", "Error detectado al unir piezas (función declarada pero no definida)."]
  - ["error en tiempo de ejecución", "runtime error", "Error que aparece cuando el programa ya se está ejecutando."]
  - ["depurador", "debugger", "Herramienta para ejecutar paso a paso e inspeccionar el programa (GDB, Visual Studio)."]
---

# 1. Información de soporte {.soporte}

:::analogia | Un programa es una receta… para un cocinero muy literal
Imagina una receta de cocina. Primero dice **qué ingredientes necesitas**, después da **pasos en orden** y cada paso termina con un punto. El cocinero no improvisa: si la receta dice «agrega sal» pero nunca dijiste qué es la sal, se detiene.

Un programa en C++ funciona igual: las **bibliotecas** son los ingredientes, las **sentencias** son los pasos (cada una termina en `;`) y la computadora es el cocinero literal. Hay un detalle: el cocinero no lee español ni C++, solo **lenguaje máquina** (ceros y unos). Por eso necesitamos un **traductor**: el compilador.
:::

:::pregunta
Antes de seguir, piensa 30 segundos: **¿cómo crees que la computadora «entiende» lo que escribes en C++ si solo maneja ceros y unos?** Anota tu idea; al final de la sección 1.5 la comparas con lo que realmente pasa.

{{lineas:2}}
:::

:::relevancia | ¿Por qué y para qué aprender esto?
C++ está detrás de motores de videojuegos (Unreal Engine), navegadores (Chrome), sistemas operativos, software de bancos y hasta de las placas Arduino. Todos esos programas, por grandes que sean, tienen la misma estructura básica que vas a aprender hoy: **un `main`, sentencias en orden y una cadena de compilación que los convierte en ejecutables**. Dominar esto te permite leer cualquier programa en C++ y entender los mensajes de error, que es la habilidad que más tiempo ahorra a un programador. {{arcs:Relevancia}}
:::

## 1.1 Las piezas, una por una

Un programa tiene varias piezas que interactúan. Para no saturar tu memoria de trabajo, las verás **aisladas**, una a la vez; al final las juntamos. {{ef:Elementos aislados}}

:::concepto | 1 | El programa más pequeño: la función `main` | Elementos aislados, Atención dividida
Todo programa en C++ empieza a ejecutarse en una función llamada **`main`**. Es el **punto de entrada**.

```cpp check
int main()     //> `int`: main devuelve un número entero al sistema operativo
{              //> `{` abre el **bloque** de instrucciones de main
    return 0;  //> `return 0;` termina el programa e informa «todo salió bien»
}              //> `}` cierra el bloque
```

Este programa compila y se ejecuta… pero no hace nada visible. Para «ver» algo necesitamos la siguiente pieza.
:::

:::concepto | 2 | Mostrar texto: `#include <iostream>` y `cout` | Elementos aislados, Atención dividida
Para escribir en pantalla usamos `cout` (*character output*), que vive en la **biblioteca** `iostream`. La línea `#include` le pide al preprocesador que copie esa biblioteca dentro de tu programa.

```cpp run
#include <iostream>                //> Directiva: trae la biblioteca de entrada/salida
int main()
{
    std::cout << "Hola, mundo";    //> `std::cout` es la pantalla; `<<` «envía» el texto hacia ella
    return 0;
}
```

- El texto entre comillas dobles (`"Hola, mundo"`) es un **literal de cadena**: se muestra tal cual.
- El operador `<<` se lee «enviar a». Puedes encadenarlo: `std::cout << "Hola" << " mundo";`
- `std::` indica que `cout` pertenece al **espacio de nombres** estándar `std`.
:::

:::concepto | 3 | El atajo `using namespace std;` | Elementos aislados
Escribir `std::` antes de cada `cout` es correcto, pero repetitivo. La línea `using namespace std;` le dice al compilador «busca los nombres también en `std`», y entonces basta con `cout`.

```cpp run
#include <iostream>
using namespace std;          //> A partir de aquí `cout` equivale a `std::cout`
int main()
{
    cout << "Hola, mundo";    //> Sin `std::` gracias a la línea 2
    return 0;
}
```

:::nota | ¿Por qué el C++ Crash Course no usa este atajo?
El libro de Lospinoso escribe siempre `std::` (y en el capítulo 1 usa `printf` de C). En programas grandes, `using namespace std;` puede provocar choques de nombres. En este curso lo usamos porque reduce la carga de lectura en programas pequeños; en la Ruta B verás ambas formas.
:::
:::

:::concepto | 4 | Saltos de línea y tabuladores: `\n`, `endl`, `\t` | Elementos aislados, Atención dividida
`cout` no cambia de renglón por sí solo. Para controlar el formato se usan **secuencias de escape** (una barra invertida `\` seguida de una letra) o el manipulador `endl`.

```cpp run
#include <iostream>
using namespace std;
int main()
{
    cout << "Linea 1";                 //> Sin salto: lo siguiente queda pegado
    cout << " (sigue)\n";              //> `\n` = salto de línea dentro del texto
    cout << "Linea 2" << endl;         //> `endl` = salto de línea (y vacía el búfer)
    cout << "Nombre:\tAna\n";          //> `\t` = tabulador: alinea en columnas
    cout << "Edad:\t17\n";
    return 0;
}
```
:::

:::concepto | 5 | Comentarios: notas para humanos | Elementos aislados
El compilador **ignora** los comentarios; sirven para explicar el código a otras personas (¡y a ti en el futuro!).

```cpp run
#include <iostream>
using namespace std;
/* Comentario de bloque:
   puede ocupar varias lineas.
   Autor: equipo 3, Programacion basica */
int main()
{
    cout << "Los comentarios no se muestran\n";  // comentario de una linea
    return 0;
}
```
:::

:::concepto | 6 | Reglas de escritura (delimitadores) | Elementos aislados
| Símbolo | Para qué sirve | Ejemplo |
|---|---|---|
| `;` | Termina una sentencia | `return 0;` |
| `{ }` | Abren y cierran un bloque | cuerpo de `main` |
| `( )` | Encierran parámetros de una función | `main()` |
| `" "` | Delimitan un literal de cadena | `"Hola"` |
| `< >` | Encierran el nombre de una biblioteca estándar | `#include <iostream>` |
| `//`, `/* */` | Comentarios | `// nota` |

Además: **C++ distingue mayúsculas de minúsculas** (`Main` ≠ `main`, `Cout` ≠ `cout`) y los espacios y saltos de línea extra no importan al compilador, pero sí a quien lee tu código: **indenta** el contenido de cada bloque.
:::

## 1.2 Todas las piezas juntas: anatomía de un programa

Ahora que conoces cada pieza por separado, mira cómo interactúan en un programa completo. La explicación de cada línea está **integrada a su derecha** para que no tengas que ir y venir entre texto y código. {{ef:Atención dividida}}

```cpp run title="anatomia.cpp"
// Programa: saludo de bienvenida                 //> **Comentario**: describe el programa
// Curso: Programacion basica en C++              //> El compilador lo ignora
#include <iostream>                               //> **Directiva** del preprocesador: incluye la biblioteca
using namespace std;                              //> Permite escribir `cout` en lugar de `std::cout`
                                                  //> Línea en blanco: solo legibilidad
int main()                                        //> **Función principal**: aquí inicia la ejecución
{                                                 //> Inicio del bloque de `main`
    cout << "Bienvenido a C++\n";                 //> **Sentencia** de salida; termina en `;`
    cout << "Hoy aprendes la estructura\n";       //> Las sentencias se ejecutan en orden, de arriba abajo
    return 0;                                     //> Devuelve 0 al sistema: «terminó sin problemas»
}                                                 //> Fin del bloque (y del programa)
```

## 1.3 Del texto al ejecutable: la cadena de compilación

Tu archivo `.cpp` es solo texto. Para que la computadora lo ejecute, pasa por una **cadena de herramientas** (*tool chain*). Sigue el diagrama de izquierda a derecha: arriba están las fases y abajo lo que cada una produce.

```dot caption="Figura 1. Cadena de compilación: arriba las fases, abajo lo que cada una produce." w="92%"
rankdir=LR; nodesep=0.3; ranksep=0.45;
@file(src, "bienvenida.cpp\ncódigo fuente")
@proc(pre, "1. Preprocesador\ncopia <iostream>,\nquita comentarios")
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
| Edición | Tus ideas | Escribes el programa en un editor o IDE | `nombre.cpp` (código fuente) |
| Preprocesamiento | `nombre.cpp` | Ejecuta las directivas `#` (copia `<iostream>`), elimina comentarios | Código fuente expandido (temporal) |
| Compilación | Código expandido | Verifica reglas del lenguaje y traduce a lenguaje máquina | `nombre.o` / `nombre.obj` (código objeto) |
| Enlace | Código objeto + bibliotecas | Une todas las piezas y verifica que cada función usada exista | `nombre.exe` (ejecutable) |
| Ejecución | Ejecutable | El sistema operativo lo carga en memoria y ejecuta `main` | La salida en pantalla |

Con el compilador **g++** (MinGW en Windows, Linux) todo se hace con un comando; en Visual Studio, con el botón «Compilar y ejecutar»:

```console title="Terminal: compilar y ejecutar con g++"
$ g++ bienvenida.cpp -o bienvenida      # preprocesa, compila y enlaza
$ ./bienvenida                          # en Windows: bienvenida.exe
Bienvenido a C++
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
@note(ec, "Error de COMPILACIÓN: falta ;  ·  nombre no declarado  ·  Cout en vez de cout")
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
    Escribir "|  PROGRAMACION BASICA EN C++   |"
    Escribir "|  Lenguaje: C++   Sesiones: 2  |"
    Escribir "+-------------------------------+"
FinAlgoritmo
```

**C. Código en C++** (cada paso del algoritmo es una o más sentencias)

```cpp run title="tarjeta.cpp"
// Tarjeta de bienvenida                     //> Comentario: propósito del programa
#include <iostream>                          //> Paso 0: «ingredientes» (biblioteca)
using namespace std;
int main()
{
    cout << "+-------------------------------+\n";  //> Paso 1: borde superior
    cout << "|  PROGRAMACION BASICA EN C++   |\n";  //> Paso 2: título
    cout << "|  Lenguaje:\tC++\t\t|\n";             //> Paso 3: `\t` alinea los datos en columnas
    cout << "|  Sesiones:\t2\t\t|\n";
    cout << "+-------------------------------+\n";  //> Paso 4: borde inferior
    return 0;                                       //> Fin exitoso
}
```

**D. Verificación.** La salida coincide con lo planeado en el algoritmo: cuatro partes, en el mismo orden en que se escribieron las sentencias (estructura **secuencial**).
:::

:::pregunta | Vuelve a tu respuesta inicial
¿Tu idea de cómo la computadora «entiende» C++ se parece a la cadena preprocesador → compilador → enlazador? ¿Qué cambiarías? {{arcs:Confianza}}
:::

:::resumen | Mapa del tema
```dot
rankdir=TB; nodesep=0.25; ranksep=0.3;
@term(p, "Programa C++")
@proc(f, "Archivo .cpp")
@proc(d, "Directivas #include")
@proc(m, "main(): punto de entrada")
@proc(s, "Sentencias ; en orden")
@proc(o, "cout << \"texto\"  \\n  \\t  endl")
@proc(cm, "Comentarios // /* */")
@sub(cad, "Cadena de compilación:\npreprocesar → compilar → enlazar → ejecutar")
@hl(err, "Errores: compilación · enlace\nejecución · lógica")
p -> f; f -> d; f -> m; f -> cm; m -> s; s -> o; f -> cad; cad -> err;
```
:::

# 2. Información procedimental {.procedimental}

Esta sección es tu **caja de herramientas**: no hay que memorizarla, hay que **consultarla** mientras resuelves las tareas.

:::sintaxis | Tarjeta de sintaxis 2.1 · Plantilla de todo programa
```cpp check title="plantilla.cpp"
#include <iostream>
using namespace std;

int main()
{
    // tus sentencias aqui
    return 0;
}
```

| Quiero… | Escribo | Resultado |
|---|---|---|
| Mostrar texto | `cout << "Hola";` | `Hola` |
| Mostrar y saltar de línea | `cout << "Hola\n";` o `cout << "Hola" << endl;` | `Hola` + nuevo renglón |
| Encadenar varias partes | `cout << "A" << "B" << "C\n";` | `ABC` |
| Alinear en columnas | `cout << "Dato:\tvalor\n";` | `Dato:   valor` |
| Mostrar comillas o barra | `cout << "Dijo \"hola\" \\ fin";` | `Dijo "hola" \ fin` |
| Comentar una línea | `// nota` | (se ignora) |
| Comentar un bloque | `/* varias lineas */` | (se ignora) |
| Compilar (g++) | `g++ prog.cpp -o prog` | crea `prog.exe` |
| Compilar con avisos | `g++ -Wall prog.cpp -o prog` | muestra advertencias útiles |
:::

:::checklist | Guía de preguntas de rutina 2.2 · Antes de compilar, pregúntate…
<ul class="checks">
<li>¿Incluí <code>#include &lt;iostream&gt;</code> y escribí <code>using namespace std;</code> (o <code>std::</code>)?</li>
<li>¿<code>main</code> está escrita en minúsculas y tiene paréntesis: <code>int main()</code>?</li>
<li>¿Cada <code>{</code> tiene su <code>}</code>? (Indentar ayuda a verlo.)</li>
<li>¿Cada sentencia termina en <code>;</code>? (Las líneas <code>#include</code>, <code>int main()</code>, <code>{</code> y <code>}</code> <b>no</b> llevan <code>;</code>.)</li>
<li>¿Cada texto abre y cierra comillas dobles <code>" "</code>?</li>
<li>Si hay errores: ¿leí el <b>primero</b> y fui a la línea y columna que indica?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 · Lee el mensaje, encuentra la causa | Variabilidad, Autoexplicación
Antes de leer la corrección, intenta explicar **por qué** falla cada programa.

**a) Falta el punto y coma.** El compilador se da cuenta hasta la *siguiente* línea, por eso el error puede señalar una línea después.

```cpp err
#include <iostream>
using namespace std;
int main()
{
    cout << "Hola"
    return 0;
}
```
*Corrección:* `cout << "Hola";` — el mensaje dice *expected ';' before 'return'*: falta `;` **antes** de `return`.

**b) Mayúscula donde no va.** `Cout` no existe; C++ distingue mayúsculas.

```cpp err
#include <iostream>
using namespace std;
int main()
{
    Cout << "Hola\n";
    return 0;
}
```
*Corrección:* `cout`. El mensaje *was not declared in this scope* significa «no conozco ese nombre».

**c) Olvidar la biblioteca.** Sin `#include <iostream>`, `cout` no está declarado.

```cpp err
using namespace std;
int main()
{
    std::cout << "Hola\n";
    return 0;
}
```
*Corrección:* agregar `#include <iostream>` al inicio. Observa que g++ incluso sugiere la solución en el mensaje (*did you forget to include?*).

**d) Comillas sin cerrar.**

```cpp err
#include <iostream>
using namespace std;
int main()
{
    cout << "Hola\n;
    return 0;
}
```
*Corrección:* cerrar la cadena: `"Hola\n";`.

**e) `Main` con mayúscula: ¡error de enlace!** El archivo **compila** (no hay errores de sintaxis), pero el **enlazador** no encuentra la función `main` que todo programa necesita.

```cpp err
#include <iostream>
using namespace std;
int Main()
{
    cout << "Hola\n";
    return 0;
}
```
*Corrección:* `int main()`. Si el mensaje menciona **`ld`** o ***undefined reference***, el problema está en la fase de **enlace**.
:::

:::tip | Acentos y eñes en la consola de Windows
Si escribes `cout << "Programación";` puede que la consola de Windows muestre símbolos raros. Por eso en este material los **mensajes** se escriben sin acentos (los comentarios sí pueden llevarlos). Si quieres usarlos, ejecuta `chcp 65001` en la terminal antes de correr el programa o guarda el archivo en UTF-8 y configura tu IDE.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · El mismo patrón, otro contexto | Variabilidad
El patrón «planear la salida → una sentencia por renglón → verificar» sirve para cualquier texto con formato. Aquí, un boleto de cine:

```cpp run title="boleto.cpp"
#include <iostream>
using namespace std;
int main()
{
    cout << "=== CINEMA C++ ===\n";       //> Encabezado
    cout << "Pelicula:\tEl Compilador\n";  //> `\t` alinea las columnas
    cout << "Sala:\t\t4\n";                //> Dos `\t` porque «Sala:» es más corto
    cout << "Asiento:\tF-12\n";
    cout << "==================\n";
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

```cpp run title="cartel_robotica.cpp"
#include <iostream>
using namespace std;
int main()
{
    cout << "******************************\n";  //> Borde superior: 30 asteriscos
    cout << "*   TORNEO DE ROBOTICA 2026  *\n";  //> Título centrado a mano con espacios (30 caracteres)
    cout << "******************************\n";
    cout << "Fecha:\t15 de noviembre\n";          //> `\t` separa etiqueta y dato
    cout << "Lugar:\tLaboratorio 3\n";
    cout << "Hora:\t10:00\n";
    return 0;
}
```

**Paso 2 · Ahora tú (problema gemelo).** Escribe `cartel_feria.cpp` para la **Feria de Ciencias**: mismo formato (borde, título, tres datos alineados), con fecha *20 de noviembre*, lugar *Patio central* y hora *09:30*.

**Resultado esperado:** un cartel idéntico en estructura al del ejemplo, con los datos nuevos.

:::checkpoint
¿Tu programa compila al primer intento? Si no, usa la guía 2.2. ¿Los tres datos quedaron alineados? {{arcs:Confianza}}
:::

:::solucion | T1
```cpp run title="cartel_feria.cpp"
#include <iostream>
using namespace std;
int main()
{
    cout << "******************************\n";
    cout << "*     FERIA DE CIENCIAS      *\n";
    cout << "******************************\n";
    cout << "Fecha:\t20 de noviembre\n";
    cout << "Lugar:\tPatio central\n";
    cout << "Hora:\t09:30\n";
    return 0;
}
```
:::
:::

:::tarea A | T2. Ticket de la cafetería (completa con pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** La cafetería de la escuela necesita imprimir un ticket de ejemplo para probar su nueva impresora.

**¿Por qué y para qué?** Los tickets usan columnas alineadas: el mismo principio de los reportes de cualquier sistema de ventas.

Completa los huecos {{c:1}} a {{c:5}}. Las pistas están en los comentarios.

```cpp blank title="ticket.cpp"
#include __1__                         // 1: biblioteca para usar cout
using namespace std;
int __2__()                            // 2: punto de entrada del programa
{
    cout << "CAFETERIA ESCOLAR" __3__  // 3: termina la linea con un salto (dos formas validas)
    cout << "Producto\tPrecio\n";
    cout << "Torta" __4__ "$35\n";     // 4: alinea el precio en la columna (operador + escape)
    cout << "Agua\t\t$15\n";
    cout << "TOTAL\t\t$50\n"__5__      // 5: lo que termina toda sentencia
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
{{c:1}} `<iostream>` · {{c:2}} `main` · {{c:3}} `<< endl;` o `<< "\n";` · {{c:4}} `<< "\t\t" <<` · {{c:5}} `;`

```cpp run title="ticket.cpp"
#include <iostream>
using namespace std;
int main()
{
    cout << "CAFETERIA ESCOLAR" << endl;
    cout << "Producto\tPrecio\n";
    cout << "Torta" << "\t\t" << "$35\n";
    cout << "Agua\t\t$15\n";
    cout << "TOTAL\t\t$50\n";
    return 0;
}
```
:::
:::

:::tarea AB | T3. Menú de un videojuego (completa sin pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Estás programando la pantalla de inicio de un videojuego de consola. **¿Para qué?** Todo juego empieza con un menú; después aprenderás a leer la opción del jugador (Tema 05).

Ahora hay más huecos y **ninguna pista**. Usa la tarjeta 2.1.

```cpp blank title="menu_juego.cpp"
#include <iostream>
__1__ namespace std__2__
int main()
__3__
    cout << "==========================\n";
    cout << "     LA CRIPTA DEL BIT\n";
    cout << "==========================\n" __4__
    cout << "1.\tNueva partida\n";
    cout << "2.\tContinuar\n";
    cout __5__ "3.\tSalir\n";
    __6__ 0;
__7__
```

**Resultado esperado:** el menú con las tres opciones numeradas y alineadas.

:::solucion | T3
{{c:1}} `using` · {{c:2}} `;` · {{c:3}} `{` · {{c:4}} `;` · {{c:5}} `<<` · {{c:6}} `return` · {{c:7}} `}`

```cpp run title="menu_juego.cpp"
#include <iostream>
using namespace std;
int main()
{
    cout << "==========================\n";
    cout << "     LA CRIPTA DEL BIT\n";
    cout << "==========================\n";
    cout << "1.\tNueva partida\n";
    cout << "2.\tContinuar\n";
    cout << "3.\tSalir\n";
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
5. Debe compilar sin errores con `g++ -Wall`.

**Resultado esperado (ejemplo):**

```console title="Ejemplo de salida"
################################
Nombre:     Ana Lopez
Grado:      2o semestre
Lenguaje:   C++
Pasatiempo: videojuegos
"Aprender a programar es aprender a pensar"
################################
```

:::reto | Reto extra
Dibuja tu inicial en grande con asteriscos debajo de la tarjeta (arte ASCII). {{arcs:Satisfacción}}
:::

:::solucion | T4
Hay muchas soluciones correctas; esta es una posible:

```cpp run title="tarjeta_presentacion.cpp"
/* Tarjeta de presentacion
   Autora: Ana Lopez
   Fecha: agosto 2026 */
#include <iostream>
using namespace std;
int main()
{
    cout << "################################\n";
    cout << "Nombre:\t\tAna Lopez\n";
    cout << "Grado:\t\t2o semestre\n";
    cout << "Lenguaje:\tC++\n";
    cout << "Pasatiempo:\tvideojuegos\n";
    cout << "\"Aprender a programar es aprender a pensar\"\n";
    cout << "################################\n";
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

**Tarea de solución libre:** no hay una única respuesta. **Escribe todas las versiones del programa que se te ocurran** para producir exactamente la misma figura. Por ejemplo: un `cout` por renglón, un solo `cout` con varios `\n`, usando `endl`, encadenando con `<<`… Compara tus versiones: ¿cuál es más fácil de leer?, ¿cuál es más corta?

:::solucion | T5
Algunas de las soluciones posibles (todas producen la misma salida):

```cpp run title="version1_un_cout_por_linea.cpp"
#include <iostream>
using namespace std;
int main()
{
    cout << "*\n";
    cout << "**\n";
    cout << "***\n";
    cout << "****\n";
    return 0;
}
```

```cpp run title="version2_un_solo_cout.cpp"
#include <iostream>
using namespace std;
int main()
{
    cout << "*\n**\n***\n****\n";
    return 0;
}
```

```cpp run title="version3_endl_encadenado.cpp"
#include <iostream>
int main()
{
    std::cout << "*" << std::endl << "**" << std::endl
              << "***" << std::endl << "****" << std::endl;
    return 0;
}
```
La versión 1 es la más legible; la 2, la más corta; la 3 muestra que una sentencia puede ocupar varias líneas (el `;` marca el final, no el salto de línea).
:::
:::

:::tarea B | T6. ¿Puedes ayudar a tu compañero? (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
**Contexto.** Un compañero escribió este programa para mostrar el horario del laboratorio, pero no compila. Te pide ayuda porque no entiende los mensajes del compilador.

```cpp blank title="horario_con_errores.cpp"
using namespace std;
int main()
{
    Cout << "HORARIO DE LABORATORIO\n";
    cout << "Lunes:\t\t8:00 - 10:00\n"
    cout << "Miercoles:\t12:00 - 14:00\n;
    cout << "Viernes:\t9:00 - 11:00\n";
    return 0;
}
```

1. Encuentra **los cuatro errores**.
2. Para cada uno, **explica con tus palabras** por qué es un error y qué fase lo detecta.
3. Escribe la versión corregida y compílala.

{{lineas:4}}

:::solucion | T6
1. Falta `#include <iostream>` (línea 1): sin la biblioteca, `cout` no está declarado (**compilación**).
2. `Cout` con mayúscula (línea 4): C++ distingue mayúsculas; el nombre no existe (**compilación**).
3. Falta `;` al final de la línea 5 (**compilación**; el error se reporta en la línea 6).
4. Comillas sin cerrar en la línea 6: `"...\n;` debe ser `"...\n";` (**compilación**).

```cpp run title="horario.cpp"
#include <iostream>
using namespace std;
int main()
{
    cout << "HORARIO DE LABORATORIO\n";
    cout << "Lunes:\t\t8:00 - 10:00\n";
    cout << "Miercoles:\t12:00 - 14:00\n";
    cout << "Viernes:\t9:00 - 11:00\n";
    return 0;
}
```
:::
:::

:::tarea B | T7. Imagina el viaje del programa (imaginación) | 15 min | Imaginación
**Contexto.** Este programa declara una función `saludar` (adelanto del Tema 10) pero nunca la define.

```cpp blank title="viaje.cpp"
#include <iostream>
using namespace std;
void saludar();          // prototipo: "existe una funcion saludar"
int main()
{
    // comentario que desaparece
    saludar();
    return 0;
}
```

**Sin compilarlo**, imagina el recorrido por la cadena de la Figura 1 y responde:

1. ¿Qué le hace el **preprocesador** a las líneas 1 y 6?
2. ¿El **compilador** encuentra algún error? ¿Por qué sí o por qué no?
3. ¿Qué ocurre en el **enlazador**? Escribe el mensaje que esperas ver.
4. Ahora compílalo y compara tu predicción con el mensaje real.

{{lineas:4}}

:::solucion | T7
1. Sustituye la línea 1 por el contenido de `<iostream>` y elimina el comentario de la línea 6.
2. No: la línea 3 (prototipo) le promete al compilador que `saludar` existe, así que la llamada de la línea 7 es válida sintácticamente.
3. El enlazador busca la **definición** de `saludar` para unirla con `main` y no la encuentra:

```cpp err
#include <iostream>
using namespace std;
void saludar();
int main()
{
    saludar();
    return 0;
}
```
Se corrige agregando la definición: `void saludar() { cout << "Hola\n"; }`.
:::
:::

:::tarea AB | T8. La cadena de compilación en vivo (reto colaborativo) | 30 min | Memoria colectiva de trabajo, Movimiento humano
:::colab | Organización
**Equipos de 4, heterogéneos** (al menos un integrante de Ruta B). Roles: **Programador**, **Preprocesador**, **Compilador**, **Enlazador**. Cada integrante procesa solo su parte: así la carga del problema se reparte entre cuatro memorias de trabajo.
:::

:::movimiento | La hoja viaja por el salón
1. El **Programador** escribe en una hoja un programa corto (5–8 líneas) que use `cout` y **una función** declarada con prototipo.
2. Entrega la hoja (físicamente) al **Preprocesador**, que tacha los comentarios y pega una tarjeta que dice «contenido de iostream» sobre cada `#include`.
3. El **Compilador** revisa línea por línea: `;`, llaves, comillas, mayúsculas. Si encuentra un error, marca `línea:columna` y devuelve la hoja al Programador.
4. El **Enlazador** verifica que cada función llamada tenga una definición. Si falta, escribe *undefined reference*.
5. Si la hoja pasa todas las fases, el equipo la escribe en la computadora y la ejecuta. Luego **rotan roles**.
:::

**Producto del equipo:** escriban un programa con **un error de compilación, uno de enlace y uno de lógica** y entréguenlo a otro equipo para que lo depure y explique cada error.

:::solucion | T8
Ejemplo de programa con un error de cada tipo (para el equipo que depura):

- **Compilación:** falta `;` en un `cout`.
- **Enlace:** se llama a `void despedir();` que solo tiene prototipo.
- **Lógica:** el programa debe mostrar «Hoy es lunes» y muestra «Hoy es martes» (compila y corre, pero el resultado es incorrecto).

La depuración se hace en ese orden: primero el compilador, luego el enlazador y, por último, la comparación de la salida con lo esperado.
:::
:::

:::tarea B | T9. Mejora este material (autogestión) | 20 min | Autogestión, Atención dividida, Redundancia
**Contexto.** Un sitio web explica el «Hola mundo» así:

:::autog | Material original (mal diseñado)
*El programa comienza con una directiva al preprocesador que incluye la biblioteca de flujos de entrada y salida, luego se indica el uso del espacio de nombres estándar, después se declara la función principal que devuelve un entero y dentro de su bloque se envía al flujo de salida la cadena literal Hola mundo seguida de un salto de línea y finalmente se devuelve cero. El programa comienza con una directiva al preprocesador…* (el párrafo se repite debajo del código, y el código aparece dos páginas después).
:::

Identifica sus problemas de diseño (atención dividida, redundancia, texto excesivo) y **rediséñalo**: código a la izquierda y una explicación breve pegada a cada línea, sin repetir información. Compara tu versión con la solución.

:::solucion | T9
Problemas: (1) el texto está **separado** del código (atención dividida), (2) el párrafo se **repite** (redundancia), (3) un solo bloque de texto largo sin señalizar qué parte del código explica. Rediseño:

```cpp run title="hola_redisenado.cpp"
#include <iostream>        //> Trae `cout` (biblioteca de E/S)
using namespace std;       //> Permite omitir `std::`
int main()                 //> Aquí empieza la ejecución
{
    cout << "Hola mundo\n";  //> Envía el texto a la pantalla y salta de línea
    return 0;              //> Termina: «todo bien»
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Una experta resuelve un problema nuevo pensando en voz alta | Modalidad, Ejemplo resuelto
*Guion para narración en audio (≈ 3 min). Para evitar el efecto de **información transitoria**, grábalo en 4 segmentos cortos que el estudiante pueda pausar y repetir, mostrando en pantalla el código mientras se escucha (sin el texto del guion, para no generar **redundancia**).*

**Problema:** «Mostrar el recibo de una papelería con tres productos y el total, alineado en columnas».

**Segmento 1 — Planear antes de teclear.** {{como}} Primero dibujo en papel cómo quiero que se vea la salida: un encabezado, tres renglones de producto y precio, y el total. {{porque}} Si no sé qué quiero ver, no sé qué sentencias escribir; cada renglón de la salida será un `cout`.

**Segmento 2 — Esqueleto y primera compilación.** {{como}} Escribo la plantilla: `#include <iostream>`, `using namespace std;`, `int main()`, llaves y `return 0;`. Compilo **ya**, aunque no haga nada. {{porque}} Si hay un error ahora, sé que está en cinco líneas y no en cincuenta.

**Segmento 3 — Agregar de a poco.** {{como}} Agrego el encabezado y compilo; luego los productos con `\t` entre nombre y precio. Veo que «Cuaderno» desalinea la columna porque es más largo, así que a los nombres cortos les pongo dos `\t`. {{porque}} El tabulador salta a la siguiente columna fija (cada 8 caracteres); los textos de distinta longitud necesitan distinto número de saltos.

**Segmento 4 — Leer el error, no adivinarlo.** {{como}} Al compilar aparece `recibo.cpp:9:5: error: expected ';' before 'cout'`. Voy a la línea **9**… pero el `;` que falta está al final de la **8**. {{porque}} El compilador descubre que faltaba el `;` cuando ya está leyendo lo siguiente. Corrijo, compilo y comparo la salida con mi dibujo inicial.

```cpp run title="recibo.cpp"
#include <iostream>
using namespace std;
int main()
{
    cout << "PAPELERIA EL LAPIZ\n";
    cout << "Producto\tPrecio\n";
    cout << "Cuaderno\t$40\n";
    cout << "Lapiz\t\t$8\n";
    cout << "Goma\t\t$6\n";
    cout << "TOTAL\t\t$54\n";
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo (10 reactivos)
1. ¿Cuál es el punto de entrada de todo programa en C++?
   a) `inicio()` · b) `main()` · c) `#include` · d) `cout`
2. ¿Qué biblioteca debe incluirse para usar `cout`?
   a) `<string>` · b) `<cmath>` · c) `<iostream>` · d) `<cstdio>`
3. ¿Qué símbolo marca el final de una sentencia? \_\_\_\_\_
4. Relaciona cada fase con lo que produce: (1) Preprocesamiento, (2) Compilación, (3) Enlace.
   a) Ejecutable · b) Código fuente expandido · c) Código objeto
5. Verdadero o falso: `Cout` y `cout` son el mismo nombre para el compilador.
6. ¿Qué hace la secuencia de escape `\t`?
7. ¿Cómo se escribe un comentario que ocupa varias líneas?
8. El mensaje *undefined reference to main* aparece en la fase de:
   a) edición · b) preprocesamiento · c) compilación · d) enlace
9. ¿Qué significa `return 0;` al final de `main`?
10. Explica en una oración la diferencia entre un error de **sintaxis** y un error de **lógica**.
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida** exacta (marca con ⏎ los saltos de línea):

```cpp check title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    cout << "Uno";
    cout << "Dos\n";
    cout << "Tres" << endl << "Cuatro\n\n";
    cout << "Fin";
    return 0;
}
```

**P2. Corrige** el programa (tiene tres errores) y explica en qué fase se detecta cada uno:

```cpp blank title="p2.cpp"
#include <iostream>
using namespace std
int main()
{
    cout << "Prueba de errores\n";
    cout << "Linea dos\n;
    return 0;
```

**P3. Ordena las líneas** para formar un programa válido que muestre `Listo`:
`}` · `return 0;` · `#include <iostream>` · `{` · `int main()` · `std::cout << "Listo\n";`

**P4. Escribe un programa** que muestre tu horario de clases de un día con tres materias, una por renglón, con la hora y la materia alineadas por `\t`, y un comentario de bloque con tu nombre.
:::

:::registro | 5.3 Autorregistro
Marca lo que ya puedes hacer:
<ul class="checks">
<li>Escribo la plantilla de un programa sin mirar la tarjeta.</li>
<li>Uso <code>cout</code>, <code>\n</code>, <code>endl</code> y <code>\t</code> para dar formato a la salida.</li>
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

```cpp run title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    cout << "Uno";
    cout << "Dos\n";
    cout << "Tres" << endl << "Cuatro\n\n";
    cout << "Fin";
    return 0;
}
```

**P2.** (1) Falta `;` después de `using namespace std` — compilación. (2) Comillas sin cerrar en `"Linea dos\n;` — compilación. (3) Falta la llave de cierre `}` de `main` — compilación.

**P3.** `#include <iostream>` → `int main()` → `{` → `std::cout << "Listo\n";` → `return 0;` → `}`.

**P4.** Ejemplo:

```cpp run title="horario.cpp"
/* Horario del lunes
   Autor: Luis Perez */
#include <iostream>
using namespace std;
int main()
{
    cout << "07:00\tMatematicas\n";
    cout << "09:00\tProgramacion\n";
    cout << "11:00\tFisica\n";
    return 0;
}
```
:::
