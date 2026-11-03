---
num: "09"
archivo: "Tema09_Arreglos_bidimensionales_matrices"
titulo: "Arreglos bidimensionales (matrices)"
corto: "Matrices"
lema: "Filas y columnas: cuando los datos forman una tabla, cada casilla tiene dos coordenadas."
duracion: "5 h · 3 sesiones"
previos: "Tema 07 (ciclos anidados) y Tema 08 (arreglos unidimensionales)."
fuentes:
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Cap. 7: Arreglos multidimensionales (§7.1 Concepto, §7.2 Declaración, §7.3 Inicialización en la declaración, aleatoria y por captura, §7.4 Procesamiento, §7.5 Ejercicios)."
  - "Lospinoso, J. (2019). *C++ Crash Course*. Cap. 2: Arrays (inicialización con llaves y acceso a elementos), base para los arreglos de arreglos."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §6.1.14: problema colaborativo del cuadrado mágico de orden impar."
objetivos:
  A:
    - "Declarar, inicializar y acceder a los elementos de una matriz con `m[fila][columna]`."
    - "Recorrer una matriz con ciclos anidados para capturar, mostrar y procesar sus datos."
    - "Calcular sumas y promedios por fila, por columna, de la diagonal principal y del total."
    - "Modelar con matrices problemas de tablas (calificaciones por alumno y materia, ventas por sucursal y mes)."
  B:
    - "Implementar la transpuesta, la suma y el producto de matrices."
    - "Recorrer diagonal secundaria, triángulos y bordes, y recorrer por columnas."
    - "Explicar el almacenamiento por filas (*row-major*) en memoria."
    - "Resolver problemas combinados (cuadrado mágico, verificación de un tablero de juego)."
