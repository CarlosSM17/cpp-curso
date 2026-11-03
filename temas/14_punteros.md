---
num: "14"
archivo: "Tema14_Punteros_y_referencias"
titulo: "Punteros y referencias"
corto: "Punteros y referencias"
lema: "Un puntero no es la casa: es la nota donde escribiste su dirección."
duracion: "6 h · 3 sesiones de 2 h"
previos: "Tema 08 (arreglos), Tema 10 (funciones y paso por referencia), Tema 13 (estructuras)."
fuentes:
  - "Lospinoso, J. (2019). *C++ Crash Course*. Cap. 3 «Reference Types»: Pointers (Addressing Variables, Dereferencing Pointers, The Member-of-Pointer Operator, Pointers and Arrays, Pointers Are Dangerous, void Pointers, nullptr), References, Usage of Pointers and References (Forward-Linked Lists, Employing References, const Correctness), auto Type Deduction."
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Cap. 1, §1.2.9 Variables (dirección de memoria con `&`, ejemplo 4 con `char*`); Cap. 8 (paso por referencia)."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §5.4: estudio piloto del modelo CLT4BP sobre punteros (Tablas 5.14 y 5.15; Figura 5.2: analogía de las casas y secuencia declaración → dirección → desreferencia → modificación)."
objetivos:
  A:
    - "Comprender el concepto fundamental de puntero en C++."
    - "Identificar la sintaxis correcta para declarar y utilizar punteros."
    - "Explicar la diferencia entre un puntero y una variable regular."
    - "Aplicar los operadores de dirección (`&`) y desreferencia (`*`) correctamente."
    - "Implementar operaciones básicas (asignación, aritmética) y relacionar los punteros con arreglos y funciones."
  B:
    - "Comprender el funcionamiento avanzado de los punteros (aritmética, `->`, `nullptr`, `const`)."
    - "Utilizar correctamente la sintaxis de declaración y asignación en casos combinados."
    - "Implementar aritmética de punteros compleja (dos punteros, recorridos)."
    - "Aplicar punteros en la creación y manipulación de estructuras enlazadas."
    - "Implementar funciones que modifiquen variables externas con punteros y con referencias."
