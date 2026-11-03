---
num: "08"
archivo: "Tema08_Arreglos_unidimensionales_vectores"
titulo: "Arreglos unidimensionales (vectores)"
corto: "Arreglos (vectores)"
lema: "Muchos datos del mismo tipo, un solo nombre y un número de casilla para cada uno."
duracion: "6 h · 3 sesiones de 2 h"
previos: "Tema 06 y Tema 07 (ciclos `for`, contadores, acumuladores, ciclos anidados)."
fuentes:
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Cap. 6: Arreglos unidimensionales (§6.1 Concepto, §6.2 Declaración, §6.3 Inicialización: en la declaración, aleatoria y por captura; §6.4 Ejercicios)."
  - "Lospinoso, J. (2019). *C++ Crash Course*. Cap. 2: Arrays (Array Initialization, Accessing Array Elements, A Nickel Tour of for Loops, range-based for). Cap. 13: Sequence Containers (`std::array`, `std::vector`)."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §6.1.1–6.1.17: ejemplos de arreglos (llenado con tamaño TAM, ordenamiento burbuja y selección) para los efectos de la TCC."
objetivos:
  A:
    - "Declarar e inicializar arreglos y acceder a sus elementos por índice (de 0 a n − 1)."
    - "Recorrer arreglos con `for` para capturar, mostrar, sumar, promediar y encontrar máximo y mínimo."
    - "Buscar un valor (búsqueda secuencial) y contar ocurrencias."
    - "Ordenar un arreglo con el método de la burbuja."
  B:
    - "Usar el `for` de rango, `std::size`, `std::array` y `std::vector` con tamaño definido en ejecución."
    - "Explicar el acceso fuera de rango (comportamiento indefinido) y prevenirlo (`.at()`)."
    - "Implementar el ordenamiento por selección y compararlo con la burbuja."
    - "Llenar arreglos con números aleatorios (`rand`, `srand`) y verificar los resultados."
efectos:
  soporte:
    - ["Elementos aislados", "Necesidad → declaración e índices → inicialización → recorrido → patrones → búsqueda → aleatorios → ordenamiento."]
    - ["Atención dividida", "Burbuja explicada con una traza visual integrada: explicación, estado del arreglo y código en un mismo lugar (tesis §6.1.4)."]
    - ["Ejemplo resuelto", "Crear y llenar un arreglo de tamaño TAM: algoritmo → pseudocódigo → C++ comentado (tesis §6.1.2)."]
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
    A: "Arreglos estáticos, recorridos, búsqueda, burbuja con traza visual."
    B: "`std::vector`, `std::array`, `.at()`, `for` de rango, selección vs burbuja."
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
    B: "Compilación con `-fsanitize=address` para detectar accesos fuera de rango."
plan:
  - ["Sesión 1", "Soporte", "Pregunta inicial; conceptos 1–5; ejemplo resuelto TAM; T1 y T2.", "120 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–8; burbuja humana; T3, T4; Ruta B: T6, T7.", "120 min"]
  - ["Sesión 3", "Tareas + evaluación", "T5, T8 colaborativa, T9 (Ruta B), protocolo verbal, tests.", "120 min"]
glosario:
  - ["arreglo / vector", "array", "Colección de elementos del mismo tipo guardados de forma contigua bajo un nombre."]
  - ["elemento", "element", "Cada valor guardado en el arreglo."]
  - ["índice / subíndice", "index", "Posición de un elemento; en C++ empieza en 0."]
  - ["tamaño", "size / length", "Número de elementos del arreglo."]
  - ["recorrido", "traversal", "Visitar cada elemento, normalmente con un `for`."]
  - ["búsqueda secuencial", "linear search", "Revisar los elementos uno por uno hasta encontrar el buscado."]
  - ["ordenamiento burbuja", "bubble sort", "Comparar vecinos e intercambiarlos si están en desorden, en varias pasadas."]
  - ["ordenamiento por selección", "selection sort", "Buscar el menor y colocarlo al inicio; repetir con el resto."]
  - ["intercambio", "swap", "Cambiar de lugar dos valores usando una variable auxiliar."]
  - ["fuera de rango", "out of bounds", "Acceder a un índice que no existe; produce comportamiento indefinido."]
  - ["comportamiento indefinido", "undefined behavior", "El estándar no dice qué pasa: puede funcionar, fallar o corromper datos."]
  - ["for de rango", "range-based for", "`for (int x : arreglo)`: recorre todos los elementos sin índices."]
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
Las listas están en todas partes: los puntajes más altos de un juego, las lecturas de un sensor cada segundo, los píxeles de una fila de la pantalla, las canciones de una lista de reproducción. Los arreglos permiten **guardar** muchos datos y **procesarlos con ciclos**, y son la puerta a los algoritmos de búsqueda y ordenamiento que usan todas las aplicaciones. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | ¿Por qué arreglos? | Elementos aislados, Atención dividida
<div class="cols eq">
<div>

