---
num: "06"
archivo: "Tema06_Estructuras_repetitivas_while_do_for"
titulo: "Estructuras repetitivas: while, do-while y for"
corto: "while, do-while y for"
lema: "Lo que harías mil veces a mano, la computadora lo repite sin cansarse: solo dile cuándo empezar, qué repetir y cuándo parar."
duracion: "6 h · 3 sesiones de 2 h"
previos: "Tema 04 (condiciones e if) y Tema 03 (asignación compuesta, `++`)."
fuentes:
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Cap. 5: Estructuras repetitivas (§5.1 for, §5.2 while, §5.3 do-while, §5.4 ejercicios)."
  - "Lospinoso, J. (2019). *C++ Crash Course*. Cap. 2: A Nickel Tour of for Loops. Cap. 8: Iteration Statements (while, do-while, for)."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §6.1.13: propuesta de desvanecimiento de guía para ciclos (pares 50–100, factorial, Fibonacci, tabla de multiplicar) y §6.1.1 (solución libre: serie 5, 10, 15…)."
objetivos:
  A:
    - "Identificar las cuatro partes de un ciclo: inicialización, condición, cuerpo y actualización."
    - "Escribir ciclos `while`, `do-while` y `for` y elegir el más adecuado para cada problema."
    - "Aplicar los patrones contador, acumulador, centinela y validación de entrada."
    - "Realizar pruebas de escritorio (tablas de traza) de un ciclo."
  B:
    - "Convertir un ciclo entre sus tres formas y justificar cuál es más claro."
    - "Detectar y corregir ciclos infinitos y errores «por uno» (*off-by-one*)."
    - "Implementar patrones de máximo, mínimo, promedio con centinela y banderas."
    - "Calcular cuántas veces se ejecuta el cuerpo de un ciclo."