eval_recall: "Opción múltiple sobre conceptos, identificación de sintaxis, asociación de definiciones y cuestionario de operaciones (como en el piloto de la tesis, Tabla 5.14)."
eval_compr: "Resolver problemas simples de implementación, corregir errores, analizar la salida de código y desarrollar un programa pequeño de manipulación de datos."
efectos:
  soporte:
    - ["Modalidad", "El guion del protocolo verbal acompaña a los diagramas de memoria (texto e imágenes con narración, como en el piloto)."]
    - ["Atención dividida", "Integración de texto explicativo con diagramas de memoria en cada paso."]
    - ["Ejemplo resuelto", "Ejemplos paso a paso sobre declaración y uso de punteros (Figura 5.2 de la tesis)."]
    - ["Elementos aislados", "Primero dirección, luego declaración, después desreferencia y, al final, aritmética, funciones y estructuras."]
  tareas:
    - ["Problema por completar", "Código parcialmente desarrollado para completar (T2, T3)."]
    - ["Elementos aislados", "Introducción progresiva: primero declaración (T1), luego manipulación (T2–T4)."]
    - ["Desvanecimiento de guía", "Reducción gradual del apoyo de T1 a T4."]
    - ["Variabilidad", "Problemas en contextos distintos (división, arreglos, inventario, listas)."]
    - ["Imaginación", "T7, para estudiantes intermedios con conocimientos previos."]
    - ["Solución libre", "T5: todas las formas de acceder a un elemento."]
    - ["Memoria colectiva de trabajo", "T8: lista enlazada por equipos."]
  procedimental:
    - ["Variabilidad", "Múltiples ejemplos con diferentes contextos."]
    - ["Autoexplicación", "Fomentar que los estudiantes expliquen su comprensión (T6)."]
    - ["Autogestión", "Sugerencias para que los estudiantes optimicen sus propios materiales (dibujar su diagrama de memoria)."]
    - ["Desvanecimiento de guía", "La tarjeta de sintaxis se retira en las tareas finales."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Analogía de las casas; `&`, `*`, `nullptr`; punteros y arreglos; paso de punteros a funciones."
    B: "Aritmética con dos punteros, `->`, `const` con punteros, `void*`, listas enlazadas."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 dibujando el diagrama de memoria de cada línea; pares mixtos."
    B: "T5 (variantes), T6, T7 autónomas; arquitectos en T8."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Programa que invierte un arreglo con punteros (T4)."
    B: "Lista enlazada con inserción y recorrido (T8)."
  Entorno:
    comp: "Información procedimental"
    A: "Hoja de diagramas de memoria impresa; depurador mostrando direcciones."
    B: "Compilación con `-fsanitize=address` para detectar accesos inválidos."
plan:
  - ["Sesión 1 · apertura", "Soporte", "Analogía de las casas (atención) y aplicaciones reales (relevancia).", "15 min"]
  - ["Sesión 1 · desarrollo", "Soporte", "Conceptos 1–5 con diagramas de memoria; ejemplo resuelto (Figura 5.2) con narración.", "60 min"]
  - ["Sesión 1 · práctica", "Tareas", "T1; Ruta B: T6.", "45 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–9; T2, T3, T4 con apoyo decreciente del instructor; Ruta B: T7.", "120 min"]
  - ["Sesión 3", "Tareas + evaluación", "T5, T8 colaborativa; protocolo verbal; recall y comprehension test; cuestionarios de carga cognitiva y de percepción.", "120 min"]
glosario:
  - ["puntero / apuntador", "pointer", "Variable que guarda una dirección de memoria."]
  - ["dirección de memoria", "memory address", "Número que identifica una posición de memoria."]
  - ["operador dirección", "address-of operator (`&`)", "Obtiene la dirección de una variable: `&x`."]
  - ["desreferenciar", "dereference (`*`)", "Acceder a lo que hay en la dirección guardada: `*p`."]
  - ["puntero nulo", "null pointer (`nullptr`)", "Puntero que no apunta a nada."]
  - ["aritmética de punteros", "pointer arithmetic", "Sumar/restar enteros a un puntero para moverse entre elementos."]
  - ["operador flecha", "member-of-pointer operator (`->`)", "`p->campo` equivale a `(*p).campo`."]
  - ["referencia", "reference", "Alias de una variable existente (`int& r = x;`)."]
  - ["puntero colgante", "dangling pointer", "Puntero a memoria que ya no es válida."]
  - ["lista enlazada", "linked list", "Nodos que se conectan entre sí mediante punteros."]
  - ["corrección de const", "const correctness", "Usar `const` para impedir modificaciones no deseadas."]
  - ["puntero genérico", "void pointer (`void*`)", "Puntero sin tipo; no se puede desreferenciar directamente."]
---

# 1. Información de soporte {.soporte}

:::analogia | Las casas y la nota con la dirección (tesis, Figura 5.2)
**Imagina las variables como casas, cada una con una dirección única.** Un puntero es como **una nota donde anotas la dirección de una casa específica**. No es la casa en sí, sino simplemente la información sobre **dónde encontrarla**. Con la nota puedes ir a la casa, ver qué hay dentro e incluso cambiar los muebles… sin mudar la casa.

```dot w="78%"
rankdir=LR; nodesep=0.3; ranksep=0.5;
@file(nota, "Nota (puntero)\n«Madero #2»")
@proc(c1, "Casa\nMadero #1")
@hl(c2, "Casa\nMadero #2")
@proc(c3, "Casa\nMadero #3")
nota -> c2 [label=" lleva a", color="#2563eb", fontcolor="#2563eb"];
{rank=same; c1; c2; c3;}
c1 -> c2 -> c3 [style=invis];
```
:::

:::pregunta
Si le das a un amigo **la dirección** de tu casa (y no la casa), **¿qué puede hacer él con esa información?** ¿Qué pasaría si la dirección está mal escrita o la casa ya fue demolida?

{{lineas:2}}
:::

:::relevancia
Los punteros son la forma en que C++ trabaja «cerca de la máquina»: los motores de videojuegos los usan para manejar miles de objetos sin copiarlos, los sistemas operativos y los controladores de Arduino los usan para leer sensores en direcciones fijas, y estructuras como listas, árboles y grafos se construyen enlazando nodos con punteros. Entenderlos también explica **qué ocurre** cuando pasas un arreglo o una referencia a una función. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | Toda variable tiene una dirección: el operador `&` | Elementos aislados, Atención dividida
Ya lo viste en el Tema 02: una variable tiene nombre, tipo, contenido y **dirección**. El operador `&` («dirección de») la obtiene:

```cpp run title="direcciones.cpp"
#include <iostream>
using namespace std;
int main()
{
    int numero = 42;
    double precio = 9.5;
    cout << "numero vale " << numero << " y vive en " << &numero << "\n";   //> `&numero`: la dirección (hexadecimal)
    cout << "precio vale " << precio << " y vive en " << &precio << "\n";
    return 0;
}
```
*Las direcciones cambian en cada ejecución y en cada computadora; lo importante es que existen y son únicas.*
:::

:::concepto | 2 | Declarar un puntero | Elementos aislados, Atención dividida
Un **puntero** es una variable cuyo contenido es una **dirección**. Se declara con `*` después del tipo al que apuntará:

```cpp run title="declarar.cpp"
#include <iostream>
using namespace std;
int main()
{
    int numero = 42;
    int* puntero = &numero;        //> `int*`: «puntero a int». Guarda la dirección de numero
    int* vacio = nullptr;          //> nullptr: el puntero no apunta a nada (todavía)
    cout << "puntero guarda " << puntero << "\n";
    cout << "&numero es     " << &numero << "\n";    //> Son la misma dirección
    cout << "vacio es nulo: " << (vacio == nullptr) << "\n";
    return 0;
}
```

```diagram mem
vars:
  - {name: numero, type: int, val: 42, addr: "0x100"}
  - {name: puntero, type: "int*", val: "0x100", addr: "0x108", to: numero, kind: ptr}
  - {name: vacio, type: "int*", val: "nullptr", addr: "0x110", kind: ptr}
figcaption: "Figura 1. El contenido de puntero es la dirección de numero (direcciones simplificadas)."
```
El tipo importa: un `int*` solo puede guardar direcciones de `int`; un `double*`, de `double`.
:::

:::concepto | 3 | Desreferenciar: ir a la casa con `*` | Elementos aislados, Atención dividida
Con `*puntero` («lo apuntado por puntero») se **lee** o **modifica** el contenido de la variable a la que apunta:

```cpp run title="desreferenciar.cpp"
#include <iostream>
using namespace std;
int main()
{
    int numero = 42;
    int* puntero = &numero;
    int valor = *puntero;           //> LEER: valor recibe lo que hay en la dirección → 42
    *puntero = 100;                 //> ESCRIBIR: cambia lo que hay en la dirección → numero ahora vale 100
    cout << "valor = " << valor << ", numero = " << numero << "\n";
    return 0;
}
```

:::cuidado | El asterisco tiene dos significados
En una **declaración** (`int* p`), `*` dice «p es un puntero». En una **expresión** (`*p = 5`), `*` dice «ve a la dirección guardada en p». Leer en voz alta ayuda: `int* p` = «p es puntero a int»; `*p` = «lo apuntado por p».
:::
:::

:::concepto | 4 | Puntero vs. variable regular | Elementos aislados
| | Variable regular `int x = 5;` | Puntero `int* p = &x;` |
|---|---|---|
| Guarda | un valor (5) | una dirección (la de `x`) |
| `x` / `p` | 5 | la dirección de `x` |
| `&x` / `&p` | dirección de `x` | dirección **del propio puntero** |
| `*p` | — | 5 (el valor de `x`) |
| Tamaño | depende del tipo (`int`: 4 bytes) | igual para todos los punteros (8 bytes en 64 bits) |
| Puede cambiar a… | otro valor | otra dirección (apuntar a otra variable) |
:::

:::movimiento | Notas y casas (10 min)
Cinco estudiantes son «casas»: cada uno tiene en la espalda un número de dirección (100, 104, 108…) y en la mano una hoja con su valor. Otros dos son «punteros»: sostienen una hoja con **una dirección** escrita. El instructor dicta: «`p = &casa2`» (el puntero escribe 108 en su hoja), «`*p = 7`» (el puntero **camina** hasta la casa 108 y cambia su hoja), «`q = p`» (el segundo puntero copia la dirección: ahora dos notas llevan a la misma casa), «`p = &casa4`» (¿cambió la casa 2?). ¿Qué pasa con «`*r = 3`» si `r` nunca recibió una dirección?
:::

:::concepto | 5 | Punteros y arreglos | Elementos aislados, Atención dividida
El nombre de un arreglo se convierte en la **dirección de su primer elemento**. Sumar `1` a un puntero lo mueve **un elemento** (no un byte):

```cpp run title="punteros_arreglos.cpp"
#include <iostream>
using namespace std;
int main()
{
    int a[5] = {10, 20, 30, 40, 50};
    int* p = a;                              //> Igual que p = &a[0]
    cout << *p << " " << *(p + 2) << " " << p[3] << "\n";   //> *(p + i) es lo mismo que p[i] y a[i]
    p++;                                     //> Avanza al siguiente int (4 bytes más adelante)
    cout << "Ahora p apunta a " << *p << "\n";
    int suma = 0;
    for (int* q = a; q < a + 5; q++)         //> Recorrer con puntero: de a hasta a + 5 (sin incluirlo)
        suma += *q;
    cout << "Suma: " << suma << "\n";
    return 0;
}
```

```diagram arr
name: a
type: "int[5]"
vals: [10, 20, 30, 40, 50]
hl: [1]
marks: {0: "a", 1: "p (tras p++)", 2: "p+1"}
addr: "0x200"
step: 4
figcaption: "Figura 2. p + 1 avanza sizeof(int) = 4 bytes: del elemento [1] al [2]."
```
Por eso, al pasar un arreglo a una función, se pasa la **dirección** del primer elemento: la función trabaja sobre el original.
:::

:::concepto | 6 | Punteros y funciones: modificar variables externas | Elementos aislados, Atención dividida
Si una función recibe la **dirección** de una variable, puede modificarla. Compara con la referencia del Tema 10:

<div class="cols eq">
<div>

```cpp run title="con_puntero.cpp"
#include <iostream>
using namespace std;
void intercambiar(int* a, int* b)
{
    int aux = *a;
    *a = *b;
    *b = aux;
}
int main()
{
    int x = 3, y = 8;
    intercambiar(&x, &y);   // se envian direcciones
    cout << x << " " << y << "\n";
    return 0;
}
```

</div>
<div>

```cpp run title="con_referencia.cpp"
#include <iostream>
using namespace std;
void intercambiar(int& a, int& b)
{
    int aux = a;
    a = b;
    b = aux;
}
int main()
{
    int x = 3, y = 8;
    intercambiar(x, y);     // se envian las variables
    cout << x << " " << y << "\n";
    return 0;
}
```

</div>
</div>

Mismo efecto, distinta sintaxis: con punteros se escribe `&` al llamar y `*` dentro; con referencias, nada. El *C++ Crash Course* recomienda **referencias** cuando el parámetro nunca debe ser nulo y **punteros** cuando «no apuntar a nada» (`nullptr`) es una posibilidad válida.
:::

:::concepto | 7 | Punteros a estructuras: el operador flecha `->` | Elementos aislados
```cpp run title="flecha.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Producto { string nombre; double precio; int existencias; };
void rebajar(Producto* p, double pct)        //> Recibe la dirección del producto
{
    p->precio = p->precio * (1 - pct / 100); //> p->precio es (*p).precio
}
int main()
{
    Producto mochila = {"Mochila", 600, 5};
    Producto* ptr = &mochila;
    rebajar(ptr, 25);
    cout << ptr->nombre << " ahora cuesta $" << (*ptr).precio << "\n";   //> Ambas formas son equivalentes
    return 0;
}
```
:::

:::concepto | 8 | Referencias: alias que no se reasignan | Elementos aislados
Una **referencia** es otro nombre para una variable existente. A diferencia de un puntero, **debe** inicializarse, **no** puede ser nula y **no** se puede cambiar para que «apunte» a otra:

```cpp run title="referencias.cpp"
#include <iostream>
using namespace std;
int main()
{
    int original = 10;
    int& alias = original;     //> alias ES original (mismo lugar en memoria)
    alias = 25;                //> Cambia original
    int otro = 99;
    alias = otro;              //> NO reasigna: copia 99 en original
    cout << original << " " << &original << " " << &alias << "\n";   //> Misma dirección
    return 0;
}
```

| | Puntero `int* p` | Referencia `int& r` |
|---|---|---|
| ¿Puede ser nulo? | sí (`nullptr`) | no |
| ¿Se puede cambiar a otra variable? | sí | no |
| ¿Debe inicializarse? | no (pero conviene) | sí |
| Acceso al valor | `*p` | `r` |
:::

:::concepto | 9 | Ruta B · Los punteros son peligrosos (y cómo protegerse) | Elementos aislados, Reversión de la experiencia
El *C++ Crash Course* dedica una sección a sus peligros:

- **Puntero sin inicializar:** `int* p; *p = 5;` escribe en una dirección al azar → comportamiento indefinido. Inicializa siempre (con una dirección o `nullptr`).
- **Desreferenciar `nullptr`:** el programa se detiene. Verifica: `if (p != nullptr) …` (o simplemente `if (p)`).
- **Salirse del arreglo** con aritmética: `*(a + 10)` en un arreglo de 5.
- **Puntero colgante:** devolver la dirección de una variable local que ya no existe.
- **`const`:** `const int* p` → no puedes modificar `*p`; `int* const p` → no puedes cambiar `p`.

```cpp run title="const_punteros.cpp"
#include <iostream>
using namespace std;
int buscar(const int* datos, int n, int x)    //> const int*: la función promete NO modificar los datos
{
    for (const int* q = datos; q < datos + n; q++)
        if (*q == x) return static_cast<int>(q - datos);   //> Restar punteros da la distancia en elementos
    return -1;
}
int main()
{
    int v[] = {4, 8, 15, 16, 23, 42};
    int* p = nullptr;
    if (p) cout << *p;                         //> Se protege: no se desreferencia un nulo
    cout << "15 esta en la posicion " << buscar(v, 6, 15) << "\n";
    return 0;
}
```
:::

## 1.2 Ejemplo resuelto: declaración, dirección, desreferencia y modificación (tesis, Figura 5.2)

:::ejemplo | Cuatro pasos con el mismo puntero | Ejemplo resuelto, Atención dividida, Modalidad
**Problema.** Mostrar, paso a paso, qué ocurre en memoria al declarar un puntero, darle una dirección, leer a través de él y modificar a través de él.

<div class="cols eq">
<div>

**Paso 1 · Declaración de variables**

```cpp nolines
int numero = 42;
int* puntero;     // declarado, sin inicializar
```

```diagram mem
vars:
  - {name: numero, type: int, val: 42, addr: "0x100"}
  - {name: puntero, type: "int*", val: "?", addr: "0x108", kind: ptr}
```

*`numero` es una variable de tipo entero con el valor 42; `puntero` está declarado pero aún no apunta a nada válido.*

**Paso 2 · El puntero guarda la dirección de numero**

```cpp nolines
puntero = &numero;
```

```diagram mem
vars:
  - {name: numero, type: int, val: 42, addr: "0x100"}
  - {name: puntero, type: "int*", val: "0x100", addr: "0x108", to: numero, kind: ptr, hl: true}
```

</div>
<div>

**Paso 3 · Desreferencia del puntero**

```cpp nolines
int valor = *puntero;
```

```diagram mem
vars:
  - {name: numero, type: int, val: 42, addr: "0x100"}
  - {name: puntero, type: "int*", val: "0x100", to: numero, kind: ptr, addr: "0x108"}
  - {name: valor, type: int, val: 42, addr: "0x10c", hl: true}
```

*Se va a la dirección 0x100 y se copia lo que hay ahí (42) en `valor`.*

**Paso 4 · Modificación a través del puntero**

```cpp nolines
*puntero = 100;
```

```diagram mem
vars:
  - {name: numero, type: int, val: 100, addr: "0x100", hl: true}
  - {name: puntero, type: "int*", val: "0x100", to: numero, kind: ptr, addr: "0x108"}
  - {name: valor, type: int, val: 42, addr: "0x10c"}
```

*Ahora `numero` vale 100; `valor` conserva 42 porque era una copia.*

</div>
</div>

**Programa completo y verificación:**

```cpp run title="cuatro_pasos.cpp"
#include <iostream>
using namespace std;
int main()
{
    int numero = 42;                       //> Paso 1
    int* puntero;
    puntero = &numero;                     //> Paso 2: el puntero guarda la dirección de numero
    int valor = *puntero;                  //> Paso 3: desreferencia (lee 42)
    *puntero = 100;                        //> Paso 4: modifica numero a través del puntero
    cout << "numero = " << numero << ", valor = " << valor
         << ", *puntero = " << *puntero << "\n";
    cout << boolalpha << "puntero == &numero: " << (puntero == &numero) << "\n";
    return 0;
}
```
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.16; ranksep=0.3;
@term(p, "Puntero\nint* p")
@proc(d, "&x: dirección de x")
@proc(s, "*p: lo apuntado\n(leer / escribir)")
@proc(n, "nullptr: no apunta\na nada")
@proc(a, "arreglos: p + i\n*(p + i) == p[i]")
@proc(f, "funciones: f(&x)\nmodifica el original")
@proc(e, "estructuras: p->campo")
@sub(r, "referencia int& r:\nalias, no nula")
@hl(z, "peligros: sin inicializar,\nnulo, fuera de rango, colgante")
p -> d; p -> s; p -> n; p -> a; p -> f; p -> e; p -> r [style=dashed]; p -> z [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1
| Quiero… | Código | Se lee |
|---|---|---|
| Declarar un puntero a `int` | `int* p = nullptr;` | «p es puntero a int, nulo» |
| Guardar la dirección de `x` | `p = &x;` | «p recibe la dirección de x» |
| Leer el valor apuntado | `int v = *p;` | «v recibe lo apuntado por p» |
| Modificar el valor apuntado | `*p = 7;` | «lo apuntado por p recibe 7» |
| Apuntar al primer elemento | `int* q = arreglo;` | |
| Elemento `i` vía puntero | `*(q + i)` o `q[i]` | |
| Avanzar al siguiente elemento | `q++;` | |
| Distancia entre punteros | `q2 - q1` | en elementos |
| Miembro de estructura apuntada | `ps->campo` | `(*ps).campo` |
| Función que modifica `x` | `void f(int* p)` → `f(&x);` | |
| Verificar que no sea nulo | `if (p != nullptr)` / `if (p)` | |
| Referencia (alias) | `int& r = x;` | |

**Dibuja siempre** las cajas: una para la variable y otra para el puntero, con una flecha desde el puntero hasta la variable.
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿Inicialicé el puntero (con <code>&amp;variable</code>, un arreglo o <code>nullptr</code>)?</li>
<li>¿Uso <code>&amp;</code> para obtener una dirección y <code>*</code> para llegar al valor?</li>
<li>¿El tipo del puntero coincide con el tipo de la variable?</li>
<li>Antes de <code>*p</code>, ¿estoy seguro de que <code>p</code> no es <code>nullptr</code>?</li>
<li>Con aritmética, ¿me mantengo dentro del arreglo?</li>
<li>¿Dibujé el diagrama de memoria después de cada asignación a un puntero?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Asignar un valor en lugar de una dirección.**

```cpp err
int main()
{
    int x = 5;
    int* p = x;
    return *p;
}
```
*Corrección:* `int* p = &x;`

**b) Tipos que no coinciden.**

```cpp err
int main()
{
    double d = 2.5;
    int* p = &d;
    return 0;
}
```

**c) Olvidar el `*` al usar el valor.** `p = p + 1;` mueve el puntero; `*p = *p + 1;` incrementa el valor apuntado.

