---
num: "15"
archivo: "Tema15_Memoria_dinamica"
titulo: "Memoria dinámica: new, delete y arreglos dinámicos"
corto: "Memoria dinámica"
lema: "Pedir memoria cuando la necesitas, del tamaño que necesitas… y devolverla cuando terminas."
duracion: "5 h · 3 sesiones"
previos: "Tema 14 (punteros), Tema 08 (arreglos), Tema 10 (funciones) y Tema 13 (estructuras)."
fuentes:
  - "Lospinoso, J. (2019). *C++ Crash Course*. Cap. 4 «The Object Life Cycle»: An Object's Storage Duration (Automatic, Static, Dynamic Storage Duration; Allocation, Deallocation and Lifetime; Memory Management). Cap. 3: Pointers Are Dangerous, Forward-Linked Lists. Cap. 11: Smart Pointers (`std::unique_ptr`). Cap. 13: `std::vector`."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §5.4: el estudio piloto del modelo CLT4BP abarcó estructuras anidadas, punteros y memoria dinámica (objetivo intermedio: «optimización vía asignación dinámica de memoria», Tabla 5.14)."
objetivos:
  A:
    - "Distinguir la memoria automática (pila) de la memoria dinámica (montón)."
    - "Reservar y liberar una variable dinámica con `new` y `delete`."
    - "Crear arreglos dinámicos con `new[]` y `delete[]` cuyo tamaño se decide en ejecución."
    - "Reconocer y evitar fugas de memoria y punteros colgantes."
  B:
    - "Redimensionar un arreglo dinámico copiando sus datos a uno más grande."
    - "Crear estructuras enlazadas con nodos dinámicos y liberarlas por completo."
    - "Reservar matrices dinámicas (arreglo de punteros a filas)."
    - "Explicar por qué `std::vector` y `std::unique_ptr` (RAII) son alternativas más seguras."
