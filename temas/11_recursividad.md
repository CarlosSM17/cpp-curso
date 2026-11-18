---
num: "11"
archivo: "Tema11_Recursividad"
titulo: "Recursividad"
corto: "Recursividad"
lema: "Una función que se llama a sí misma con un problema más pequeño, hasta llegar a uno tan sencillo que ya conoce la respuesta."
duracion: "4 h · 2 sesiones de 2 h"
previos: "Tema 10 (funciones, parámetros, `return` y pila de llamadas)."
fuentes:
  - "Kernighan, B. W. y Ritchie, D. M. (1988). *The C Programming Language* (2.ª ed.). Prentice Hall. Cap. 4: §4.10 Recursion."
  - "King, K. N. (2008). *C Programming: A Modern Approach* (2.ª ed.). W. W. Norton. Cap. 9: §9.6 Recursion (incluye *quicksort*)."
objetivos:
  A:
    - "Explicar qué es una función recursiva e identificar su caso base y su caso recursivo."
    - "Rastrear la ejecución de una función recursiva con la pila de llamadas (apilar y desapilar)."
    - "Implementar funciones recursivas para factorial, potencia, sumas y Fibonacci."
    - "Comparar una solución recursiva con su equivalente iterativa."
  B:
    - "Aplicar recursión sobre arreglos (suma, máximo, búsqueda binaria)."
    - "Analizar el costo de la recursión múltiple (Fibonacci, Torres de Hanói)."
    - "Reconocer recursión directa e indirecta."
    - "Diagnosticar el desbordamiento de pila por falta de caso base."