**d) Precedencia de `*p++`.** `*p++` incrementa el **puntero** (y lee el valor anterior); para incrementar el valor: `(*p)++`.

```cpp run
#include <iostream>
using namespace std;
int main()
{
    int a[3] = {10, 20, 30};
    int* p = a;
    (*p)++;              //> Incrementa a[0]: 11
    *p++;                //> Avanza p a a[1] (el valor leído se descarta)
    cout << a[0] << " " << *p << "\n";
    return 0;
}
```

**e) Puntero colgante.** Una función no debe devolver la dirección de su variable local (g++ avisa: *address of local variable returned*).
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Recorrer un texto con un puntero | Variabilidad
El mismo recorrido con puntero, ahora sobre una cadena de C (Tema 12):

```cpp run title="recorre_texto.cpp"
#include <iostream>
using namespace std;
int main()
{
    const char* texto = "Punteros";      //> Apunta al primer carácter de la cadena
    int n = 0;
    for (const char* c = texto; *c != '\0'; c++)   //> Avanza hasta el tope
    {
        cout << *c << '.';
        n++;
    }
    cout << "\n" << n << " caracteres\n";
    return 0;
}
```
:::

:::tip | Autogestión: construye tu propio material
Si un ejemplo de internet sobre punteros te confunde, **rediséñalo**: copia el código, dibuja junto a cada línea el diagrama de memoria (cajas y flechas), elimina explicaciones repetidas y resalta con color la línea que cambia la flecha. Es la estrategia que usa este material.
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} {{ef:Elementos aislados}} Primero solo declaración (T1), después manipulación (T2–T4). Dibuja la memoria en cada tarea.

