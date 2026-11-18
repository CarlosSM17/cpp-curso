---
num: "08"
archivo: "Tema08_Arreglos_unidimensionales_vectores"
titulo: "Arreglos unidimensionales (vectores)"
corto: "Arreglos (vectores)"
lema: "Muchos datos del mismo tipo, un solo nombre y un número de casilla para cada uno."
duracion: "6 h · 3 sesiones de 2 h"
previos: "Tema 06 y Tema 07 (ciclos `for`, contadores, acumuladores, ciclos anidados)."
fuentes:
  - "Kernighan, B. W. y Ritchie, D. M. (1988). *The C Programming Language* (2.ª ed.). Prentice Hall. Cap. 1: §1.6 Arrays. Cap. 4: §4.9 Initialization (arreglos). Apéndice B, §B5 (`rand`, `srand`)."
  - "King, K. N. (2008). *C Programming: A Modern Approach* (2.ª ed.). W. W. Norton. Cap. 8: §8.1 One-Dimensional Arrays, §8.3 Variable-Length Arrays."
  - "Seacord, R. C. (2020). *Effective C*. No Starch Press. Cap. 2 (arreglos como tipos derivados) y Cap. 11 «Debugging, Testing, and Analysis» (AddressSanitizer)."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §6.1.1–6.1.17: ejemplos de arreglos (llenado con tamaño TAM, ordenamiento burbuja y selección) para los efectos de la TCC."
objetivos:
  A:
    - "Declarar e inicializar arreglos y acceder a sus elementos por índice (de 0 a n − 1)."
    - "Recorrer arreglos con `for` para capturar, mostrar, sumar, promediar y encontrar máximo y mínimo."
    - "Buscar un valor (búsqueda secuencial) y contar ocurrencias."
    - "Ordenar un arreglo con el método de la burbuja."
  B:
    - "Calcular el número de elementos con `sizeof(a) / sizeof(a[0])` y explicar los arreglos de longitud variable (VLA) y sus riesgos."
    - "Explicar el acceso fuera de rango (comportamiento indefinido) y detectarlo con `-fsanitize=address`."
    - "Implementar el ordenamiento por selección y compararlo con la burbuja."
    - "Llenar arreglos con números aleatorios (`rand`, `srand`) y verificar los resultados."