efectos:
  soporte:
    - ["Elementos aislados", "Idea → caso base/recursivo → pila → acción antes/después → reducción del problema → recursión múltiple → tipos."]
    - ["Atención dividida", "Pila de llamadas y árbol de llamadas integrados con el código y la traza."]
    - ["Ejemplo resuelto", "Potencia bᵉ recursiva con traza de subida y bajada."]
    - ["Movimiento humano", "«¿Cuántos hay detrás de ti?»: la pregunta viaja por la fila y la respuesta regresa."]
  procedimental:
    - ["Variabilidad", "Plantilla «caso base + llamada más pequeña» aplicada a números, dígitos y arreglos."]
    - ["Autoexplicación", "Antes de ejecutar, explicar qué llamada hace cada nivel."]
  tareas:
    - ["Ejemplo resuelto", "T1: suma de 1 a n recursiva + gemelo (multiplicación por sumas)."]
    - ["Problema por completar", "T2 (Fibonacci, con pistas) y T3 (dígitos al revés, sin pistas)."]
    - ["Desvanecimiento de guía", "T1 → T4."]
    - ["Solución libre", "T5: todas las formas de calcular 1 + 2 + … + n."]
    - ["Autoexplicación", "T6: tres funciones recursivas defectuosas."]
    - ["Imaginación", "T7: imaginar los movimientos de las Torres de Hanói."]
    - ["Memoria colectiva de trabajo", "T8: adivinador de números con búsqueda binaria recursiva."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Factorial, potencia, sumas; pila de llamadas paso a paso."
    B: "Recursión múltiple y su costo, arreglos, búsqueda binaria, recursión indirecta."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 con hoja de pila impresa (marcos para llenar)."
    B: "T5, T6, T7 autónomas; T8 como diseñadores del algoritmo."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "MCD recursivo (T4) con su traza."
    B: "Hanói con conteo de movimientos y análisis de 2ⁿ − 1 (T7)."
  Entorno:
    comp: "Información procedimental"
    A: "Depurador mostrando la pila de llamadas (*call stack*)."
    B: "Terminal; medir llamadas con un contador `static`."
plan:
  - ["Sesión 1", "Soporte + tareas", "«¿Cuántos hay detrás de ti?»; conceptos 1–5; ejemplo resuelto; T1, T2.", "120 min"]
  - ["Sesión 2", "Soporte + tareas + evaluación", "Conceptos 6–8; T3–T8 según la ruta; protocolo verbal; tests.", "120 min"]
glosario:
  - ["recursividad", "recursion", "Técnica en la que una función se llama a sí misma."]
  - ["caso base", "base case", "Caso que se resuelve directamente, sin llamada recursiva; detiene la recursión."]
  - ["caso recursivo", "recursive case", "Caso que se resuelve llamando a la función con un problema más pequeño."]
  - ["llamada recursiva", "recursive call", "La llamada de la función a sí misma."]
  - ["apilar / desapilar", "push / pop (stack frames)", "Crear y destruir marcos en la pila de llamadas."]
  - ["desbordamiento de pila", "stack overflow", "Error por demasiadas llamadas anidadas (p. ej., sin caso base)."]
  - ["recursión directa", "direct recursion", "La función se llama a sí misma."]
  - ["recursión indirecta / mutua", "indirect / mutual recursion", "A llama a B y B llama a A."]
  - ["recursión múltiple", "tree recursion", "Cada llamada genera dos o más llamadas (Fibonacci)."]
  - ["iterativo", "iterative", "Solución con ciclos en lugar de recursión."]
  - ["búsqueda binaria", "binary search", "Buscar en un arreglo ordenado descartando la mitad en cada paso."]
  - ["memoización", "memoization", "Guardar resultados ya calculados para no repetir llamadas."]
---

# 1. Información de soporte {.soporte}

:::analogia | Las muñecas rusas (matrioskas)
Para encontrar la muñeca más pequeña, abres la muñeca grande y encuentras… otra muñeca igual, pero más pequeña. Repites **la misma acción** con ella. En algún momento llegas a una muñeca que **ya no se abre**: ahí te detienes. La recursividad funciona igual: una función resuelve un problema pidiéndose **a sí misma** que resuelva una versión **más pequeña**, hasta llegar a un caso tan simple que se resuelve directamente.
:::

:::pregunta
5! = 5 · 4 · 3 · 2 · 1. Observa: 5! = 5 · 4!. **¿Cómo podrías definir n! usando (n − 1)!? ¿Cuándo debe detenerse esa definición?**

{{lineas:2}}
:::

:::relevancia
La recursividad aparece en la vida real y en la computación: carpetas que contienen carpetas, fractales en gráficos, árboles de decisiones en la inteligencia artificial de los juegos (minimax del ajedrez), algoritmos rápidos de ordenamiento (*quicksort*, que King presenta en C) y la búsqueda binaria. Pensar recursivamente te da una herramienta poderosa para problemas que «se parecen a sí mismos». {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | Una definición que se usa a sí misma | Elementos aislados
En matemáticas: `n! = n · (n − 1)!` si `n > 0`, y `0! = 1`. Tiene dos partes:

- **Caso base:** `0! = 1` — se responde **sin** usar la definición.
- **Caso recursivo:** `n! = n · (n − 1)!` — usa la definición con un problema **más pequeño** (`n − 1`).

Cada paso acerca el problema al caso base: 4! → 3! → 2! → 1! → 0!.
:::

:::concepto | 2 | La primera función recursiva | Elementos aislados, Atención dividida
```c run title="factorial.c"
#include <stdio.h>

long long factorial(int n)
{
    if (n == 0)                        //> **Caso base**: se responde directamente
        return 1;
    return n * factorial(n - 1);       //> **Caso recursivo**: se llama a sí misma con n − 1
}

int main(void)
{
    for (int i = 0; i <= 5; i++)
        printf("%d! = %lld\n", i, factorial(i));
    return 0;
}
```
Toda función recursiva correcta cumple dos reglas: (1) **tiene** un caso base y (2) cada llamada recursiva **se acerca** al caso base.
:::

:::concepto | 3 | Lo que pasa en la pila: subir y bajar | Elementos aislados, Atención dividida
Cada llamada crea un **marco** nuevo con **su propia** `n`, que espera el resultado de la llamada de arriba.

<div class="cols eq">
<div>

```diagram stack
title: "Subida: se apilan llamadas"
frames:
  - {name: "main()", vars: [["", "factorial(3)"]]}
  - {name: "factorial(3)", vars: [[n, 3]], note: "espera 2!"}
  - {name: "factorial(2)", vars: [[n, 2]], note: "espera 1!"}
  - {name: "factorial(1)", vars: [[n, 1]], note: "espera 0!"}
  - {name: "factorial(0)", vars: [[n, 0]], hl: true, note: "caso base → 1"}
```

</div>
<div>

<div class="traza" markdown="1">

| Bajada (desapilar) | devuelve |
|---|---|
| `factorial(0)` | 1 |
| `factorial(1)` = 1 · 1 | 1 |
| `factorial(2)` = 2 · 1 | 2 |
| `factorial(3)` = 3 · 2 | **6** |

</div>

Las multiplicaciones se hacen **al regresar**: ninguna llamada puede terminar hasta que termina la de arriba.

</div>
</div>
:::

:::movimiento | ¿Cuántos hay detrás de ti? (10 min)
Una fila de estudiantes, todos mirando al frente. El instructor pregunta al **primero**: «¿cuántas personas hay detrás de ti?». Nadie puede voltear a contar: solo puede **preguntarle lo mismo** al de atrás y esperar. La pregunta viaja hasta el **último**, que responde «0» (caso base). Cada uno responde a quien le preguntó «lo que me dijeron **+ 1**». La respuesta regresa hasta el frente. El grupo identifica: ¿cuál fue el caso base? ¿qué se hizo «a la subida» y qué «a la bajada»?
:::

:::concepto | 4 | ¿Antes o después de la llamada? | Elementos aislados, Atención dividida
Lo que se hace **antes** de la llamada recursiva ocurre a la **subida**; lo que se hace **después**, a la **bajada** (en orden inverso):

<div class="cols eq">
<div>

```c run title="antes.c"
#include <stdio.h>
void contar(int n)
{
    if (n == 0) return;
    printf("%d ", n);   // ANTES
    contar(n - 1);
}
int main(void)
{
    contar(5);
    printf("\n");
    return 0;
}
```

</div>
<div>

```c run title="despues.c"
#include <stdio.h>
void contar(int n)
{
    if (n == 0) return;
    contar(n - 1);
    printf("%d ", n);   // DESPUES
}
int main(void)
{
    contar(5);
    printf("\n");
    return 0;
}
```

</div>
</div>
:::

:::concepto | 5 | Reducir el problema: dígitos y sumas | Elementos aislados
La pregunta clave para diseñar una función recursiva: **«si alguien me resolviera el problema un poco más pequeño, ¿cómo lo usaría?»**

```c run title="digitos.c"
#include <stdio.h>

int sumaDigitos(int n)
{
    if (n < 10)                          //> Caso base: un solo dígito
        return n;
    return n % 10 + sumaDigitos(n / 10); //> Último dígito + suma de los demás (número más corto)
}

int main(void)
{
    printf("%d\n", sumaDigitos(4072));   //> 2 + sumaDigitos(407) = 2 + 7 + sumaDigitos(40) = …
    return 0;
}
```
:::

:::concepto | 6 | Recursión múltiple: Fibonacci y su costo | Elementos aislados, Atención dividida
Si una llamada genera **dos** llamadas, el número de llamadas crece muy rápido:

```c run title="fib.c"
#include <stdio.h>
long long llamadas = 0;
long long fib(int n)
{
    llamadas++;
    if (n < 2) return n;                 //> Dos casos base: fib(0) = 0, fib(1) = 1
    return fib(n - 1) + fib(n - 2);      //> Dos llamadas recursivas
}
int main(void)
{
    int prueba[] = {5, 20, 30};
    for (int i = 0; i < 3; i++)
    {
        llamadas = 0;
        long long r = fib(prueba[i]);
        printf("fib(%d) = %lld con %lld llamadas\n", prueba[i], r, llamadas);
    }
    return 0;
}
```

```dot caption="Árbol de llamadas de fib(4): fib(2) se calcula dos veces y fib(1) tres." w="70%"
rankdir=TB; nodesep=0.15; ranksep=0.25;
node [shape=box, style="rounded,filled", fillcolor="#eff6ff", color="#2563eb", fontsize=11];
a [label="fib(4)"]; b [label="fib(3)"]; c [label="fib(2)", fillcolor="#fde68a"];
d [label="fib(2)", fillcolor="#fde68a"]; e [label="fib(1)"]; f [label="fib(1)"]; g [label="fib(0)"];
h [label="fib(1)"]; i [label="fib(0)"];
a -> b; a -> c; b -> d; b -> e; d -> f; d -> g; c -> h; c -> i;
```
**Moraleja:** la recursión es elegante, pero no siempre eficiente; Fibonacci iterativo (Tema 06) hace solo `n` pasos.
:::

:::concepto | 7 | Tipos, ventajas y desventajas | Elementos aislados
| Tipo | Descripción | Ejemplo |
|---|---|---|
| Directa | la función se llama a sí misma | `factorial` |
| Indirecta (mutua) | A llama a B y B llama a A | `esPar(n)` llama a `esImpar(n − 1)` y viceversa |
| Simple | una llamada recursiva por nivel | factorial, suma de dígitos |
| Múltiple | varias llamadas por nivel | Fibonacci, Hanói |

| Ventajas | Desventajas |
|---|---|
| Código corto y cercano a la definición matemática | Cada llamada ocupa memoria en la pila |
| Natural para estructuras que se contienen a sí mismas (árboles, carpetas) | Puede ser lenta si repite cálculos (Fibonacci) |
| Facilita algoritmos de «divide y vencerás» | Sin caso base: desbordamiento de pila |
:::

:::concepto | 8 | Ruta B · Recursión sobre arreglos y búsqueda binaria | Elementos aislados, Reversión de la experiencia
```c run title="arreglos_rec.c"
#include <stdio.h>

int suma(const int a[], int n)                 //> Suma de los primeros n elementos
{
    if (n == 0) return 0;
    return suma(a, n - 1) + a[n - 1];
}

int binaria(const int a[], int ini, int fin, int x)   //> a debe estar ORDENADO
{
    if (ini > fin) return -1;                  //> Caso base: rango vacío → no está
    int mitad = (ini + fin) / 2;
    if (a[mitad] == x) return mitad;           //> Caso base: lo encontramos
    if (x < a[mitad]) return binaria(a, ini, mitad - 1, x);   //> Descarta la mitad derecha
    return binaria(a, mitad + 1, fin, x);                     //> Descarta la mitad izquierda
}

int main(void)
{
    int v[] = {3, 8, 15, 21, 34, 42, 57, 63};
    printf("Suma: %d\n", suma(v, 8));
    printf("42 esta en %d; 10 esta en %d\n", binaria(v, 0, 7, 42), binaria(v, 0, 7, 10));
    return 0;
}
```
La búsqueda binaria encuentra un dato entre 1 000 000 en a lo más 20 pasos: cada llamada **descarta la mitad**.
:::

## 1.2 Ejemplo resuelto: potencia recursiva

:::ejemplo | bᵉ con recursión | Ejemplo resuelto, Atención dividida
**Problema.** Calcular `b` elevado a `e` (entero `e ≥ 0`) sin `pow` ni ciclos, usando recursión.

**A. Algoritmo (definición recursiva):** `b⁰ = 1` (caso base); `bᵉ = b · bᵉ⁻¹` (caso recursivo).

**B. Pseudocódigo**

```pseudo
Funcion r <- potencia(b, e)
    Si e = 0 Entonces
        r <- 1
    SiNo
        r <- b * potencia(b, e - 1)
    FinSi
FinFuncion

Algoritmo Potencias
    Leer b, e
    Escribir potencia(b, e)
FinAlgoritmo
```

**C. Código en C** (con traza de cada nivel)

```c run title="potencia.c" stdin="2 4\n"
#include <stdio.h>

double potencia(double b, int e, int nivel)          //> `nivel` solo sirve para mostrar la traza con sangría
{
    printf("%*spotencia(%.0f, %d)\n", nivel * 2, "", b, e);   //> Subida; `%*s` con "" imprime nivel·2 espacios
    if (e == 0)                                      //> Caso base
    {
        printf("%*s-> 1 (caso base)\n", nivel * 2, "");
        return 1;
    }
    double r = b * potencia(b, e - 1, nivel + 1);   //> Caso recursivo: problema más pequeño (e − 1)
    printf("%*s-> %.0f\n", nivel * 2, "", r);        //> Bajada: el resultado se construye al regresar
    return r;
}

int main(void)
{
    double b;
    int e;
    printf("Base y exponente: ");
    scanf("%lf %d", &b, &e);
    double r = potencia(b, e, 0);                    //> El nivel inicial es 0 (C no tiene valores por defecto)
    printf("Resultado: %.0f\n", r);
    return 0;
}
```

**D. Verificación.** La traza muestra 5 llamadas (exponentes 4, 3, 2, 1, 0) y cómo el resultado se construye al regresar: 1 → 2 → 4 → 8 → 16 ✔.
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.18; ranksep=0.3;
@term(r, "Función recursiva")
@hl(b, "caso base\n(detiene)")
@proc(c, "caso recursivo\nproblema más pequeño")
@proc(p, "pila: subida (apilar)\nbajada (desapilar)")
@proc(ad, "acción antes = subida\nacción después = bajada")
@sub(m, "recursión múltiple\n(costo exponencial)")
@sub(t, "directa · indirecta")
r -> b; r -> c; c -> p; p -> ad; r -> m [style=dashed]; r -> t [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1 · Plantilla y receta | Variabilidad
```c blank title="plantilla_recursiva.c"
tipo resolver(problema)
{
    if (problema es trivial)               // 1) CASO BASE: respuesta directa
        return respuesta_directa;
    // 2) CASO RECURSIVO: problema mas pequeno + combinar
    return combinar(parte, resolver(problema_mas_pequeno));
}
```

**Receta en 4 preguntas:** (1) ¿Cuál es el caso más pequeño y su respuesta? (2) ¿Cómo hago el problema más pequeño? (`n − 1`, `n / 10`, mitad del arreglo) (3) Si tuviera la respuesta del problema pequeño, ¿cómo obtengo la del grande? (4) ¿Cada llamada se acerca al caso base?

| Problema | Caso base | Caso recursivo |
|---|---|---|
| n! | `n == 0 → 1` | `n * f(n - 1)` |
| bᵉ | `e == 0 → 1` | `b * p(b, e - 1)` |
| suma 1..n | `n == 0 → 0` | `n + s(n - 1)` |
| dígitos de n | `n < 10 → 1` | `1 + d(n / 10)` |
| MCD(a, b) | `b == 0 → a` | `mcd(b, a % b)` |
| suma de arreglo | `n == 0 → 0` | `s(a, n - 1) + a[n - 1]` |
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿Hay un caso base y está <b>antes</b> de la llamada recursiva?</li>
<li>¿El caso base cubre todos los valores mínimos posibles (0, 1, negativos)?</li>
<li>¿La llamada recursiva usa un problema <b>más pequeño</b> (<code>n − 1</code>, no <code>n</code>)?</li>
<li>¿Uso (con <code>return</code>) el resultado de la llamada recursiva?</li>
<li>¿Hice la traza de la pila con un caso pequeño (2 o 3 niveles)?</li>
<li>¿La recursión repite cálculos? ¿Sería mejor una versión iterativa?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Sin caso base (o inalcanzable): desbordamiento de pila.** El programa se detiene con *Segmentation fault* / *stack overflow* tras miles de llamadas:

```c blank title="sin_base.c"
int f(int n)
{
    return n * f(n - 1);    // nunca se detiene
}
```

**b) Caso base que no se alcanza** con algunos datos: `if (n == 1) return 1;` con `factorial(0)` baja a −1, −2… sin fin. Usa `n <= 1` o `n == 0`.

**c) Llamada recursiva que no reduce:** `return n * factorial(n);` llama siempre con el mismo valor.

**d) Ignorar el resultado de la llamada.** El valor calculado se pierde:

```c run
#include <stdio.h>
int suma(int n)
{
    if (n == 0) return 0;
    suma(n - 1);              //> Se calcula… y se descarta
    return n;                 //> Devuelve solo n
}
int main(void)
{
    printf("%d\n", suma(4));  //> Esperado 10, sale 4
    return 0;
}
```
*Corrección:* `return n + suma(n - 1);`

**e) Función no `void` sin `return` en el caso recursivo:** compila con advertencia (*control reaches end of non-void function*); el resultado es indefinido.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Recursión indirecta: ¿par o impar? | Variabilidad
Dos funciones que se llaman mutuamente:

```c run title="mutua.c"
#include <stdio.h>
#include <stdbool.h>
bool esImpar(int n);                  //> Prototipo necesario: esPar usa esImpar antes de definirla
bool esPar(int n)
{
    if (n == 0) return true;          //> Caso base
    return esImpar(n - 1);            //> n es par si n − 1 es impar
}
bool esImpar(int n)
{
    if (n == 0) return false;
    return esPar(n - 1);
}
int main(void)
{
    printf("esPar(10): %s  esPar(7): %s  esImpar(7): %s\n",
           esPar(10) ? "si" : "no", esPar(7) ? "si" : "no", esImpar(7) ? "si" : "no");
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Para cada función responde primero las 4 preguntas de la receta (tarjeta 2.1).

:::tarea A | T1. Suma de 1 a n: ejemplo y gemelo | 20 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia:**

```c run title="suma_rec.c" stdin="5\n"
#include <stdio.h>