efectos:
  soporte:
    - ["Elementos aislados", "Duración de almacenamiento → new/delete de una variable → arreglos dinámicos → fugas → colgantes → funciones que reservan → crecimiento → nodos → RAII."]
    - ["Atención dividida", "Diagramas de pila y montón integrados con cada línea de código."]
    - ["Ejemplo resuelto", "Calificaciones con arreglo dinámico de tamaño elegido por el usuario."]
    - ["Modalidad", "Guion narrado del protocolo verbal sobre los diagramas de pila/montón."]
  procedimental:
    - ["Variabilidad", "El par reservar/liberar en contextos distintos (arreglos, nodos, matrices)."]
    - ["Autoexplicación", "Lista de verificación «por cada new, un delete» explicada en voz alta."]
  tareas:
    - ["Ejemplo resuelto", "T1: temperaturas dinámicas + gemelo (precios)."]
    - ["Problema por completar", "T2 (crear arreglo, con pistas) y T3 (agrandar, sin pistas)."]
    - ["Desvanecimiento de guía", "T1 → T4."]
    - ["Solución libre", "T5: todas las formas de tener n datos con n leído en ejecución."]
    - ["Autoexplicación", "T6: fugas, `delete` vs `delete[]`, colgantes."]
    - ["Imaginación", "T7: imaginar pila y montón línea por línea."]
    - ["Memoria colectiva de trabajo", "T8: cola de turnos con nodos dinámicos."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Pila vs montón, `new`/`delete`, `new[]`/`delete[]`, fugas y colgantes."
    B: "Redimensionamiento, nodos dinámicos, matrices dinámicas, RAII."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 dibujando pila y montón."
    B: "T5, T6, T7 autónomas; diseñadores de la estructura en T8."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Lista de compras que crece (T4) sin fugas."
    B: "Cola de turnos dinámica (T8) que libera todo al terminar."
  Entorno:
    comp: "Información procedimental"
    A: "Hoja de diagramas pila/montón."
    B: "Compilar con `-fsanitize=address` (detecta fugas y accesos inválidos)."
plan:
  - ["Sesión 1", "Soporte + tareas", "Analogía del hotel; conceptos 1–5; ejemplo resuelto; T1, T2.", "100 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–9; T3, T4; Ruta B: T6, T7.", "100 min"]
  - ["Sesión 3", "Tareas + evaluación", "T5, T8 colaborativa; protocolo verbal; tests; instrumentos de carga cognitiva.", "100 min"]
glosario:
  - ["memoria dinámica", "dynamic memory", "Memoria que el programa pide y libera en ejecución."]
  - ["montón", "heap / free store", "Zona de memoria para objetos dinámicos."]
  - ["pila", "stack", "Zona de memoria de las variables automáticas (locales)."]
  - ["duración de almacenamiento", "storage duration", "Tiempo de vida de un objeto: automática, estática o dinámica."]
  - ["reservar / asignar", "allocate (`new`)", "Pedir memoria al montón."]
  - ["liberar", "deallocate (`delete`)", "Devolver memoria al montón."]
  - ["arreglo dinámico", "dynamic array (`new T[n]`)", "Arreglo cuyo tamaño se decide en ejecución."]
  - ["fuga de memoria", "memory leak", "Memoria reservada que ya no se puede liberar porque se perdió su dirección."]
  - ["puntero colgante", "dangling pointer", "Puntero a memoria ya liberada."]
  - ["doble liberación", "double free", "Liberar dos veces el mismo bloque: comportamiento indefinido."]
  - ["nodo", "node", "Estructura con datos y un puntero a otro nodo."]
  - ["RAII", "Resource Acquisition Is Initialization", "Un objeto adquiere el recurso al crearse y lo libera al destruirse (vector, unique_ptr)."]
  - ["puntero inteligente", "smart pointer (`unique_ptr`)", "Objeto que libera automáticamente la memoria que posee."]
---

# 1. Información de soporte {.soporte}

:::analogia | El hotel y la mochila
Tus variables locales son como lo que llevas en la **mochila**: cabe poco, se organiza solo (lo último que metes es lo primero que sacas) y, al terminar el día (la función), se vacía sola. Cuando necesitas más espacio, o espacio que dure más que un día, **rentas un cuarto de hotel** (el **montón**): pides el cuarto (`new`), te dan la **llave con el número de cuarto** (un puntero) y, cuando terminas, **debes entregar el cuarto** (`delete`). Si pierdes la llave sin entregarlo, el cuarto queda ocupado para siempre: eso es una **fuga de memoria**.
:::

:::pregunta
En el Tema 08 reservaste `int notas[100]` aunque el grupo tuviera 12 alumnos, y no podías tener más de 100. **¿Cómo crees que una app de fotos guarda 15 fotos hoy y 3 000 mañana sin saber de antemano cuántas habrá?**

{{lineas:2}}
:::

:::relevancia
Las listas que crecen (mensajes de un chat, enemigos que aparecen en un juego, filas que se cargan de un archivo) necesitan memoria cuyo tamaño se decide **mientras el programa corre**. `std::vector`, `std::string` y todos los contenedores usan memoria dinámica por dentro. Entender `new` y `delete` te permite saber qué hacen y evitar los dos errores más costosos de C++: las fugas y los punteros colgantes. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | ¿Cuánto vive un objeto? Duración de almacenamiento | Elementos aislados, Atención dividida
El *C++ Crash Course* (cap. 4) clasifica los objetos por su **duración**:

| Duración | Dónde vive | Cuándo nace | Cuándo muere | Ejemplo |
|---|---|---|---|---|
| Automática | pila | al entrar al bloque | al salir del bloque | variables locales, parámetros |
| Estática | zona estática | al iniciar el programa (o la 1.ª llamada) | al terminar el programa | globales, `static` locales |
| **Dinámica** | **montón** | cuando se ejecuta `new` | cuando se ejecuta `delete` | `new int`, `new double[n]` |

```diagram mem
regions:
  - name: "Pila (automática)"
    vars:
      - {name: n, type: int, val: 3}
      - {name: p, type: "int*", val: "0x5a0", kind: ptr, to: bloque}
  - name: "Montón (dinámica)"
    color: "#fdf4ff"
    vars:
      - {name: bloque, type: "int[3]", val: "7 | 8 | 9", addr: "0x5a0"}
figcaption: "Figura 1. El puntero vive en la pila; el bloque que reservó con new vive en el montón."
```
:::

:::concepto | 2 | `new` y `delete`: una variable dinámica | Elementos aislados, Atención dividida
```cpp run title="new_delete.cpp"
#include <iostream>
using namespace std;
int main()
{
    int* p = new int(42);       //> `new int(42)`: reserva un int en el montón, lo inicia en 42 y devuelve su dirección
    cout << "*p = " << *p << "\n";
    *p += 8;                     //> Se usa como cualquier puntero
    cout << "*p = " << *p << "\n";
    delete p;                    //> Devuelve la memoria al montón (el puntero sigue existiendo)
    p = nullptr;                 //> Buena práctica: así no queda «colgando»
    return 0;
}
```
**Regla de oro:** por cada `new`, **exactamente un** `delete`.
:::

:::concepto | 3 | Arreglos dinámicos: el tamaño se decide en ejecución | Elementos aislados, Atención dividida
`new tipo[n]` reserva `n` elementos contiguos; se liberan con `delete[]` (con corchetes):

```cpp run title="arreglo_dinamico.cpp" stdin="4\n10 20 30 40\n"
#include <iostream>
using namespace std;
int main()
{
    int n;
    cout << "Cuantos datos? ";
    cin >> n;
    int* datos = new int[n];          //> Exactamente n enteros: ni más ni menos (C++ estándar, a diferencia de int a[n])
    for (int i = 0; i < n; i++)
        cin >> datos[i];              //> Se usa con índices, igual que un arreglo
    int suma = 0;
    for (int i = 0; i < n; i++) suma += datos[i];
    cout << "Suma: " << suma << "\n";
    delete[] datos;                   //> new[] se libera con delete[]
    datos = nullptr;
    return 0;
}
```
Esto resuelve el problema del Tema 08 (T2): el tamaño `TAM` del usuario ya no necesita un máximo fijo.
:::

:::concepto | 4 | Fugas de memoria: perder la llave | Elementos aislados, Atención dividida
Si el único puntero a un bloque se pierde (se reasigna o la función termina) **antes** de `delete`, ese bloque queda inaccesible y ocupado hasta que termine el programa:

<div class="cols eq">
<div>

```cpp nolines
int* p = new int[1000];
p = new int[1000];   // el primer bloque
                     // quedo sin llave
delete[] p;          // solo libera el segundo
```

</div>
<div>

```diagram mem
regions:
  - name: "Pila"
    vars:
      - {name: p, type: "int*", val: "0x900", kind: ptr, to: B2}
  - name: "Montón"
    color: "#fdf4ff"
    vars:
      - {name: B1, type: "int[1000]", val: "fuga", kind: dead, addr: "0x500"}
      - {name: B2, type: "int[1000]", val: "...", addr: "0x900"}
```

</div>
</div>

En programas que corren mucho tiempo (servidores, juegos), las fugas se acumulan hasta agotar la memoria.
:::

:::concepto | 5 | Punteros colgantes y doble liberación | Elementos aislados
- **Colgante:** usar el puntero **después** de `delete`: la memoria ya no es tuya.
- **Doble liberación:** hacer `delete` dos veces del mismo bloque: comportamiento indefinido (normalmente el programa aborta).
- **Mezclar formas:** `new` con `delete[]` o `new[]` con `delete`: indefinido.

```cpp blank title="peligros.cpp"
int* p = new int(5);
delete p;
cout << *p;     // colgante: lectura invalida
delete p;       // doble liberacion
```
**Protección sencilla:** después de `delete p;` escribe `p = nullptr;` (borrar un `nullptr` no hace nada y `if (p)` detecta que ya no apunta a nada).
:::

:::concepto | 6 | Funciones que reservan memoria: ¿quién la libera? | Elementos aislados, Atención dividida
Una función puede crear un bloque dinámico y devolver su dirección: el bloque **sobrevive** a la función (a diferencia de una variable local, Tema 14, T6). Pero alguien debe liberarlo: se documenta quién es el **dueño**.

```cpp run title="fabrica.cpp"
#include <iostream>
using namespace std;

int* crearSecuencia(int n)              //> Devuelve un bloque NUEVO: quien llama se vuelve su dueño
{
    int* a = new int[n];
    for (int i = 0; i < n; i++) a[i] = (i + 1) * (i + 1);
    return a;                            //> Correcto: el bloque está en el montón, no en la pila
}

int main()
{
    int* cuadrados = crearSecuencia(6);
    for (int i = 0; i < 6; i++) cout << cuadrados[i] << " ";
    cout << "\n";
    delete[] cuadrados;                  //> El dueño (main) libera
    return 0;
}
```
:::

:::concepto | 7 | Hacer crecer un arreglo dinámico | Elementos aislados, Atención dividida
Un bloque reservado **no** puede agrandarse en su lugar. Para crecer: (1) reservar uno más grande, (2) copiar, (3) liberar el viejo, (4) apuntar al nuevo. Es lo que hace `std::vector` por dentro (duplicando la capacidad):

```cpp run title="crecer.cpp"
#include <iostream>
using namespace std;
int main()
{
    int capacidad = 2, n = 0;
    int* a = new int[capacidad];
    for (int x = 10; x <= 70; x += 10)        //> Insertamos 7 datos en un arreglo de capacidad 2
    {
        if (n == capacidad)                   //> ¿Lleno? Crecer
        {
            int* nuevo = new int[capacidad * 2];      //> 1) más grande (el doble)
            for (int i = 0; i < n; i++) nuevo[i] = a[i];   //> 2) copiar
            delete[] a;                               //> 3) liberar el viejo
            a = nuevo;                                //> 4) apuntar al nuevo
            capacidad *= 2;
            cout << "(crece a " << capacidad << ") ";
        }
        a[n++] = x;
    }
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << "\n";
    delete[] a;
    return 0;
}
```
:::

:::concepto | 8 | Ruta B · Nodos dinámicos | Elementos aislados, Reversión de la experiencia
En el Tema 14 enlazaste vagones que eran variables locales. Con `new`, los nodos se crean **cuando se necesitan**:

```cpp run title="lista_dinamica.cpp"
#include <iostream>
using namespace std;
struct Nodo { int dato; Nodo* sig; };

int main()
{
    Nodo* cabeza = nullptr;
    for (int x = 1; x <= 4; x++)
        cabeza = new Nodo{x * 10, cabeza};          //> Nuevo nodo al INICIO: apunta a la cabeza anterior
    for (Nodo* p = cabeza; p != nullptr; p = p->sig)
        cout << p->dato << " -> ";
    cout << "nullptr\n";
    while (cabeza != nullptr)                        //> Liberar TODOS los nodos
    {
        Nodo* siguiente = cabeza->sig;               //> Guardar el siguiente ANTES de borrar
        delete cabeza;
        cabeza = siguiente;
    }
    return 0;
}
```
:::

:::concepto | 9 | Ruta B · Que la memoria se libere sola: RAII | Elementos aislados, Reversión de la experiencia
El *C++ Crash Course* insiste en que, en C++ moderno, casi nunca se escribe `delete` a mano: se usan objetos que **liberan al destruirse** (RAII), como `std::vector` y los punteros inteligentes (cap. 11):

```cpp run title="raii.cpp" stdin="5\n"
#include <iostream>
#include <vector>
#include <memory>
using namespace std;
int main()
{
    int n;
    cin >> n;
    vector<double> v(n, 1.5);                    //> Arreglo dinámico que se libera solo
    v.push_back(9.0);                            //> Y crece solo
    unique_ptr<int> p = make_unique<int>(42);    //> Un int dinámico con dueño único
    unique_ptr<int[]> arr = make_unique<int[]>(n);   //> Arreglo dinámico con dueño único
    arr[0] = *p;
    cout << v.size() << " " << *p << " " << arr[0] << "\n";
    return 0;                                    //> Aquí v, p y arr liberan su memoria: sin delete
}
```
:::

## 1.2 Ejemplo resuelto: calificaciones con arreglo dinámico

:::ejemplo | Arreglo de calificaciones del tamaño exacto del grupo | Ejemplo resuelto, Atención dividida
**Problema.** Leer el número de alumnos `n` (cualquier tamaño positivo) y sus calificaciones; mostrar el promedio y cuántos están por encima de él. Usar exactamente la memoria necesaria y liberarla al final.

**A. Algoritmo:** 1) Leer `n` (validar > 0). 2) Reservar un arreglo dinámico de `n` `double`. 3) Leer las calificaciones y sumar. 4) Calcular el promedio y contar las que lo superan (segundo recorrido). 5) Liberar el arreglo.

