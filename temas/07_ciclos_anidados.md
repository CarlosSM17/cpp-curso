---
num: "07"
archivo: "Tema07_Ciclos_anidados_break_continue"
titulo: "Ciclos anidados, break y continue"
corto: "Ciclos anidados"
lema: "Un ciclo dentro de otro: como las manecillas de un reloj, el de adentro da la vuelta completa por cada paso del de afuera."
duracion: "4 h · 2 sesiones de 2 h"
previos: "Tema 06 (while, do-while, for, contador y acumulador). Este tema aplica el efecto de elementos aislados: primero ciclos simples, ahora ciclos anidados."
fuentes:
  - "Kernighan, B. W. y Ritchie, D. M. (1988). *The C Programming Language* (2.ª ed.). Prentice Hall. Cap. 3: §3.5 Loops—While and For, §3.7 Break and Continue, §3.8 Goto and Labels."
  - "King, K. N. (2008). *C Programming: A Modern Approach* (2.ª ed.). W. W. Norton. Cap. 6: §6.3 The for Statement, §6.4 Exiting from a Loop."
  - "Seacord, R. C. (2020). *Effective C*. No Starch Press. Cap. 5 «Control Flow»: Iteration Statements, Jump Statements."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §6.1.9 (variabilidad: cuadrado de n×n con `*`) y §6.1.11 (elementos aislados: ciclos → ciclos anidados)."
objetivos:
  A:
    - "Explicar cómo se ejecuta un ciclo dentro de otro: el interno completa todas sus vueltas por cada vuelta del externo."
    - "Dibujar figuras y tablas en pantalla con ciclos anidados (rectángulos, triángulos, tablas de multiplicar)."
    - "Usar `break` para salir de un ciclo y `continue` para saltar a la siguiente iteración."
    - "Calcular cuántas veces se ejecuta el cuerpo del ciclo interno."
  B:
    - "Diseñar patrones en los que el número de vueltas del ciclo interno depende del externo (pirámides, triángulos invertidos)."
    - "Salir de varios ciclos a la vez con una bandera y explicar por qué se evita `goto`."
    - "Resolver problemas de búsqueda con salida temprana (primos, divisores, números perfectos)."
    - "Estimar el costo de un ciclo anidado (n · m iteraciones) y reducirlo cuando sea posible."