efectos:
  soporte:
    - ["Elementos aislados", "Vector → matriz → índices → inicialización → recorrido por filas → sumas → diagonales → por columnas → operaciones."]
    - ["Atención dividida", "Cada recorrido se muestra con la cuadrícula resaltada junto al código que la produce."]
    - ["Ejemplo resuelto", "Calificaciones de alumnos por materia con promedios por fila y por columna."]
    - ["Movimiento humano", "«Matriz humana»: estudiantes sentados en filas y columnas responden a coordenadas."]
  procedimental:
    - ["Variabilidad", "Mismos recorridos aplicados a ventas, tableros, asientos y mapas."]
    - ["Interactividad de elementos", "Plantillas separadas para recorrer filas, columnas y diagonales."]
  tareas:
    - ["Ejemplo resuelto", "T1: ventas por sucursal y mes + gemelo (puntos por jornada)."]
    - ["Problema por completar", "T2 (diagonal y matriz identidad, con pistas) y T3 (transpuesta, sin pistas)."]
    - ["Desvanecimiento de guía", "T1 → T4."]
    - ["Solución libre", "T5: descubrir todo lo posible de una matriz 4 × 4."]
    - ["Autoexplicación", "T6: errores de índices y acumuladores."]
    - ["Imaginación", "T7: imaginar la rotación de 90° de una imagen."]
    - ["Memoria colectiva de trabajo", "T8: cuadrado mágico de orden impar (tesis §6.1.14)."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Declaración, recorrido por filas, sumas por fila/columna, diagonal principal."
    B: "Memoria *row-major*, transpuesta, producto, diagonales y triángulos."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 con cuadrícula impresa para anotar índices."
    B: "T5, T6, T7 autónomas; T8 como coordinadores."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Sistema de asientos (T4)."
    B: "Rotación de imagen (T7) y explicación del método del cuadrado mágico (T8)."
  Entorno:
    comp: "Información procedimental"
    A: "Hojas cuadriculadas; depurador con vista de la matriz."
    B: "Terminal; pruebas con matrices no cuadradas."
plan:
  - ["Sesión 1", "Soporte", "Matriz humana; conceptos 1–5; ejemplo resuelto; T1.", "100 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–8; T2, T3, T4; Ruta B: T5, T6, T7.", "100 min"]
  - ["Sesión 3", "Tareas + evaluación", "T8 cuadrado mágico; protocolo verbal; tests y autorregistro.", "100 min"]
glosario:
  - ["matriz / tabla", "matrix / 2D array", "Arreglo de dos dimensiones: filas y columnas."]
  - ["fila / renglón", "row", "Línea horizontal de la matriz; primer índice."]
  - ["columna", "column", "Línea vertical de la matriz; segundo índice."]
  - ["diagonal principal", "main diagonal", "Elementos con `i == j`."]
  - ["diagonal secundaria", "anti-diagonal", "Elementos con `i + j == n − 1`."]
  - ["matriz cuadrada", "square matrix", "Igual número de filas y columnas."]
  - ["matriz identidad", "identity matrix", "Cuadrada con 1 en la diagonal y 0 en el resto."]
  - ["transpuesta", "transpose", "Matriz que intercambia filas por columnas: `t[j][i] = m[i][j]`."]
  - ["orden por filas", "row-major order", "Los elementos se guardan fila tras fila en memoria contigua."]
  - ["cuadrado mágico", "magic square", "Matriz n × n con 1..n² donde filas, columnas y diagonales suman lo mismo."]
---

# 1. Información de soporte {.soporte}

:::analogia | La hoja de cálculo y el juego de «batalla naval»
En una hoja de cálculo cada celda se identifica con **dos** datos: la fila y la columna («B3»). En batalla naval disparas a «fila 4, columna 7». Una **matriz** es un arreglo con esas dos coordenadas: guarda una **tabla** de datos del mismo tipo.
:::

:::pregunta
Un profesor tiene 30 alumnos y 5 materias. Quiere el promedio de **cada alumno** y el promedio de **cada materia**. Con arreglos de una dimensión, **¿cuántos arreglos necesitarías?** ¿Cómo sabrías qué calificación es de qué alumno y de qué materia?

{{lineas:2}}
:::

:::relevancia
Las imágenes digitales son matrices de píxeles; los tableros de ajedrez, gato y buscaminas son matrices; los mapas de los videojuegos por mosaicos son matrices; en inteligencia artificial y gráficos 3D todo se calcula con operaciones de matrices. Este tema es la base para todo eso. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | De la lista a la tabla | Elementos aislados, Atención dividida
Un arreglo unidimensional es una **fila** de casillas. Una matriz es **un arreglo de filas**: cada fila es, a su vez, un arreglo.

<div class="cols eq">
<div>

```diagram arr
name: "notasAna"
type: "double[3]"
vals: [8.5, 9, 7]
```

</div>
<div>

```diagram mat
name: "notas[4][3]  (alumno × materia)"
rows: [[8.5, 9, 7], [6, 7.5, 8], [10, 9.5, 9], [5, 6, 7.5]]
hlrow: 0
```

</div>
</div>

La fila 0 de la matriz es la lista de Ana; las otras filas son los demás alumnos. Cada **columna** es una materia.
:::

:::concepto | 2 | Declaración e índices `[fila][columna]` | Elementos aislados, Atención dividida
`tipo nombre[FILAS][COLUMNAS];` — el primer índice es la fila, el segundo la columna; ambos empiezan en 0.

```cpp run title="indices.cpp"
#include <iostream>
using namespace std;
int main()
{
    int m[3][4] = { {1, 2, 3, 4},       //> Fila 0
                    {5, 6, 7, 8},       //> Fila 1
                    {9, 10, 11, 12} };  //> Fila 2
    cout << "m[1][2] = " << m[1][2] << "\n";   //> Fila 1, columna 2 → 7
    m[2][0] = 99;                             //> Se usa como cualquier variable
    cout << "m[2][0] = " << m[2][0] << "\n";
    cout << "Bytes: " << sizeof(m) << " (3 x 4 x 4)\n";
    return 0;
}
```

```diagram mat
name: "m[3][4]"
rows: [[1, 2, 3, 4], [5, 6, 7, 8], [99, 10, 11, 12]]
hl: [[1, 2]]
hl2: [[2, 0]]
caption: "amarillo: m[1][2]  ·  verde: m[2][0] modificado"
```

:::nota | Ruta B · Así vive en memoria (orden por filas)
La memoria es una sola «tira». C++ guarda la matriz **fila tras fila**: primero `m[0][0..3]`, luego `m[1][0..3]`… El elemento `m[i][j]` está en la posición `i × COLUMNAS + j` de esa tira.

```diagram arr
name: "memoria"
vals: [1, 2, 3, 4, 5, 6, 7, 8, 99, 10, 11, 12]
hl: [6]
idx: true
caption: "m[1][2] está en la posición 1 × 4 + 2 = 6"
```
:::
:::

:::concepto | 3 | Formas de inicializar | Elementos aislados
| Declaración | Resultado |
|---|---|
| `int a[2][3] = {{1, 2, 3}, {4, 5, 6}};` | dos filas completas |
| `int b[2][3] = {{1}, {4, 5}};` | `1 0 0` / `4 5 0` (lo que falta, en cero) |
| `int c[3][3] = {};` | todo en cero |
| `int d[][2] = {{1, 2}, {3, 4}, {5, 6}};` | 3 filas (se deduce); las **columnas** siempre se indican |
| Captura | `for (i…) for (j…) cin >> a[i][j];` |
| Aleatoria | `for (i…) for (j…) a[i][j] = rand() % 10;` |
:::

:::concepto | 4 | Recorrer por filas: ciclos anidados | Elementos aislados, Atención dividida
El ciclo **externo** recorre filas (`i`), el **interno** columnas (`j`): exactamente lo que practicaste en el Tema 07.

```cpp run title="captura_matriz.cpp" stdin="1 2 3\n4 5 6\n"
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    const int F = 2, C = 3;                 //> Constantes para filas y columnas
    int m[F][C];
    for (int i = 0; i < F; i++)             //> Para cada fila…
        for (int j = 0; j < C; j++)         //> …cada columna
            cin >> m[i][j];
    for (int i = 0; i < F; i++)
    {
        for (int j = 0; j < C; j++)
            cout << setw(4) << m[i][j];     //> setw alinea las columnas
        cout << "\n";                       //> Fin de la fila
    }
    return 0;
}
```
:::

:::movimiento | Matriz humana (10 min)
Los estudiantes se sientan en una cuadrícula de 4 filas × 5 columnas; cada uno escribe un número del 1 al 9 en una hoja. El instructor dice coordenadas: «`m[2][3]`» → ese estudiante se pone de pie y dice su número. Luego: «suma de la fila 1» (se levanta toda la fila 1 y suman), «suma de la columna 0», «diagonal principal» (¿quiénes cumplen `i == j`?). Pregunta final: ¿qué estudiantes cumplen `i + j == 4`?
:::

:::concepto | 5 | Sumas por fila y por columna | Elementos aislados, Atención dividida
La clave es **dónde se reinicia** el acumulador: la suma de cada fila empieza en 0 **dentro** del ciclo de filas.

```cpp run title="sumas.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int F = 3, C = 4;
    int m[F][C] = {{2, 4, 1, 3}, {5, 0, 2, 2}, {1, 1, 6, 4}};
    for (int i = 0; i < F; i++)
    {
        int sumaFila = 0;                   //> Se reinicia para CADA fila
        for (int j = 0; j < C; j++)
            sumaFila += m[i][j];
        cout << "Fila " << i << ": " << sumaFila << "\n";
    }
    for (int j = 0; j < C; j++)             //> Para columnas: el EXTERNO recorre columnas
    {
        int sumaCol = 0;
        for (int i = 0; i < F; i++)
            sumaCol += m[i][j];
        cout << "Columna " << j << ": " << sumaCol << "\n";
    }
    return 0;
}
```
:::

:::concepto | 6 | Diagonales de una matriz cuadrada | Elementos aislados, Atención dividida
<div class="cols">
<div>

```cpp run title="diagonales.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int N = 4;
    int m[N][N] = {{3, 1, 4, 1}, {5, 9, 2, 6},
                   {5, 3, 5, 8}, {9, 7, 9, 3}};
    int dp = 0, ds = 0;
    for (int i = 0; i < N; i++)
    {
        dp += m[i][i];             //> Principal: fila = columna
        ds += m[i][N - 1 - i];     //> Secundaria: i + j = N − 1
    }
    cout << "Principal: " << dp << "  Secundaria: " << ds << "\n";
    return 0;
}
```

</div>
<div>

```diagram mat
name: "principal (amarillo) y secundaria (verde)"
rows: [[3, 1, 4, 1], [5, 9, 2, 6], [5, 3, 5, 8], [9, 7, 9, 3]]
hl: [[0, 0], [1, 1], [2, 2], [3, 3]]
hl2: [[0, 3], [1, 2], [2, 1], [3, 0]]
```

</div>
</div>

Basta **un** ciclo: en la diagonal, la columna se calcula a partir de la fila.
:::

:::concepto | 7 | Ruta B · Transpuesta, suma y producto | Elementos aislados, Reversión de la experiencia
```cpp run title="operaciones.cpp"
#include <iostream>
using namespace std;
int main()
{
    int A[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int B[3][2] = {{7, 8}, {9, 10}, {11, 12}};
    int T[3][2], P[2][2] = {};
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 3; j++)
            T[j][i] = A[i][j];                        //> Transpuesta: filas ↔ columnas
    for (int i = 0; i < 2; i++)                       //> Producto: fila i de A por columna j de B
        for (int j = 0; j < 2; j++)
            for (int k = 0; k < 3; k++)
                P[i][j] += A[i][k] * B[k][j];         //> Tres ciclos: k recorre la «dimensión común»
    cout << "T:\n";
    for (int i = 0; i < 3; i++) { for (int j = 0; j < 2; j++) cout << T[i][j] << " "; cout << "\n"; }
    cout << "A x B:\n";
    for (int i = 0; i < 2; i++) { for (int j = 0; j < 2; j++) cout << P[i][j] << " "; cout << "\n"; }
    return 0;
}
```
Para multiplicar, las **columnas de A** deben ser iguales a las **filas de B** (aquí, 3).
:::

## 1.2 Ejemplo resuelto: calificaciones por alumno y por materia

:::ejemplo | Promedios por alumno (fila) y por materia (columna) | Ejemplo resuelto, Atención dividida
**Problema.** Capturar las calificaciones de 4 alumnos en 3 materias y mostrar la tabla con el promedio de cada alumno al final de su fila y el promedio de cada materia al pie de su columna.

**A. Algoritmo:** 1) Capturar la matriz 4 × 3. 2) Para cada fila: mostrar sus calificaciones y su promedio. 3) Para cada columna: calcular y mostrar su promedio.