efectos:
  soporte:
    - ["Elementos aislados", "Necesidad → declaración e índices → inicialización → recorrido → patrones → búsqueda → aleatorios → ordenamiento."]
    - ["Atención dividida", "Burbuja explicada con una traza visual integrada: explicación, estado del arreglo y código en un mismo lugar (tesis §6.1.4)."]
    - ["Ejemplo resuelto", "Crear y llenar un arreglo de tamaño TAM: algoritmo → pseudocódigo → C comentado (tesis §6.1.2)."]
    - ["Movimiento humano", "«Burbuja humana»: estudiantes con tarjetas se ordenan intercambiando lugares."]
  procedimental:
    - ["Variabilidad", "Mismos patrones de recorrido en contextos distintos (temperaturas, ventas, votos)."]
    - ["Autogestión", "T9: rediseñar material mal diseñado sobre la burbuja (tesis §6.1.17)."]
  tareas:
    - ["Ejemplo resuelto", "T1: temperaturas de la semana + gemelo (ventas)."]
    - ["Problema por completar", "T2: la versión por completar del ejemplo TAM (tesis §6.1.3); T3: búsqueda sin pistas."]
    - ["Desvanecimiento de guía", "T1 → T4."]
    - ["Solución libre", "T5: ordenar {5, 6, 2, 3, 8, 1, 7, 4} con cualquier algoritmo (tesis §6.1.1)."]
    - ["Autoexplicación", "T6: explicar a tus compañeros los bloques del programa de la burbuja (tesis §6.1.6)."]
    - ["Imaginación", "T7: imaginar el ordenamiento por selección a partir de su descripción (tesis §6.1.10)."]
    - ["Memoria colectiva de trabajo", "T8: sistema de votación escolar."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Arreglos con tamaño `#define`, recorridos, búsqueda, burbuja con traza visual."
    B: "`sizeof(a) / sizeof(a[0])`, VLA, `-fsanitize=address`, selección vs burbuja."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4; diagramas de casillas en papel; burbuja humana."
    B: "T5, T6, T7, T9 autónomas; coordinación de T8."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Estadísticas del grupo (T4) con dos recorridos del arreglo."
    B: "Comparación burbuja vs selección con conteo de comparaciones (T7)."
  Entorno:
    comp: "Información procedimental"
    A: "Depurador mostrando el arreglo completo en cada iteración."
    B: "Compilación con `-g -fsanitize=address` para detectar accesos fuera de rango."
plan:
  - ["Sesión 1", "Soporte", "Pregunta inicial; conceptos 1–5; ejemplo resuelto TAM; T1 y T2.", "120 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–9; burbuja humana; T3, T4; Ruta B: T6, T7.", "120 min"]
  - ["Sesión 3", "Tareas + evaluación", "T5, T8 colaborativa, T9 (Ruta B), protocolo verbal, tests.", "120 min"]
glosario:
  - ["arreglo / vector", "array", "Colección de elementos del mismo tipo guardados de forma contigua bajo un nombre."]
  - ["elemento", "element", "Cada valor guardado en el arreglo."]
  - ["índice / subíndice", "index", "Posición de un elemento; en C empieza en 0."]
  - ["tamaño", "size / length", "Número de elementos del arreglo."]
  - ["recorrido", "traversal", "Visitar cada elemento, normalmente con un `for`."]
  - ["búsqueda secuencial", "linear search", "Revisar los elementos uno por uno hasta encontrar el buscado."]
  - ["ordenamiento burbuja", "bubble sort", "Comparar vecinos e intercambiarlos si están en desorden, en varias pasadas."]
  - ["ordenamiento por selección", "selection sort", "Buscar el menor y colocarlo al inicio; repetir con el resto."]
  - ["intercambio", "swap", "Cambiar de lugar dos valores usando una variable auxiliar."]
  - ["fuera de rango", "out of bounds", "Acceder a un índice que no existe; produce comportamiento indefinido."]
  - ["comportamiento indefinido", "undefined behavior", "El estándar no dice qué pasa: puede funcionar, fallar o corromper datos."]
  - ["arreglo de longitud variable", "variable-length array (VLA)", "Arreglo cuyo tamaño se decide en ejecución (`int a[n];`); no se puede inicializar con valores."]
  - ["semilla", "seed (`srand`)", "Valor inicial del generador de números pseudoaleatorios."]
---

# 1. Información de soporte {.soporte}

:::analogia | Los casilleros numerados del gimnasio
Imagina una pared con 30 casilleros **iguales**, uno junto a otro, con un solo letrero arriba que dice «Equipo de fútbol» y un número en cada puerta: 0, 1, 2… 29. Para guardar o sacar algo no necesitas 30 nombres distintos: dices «Equipo de fútbol, casillero 7». Un **arreglo** es eso: muchas cajas del mismo tipo, un solo nombre y un **índice** para cada una.
:::

:::pregunta
Necesitas guardar las calificaciones de los 40 estudiantes de tu grupo y luego decir cuántos están **por encima del promedio**. Con lo que sabes hasta ahora (variables sueltas), **¿cómo lo harías? ¿Cuántas variables necesitarías?**

{{lineas:2}}
:::

:::relevancia
Las listas están en todas partes: los puntajes más altos de un juego, las lecturas de un sensor cada segundo, los píxeles de una fila de la pantalla, las canciones de una lista de reproducción. Los arreglos permiten **guardar** muchos datos y **procesarlos con ciclos**, y son la puerta a los algoritmos de búsqueda y ordenamiento que usan todas las aplicaciones. En C, además, son la estructura más cercana a la memoria real de la computadora. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | ¿Por qué arreglos? | Elementos aislados, Atención dividida
<div class="cols eq">
<div>

```c check title="sin arreglo"
#include <stdio.h>
int main(void)
{
    double c1, c2, c3, c4, c5;
    scanf("%lf %lf %lf %lf %lf", &c1, &c2, &c3, &c4, &c5);
    double prom = (c1 + c2 + c3 + c4 + c5) / 5;
    // ¿Cuantas superan el promedio?
    int arriba = 0;
    if (c1 > prom) arriba++;
    if (c2 > prom) arriba++;
    if (c3 > prom) arriba++;
    if (c4 > prom) arriba++;
    if (c5 > prom) arriba++;
    printf("%d\n", arriba);
    return 0;
}
```

</div>
<div>

```c check title="con arreglo"
#include <stdio.h>
#define N 5
int main(void)
{
    double c[N], suma = 0;
    for (int i = 0; i < N; i++)
    {
        scanf("%lf", &c[i]);
        suma += c[i];
    }
    double prom = suma / N;
    int arriba = 0;
    for (int i = 0; i < N; i++)
        if (c[i] > prom) arriba++;
    printf("%d\n", arriba);
    return 0;
}
```

</div>
</div>

Con 40 alumnos, la versión de la izquierda necesitaría 40 variables y 40 `if`; a la derecha solo cambias `#define N 40`. Y observa: hacen falta **dos** recorridos (primero el promedio, luego comparar), así que los datos deben **guardarse**.
:::

:::concepto | 2 | Declaración, índices y memoria | Elementos aislados, Atención dividida
`tipo nombre[TAMAÑO];` reserva `TAMAÑO` casillas **contiguas** en memoria. Los índices van de **0** a **TAMAÑO − 1**.

```c run
#include <stdio.h>
int main(void)
{
    int edades[5] = {12, 15, 9, 20, 17};          //> 5 enteros: índices 0, 1, 2, 3 y 4
    printf("Primero: %d\n", edades[0]);           //> El primer elemento es el [0]
    printf("Ultimo:  %d\n", edades[4]);           //> El último es el [TAMAÑO − 1]
    edades[2] = 10;                               //> Un elemento se usa como cualquier variable
    printf("Nuevo [2]: %d\n", edades[2]);
    printf("Bytes: %zu\n", sizeof(edades));       //> 5 × 4 bytes = 20
    return 0;
}
```

```diagram arr
name: edades
type: "int[5]"
vals: [12, 15, 10, 20, 17]
hl: [2]
addr: "0x1000"
step: 4
figcaption: "Figura 1. Cinco enteros contiguos: cada casilla ocupa 4 bytes; el índice indica cuántas casillas se avanza desde el inicio."
```
:::

:::concepto | 3 | Formas de inicializar | Elementos aislados
| Declaración | Contenido |
|---|---|
| `int a[5] = {4, 8, 15, 16, 23};` | 4 8 15 16 23 |
| `int b[5] = {7, 3};` | 7 3 0 0 0 (el resto se llena con ceros) |
| `int c[5] = {0};` | 0 0 0 0 0 |
| `int d[] = {1, 2, 3};` | el tamaño (3) se deduce de la lista |
| `int e[5];` | **basura**: sin inicializar |

El tamaño debe ser una **constante del compilador**; en C se escribe con `#define`: `#define N 40` … `int notas[N];`. Ojo: en C, `const int N = 40;` **no** sirve para esto (lo verás en los errores frecuentes 2.3). Si el tamaño lo decide el usuario, usa una capacidad máxima (`MAX`) y valida (ejemplo 1.2).
:::

:::concepto | 4 | Recorrer: el `for` de 0 a N − 1 | Elementos aislados, Atención dividida
El patrón que usarás en casi todos los programas con arreglos:

```c run title="captura_muestra.c" stdin="23.5\n25\n27.1\n22\n19.8\n"
#include <stdio.h>
#define N 5
int main(void)
{
    double temp[N];
    for (int i = 0; i < N; i++)                          //> `i < N` (no `<=`): el último índice es N − 1
    {
        printf("Temperatura del dia %d: ", i + 1);       //> Para el usuario los días empiezan en 1
        scanf("%lf", &temp[i]);                          //> Cada casilla es una variable: lleva `&`
    }
    printf("Registradas:");
    for (int i = 0; i < N; i++)
        printf(" %.1f", temp[i]);                        //> Muestra cada casilla
    printf("\n");
    return 0;
}
```
:::

:::concepto | 5 | Patrones: suma, promedio, máximo y mínimo | Elementos aislados, Atención dividida
```c run title="estadisticas.c"
#include <stdio.h>
#define N 6
int main(void)
{
    int ventas[N] = {120, 340, 95, 410, 260, 180};
    int suma = 0;
    int posMax = 0, posMin = 0;            //> Guardamos la POSICIÓN del mayor y del menor
    for (int i = 0; i < N; i++)
    {
        suma += ventas[i];                 //> Acumulador
        if (ventas[i] > ventas[posMax]) posMax = i;   //> ¿Hay uno mayor que el mejor hasta ahora?
        if (ventas[i] < ventas[posMin]) posMin = i;
    }
    printf("Total: %d  Promedio: %.2f\n", suma, (double)suma / N);
    printf("Mejor mes: %d (%d)\n", posMax + 1, ventas[posMax]);
    printf("Peor mes:  %d (%d)\n", posMin + 1, ventas[posMin]);
    return 0;
}
```
**Clave del máximo:** empieza suponiendo que el mejor es el **primero** (no 0, porque podría haber valores negativos).
:::

:::concepto | 6 | Búsqueda secuencial | Elementos aislados
Revisar uno por uno hasta encontrar el valor buscado:

```c run title="busqueda.c" runs="41|7"
#include <stdio.h>
#define N 8
int main(void)
{
    int folios[N] = {17, 3, 41, 8, 25, 41, 12, 30};
    int buscado, pos = -1;                  //> -1 significa «no encontrado»
    printf("Folio a buscar: ");
    scanf("%d", &buscado);
    for (int i = 0; i < N; i++)
    {
        if (folios[i] == buscado)
        {
            pos = i;
            break;                          //> Primera aparición: ya no seguimos
        }
    }
    if (pos != -1)
        printf("Encontrado en la posicion %d\n", pos);
    else
        printf("No existe\n");
    return 0;
}
```
:::

:::concepto | 7 | Llenado aleatorio (`rand` y `srand`) | Elementos aislados
Para pruebas y juegos se llenan arreglos con números pseudoaleatorios:

```c run title="aleatorios.c"
#include <stdio.h>
#include <stdlib.h>         //> rand, srand
#include <time.h>           //> time
#define N 10
int main(void)
{
    int dados[N];
    srand(42);              //> Semilla fija: misma secuencia siempre (útil para probar). Con srand(time(NULL)) cambia en cada ejecución
    for (int i = 0; i < N; i++)
        dados[i] = rand() % 6 + 1;   //> rand() % 6 da 0..5; +1 da 1..6
    for (int i = 0; i < N; i++)
        printf("%d ", dados[i]);
    printf("\n");
    return 0;
}
```
*En tu computadora los números pueden ser distintos: cada biblioteca de C implementa `rand` a su manera.*
:::

:::concepto | 8 | Ordenamiento burbuja: explicación, traza y código integrados | Elementos aislados, Atención dividida
**Idea:** recorrer el arreglo comparando cada elemento con su **vecino**; si están en desorden, se **intercambian**. Al terminar la primera pasada, el mayor «burbujea» hasta el final. Se repite con el resto.

```diagram arrs
rows:
  - {label: "Inicio", vals: [5, 3, 8, 1, 4]}
  - {label: "P1 · compara [0],[1]", vals: [3, 5, 8, 1, 4], hl: [0, 1], swap: true, note: "5 > 3 → intercambia"}
  - {label: "P1 · compara [1],[2]", vals: [3, 5, 8, 1, 4], hl: [1, 2], note: "5 < 8 → no cambia"}
  - {label: "P1 · compara [2],[3]", vals: [3, 5, 1, 8, 4], hl: [2, 3], swap: true, note: "8 > 1 → intercambia"}
  - {label: "P1 · compara [3],[4]", vals: [3, 5, 1, 4, 8], hl: [3, 4], swap: true, note: "8 > 4 → intercambia"}
  - {label: "Fin pasada 1", vals: [3, 5, 1, 4, 8], ok: [4], note: "el 8 ya está en su lugar"}
  - {label: "Fin pasada 2", vals: [3, 1, 4, 5, 8], ok: [3, 4], note: "el 5 se acomoda"}
  - {label: "Fin pasada 3", vals: [1, 3, 4, 5, 8], ok: [2, 3, 4]}
  - {label: "Fin pasada 4", vals: [1, 3, 4, 5, 8], ok: [0, 1, 2, 3, 4], note: "ordenado"}
figcaption: "Figura 2. Traza de la burbuja: amarillo = par comparado; verde = elementos ya en su posición final."
```

```c run title="burbuja.c"
#include <stdio.h>
#define N 5
int main(void)
{
    int v[N] = {5, 3, 8, 1, 4};
    for (int pasada = 1; pasada < N; pasada++)        //> N − 1 pasadas
    {
        for (int j = 0; j < N - pasada; j++)          //> En cada pasada, una comparación menos (el final ya está ordenado)
        {
            if (v[j] > v[j + 1])                      //> ¿El vecino de la derecha es menor?
            {
                int aux = v[j];                       //> Intercambio con variable auxiliar
                v[j] = v[j + 1];
                v[j + 1] = aux;
            }
        }
    }
    for (int i = 0; i < N; i++) printf("%d ", v[i]);
    printf("\n");
    return 0;
}
```

:::nota | ¿Por qué hace falta `aux`?
Si escribieras `v[j] = v[j + 1]; v[j + 1] = v[j];`, la primera asignación **destruye** el valor original de `v[j]` y ambos quedarían iguales. `aux` lo guarda temporalmente.
:::
:::

:::movimiento | Burbuja humana (15 min)
Seis estudiantes forman una fila con tarjetas numéricas al azar. Un «comparador» camina de izquierda a derecha: en cada par de vecinos, si el de la izquierda tiene número mayor, **ambos cambian de lugar**. Al llegar al final, el mayor queda en el extremo derecho y se sienta (ya está en su lugar). Se repiten las pasadas. El grupo cuenta cuántas comparaciones e intercambios hubo. Después prueben con la fila ya ordenada: ¿cuántos intercambios hay?
:::

:::concepto | 9 | Ruta B · Contar elementos con `sizeof`, arreglos de longitud variable y la ausencia de revisión de índices | Elementos aislados, Reversión de la experiencia
`sizeof` da el tamaño en **bytes**; dividido entre el tamaño de un elemento da el **número de elementos**. Y desde C99 existen los **arreglos de longitud variable** (VLA): su tamaño se decide en ejecución.

```c run title="tam_arreglo.c" stdin="4\n10 20 30 40\n"
#include <stdio.h>
int main(void)
{
    int primos[] = {2, 3, 5, 7, 11, 13};
    size_t cuantos = sizeof(primos) / sizeof(primos[0]);   //> Bytes totales / bytes de uno = elementos
    printf("primos tiene %zu elementos\n", cuantos);
    int n;
    scanf("%d", &n);
    if (n < 1 || n > 1000)                                 //> Valida ANTES de crear el VLA
        return 1;
    int datos[n];                                          //> VLA: tamaño decidido en ejecución
    int suma = 0;
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &datos[i]);
        suma += datos[i];
    }
    printf("%d datos, suma %d\n", n, suma);
    return 0;
}
```

Un VLA **no se puede inicializar** con `= {…}`, vive en una zona de memoria pequeña (la pila) y, si `n` es enorme o negativo, el programa falla sin aviso. En el Tema 15 verás `malloc`, la forma robusta de pedir memoria del tamaño que decida el usuario.

:::cuidado | C no revisa los índices
`int a[5]; a[5] = 1;` compila, pero escribe **fuera** del arreglo: es **comportamiento indefinido** (puede «funcionar», fallar o dañar otras variables). C no revisa los índices por ti. Mientras pruebas, compila con `gcc -g -fsanitize=address prog.c`: si te sales del arreglo, el programa se detiene y te dice en qué línea (*stack-buffer-overflow*).
:::
:::

## 1.2 Ejemplo resuelto: crear y llenar un arreglo de tamaño TAM

:::ejemplo | Arreglo de enteros con tamaño definido por el usuario (tesis §6.1.2) | Ejemplo resuelto, Atención dividida
**Problema.** Crear un programa en C que cree y llene un arreglo de números enteros, identificado como `vec`, cuyo tamaño lo define el usuario mediante la variable `TAM`. Al final, mostrar su contenido.

**A. Algoritmo**

1. Solicitar el tamaño del arreglo al usuario.
2. Guardar el valor en una variable (`TAM`), validando que no exceda el máximo.
3. Definir el arreglo del tamaño introducido.
4. Capturar el contenido del arreglo uno a uno hasta el tamaño solicitado (y mostrarlo).

**B. Pseudocódigo**

```pseudo
Algoritmo LlenarArreglo
    Definir TAM, i Como Entero
    Escribir "Tamanio del arreglo: "
    Leer TAM
    Dimension vec[TAM]
    Para i <- 1 Hasta TAM Hacer
        Escribir "Elemento ", i, ": "
        Leer vec[i]
    FinPara
    Para i <- 1 Hasta TAM Hacer
        Escribir Sin Saltar vec[i], " "
    FinPara
FinAlgoritmo
```

**C. Código en C** (cada línea comentada)

```c run title="llenar_arreglo.c" stdin="150\n4\n7\n-2\n13\n5\n"
#include <stdio.h>
#define MAX 100                               //> Tamaño máximo reservado (constante del compilador)
int main(void)
{
    int vec[MAX];                             //> Paso 3: arreglo con capacidad para MAX enteros
    int TAM;                                  //> Paso 2: aquí se guarda el tamaño pedido
    do
    {
        printf("Tamanio del arreglo (1-%d): ", MAX);   //> Paso 1: solicitar
        scanf("%d", &TAM);
    } while (TAM < 1 || TAM > MAX);           //> Validación: no exceder la capacidad
    for (int i = 0; i < TAM; i++)             //> Paso 4: capturar uno a uno (índices 0..TAM−1)
    {
        printf("Elemento %d: ", i + 1);
        scanf("%d", &vec[i]);
    }
    printf("Contenido:");
    for (int i = 0; i < TAM; i++)             //> Mostrar lo capturado
        printf(" %d", vec[i]);
    printf("\n");
    return 0;
}
```

**D. Verificación.** Con `150` el programa vuelve a preguntar, porque excede la capacidad `MAX`; con `4` captura exactamente cuatro elementos (índices 0 a 3) y los muestra en el mismo orden.
:::

:::pregunta | Autoexplícalo
¿Qué pasaría si quitaras el `do-while` y el usuario escribiera 150? ¿En qué casillas intentaría guardar el programa los elementos 101 a 150? ¿Por qué eso es peligroso aunque el programa compile?

{{lineas:2}}
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.18; ranksep=0.3;
@term(a, "Arreglo\ntipo nombre[N]")
@proc(i, "índices 0 … N−1\nmemoria contigua")
@proc(r, "recorrido\nfor (i = 0; i < N; i++)")
@proc(p, "patrones: suma · promedio\nmáx/mín · contar")
@proc(b, "búsqueda secuencial")
@proc(o, "ordenamiento\nburbuja · selección")
@sub(v, "#define N · sizeof(a)/sizeof(a[0])\nVLA · -fsanitize=address")
@hl(e, "¡fuera de rango =\ncomportamiento indefinido!")
a -> i; a -> r; r -> p; r -> b; r -> o; a -> v [style=dashed]; i -> e [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1
| Quiero… | Código |
|---|---|
| Declarar con tamaño constante | `#define N 10` … `int a[N];` |
| Declarar e inicializar | `int a[] = {3, 1, 4};` · `double b[N] = {0};` |
| Leer todos | `for (int i = 0; i < N; i++) scanf("%d", &a[i]);` |
| Mostrar todos | `for (int i = 0; i < N; i++) printf("%d ", a[i]);` |
| Sumar | `suma = 0; for (…) suma += a[i];` |
| Posición del mayor | `pm = 0; for (int i = 1; i < N; i++) if (a[i] > a[pm]) pm = i;` |
| Contar los que cumplen | `c = 0; for (…) if (cond(a[i])) c++;` |
| Buscar | `pos = -1; for (…) if (a[i] == x) { pos = i; break; }` |
| Intercambiar | `int aux = a[i]; a[i] = a[j]; a[j] = aux;` |
| Copiar un arreglo | `for (…) b[i] = a[i];` (no se puede `b = a;`) |
| Número de elementos | `sizeof(a) / sizeof(a[0])` (solo donde se declaró el arreglo) |
| Aleatorio entre 1 y k | `rand() % k + 1` (con `srand(time(NULL));` una vez; `<stdlib.h>` y `<time.h>`) |
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿El ciclo va de <code>0</code> a <code>N − 1</code> (<code>i &lt; N</code>)?</li>
<li>¿El tamaño del arreglo es un <code>#define</code>? ¿Validé que el tamaño pedido no exceda el máximo?</li>
<li>¿Inicialicé el arreglo o lo llené antes de leerlo?</li>
<li>¿En <code>a[i + 1]</code> el índice puede llegar a <code>N</code>? (Entonces el ciclo debe terminar en <code>N − 1</code>.)</li>
<li>Para el máximo/mínimo, ¿empecé con el primer elemento y no con 0?</li>
<li>¿Uso una variable auxiliar al intercambiar?</li>
<li>¿Puse <code>&amp;</code> en <code>scanf("%d", &amp;a[i])</code>?</li>
<li>¿Muestro al usuario posiciones desde 1 aunque internamente empiecen en 0?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) `<=` en lugar de `<`: lectura fuera del arreglo.** Con `-Wall` solo, gcc no dice nada; si además optimizas con `-O2`, analiza el ciclo y avisa que la última vuelta es comportamiento indefinido:

```c warn flags="-O2"
#include <stdio.h>
int main(void)
{
    int a[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i <= 5; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
*Corrección:* `i < 5`. El sexto valor que mostraría es basura (o el programa falla): `a[5]` no existe.

**b) Tamaño con `const int`.** En C++ funciona; en C, `N` es una variable de solo lectura y el arreglo se vuelve de longitud variable, que no admite inicializador:

```c err
#include <stdio.h>
int main(void)
{
    const int N = 5;
    int a[N] = {1, 2, 3, 4, 5};
    printf("%d\n", a[0]);
    return 0;
}
```
*Corrección:* `#define N 5`.

**c) Asignar un arreglo completo.**