:::tarea A | T1. Funciones que devuelven varios resultados: ejemplo y gemelo | 25 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia** cómo una función entrega dos resultados a través de punteros:

```cpp run title="min_max.cpp"
#include <iostream>
using namespace std;

void minMax(const int* a, int n, int* menor, int* mayor)   //> menor y mayor: direcciones donde escribir
{
    *menor = a[0];                                          //> Se escribe EN la variable de main
    *mayor = a[0];
    for (int i = 1; i < n; i++)
    {
        if (a[i] < *menor) *menor = a[i];
        if (a[i] > *mayor) *mayor = a[i];
    }
}

int main()
{
    int datos[] = {17, 4, 29, 11, 8};
    int mn, mx;
    minMax(datos, 5, &mn, &mx);                            //> Se envían las DIRECCIONES de mn y mx
    cout << "Menor: " << mn << "  Mayor: " << mx << "\n";
    return 0;
}
```

**Paso 2 · Gemelo.** Escribe `void dividir(int a, int b, int* cociente, int* residuo)` que entregue el cociente y el residuo de `a / b`, y úsala desde `main` con 47 y 5.

:::solucion | T1
```cpp run title="dividir.cpp"
#include <iostream>
using namespace std;
void dividir(int a, int b, int* cociente, int* residuo)
{
    *cociente = a / b;
    *residuo = a % b;
}
int main()
{
    int c, r;
    dividir(47, 5, &c, &r);
    cout << "47 = 5 x " << c << " + " << r << "\n";
    return 0;
}
```
:::
:::