**B. Pseudocódigo**

```pseudo
Algoritmo CalificacionesDinamicas
    Repetir
        Leer n
    Hasta Que n > 0
    Dimension cal[n]
    suma <- 0
    Para i <- 1 Hasta n Hacer
        Leer cal[i]
        suma <- suma + cal[i]
    FinPara
    prom <- suma / n
    Escribir prom
FinAlgoritmo
```

**C. Código en C++**

```cpp run title="calificaciones_dinamicas.cpp" stdin="0\n5\n8 9.5 6 7 10\n"
#include <iostream>
using namespace std;
int main()
{
    int n;
    do {
        cout << "Numero de alumnos: ";
        cin >> n;
    } while (n <= 0);                         //> 1) Validar
    double* cal = new double[n];              //> 2) Reservar EXACTAMENTE n (en el montón)
    double suma = 0;
    for (int i = 0; i < n; i++)               //> 3) Leer y acumular
    {
        cin >> cal[i];
        suma += cal[i];
    }
    double prom = suma / n;                   //> 4) Promedio y segundo recorrido
    int arriba = 0;
    for (int i = 0; i < n; i++)
        if (cal[i] > prom) arriba++;
    cout << "Promedio: " << prom << ", por encima: " << arriba << "\n";
    delete[] cal;                             //> 5) Liberar: un new[] → un delete[]
    cal = nullptr;
    return 0;
}
```