```c err
int main(void)
{
    int a[3] = {1, 2, 3};
    int b[3];
    b = a;
    return 0;
}
```
*Corrección:* copiar elemento por elemento con un `for`.

**d) Máximo inicializado en 0** con datos negativos: `{-5, -2, -9}` daría 0 como máximo. Empieza con `a[0]`.

**e) Intercambio sin auxiliar:** `a[i] = a[j]; a[j] = a[i];` deja los dos valores iguales.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Invertir una lista | Variabilidad
Mismo recorrido, otra tarea: intercambiar el primero con el último, el segundo con el penúltimo… hasta la mitad.

```c run title="invertir.c"
#include <stdio.h>
#define N 7
int main(void)
{
    char letras[N] = {'R', 'E', 'C', 'O', 'N', 'O', 'C'};
    for (int i = 0; i < N / 2; i++)           //> Solo hasta la mitad: si llega al final, ¡vuelve a invertir!
    {
        char aux = letras[i];
        letras[i] = letras[N - 1 - i];        //> El «espejo» de i es N − 1 − i
        letras[N - 1 - i] = aux;
    }
    for (int i = 0; i < N; i++) putchar(letras[i]);
    putchar('\n');
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Dibuja las casillas del arreglo en papel cuando dudes qué índice usar.

:::tarea A | T1. Temperaturas de la semana: ejemplo y gemelo | 25 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia:**

```c run title="semana.c" stdin="21 24.5 26 19 23 27.5 22\n"
#include <stdio.h>
#define DIAS 7
int main(void)
{
    const char *NOMBRES[DIAS] = {"Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"}; //> Arreglo de textos paralelo
    double t[DIAS], suma = 0;
    int pmax = 0;
    for (int i = 0; i < DIAS; i++)
    {
        scanf("%lf", &t[i]);
        suma += t[i];
        if (t[i] > t[pmax]) pmax = i;
    }
    printf("Promedio: %.1f C\n", suma / DIAS);
    printf("Dia mas caluroso: %s (%.1f C)\n", NOMBRES[pmax], t[pmax]);
    printf("Dias sobre el promedio:");
    for (int i = 0; i < DIAS; i++)                  //> Segundo recorrido: ya conocemos el promedio
        if (t[i] > suma / DIAS) printf(" %s", NOMBRES[i]);
    printf("\n");
    return 0;
}
```

**Paso 2 · Gemelo.** Una tienda registra sus **ventas de 6 meses**. Lee las 6 cantidades y muestra el total, el promedio, el **peor** mes y los meses que estuvieron **por debajo** del promedio.

:::solucion | T1
```c run title="ventas.c" stdin="12000 9500 15800 8700 11000 13400\n"
#include <stdio.h>
#define M 6
int main(void)
{
    const char *MES[M] = {"Ene", "Feb", "Mar", "Abr", "May", "Jun"};
    double v[M], total = 0;
    int pmin = 0;
    for (int i = 0; i < M; i++)
    {
        scanf("%lf", &v[i]);
        total += v[i];
        if (v[i] < v[pmin]) pmin = i;
    }
    double prom = total / M;
    printf("Total: %.2f  Promedio: %.2f\n", total, prom);
    printf("Peor mes: %s\nBajo el promedio:", MES[pmin]);
    for (int i = 0; i < M; i++)
        if (v[i] < prom) printf(" %s", MES[i]);
    printf("\n");
    return 0;
}
```
:::
:::

:::tarea A | T2. El ejemplo TAM, ahora por completar (tesis §6.1.3) | 25 min | Problema por completar
**Contexto.** Es el mismo problema del ejemplo resuelto, pero **parcialmente resuelto**: completa el algoritmo y los huecos del código.

**Algoritmo:** 1. Solicitar… 2. Guardar… 3. Definir… 4. Capturar…

{{lineas:3}}

```c blank title="llenar_completar.c"
#include <stdio.h>
#define MAX 100
int main(void)
{
    int vec[__1__];                           // 1: capacidad del arreglo
    int TAM;
    do {
        printf("Tamanio (1-100): ");
        scanf("%d", &TAM);
    } while (__2__);                          // 2: repetir mientras sea invalido
    for (int i = __3__; i __4__ TAM; i++)     // 3 y 4: recorrido de todas las casillas
    {
        printf("Elemento %d: ", i + 1);
        scanf("%d", __5__);                   // 5: direccion de la casilla donde se guarda
    }
    for (int i = 0; i < TAM; i++)
        printf("%d ", vec[i]);
    printf("\n");
    return 0;
}
```

:::solucion | T2
Algoritmo: 1. Solicitar el tamaño del arreglo al usuario. 2. Guardar el valor en `TAM`. 3. Definir el vector del tamaño introducido (dentro de la capacidad `MAX`). 4. Capturar el contenido uno a uno hasta `TAM`.

{{c:1}} `MAX` · {{c:2}} `TAM < 1 || TAM > MAX` · {{c:3}} `0` · {{c:4}} `<` · {{c:5}} `&vec[i]`

```c run title="llenar_completar.c" stdin="0\n3\n8\n6\n4\n"
#include <stdio.h>
#define MAX 100
int main(void)
{
    int vec[MAX];
    int TAM;
    do {
        printf("Tamanio (1-100): ");
        scanf("%d", &TAM);
    } while (TAM < 1 || TAM > MAX);
    for (int i = 0; i < TAM; i++)
    {
        printf("Elemento %d: ", i + 1);
        scanf("%d", &vec[i]);
    }
    for (int i = 0; i < TAM; i++)
        printf("%d ", vec[i]);
    printf("\n");
    return 0;
}
```
:::
:::

:::tarea AB | T3. ¿Dónde está y cuántas veces? (completa sin pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** En una rifa se registraron 10 boletos ganadores (pueden repetirse). Busca un número y muestra **todas** las posiciones donde aparece y cuántas veces.

```c blank title="rifa.c"
#include <stdio.h>
#define N 10
int main(void)
{
    int boletos[N] = {45, 12, 7, 45, 90, 3, 45, 18, 7, 61};
    int x, veces = 0;
    scanf("%d", &x);
    printf("Posiciones:");
    for (__1__; __2__; __3__)
    {
        if (__4__)
        {
            printf(" %d", __5__);
            __6__;
        }
    }
    if (veces == 0) printf(" ninguna");
    printf("\nAparece %d veces\n", veces);
    return 0;
}
```

:::solucion | T3
{{c:1}} `int i = 0` · {{c:2}} `i < N` · {{c:3}} `i++` · {{c:4}} `boletos[i] == x` · {{c:5}} `i + 1` (posición para el usuario) · {{c:6}} `veces++`. No hay `break`: se necesitan **todas** las apariciones.

```c run title="rifa.c" runs="45|7|100"
#include <stdio.h>
#define N 10
int main(void)
{
    int boletos[N] = {45, 12, 7, 45, 90, 3, 45, 18, 7, 61};
    int x, veces = 0;
    scanf("%d", &x);
    printf("Posiciones:");
    for (int i = 0; i < N; i++)
    {
        if (boletos[i] == x)
        {
            printf(" %d", i + 1);
            veces++;
        }
    }
    if (veces == 0) printf(" ninguna");
    printf("\nAparece %d veces\n", veces);
    return 0;
}
```
:::
:::

:::tarea AB | T4. Estadísticas del grupo (problema convencional) | 35 min | Variabilidad
**Contexto.** Lee el número de alumnos `n` (máximo 40, valídalo) y sus calificaciones (0 a 10, valídalas). Muestra: promedio, la calificación más alta y la más baja, cuántos aprobaron (≥ 6), cuántos están **por encima del promedio** y la lista de calificaciones ordenada de mayor a menor (adapta la burbuja).

:::solucion | T4
```c run title="grupo.c" stdin="6\n8.5 5 9.5 7 6 10\n"
#include <stdio.h>
#define MAX 40
int main(void)
{
    double c[MAX], suma = 0;
    int n;
    do { printf("Alumnos (1-40): "); scanf("%d", &n); } while (n < 1 || n > MAX);
    for (int i = 0; i < n; i++)
    {
        do { scanf("%lf", &c[i]); } while (c[i] < 0 || c[i] > 10);
        suma += c[i];
    }
    double prom = suma / n;
    int aprobados = 0, arriba = 0;
    for (int i = 0; i < n; i++)
    {
        if (c[i] >= 6) aprobados++;
        if (c[i] > prom) arriba++;
    }
    for (int p = 1; p < n; p++)                 // burbuja descendente: cambia > por <
        for (int j = 0; j < n - p; j++)
            if (c[j] < c[j + 1]) { double a = c[j]; c[j] = c[j + 1]; c[j + 1] = a; }
    printf("Promedio %.2f | max %.1f | min %.1f | aprobados %d | sobre el promedio %d\nOrdenadas:",
           prom, c[0], c[n - 1], aprobados, arriba);
    for (int i = 0; i < n; i++) printf(" %.1f", c[i]);
    printf("\n");
    return 0;
}
```
Después de ordenar de mayor a menor, el máximo queda en `c[0]` y el mínimo en `c[n − 1]`: ya no hace falta buscarlos con un recorrido aparte.
:::
:::

:::tarea A | T5. Ordena como quieras (solución libre, tesis §6.1.1) | 25 min | Solución libre
**Contexto.** «Dado un arreglo llamado `enteros`, cuyo contenido es 5, 6, 2, 3, 8, 1, 7, 4: utilizando **cualquier** algoritmo de ordenación, ordena el arreglo y muestra el resultado en pantalla». **Reto ampliado:** genera **todas las soluciones que te sea posible** (burbuja, selección, inserción, contando apariciones…).

:::solucion | T5
Tres soluciones distintas (todas producen `1 2 3 4 5 6 7 8`):

```c run title="ordenar_libre.c"
#include <stdio.h>
#define N 8
int main(void)
{
    int a[N] = {5, 6, 2, 3, 8, 1, 7, 4};
    int b[N];
    for (int i = 0; i < N; i++) b[i] = a[i];
    // 1) Burbuja
    for (int p = 1; p < N; p++)
        for (int j = 0; j < N - p; j++)
            if (a[j] > a[j + 1]) { int aux = a[j]; a[j] = a[j + 1]; a[j + 1] = aux; }
    // 2) Insercion: cada elemento se inserta en su lugar entre los ya ordenados
    for (int i = 1; i < N; i++)
    {
        int x = b[i], j = i - 1;
        while (j >= 0 && b[j] > x) { b[j + 1] = b[j]; j--; }
        b[j + 1] = x;
    }
    // 3) Conteo: como los valores van de 1 a 8, se cuenta cuantas veces aparece cada uno
    int cuenta[9] = {0};
    for (int i = 0; i < N; i++) cuenta[b[i]]++;
    for (int i = 0; i < N; i++) printf("%d ", a[i]);
    printf("| ");
    for (int i = 0; i < N; i++) printf("%d ", b[i]);
    printf("| ");
    for (int v = 1; v <= 8; v++)
        for (int k = 0; k < cuenta[v]; k++) printf("%d ", v);
    printf("\n");
    return 0;
}
```
La selección aparece en la T7. La biblioteca estándar de C también ofrece `qsort` (en `<stdlib.h>`), que verás cuando conozcas las funciones.
:::
:::

:::tarea B | T6. ¿Puedes ayudar a tus compañeros? (autoexplicación, tesis §6.1.6) | 20 min | Autoexplicación, Reversión de la experiencia
**Contexto.** La maestra envió un programa de ejemplo sobre el método de la burbuja, pero algunos de tus compañeros no entendieron el tema y tampoco el ejemplo. **Revisa el código y, en el espacio de abajo, explica con tus palabras a tus compañeros cada bloque** (A, B, C y D). Incluye por qué el ciclo interno llega a `N - 1 - p` y para qué sirve la variable `hubo`.

```c run title="burbuja_mejorada.c"
#include <stdio.h>
#include <stdbool.h>
#define N 6
int main(void)
{
    int v[N] = {9, 4, 7, 1, 8, 2};
    // Bloque A
    for (int p = 0; p < N - 1; p++)
    {
        // Bloque B
        bool hubo = false;
        for (int j = 0; j < N - 1 - p; j++)
        {
            // Bloque C
            if (v[j] > v[j + 1])
            {
                int aux = v[j];
                v[j] = v[j + 1];
                v[j + 1] = aux;
                hubo = true;
            }
        }
        // Bloque D
        if (!hubo) break;
    }
    for (int i = 0; i < N; i++) printf("%d ", v[i]);
    printf("\n");
    return 0;
}
```

{{lineas:5}}

:::solucion | T6
**A:** controla las pasadas; como máximo se necesitan `N − 1`. **B:** en cada pasada se reinicia la bandera `hubo` (¿hubo algún intercambio?) y el ciclo interno compara vecinos solo hasta `N − 1 − p`, porque tras `p` pasadas los últimos `p` elementos ya están en su lugar y `j + 1` nunca debe salirse del arreglo. **C:** si el vecino derecho es menor, se intercambian con `aux` y se marca `hubo = true`. **D:** si en una pasada completa no hubo intercambios, el arreglo ya está ordenado y se sale antes (`break`): es la versión optimizada de la burbuja.
:::
:::

:::tarea B | T7. Imagina el ordenamiento por selección (imaginación, tesis §6.1.10) | 30 min | Imaginación
**Contexto.** «El algoritmo de ordenamiento por **selección** consiste en buscar el elemento más pequeño del arreglo e intercambiarlo por el que está en la primera posición; luego, entre los restantes, se busca de nuevo el más pequeño y se intercambia por el que está en la segunda posición, y así sucesivamente».

A partir de esta descripción y del arreglo `{29, 10, 14, 37, 13}`:

1. **Imagina** el proceso y **represéntalo a mano** (dibujos y texto) iteración por iteración hasta ordenar el arreglo.
2. Genera el pseudocódigo en PSeInt y el código en C de tu representación.
3. Cuenta las comparaciones y los intercambios y compáralos con la burbuja para el mismo arreglo.

:::solucion | T7
```diagram arrs
rows:
  - {label: "Inicio", vals: [29, 10, 14, 37, 13]}
  - {label: "i=0: menor es 10", vals: [10, 29, 14, 37, 13], hl: [0, 1], swap: true, ok: [0]}
  - {label: "i=1: menor es 13", vals: [10, 13, 14, 37, 29], hl: [1, 4], swap: true}
  - {label: "i=2: menor es 14", vals: [10, 13, 14, 37, 29], ok: [0, 1, 2], note: "ya estaba en su lugar"}
  - {label: "i=3: menor es 29", vals: [10, 13, 14, 29, 37], hl: [3, 4], swap: true}
  - {label: "Ordenado", vals: [10, 13, 14, 29, 37], ok: [0, 1, 2, 3, 4]}