efectos:
  soporte:
    - ["Elementos aislados", "Necesidad de repetir → partes del ciclo → while → do-while → for → patrones. Los ciclos anidados quedan para el Tema 07."]
    - ["Atención dividida", "Diagrama de flujo + código + tabla de traza integrados para cada ciclo."]
    - ["Ejemplo resuelto", "Pares de 50 a 100 con Mientras/Para (PSeInt) y while/for (C++), según la tesis (§6.1.13, fase 1)."]
    - ["Movimiento humano", "«Vueltas a la pista»: un estudiante camina, otro cuenta y otro acumula."]
  procedimental:
    - ["Variabilidad", "Errores típicos de ciclos en contextos distintos."]
    - ["Autogestión", "T9: rediseñar una explicación de `for` mal diseñada."]
  tareas:
    - ["Problema por completar", "T2 factorial (con pistas) y T3 Fibonacci (sin pistas), como en la tesis §6.1.13, fase 2."]
    - ["Desvanecimiento de guía", "T1 (resuelto) → T2 → T3 → T4 (tabla de multiplicar, problema completo, fase 3)."]
    - ["Solución libre", "T5: sumar la serie 5, 10, 15… hasta 100 con todas las estructuras posibles (tesis §6.1.1)."]
    - ["Autoexplicación", "T4 y T6: explicar paso a paso; encontrar errores en ciclos."]
    - ["Imaginación", "T7: imaginar la traza de un ciclo que separa dígitos."]
    - ["Memoria colectiva de trabajo", "T8: cajero automático con menú repetitivo."]
    - ["Autogestión", "T9: mejorar material mal diseñado (Ruta B)."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Las tres formas de ciclo con trazas completas y diagramas."
    B: "Conversión entre formas, conteo de iteraciones, banderas, *off-by-one*."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "Secuencia de desvanecimiento T1 → T4 tal como la propone la tesis; pares mixtos."
    B: "T5 (todas las variantes), T6, T7, T9 autónomas; líderes de integración en T8."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Tabla de multiplicar en `while` y `for` con explicación paso a paso (T4)."
    B: "Material rediseñado (T9) y análisis de errores (T6)."
  Entorno:
    comp: "Información procedimental"
    A: "Depurador paso a paso para observar cómo cambia la variable de control."
    B: "Terminal; uso de `Ctrl+C` para detener ciclos infinitos y `-Wall` para `;` sospechosos."
plan:
  - ["Sesión 1 · apertura", "Soporte", "Escribir 1..5 «a mano» y luego 1..1000: ¿por qué necesitamos ciclos?", "10 min"]
  - ["Sesión 1 · desarrollo", "Soporte", "Conceptos 1–5, vueltas a la pista, ejemplo resuelto (pares 50–100).", "60 min"]
  - ["Sesión 1 · práctica", "Tareas", "T1 (todos), T2 (Ruta A); Ruta B: T6.", "50 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–8 (patrones); T3, T4; Ruta B: T7, T9.", "120 min"]
  - ["Sesión 3", "Tareas + evaluación", "T5, T8 colaborativa, protocolo verbal, tests y autorregistro.", "120 min"]
glosario:
  - ["ciclo / bucle", "loop", "Estructura que repite un bloque de sentencias."]
  - ["iteración", "iteration", "Cada repetición del cuerpo de un ciclo."]
  - ["variable de control", "loop variable", "Variable que decide cuándo termina el ciclo (p. ej., `i`)."]
  - ["contador", "counter", "Variable que aumenta en una cantidad fija (`cont++`)."]
  - ["acumulador", "accumulator", "Variable que va sumando o multiplicando valores (`suma += x`)."]
  - ["centinela", "sentinel value", "Valor especial que indica el fin de los datos (p. ej., −1)."]
  - ["bandera", "flag", "Variable `bool` que recuerda si algo ocurrió."]
  - ["ciclo infinito", "infinite loop", "Ciclo cuya condición nunca se vuelve falsa."]
  - ["error por uno", "off-by-one error", "Repetir una vez de más o de menos (`<` vs `<=`)."]
  - ["prueba de escritorio / traza", "trace table / desk check", "Tabla con el valor de cada variable en cada iteración."]
  - ["ciclo precondicional", "pre-test loop (`while`, `for`)", "Evalúa la condición antes de cada iteración; puede no ejecutarse nunca."]
  - ["ciclo poscondicional", "post-test loop (`do-while`)", "Evalúa la condición al final; se ejecuta al menos una vez."]
---

# 1. Información de soporte {.soporte}

:::analogia | Vueltas a la pista
En la clase de educación física el profesor dice: «**Mientras** no completes 5 vueltas, sigue corriendo». Hay un **punto de partida** (vuelta 0), una **pregunta** que se hace en cada paso por la meta (¿ya van 5?), una **acción** que se repite (correr una vuelta) y algo que **cambia** cada vez (el número de vueltas). Si nadie contara las vueltas, correrías para siempre. Un ciclo en C++ tiene exactamente esas cuatro partes.
:::

:::pregunta
Escribe en papel un programa que muestre los números del 1 al 5 con lo que ya sabes. Ahora imagina que te piden del 1 al 1000. **¿Qué parte de tu programa se repite? ¿Qué cambia de una línea a otra?**

{{lineas:2}}
:::

:::relevancia
Un videojuego repite su «ciclo principal» 60 veces por segundo; una hoja de cálculo suma miles de celdas; un cajero repite su menú hasta que eliges «Salir»; un sensor Arduino lee la temperatura cada segundo. Como dice el modelo ARCS, **los ciclos ahorran tiempo y esfuerzo al escribir código profesional** y son la base de juegos y sitios interactivos. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | La necesidad de repetir | Elementos aislados, Atención dividida
<div class="cols eq">
<div>

```cpp run title="sin ciclo"
#include <iostream>
using namespace std;
int main()
{
    cout << 1 << "\n";
    cout << 2 << "\n";
    cout << 3 << "\n";
    cout << 4 << "\n";
    cout << 5 << "\n";
    return 0;
}
```

</div>
<div>

```cpp run title="con ciclo"
#include <iostream>
using namespace std;
int main()
{
    int i = 1;
    while (i <= 5)
    {
        cout << i << "\n";
        i++;
    }
    return 0;
}
```

</div>
</div>

Las dos producen lo mismo. Pero para llegar a 1000, a la izquierda tendrías que escribir 995 líneas más; a la derecha solo cambias `5` por `1000`.
:::

:::concepto | 2 | Las cuatro partes de un ciclo y el `while` | Elementos aislados, Atención dividida
<div class="cols">
<div>

```cpp run title="cuenta.cpp"
#include <iostream>
using namespace std;
int main()
{
    int i = 1;                //> ① **Inicialización**: valor de partida
    while (i <= 5)            //> ② **Condición**: se evalúa ANTES de cada vuelta
    {
        cout << i << " ";     //> ③ **Cuerpo**: lo que se repite
        i++;                  //> ④ **Actualización**: acerca el ciclo a su fin
    }
    cout << "\nFin, i = " << i << "\n";  //> Al salir, i vale 6
    return 0;
}
```

</div>
<div>

```dot
rankdir=TB; nodesep=0.3; ranksep=0.22;
@proc(ini, "① i ← 1")
@dec(c, "② i <= 5?")
@proc(b, "③ mostrar i")
@proc(u, "④ i ← i + 1")
@io(f, "Fin")
ini -> c; c -> b [label=" Sí"]; b -> u; u -> c [constraint=false]; c -> f [label=" No"];
```

</div>
</div>

<div class="traza" markdown="1">

| Vuelta | `i` al evaluar | ¿`i <= 5`? | Muestra | `i` después |
|---|---|---|---|---|
| 1 | 1 | true | 1 | 2 |
| 2 | 2 | true | 2 | 3 |
| 3 | 3 | true | 3 | 4 |
| 4 | 4 | true | 4 | 5 |
| 5 | 5 | true | 5 | 6 |
| — | 6 | **false** | (sale) | — |

</div>

La tabla de traza (prueba de escritorio) es tu mejor herramienta para entender un ciclo: el cuerpo se ejecutó **5 veces** y la condición se evaluó **6**.
:::

:::concepto | 3 | El ciclo infinito: olvidar la actualización | Elementos aislados
Si el cuerpo nunca cambia la variable de la condición, la condición nunca se vuelve falsa:

```cpp blank title="infinito.cpp (¡no lo ejecutes sin saber detenerlo!)"
int i = 1;
while (i <= 5)
{
    cout << i << " ";   // falta i++: siempre muestra 1
}
```
Si te ocurre, detén el programa con **Ctrl + C** en la terminal (o el botón «detener» del IDE).
:::

:::movimiento | Vueltas a la pista (10 min)
Tres voluntarios: el **corredor** (cuerpo del ciclo), el **contador** (actualización: anota cada vuelta en el pizarrón) y el **juez** (condición: antes de cada vuelta pregunta en voz alta «¿vueltas menor que 4?»). En la segunda ronda el juez pregunta **al terminar** cada vuelta (eso es `do-while`). Prueben con «vueltas menor que 0»: ¿el corredor da alguna vuelta en cada versión?
:::

:::concepto | 4 | `do-while`: primero actúa, luego pregunta | Elementos aislados, Atención dividida
El `do-while` evalúa la condición **al final**: el cuerpo se ejecuta **al menos una vez**. Es perfecto para **validar** datos («pide el dato mientras sea inválido»).

<div class="cols">
<div>

```cpp run title="valida_edad.cpp" stdin="-4\n150\n17\n"
#include <iostream>
using namespace std;
int main()
{
    int edad;
    do
    {
        cout << "Edad (0-120): ";        //> Se pregunta al menos una vez
        cin >> edad;
    } while (edad < 0 || edad > 120);    //> Repite MIENTRAS sea inválida. ¡Lleva `;`!
    cout << "Edad registrada: " << edad << "\n";
    return 0;
}
```

</div>
<div>

```dot
rankdir=TB; nodesep=0.3; ranksep=0.22;
@io(l, "Pedir y leer edad")
@dec(c, "edad inválida?")
@io(f, "Mostrar edad")
l -> c; c -> l [label=" Sí"]; c -> f [label=" No"];
```

</div>
</div>
:::

:::concepto | 5 | `for`: el ciclo con contador, en una sola línea | Elementos aislados, Atención dividida
Cuando sabes **cuántas veces** repetir, `for` reúne las partes ①, ② y ④ en su encabezado:

```cpp run title="for.cpp"
#include <iostream>
using namespace std;
int main()
{
    for (int i = 1; i <= 5; i++)    //> `for (① inicialización; ② condición; ④ actualización)`
    {
        cout << i << " ";           //> ③ cuerpo
    }
    cout << "\n";
    for (int j = 10; j >= 0; j -= 2)  //> También puede contar hacia atrás y de 2 en 2
        cout << j << " ";
    cout << "\n";
    return 0;
}
```

| `while` | `for` equivalente |
|---|---|
| `int i = 1;`<br>`while (i <= 5) {`<br>`    cout << i;`<br>`    i++;`<br>`}` | `for (int i = 1; i <= 5; i++) {`<br>`    cout << i;`<br>`}` |

En el `for`, la variable `i` declarada en el encabezado **solo existe dentro del ciclo**.
:::

:::concepto | 6 | Patrones: contador y acumulador | Elementos aislados, Atención dividida
Dos variables que aparecen en casi todos los ciclos:

- **Contador:** aumenta en una cantidad fija → `cuantos++`.
- **Acumulador:** va sumando (o multiplicando) valores → `suma += x;` (empieza en 0) · `producto *= x;` (empieza en 1).

```cpp run title="promedio.cpp" stdin="5\n8 9.5 7 10 6.5\n"
#include <iostream>
using namespace std;
int main()
{
    int n;
    double nota, suma = 0;                 //> El acumulador SIEMPRE se inicializa (0 para sumas)
    int aprobadas = 0;                     //> Contador inicializado en 0
    cout << "Cuantas notas? ";
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> nota;
        suma += nota;                      //> Acumula
        if (nota >= 6) aprobadas++;        //> Cuenta solo las que cumplen
    }
    cout << "Promedio: " << suma / n << "  Aprobadas: " << aprobadas << "\n";
    return 0;
}
```
:::

:::concepto | 7 | Patrón centinela: «hasta que escriba −1» | Elementos aislados
Cuando **no** se sabe cuántos datos habrá, se pide un valor especial que marca el final:

```cpp run title="centinela.cpp" stdin="120\n80.5\n45\n-1\n"
#include <iostream>
using namespace std;
int main()
{
    double gasto, total = 0;
    int cuantos = 0;
    cout << "Gasto (-1 para terminar): ";
    cin >> gasto;                       //> Lectura ANTES del ciclo
    while (gasto != -1)                 //> El centinela no se procesa
    {
        total += gasto;
        cuantos++;
        cout << "Gasto (-1 para terminar): ";
        cin >> gasto;                   //> Lectura al FINAL del cuerpo
    }
    cout << cuantos << " gastos, total $" << total << "\n";
    return 0;
}
```
:::

:::concepto | 8 | ¿Qué ciclo elijo? | Elementos aislados
| Si… | Usa | Ejemplo |
|---|---|---|
| sabes cuántas veces repetir | `for` | tabla de multiplicar, 1 a n |
| repites mientras se cumpla algo y quizá **ninguna** vez | `while` | centinela, leer hasta fin de datos |
| debes ejecutar **al menos una vez** | `do-while` | validar entrada, menú «¿otra vez?» |

En PSeInt: `Para i <- 1 Hasta n Con Paso 1 Hacer … FinPara`, `Mientras cond Hacer … FinMientras`, `Repetir … Hasta Que cond` (¡ojo: el `Repetir` de PSeInt termina cuando la condición es **verdadera**, al revés que `do-while`!).
:::

## 1.2 Ejemplo resuelto: números pares de 50 a 100

:::ejemplo | Pares entre 50 y 100 con Mientras/Para y while/for (tesis, §6.1.13, fase 1) | Ejemplo resuelto, Atención dividida
**Problema.** Crear dos algoritmos en PSeInt que muestren los números pares comprendidos entre 50 y 100, usando `Mientras` y `Para`. Después, pasarlos a C++ con `while` y `for`.

**A. Algoritmo:** 1) Empezar en 50 (primer par). 2) Mientras no pase de 100: mostrar el número y sumarle 2. 3) Terminar.