efectos:
  soporte:
    - ["Elementos aislados", "Se parte de un solo renglón (ciclo simple ya dominado) y se agrega el segundo ciclo; `break` y `continue` se presentan al final, por separado."]
    - ["Atención dividida", "Cuadrícula que numera el orden de visita junto al código y su traza (i, j)."]
    - ["Ejemplo resuelto", "Cuadrado de n×n con asteriscos (tesis §6.1.9)."]
    - ["Movimiento humano", "«Reloj humano»: dos estudiantes representan los ciclos externo e interno."]
  procedimental:
    - ["Variabilidad", "Catálogo de patrones (rectángulo, triángulos, pirámide) con el mismo esquema."]
    - ["Interactividad de elementos", "Plantilla «una fila = un ciclo interno + salto de línea» que reduce los elementos a coordinar."]
  tareas:
    - ["Ejemplo resuelto", "T1: rectángulo resuelto + gemelo (asientos del estadio)."]
    - ["Problema por completar", "T2 (triángulo de números, con pistas) y T3 (tabla completa, sin pistas)."]
    - ["Desvanecimiento de guía", "T1 → T4."]
    - ["Solución libre", "T5: todas las figuras posibles con n = 4."]
    - ["Autoexplicación", "T6: explicar errores en ciclos anidados."]
    - ["Imaginación", "T7: imaginar la salida de ciclos con `break`/`continue`."]
    - ["Memoria colectiva de trabajo", "T8: tablero de batalla naval por equipos."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Rectángulos, triángulos y tablas; `break` y `continue` en ciclos simples."
    B: "Pirámides centradas, banderas para salir de dos ciclos, costo n·m."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 con cuadrícula de papel para dibujar cada figura antes de codificarla."
    B: "T5 (figuras difíciles), T6, T7 autónomas; liderazgo en T8."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Lista de primos (T4) con traza de un caso."
    B: "Galería de figuras (T5) con la fórmula de espacios y símbolos por fila."
  Entorno:
    comp: "Información procedimental"
    A: "Hojas cuadriculadas; depurador con vigilancia de `i` y `j`."
    B: "Terminal; medición de iteraciones con un contador."
plan:
  - ["Apertura", "Soporte", "Reloj humano; pregunta: «¿cuántas veces se mueve el minutero en 3 horas?».", "15 min"]
  - ["Desarrollo", "Soporte", "Conceptos 1–8 y ejemplo resuelto del cuadrado.", "50 min"]
  - ["Práctica guiada", "Tareas + procedimental", "Ruta A: T1 → T3. Ruta B: T5, T6, T7.", "55 min"]
  - ["Colaborativa", "Tareas", "T8 batalla naval.", "35 min"]
  - ["Autónoma", "Tareas", "T4 primos (todos).", "25 min"]
  - ["Cierre", "Protocolo + evaluación", "Protocolo verbal (pirámide), tests, autorregistro.", "40 min"]
glosario:
  - ["ciclo anidado", "nested loop", "Ciclo que está dentro del cuerpo de otro ciclo."]
  - ["ciclo externo", "outer loop", "Ciclo que contiene a otro; suele recorrer filas."]
  - ["ciclo interno", "inner loop", "Ciclo contenido; suele recorrer columnas."]
  - ["romper", "break", "Termina inmediatamente el ciclo más interno que lo contiene."]
  - ["continuar", "continue", "Salta el resto del cuerpo y pasa a la siguiente iteración."]
  - ["sentencia de salto", "jump statement", "`break`, `continue`, `return` y `goto`."]
  - ["bandera", "flag", "Variable `bool` que avisa a otros ciclos que deben terminar."]
  - ["patrón", "pattern", "Figura o tabla regular que se genera con ciclos."]
  - ["número primo", "prime number", "Entero mayor que 1 cuyos únicos divisores son 1 y él mismo."]
  - ["ancho de campo", "field width", "Número de columnas que ocupa un dato al mostrarse: `%4d` en `printf`."]
---

# 1. Información de soporte {.soporte}

:::analogia | Las manecillas del reloj
El minutero da **una vuelta completa** (60 minutos) por cada paso que avanza la manecilla de las horas. En 3 horas, el minutero recorre 3 × 60 = 180 posiciones. Un **ciclo anidado** funciona igual: el ciclo **interno** (minutero) completa todas sus vueltas cada vez que el ciclo **externo** (horario) avanza una.
:::

:::pregunta
Un cine tiene 5 filas (A a E) con 8 asientos cada una. **¿Cómo describirías, paso a paso, el recorrido que hace un acomodador que revisa todos los asientos?** ¿Qué se repite dentro de qué?

{{lineas:2}}
:::

:::relevancia
Las pantallas son cuadrículas de píxeles (filas × columnas); un tablero de ajedrez, una hoja de cálculo, un mapa de un videojuego de mosaicos (*tiles*), los asientos de un estadio: todo lo que tiene **dos dimensiones** se recorre con ciclos anidados. Son también la base de las matrices (Tema 09) y de los algoritmos de ordenamiento. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | Punto de partida: un renglón (lo que ya sabes) | Elementos aislados
Del Tema 06 ya dominas este ciclo simple, que dibuja **un renglón** de 5 asteriscos:

```c run
#include <stdio.h>
int main(void)
{
    for (int j = 1; j <= 5; j++)
        printf("*");
    printf("\n");
    return 0;
}
```
:::

:::concepto | 2 | Repetir el renglón: un ciclo dentro de otro | Elementos aislados, Atención dividida
Si quieres **3 renglones** (aquí de 4 asteriscos cada uno), repites… ¡el ciclo completo! El ciclo de renglones (externo) contiene al ciclo de asteriscos (interno):

<div class="cols">
<div>

```c run title="rectangulo.c"
#include <stdio.h>
int main(void)
{
    for (int i = 1; i <= 3; i++)        //> Externo: una vuelta por FILA
    {
        for (int j = 1; j <= 4; j++)    //> Interno: una vuelta por COLUMNA
            printf("*");
        printf("\n");                   //> Al terminar la fila: salto de línea
    }
    return 0;
}
```

</div>
<div>

```diagram mat
name: "Orden de visita (i, j)"
rows: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
hlrow: 1
hl: [[1, 0]]
caption: "Fila i = 2 (índice 1): j recorre 1..4"
```

</div>
</div>

**Regla de lectura:** «para **cada** fila `i`, recorro **todas** las columnas `j`». El salto de línea va **después** del ciclo interno y **dentro** del externo.
:::

:::concepto | 3 | La traza de un ciclo anidado y el número de vueltas | Elementos aislados, Atención dividida
```c run title="pares_ij.c"
#include <stdio.h>
int main(void)
{
    int vueltas = 0;
    for (int i = 1; i <= 2; i++)
        for (int j = 1; j <= 3; j++)
        {
            printf("(%d,%d) ", i, j);       //> Observa: j se reinicia en 1 para cada i
            vueltas++;
        }
    printf("\nCuerpo interno ejecutado %d veces\n", vueltas);
    return 0;
}
```

<div class="traza" markdown="1">

| `i` | `j` toma los valores | vueltas del interno | acumulado |
|---|---|---|---|
| 1 | 1, 2, 3 | 3 | 3 |
| 2 | 1, 2, 3 | 3 | 6 |

</div>

Si el externo da `n` vueltas y el interno `m`, el cuerpo interno se ejecuta **`n × m`** veces.
:::

:::movimiento | El reloj humano (10 min)
Dos estudiantes al frente. «Horas» sostiene un letrero con `i` y avanza de 1 a 3. «Minutos» sostiene `j` y, **cada vez** que «Horas» avanza, cuenta en voz alta de 1 a 4 y regresa a 1. El grupo escribe en el pizarrón cada par `(i, j)` que se dice en voz alta. Después: ¿cuántos pares hubo? ¿Quién se movió más veces? Repitan con la regla «Minutos cuenta solo hasta el valor de Horas» (concepto 4).
:::

:::concepto | 4 | Cuando el interno depende del externo: triángulos | Elementos aislados, Atención dividida
Si el límite del ciclo interno **usa `i`**, cada fila tiene una longitud distinta:

```c run title="triangulo.c" stdin="5\n"
#include <stdio.h>
int main(void)
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)    //> La fila i tiene i asteriscos
            printf("* ");
        printf("\n");
    }
    return 0;
}
```

<div class="traza" markdown="1">

| fila `i` | `j` va de 1 a… | asteriscos |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| … | `i` | `i` |

</div>

**Método para cualquier figura:** dibújala en papel cuadriculado y llena una tabla con «fila → cuántos espacios → cuántos símbolos». La fórmula de cada columna de esa tabla es el límite de un ciclo interno.
:::

:::concepto | 5 | Tablas con formato: el ancho de campo | Elementos aislados
Para que las columnas se alineen, el especificador `%4d` (Tema 03) reserva 4 espacios para cada número, alineado a la derecha:

```c run title="tabla_5x5.c"
#include <stdio.h>
int main(void)
{
    for (int i = 1; i <= 5; i++)
    {
        for (int j = 1; j <= 5; j++)
            printf("%4d", i * j);     //> Cada producto ocupa 4 columnas
        printf("\n");
    }
    return 0;
}
```
:::

:::concepto | 6 | `break`: salir del ciclo antes de tiempo | Elementos aislados, Atención dividida
`break` termina **inmediatamente** el ciclo que lo contiene. Útil cuando ya encontraste lo que buscabas:

```c run title="primer_multiplo.c" stdin="37 7\n"
#include <stdio.h>
int main(void)
{
    int desde, m;
    printf("Desde y multiplo de: ");
    scanf("%d %d", &desde, &m);
    for (int x = desde; x <= desde + 100; x++)
    {
        if (x % m == 0)
        {
            printf("Primer multiplo de %d desde %d: %d\n", m, desde, x);
            break;                 //> Ya lo encontramos: no tiene caso seguir
        }
    }
    return 0;
}
```
:::

:::concepto | 7 | `continue`: saltar a la siguiente vuelta | Elementos aislados
`continue` **salta el resto del cuerpo** y pasa a la siguiente iteración (en un `for`, primero ejecuta la actualización):

```c run title="sin_multiplos_3.c"
#include <stdio.h>
int main(void)
{
    for (int x = 1; x <= 12; x++)
    {
        if (x % 3 == 0)
            continue;              //> Los múltiplos de 3 no se muestran
        printf("%d ", x);
    }
    printf("\n");
    return 0;
}
```
:::

:::concepto | 8 | Ruta B · `break` solo sale de UN ciclo: banderas | Elementos aislados, Reversión de la experiencia
En ciclos anidados, `break` termina **solo el ciclo más interno**. Para salir de ambos se usa una **bandera**:

```c run title="busca_par.c"
#include <stdio.h>
#include <stdbool.h>
int main(void)
{
    bool encontrado = false;                           //> Bandera
    for (int i = 1; i <= 9 && !encontrado; i++)        //> El externo también la consulta
        for (int j = 1; j <= 9; j++)
            if (i * j == 24 && i + j == 10)
            {
                printf("i = %d, j = %d\n", i, j);
                encontrado = true;
                break;                                 //> Sale del interno; la bandera detiene al externo
            }
    return 0;
}
```

C también tiene `goto`. Kernighan y Ritchie (§3.8) muestran que puede salir de ciclos anidados de un salto, pero advierten que casi nunca es necesario y que vuelve el código difícil de entender; en programación estructurada se evita. Otra salida limpia es poner los ciclos en una función y usar `return` (Tema 10).
:::

## 1.2 Ejemplo resuelto: el cuadrado de n × n

:::ejemplo | Cuadrado de asteriscos de tamaño n (tesis §6.1.9, ej. 4a) | Ejemplo resuelto, Atención dividida
**Problema.** Dado un número `n`, mostrar un cuadrado de `n × n` asteriscos. Por ejemplo, para 5, un cuadrado de 5 × 5.

**A. Algoritmo:** 1) Leer `n`. 2) Repetir `n` veces (filas): 2.1) repetir `n` veces (columnas): mostrar `*`; 2.2) saltar de línea.