```cpp check title="sin arreglo"
#include <iostream>
using namespace std;
int main()
{
    double c1, c2, c3, c4, c5;
    cin >> c1 >> c2 >> c3 >> c4 >> c5;
    double prom = (c1 + c2 + c3 + c4 + c5) / 5;
    // ¿Cuantas superan el promedio?
    int arriba = 0;
    if (c1 > prom) arriba++;
    if (c2 > prom) arriba++;
    if (c3 > prom) arriba++;
    if (c4 > prom) arriba++;
    if (c5 > prom) arriba++;
    cout << arriba << "\n";
    return 0;
}
```

</div>
<div>

```cpp check title="con arreglo"
#include <iostream>
using namespace std;
int main()
{
    const int N = 5;
    double c[N], suma = 0;
    for (int i = 0; i < N; i++)
    {
        cin >> c[i];
        suma += c[i];
    }
    double prom = suma / N;
    int arriba = 0;
    for (int i = 0; i < N; i++)
        if (c[i] > prom) arriba++;
    cout << arriba << "\n";
    return 0;
}
```

</div>
</div>

Con 40 alumnos, la versión de la izquierda necesitaría 40 variables y 40 `if`; a la derecha solo cambias `N = 40`. Y observa: hacen falta **dos** recorridos (primero el promedio, luego comparar), así que los datos deben **guardarse**.
:::

:::concepto | 2 | Declaración, índices y memoria | Elementos aislados, Atención dividida
`tipo nombre[TAMAÑO];` reserva `TAMAÑO` casillas **contiguas** en memoria. Los índices van de **0** a **TAMAÑO − 1**.