```diagram mem
regions:
  - name: "Pila de main"
    vars:
      - {name: n, type: int, val: 5}
      - {name: cal, type: "double*", val: "0x7a0", kind: ptr, to: bloque}
      - {name: prom, type: double, val: 8.1}
  - name: "Montón"
    color: "#fdf4ff"
    vars:
      - {name: bloque, type: "double[5]", val: "8 | 9.5 | 6 | 7 | 10", addr: "0x7a0"}
figcaption: "Figura 2. Estado antes de delete[]: el bloque mide exactamente lo que pidió el usuario."
```

**D. Verificación.** (8 + 9.5 + 6 + 7 + 10) / 5 = 8.1; superan el promedio 9.5 y 10 → 2 ✔. El programa tiene un `new[]` y un `delete[]`.
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.16; ranksep=0.3;
@term(m, "Memoria dinámica\n(montón)")
@proc(a, "new T(valor)  →  delete p")
@proc(b, "new T[n]  →  delete[] p")
@proc(c, "tamaño decidido\nen ejecución")
@proc(g, "crecer: nuevo + copiar\n+ delete viejo")
@proc(nd, "nodos: new Nodo{…}\nliberar todos")
@hl(e, "errores: fuga · colgante\ndoble delete · mezclar formas")
@sub(r, "RAII: vector · unique_ptr\n(se liberan solos)")
m -> a; m -> b; b -> c; b -> g; m -> nd; m -> e [style=dashed]; m -> r [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1
| Quiero… | Reservar | Liberar |
|---|---|---|
| Un valor | `T* p = new T(valor);` | `delete p; p = nullptr;` |
| Un arreglo de `n` | `T* a = new T[n];` | `delete[] a; a = nullptr;` |
| Un arreglo en ceros | `T* a = new T[n]();` | `delete[] a;` |
| Una estructura | `Nodo* x = new Nodo{dato, nullptr};` | `delete x;` |
| Una matriz `f × c` | `T** m = new T*[f]; for (i…) m[i] = new T[c];` | `for (i…) delete[] m[i]; delete[] m;` |
| Sin `delete` (recomendado) | `vector<T> v(n);` · `auto p = make_unique<T>(v);` | (automático) |

**Patrón para crecer:** `T* nuevo = new T[cap * 2]; copiar; delete[] viejo; viejo = nuevo; cap *= 2;`
:::

:::checklist | Guía de preguntas de rutina 2.2 · «Por cada new, un delete»
<ul class="checks">
<li>¿Cuento mis <code>new</code> y mis <code>delete</code>? ¿Coinciden en número y forma (<code>new[]</code> ↔ <code>delete[]</code>)?</li>
<li>¿Hay algún camino (un <code>return</code> temprano, un <code>break</code>) que salte el <code>delete</code>?</li>
<li>¿Reasigno un puntero que todavía es el único que conoce un bloque? (Fuga.)</li>
<li>Después de <code>delete</code>, ¿puse el puntero en <code>nullptr</code> y ya no lo uso?</li>
<li>Si una función devuelve memoria dinámica, ¿está claro quién la libera?</li>
<li>¿Podría usar <code>vector</code> o <code>unique_ptr</code> y olvidarme del <code>delete</code>?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) `delete` en lugar de `delete[]`.** Compila (g++ puede avisar), pero es indefinido: `int* a = new int[10]; delete a;` → `delete[] a;`.

**b) Fuga dentro de un ciclo.** Cada vuelta reserva y nunca libera:

```cpp blank title="fuga_ciclo.cpp"
for (int i = 0; i < 1000; i++)
{
    double* temp = new double[500];
    // ... usa temp ...
}           // falta delete[] temp; -> 1000 bloques perdidos
```