int sumaHasta(int n)
{
    if (n == 0)                     //> 1) Caso más pequeño: la suma de nada es 0
        return 0;
    return n + sumaHasta(n - 1);    //> 2) Más pequeño: n − 1   3) Combinar: sumarle n
}

int main(void)
{
    int n;
    scanf("%d", &n);
    printf("1 + ... + %d = %d\n", n, sumaHasta(n));
    return 0;
}
```

**Paso 2 · Gemelo.** Escribe `int multiplicar(int a, int b)` que calcule `a × b` (con `b ≥ 0`) **solo con sumas**, usando recursión: `a × 0 = 0` y `a × b = a + a × (b − 1)`.

:::solucion | T1
```c run title="multiplicar.c" runs="7 4|9 0"
#include <stdio.h>

int multiplicar(int a, int b)
{
    if (b == 0)
        return 0;
    return a + multiplicar(a, b - 1);
}

int main(void)
{
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d x %d = %d\n", a, b, multiplicar(a, b));
    return 0;
}
```
:::
:::

:::tarea A | T2. Fibonacci recursivo (completa con pistas) | 20 min | Problema por completar
**Contexto.** Compara con tu versión iterativa del Tema 06 (T3).

```c blank title="fib_rec.c"
#include <stdio.h>

long long fib(int n)
{
    if (n == __1__)                // 1: primer caso base
        return 0;
    if (n == __2__)                // 2: segundo caso base
        return 1;
    return __3__ + __4__;          // 3 y 4: los dos terminos anteriores
}