```cpp run
#include <iostream>
using namespace std;
int main()
{
    int edades[5] = {12, 15, 9, 20, 17};   //> 5 enteros: índices 0, 1, 2, 3 y 4
    cout << "Primero: " << edades[0] << "\n";  //> El primer elemento es el [0]
    cout << "Ultimo:  " << edades[4] << "\n";  //> El último es el [TAMAÑO − 1]
    edades[2] = 10;                             //> Un elemento se usa como cualquier variable
    cout << "Nuevo [2]: " << edades[2] << "\n";
    cout << "Bytes: " << sizeof(edades) << "\n"; //> 5 × 4 bytes = 20
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
| `int c[5] = {};` o `int c[5]{};` | 0 0 0 0 0 |
| `int d[] = {1, 2, 3};` | el tamaño (3) se deduce de la lista |
| `int e[5];` | **basura**: sin inicializar |

El tamaño debe ser una **constante** conocida al compilar: `const int N = 40; int notas[N];`. Si el tamaño lo decide el usuario, usa un máximo (`MAX`) o un `std::vector` (concepto 9).
:::

:::concepto | 4 | Recorrer: el `for` de 0 a N − 1 | Elementos aislados, Atención dividida
El patrón que usarás en casi todos los programas con arreglos:

```cpp run title="captura_muestra.cpp" stdin="23.5\n25\n27.1\n22\n19.8\n"
#include <iostream>
using namespace std;
int main()
{
    const int N = 5;
    double temp[N];
    for (int i = 0; i < N; i++)             //> `i < N` (no `<=`): el último índice es N − 1
    {
        cout << "Temperatura del dia " << i + 1 << ": ";  //> Para el usuario los días empiezan en 1
        cin >> temp[i];                     //> Captura en la casilla i
    }
    cout << "Registradas:";
    for (int i = 0; i < N; i++)
        cout << " " << temp[i];             //> Muestra cada casilla
    cout << "\n";
    return 0;
}
```
:::

:::concepto | 5 | Patrones: suma, promedio, máximo y mínimo | Elementos aislados, Atención dividida
```cpp run title="estadisticas.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int N = 6;
    int ventas[N] = {120, 340, 95, 410, 260, 180};
    int suma = 0;
    int posMax = 0, posMin = 0;            //> Guardamos la POSICIÓN del mayor y del menor
    for (int i = 0; i < N; i++)
    {
        suma += ventas[i];                 //> Acumulador
        if (ventas[i] > ventas[posMax]) posMax = i;   //> ¿Hay uno mayor que el mejor hasta ahora?
        if (ventas[i] < ventas[posMin]) posMin = i;
    }
    cout << "Total: " << suma << "  Promedio: " << static_cast<double>(suma) / N << "\n";
    cout << "Mejor mes: " << posMax + 1 << " (" << ventas[posMax] << ")\n";
    cout << "Peor mes:  " << posMin + 1 << " (" << ventas[posMin] << ")\n";
    return 0;
}
```
**Clave del máximo:** empieza suponiendo que el mejor es el **primero** (no 0, porque podría haber valores negativos).
:::

:::concepto | 6 | Búsqueda secuencial | Elementos aislados
Revisar uno por uno hasta encontrar el valor buscado:

```cpp run title="busqueda.cpp" runs="41|7"
#include <iostream>
using namespace std;
int main()
{
    const int N = 8;
    int folios[N] = {17, 3, 41, 8, 25, 41, 12, 30};
    int buscado, pos = -1;                  //> -1 significa «no encontrado»
    cout << "Folio a buscar: ";
    cin >> buscado;
    for (int i = 0; i < N; i++)
    {
        if (folios[i] == buscado)
        {
            pos = i;
            break;                          //> Primera aparición: ya no seguimos
        }
    }
    if (pos != -1)
        cout << "Encontrado en la posicion " << pos << "\n";
    else
        cout << "No existe\n";
    return 0;
}
```
:::

:::concepto | 7 | Llenado aleatorio (`rand` y `srand`) | Elementos aislados
Para pruebas y juegos se llenan arreglos con números pseudoaleatorios (Betancourt y Polanco, §6.3.2):

```cpp run title="aleatorios.cpp"
#include <iostream>
#include <cstdlib>          //> rand, srand
#include <ctime>            //> time
using namespace std;
int main()
{
    const int N = 10;
    int dados[N];
    srand(42);              //> Semilla fija: misma secuencia siempre (útil para probar). Con srand(time(0)) cambia en cada ejecución
    for (int i = 0; i < N; i++)
        dados[i] = rand() % 6 + 1;   //> rand() % 6 da 0..5; +1 da 1..6
    for (int i = 0; i < N; i++)
        cout << dados[i] << " ";
    cout << "\n";
    return 0;
}
```
*En tu computadora los números pueden ser distintos: cada compilador implementa `rand` a su manera.*
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

```cpp run title="burbuja.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int N = 5;
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
    for (int i = 0; i < N; i++) cout << v[i] << " ";
    cout << "\n";
    return 0;
}
```

:::nota | ¿Por qué hace falta `aux`?
Si escribieras `v[j] = v[j + 1]; v[j + 1] = v[j];`, la primera asignación **destruye** el valor original de `v[j]` y ambos quedarían iguales. `aux` lo guarda temporalmente (en C++ también existe `swap(v[j], v[j + 1]);`).
:::
:::

:::movimiento | Burbuja humana (15 min)
Seis estudiantes forman una fila con tarjetas numéricas al azar. Un «comparador» camina de izquierda a derecha: en cada par de vecinos, si el de la izquierda tiene número mayor, **ambos cambian de lugar**. Al llegar al final, el mayor queda en el extremo derecho y se sienta (ya está en su lugar). Se repiten las pasadas. El grupo cuenta cuántas comparaciones e intercambios hubo. Después prueben con la fila ya ordenada: ¿cuántos intercambios hay?
:::

:::concepto | 9 | Ruta B · `std::vector`, `std::array`, `for` de rango y `.at()` | Elementos aislados, Reversión de la experiencia
El *C++ Crash Course* (cap. 2 y 13) recomienda contenedores de la biblioteca estándar:

```cpp run title="vector.cpp" stdin="4\n10 20 30 40\n"
#include <iostream>
#include <vector>
#include <array>
using namespace std;
int main()
{
    int tam;
    cin >> tam;
    vector<int> datos(tam);                 //> Tamaño decidido en EJECUCIÓN
    for (int i = 0; i < static_cast<int>(datos.size()); i++)
        cin >> datos[i];
    datos.push_back(99);                    //> Puede crecer: agrega al final
    for (int x : datos)                     //> for de rango: «para cada x en datos»
        cout << x << " ";
    cout << "| tam = " << datos.size() << "\n";
    array<int, 3> fijo{7, 8, 9};            //> Arreglo de tamaño fijo con .size()
    cout << fijo.at(1) << "\n";             //> .at() verifica el índice
    return 0;
}
```

:::cuidado | Fuera de rango
`int a[5]; a[5] = 1;` compila, pero escribe **fuera** del arreglo: es **comportamiento indefinido** (puede «funcionar», fallar o dañar otras variables). Con `vector` o `array`, `.at(5)` lanza una excepción en lugar de corromper la memoria.
:::
:::

## 1.2 Ejemplo resuelto: crear y llenar un arreglo de tamaño TAM

:::ejemplo | Arreglo de enteros con tamaño definido por el usuario (tesis §6.1.2) | Ejemplo resuelto, Atención dividida
**Problema.** Crear un programa en C++ que cree y llene un arreglo de números enteros, identificado como `vec`, cuyo tamaño lo define el usuario mediante la variable `TAM`. Al final, mostrar su contenido.

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

**C. Código en C++** (cada línea comentada)

```cpp run title="llenar_arreglo.cpp" stdin="150\n4\n7\n-2\n13\n5\n"
#include <iostream>
using namespace std;
int main()
{
    const int MAX = 100;                  //> Tamaño máximo reservado (constante)
    int vec[MAX];                         //> Paso 3: arreglo con capacidad para MAX enteros
    int TAM;                              //> Paso 2: aquí se guarda el tamaño pedido
    do
    {
        cout << "Tamanio del arreglo (1-" << MAX << "): ";   //> Paso 1: solicitar
        cin >> TAM;
    } while (TAM < 1 || TAM > MAX);       //> Validación: no exceder la capacidad
    for (int i = 0; i < TAM; i++)         //> Paso 4: capturar uno a uno (índices 0..TAM−1)
    {
        cout << "Elemento " << i + 1 << ": ";
        cin >> vec[i];
    }
    cout << "Contenido:";
    for (int i = 0; i < TAM; i++)         //> Mostrar lo capturado
        cout << " " << vec[i];
    cout << "\n";
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
@sub(v, "std::vector · std::array\nfor de rango · .at()")
@hl(e, "¡fuera de rango =\ncomportamiento indefinido!")
a -> i; a -> r; r -> p; r -> b; r -> o; a -> v [style=dashed]; i -> e [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1
| Quiero… | Código |
|---|---|
| Declarar con tamaño constante | `const int N = 10; int a[N];` |
| Declarar e inicializar | `int a[] = {3, 1, 4};` · `double b[N] = {};` |
| Leer todos | `for (int i = 0; i < N; i++) cin >> a[i];` |
| Mostrar todos | `for (int i = 0; i < N; i++) cout << a[i] << " ";` |
| Sumar | `suma = 0; for (…) suma += a[i];` |
| Posición del mayor | `pm = 0; for (int i = 1; i < N; i++) if (a[i] > a[pm]) pm = i;` |
| Contar los que cumplen | `c = 0; for (…) if (cond(a[i])) c++;` |
| Buscar | `pos = -1; for (…) if (a[i] == x) { pos = i; break; }` |
| Intercambiar | `int aux = a[i]; a[i] = a[j]; a[j] = aux;` o `swap(a[i], a[j]);` |
| Copiar un arreglo | `for (…) b[i] = a[i];` (no se puede `b = a;`) |
| Aleatorio entre 1 y k | `rand() % k + 1` (con `srand(time(0));` una vez) |
| Tamaño en ejecución | `vector<int> v(n);` · `v.size()` · `v.push_back(x);` |
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿El ciclo va de <code>0</code> a <code>N − 1</code> (<code>i &lt; N</code>)?</li>
<li>¿El tamaño del arreglo es una constante? ¿Validé que el tamaño pedido no exceda el máximo?</li>
<li>¿Inicialicé el arreglo o lo llené antes de leerlo?</li>
<li>¿En <code>a[i + 1]</code> el índice puede llegar a <code>N</code>? (Entonces el ciclo debe terminar en <code>N − 1</code>.)</li>
<li>Para el máximo/mínimo, ¿empecé con el primer elemento y no con 0?</li>
<li>¿Uso una variable auxiliar al intercambiar?</li>
<li>¿Muestro al usuario posiciones desde 1 aunque internamente empiecen en 0?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) `<=` en lugar de `<`: lectura fuera del arreglo.** El sexto valor que se muestra es basura (o el programa falla):

```cpp blank title="fuera_de_rango.cpp"
int a[5] = {1, 2, 3, 4, 5};
for (int i = 0; i <= 5; i++)   // i = 5 no existe
    cout << a[i] << " ";
```

**b) Tamaño no constante.** g++ lo acepta como extensión (VLA), pero **no es C++ estándar**: con `-pedantic` avisa y otros compiladores (Visual Studio) lo rechazan.