<div class="cols eq">
<div>

```pseudo title="Mientras"
Algoritmo ParesMientras
    Definir n Como Entero
    n <- 50
    Mientras n <= 100 Hacer
        Escribir n
        n <- n + 2
    FinMientras
FinAlgoritmo
```

</div>
<div>

```pseudo title="Para"
Algoritmo ParesPara
    Definir n Como Entero
    Para n <- 50 Hasta 100 Con Paso 2 Hacer
        Escribir n
    FinPara
FinAlgoritmo
```

</div>
</div>

**C. Código en C++**

```cpp run title="pares_while.cpp"
#include <iostream>
using namespace std;
int main()
{
    int n = 50;                 //> Inicialización: el primer par del rango
    while (n <= 100)            //> Condición: hasta 100 inclusive
    {
        cout << n << " ";       //> Cuerpo
        n += 2;                 //> Actualización de 2 en 2: así solo visitamos pares
    }
    cout << "\n";
    return 0;
}
```

```cpp run title="pares_for.cpp"
#include <iostream>
using namespace std;
int main()
{
    for (int n = 50; n <= 100; n += 2)   //> Las tres partes en el encabezado
        cout << n << " ";
    cout << "\n";
    return 0;
}
```

**D. Verificación.** Se muestran 26 números (50, 52, …, 100). ¿Por qué 26? Del 50 al 100 hay 51 enteros; la mitad redondeada hacia arriba son pares porque ambos extremos lo son. Otra forma de resolverlo: recorrer **todos** los números y mostrar solo los que cumplan `n % 2 == 0`; funciona, pero hace el doble de vueltas.
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.18; ranksep=0.3;
@term(c, "Ciclo")
@proc(p, "4 partes:\ninicialización · condición\ncuerpo · actualización")
@proc(w, "while\n(pregunta antes)")
@proc(d, "do-while\n(pregunta después,\n≥ 1 vez)")
@proc(f, "for\n(contador conocido)")
@sub(pt, "Patrones: contador · acumulador\ncentinela · validación")
@hl(e, "Cuidado: ciclo infinito\nerror por uno · ; tras for")
c -> p; c -> w; c -> d; c -> f; w -> pt [style=dashed]; f -> pt [style=dashed]; d -> pt [style=dashed]; c -> e [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1
```cpp run title="tres_ciclos.cpp"
#include <iostream>
using namespace std;
int main()
{
    // while: pregunta antes
    int i = 0;
    while (i < 3) { cout << "w" << i << " "; i++; }
    // do-while: pregunta despues (lleva ; al final)
    int j = 0;
    do { cout << "d" << j << " "; j++; } while (j < 3);
    // for: inicializacion; condicion; actualizacion
    for (int k = 0; k < 3; k++) { cout << "f" << k << " "; }
    cout << "\n";
    return 0;
}
```

| Para repetir… | Encabezado |
|---|---|
| n veces (de 1 a n) | `for (int i = 1; i <= n; i++)` |
| n veces (de 0 a n−1) | `for (int i = 0; i < n; i++)` |
| hacia atrás de n a 1 | `for (int i = n; i >= 1; i--)` |
| de 5 en 5 hasta 100 | `for (int x = 5; x <= 100; x += 5)` |
| hasta centinela | `cin >> x; while (x != -1) { …; cin >> x; }` |
| hasta dato válido | `do { cin >> x; } while (x < 0);` |
| menú repetido | `do { …menú…; cin >> op; switch(op){…} } while (op != 0);` |
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿Identifiqué las 4 partes? ¿Dónde se inicializa, qué condición, qué se repite y qué cambia?</li>
<li>¿La actualización acerca la variable a que la condición sea falsa? (Si no: ciclo infinito.)</li>
<li>¿Uso <code>&lt;</code> o <code>&lt;=</code>? Pruébalo con el primer y el último valor (error por uno).</li>
<li>¿Inicialicé los acumuladores (0 para sumas, 1 para productos) y contadores <b>antes</b> del ciclo?</li>
<li>¿Hay un <code>;</code> justo después de <code>for (…)</code> o <code>while (…)</code>? (No debe haberlo.)</li>
<li>¿El <code>do-while</code> termina en <code>while (…);</code>?</li>
<li>¿Hice la traza con un caso pequeño (2 o 3 vueltas)?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Punto y coma después del `for`.** ¿Por qué solo se muestra un número?

```cpp run
#include <iostream>
using namespace std;
int main()
{
    int i;
    for (i = 1; i <= 5; i++);        //> El `;` es el cuerpo (vacío): el ciclo da 5 vueltas sin hacer nada
    {
        cout << "Valor: " << i << "\n";  //> Esto se ejecuta UNA vez, después, con i = 6
    }
    return 0;
}
```

**b) Error por uno.** Se pidieron 10 números y aparecen 11 (o 9):