int main(void)
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        printf("%lld ", __5__);    // 5: termino i de la serie
    printf("\n");
    return 0;
}
```

:::solucion | T2
{{c:1}} `0` · {{c:2}} `1` · {{c:3}} `fib(n - 1)` · {{c:4}} `fib(n - 2)` · {{c:5}} `fib(i)`

```c run title="fib_rec.c" stdin="12\n"
#include <stdio.h>

long long fib(int n)
{
    if (n == 0)
        return 0;
    if (n == 1)
        return 1;
    return fib(n - 1) + fib(n - 2);
}

int main(void)
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        printf("%lld ", fib(i));
    printf("\n");
    return 0;
}
```
:::
:::

:::tarea AB | T3. Dígitos al revés (completa sin pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Muestra los dígitos de un número **al revés** (4072 → `2 7 0 4`) y después **en orden** (`4 0 7 2`), con dos funciones recursivas `void`. Pista conceptual: concepto 4.

```c blank title="digitos_orden.c"
#include <stdio.h>

void alReves(int n)
{
    printf("%d ", __1__);
    if (n >= 10)
        __2__;
}

void enOrden(int n)
{
    if (n >= 10)
        __3__;
    printf("%d ", __4__);
}

int main(void)
{
    int n;
    scanf("%d", &n);
    alReves(n);
    printf("\n");
    enOrden(n);
    printf("\n");
    return 0;
}
```

:::solucion | T3
{{c:1}} `n % 10` · {{c:2}} `alReves(n / 10)` · {{c:3}} `enOrden(n / 10)` · {{c:4}} `n % 10`. La única diferencia es si el `printf` va **antes** (subida) o **después** (bajada) de la llamada.

```c run title="digitos_orden.c" stdin="4072\n"
#include <stdio.h>