<div class="cols eq">
<div>

**B. Pseudocódigo**

```pseudo
Algoritmo Cuadrado
    Leer n
    Para i <- 1 Hasta n Hacer
        Para j <- 1 Hasta n Hacer
            Escribir Sin Saltar "* "
        FinPara
        Escribir ""
    FinPara
FinAlgoritmo
```

</div>
<div>

**Diagrama de flujo**

```dot
rankdir=TB; nodesep=0.25; ranksep=0.18;
@io(l, "Leer n")
@proc(i0, "i ← 1")
@dec(ci, "i <= n?")
@proc(j0, "j ← 1")
@dec(cj, "j <= n?")
@io(p, "Mostrar *")
@proc(jj, "j ← j + 1")
@io(nl, "Salto de línea")
@proc(ii, "i ← i + 1")
@term(f, "Fin")
l -> i0 -> ci; ci -> j0 [label=" Sí"]; j0 -> cj; cj -> p [label=" Sí"]; p -> jj; jj -> cj [constraint=false];
cj -> nl [label=" No"]; nl -> ii; ii -> ci [constraint=false]; ci -> f [label=" No"];
```

</div>
</div>

**C. Código en C**

```c run title="cuadrado.c" runs="3|5"
#include <stdio.h>
int main(void)
{
    int n;
    printf("Tamanio: ");
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)          //> n filas
    {
        for (int j = 1; j <= n; j++)      //> n columnas en cada fila
            printf("* ");
        printf("\n");                     //> fin de la fila
    }
    return 0;
}
```