:::tarea A | T2. Recorrer un arreglo con un puntero (completa con pistas) | 25 min | Problema por completar
**Contexto.** Calcular la suma y el máximo de las lecturas de un sensor recorriendo el arreglo **solo con un puntero** (sin índices).

```cpp blank title="sensor_puntero.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int N = 6;
    double lecturas[N] = {21.5, 23.0, 22.8, 25.1, 24.4, 20.9};
    double* p = __1__;                       // 1: direccion del primer elemento
    double suma = 0, maximo = __2__;         // 2: el primer valor, a traves de p
    while (p < __3__)                        // 3: direccion "una despues" del ultimo
    {
        suma += __4__;                       // 4: valor apuntado
        if (*p > maximo) maximo = *p;
        __5__;                               // 5: avanzar al siguiente elemento
    }
    cout << "Suma: " << suma << "  Maximo: " << maximo << "\n";
    return 0;
}
```

:::solucion | T2
{{c:1}} `lecturas` (o `&lecturas[0]`) · {{c:2}} `*p` · {{c:3}} `lecturas + N` · {{c:4}} `*p` · {{c:5}} `p++`

```cpp run title="sensor_puntero.cpp"
#include <iostream>
using namespace std;
int main()
{
    const int N = 6;
    double lecturas[N] = {21.5, 23.0, 22.8, 25.1, 24.4, 20.9};
    double* p = lecturas;
    double suma = 0, maximo = *p;
    while (p < lecturas + N)
    {
        suma += *p;
        if (*p > maximo) maximo = *p;
        p++;
    }
    cout << "Suma: " << suma << "  Maximo: " << maximo << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T3. Inventario con punteros a estructuras (completa sin pistas) | 25 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Una función recibe un **puntero** a un producto y registra una venta si hay existencias suficientes; otra devuelve un puntero al producto más caro de un arreglo.

```cpp blank title="inventario_ptr.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Producto { string nombre; double precio; int existencias; };