**c) Usar un bloque después de liberarlo** (colgante) o liberarlo dos veces: pon el puntero en `nullptr` tras el `delete`.

**d) Liberar memoria que no vino de `new`.** `int x = 5; int* p = &x; delete p;` es indefinido: `x` vive en la pila.

**e) Liberar una lista «de golpe».** `delete cabeza;` libera solo el primer nodo; los demás quedan como fuga. Hay que recorrer guardando el siguiente (concepto 8).
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Copia exacta de un texto | Variabilidad
El mismo patrón (medir → reservar exacto → usar → liberar), ahora con una cadena de C:

```cpp run title="copia_texto.cpp"
#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    const char* original = "Memoria dinamica";
    int n = strlen(original);
    char* copia = new char[n + 1];      //> +1 para el '\0'
    strcpy(copia, original);
    copia[0] = 'm';
    cout << original << " | " << copia << "\n";
    delete[] copia;
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} En cada tarea, dibuja la pila y el montón y verifica «por cada `new`, un `delete`».

:::tarea A | T1. Temperaturas dinámicas: ejemplo y gemelo | 20 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia:**

```cpp run title="temperaturas_dinamicas.cpp" stdin="4\n18.5 22 25.5 20\n"
#include <iostream>
using namespace std;
int main()
{
    int dias;
    cin >> dias;
    double* t = new double[dias];             //> Tantos días como diga el usuario
    double max = -1000;
    for (int i = 0; i < dias; i++)
    {
        cin >> t[i];
        if (t[i] > max) max = t[i];
    }
    cout << "Maxima: " << max << "\nDias con la maxima:";
    for (int i = 0; i < dias; i++)
        if (t[i] == max) cout << " " << i + 1;
    cout << "\n";
    delete[] t;                               //> Liberar
    return 0;
}
```

**Paso 2 · Gemelo.** Lee `n` precios en un arreglo dinámico, aplica un descuento del 15 % a los mayores de $500, muestra los precios finales y el total; libera la memoria.

:::solucion | T1
```cpp run title="precios_dinamicos.cpp" stdin="4\n350 899 120 1500\n"
#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    double* p = new double[n];
    double total = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> p[i];
        if (p[i] > 500) p[i] *= 0.85;
        total += p[i];
    }
    for (int i = 0; i < n; i++) cout << p[i] << " ";
    cout << "\nTotal: " << total << "\n";
    delete[] p;
    return 0;
}
```
:::
:::

:::tarea A | T2. Una función que crea arreglos (completa con pistas) | 20 min | Problema por completar
```cpp blank title="crear_arreglo.cpp"
#include <iostream>
using namespace std;

__1__ crearArreglo(int n, int valor)       // 1: tipo de retorno: direccion de un bloque de int
{
    int* a = __2__;                        // 2: reservar n enteros
    for (int i = 0; i < n; i++)
        a[i] = valor;
    return a;
}

void mostrar(const int* a, int n)
{
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << "\n";
}

int main()
{
    int* unos = crearArreglo(5, 1);
    int* sietes = crearArreglo(3, 7);
    mostrar(unos, 5);
    mostrar(sietes, 3);
    __3__;                                 // 3: liberar unos
    __4__;                                 // 4: liberar sietes
    return 0;
}
```

:::solucion | T2
{{c:1}} `int*` · {{c:2}} `new int[n]` · {{c:3}} `delete[] unos` · {{c:4}} `delete[] sietes`

```cpp run title="crear_arreglo.cpp"
#include <iostream>
using namespace std;

int* crearArreglo(int n, int valor)
{
    int* a = new int[n];
    for (int i = 0; i < n; i++)
        a[i] = valor;
    return a;
}

void mostrar(const int* a, int n)
{
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << "\n";
}

int main()
{
    int* unos = crearArreglo(5, 1);
    int* sietes = crearArreglo(3, 7);
    mostrar(unos, 5);
    mostrar(sietes, 3);
    delete[] unos;
    delete[] sietes;
    return 0;
}
```
:::
:::

:::tarea AB | T3. Agrandar un arreglo (completa sin pistas) | 25 min | Problema por completar, Desvanecimiento de guía
```cpp blank title="agrandar.cpp"
#include <iostream>
using namespace std;

int* agrandar(int* viejo, int n, int nuevoN)
{
    int* nuevo = __1__;
    for (int i = 0; i < __2__; i++)
        nuevo[i] = __3__;
    for (int i = n; i < nuevoN; i++)
        nuevo[i] = 0;
    __4__;
    return __5__;
}

int main()
{
    int n = 3;
    int* a = new int[n]{4, 5, 6};
    a = agrandar(a, n, 6);
    n = 6;
    a[3] = 7;
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << "\n";
    __6__;
    return 0;
}
```

:::solucion | T3
{{c:1}} `new int[nuevoN]` · {{c:2}} `n` · {{c:3}} `viejo[i]` · {{c:4}} `delete[] viejo` · {{c:5}} `nuevo` · {{c:6}} `delete[] a`

```cpp run title="agrandar.cpp"
#include <iostream>
using namespace std;

int* agrandar(int* viejo, int n, int nuevoN)
{
    int* nuevo = new int[nuevoN];
    for (int i = 0; i < n; i++)
        nuevo[i] = viejo[i];
    for (int i = n; i < nuevoN; i++)
        nuevo[i] = 0;
    delete[] viejo;
    return nuevo;
}