**D. Verificación.** Para `n = 3` el cuerpo interno se ejecutó 3 × 3 = 9 veces (9 asteriscos) y hubo 3 saltos de línea.
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.18; ranksep=0.3;
@term(a, "Ciclos anidados")
@proc(e, "externo: filas (i)")
@proc(n, "interno: columnas (j)\nse reinicia en cada i")
@proc(c, "vueltas = n × m")
@proc(t, "límite que depende de i\n→ triángulos, pirámides")
@sub(b, "break: sale del ciclo\nmás interno")
@sub(k, "continue: salta a la\nsiguiente vuelta")
@hl(f, "bandera para salir\nde dos ciclos")
a -> e -> n; n -> c; n -> t; a -> b; a -> k; b -> f [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1 · Catálogo de patrones (n = 4) | Variabilidad, Interactividad de elementos
**Plantilla:** `for (filas) { for (espacios) putchar(' '); for (símbolos) putchar('*'); putchar('\n'); }` — `putchar(c)` muestra **un solo carácter** (equivale a `printf("%c", c)`).

| Figura | Espacios en la fila `i` | Símbolos en la fila `i` |
|---|---|---|
| Rectángulo `n × m` | 0 | `m` |
| Triángulo rectángulo | 0 | `i` |
| Triángulo invertido | 0 | `n - i + 1` |
| Triángulo alineado a la derecha | `n - i` | `i` |
| Pirámide centrada | `n - i` | `2 * i - 1` |

```c run title="patrones.c"
#include <stdio.h>
int main(void)
{
    int n = 4;
    for (int i = 1; i <= n; i++)                         // alineado a la derecha
    {
        for (int e = 1; e <= n - i; e++) putchar(' ');
        for (int s = 1; s <= i; s++) putchar('*');
        putchar('\n');
    }
    for (int i = 1; i <= n; i++)                         // piramide centrada
    {
        for (int e = 1; e <= n - i; e++) putchar(' ');
        for (int s = 1; s <= 2 * i - 1; s++) putchar('*');
        putchar('\n');
    }
    return 0;
}
```

| Sentencia | Efecto |
|---|---|
| `break;` | sale del ciclo (o `switch`) más interno |
| `continue;` | salta a la siguiente iteración del ciclo más interno |
| `return 0;` | termina `main` (y con ella todos los ciclos) |
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿Dibujé la figura en papel cuadriculado y escribí la tabla fila → espacios → símbolos?</li>
<li>¿Uso variables <b>distintas</b> para cada ciclo (<code>i</code>, <code>j</code>)?</li>
<li>¿El salto de línea está después del ciclo interno y dentro del externo?</li>
<li>¿Las variables que deben empezar de nuevo en cada fila (contadores, sumas por fila) se inicializan <b>dentro</b> del externo?</li>
<li>¿Mi <code>break</code> sale del ciclo que yo creo? (Solo del más interno.)</li>
<li>¿Cuántas vueltas da el cuerpo interno? ¿Coincide con lo que espero?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) La misma variable en ambos ciclos.** ¿Por qué solo aparece una fila?