bool vender(__1__ p, int cant)
{
    if (__2__ < cant) return false;
    __3__ -= cant;
    return true;
}

Producto* masCaro(Producto* a, int n)
{
    Producto* mejor = __4__;
    for (int i = 1; i < n; i++)
        if (a[i].precio > __5__) mejor = __6__;
    return mejor;
}

int main()
{
    Producto inv[3] = {{"Lapiz", 8, 50}, {"Mochila", 520, 3}, {"Cuaderno", 45, 20}};
    cout << vender(&inv[1], 2) << " " << vender(&inv[1], 2) << "\n";
    Producto* c = masCaro(inv, 3);
    cout << c->nombre << " quedan " << c->existencias << "\n";
    return 0;
}
```

:::solucion | T3
{{c:1}} `Producto*` · {{c:2}} `p->existencias` · {{c:3}} `p->existencias` · {{c:4}} `a` (o `&a[0]`) · {{c:5}} `mejor->precio` · {{c:6}} `&a[i]`

```cpp run title="inventario_ptr.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Producto { string nombre; double precio; int existencias; };

bool vender(Producto* p, int cant)
{
    if (p->existencias < cant) return false;
    p->existencias -= cant;
    return true;
}

Producto* masCaro(Producto* a, int n)
{
    Producto* mejor = a;
    for (int i = 1; i < n; i++)
        if (a[i].precio > mejor->precio) mejor = &a[i];
    return mejor;
}