**B. Pseudocódigo**

```pseudo
Algoritmo Calificaciones
    Dimension cal[4,3]
    Para i <- 1 Hasta 4 Hacer
        Para j <- 1 Hasta 3 Hacer
            Leer cal[i,j]
        FinPara
    FinPara
    Para i <- 1 Hasta 4 Hacer
        suma <- 0
        Para j <- 1 Hasta 3 Hacer
            suma <- suma + cal[i,j]
        FinPara
        Escribir "Alumno ", i, ": ", suma / 3
    FinPara
    Para j <- 1 Hasta 3 Hacer
        suma <- 0
        Para i <- 1 Hasta 4 Hacer
            suma <- suma + cal[i,j]
        FinPara
        Escribir "Materia ", j, ": ", suma / 4
    FinPara
FinAlgoritmo
```

**C. Código en C++**

```cpp run title="calificaciones.cpp" stdin="8.5 9 7\n6 7.5 8\n10 9.5 9\n5 6 7.5\n"
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    const int AL = 4, MAT = 3;
    double cal[AL][MAT];
    for (int i = 0; i < AL; i++)                     //> Paso 1: captura fila por fila
        for (int j = 0; j < MAT; j++)
            cin >> cal[i][j];
    cout << fixed << setprecision(1);
    cout << "         Mat  Fis  Prog  Prom\n";
    for (int i = 0; i < AL; i++)                     //> Paso 2: cada fila y su promedio
    {
        double suma = 0;                             //> Acumulador de la fila (se reinicia)
        cout << "Alumno " << i + 1;
        for (int j = 0; j < MAT; j++)
        {
            cout << setw(5) << cal[i][j];
            suma += cal[i][j];
        }
        cout << setw(6) << suma / MAT << "\n";
    }
    cout << "Prom.   ";
    for (int j = 0; j < MAT; j++)                    //> Paso 3: externo por COLUMNAS
    {
        double suma = 0;
        for (int i = 0; i < AL; i++)
            suma += cal[i][j];
        cout << setw(5) << suma / AL;
    }
    cout << "\n";
    return 0;
}
```