int main()
{
    int n = 3;
    int* a = new int[n]{4, 5, 6};
    a = agrandar(a, n, 6);
    n = 6;
    a[3] = 7;
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << "\n";
    delete[] a;
    return 0;
}
```
`a = agrandar(a, …)` no produce fuga porque la función libera el bloque viejo antes de devolver el nuevo.
:::
:::

:::tarea AB | T4. Lista de compras que crece (problema convencional) | 35 min | Variabilidad
**Contexto.** Lee artículos (una palabra cada uno) hasta escribir `fin`. Guárdalos en un arreglo dinámico de `string` que empieza con capacidad 2 y **duplica** su capacidad cuando se llena (informa cada crecimiento). Al final muestra la lista numerada, el número de artículos y la capacidad final; libera la memoria.

:::solucion | T4
```cpp run title="compras.cpp" stdin="leche\npan\nhuevo\nfruta\narroz\nfin\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    int cap = 2, n = 0;
    string* lista = new string[cap];
    string art;
    while (cin >> art && art != "fin")
    {
        if (n == cap)
        {
            string* nuevo = new string[cap * 2];
            for (int i = 0; i < n; i++) nuevo[i] = lista[i];
            delete[] lista;
            lista = nuevo;
            cap *= 2;
            cout << "(capacidad: " << cap << ")\n";
        }
        lista[n++] = art;
    }
    for (int i = 0; i < n; i++) cout << i + 1 << ". " << lista[i] << "\n";
    cout << n << " articulos, capacidad " << cap << "\n";
    delete[] lista;
    return 0;
}
```
:::
:::

:::tarea A | T5. n datos, n decidido en ejecución: ¿de cuántas formas? (solución libre) | 25 min | Solución libre
**Contexto.** Necesitas guardar `n` enteros, con `n` leído del teclado. **Escribe todas las soluciones que conozcas** y compáralas en una tabla (¿es C++ estándar?, ¿hay límite?, ¿quién libera?, ¿puede crecer?): arreglo con tamaño máximo, arreglo de tamaño variable (VLA), `new[]`/`delete[]`, `std::vector`, `std::unique_ptr<int[]>`…

:::solucion | T5
```cpp run title="cinco_formas.cpp" stdin="4\n"
#include <iostream>
#include <vector>
#include <memory>
using namespace std;
int main()
{
    int n;
    cin >> n;
    const int MAX = 100;
    int fijo[MAX];                                  // 1) maximo fijo: estandar, limite 100, se libera solo
    int* din = new int[n];                          // 2) new[]: estandar, sin limite, liberar a mano
    vector<int> v(n);                               // 3) vector: estandar, crece, se libera solo
    unique_ptr<int[]> u = make_unique<int[]>(n);    // 4) unique_ptr: estandar, se libera solo, no crece
    for (int i = 0; i < n; i++) fijo[i] = din[i] = v[i] = u[i] = i * i;
    cout << fijo[n - 1] << " " << din[n - 1] << " " << v[n - 1] << " " << u[n - 1] << "\n";
    delete[] din;
    return 0;
}
```
| Forma | ¿Estándar? | ¿Límite? | ¿Quién libera? | ¿Crece? |
|---|---|---|---|---|
| `int a[MAX]` | sí | sí (MAX) | automático | no |
| `int a[n]` (VLA) | **no** (extensión de g++) | pila pequeña | automático | no |
| `new int[n]` | sí | memoria disponible | tú (`delete[]`) | copiando a mano |
| `vector<int>` | sí | memoria disponible | automático | sí (`push_back`) |
| `unique_ptr<int[]>` | sí | memoria disponible | automático | no |
:::
:::

:::tarea B | T6. Encuentra las fugas (autoexplicación) | 25 min | Autoexplicación, Reversión de la experiencia
**Explica** qué está mal en cada función, qué consecuencia tiene y cómo corregirla.

```cpp blank title="fugas.cpp"
void a()
{
    int* p = new int[50];
    if (p[0] > 10) return;
    delete[] p;
}
void b()
{
    int* q = new int(3);
    int* r = new int(4);
    q = r;
    delete q;
    delete r;
}
void c()
{
    double* m = new double[8];
    delete m;
}
```

{{lineas:5}}

:::solucion | T6
**a:** el `return` temprano salta el `delete[]` → fuga cuando `p[0] > 10` (además `p[0]` no está inicializado). Liberar antes de cada `return` (o usar `vector`). **b:** `q = r` pierde el bloque del 3 (fuga) y luego `delete q` y `delete r` liberan **dos veces** el bloque del 4 (doble liberación). Corrección: `delete q; q = r;` y un solo `delete` final. **c:** `new[]` con `delete` (sin corchetes): comportamiento indefinido → `delete[] m;`.
:::
:::

:::tarea B | T7. Pila y montón, línea por línea (imaginación) | 25 min | Imaginación
**Sin ejecutar**, dibuja la pila y el montón después de cada línea marcada. Al final: ¿cuántos bloques quedan sin liberar? ¿qué imprime?

```cpp check title="imagina_heap.cpp"
#include <iostream>
using namespace std;
int main()
{
    int* a = new int(5);          // (1)
    int* b = new int[3]{1, 2, 3}; // (2)
    int* c = a;                   // (3)
    *c = *c + b[2];               // (4)
    delete a;                     // (5)
    a = new int(*b);              // (6)
    c = nullptr;                  // (7)
    cout << *a << " " << b[1] << "\n";
    delete[] b;
    return 0;
}
```

{{lineas:4}}

:::solucion | T7
(1) bloque X = 5 apuntado por `a`. (2) bloque Y = {1, 2, 3} apuntado por `b`. (3) `c` también apunta a X. (4) X = 5 + 3 = 8. (5) X se libera: `c` queda **colgante**. (6) nuevo bloque Z = `*b` = 1, apuntado por `a`. (7) `c` deja de colgar. Imprime `1 2`. Al final se libera Y, pero **Z nunca se libera**: queda 1 bloque (un `int`) sin liberar.

```cpp run title="imagina_heap.cpp"
#include <iostream>
using namespace std;
int main()
{
    int* a = new int(5);
    int* b = new int[3]{1, 2, 3};
    int* c = a;
    *c = *c + b[2];
    delete a;
    a = new int(*b);
    c = nullptr;
    cout << *a << " " << b[1] << "\n";
    delete[] b;
    return 0;
}
```
:::
:::

:::tarea AB | T8. Cola de turnos de una clínica (reto colaborativo) | 45 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Equipos de 4, niveles mezclados. Una cola: los pacientes **llegan al final** y se **atienden por el frente**. `struct Turno { int numero; string nombre; Turno* sig; };` con punteros `frente` y `final`.
- **Integrante 1:** `void llegar(Turno*& frente, Turno*& final, int num, string nombre)` (crea el nodo con `new` y lo enlaza al final).
- **Integrante 2:** `bool atender(Turno*& frente, Turno*& final)` (muestra y libera el primero con `delete`; cuidado si la cola queda vacía).
- **Integrante 3:** `void mostrar(Turno* frente)` y el menú (`L nombre`, `A`, `M`, `S`).
- **Integrante 4:** al salir, liberar **todos** los turnos pendientes y verificar con un contador que hubo tantos `delete` como `new`.
:::

:::solucion | T8
```cpp run title="cola_turnos.cpp" stdin="L Ana\nL Beto\nL Carla\nA\nM\nL Dario\nA\nS\n"
#include <iostream>
#include <string>
using namespace std;
struct Turno { int numero; string nombre; Turno* sig; };
int creados = 0, liberados = 0;