int main()
{
    Producto inv[3] = {{"Lapiz", 8, 50}, {"Mochila", 520, 3}, {"Cuaderno", 45, 20}};
    cout << vender(&inv[1], 2) << " " << vender(&inv[1], 2) << "\n";
    Producto* c = masCaro(inv, 3);
    cout << c->nombre << " quedan " << c->existencias << "\n";
    return 0;
}
```
La primera venta se realiza (quedan 1) y la segunda se rechaza: por eso se imprime `1 0`.
:::
:::

:::tarea AB | T4. Invertir con dos punteros (problema convencional) | 30 min | Variabilidad
**Contexto.** Escribe `void invertir(int* ini, int* fin)` que invierta los elementos entre `ini` y `fin` (inclusive) usando **dos punteros** que avanzan uno hacia el otro e intercambian valores. Luego escribe `int* buscar(int* ini, int* fin, int x)` que devuelva un puntero al primer elemento igual a `x` o `nullptr` si no está; úsalo para poner en cero el elemento encontrado.

:::solucion | T4
```cpp run title="dos_punteros.cpp"
#include <iostream>
using namespace std;
void invertir(int* ini, int* fin)
{
    while (ini < fin)
    {
        int aux = *ini;
        *ini = *fin;
        *fin = aux;
        ini++;
        fin--;
    }
}
int* buscar(int* ini, int* fin, int x)
{
    for (int* p = ini; p <= fin; p++)
        if (*p == x) return p;
    return nullptr;
}
int main()
{
    int a[7] = {1, 2, 3, 4, 5, 6, 7};
    invertir(a, a + 6);
    int* p = buscar(a, a + 6, 4);
    if (p) *p = 0;
    if (buscar(a, a + 6, 99) == nullptr) cout << "99 no esta\n";
    for (int x : a) cout << x << " ";
    cout << "\n";
    return 0;
}
```
:::
:::

:::tarea A | T5. Todas las formas de llegar al tercer elemento (solución libre) | 20 min | Solución libre
**Contexto.** Con `int a[5] = {2, 4, 6, 8, 10};` e `int* p = a;`, escribe **todas las expresiones distintas que puedas** que lean el tercer elemento (6), y también todas las formas que conozcas de **recorrer** el arreglo completo. Verifica cada una en un programa.

:::solucion | T5
```cpp run title="formas.cpp"
#include <iostream>
using namespace std;
int main()
{
    int a[5] = {2, 4, 6, 8, 10};
    int* p = a;
    int* q = &a[2];
    cout << a[2] << " " << *(a + 2) << " " << p[2] << " " << *(p + 2) << " "
         << *q << " " << 2[a] << " " << *(&a[0] + 2) << "\n";   // 2[a] es valido (y confuso)
    for (int i = 0; i < 5; i++) cout << a[i];              // indice
    cout << " ";
    for (int* r = a; r != a + 5; r++) cout << *r;          // puntero
    cout << " ";
    for (int x : a) cout << x;                            // for de rango
    cout << "\n";
    return 0;
}
```
:::
:::

:::tarea B | T6. Explica a tu compañero (autoexplicación) | 25 min | Autoexplicación, Reversión de la experiencia
**Contexto.** Un compañero escribió este código y obtiene resultados extraños (a veces el programa se cierra). **Explica con tus palabras qué hace cada bloque, cuál es el error y por qué es peligroso**; propone la corrección.

```cpp blank title="punteros_bug.cpp"
// Bloque A
int* p;
*p = 10;
// Bloque B
int x = 5;
int* q = &x;
q = q + 1;
cout << *q;
// Bloque C
int* crear()
{
    int local = 7;
    return &local;
}
// Bloque D
int* r = nullptr;
cout << *r;
```

{{lineas:5}}

:::solucion | T6
**A:** `p` no está inicializado: contiene una dirección al azar y `*p = 10` escribe en memoria ajena (comportamiento indefinido). Corrección: `int y; int* p = &y;`. **B:** `q + 1` apunta **después** de `x`, que no es un arreglo: leer `*q` es inválido. Para cambiar el valor era `*q = *q + 1`. **C:** devuelve la dirección de una variable local que deja de existir al terminar la función: puntero **colgante**. Corrección: devolver el valor (`int crear()`) o usar memoria dinámica (Tema 15). **D:** desreferenciar `nullptr` detiene el programa; hay que verificar `if (r)` antes.
:::
:::

:::tarea B | T7. Imagina las flechas (imaginación) | 25 min | Imaginación
**Sin ejecutar**, imagina y dibuja el diagrama de memoria (cajas y flechas) **después de cada línea**; luego escribe la salida y compruébala.

```cpp check title="imagina_punteros.cpp"
#include <iostream>
using namespace std;
int main()
{
    int a = 1, b = 2;
    int* p = &a;
    int* q = &b;
    *p = *q + 3;
    p = q;
    *p = *p * 10;
    q = &a;
    *q += *p;
    cout << a << " " << b << " " << *p << " " << *q << "\n";
    return 0;
}
```

{{lineas:4}}

:::solucion | T7
`*p = *q + 3` → `a = 5`. `p = q` → ahora **ambos** apuntan a `b`. `*p = *p * 10` → `b = 20`. `q = &a` → `q` apunta a `a`. `*q += *p` → `a = 5 + 20 = 25`. Final: `p → b`, `q → a`.

```cpp run title="imagina_punteros.cpp"
#include <iostream>
using namespace std;
int main()
{
    int a = 1, b = 2;
    int* p = &a;
    int* q = &b;
    *p = *q + 3;
    p = q;
    *p = *p * 10;
    q = &a;
    *q += *p;
    cout << a << " " << b << " " << *p << " " << *q << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T8. Una lista enlazada de vagones (reto colaborativo) | 45 min | Memoria colectiva de trabajo, Variabilidad
**Contexto.** El *C++ Crash Course* (cap. 3) presenta la **lista enlazada** como la estructura canónica basada en punteros: cada **nodo** guarda un dato y un puntero al siguiente. Modelen un tren: cada vagón tiene una carga y apunta al vagón siguiente; el último apunta a `nullptr`.

:::colab | Organización
Equipos de 4, niveles mezclados.
- **Integrante 1:** `struct Vagon { string carga; int toneladas; Vagon* siguiente; };` y crear 4 vagones como variables locales.
- **Integrante 2:** enlazarlos (`v1.siguiente = &v2; …`) y escribir `void recorrer(Vagon* inicio)` que muestre el tren hasta llegar a `nullptr`.
- **Integrante 3:** `int totalToneladas(Vagon* inicio)` y `Vagon* buscar(Vagon* inicio, string carga)`.
- **Integrante 4:** insertar un vagón **en medio** del tren solo cambiando punteros (sin mover los demás) y verificar con `recorrer`.

Dibujen el tren en el pizarrón (cajas y flechas) antes de programar cada paso.
:::

:::solucion | T8
```cpp run title="tren.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Vagon { string carga; int toneladas; Vagon* siguiente; };

void recorrer(Vagon* v)
{
    while (v != nullptr)
    {
        cout << "[" << v->carga << " " << v->toneladas << "t] -> ";
        v = v->siguiente;
    }
    cout << "fin\n";
}
int totalToneladas(Vagon* v)
{
    int t = 0;
    for (; v; v = v->siguiente) t += v->toneladas;
    return t;
}
Vagon* buscar(Vagon* v, const string& carga)
{
    for (; v; v = v->siguiente)
        if (v->carga == carga) return v;
    return nullptr;
}
int main()
{
    Vagon v4 = {"Granos", 30, nullptr};
    Vagon v3 = {"Acero", 50, &v4};
    Vagon v2 = {"Autos", 20, &v3};
    Vagon v1 = {"Carbon", 40, &v2};
    recorrer(&v1);
    Vagon nuevo = {"Madera", 25, nullptr};
    Vagon* acero = buscar(&v1, "Acero");
    if (acero)
    {
        nuevo.siguiente = acero->siguiente;   // el nuevo apunta a lo que seguia de Acero
        acero->siguiente = &nuevo;            // Acero ahora apunta al nuevo
    }
    recorrer(&v1);
    cout << "Total: " << totalToneladas(&v1) << " toneladas\n";
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Encontrar el máximo y modificarlo desde fuera | Modalidad, Ejemplo resuelto
*Guion para narración en audio/video (≈ 4 min). Como en el piloto de la tesis, se presenta con los diagramas de memoria en pantalla y se divide en segmentos que el estudiante puede pausar.*

**Problema:** «Una función debe encontrar el mayor puntaje de un arreglo y permitir que `main` lo **reinicie a cero** (el jugador canjeó sus puntos)».

**Segmento 1 — ¿Qué debe devolver?** {{como}} Si la función devolviera el **valor** máximo (`int`), `main` tendría una copia y no podría cambiar el arreglo. Por eso decido devolver **dónde** está: un `int*`. {{porque}} Con la dirección, `main` puede llegar a la casilla original y modificarla.

**Segmento 2 — Recorrer guardando la mejor dirección.** {{como}} Empiezo con `int* mejor = a;` (la dirección del primero) y en el ciclo, si `a[i] > *mejor`, actualizo `mejor = &a[i]`. {{porque}} Comparo **valores** (`*mejor`), pero guardo **direcciones** (`&a[i]`); mezclar ambas cosas es el error más común.

**Segmento 3 — Usar el resultado con cuidado.** {{como}} En `main` escribo `int* p = maximo(puntos, 5); *p = 0;`. Dibujo la flecha de `p` a la casilla del máximo. {{porque}} El diagrama me confirma que `*p = 0` cambia esa casilla y no otra.

**Segmento 4 — El caso borde.** {{como}} Agrego la validación `if (n <= 0) return nullptr;` y en `main` verifico `if (p)` antes de usarlo. {{porque}} Un arreglo vacío no tiene máximo; devolver `nullptr` y comprobarlo evita desreferenciar una dirección inválida.

```cpp run title="maximo_ptr.cpp"
#include <iostream>
using namespace std;
int* maximo(int* a, int n)
{
    if (n <= 0) return nullptr;
    int* mejor = a;
    for (int i = 1; i < n; i++)
        if (a[i] > *mejor) mejor = &a[i];
    return mejor;
}
int main()
{
    int puntos[5] = {120, 340, 95, 410, 260};
    int* p = maximo(puntos, 5);
    if (p)
    {
        cout << "Maximo " << *p << " en la posicion " << p - puntos << "\n";
        *p = 0;
    }
    for (int x : puntos) cout << x << " ";
    cout << "\n";
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo (opción múltiple, sintaxis, asociación y operaciones)
1. Un puntero es una variable que guarda… a) un valor entero · b) una dirección de memoria · c) un arreglo · d) un tipo de dato
2. ¿Cuál declaración es correcta para un puntero a `double`? a) `double p*;` · b) `*double p;` · c) `double* p;` · d) `ptr double p;`
3. Relaciona: (1) `&x` (2) `*p` (3) `nullptr` (4) `p->m` — a) puntero que no apunta a nada · b) dirección de x · c) miembro m de la estructura apuntada · d) valor apuntado por p
4. Con `int x = 8; int* p = &x;` ¿qué valen `*p` y `p == &x`?
5. Verdadero o falso: un puntero y una referencia pueden ser nulos.
6. Si `int a[4]` empieza en `0x100` e `int` ocupa 4 bytes, ¿qué dirección es `a + 3`?
7. ¿A qué equivale `*(a + i)`?
8. ¿Qué diferencia hay entre `(*p)++` y `*p++`?
9. ¿Qué es un puntero colgante?
10. ¿Qué significa `const int* p`?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Analiza la salida:**