**D. Verificación.** Alumno 1: (8.5 + 9 + 7) / 3 = 8.2 ✔. Materia 1: (8.5 + 6 + 10 + 5) / 4 = 7.4 ✔ (redondeado a un decimal).
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.18; ranksep=0.3;
@term(m, "Matriz\ntipo m[F][C]")
@proc(ix, "m[fila][columna]\nambos desde 0")
@proc(rf, "recorrido por filas:\nfor i { for j }")
@proc(rc, "recorrido por columnas:\nfor j { for i }")
@proc(sm, "sumas por fila / columna\n(acumulador reiniciado)")
@proc(dg, "diagonales: i == j\ni + j == N−1")
@sub(op, "transpuesta · suma\nproducto (3 ciclos)")
m -> ix; m -> rf -> sm; m -> rc -> sm; m -> dg; m -> op [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1 | Interactividad de elementos
| Quiero… | Código |
|---|---|
| Declarar | `const int F = 3, C = 4; int m[F][C];` |
| Capturar | `for (int i = 0; i < F; i++) for (int j = 0; j < C; j++) cin >> m[i][j];` |
| Mostrar como tabla | `for (i…) { for (j…) cout << setw(4) << m[i][j]; cout << "\n"; }` |
| Sumar todo | `s = 0; for (i…) for (j…) s += m[i][j];` |
| Suma de la fila `i` | `s = 0; for (int j = 0; j < C; j++) s += m[i][j];` |
| Suma de la columna `j` | `s = 0; for (int i = 0; i < F; i++) s += m[i][j];` |
| Diagonal principal | `for (int i = 0; i < N; i++) … m[i][i]` |
| Diagonal secundaria | `for (int i = 0; i < N; i++) … m[i][N - 1 - i]` |
| Triángulo superior | `for (i…) for (int j = i; j < N; j++)` |
| Bordes | `if (i == 0 \|\| i == F - 1 \|\| j == 0 \|\| j == C - 1)` |
| Vecinos de `[i][j]` | `[i-1][j]`, `[i+1][j]`, `[i][j-1]`, `[i][j+1]` (¡verifica límites!) |
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿El primer índice es la fila y el segundo la columna, en todas las líneas?</li>
<li>¿El ciclo de filas usa <code>F</code> y el de columnas <code>C</code> (no al revés, sobre todo si no es cuadrada)?</li>
<li>¿Reinicio los acumuladores por fila/columna dentro del ciclo externo correcto?</li>
<li>¿Para sumar columnas puse el ciclo de columnas por fuera?</li>
<li>¿Al usar vecinos (<code>i − 1</code>, <code>j + 1</code>) verifico que no salgan de la matriz?</li>
<li>¿Probé con una matriz <b>no cuadrada</b> para detectar índices intercambiados?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Índices intercambiados en una matriz no cuadrada.** `m[j][i]` con `i < 2` y `j < 3` en una matriz `int m[2][3]` accede a `m[2][…]`, que **no existe**.

**b) Acumulador fuera de lugar.** `int s = 0;` antes de **ambos** ciclos da la suma acumulada de todas las filas, no la de cada una.

**c) Usar una coma en lugar de dos corchetes.** `m[1, 2]` no es la fila 1, columna 2 (en C++ la coma evalúa y descarta el 1): escribe `m[1][2]`.

```cpp err
#include <iostream>
int main()
{
    int m[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int x = m[1, 2];
    std::cout << x;
    return 0;
}
```

**d) Omitir el número de columnas.** `int m[][] = {{1, 2}, {3, 4}};` no compila: las columnas siempre deben indicarse.
:::

{{salto}}

:::isomorfo | Ejemplo isomórfico 2.4 · Mapa de un videojuego por mosaicos | Variabilidad
Mismo recorrido por filas; los números representan tipos de terreno:

```cpp run title="mapa.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int F = 4, C = 8;
    int mapa[F][C] = {{0, 0, 1, 1, 0, 0, 0, 2},
                      {0, 1, 1, 0, 0, 3, 0, 0},
                      {0, 0, 0, 0, 3, 3, 0, 0},
                      {2, 0, 0, 0, 0, 0, 1, 1}};
    for (int i = 0; i < F; i++)
    {
        for (int j = 0; j < C; j++)
        {
            switch (mapa[i][j])                  //> Cada número se dibuja con un símbolo
            {
                case 0: cout << '.'; break;      //> pasto
                case 1: cout << '^'; break;      //> montaña
                case 2: cout << '$'; break;      //> tesoro
                case 3: cout << '~'; break;      //> agua
            }
        }
        cout << "\n";
    }
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Prueba siempre con matrices pequeñas y verifica a mano al menos una fila y una columna.

:::tarea A | T1. Ventas por sucursal y mes: ejemplo y gemelo | 25 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia:**

```cpp run title="ventas_sucursal.cpp"
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    const int S = 3, M = 4;
    int v[S][M] = {{120, 150, 90, 200},           //> Sucursal 1: ene..abr
                   {80, 95, 110, 130},            //> Sucursal 2
                   {210, 180, 160, 190}};         //> Sucursal 3
    int mejorS = 0, mejorTotal = 0;
    for (int i = 0; i < S; i++)
    {
        int total = 0;                            //> Total de la sucursal i
        for (int j = 0; j < M; j++) total += v[i][j];
        cout << "Sucursal " << i + 1 << ": " << total << "\n";
        if (total > mejorTotal) { mejorTotal = total; mejorS = i; }
    }
    cout << "Mejor sucursal: " << mejorS + 1 << "\nTotal por mes:";
    for (int j = 0; j < M; j++)                   //> Externo por columnas (meses)
    {
        int t = 0;
        for (int i = 0; i < S; i++) t += v[i][j];
        cout << setw(5) << t;
    }
    cout << "\n";
    return 0;
}
```

**Paso 2 · Gemelo.** Un torneo tiene 4 equipos y 5 jornadas; cada casilla son los puntos del equipo en esa jornada. Muestra los puntos totales de cada equipo, el líder y la jornada con más puntos repartidos.

:::solucion | T1
```cpp run title="torneo.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int E = 4, J = 5;
    int p[E][J] = {{3, 1, 3, 0, 3}, {1, 1, 0, 3, 3}, {0, 3, 1, 3, 1}, {3, 0, 1, 1, 0}};
    int lider = 0, maxPts = -1;
    for (int i = 0; i < E; i++)
    {
        int t = 0;
        for (int j = 0; j < J; j++) t += p[i][j];
        cout << "Equipo " << i + 1 << ": " << t << " pts\n";
        if (t > maxPts) { maxPts = t; lider = i; }
    }
    int mejorJ = 0, maxJ = -1;
    for (int j = 0; j < J; j++)
    {
        int t = 0;
        for (int i = 0; i < E; i++) t += p[i][j];
        if (t > maxJ) { maxJ = t; mejorJ = j; }
    }
    cout << "Lider: equipo " << lider + 1 << "\nJornada con mas puntos: " << mejorJ + 1
         << " (" << maxJ << ")\n";
    return 0;
}
```
:::
:::

:::tarea A | T2. ¿Es una matriz identidad? (completa con pistas) | 20 min | Problema por completar
**Contexto.** En gráficos 3D, la matriz identidad significa «no transformar nada». Lee una matriz 3 × 3 y decide si es identidad (1 en la diagonal principal, 0 en el resto). Muestra también la suma de su diagonal (su **traza**).

```cpp blank title="identidad.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int N = 3;
    int m[N][N];
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> __1__;                      // 1: casilla a leer
    bool esIdentidad = true;
    int traza = 0;
    for (int i = 0; i < N; i++)
    {
        traza += __2__;                        // 2: elemento de la diagonal principal
        for (int j = 0; j < N; j++)
        {
            int esperado = (__3__) ? 1 : 0;    // 3: condicion de "estar en la diagonal"
            if (m[i][j] != esperado)
                esIdentidad = __4__;           // 4: ya no es identidad
        }
    }
    cout << "Traza: " << traza << "\n";
    cout << (esIdentidad ? "Es identidad\n" : "No es identidad\n");
    return 0;
}
```

:::solucion | T2
{{c:1}} `m[i][j]` · {{c:2}} `m[i][i]` · {{c:3}} `i == j` · {{c:4}} `false`

```cpp run title="identidad.cpp" runs="1 0 0 0 1 0 0 0 1|1 0 0 0 2 0 0 0 1"
#include <iostream>
using namespace std;
int main()
{
    const int N = 3;
    int m[N][N];
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> m[i][j];
    bool esIdentidad = true;
    int traza = 0;
    for (int i = 0; i < N; i++)
    {
        traza += m[i][i];
        for (int j = 0; j < N; j++)
        {
            int esperado = (i == j) ? 1 : 0;
            if (m[i][j] != esperado)
                esIdentidad = false;
        }
    }
    cout << "Traza: " << traza << "\n";
    cout << (esIdentidad ? "Es identidad\n" : "No es identidad\n");
    return 0;
}
```
:::
:::

:::tarea AB | T3. La transpuesta (completa sin pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Una tabla de 2 filas (sucursales) × 4 columnas (meses) debe mostrarse «girada»: 4 filas (meses) × 2 columnas (sucursales).

```cpp blank title="transpuesta.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int F = 2, C = 4;
    int a[F][C] = {{1, 2, 3, 4}, {5, 6, 7, 8}};
    int t[__1__][__2__];
    for (int i = 0; i < F; i++)
        for (int j = 0; j < C; j++)
            __3__ = a[i][j];
    for (int i = 0; i < __4__; i++)
    {
        for (int j = 0; j < __5__; j++)
            cout << t[i][j] << " ";
        __6__
    }
    return 0;
}
```

:::solucion | T3
{{c:1}} `C` · {{c:2}} `F` · {{c:3}} `t[j][i]` · {{c:4}} `C` · {{c:5}} `F` · {{c:6}} `cout << "\n";`

```cpp run title="transpuesta.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int F = 2, C = 4;
    int a[F][C] = {{1, 2, 3, 4}, {5, 6, 7, 8}};
    int t[C][F];
    for (int i = 0; i < F; i++)
        for (int j = 0; j < C; j++)
            t[j][i] = a[i][j];
    for (int i = 0; i < C; i++)
    {
        for (int j = 0; j < F; j++)
            cout << t[i][j] << " ";
        cout << "\n";
    }
    return 0;
}
```
:::
:::

:::tarea AB | T4. Reservación de asientos (problema convencional) | 35 min | Variabilidad
**Contexto.** Una sala tiene 5 filas × 8 asientos. La matriz guarda `0` (libre) o `1` (ocupado); algunos ya están ocupados al inicio. El usuario reserva asientos indicando fila y asiento (desde 1) hasta escribir `0 0`. El programa rechaza asientos inexistentes u ocupados. Al final muestra el mapa (`L` libre, `X` ocupado) y cuántos asientos libres quedan en cada fila.

:::solucion | T4
```cpp run title="sala.cpp" stdin="3 4\n3 4\n9 1\n1 8\n0 0\n"
#include <iostream>
using namespace std;
int main()
{
    const int F = 5, C = 8;
    int sala[F][C] = {};
    sala[0][0] = sala[0][1] = sala[2][5] = 1;       // ocupados de inicio
    int f, c;
    cout << "Fila y asiento (0 0 termina): ";
    cin >> f >> c;
    while (!(f == 0 && c == 0))
    {
        if (f < 1 || f > F || c < 1 || c > C)
            cout << "No existe ese asiento\n";
        else if (sala[f - 1][c - 1] == 1)
            cout << "Ocupado\n";
        else
        {
            sala[f - 1][c - 1] = 1;
            cout << "Reservado\n";
        }
        cout << "Fila y asiento (0 0 termina): ";
        cin >> f >> c;
    }
    for (int i = 0; i < F; i++)
    {
        int libres = 0;
        cout << "Fila " << i + 1 << ": ";
        for (int j = 0; j < C; j++)
        {
            cout << (sala[i][j] ? 'X' : 'L') << ' ';
            if (sala[i][j] == 0) libres++;
        }
        cout << " libres: " << libres << "\n";
    }
    return 0;
}
```
:::
:::

:::tarea A | T5. Todo sobre una matriz (solución libre) | 25 min | Solución libre
**Contexto.** Te dan esta matriz y **ninguna pregunta específica**: descubre y muestra **todo lo que puedas** (sumas de filas y columnas, el mayor y su posición, las diagonales, cuántos pares hay, si es simétrica, el promedio, cuántos valores superan el promedio…).

```console title="Matriz"
 4  9  2  7
 3  5  7  1
 8  1  6  5
 2  6  4  8