```cpp run
#include <iostream>
using namespace std;
int main()
{
    for (int i = 0; i <= 10; i++)    //> De 0 a 10 inclusive son ONCE vueltas
        cout << i << " ";
    cout << "\n";
    return 0;
}
```
*Corrección:* `for (int i = 1; i <= 10; i++)` o `for (int i = 0; i < 10; i++)`.

**c) Acumulador sin inicializar o inicializado dentro del ciclo.** `double suma;` contiene basura; y `for (…) { double suma = 0; suma += x; }` lo reinicia en cada vuelta. Declara e inicializa **antes** del ciclo.

**d) Condición que nunca cambia.** `while (n > 0) { cout << n; }` sin `n--`: ciclo infinito.

**e) Usar la variable del `for` fuera de él.**

```cpp err
#include <iostream>
int main()
{
    for (int i = 0; i < 3; i++)
        std::cout << i;
    std::cout << "Ultimo: " << i;
    return 0;
}
```
*Corrección:* declara `int i;` antes del `for` si necesitas su valor al final.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Cuenta regresiva de lanzamiento | Variabilidad
Mismo patrón (contador con for), otro contexto y otra dirección:

```cpp run title="despegue.cpp"
#include <iostream>
using namespace std;
int main()
{
    for (int t = 10; t >= 1; t--)     //> Empieza en 10, baja de 1 en 1, termina en 1
        cout << t << "... ";
    cout << "DESPEGUE!\n";
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

Esta secuencia sigue la propuesta de **desvanecimiento de guía** de la tesis (§6.1.13): fase 1 ejemplo resuelto → fase 2 problemas por completar (primero con ayuda, después con más huecos y sin ayuda) → fase 3 problema completo. {{ef:Desvanecimiento de guía}}

:::tarea A | T1. Múltiplos de 5 (gemelo del ejemplo resuelto) | 20 min | Ejemplo resuelto, Variabilidad
**Contexto.** Estudia de nuevo el ejemplo 1.2 (pares de 50 a 100). Ahora resuelve su **gemelo**: escribe dos algoritmos en PSeInt (`Mientras` y `Para`) y dos programas en C++ (`while` y `for`) que muestren los **múltiplos de 5 entre 1 y 100**.

**Resultado esperado:** `5 10 15 … 100` (20 números).

:::solucion | T1
```cpp run title="multiplos5.cpp"
#include <iostream>
using namespace std;
int main()
{
    int m = 5;                          // version while
    while (m <= 100)
    {
        cout << m << " ";
        m += 5;
    }
    cout << "\n";
    for (int k = 5; k <= 100; k += 5)   // version for
        cout << k << " ";
    cout << "\n";
    return 0;
}
```
En PSeInt: `m <- 5; Mientras m <= 100 Hacer Escribir m; m <- m + 5; FinMientras` y `Para m <- 5 Hasta 100 Con Paso 5 Hacer Escribir m; FinPara`.
:::
:::

:::tarea A | T2. Factorial (fase 2a: completa con ayuda en comentarios) | 25 min | Problema por completar
**Contexto.** El factorial de `n` es `n! = 1 · 2 · 3 · … · n` (y `0! = 1`). Se usa para contar combinaciones: ¿de cuántas formas se pueden ordenar 5 libros? `5! = 120`. Completa la versión `while` y la versión `for`.

```cpp blank title="factorial.cpp"
#include <iostream>
using namespace std;
int main()
{
    int n;
    cout << "Numero: ";
    cin >> n;
    // Version while
    long long fact = __1__;          // 1: valor inicial de un acumulador de PRODUCTOS
    int i = 1;
    while (i __2__ n)                // 2: ¿hasta n inclusive?
    {
        fact __3__ i;                // 3: acumula multiplicando
        i++;
    }
    cout << "while: " << n << "! = " << fact << "\n";
    // Version for
    long long f2 = 1;
    for (int k = 1; __4__; __5__)    // 4: condicion  5: actualizacion
        f2 *= k;
    cout << "for:   " << n << "! = " << f2 << "\n";
    return 0;
}
```

:::solucion | T2
{{c:1}} `1` · {{c:2}} `<=` · {{c:3}} `*=` · {{c:4}} `k <= n` · {{c:5}} `k++`

```cpp run title="factorial.cpp" runs="5|0|15"
#include <iostream>
using namespace std;
int main()
{
    int n;
    cout << "Numero: ";
    cin >> n;
    long long fact = 1;
    int i = 1;
    while (i <= n)
    {
        fact *= i;
        i++;
    }
    cout << "while: " << n << "! = " << fact << "\n";
    long long f2 = 1;
    for (int k = 1; k <= n; k++)
        f2 *= k;
    cout << "for:   " << n << "! = " << f2 << "\n";
    return 0;
}
```
Observa que con `n = 0` el ciclo no se ejecuta y el resultado queda en 1: correcto, porque `0! = 1`. Se usa `long long` porque `15!` no cabe en `int`.
:::
:::

:::tarea AB | T3. Serie de Fibonacci (fase 2b: más huecos, sin ayuda) | 25 min | Problema por completar, Desvanecimiento de guía
**Contexto.** En la serie de Fibonacci cada término es la suma de los dos anteriores: `0 1 1 2 3 5 8 13…`. Aparece en la naturaleza (espirales de girasoles) y en algoritmos. Muestra los primeros `n` términos, con `while` y con `for`.

```cpp blank title="fibonacci.cpp"
#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    long long a = 0, b = 1;
    int cont = 0;
    while (__1__)
    {
        cout << a << " ";
        long long sig = __2__;
        a = __3__;
        b = __4__;
        __5__;
    }
    cout << "\n";
    long long x = 0, y = 1;
    for (__6__; __7__; __8__)
    {
        cout << x << " ";
        long long s = x + y;
        x = y;
        y = s;
    }
    cout << "\n";
    return 0;
}
```

:::solucion | T3
{{c:1}} `cont < n` · {{c:2}} `a + b` · {{c:3}} `b` · {{c:4}} `sig` · {{c:5}} `cont++` · {{c:6}} `int i = 0` · {{c:7}} `i < n` · {{c:8}} `i++`

```cpp run title="fibonacci.cpp" stdin="12\n"
#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    long long a = 0, b = 1;
    int cont = 0;
    while (cont < n)
    {
        cout << a << " ";
        long long sig = a + b;
        a = b;
        b = sig;
        cont++;
    }
    cout << "\n";
    long long x = 0, y = 1;
    for (int i = 0; i < n; i++)
    {
        cout << x << " ";
        long long s = x + y;
        x = y;
        y = s;
    }
    cout << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T4. Tabla de multiplicar (fase 3: problema completo + autoexplicación) | 30 min | Autoexplicación, Desvanecimiento de guía