void alReves(int n)
{
    printf("%d ", n % 10);
    if (n >= 10)
        alReves(n / 10);
}

void enOrden(int n)
{
    if (n >= 10)
        enOrden(n / 10);
    printf("%d ", n % 10);
}

int main(void)
{
    int n;
    scanf("%d", &n);
    alReves(n);
    printf("\n");
    enOrden(n);
    printf("\n");
    return 0;
}
```
:::
:::

:::tarea AB | T4. Máximo común divisor de Euclides (problema convencional) | 30 min | Variabilidad
**Contexto.** El algoritmo de Euclides (¡de hace más de 2000 años!) dice: `mcd(a, 0) = a` y `mcd(a, b) = mcd(b, a % b)`. Escribe la función recursiva, úsala para calcular el **mínimo común múltiplo** (`mcm(a, b) = a / mcd(a, b) * b`) y para **simplificar una fracción** (por ejemplo, 84/36 → 7/3). Incluye la traza de `mcd(84, 36)`.

:::solucion | T4
Traza: `mcd(84, 36)` → `mcd(36, 12)` → `mcd(12, 0)` → 12.

```c run title="euclides.c" stdin="84 36\n"
#include <stdio.h>

int mcd(int a, int b)
{
    if (b == 0)
        return a;
    return mcd(b, a % b);
}

int main(void)
{
    int a, b;
    scanf("%d %d", &a, &b);
    int d = mcd(a, b);
    printf("mcd = %d, mcm = %d\n", d, a / d * b);
    printf("%d/%d = %d/%d\n", a, b, a / d, b / d);
    return 0;
}
```
:::
:::

:::tarea A | T5. 1 + 2 + … + n de todas las formas (solución libre) | 25 min | Solución libre
**Contexto.** Escribe **todas las versiones que puedas** para calcular `1 + 2 + … + n`: con `for`, con `while`, con la fórmula de Gauss, recursiva «hacia abajo» (`n + s(n − 1)`), recursiva «hacia arriba» (empezando en 1 hasta `n`), recursiva con acumulador… Compara: ¿cuál usa más memoria? ¿cuál es más clara?

:::solucion | T5
```c run title="sumas_todas.c"
#include <stdio.h>
int abajo(int n) { return n == 0 ? 0 : n + abajo(n - 1); }
int arriba(int i, int n) { return i > n ? 0 : i + arriba(i + 1, n); }
int acum(int n, int total) { return n == 0 ? total : acum(n - 1, total + n); }
int main(void)
{
    int n = 100, s1 = 0, s2 = 0, i = 1;
    for (int k = 1; k <= n; k++) s1 += k;
    while (i <= n) s2 += i++;
    printf("%d %d %d %d %d %d\n", s1, s2, n * (n + 1) / 2, abajo(n), arriba(1, n), acum(n, 0));
    return 0;
}
```
La fórmula no usa ciclos ni pila; las versiones recursivas usan `n` marcos en la pila; la versión con acumulador hace la suma «a la subida».
:::
:::

:::tarea B | T6. Tres funciones recursivas que fallan (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
Explica **qué ocurre** con cada función cuando se llama con el valor indicado, **por qué**, y corrígela.

```c blank title="fallas.c"
// A: potencia(2, 3)
int potencia(int b, int e) { if (e == 1) return b; return b * potencia(b, e - 1); }
//    ...y potencia(2, 0)?

// B: contarDigitos(500)
int contarDigitos(int n) { if (n == 0) return 0; return 1 + contarDigitos(n % 10); }