```

:::solucion | T5
Una exploración posible:

```cpp run title="explora_matriz.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int N = 4;
    int m[N][N] = {{4, 9, 2, 7}, {3, 5, 7, 1}, {8, 1, 6, 5}, {2, 6, 4, 8}};
    int total = 0, pares = 0, fi = 0, co = 0, dp = 0, ds = 0;
    bool simetrica = true;
    for (int i = 0; i < N; i++)
    {
        dp += m[i][i];
        ds += m[i][N - 1 - i];
        for (int j = 0; j < N; j++)
        {
            total += m[i][j];
            if (m[i][j] % 2 == 0) pares++;
            if (m[i][j] > m[fi][co]) { fi = i; co = j; }
            if (m[i][j] != m[j][i]) simetrica = false;
        }
    }
    double prom = total / double(N * N);
    int sobre = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (m[i][j] > prom) sobre++;
    cout << "Total " << total << ", promedio " << prom << ", sobre el promedio " << sobre << "\n";
    cout << "Pares " << pares << ", mayor " << m[fi][co] << " en [" << fi << "][" << co << "]\n";
    cout << "Diagonales " << dp << " y " << ds << ", simetrica: " << (simetrica ? "si" : "no") << "\n";
    return 0;
}
```
:::
:::

:::tarea B | T6. La tabla que suma mal (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
**Contexto.** El programa debía mostrar la suma de cada **columna** de una matriz 2 × 3, pero muestra valores extraños (y en otra computadora incluso falló). Explica **cada** error y corrígelo.

```cpp blank title="columnas_bug.cpp"
const int F = 2, C = 3;
int m[F][C] = {{1, 2, 3}, {4, 5, 6}};
int suma = 0;
for (int i = 0; i < C; i++)
{
    for (int j = 0; j < F; j++)
        suma += m[i][j];
    cout << "Columna " << i << ": " << suma << "\n";
}
```

{{lineas:4}}

:::solucion | T6
1. `suma` se inicializa una sola vez: debe reiniciarse dentro del ciclo externo.
2. El externo recorre columnas con `i`, pero el acceso `m[i][j]` usa `i` como **fila**: con `i = 2` accede a `m[2][…]`, que no existe (fuera de rango). Debe ser `m[j][i]` (fila `j`, columna `i`).

```cpp run title="columnas.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int F = 2, C = 3;
    int m[F][C] = {{1, 2, 3}, {4, 5, 6}};
    for (int col = 0; col < C; col++)
    {
        int suma = 0;
        for (int fil = 0; fil < F; fil++)
            suma += m[fil][col];
        cout << "Columna " << col << ": " << suma << "\n";
    }
    return 0;
}
```
Usar nombres como `fil` y `col` en lugar de `i` y `j` evita este tipo de confusión.
:::
:::

:::tarea B | T7. Girar una imagen 90° (imaginación) | 30 min | Imaginación
**Contexto.** Una imagen en blanco y negro de 3 × 4 píxeles está guardada en una matriz. **Imagina** cómo se ve girada 90° en el sentido de las manecillas del reloj: ¿cuántas filas y columnas tendrá?, ¿a dónde va el píxel `[0][0]`?, ¿y el `[2][3]`? Dibuja la imagen girada a mano, **deduce la fórmula** de la nueva posición y después prográmala.

```console title="Imagen original (3 × 4)"
# . . .
# # . .
# # # .
```

:::solucion | T7
La imagen girada tiene 4 × 3. El píxel `[i][j]` va a `[j][F − 1 − i]`: `[0][0]` → `[0][2]` y `[2][3]` → `[3][0]`.

```cpp run title="rotar90.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int F = 3, C = 4;
    char img[F][C] = {{'#', '.', '.', '.'}, {'#', '#', '.', '.'}, {'#', '#', '#', '.'}};
    char rot[C][F];
    for (int i = 0; i < F; i++)
        for (int j = 0; j < C; j++)
            rot[j][F - 1 - i] = img[i][j];
    for (int i = 0; i < C; i++)
    {
        for (int j = 0; j < F; j++) cout << rot[i][j] << ' ';
        cout << "\n";
    }
    return 0;
}
```
:::
:::

:::tarea AB | T8. Cuadrado mágico de orden impar (reto colaborativo, tesis §6.1.14) | 45 min | Memoria colectiva de trabajo, Variabilidad
**Contexto.** «Escribir un programa que visualice un cuadrado mágico de orden impar `n` comprendido entre 3 y 11; el usuario debe elegir el valor de `n`. Un cuadrado mágico se compone de números enteros comprendidos entre 1 y `n²`. La suma de los números que figuran en cada fila, columna y diagonal son iguales» (adaptado de Weiss, citado en la tesis).

```console title="Ejemplo n = 3"
8 1 6
3 5 7
4 9 2
```

:::colab | Organización (grupos heterogéneos)
El problema combina variables, condicionales, ciclos y matrices: formen equipos donde **no todos dominen los mismos temas**, para que se complementen.
- **Integrante 1:** validación de `n` (impar, 3 a 11) con `do-while`.
- **Integrante 2:** el **método siamés**: el 1 va en la fila 0, columna central; cada número siguiente va una fila **arriba** y una columna a la **derecha** (dando la vuelta por los bordes); si esa casilla está ocupada, se coloca **debajo** del anterior.
- **Integrante 3:** mostrar el cuadrado con `setw`.
- **Integrante 4:** verificar que todas las filas, columnas y diagonales sumen `n(n² + 1) / 2`.

Al terminar, cada equipo **explica su solución a los demás equipos**, como propone la tesis.
:::

:::solucion | T8
```cpp run title="cuadrado_magico.cpp" runs="4\n3|5"
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    const int MAX = 11;
    int n;
    do {
        cout << "Orden impar (3-11): ";
        cin >> n;
    } while (n < 3 || n > MAX || n % 2 == 0);
    int m[MAX][MAX] = {};
    int i = 0, j = n / 2;
    for (int k = 1; k <= n * n; k++)
    {
        m[i][j] = k;
        int ni = (i - 1 + n) % n, nj = (j + 1) % n;   // arriba y a la derecha, con vuelta
        if (m[ni][nj] != 0)                         // ocupada: abajo del actual
        {
            ni = (i + 1) % n;
            nj = j;
        }
        i = ni; j = nj;
    }
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < n; c++) cout << setw(4) << m[r][c];
        cout << "\n";
    }
    int objetivo = n * (n * n + 1) / 2;
    bool ok = true;
    int d1 = 0, d2 = 0;
    for (int r = 0; r < n; r++)
    {
        int sf = 0, sc = 0;
        for (int c = 0; c < n; c++) { sf += m[r][c]; sc += m[c][r]; }
        if (sf != objetivo || sc != objetivo) ok = false;
        d1 += m[r][r];
        d2 += m[r][n - 1 - r];
    }
    if (d1 != objetivo || d2 != objetivo) ok = false;
    cout << "Constante magica " << objetivo << ": " << (ok ? "verificado" : "ERROR") << "\n";
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · ¿Quién ganó en el juego del gato? | Modalidad, Ejemplo resuelto
*Guion segmentado (≈ 4 min), con el tablero en pantalla.*