```

```c run title="seleccion.c"
#include <stdio.h>
#define N 5
int main(void)
{
    int a[N] = {29, 10, 14, 37, 13};
    int comparaciones = 0, intercambios = 0;
    for (int i = 0; i < N - 1; i++)
    {
        int pmin = i;
        for (int j = i + 1; j < N; j++)
        {
            comparaciones++;
            if (a[j] < a[pmin]) pmin = j;
        }
        if (pmin != i)
        {
            int aux = a[i]; a[i] = a[pmin]; a[pmin] = aux;
            intercambios++;
        }
    }
    for (int i = 0; i < N; i++) printf("%d ", a[i]);
    printf("\nComparaciones: %d  Intercambios: %d\n", comparaciones, intercambios);
    return 0;
}
```
La selección siempre hace `N(N−1)/2 = 10` comparaciones, pero **pocos intercambios** (como máximo `N − 1`); la burbuja, con el mismo arreglo, hace el mismo número de comparaciones y más intercambios.
:::
:::

:::tarea AB | T8. Votación escolar (reto colaborativo) | 40 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Equipos de 4, niveles mezclados. Hay 5 planillas (1 a 5). Se capturan votos (números del 1 al 5) hasta que se escribe 0; los votos fuera de rango cuentan como **nulos**.
- **Integrante 1:** arreglo contador `int votos[P] = {0};` y la captura con centinela (`votos[v - 1]++`).
- **Integrante 2:** total de votos válidos y nulos.
- **Integrante 3:** porcentaje de cada planilla con una barra de asteriscos (un `*` por cada 5 %).
- **Integrante 4:** la planilla ganadora y la detección de **empates** en el primer lugar.
:::

:::solucion | T8
```c run title="votacion.c" stdin="3 1 3 5 2 3 9 1 3 5 1 0\n"
#include <stdio.h>
#define P 5
int main(void)
{
    int votos[P] = {0};
    int v, nulos = 0, validos = 0;
    scanf("%d", &v);
    while (v != 0)
    {
        if (v >= 1 && v <= P) { votos[v - 1]++; validos++; }
        else nulos++;
        scanf("%d", &v);
    }
    int ganador = 0;
    for (int i = 0; i < P; i++)
    {
        double pct = validos > 0 ? 100.0 * votos[i] / validos : 0;
        printf("Planilla %d: %d (%.1f%%) ", i + 1, votos[i], pct);
        for (int k = 0; k < (int)(pct / 5); k++) putchar('*');
        putchar('\n');
        if (votos[i] > votos[ganador]) ganador = i;
    }
    int empatados = 0;
    for (int i = 0; i < P; i++)
        if (votos[i] == votos[ganador]) empatados++;
    printf("Validos: %d  Nulos: %d\n", validos, nulos);
    if (empatados > 1) printf("Empate en el primer lugar\n");
    else printf("Gana la planilla %d\n", ganador + 1);
    return 0;
}
```
:::
:::

:::tarea B | T9. Mejora este material sobre la burbuja (autogestión, tesis §6.1.17) | 25 min | Autogestión, Atención dividida, Redundancia
**Fase de entrenamiento.** Este fragmento proviene de un sitio web:

:::autog | Material original (con problemas de diseño)
*«El ordenamiento de burbuja (Bubble Sort en inglés) es un sencillo algoritmo de ordenamiento. Funciona revisando cada elemento de la lista que va a ser ordenada con el siguiente, intercambiándolos de posición si están en el orden equivocado. Es necesario revisar varias veces toda la lista hasta que no se necesiten más intercambios, lo cual significa que la lista está ordenada. También es conocido como el método del intercambio directo. Dado que solo usa comparaciones para operar elementos, se lo considera un algoritmo de comparación, siendo el más sencillo de implementar.»* — A continuación vienen cuatro figuras sin texto, en otra página, y al final el código sin comentarios, con un audio que lee el mismo párrafo.
:::

1. Identifica los problemas: demasiado texto, texto y visualizaciones separados, información redundante o no esencial, falta de señalización, información transitoria.
2. Aplica las estrategias de autogestión: integra el texto **dentro** de las figuras, elimina lo no esencial, resalta lo importante, segmenta y crea un resumen visual.
3. Compara tu versión con el concepto 8 de este material (la versión optimizada).

**Fase de transferencia:** aplica las mismas estrategias a una explicación de la **búsqueda secuencial** que encuentres en internet.

:::solucion | T9
Problemas: texto largo con información no esencial (nombre en inglés, «algoritmo de comparación»); figuras **separadas** del texto (atención dividida); audio que repite el texto escrito (redundancia); código sin señalización. Estrategias aplicadas en el concepto 8: una sola frase de idea central; traza visual con anotaciones **dentro** de cada fila («5 > 3 → intercambia»); colores para señalizar el par comparado y los elementos fijos; código con comentarios integrados línea por línea; sin audio duplicado.
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Rotar una lista una posición a la derecha | Modalidad, Ejemplo resuelto
*Guion segmentado (≈ 3 min), con casillas dibujadas en pantalla.*

**Problema:** «En un juego por turnos, el orden de los jugadores `{A, B, C, D, E}` rota en cada ronda: el último pasa al inicio → `{E, A, B, C, D}`».

**Segmento 1 — Dibujar antes de programar.** {{como}} Dibujo las casillas antes y después y trazo flechas: cada elemento se mueve una casilla a la derecha y el último «da la vuelta» a la posición 0. {{porque}} Ver las flechas me dice que hay **dos** tipos de movimiento: el desplazamiento general y el caso especial del último.

**Segmento 2 — Guardar lo que se va a perder.** {{como}} Guardo `ultimo = j[4]` antes de mover nada. {{porque}} Al desplazar, la casilla 4 se sobrescribe con el valor de la 3; si no lo guardo, la E desaparece.

**Segmento 3 — La dirección del ciclo importa.** {{como}} Recorro de **derecha a izquierda**: `for (i = N − 1; i > 0; i--) j[i] = j[i − 1];`. {{porque}} Si fuera de izquierda a derecha, copiaría A en la casilla 1, luego esa misma A en la 2, en la 3… y todo quedaría lleno de A. Lo comprobé con una traza de dos pasos.

**Segmento 4 — Cerrar y probar varias rondas.** {{como}} Pongo `j[0] = ultimo` y ejecuto la rotación tres veces dentro de otro ciclo. {{porque}} Si después de 5 rondas vuelvo al orden original, sé que la rotación es correcta.

```c run title="rotar.c"
#include <stdio.h>
#define N 5
int main(void)
{
    char j[N] = {'A', 'B', 'C', 'D', 'E'};
    for (int ronda = 1; ronda <= 3; ronda++)
    {
        char ultimo = j[N - 1];
        for (int i = N - 1; i > 0; i--)
            j[i] = j[i - 1];
        j[0] = ultimo;
        printf("Ronda %d: ", ronda);
        for (int i = 0; i < N; i++) printf("%c ", j[i]);
        printf("\n");
    }
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. ¿Cuál es el índice del primer y del último elemento de `int a[12];`?
2. ¿Qué contiene `int b[5] = {3, 4};`?
3. ¿Cuántos bytes ocupa `double d[10];` si un `double` ocupa 8?
4. ¿Por qué no se puede escribir `b = a;` con arreglos de C?
5. Verdadero o falso: acceder a `a[12]` en `int a[12];` siempre produce un error de compilación.
6. ¿Qué devuelve una búsqueda secuencial cuando el valor no está (en la convención del curso)?
7. En la burbuja, ¿qué ocurre al terminar la primera pasada?
8. ¿Para qué sirve la variable auxiliar en un intercambio?
9. ¿Qué hace `rand() % 10 + 1`?
10. ¿Por qué en C se escribe `#define N 10` y no `const int N = 10;` para declarar `int a[N] = {0};`?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida:**

```c check title="p1.c"
#include <stdio.h>
int main(void)
{
    int a[6] = {4, 9, 2, 9, 5, 1};
    int x = 0, y = 0;
    for (int i = 0; i < 6; i++)
    {
        if (a[i] > a[x]) x = i;
        if (a[i] % 2 == 1) y += a[i];
    }
    printf("%d %d %d\n", x, a[x], y);
    return 0;
}
```

**P2. Escribe la traza** (estado del arreglo al final de cada pasada) de la burbuja sobre `{6, 2, 9, 4}`.

**P3. Corrige:** el programa debe contar los elementos negativos de `int v[8]`, pero a veces falla o da números raros: `int neg; for (int i = 1; i <= 8; i++) if (v[i] < 0) neg++;`

**P4. Escribe un programa** que lea 10 enteros, guarde en un segundo arreglo solo los pares (en el mismo orden) y muestre ambos arreglos.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Declaro, inicializo y recorro arreglos sin salirme de sus índices.</li>
<li>Calculo suma, promedio, máximo, mínimo y conteos con un recorrido.</li>
<li>Busco valores y ordeno con la burbuja (y explico cada bloque).</li>
<li>Sé cuándo hacen falta dos recorridos (por ejemplo, para comparar con el promedio).</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 `a[0]` y `a[11]` · 2 `3 4 0 0 0` · 3 80 · 4 Porque los arreglos de C no se pueden asignar completos; hay que copiar elemento por elemento · 5 Falso: compila; es comportamiento indefinido en ejecución · 6 −1 · 7 El mayor queda en la última posición · 8 Guardar temporalmente uno de los valores para no perderlo · 9 Un número pseudoaleatorio entre 1 y 10 · 10 Porque en C una variable `const` no es una constante del compilador: `int a[N]` sería un arreglo de longitud variable, que no admite inicializador; `#define` sustituye `N` por `10` antes de compilar.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** `x` queda en la primera posición del máximo (1, valor 9, porque `>` no reemplaza al empatado de la posición 3); `y` suma los impares 9 + 9 + 5 + 1 = 24.

```c run title="p1.c"
#include <stdio.h>
int main(void)
{
    int a[6] = {4, 9, 2, 9, 5, 1};
    int x = 0, y = 0;
    for (int i = 0; i < 6; i++)
    {
        if (a[i] > a[x]) x = i;
        if (a[i] % 2 == 1) y += a[i];
    }
    printf("%d %d %d\n", x, a[x], y);
    return 0;
}
```

**P2.** Pasada 1: `2 6 4 9` · Pasada 2: `2 4 6 9` · Pasada 3: `2 4 6 9` (sin cambios).

**P3.** Inicializar `neg = 0`; los índices van de 0 a 7: `for (int i = 0; i < 8; i++)`.

**P4.**

```c run title="p4.c" stdin="3 8 5 12 7 6 1 10 4 9\n"
#include <stdio.h>
#define N 10
int main(void)
{
    int a[N], pares[N], np = 0;
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &a[i]);
        if (a[i] % 2 == 0) pares[np++] = a[i];   // np cuenta cuantos pares hay
    }
    printf("Original:");
    for (int i = 0; i < N; i++) printf(" %d", a[i]);
    printf("\nPares:");
    for (int i = 0; i < np; i++) printf(" %d", pares[i]);
    printf("\n");
    return 0;
}
```
:::