```cpp blank title="vla.cpp"
int n;
cin >> n;
int a[n];          // no estandar: usa const int MAX o vector<int> a(n);
```

**c) Asignar un arreglo completo.**

```cpp err
int main()
{
    int a[3] = {1, 2, 3};
    int b[3];
    b = a;
    return 0;
}
```
*Corrección:* copiar elemento por elemento con un `for` (o usar `std::array`/`std::vector`, que sí se asignan).

**d) Máximo inicializado en 0** con datos negativos: `{-5, -2, -9}` daría 0 como máximo. Empieza con `a[0]`.

**e) Intercambio sin auxiliar:** `a[i] = a[j]; a[j] = a[i];` deja los dos valores iguales.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Invertir una lista | Variabilidad
Mismo recorrido, otra tarea: intercambiar el primero con el último, el segundo con el penúltimo… hasta la mitad.

```cpp run title="invertir.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int N = 7;
    char letras[N] = {'R', 'E', 'C', 'O', 'N', 'O', 'C'};
    for (int i = 0; i < N / 2; i++)           //> Solo hasta la mitad: si llega al final, ¡vuelve a invertir!
    {
        char aux = letras[i];
        letras[i] = letras[N - 1 - i];        //> El «espejo» de i es N − 1 − i
        letras[N - 1 - i] = aux;
    }
    for (int i = 0; i < N; i++) cout << letras[i];
    cout << "\n";
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Dibuja las casillas del arreglo en papel cuando dudes qué índice usar.

:::tarea A | T1. Temperaturas de la semana: ejemplo y gemelo | 25 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia:**

```cpp run title="semana.cpp" stdin="21 24.5 26 19 23 27.5 22\n"
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    const int DIAS = 7;
    const char* NOMBRES[DIAS] = {"Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"}; //> Arreglo de textos paralelo
    double t[DIAS], suma = 0;
    int pmax = 0;
    for (int i = 0; i < DIAS; i++)
    {
        cin >> t[i];
        suma += t[i];
        if (t[i] > t[pmax]) pmax = i;
    }
    cout << fixed << setprecision(1);
    cout << "Promedio: " << suma / DIAS << " C\n";
    cout << "Dia mas caluroso: " << NOMBRES[pmax] << " (" << t[pmax] << " C)\n";
    cout << "Dias sobre el promedio:";
    for (int i = 0; i < DIAS; i++)                  //> Segundo recorrido: ya conocemos el promedio
        if (t[i] > suma / DIAS) cout << " " << NOMBRES[i];
    cout << "\n";
    return 0;
}
```

**Paso 2 · Gemelo.** Una tienda registra sus **ventas de 6 meses**. Lee las 6 cantidades y muestra el total, el promedio, el **peor** mes y los meses que estuvieron **por debajo** del promedio.

:::solucion | T1
```cpp run title="ventas.cpp" stdin="12000 9500 15800 8700 11000 13400\n"
#include <iostream>
using namespace std;
int main()
{
    const int M = 6;
    const char* MES[M] = {"Ene", "Feb", "Mar", "Abr", "May", "Jun"};
    double v[M], total = 0;
    int pmin = 0;
    for (int i = 0; i < M; i++)
    {
        cin >> v[i];
        total += v[i];
        if (v[i] < v[pmin]) pmin = i;
    }
    double prom = total / M;
    cout << "Total: " << total << "  Promedio: " << prom << "\n";
    cout << "Peor mes: " << MES[pmin] << "\nBajo el promedio:";
    for (int i = 0; i < M; i++)
        if (v[i] < prom) cout << " " << MES[i];
    cout << "\n";
    return 0;
}
```
:::
:::

:::tarea A | T2. El ejemplo TAM, ahora por completar (tesis §6.1.3) | 25 min | Problema por completar
**Contexto.** Es el mismo problema del ejemplo resuelto, pero **parcialmente resuelto**: completa el algoritmo y los huecos del código.

**Algoritmo:** 1. Solicitar… 2. Guardar… 3. Definir… 4. Capturar…

{{lineas:3}}

```cpp blank title="llenar_completar.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int MAX = 100;
    int vec[__1__];                           // 1: capacidad del arreglo
    int TAM;
    do {
        cout << "Tamanio (1-100): ";
        cin >> TAM;
    } while (__2__);                          // 2: repetir mientras sea invalido
    for (int i = __3__; i __4__ TAM; i++)     // 3 y 4: recorrido de todas las casillas
    {
        cout << "Elemento " << i + 1 << ": ";
        cin >> __5__;                         // 5: casilla donde se guarda
    }
    for (int i = 0; i < TAM; i++)
        cout << vec[i] << " ";
    cout << "\n";
    return 0;
}
```

:::solucion | T2
Algoritmo: 1. Solicitar el tamaño del arreglo al usuario. 2. Guardar el valor en `TAM`. 3. Definir el vector del tamaño introducido (dentro de la capacidad `MAX`). 4. Capturar el contenido uno a uno hasta `TAM`.

{{c:1}} `MAX` · {{c:2}} `TAM < 1 || TAM > MAX` · {{c:3}} `0` · {{c:4}} `<` · {{c:5}} `vec[i]`

```cpp run title="llenar_completar.cpp" stdin="0\n3\n8\n6\n4\n"
#include <iostream>
using namespace std;
int main()
{
    const int MAX = 100;
    int vec[MAX];
    int TAM;
    do {
        cout << "Tamanio (1-100): ";
        cin >> TAM;
    } while (TAM < 1 || TAM > MAX);
    for (int i = 0; i < TAM; i++)
    {
        cout << "Elemento " << i + 1 << ": ";
        cin >> vec[i];
    }
    for (int i = 0; i < TAM; i++)
        cout << vec[i] << " ";
    cout << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T3. ¿Dónde está y cuántas veces? (completa sin pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** En una rifa se registraron 10 boletos ganadores (pueden repetirse). Busca un número y muestra **todas** las posiciones donde aparece y cuántas veces.

```cpp blank title="rifa.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int N = 10;
    int boletos[N] = {45, 12, 7, 45, 90, 3, 45, 18, 7, 61};
    int x, veces = 0;
    cin >> x;
    cout << "Posiciones:";
    for (__1__; __2__; __3__)
    {
        if (__4__)
        {
            cout << " " << __5__;
            __6__;
        }
    }
    if (veces == 0) cout << " ninguna";
    cout << "\nAparece " << veces << " veces\n";
    return 0;
}
```

:::solucion | T3
{{c:1}} `int i = 0` · {{c:2}} `i < N` · {{c:3}} `i++` · {{c:4}} `boletos[i] == x` · {{c:5}} `i + 1` (posición para el usuario) · {{c:6}} `veces++`. No hay `break`: se necesitan **todas** las apariciones.

```cpp run title="rifa.cpp" runs="45|7|100"
#include <iostream>
using namespace std;
int main()
{
    const int N = 10;
    int boletos[N] = {45, 12, 7, 45, 90, 3, 45, 18, 7, 61};
    int x, veces = 0;
    cin >> x;
    cout << "Posiciones:";
    for (int i = 0; i < N; i++)
    {
        if (boletos[i] == x)
        {
            cout << " " << i + 1;
            veces++;
        }
    }
    if (veces == 0) cout << " ninguna";
    cout << "\nAparece " << veces << " veces\n";
    return 0;
}
```
:::
:::

:::tarea AB | T4. Estadísticas del grupo (problema convencional) | 35 min | Variabilidad
**Contexto.** Lee el número de alumnos `n` (máximo 40, valídalo) y sus calificaciones (0 a 10, valídalas). Muestra: promedio, la calificación más alta y la más baja, cuántos aprobaron (≥ 6), cuántos están **por encima del promedio** y la lista de calificaciones ordenada de mayor a menor (adapta la burbuja).

:::solucion | T4
```cpp run title="grupo.cpp" stdin="6\n8.5 5 9.5 7 6 10\n"
#include <iostream>
using namespace std;
int main()
{
    const int MAX = 40;
    double c[MAX], suma = 0;
    int n;
    do { cout << "Alumnos (1-40): "; cin >> n; } while (n < 1 || n > MAX);
    for (int i = 0; i < n; i++)
    {
        do { cin >> c[i]; } while (c[i] < 0 || c[i] > 10);
        suma += c[i];
    }
    double prom = suma / n;
    int aprobados = 0, arriba = 0, pmax = 0, pmin = 0;
    for (int i = 0; i < n; i++)
    {
        if (c[i] >= 6) aprobados++;
        if (c[i] > prom) arriba++;
        if (c[i] > c[pmax]) pmax = i;
        if (c[i] < c[pmin]) pmin = i;
    }
    for (int p = 1; p < n; p++)                 // burbuja descendente: cambia > por <
        for (int j = 0; j < n - p; j++)
            if (c[j] < c[j + 1]) { double a = c[j]; c[j] = c[j + 1]; c[j + 1] = a; }
    cout << "Promedio " << prom << " | max " << c[0] << " | min " << c[n - 1]
         << " | aprobados " << aprobados << " | sobre el promedio " << arriba << "\nOrdenadas:";
    for (int i = 0; i < n; i++) cout << " " << c[i];
    cout << "\n";
    return 0;
}
```
Después de ordenar de mayor a menor, el máximo queda en `c[0]` y el mínimo en `c[n − 1]` (las posiciones `pmax` y `pmin` se calcularon antes de ordenar).
:::
:::

:::tarea A | T5. Ordena como quieras (solución libre, tesis §6.1.1) | 25 min | Solución libre
**Contexto.** «Dado un arreglo llamado `enteros`, cuyo contenido es 5, 6, 2, 3, 8, 1, 7, 4: utilizando **cualquier** algoritmo de ordenación, ordena el arreglo y muestra el resultado en pantalla». **Reto ampliado:** genera **todas las soluciones que te sea posible** (burbuja, selección, inserción, contando apariciones, usando `std::sort`…).

:::solucion | T5
Tres soluciones distintas (todas producen `1 2 3 4 5 6 7 8`):

```cpp run title="ordenar_libre.cpp"
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    const int N = 8;
    int a[N] = {5, 6, 2, 3, 8, 1, 7, 4};
    int b[N], c[N];
    for (int i = 0; i < N; i++) { b[i] = a[i]; c[i] = a[i]; }
    // 1) Burbuja
    for (int p = 1; p < N; p++)
        for (int j = 0; j < N - p; j++)
            if (a[j] > a[j + 1]) swap(a[j], a[j + 1]);
    // 2) Insercion: cada elemento se inserta en su lugar entre los ya ordenados
    for (int i = 1; i < N; i++)
    {
        int x = b[i], j = i - 1;
        while (j >= 0 && b[j] > x) { b[j + 1] = b[j]; j--; }
        b[j + 1] = x;
    }
    // 3) Biblioteca estandar
    sort(c, c + N);
    for (int i = 0; i < N; i++) cout << a[i] << " ";
    cout << "| ";
    for (int i = 0; i < N; i++) cout << b[i] << " ";
    cout << "| ";
    for (int i = 0; i < N; i++) cout << c[i] << " ";
    cout << "\n";
    return 0;
}
```
La selección aparece en la T7.
:::
:::

:::tarea B | T6. ¿Puedes ayudar a tus compañeros? (autoexplicación, tesis §6.1.6) | 20 min | Autoexplicación, Reversión de la experiencia
**Contexto.** La maestra envió un programa de ejemplo sobre el método de la burbuja, pero algunos de tus compañeros no entendieron el tema y tampoco el ejemplo. **Revisa el código y, en el espacio de abajo, explica con tus palabras a tus compañeros cada bloque** (A, B, C y D). Incluye por qué el ciclo interno llega a `N - 1 - p` y para qué sirve la variable `hubo`.

```cpp run title="burbuja_mejorada.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int N = 6;
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
    for (int x : v) cout << x << " ";
    cout << "\n";
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
2. Genera el pseudocódigo en PSeInt y el código en C++ de tu representación.
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

```cpp run title="seleccion.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int N = 5;
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
    for (int x : a) cout << x << " ";
    cout << "\nComparaciones: " << comparaciones << "  Intercambios: " << intercambios << "\n";
    return 0;
}
```
La selección siempre hace `N(N−1)/2 = 10` comparaciones, pero **pocos intercambios** (como máximo `N − 1`); la burbuja, con el mismo arreglo, hace el mismo número de comparaciones y más intercambios.
:::
:::

:::tarea AB | T8. Votación escolar (reto colaborativo) | 40 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Equipos de 4, niveles mezclados. Hay 5 planillas (1 a 5). Se capturan votos (números del 1 al 5) hasta que se escribe 0; los votos fuera de rango cuentan como **nulos**.
- **Integrante 1:** arreglo contador `int votos[5] = {}` y la captura con centinela (`votos[v - 1]++`).
- **Integrante 2:** total de votos válidos y nulos.
- **Integrante 3:** porcentaje de cada planilla con una barra de asteriscos (un `*` por cada 5 %).
- **Integrante 4:** la planilla ganadora y la detección de **empates** en el primer lugar.
:::

:::solucion | T8
```cpp run title="votacion.cpp" stdin="3 1 3 5 2 3 9 1 3 5 1 0\n"
#include <iostream>
using namespace std;
int main()
{
    const int P = 5;
    int votos[P] = {};
    int v, nulos = 0, validos = 0;
    cin >> v;
    while (v != 0)
    {
        if (v >= 1 && v <= P) { votos[v - 1]++; validos++; }
        else nulos++;
        cin >> v;
    }
    int ganador = 0;
    for (int i = 0; i < P; i++)
    {
        double pct = validos > 0 ? 100.0 * votos[i] / validos : 0;
        cout << "Planilla " << i + 1 << ": " << votos[i] << " (" << pct << "%) ";
        for (int k = 0; k < static_cast<int>(pct / 5); k++) cout << "*";
        cout << "\n";
        if (votos[i] > votos[ganador]) ganador = i;
    }
    int empatados = 0;
    for (int i = 0; i < P; i++)
        if (votos[i] == votos[ganador]) empatados++;
    cout << "Validos: " << validos << "  Nulos: " << nulos << "\n";
    if (empatados > 1) cout << "Empate en el primer lugar\n";
    else cout << "Gana la planilla " << ganador + 1 << "\n";
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

```cpp run title="rotar.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int N = 5;
    char j[N] = {'A', 'B', 'C', 'D', 'E'};
    for (int ronda = 1; ronda <= 3; ronda++)
    {
        char ultimo = j[N - 1];
        for (int i = N - 1; i > 0; i--)
            j[i] = j[i - 1];
        j[0] = ultimo;
        cout << "Ronda " << ronda << ": ";
        for (char c : j) cout << c << " ";
        cout << "\n";
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
10. Menciona una ventaja de `std::vector` sobre un arreglo de C.
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida:**

```cpp check title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int a[6] = {4, 9, 2, 9, 5, 1};
    int x = 0, y = 0;
    for (int i = 0; i < 6; i++)
    {
        if (a[i] > a[x]) x = i;
        if (a[i] % 2 == 1) y += a[i];
    }
    cout << x << " " << a[x] << " " << y << "\n";
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
1 `a[0]` y `a[11]` · 2 `3 4 0 0 0` · 3 80 · 4 Porque los arreglos de C no se pueden asignar completos; hay que copiar elemento por elemento · 5 Falso: compila; es comportamiento indefinido en ejecución · 6 −1 · 7 El mayor queda en la última posición · 8 Guardar temporalmente uno de los valores para no perderlo · 9 Un número pseudoaleatorio entre 1 y 10 · 10 Su tamaño puede definirse en ejecución y crecer (`push_back`), conoce su tamaño (`.size()`) y se puede copiar con `=`.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** `x` queda en la primera posición del máximo (1, valor 9, porque `>` no reemplaza al empatado de la posición 3); `y` suma los impares 9 + 9 + 5 + 1 = 24.

```cpp run title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int a[6] = {4, 9, 2, 9, 5, 1};
    int x = 0, y = 0;
    for (int i = 0; i < 6; i++)
    {
        if (a[i] > a[x]) x = i;
        if (a[i] % 2 == 1) y += a[i];
    }
    cout << x << " " << a[x] << " " << y << "\n";
    return 0;
}
```

**P2.** Pasada 1: `2 6 4 9` · Pasada 2: `2 4 6 9` · Pasada 3: `2 4 6 9` (sin cambios).

**P3.** Inicializar `neg = 0`; los índices van de 0 a 7: `for (int i = 0; i < 8; i++)`.

**P4.**

```cpp run title="p4.cpp" stdin="3 8 5 12 7 6 1 10 4 9\n"
#include <iostream>
using namespace std;
int main()
{
    const int N = 10;
    int a[N], pares[N], np = 0;
    for (int i = 0; i < N; i++)
    {
        cin >> a[i];
        if (a[i] % 2 == 0) pares[np++] = a[i];   // np cuenta cuantos pares hay
    }
    cout << "Original:";
    for (int i = 0; i < N; i++) cout << " " << a[i];
    cout << "\nPares:";
    for (int i = 0; i < np; i++) cout << " " << pares[i];
    cout << "\n";
    return 0;
}
```
:::