**Problema:** «Dado un tablero de gato (3 × 3) con `X`, `O` o `.`, decir si ganó X, ganó O o nadie».

**Segmento 1 — Enumerar los casos.** {{como}} Cuento las formas de ganar: 3 filas, 3 columnas y 2 diagonales: 8 líneas. {{porque}} Si escribo las 8 comparaciones a mano es fácil equivocarse; mejor recorro filas y columnas con un ciclo y trato las diagonales aparte.

**Segmento 2 — Una función de pensamiento: «tres iguales y no vacías».** {{como}} Para cada fila `i` reviso `t[i][0] == t[i][1] && t[i][1] == t[i][2] && t[i][0] != '.'`. Para cada columna, lo mismo cambiando el orden de los índices. {{porque}} La condición `!= '.'` evita declarar ganador a una fila vacía; ese es el error que más se comete.

**Segmento 3 — Guardar el ganador, no solo un sí/no.** {{como}} Uso `char ganador = '.'` y, cuando encuentro una línea completa, guardo el símbolo. {{porque}} Así la misma lógica sirve para X y para O sin duplicar código.

**Segmento 4 — Probar con tableros diseñados a propósito.** {{como}} Pruebo un tablero donde O gana por columna, otro donde X gana por diagonal secundaria y uno sin ganador. {{porque}} Cada prueba ejercita un recorrido distinto (columnas, diagonal secundaria, ninguno); si solo probara filas, los errores de índices en columnas pasarían desapercibidos.