```c run
#include <stdio.h>
int main(void)
{
    int i;
    for (i = 1; i <= 3; i++)
    {
        for (i = 1; i <= 4; i++)    //> El interno deja i en 5...
            printf("*");
        printf("\n");               //> ...y el externo termina porque 5 > 3
    }
    return 0;
}
```
*Corrección:* usar `j` en el ciclo interno.

**b) Salto de línea dentro del ciclo interno.** Cada asterisco queda en su propio renglón:

```c run
#include <stdio.h>
int main(void)
{
    for (int i = 1; i <= 2; i++)
        for (int j = 1; j <= 3; j++)
            printf("*\n");              //> El \n debería ir fuera del for de j
    return 0;
}
```

**c) Acumulador por fila que no se reinicia.** Para sumar cada fila por separado, `int sumaFila = 0;` debe ir **dentro** del externo y **antes** del interno.

**d) Esperar que `break` salga de ambos ciclos.** Usa una bandera (concepto 8).
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Mapa de asientos | Variabilidad
El mismo esquema filas × columnas, ahora con letras para las filas (`char` también se puede incrementar):

```c run title="asientos.c"
#include <stdio.h>
int main(void)
{
    for (char fila = 'A'; fila <= 'C'; fila++)     //> 'A', 'B', 'C' (códigos 65, 66, 67)
    {
        for (int asiento = 1; asiento <= 6; asiento++)
            printf("%c%d ", fila, asiento);
        printf("\n");
    }
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Antes de cada figura, dibújala en papel cuadriculado.

:::tarea A | T1. El rectángulo de símbolos: ejemplo y gemelo | 20 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia** cómo se generaliza el cuadrado del ejemplo a un rectángulo de `f` filas y `c` columnas con un símbolo elegido por el usuario:

```c run title="rect_simbolo.c" stdin="3 7 #\n"
#include <stdio.h>
int main(void)
{
    int f, c;
    char s;
    printf("Filas, columnas y simbolo: ");
    scanf("%d %d %c", &f, &c, &s);
    for (int i = 1; i <= f; i++)        //> El externo usa f
    {
        for (int j = 1; j <= c; j++)    //> El interno usa c: ya no es un cuadrado
            putchar(s);
        putchar('\n');
    }
    return 0;
}
```

**Paso 2 · Gemelo.** Un estadio tiene filas identificadas con letras (de la `A` a la letra que indique el usuario) y `n` asientos por fila. Muestra el mapa: `A1 A2 … An` en la primera fila, `B1 B2 …` en la segunda, etc. (ver ejemplo 2.4).

:::solucion | T1
```c run title="estadio.c" stdin="D 5\n"
#include <stdio.h>
int main(void)
{
    char ultima;
    int n;
    printf("Ultima fila y asientos por fila: ");
    scanf(" %c %d", &ultima, &n);
    for (char fila = 'A'; fila <= ultima; fila++)
    {
        for (int a = 1; a <= n; a++)
            printf("%c%d ", fila, a);
        printf("\n");
    }
    return 0;
}
```
:::
:::

:::tarea A | T2. Triángulo de números (completa con pistas) | 20 min | Problema por completar
**Contexto.** Para una actividad de primaria se necesita este patrón para `n = 5`:

```console title="Salida esperada"
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

```c blank title="triangulo_numeros.c"
#include <stdio.h>
int main(void)
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= __1__; i++)        // 1: cuantas filas hay
    {
        for (int j = 1; j <= __2__; j++)    // 2: la fila i tiene i numeros
            printf("%d ", __3__);           // 3: que numero se muestra (cambia en cada columna)
        __4__                               // 4: termina la fila
    }
    return 0;
}
```

:::solucion | T2
{{c:1}} `n` · {{c:2}} `i` · {{c:3}} `j` · {{c:4}} `printf("\n");`

```c run title="triangulo_numeros.c" stdin="5\n"
#include <stdio.h>
int main(void)
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
            printf("%d ", j);
        printf("\n");
    }
    return 0;
}
```
Variante: si en el hueco {{c:3}} pones `i`, obtienes `1`, `2 2`, `3 3 3`… ¡Pruébalo!
:::
:::