// C: maximo(v, 4) con v = {3, 9, 2, 7}
int maximo(const int v[], int n)
{
    if (n == 1) return v[0];
    int m = maximo(v, n - 1);
    if (v[n - 1] > m) return v[n - 1];
}
```

{{lineas:5}}

:::solucion | T6
**A:** con `e = 3` funciona (8), pero con `e = 0` el caso base `e == 1` nunca se alcanza: `e` baja a −1, −2… → desbordamiento de pila. Caso base: `e == 0 → 1`.
**B:** `n % 10` no «achica» el número: `500 % 10 = 0` → devuelve 1 (incorrecto); para 123 llama con 3 → 2. Debe ser `contarDigitos(n / 10)` y caso base `n < 10 → 1`.
**C:** si `v[n − 1] <= m` la función termina sin `return` (indefinido; gcc advierte *control reaches end of non-void function*). Falta `return m;` al final.

```c run title="corregidas.c"
#include <stdio.h>
int potencia(int b, int e) { if (e == 0) return 1; return b * potencia(b, e - 1); }
int contarDigitos(int n) { if (n < 10) return 1; return 1 + contarDigitos(n / 10); }
int maximo(const int v[], int n)
{
    if (n == 1) return v[0];
    int m = maximo(v, n - 1);
    if (v[n - 1] > m) return v[n - 1];
    return m;
}
int main(void)
{
    int v[] = {3, 9, 2, 7};
    printf("%d %d %d %d\n", potencia(2, 3), potencia(2, 0), contarDigitos(500), maximo(v, 4));
    return 0;
}
```
:::
:::

:::tarea B | T7. Las Torres de Hanói (imaginación) | 30 min | Imaginación
**Contexto.** Hay 3 postes (A, B, C) y `n` discos en A, del más grande (abajo) al más pequeño (arriba). Hay que pasarlos todos a C moviendo **un disco a la vez** y **sin poner nunca uno grande sobre uno pequeño**.

1. **Imagina** (o simula con monedas) la solución para 1, 2 y 3 discos y escribe los movimientos.
2. Descubre la idea recursiva: para mover `n` discos de A a C, primero se mueven `n − 1` de A a B (usando C), luego el grande de A a C, y luego los `n − 1` de B a C (usando A).
3. Prográmala, cuenta los movimientos para n = 1…10 y deduce la fórmula.

:::solucion | T7
```c run title="hanoi.c"
#include <stdio.h>
#include <stdbool.h>
int movimientos = 0;
void hanoi(int n, char origen, char destino, char auxiliar, bool mostrar)
{
    if (n == 0) return;
    hanoi(n - 1, origen, auxiliar, destino, mostrar);
    movimientos++;
    if (mostrar) printf("Disco %d: %c -> %c\n", n, origen, destino);
    hanoi(n - 1, auxiliar, destino, origen, mostrar);
}
int main(void)
{
    hanoi(3, 'A', 'C', 'B', true);
    printf("Movimientos con 3 discos: %d\n", movimientos);
    for (int n = 1; n <= 10; n++)
    {
        movimientos = 0;
        hanoi(n, 'A', 'C', 'B', false);
        printf("%d:%d ", n, movimientos);
    }
    printf("\n");
    return 0;
}
```
Los movimientos son `2ⁿ − 1`: con 64 discos (la leyenda) serían más de 18 trillones.
:::
:::

:::tarea AB | T8. El adivinador infalible (reto colaborativo) | 40 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Equipos de 4, niveles mezclados. El usuario piensa un número del 1 al 100 y la computadora lo adivina en a lo más 7 intentos: propone la mitad del rango y el usuario responde `<` (menor), `>` (mayor) o `=`.
- **Integrante 1:** función recursiva `int adivinar(int ini, int fin, int intento)` (búsqueda binaria).
- **Integrante 2:** lectura y validación de la respuesta (`<`, `>`, `=`).
- **Integrante 3:** detectar respuestas contradictorias (rango vacío: «¡hiciste trampa!»).
- **Integrante 4:** pruebas: simular al usuario para los números 1, 37, 64 y 100 y comprobar que nunca pasa de 7 intentos.
:::

:::solucion | T8
Ejecución simulando que el usuario pensó el 37:

```c run title="adivinador.c" stdin="<\n>\n=\n"
#include <stdio.h>

int adivinar(int ini, int fin, int intento)
{
    if (ini > fin)
    {
        printf("Respuestas contradictorias: hiciste trampa!\n");
        return -1;
    }
    int m = (ini + fin) / 2;
    char r;
    do {
        printf("Intento %d: es %d? (<, >, =): ", intento, m);
        scanf(" %c", &r);
    } while (r != '<' && r != '>' && r != '=');
    if (r == '=') return intento;
    if (r == '<') return adivinar(ini, m - 1, intento + 1);
    return adivinar(m + 1, fin, intento + 1);
}