```cpp run title="gato.cpp" runs="X O X\nX O .\n. O X|O . X\n. X O\nX . .|X O X\nX O O\nO X X"
#include <iostream>
using namespace std;
int main()
{
    char t[3][3];
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            cin >> t[i][j];
    char ganador = '.';
    for (int i = 0; i < 3; i++)
    {
        if (t[i][0] != '.' && t[i][0] == t[i][1] && t[i][1] == t[i][2]) ganador = t[i][0];
        if (t[0][i] != '.' && t[0][i] == t[1][i] && t[1][i] == t[2][i]) ganador = t[0][i];
    }
    if (t[1][1] != '.' && ((t[0][0] == t[1][1] && t[1][1] == t[2][2]) ||
                           (t[0][2] == t[1][1] && t[1][1] == t[2][0])))
        ganador = t[1][1];
    if (ganador == '.') cout << "Nadie gano\n";
    else cout << "Gano " << ganador << "\n";
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. En `int m[4][6];`, ¿cuántas filas, columnas y elementos hay?
2. ¿Cuál es el último elemento válido de esa matriz?
3. ¿Qué condición cumplen los elementos de la diagonal principal? ¿Y los de la secundaria en una matriz `N × N`?
4. Verdadero o falso: en `int a[][3] = {…};` se puede omitir también el 3.
5. ¿Qué ciclo debe ir por fuera para sumar cada columna?
6. ¿Dónde se inicializa el acumulador de la suma de cada fila?
7. ¿Qué es la transpuesta de una matriz?
8. ¿Qué es el orden por filas (*row-major*)?
9. ¿Cuántos ciclos anidados necesita el producto de dos matrices?
10. ¿Qué devuelve la expresión `m[1, 2]` en C++ y por qué es un error?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida:**

```cpp check title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int m[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int s = 0;
    for (int i = 0; i < 3; i++)
        for (int j = i; j < 3; j++)
            s += m[i][j];
    cout << s << " " << m[2][0] + m[0][2] << "\n";
    return 0;
}
```

**P2.** Escribe el fragmento que muestre solo los **bordes** de una matriz `F × C` (y espacios en el interior).

**P3. Corrige:** `int t[3][3]; for (int i = 1; i <= 3; i++) for (int j = 1; j <= 3; j++) t[i][j] = i * j;`

**P4. Escribe un programa** que lea una matriz 4 × 4 de temperaturas (cuatro sensores × cuatro horas) y muestre, para cada sensor, su máximo y la hora en que ocurrió, y la hora con el promedio más alto.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Declaro, capturo y muestro matrices como tablas.</li>
<li>Sumo por filas, por columnas y diagonales, reiniciando acumuladores en el lugar correcto.</li>
<li>Distingo filas y columnas incluso en matrices no cuadradas.</li>
<li>Modelo problemas reales (tableros, ventas, asientos) con matrices.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 4 filas, 6 columnas, 24 elementos · 2 `m[3][5]` · 3 `i == j`; `i + j == N − 1` · 4 Falso: solo puede omitirse el número de filas · 5 El de columnas · 6 Dentro del ciclo de filas, antes del ciclo de columnas · 7 La matriz que resulta de intercambiar filas por columnas · 8 Los elementos se guardan en memoria fila tras fila, en una sola secuencia contigua · 9 Tres · 10 El operador coma descarta el 1 y queda `m[2]` (la fila 2 completa, no un entero); es un error porque no accede a fila 1, columna 2.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** Se suman los elementos del triángulo superior (1 + 2 + 3 + 5 + 6 + 9 = 26) y `7 + 3 = 10`:

```cpp run title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int m[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int s = 0;
    for (int i = 0; i < 3; i++)
        for (int j = i; j < 3; j++)
            s += m[i][j];
    cout << s << " " << m[2][0] + m[0][2] << "\n";
    return 0;
}
```

**P2.** `for (int i = 0; i < F; i++) { for (int j = 0; j < C; j++) { if (i == 0 || i == F - 1 || j == 0 || j == C - 1) cout << setw(4) << m[i][j]; else cout << "    "; } cout << "\n"; }`

**P3.** Los índices van de 0 a 2: `for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) t[i][j] = (i + 1) * (j + 1);` (si se quiere la tabla del 1 al 3).

**P4.**

```cpp run title="sensores.cpp" stdin="21 23 25 24\n19 22 26 20\n24 24 23 22\n18 21 22 27\n"
#include <iostream>
using namespace std;
int main()
{
    const int S = 4, H = 4;
    double t[S][H];
    for (int i = 0; i < S; i++)
        for (int j = 0; j < H; j++)
            cin >> t[i][j];
    for (int i = 0; i < S; i++)
    {
        int hmax = 0;
        for (int j = 1; j < H; j++)
            if (t[i][j] > t[i][hmax]) hmax = j;
        cout << "Sensor " << i + 1 << ": max " << t[i][hmax] << " a la hora " << hmax + 1 << "\n";
    }
    int mejorH = 0;
    double mejorProm = -1e9;
    for (int j = 0; j < H; j++)
    {
        double s = 0;
        for (int i = 0; i < S; i++) s += t[i][j];
        if (s / S > mejorProm) { mejorProm = s / S; mejorH = j; }
    }
    cout << "Hora con mayor promedio: " << mejorH + 1 << " (" << mejorProm << ")\n";
    return 0;
}
```
:::