:::tarea AB | T3. Tabla de multiplicar completa (completa sin pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Imprimir las tablas del 1 al 10 como una cuadrícula, con encabezado de columnas y alineadas con un ancho de 4.

```c blank title="tabla_completa.c"
#include <stdio.h>
int main(void)
{
    printf("    ");
    for (int c = 1; c <= 10; c++)
        printf(__1__, c);
    printf("\n");
    for (__2__; __3__; __4__)
    {
        printf("%4d", f);
        for (int c = 1; c <= 10; c++)
            printf("%4d", __5__);
        __6__
    }
    return 0;
}
```

:::solucion | T3
{{c:1}} `"%4d"` · {{c:2}} `int f = 1` · {{c:3}} `f <= 10` · {{c:4}} `f++` · {{c:5}} `f * c` · {{c:6}} `printf("\n");`

```c run title="tabla_completa.c"
#include <stdio.h>
int main(void)
{
    printf("    ");
    for (int c = 1; c <= 10; c++)
        printf("%4d", c);
    printf("\n");
    for (int f = 1; f <= 10; f++)
    {
        printf("%4d", f);
        for (int c = 1; c <= 10; c++)
            printf("%4d", f * c);
        printf("\n");
    }
    return 0;
}
```
:::
:::

:::tarea AB | T4. Números primos hasta N (problema convencional) | 30 min | Variabilidad
**Contexto.** Los números primos son la base de la criptografía que protege tus mensajes. Lee `N` y muestra todos los primos entre 2 y `N`. **Idea:** para cada candidato `x` (ciclo externo), busca un divisor entre 2 y `x − 1` (ciclo interno); si lo encuentras, `x` no es primo y puedes salir con `break`. Muestra también cuántos primos encontraste.

**Ruta B:** basta probar divisores hasta `√x` (`d * d <= x`). Cuenta las iteraciones del ciclo interno con y sin esta mejora para `N = 1000`.

:::solucion | T4
```c run title="primos.c" stdin="50\n"
#include <stdio.h>
#include <stdbool.h>
int main(void)
{
    int N, cuantos = 0;
    printf("N: ");
    scanf("%d", &N);
    for (int x = 2; x <= N; x++)
    {
        bool primo = true;
        for (int d = 2; d * d <= x; d++)   // con d < x tambien funciona, pero hace mas vueltas
        {
            if (x % d == 0)
            {
                primo = false;
                break;                     // ya sabemos que no es primo
            }
        }
        if (primo)
        {
            printf("%d ", x);
            cuantos++;
        }
    }
    printf("\n%d primos\n", cuantos);
    return 0;
}
```
:::
:::

:::tarea A | T5. Galería de figuras (solución libre) | 30 min | Solución libre, Variabilidad
**Contexto.** Con `n = 4`, **dibuja todas las figuras que puedas** con asteriscos usando ciclos anidados: rectángulo, triángulo, triángulo invertido, triángulo alineado a la derecha, pirámide, cuadrado hueco, diagonal, letra X… No hay una lista obligatoria. Para cada figura, escribe primero su tabla «fila → espacios → símbolos».

:::solucion | T5
Algunas figuras posibles:

```c run title="galeria.c"
#include <stdio.h>
int main(void)
{
    int n = 4;
    printf("Invertido:\n");
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n - i + 1; j++) putchar('*');
        putchar('\n');
    }
    printf("Cuadrado hueco:\n");
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            putchar((i == 1 || i == n || j == 1 || j == n) ? '*' : ' ');
        putchar('\n');
    }
    printf("Diagonal:\n");
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            putchar(i == j ? '*' : '.');
        putchar('\n');
    }
    printf("Letra X:\n");
    for (int i = 1; i <= n + 1; i++)
    {
        for (int j = 1; j <= n + 1; j++)
            putchar((i == j || i + j == n + 2) ? '*' : ' ');
        putchar('\n');
    }
    return 0;
}
```
:::
:::

:::tarea B | T6. Depura la tabla de sumas (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
**Contexto.** El programa debía mostrar, para cada fila `i` de 1 a 3, la suma `i + 1 + i + 2 + … + i + 4`… pero la salida está mal. Explica **por qué** la segunda y la tercera suma son incorrectas y corrígelo.

```c run title="sumas_bug.c"
#include <stdio.h>
int main(void)
{
    int suma = 0;
    for (int i = 1; i <= 3; i++)
    {
        for (int j = 1; j <= 4; j++)
            suma += i + j;
        printf("Fila %d: %d\n", i, suma);
    }
    return 0;
}
```

{{lineas:3}}

:::solucion | T6
`suma` se inicializa **una sola vez**, antes del ciclo externo, así que las filas 2 y 3 siguen acumulando lo de las anteriores (14, 14 + 18 = 32, 32 + 22 = 54). Debe reiniciarse **dentro** del externo:

```c run title="sumas.c"
#include <stdio.h>
int main(void)
{
    for (int i = 1; i <= 3; i++)
    {
        int suma = 0;                 // se reinicia para cada fila
        for (int j = 1; j <= 4; j++)
            suma += i + j;
        printf("Fila %d: %d\n", i, suma);
    }
    return 0;
}
```
:::
:::

:::tarea B | T7. ¿Qué imprime? `break` y `continue` anidados (imaginación) | 20 min | Imaginación
**Sin ejecutar**, imagina el recorrido y escribe la salida exacta. Después cuenta cuántas veces se evaluó la condición `j <= 4`.

```c check title="saltos.c"
#include <stdio.h>
int main(void)
{
    for (int i = 1; i <= 3; i++)
    {
        for (int j = 1; j <= 4; j++)
        {
            if (j == i)
                continue;
            if (i * j > 6)
                break;
            printf("%d%d ", i, j);
        }
        printf("| ");
    }
    printf("\n");
    return 0;
}
```

{{lineas:2}}

:::solucion | T7
`i = 1`: `j = 1` se salta (j == i); 12, 13, 14. `i = 2`: 21; `j = 2` se salta; 23; `j = 4` → 8 > 6, `break`. `i = 3`: 31, 32; `j = 3` se salta; `j = 4` → 12 > 6, `break`.

```c run title="saltos.c"
#include <stdio.h>
int main(void)
{
    for (int i = 1; i <= 3; i++)
    {
        for (int j = 1; j <= 4; j++)
        {
            if (j == i)
                continue;
            if (i * j > 6)
                break;
            printf("%d%d ", i, j);
        }
        printf("| ");
    }
    printf("\n");
    return 0;
}
```
La condición `j <= 4` se evaluó 5 veces para `i = 1` (incluida la que sale), 4 para `i = 2` y 4 para `i = 3`: 13 en total.
:::
:::

:::tarea AB | T8. Batalla naval en miniatura (reto colaborativo) | 40 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Equipos de 4 con niveles mezclados. Tablero de 6 × 6. Un barco ocupa la fila 3, columnas 2 a 4 (constantes). El jugador escribe un disparo `(fila, columna)`; el programa muestra el tablero: `X` si el disparo dio en el barco, `o` si cayó al agua, `.` en las demás casillas, y el mensaje «¡Impacto!» o «Agua».

- **Integrante 1:** encabezado de columnas (`  1 2 3 4 5 6`) y etiqueta de cada fila.
- **Integrante 2:** el ciclo anidado que recorre las 36 casillas.
- **Integrante 3:** la decisión de qué símbolo va en cada casilla.
- **Integrante 4:** validación del disparo (1–6) con `do-while` y el mensaje final.
:::

:::solucion | T8
```c run title="naval.c" runs="3 3|5 1|9 9\n1 6"
#include <stdio.h>
#include <stdbool.h>
#define N 6
#define FILA_BARCO 3
#define COL_INI 2
#define COL_FIN 4
int main(void)
{
    int f, c;
    do {
        printf("Disparo (fila columna, 1-6): ");
        scanf("%d %d", &f, &c);
    } while (f < 1 || f > N || c < 1 || c > N);
    bool impacto = (f == FILA_BARCO && c >= COL_INI && c <= COL_FIN);
    printf("  ");
    for (int j = 1; j <= N; j++) printf("%d ", j);
    printf("\n");
    for (int i = 1; i <= N; i++)
    {
        printf("%d ", i);
        for (int j = 1; j <= N; j++)
        {
            if (i == f && j == c)
                printf("%c ", impacto ? 'X' : 'o');
            else
                printf(". ");
        }
        printf("\n");
    }
    printf(impacto ? "Impacto!\n" : "Agua\n");
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Un experto dibuja una pirámide centrada | Modalidad, Ejemplo resuelto
*Guion segmentado (≈ 3 min), con papel cuadriculado y código en pantalla.*

**Problema:** «Dibujar una pirámide de altura `n` centrada, por ejemplo para `n = 4`».

**Segmento 1 — Dibujo y tabla.** {{como}} Dibujo la pirámide en papel cuadriculado y hago una tabla: fila 1 → 3 espacios y 1 asterisco; fila 2 → 2 espacios y 3; fila 3 → 1 y 5; fila 4 → 0 y 7. {{porque}} El código no se adivina: se **deduce** de la tabla.

**Segmento 2 — Encontrar las fórmulas.** {{como}} Los espacios bajan de 1 en 1 desde `n − 1`: son `n − i`. Los asteriscos suben de 2 en 2 empezando en 1: son `2i − 1`. Lo compruebo con la fila 3: `4 − 3 = 1` espacio y `2·3 − 1 = 5` asteriscos. {{porque}} Comprobar la fórmula con una fila **intermedia** detecta errores que con la primera fila pasarían inadvertidos.

**Segmento 3 — Dos ciclos internos en secuencia.** {{como}} Dentro del ciclo de filas pongo **dos** ciclos, uno tras otro: primero los espacios, luego los asteriscos, y al final el salto de línea. {{porque}} Cada fila tiene dos partes distintas; anidarlas entre sí sería un error, deben ir en secuencia.

**Segmento 4 — Probar casos pequeños y grandes.** {{como}} Pruebo `n = 1` (un solo asterisco) y `n = 4`. {{porque}} El caso mínimo revela errores por uno en los límites.

```c run title="piramide.c" runs="1|4"
#include <stdio.h>
int main(void)
{
    int n;
    printf("Altura: ");
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        for (int e = 1; e <= n - i; e++)
            putchar(' ');
        for (int s = 1; s <= 2 * i - 1; s++)
            putchar('*');
        putchar('\n');
    }
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. En un ciclo anidado, ¿qué ciclo completa todas sus vueltas por cada vuelta del otro?
2. Si el externo da 5 vueltas y el interno 8, ¿cuántas veces se ejecuta el cuerpo interno?
3. ¿Dónde debe ir el salto de línea al dibujar una figura por filas?
4. ¿Qué hace `break` dentro de un ciclo anidado?
5. ¿Qué hace `continue`?
6. Verdadero o falso: se puede usar la misma variable `i` en el ciclo externo y en el interno.
7. ¿Qué es una bandera y para qué sirve en ciclos anidados?
8. Para un triángulo rectángulo, ¿cuál es el límite del ciclo interno en la fila `i`?
9. ¿Qué especificador de `printf` muestra un entero alineado en una columna de 5 espacios?
10. ¿Por qué la programación estructurada evita `goto`?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida:**

```c check title="p1.c"
#include <stdio.h>
int main(void)
{
    for (int i = 3; i >= 1; i--)
    {
        for (int j = 1; j <= i; j++)
            printf("%d", i);
        printf("\n");
    }
    return 0;
}
```

**P2. Escribe la tabla** «fila → espacios → símbolos» y el programa para este patrón con `n = 4`:

```console title="Patrón"
****
 ***
  **
   *
```

**P3. Corrige:** debía mostrar 3 filas de 5 guiones, pero muestra 15 renglones con un guion cada uno: `for (int i=0;i<3;i++) for (int j=0;j<5;j++) printf("-\n");`

**P4. Escribe un programa** que muestre todos los números perfectos menores que 10 000 (un número es perfecto si es igual a la suma de sus divisores propios; por ejemplo, 6 = 1 + 2 + 3).
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Explico cómo se ejecuta un ciclo dentro de otro y calculo cuántas vueltas da.</li>
<li>Deduzco las fórmulas de espacios y símbolos de una figura.</li>
<li>Uso <code>break</code> y <code>continue</code> sabiendo de qué ciclo salen.</li>
<li>Resuelvo búsquedas con salida temprana (primos, divisores).</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 El interno · 2 40 · 3 Después del ciclo interno, dentro del externo · 4 Termina solo el ciclo más interno que lo contiene · 5 Salta el resto del cuerpo y pasa a la siguiente iteración · 6 Falso: el interno modificaría la variable del externo · 7 Una variable `bool` que se activa al cumplirse algo; el ciclo externo la consulta para terminar también · 8 `j <= i` · 9 `%5d` · 10 Porque permite saltar a cualquier punto y vuelve el flujo difícil de seguir y de depurar.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.**

```c run title="p1.c"
#include <stdio.h>
int main(void)
{
    for (int i = 3; i >= 1; i--)
    {
        for (int j = 1; j <= i; j++)
            printf("%d", i);
        printf("\n");
    }
    return 0;
}
```

**P2.** Fila `i` → `i − 1` espacios y `n − i + 1` asteriscos:

```c run title="p2.c"
#include <stdio.h>
int main(void)
{
    int n = 4;
    for (int i = 1; i <= n; i++)
    {
        for (int e = 1; e <= i - 1; e++) putchar(' ');
        for (int s = 1; s <= n - i + 1; s++) putchar('*');
        putchar('\n');
    }
    return 0;
}
```

**P3.** El `\n` está dentro del ciclo interno. Corrección: `for (int i=0;i<3;i++) { for (int j=0;j<5;j++) printf("-"); printf("\n"); }`

**P4.**

```c run title="perfectos.c"
#include <stdio.h>
int main(void)
{
    for (int n = 2; n < 10000; n++)
    {
        int suma = 1;                       // 1 siempre divide
        for (int d = 2; d * d <= n; d++)
            if (n % d == 0)
            {
                suma += d;
                if (d != n / d) suma += n / d;   // su pareja de divisor
            }
        if (suma == n)
            printf("%d ", n);
    }
    printf("\n");
    return 0;
}
```
:::