**Contexto.** Genera los algoritmos en PSeInt para imprimir la **tabla de multiplicar** de un número dado por el usuario (del 1 al 10) usando `Mientras` y `Para`. Después pásalos a C++ con `while` y `for`. **Sin código de apoyo.**

**Autoexplicación:** al terminar, escribe paso a paso, con tus palabras, qué hace cada parte de tu ciclo y por qué termina.

```console title="Ejemplo de salida para 7"
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

{{lineas:3}}

:::solucion | T4
```cpp run title="tabla.cpp" stdin="7\n"
#include <iostream>
using namespace std;
int main()
{
    int num;
    cout << "Numero: ";
    cin >> num;
    int i = 1;                       // version while
    while (i <= 10)
    {
        cout << num << " x " << i << " = " << num * i << "\n";
        i++;
    }
    cout << "--- version for ---\n";
    for (int k = 1; k <= 10; k++)
        cout << num << " x " << k << " = " << num * k << "\n";
    return 0;
}
```
Autoexplicación esperada (ejemplo): «`i` empieza en 1 porque la tabla empieza en ×1; la condición `i <= 10` permite llegar al ×10; en cada vuelta se muestra el producto y se incrementa `i`; cuando `i` vale 11 la condición es falsa y el ciclo termina».
:::
:::

:::tarea A | T5. La serie 5, 10, 15… (solución libre, tesis §6.1.1) | 25 min | Solución libre, Variabilidad
**Contexto.** «Crea **todos los algoritmos posibles** para sumar la serie 5, 10, 15, 20… hasta 100, utilizando **todas las estructuras repetitivas** que te sea posible». No hay un solo camino correcto: mientras más versiones escribas (y verifiques que dan lo mismo), mejor.

:::solucion | T5
Todas deben dar **1050**. Algunas versiones:

```cpp run title="serie.cpp"
#include <iostream>
using namespace std;
int main()
{
    int s1 = 0;                                  // 1) for de 5 en 5
    for (int x = 5; x <= 100; x += 5) s1 += x;
    int s2 = 0, x2 = 5;                          // 2) while
    while (x2 <= 100) { s2 += x2; x2 += 5; }
    int s3 = 0, x3 = 5;                          // 3) do-while
    do { s3 += x3; x3 += 5; } while (x3 <= 100);
    int s4 = 0;                                  // 4) recorrer 1..100 y filtrar multiplos
    for (int k = 1; k <= 100; k++) if (k % 5 == 0) s4 += k;
    int s5 = 0;                                  // 5) contar terminos: 5*1 + 5*2 + ... + 5*20
    for (int k = 1; k <= 20; k++) s5 += 5 * k;
    int s6 = 5 * (20 * 21 / 2);                  // 6) sin ciclo: formula de Gauss
    cout << s1 << " " << s2 << " " << s3 << " " << s4 << " " << s5 << " " << s6 << "\n";
    return 0;
}
```
:::
:::

:::tarea B | T6. Cuatro ciclos con errores (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
Cada fragmento debería mostrar `1 2 3 4 5`. **Sin ejecutarlos**, explica qué hace realmente cada uno y por qué, y corrígelo.

```cpp blank title="errores_ciclos.cpp"
// A
int i = 1;
while (i <= 5)
    cout << i << " ";
    i++;