void llegar(Turno*& frente, Turno*& final, int num, const string& nombre)
{
    Turno* t = new Turno{num, nombre, nullptr};
    creados++;
    if (final == nullptr) frente = final = t;
    else { final->sig = t; final = t; }
}
bool atender(Turno*& frente, Turno*& final)
{
    if (frente == nullptr) return false;
    Turno* t = frente;
    cout << "Atendiendo turno " << t->numero << ": " << t->nombre << "\n";
    frente = frente->sig;
    if (frente == nullptr) final = nullptr;
    delete t;
    liberados++;
    return true;
}
void mostrar(Turno* t)
{
    cout << "En espera:";
    for (; t; t = t->sig) cout << " [" << t->numero << " " << t->nombre << "]";
    cout << "\n";
}
int main()
{
    Turno *frente = nullptr, *final = nullptr;
    int siguiente = 1;
    char op;
    while (cin >> op && op != 'S')
    {
        if (op == 'L') { string n; cin >> n; llegar(frente, final, siguiente++, n); }
        else if (op == 'A') { if (!atender(frente, final)) cout << "No hay pacientes\n"; }
        else if (op == 'M') mostrar(frente);
    }
    while (frente) { Turno* s = frente->sig; delete frente; liberados++; frente = s; }
    cout << "new: " << creados << "  delete: " << liberados << "\n";
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Una matriz dinámica: reservar y liberar en el orden correcto | Modalidad, Ejemplo resuelto
*Guion para narración (≈ 4 min) sobre el diagrama de pila y montón, segmentado para que el estudiante controle el ritmo.*

**Problema:** «Crear una matriz de `f × c` enteros con tamaño leído en ejecución, llenarla con `i * c + j`, mostrarla y liberarla sin fugas».

**Segmento 1 — Dibujar la forma.** {{como}} Dibujo en el montón un arreglo de `f` **punteros** (uno por fila) y, para cada uno, una fila de `c` enteros. En la pila solo queda `int** m`. {{porque}} Una matriz dinámica no es un bloque único: son `f + 1` bloques. Verlo me dice que necesitaré `f + 1` liberaciones.

**Segmento 2 — Reservar de afuera hacia adentro.** {{como}} Primero `m = new int*[f];`, luego en un ciclo `m[i] = new int[c];`. {{porque}} No puedo guardar la dirección de una fila en `m[i]` si el arreglo `m` todavía no existe.

**Segmento 3 — Liberar de adentro hacia afuera.** {{como}} Primero cada fila: `for (i…) delete[] m[i];`, y al final `delete[] m;`. {{porque}} Si liberara primero `m`, perdería las direcciones de las filas: serían `f` fugas. Es el orden inverso al de la reserva, como quitarse la ropa al revés de como uno se vistió.

**Segmento 4 — Contar para verificar.** {{como}} Cuento: hubo `1 + f` llamadas a `new[]` y `f + 1` a `delete[]`. Además compilo con `-fsanitize=address` para que el compilador confirme que no hay fugas. {{porque}} Con memoria dinámica, «funciona» no es suficiente: un programa con fugas también imprime bien.

```cpp run title="matriz_dinamica.cpp" stdin="3 4\n"
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    int f, c;
    cin >> f >> c;
    int** m = new int*[f];                 // arreglo de f punteros a fila
    for (int i = 0; i < f; i++)
        m[i] = new int[c];                 // cada fila: c enteros
    for (int i = 0; i < f; i++)
        for (int j = 0; j < c; j++)
            m[i][j] = i * c + j;
    for (int i = 0; i < f; i++)
    {
        for (int j = 0; j < c; j++) cout << setw(4) << m[i][j];
        cout << "\n";
    }
    for (int i = 0; i < f; i++)
        delete[] m[i];                     // primero las filas
    delete[] m;                            // despues el arreglo de punteros
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. ¿En qué zona de memoria viven las variables locales y en cuál los bloques creados con `new`?
2. ¿Qué devuelve `new int[10]`?
3. ¿Con qué se libera un bloque creado con `new[]`?
4. ¿Qué es una fuga de memoria?
5. ¿Qué es un puntero colgante?
6. Verdadero o falso: un bloque creado con `new` dentro de una función se libera automáticamente al terminar la función.
7. ¿Por qué conviene asignar `nullptr` a un puntero después de `delete`?
8. ¿Cuáles son los cuatro pasos para «agrandar» un arreglo dinámico?
9. ¿En qué orden se liberan las filas y el arreglo de punteros de una matriz dinámica?
10. ¿Qué significa RAII y qué clases de la biblioteca estándar lo aplican?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Analiza la salida** y di cuántos bloques quedan sin liberar:

```cpp check title="p1.cpp"
#include <iostream>
using namespace std;
int* f(int n)
{
    int* a = new int[n];
    for (int i = 0; i < n; i++) a[i] = n - i;
    return a;
}
int main()
{
    int* x = f(3);
    int* y = f(2);
    cout << x[0] + y[1] << "\n";
    x = y;
    delete[] x;
    return 0;
}
```

**P2. Corrige:** `int* v = new int[n]; for (int i = 0; i <= n; i++) v[i] = i; delete v;`

**P3.** Escribe `double* copiaInvertida(const double* a, int n)` que devuelva un **nuevo** arreglo dinámico con los elementos en orden inverso, y el `main` que la use y libere todo.

**P4. Desarrolla** un programa que lea `n` nombres en un arreglo dinámico de `string`, elimine los repetidos creando un **segundo** arreglo dinámico del tamaño justo, muestre ambos y libere toda la memoria.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Distingo pila y montón y sé cuánto vive cada objeto.</li>
<li>Reservo y libero valores y arreglos con la forma correcta (<code>delete</code> / <code>delete[]</code>).</li>
<li>Detecto fugas, punteros colgantes y dobles liberaciones.</li>
<li>Sé cuándo usar <code>vector</code> o <code>unique_ptr</code> en lugar de <code>new</code>.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 Pila; montón · 2 La dirección del primero de 10 enteros reservados en el montón · 3 `delete[]` · 4 Memoria reservada que ya no puede liberarse porque se perdió su dirección · 5 Un puntero que apunta a memoria ya liberada (o que ya no es válida) · 6 Falso: solo el puntero local desaparece; el bloque sigue reservado · 7 Para que no quede colgante: `delete nullptr` no hace nada y `if (p)` detecta que ya no apunta a nada · 8 Reservar uno más grande, copiar los datos, liberar el viejo y apuntar al nuevo · 9 Primero cada fila y después el arreglo de punteros · 10 *Resource Acquisition Is Initialization*: el objeto libera su recurso al destruirse; `vector`, `string`, `unique_ptr`, `shared_ptr`.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** `x = {3, 2, 1}`, `y = {2, 1}`; imprime `3 + 1 = 4`. Después `x = y` pierde el bloque de 3 elementos (fuga) y se libera solo el de `y`: **1 bloque** sin liberar.

```cpp run title="p1.cpp"
#include <iostream>
using namespace std;
int* f(int n)
{
    int* a = new int[n];
    for (int i = 0; i < n; i++) a[i] = n - i;
    return a;
}
int main()
{
    int* x = f(3);
    int* y = f(2);
    cout << x[0] + y[1] << "\n";
    x = y;
    delete[] x;
    return 0;
}
```

**P2.** El ciclo debe ser `i < n` (con `<=` escribe fuera del bloque) y la liberación `delete[] v;`.

**P3.**

```cpp run title="p3.cpp"
#include <iostream>
using namespace std;
double* copiaInvertida(const double* a, int n)
{
    double* r = new double[n];
    for (int i = 0; i < n; i++) r[i] = a[n - 1 - i];
    return r;
}
int main()
{
    double v[4] = {1.5, 2.5, 3.5, 4.5};
    double* inv = copiaInvertida(v, 4);
    for (int i = 0; i < 4; i++) cout << inv[i] << " ";
    cout << "\n";
    delete[] inv;
    return 0;
}
```

**P4.**

```cpp run title="p4.cpp" stdin="6\nAna Luis Ana Eva Luis Mia\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    int n;
    cin >> n;
    string* a = new string[n];
    for (int i = 0; i < n; i++) cin >> a[i];
    int unicos = 0;
    for (int i = 0; i < n; i++)
    {
        bool repetido = false;
        for (int j = 0; j < i; j++) if (a[j] == a[i]) repetido = true;
        if (!repetido) unicos++;
    }
    string* b = new string[unicos];
    int k = 0;
    for (int i = 0; i < n; i++)
    {
        bool repetido = false;
        for (int j = 0; j < i; j++) if (a[j] == a[i]) repetido = true;
        if (!repetido) b[k++] = a[i];
    }
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << "| ";
    for (int i = 0; i < unicos; i++) cout << b[i] << " ";
    cout << "\n";
    delete[] a;
    delete[] b;
    return 0;
}
```
:::