```cpp check title="p1.cpp"
#include <iostream>
using namespace std;
void f(int* a, int b) { *a = *a + b; b = 0; }
int main()
{
    int x = 4, y = 6;
    int* p = &y;
    f(&x, *p);
    *p = x * 2;
    cout << x << " " << y << "\n";
    return 0;
}
```

**P2. Corrige** los errores: `int* p; int v[3] = {1, 2, 3}; p = v[0]; for (int i = 0; i <= 3; i++) cout << p + i;`

**P3. Implementa** `void cuadrados(int* a, int n)` que reemplace cada elemento por su cuadrado, usando solo aritmética de punteros.

**P4. Desarrolla un programa** pequeño de manipulación de datos: un arreglo de 6 temperaturas; una función `double* masFria(double* t, int n)` que devuelva un puntero a la menor; `main` la muestra, la corrige sumándole 1.5 (por un error de calibración) y muestra el arreglo final.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Explico qué es un puntero con la analogía de las casas y las notas.</li>
<li>Uso <code>&amp;</code>, <code>*</code>, <code>nullptr</code> y <code>-&gt;</code> correctamente.</li>
<li>Recorro arreglos con punteros y modifico variables externas desde funciones.</li>
<li>Dibujo el diagrama de memoria de un fragmento con punteros.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
*Al cerrar este tema, el instructor puede aplicar la encuesta de carga cognitiva (anexo A.7 de la tesis) y los cuestionarios CIS e IMMS, como en el estudio piloto.*
:::

:::solucion | Evaluación 5.1 (recall)
1 b · 2 c · 3 (1)-b, (2)-d, (3)-a, (4)-c · 4 `*p` = 8 y `p == &x` es verdadero · 5 Falso: solo un puntero puede ser nulo · 6 `0x10c` (0x100 + 3 × 4) · 7 `a[i]` · 8 `(*p)++` incrementa el valor apuntado; `*p++` avanza el puntero al siguiente elemento · 9 Un puntero que apunta a memoria que ya no es válida (por ejemplo, a una variable local que terminó) · 10 Que a través de `p` no se puede modificar el valor apuntado (aunque `p` sí puede apuntar a otra variable).
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** `f(&x, *p)` recibe la dirección de `x` y una **copia** de `y` (6): `x = 4 + 6 = 10`; `b = 0` no afecta a `y`. Luego `*p = x * 2` → `y = 20`.

```cpp run title="p1.cpp"
#include <iostream>
using namespace std;
void f(int* a, int b) { *a = *a + b; b = 0; }
int main()
{
    int x = 4, y = 6;
    int* p = &y;
    f(&x, *p);
    *p = x * 2;
    cout << x << " " << y << "\n";
    return 0;
}
```

**P2.** `p = v;` (o `&v[0]`), no `v[0]`; el ciclo debe ser `i < 3`; para mostrar el valor: `*(p + i)` (no `p + i`, que es una dirección).

**P3.** `void cuadrados(int* a, int n) { for (int* p = a; p < a + n; p++) *p = *p * *p; }`

**P4.**

```cpp run title="p4.cpp"
#include <iostream>
using namespace std;
double* masFria(double* t, int n)
{
    double* m = t;
    for (double* p = t + 1; p < t + n; p++)
        if (*p < *m) m = p;
    return m;
}
int main()
{
    double temp[6] = {18.5, 16.2, 19.0, 14.8, 17.3, 15.9};
    double* f = masFria(temp, 6);
    cout << "Mas fria: " << *f << " (posicion " << f - temp << ")\n";
    *f += 1.5;
    for (double x : temp) cout << x << " ";
    cout << "\n";
    return 0;
}
```
:::