// B
for (int j = 1; j < 5; j++)
    cout << j << " ";
// C
int k = 1;
do {
    cout << k << " ";
} while (k <= 5);
// D
int suma;
for (int m = 1; m <= 5; m++)
    suma += m;
cout << suma;   // deberia mostrar 15
```

{{lineas:4}}

:::solucion | T6
**A:** sin llaves, el `while` solo controla `cout`; `i++` está fuera → ciclo infinito mostrando `1`. **B:** `j < 5` da cuatro vueltas (`1 2 3 4`): error por uno → `j <= 5`. **C:** falta `k++` dentro del `do` → infinito. **D:** `suma` sin inicializar contiene basura → `int suma = 0;`.

```cpp run title="corregidos.cpp"
#include <iostream>
using namespace std;
int main()
{
    int i = 1;
    while (i <= 5) { cout << i << " "; i++; }
    cout << "\n";
    for (int j = 1; j <= 5; j++) cout << j << " ";
    cout << "\n";
    int k = 1;
    do { cout << k << " "; k++; } while (k <= 5);
    cout << "\n";
    int suma = 0;
    for (int m = 1; m <= 5; m++) suma += m;
    cout << suma << "\n";
    return 0;
}
```
:::
:::

:::tarea B | T7. Separar los dígitos (imaginación) | 25 min | Imaginación
**Contexto.** Este programa usa `% 10` (último dígito) y `/ 10` (quitar el último dígito). **Imagina** su ejecución con `n = 4072` y completa la tabla de traza **antes** de ejecutarlo. Después modifícalo para que también muestre el número **al revés** (2704).

```cpp check title="digitos.cpp"
#include <iostream>
using namespace std;
int main()
{
    int n, suma = 0, cuantos = 0;
    cin >> n;
    while (n > 0)
    {
        int d = n % 10;
        suma += d;
        cuantos++;
        n /= 10;
    }
    cout << cuantos << " digitos, suman " << suma << "\n";
    return 0;
}
```

<div class="traza" markdown="1">

| Vuelta | `n` al inicio | `d` | `suma` | `cuantos` | `n` al final |
|---|---|---|---|---|---|
| 1 | 4072 | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

</div>

:::solucion | T7
Traza: (4072, 2, 2, 1, 407) → (407, 7, 9, 2, 40) → (40, 0, 9, 3, 4) → (4, 4, 13, 4, 0). Con `n = 0` la condición es falsa. Versión ampliada:

```cpp run title="digitos_reves.cpp" stdin="4072\n"
#include <iostream>
using namespace std;
int main()
{
    int n, suma = 0, cuantos = 0, reves = 0;
    cin >> n;
    while (n > 0)
    {
        int d = n % 10;
        suma += d;
        cuantos++;
        reves = reves * 10 + d;   // desplaza y agrega el digito
        n /= 10;
    }
    cout << cuantos << " digitos, suman " << suma << ", al reves: " << reves << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T8. El cajero automático, ahora sin cerrar (reto colaborativo) | 35 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Retomen el cajero del Tema 05 (T8). Equipos de 4 con niveles mezclados. **Integrante 1:** envuelve el menú en un `do-while` que se repite hasta elegir 4 (Salir). **Integrante 2:** valida con `do-while` que el monto de depósito sea positivo. **Integrante 3:** cuenta cuántas operaciones exitosas se hicieron (contador). **Integrante 4:** acumula el total depositado y el total retirado (acumuladores) y los muestra al salir. Cada uno explica su parte antes de integrar.
:::

:::solucion | T8
```cpp run title="cajero_ciclo.cpp" stdin="1\n2\n-50\n300\n3\n1000\n1\n4\n"
#include <iostream>
using namespace std;
int main()
{
    double saldo = 2500, monto, totDep = 0, totRet = 0;
    int op, operaciones = 0;
    do
    {
        cout << "\n1) Saldo 2) Depositar 3) Retirar 4) Salir: ";
        cin >> op;
        switch (op)
        {
            case 1:
                cout << "Saldo: $" << saldo << "\n";
                operaciones++;
                break;
            case 2:
                do {
                    cout << "Monto a depositar: ";
                    cin >> monto;
                } while (monto <= 0);
                saldo += monto; totDep += monto; operaciones++;
                break;
            case 3:
                cout << "Monto a retirar: ";
                cin >> monto;
                if (monto > 0 && monto <= saldo) { saldo -= monto; totRet += monto; operaciones++; }
                else cout << "Retiro no permitido\n";
                break;
            case 4:
                break;
            default:
                cout << "Opcion invalida\n";
        }
    } while (op != 4);
    cout << "Operaciones: " << operaciones << "  Depositado: $" << totDep
         << "  Retirado: $" << totRet << "  Saldo final: $" << saldo << "\n";
    return 0;
}
```
:::
:::

:::tarea B | T9. Mejora este material sobre `for` (autogestión) | 20 min | Autogestión, Atención dividida, Redundancia, Información transitoria
**Contexto.** Un video de internet explica el `for` así: muestra el código 5 segundos, luego lo quita y aparece un diagrama de flujo sin relación visual con el código; mientras tanto, una voz lee **exactamente** el mismo texto que aparece escrito en pantalla, y todo pasa sin poder pausar.

1. Identifica los problemas usando los efectos que conoces (**atención dividida, redundancia, información transitoria**).
2. Diseña una versión mejorada **en papel**: ¿qué integrarías?, ¿qué eliminarías?, ¿cómo segmentarías?
3. Compara tu diseño con el concepto 2 de este material.

:::solucion | T9
Problemas: (a) **atención dividida**: código y diagrama aparecen separados en el tiempo y el espacio; (b) **redundancia**: la narración repite el texto escrito; (c) **información transitoria**: el código desaparece antes de procesarlo y no hay control del ritmo. Mejoras: mostrar código y diagrama **juntos**, numerar las partes ①–④ en ambos (señalización), usar narración **o** texto (no ambos), dividir el video en segmentos breves con pausa, y dejar el código en pantalla todo el tiempo. El concepto 2 aplica precisamente esas estrategias: código anotado, diagrama al lado y tabla de traza permanente.
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Promedio de un grupo con centinela y validación | Modalidad, Ejemplo resuelto
*Guion segmentado (≈ 4 min), con el código y una tabla de traza en pantalla.*

**Problema:** «Leer calificaciones (0 a 10) hasta que el usuario escriba −1; rechazar valores fuera de rango; al final mostrar cuántas se registraron, el promedio y la más alta».

**Segmento 1 — Elegir el ciclo.** {{como}} No sé cuántas calificaciones habrá, así que descarto `for` y uso `while` con centinela. {{porque}} `for` es para cuando conozco el número de vueltas; aquí lo decide el usuario.

**Segmento 2 — Las variables del patrón.** {{como}} Declaro `suma = 0` (acumulador), `cuantas = 0` (contador) y `mayor = -1` (para el máximo, cualquier nota válida será mayor). {{porque}} Si no los inicializo antes del ciclo, sumaría a basura; si los inicializo dentro, se reiniciarían en cada vuelta.

**Segmento 3 — Validar sin romper el centinela.** {{como}} Dentro del ciclo uso un `if`: si la nota está fuera de 0..10 muestro «inválida» y **no** la cuento; luego vuelvo a leer. {{porque}} El −1 es especial: lo revisa la condición del `while` antes de entrar al cuerpo, así que nunca llega al `if` de validación.

**Segmento 4 — El caso borde.** {{como}} Antes de dividir pregunto `if (cuantas > 0)`. Pruebo con `8 11 9.5 6 -1` y también con `-1` directo. {{porque}} Si el usuario no captura nada, `suma / cuantas` dividiría entre cero; probar el caso vacío es tan importante como probar el normal.

```cpp run title="grupo.cpp" runs="8\n11\n9.5\n6\n-1|-1"
#include <iostream>
using namespace std;
int main()
{
    double nota, suma = 0, mayor = -1;
    int cuantas = 0;
    cout << "Calificacion (-1 termina): ";
    cin >> nota;
    while (nota != -1)
    {
        if (nota < 0 || nota > 10)
            cout << "Invalida, se ignora\n";
        else
        {
            suma += nota;
            cuantas++;
            if (nota > mayor) mayor = nota;
        }
        cout << "Calificacion (-1 termina): ";
        cin >> nota;
    }
    if (cuantas > 0)
        cout << cuantas << " registradas, promedio " << suma / cuantas
             << ", mayor " << mayor << "\n";
    else
        cout << "No se registraron calificaciones\n";
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. Menciona las cuatro partes de un ciclo.
2. ¿Qué ciclo se ejecuta al menos una vez?
3. ¿Cuántas veces se ejecuta el cuerpo de `for (int i = 0; i < 10; i++)`?
4. ¿Con qué valor se inicializa un acumulador de productos?
5. ¿Qué es un valor centinela?
6. Verdadero o falso: en `for (int i = 0; …)` la variable `i` puede usarse después del ciclo.
7. ¿Qué provoca un ciclo infinito? Da un ejemplo.
8. ¿Qué es un error «por uno»?
9. Escribe el encabezado de un `for` que cuente de 20 a 0 de 4 en 4.
10. ¿Qué estructura de PSeInt corresponde a `for`?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Haz la traza y predice la salida:**

```cpp check title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int a = 1, s = 0;
    while (a < 20)
    {
        s += a;
        a *= 3;
    }
    cout << a << " " << s << "\n";
    return 0;
}
```

**P2. Convierte** a `for` y a `do-while`: `int x = 10; while (x > 0) { cout << x << " "; x -= 3; }` ¿Producen exactamente lo mismo? ¿Hay algún valor inicial de `x` con el que el `do-while` se comporte distinto?

**P3. Corrige:** el programa debe sumar los números del 1 al `n`, pero da resultados raros: `int suma; for (int i = 1; i < n; i++); suma = suma + i;`

**P4. Escribe un programa** que lea números enteros positivos hasta que se escriba 0 y muestre cuántos fueron pares, cuántos impares y el mayor de todos.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Identifico inicialización, condición, cuerpo y actualización en cualquier ciclo.</li>
<li>Elijo entre <code>while</code>, <code>do-while</code> y <code>for</code> y sé convertir entre ellos.</li>
<li>Uso contadores, acumuladores, centinelas y validación.</li>
<li>Hago la traza de un ciclo y detecto ciclos infinitos y errores por uno.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 Inicialización, condición, cuerpo y actualización · 2 `do-while` · 3 10 · 4 1 · 5 Un valor especial que no es dato y marca el fin de la entrada · 6 Falso: solo existe dentro del `for` · 7 Una condición que nunca se vuelve falsa, p. ej., olvidar `i++` en `while (i < 5)` · 8 Repetir una vez de más o de menos por usar `<` en lugar de `<=` (o al revés) o empezar en el valor equivocado · 9 `for (int i = 20; i >= 0; i -= 4)` · 10 `Para … Hasta … Con Paso … Hacer … FinPara`
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** Traza: `s = 1, a = 3` → `s = 4, a = 9` → `s = 13, a = 27` → sale (27 ≥ 20).

```cpp run title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int a = 1, s = 0;
    while (a < 20)
    {
        s += a;
        a *= 3;
    }
    cout << a << " " << s << "\n";
    return 0;
}
```

**P2.** `for (int x = 10; x > 0; x -= 3) cout << x << " ";` y `int x = 10; do { cout << x << " "; x -= 3; } while (x > 0);`. Con `x = 10` las tres muestran `10 7 4 1`. Si `x` empieza en 0 o negativo, el `do-while` muestra un valor y las otras dos nada.

**P3.** Inicializar `suma = 0`; quitar el `;` después del `for`; usar `i <= n`; y poner `suma += i;` dentro del ciclo.

**P4.**

```cpp run title="p4.cpp" stdin="7 12 3 40 9 0\n"
#include <iostream>
using namespace std;
int main()
{
    int x, pares = 0, impares = 0, mayor = 0;
    cin >> x;
    while (x != 0)
    {
        if (x % 2 == 0) pares++; else impares++;
        if (x > mayor) mayor = x;
        cin >> x;
    }
    cout << "Pares: " << pares << "  Impares: " << impares << "  Mayor: " << mayor << "\n";
    return 0;
}
```
:::