int main(void)
{
    printf("Piensa un numero del 1 al 100\n");
    int n = adivinar(1, 100, 1);
    if (n != -1) printf("Lo adivine en %d intentos\n", n);
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · De decimal a binario, recursivamente | Modalidad, Ejemplo resuelto
*Guion segmentado (≈ 3 min), con la pila dibujada en pantalla.*

**Problema:** «Mostrar un número entero positivo en binario. Por ejemplo, 13 → 1101».

**Segmento 1 — El método a mano.** {{como}} Divido entre 2 y anoto residuos: 13 → residuo 1, queda 6; 6 → 0, queda 3; 3 → 1, queda 1; 1 → 1, queda 0. Los residuos salen `1 0 1 1`, pero el binario es `1101`: **al revés**. {{porque}} Hacerlo a mano primero me revela el detalle clave: el orden se invierte.

**Segmento 2 — ¿Dónde está la recursión?** {{como}} Observo que el binario de 13 es «el binario de 6» seguido del residuo 1. {{porque}} Eso es un problema más pequeño (`n / 2`) más una pieza (`n % 2`): la forma de toda función recursiva.

**Segmento 3 — Antes o después.** {{como}} Como el último residuo debe mostrarse al final, pongo el `printf` **después** de la llamada: `binario(n / 2); printf("%d", n % 2);`. {{porque}} Lo que va después de la llamada se ejecuta a la bajada, en orden inverso: justo la inversión que necesitaba.

**Segmento 4 — El caso base.** {{como}} Si `n < 2`, muestro `n` y termino. Pruebo con 1, 2, 13 y 255. {{porque}} El 1 y el 2 son los casos frontera: uno es el caso base y el otro es el primero que hace una llamada.

```c run title="binario.c"
#include <stdio.h>
void binario(int n)
{
    if (n < 2)
    {
        printf("%d", n);
        return;
    }
    binario(n / 2);
    printf("%d", n % 2);
}
int main(void)
{
    int prueba[] = {1, 2, 13, 255};
    for (int i = 0; i < 4; i++)
    {
        printf("%d -> ", prueba[i]);
        binario(prueba[i]);
        printf("\n");
    }
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. ¿Qué es una función recursiva?
2. ¿Qué es el caso base y por qué es indispensable?
3. ¿Qué ocurre en la pila con cada llamada recursiva?
4. ¿En qué orden se ejecutan las instrucciones colocadas después de la llamada recursiva?
5. Verdadero o falso: toda solución recursiva es más rápida que su versión iterativa.
6. ¿Qué es la recursión indirecta? Da un ejemplo.
7. ¿Por qué el Fibonacci recursivo simple es lento?
8. ¿Qué error produce una recursión sin caso base?
9. ¿Qué condición debe cumplir un arreglo para la búsqueda binaria?
10. Menciona una ventaja y una desventaja de la recursividad.
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Haz la traza y predice la salida:**

```c check title="p1.c"
#include <stdio.h>
int misterio(int a, int b)
{
    if (a < b) return 0;
    return 1 + misterio(a - b, b);
}
int main(void)
{
    printf("%d %d\n", misterio(17, 5), misterio(4, 7));
    return 0;
}
```
¿Qué operación calcula `misterio`?

**P2.** Escribe una función recursiva `int contarPares(const int a[], int n)` que cuente los pares de un arreglo.

**P3. Corrige:** `int sumaDig(int n) { if (n == 0) return 0; return n % 10 + sumaDig(n); }`

**P4. Escribe un programa** con una función recursiva `bool esPalindromo(const int a[], int ini, int fin)` que diga si un arreglo se lee igual al derecho y al revés (prueba con `{1, 3, 5, 3, 1}` y `{1, 2, 2, 3}`).
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Identifico el caso base y el caso recursivo de una función.</li>
<li>Dibujo la pila de llamadas de una recursión pequeña.</li>
<li>Escribo funciones recursivas para números, dígitos y arreglos.</li>
<li>Decido cuándo conviene la recursión y cuándo un ciclo.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 Una función que se llama a sí misma para resolver un problema más pequeño del mismo tipo · 2 El caso que se resuelve sin llamada recursiva; sin él la recursión no termina · 3 Se crea (apila) un nuevo marco con sus propios parámetros y variables locales · 4 A la bajada, en orden inverso al de las llamadas · 5 Falso · 6 Una función A llama a B y B llama a A; p. ej., `esPar`/`esImpar` · 7 Porque recalcula muchas veces los mismos valores (el número de llamadas crece exponencialmente) · 8 Desbordamiento de pila (*stack overflow*) · 9 Estar ordenado · 10 Ventaja: código corto y cercano a la definición; desventaja: consume memoria de pila y puede repetir cálculos.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** `misterio(17, 5)` = 1 + m(12, 5) = 2 + m(7, 5) = 3 + m(2, 5) = 3. Calcula la **división entera** por restas sucesivas.

```c run title="p1.c"
#include <stdio.h>
int misterio(int a, int b)
{
    if (a < b) return 0;
    return 1 + misterio(a - b, b);
}
int main(void)
{
    printf("%d %d\n", misterio(17, 5), misterio(4, 7));
    return 0;
}
```

**P2.** `int contarPares(const int a[], int n) { if (n == 0) return 0; return (a[n - 1] % 2 == 0 ? 1 : 0) + contarPares(a, n - 1); }`

**P3.** La llamada no reduce el número: debe ser `sumaDig(n / 10)`.

**P4.**

```c run title="palindromo_arreglo.c"
#include <stdio.h>
#include <stdbool.h>
bool esPalindromo(const int a[], int ini, int fin)
{
    if (ini >= fin) return true;
    if (a[ini] != a[fin]) return false;
    return esPalindromo(a, ini + 1, fin - 1);
}
int main(void)
{
    int x[] = {1, 3, 5, 3, 1};
    int y[] = {1, 2, 2, 3};
    printf("%s %s\n", esPalindromo(x, 0, 4) ? "si" : "no", esPalindromo(y, 0, 3) ? "si" : "no");
    return 0;
}
```
:::
