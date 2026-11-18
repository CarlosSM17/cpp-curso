---
num: "14"
archivo: "Tema14_Punteros"
titulo: "Punteros"
corto: "Punteros"
lema: "Un puntero no es la casa: es la nota donde escribiste su dirección."
duracion: "6 h · 3 sesiones de 2 h"
previos: "Tema 08 (arreglos), Tema 10 (funciones y paso por dirección), Tema 12 (cadenas) y Tema 13 (estructuras y `->`)."
fuentes:
  - "Kernighan, B. W. y Ritchie, D. M. (1988). *The C Programming Language* (2.ª ed.). Prentice Hall. Cap. 5 «Pointers and Arrays»: §5.1 Pointers and Addresses, §5.2 Pointers and Function Arguments, §5.3 Pointers and Arrays, §5.4 Address Arithmetic, §5.5 Character Pointers and Functions. Cap. 6: §6.4 Pointers to Structures, §6.5 Self-referential Structures."
  - "King, K. N. (2008). *C Programming: A Modern Approach* (2.ª ed.). W. W. Norton. Cap. 11 «Pointers». Cap. 12 «Pointers and Arrays». Cap. 17: §17.5 Linked Lists."
  - "Seacord, R. C. (2020). *Effective C*. No Starch Press. Cap. 2 «Objects, Functions, and Types» (tipos puntero)."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §5.4: estudio piloto del modelo CLT4BP sobre punteros (Tablas 5.14 y 5.15; Figura 5.2: analogía de las casas y secuencia declaración → dirección → desreferencia → modificación)."
objetivos:
  A:
    - "Comprender el concepto fundamental de puntero en C."
    - "Identificar la sintaxis correcta para declarar y utilizar punteros."
    - "Explicar la diferencia entre un puntero y una variable regular."
    - "Aplicar los operadores de dirección (`&`) y desreferencia (`*`) correctamente."
    - "Implementar operaciones básicas (asignación, aritmética) y relacionar los punteros con arreglos y funciones."
  B:
    - "Comprender el funcionamiento avanzado de los punteros (aritmética, `->`, `NULL`, `const`)."
    - "Utilizar correctamente la sintaxis de declaración y asignación en casos combinados (incluidos `char *` y `char []`)."
    - "Implementar aritmética de punteros compleja (dos punteros, recorridos)."
    - "Aplicar punteros en la creación y manipulación de estructuras enlazadas."
    - "Implementar funciones que modifiquen variables externas y que devuelvan punteros."
eval_recall: "Opción múltiple sobre conceptos, identificación de sintaxis, asociación de definiciones y cuestionario de operaciones (como en el piloto de la tesis, Tabla 5.14)."
eval_compr: "Resolver problemas simples de implementación, corregir errores, analizar la salida de código y desarrollar un programa pequeño de manipulación de datos."
efectos:
  soporte:
    - ["Modalidad", "El guion del protocolo verbal acompaña a los diagramas de memoria (texto e imágenes con narración, como en el piloto)."]
    - ["Atención dividida", "Integración de texto explicativo con diagramas de memoria en cada paso."]
    - ["Ejemplo resuelto", "Ejemplos paso a paso sobre declaración y uso de punteros (Figura 5.2 de la tesis)."]
    - ["Elementos aislados", "Primero dirección, luego declaración, después desreferencia y, al final, aritmética, funciones, estructuras y cadenas."]
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
    A: "Analogía de las casas; `&`, `*`, `NULL`; punteros y arreglos; paso de punteros a funciones."
    B: "Aritmética con dos punteros, `->`, `const` con punteros, `char *` frente a `char []`, `void *`, listas enlazadas."
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
    B: "Compilación con `-g -fsanitize=address` para detectar accesos inválidos."
plan:
  - ["Sesión 1 · apertura", "Soporte", "Analogía de las casas (atención) y aplicaciones reales (relevancia).", "15 min"]
  - ["Sesión 1 · desarrollo", "Soporte", "Conceptos 1–5 con diagramas de memoria; ejemplo resuelto (Figura 5.2) con narración.", "60 min"]
  - ["Sesión 1 · práctica", "Tareas", "T1; Ruta B: T6.", "45 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–9; T2, T3, T4 con apoyo decreciente del instructor; Ruta B: T7.", "120 min"]
  - ["Sesión 3", "Tareas + evaluación", "T5, T8 colaborativa; protocolo verbal; recall y comprehension test; cuestionarios de carga cognitiva y de percepción.", "120 min"]
glosario:
  - ["puntero / apuntador", "pointer", "Variable que guarda una dirección de memoria."]
  - ["dirección de memoria", "memory address", "Número que identifica una posición de memoria; `printf` la muestra con `%p`."]
  - ["operador dirección", "address-of operator (`&`)", "Obtiene la dirección de una variable: `&x`."]
  - ["desreferenciar", "dereference (`*`)", "Acceder a lo que hay en la dirección guardada: `*p`."]
  - ["puntero nulo", "null pointer (`NULL`)", "Puntero que no apunta a nada."]
  - ["aritmética de punteros", "pointer arithmetic", "Sumar/restar enteros a un puntero para moverse entre elementos."]
  - ["operador flecha", "arrow operator (`->`)", "`p->campo` equivale a `(*p).campo`."]
  - ["puntero a carácter", "pointer to char (`char *`)", "Puntero al primer carácter de un texto; un literal se apunta con `const char *`."]
  - ["puntero colgante", "dangling pointer", "Puntero a memoria que ya no es válida."]
  - ["lista enlazada", "linked list", "Nodos que se conectan entre sí mediante punteros."]
  - ["corrección de const", "const correctness", "Usar `const` para impedir modificaciones no deseadas."]
  - ["puntero genérico", "void pointer (`void *`)", "Puntero sin tipo; no se puede desreferenciar directamente (Tema 15)."]
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
Los punteros son la forma en que C trabaja «cerca de la máquina», y la razón por la que C se usa para escribir sistemas operativos: el núcleo de Linux y los controladores de dispositivos los usan para leer sensores y registros en direcciones fijas, los motores de videojuegos los usan para manejar miles de objetos sin copiarlos, y estructuras como listas, árboles y grafos se construyen enlazando nodos con punteros. Ya los has usado sin nombrarlos: el `&` de `scanf`, los arreglos que se pasan a funciones y el `->` de las estructuras. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | Toda variable tiene una dirección: el operador `&` | Elementos aislados, Atención dividida
Ya lo viste en el Tema 02: una variable tiene nombre, tipo, contenido y **dirección**. El operador `&` («dirección de») la obtiene y `printf` la muestra con `%p`:

```c run title="direcciones.c"
#include <stdio.h>
int main(void)
{
    int numero = 42;
    double precio = 9.5;
    printf("numero vale %d y vive en %p\n", numero, (void *)&numero);   //> `&numero`: la dirección (en hexadecimal)
    printf("precio vale %.1f y vive en %p\n", precio, (void *)&precio); //> `(void *)`: el tipo que `%p` espera
    return 0;
}
```
*Las direcciones cambian en cada ejecución y en cada computadora; lo importante es que existen y son únicas.*
:::

:::concepto | 2 | Declarar un puntero | Elementos aislados, Atención dividida
Un **puntero** es una variable cuyo contenido es una **dirección**. Se declara con `*` entre el tipo al que apuntará y el nombre:

```c run title="declarar.c"
#include <stdio.h>
int main(void)
{
    int numero = 42;
    int *puntero = &numero;        //> `int *`: «puntero a int». Guarda la dirección de numero
    int *vacio = NULL;             //> NULL: el puntero no apunta a nada (todavía)
    printf("puntero guarda %p\n", (void *)puntero);
    printf("&numero es     %p\n", (void *)&numero);    //> Son la misma dirección
    printf("vacio es nulo: %d\n", vacio == NULL);
    return 0;
}
```

```diagram mem
vars:
  - {name: numero, type: int, val: 42, addr: "0x100"}
  - {name: puntero, type: "int *", val: "0x100", addr: "0x108", to: numero, kind: ptr}
  - {name: vacio, type: "int *", val: "NULL", addr: "0x110", kind: ptr}
figcaption: "Figura 1. El contenido de puntero es la dirección de numero (direcciones simplificadas)."
```
El tipo importa: un `int *` solo debe guardar direcciones de `int`; un `double *`, de `double`. Ojo con declarar varios: en `int *p, q;` solo `p` es puntero (`q` es un `int`); por eso se escribe el `*` pegado al nombre.
:::

:::concepto | 3 | Desreferenciar: ir a la casa con `*` | Elementos aislados, Atención dividida
Con `*puntero` («lo apuntado por puntero») se **lee** o **modifica** el contenido de la variable a la que apunta:

```c run title="desreferenciar.c"
#include <stdio.h>
int main(void)
{
    int numero = 42;
    int *puntero = &numero;
    int valor = *puntero;           //> LEER: valor recibe lo que hay en la dirección → 42
    *puntero = 100;                 //> ESCRIBIR: cambia lo que hay en la dirección → numero ahora vale 100
    printf("valor = %d, numero = %d\n", valor, numero);
    return 0;
}
```

:::cuidado | El asterisco tiene dos significados
En una **declaración** (`int *p`), `*` dice «p es un puntero». En una **expresión** (`*p = 5`), `*` dice «ve a la dirección guardada en p». Leer en voz alta ayuda: `int *p` = «p es puntero a int»; `*p` = «lo apuntado por p».
:::
:::

:::concepto | 4 | Puntero vs. variable regular | Elementos aislados
| | Variable regular `int x = 5;` | Puntero `int *p = &x;` |
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

```c run title="punteros_arreglos.c"
#include <stdio.h>
int main(void)
{
    int a[5] = {10, 20, 30, 40, 50};
    int *p = a;                              //> Igual que p = &a[0]
    printf("%d %d %d\n", *p, *(p + 2), p[3]);   //> *(p + i) es lo mismo que p[i] y a[i]
    p++;                                     //> Avanza al siguiente int (4 bytes más adelante)
    printf("Ahora p apunta a %d\n", *p);
    int suma = 0;
    for (int *q = a; q < a + 5; q++)         //> Recorrer con puntero: de a hasta a + 5 (sin incluirlo)
        suma += *q;
    printf("Suma: %d\n", suma);
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
Por eso, al pasar un arreglo a una función, se pasa la **dirección** del primer elemento: la función trabaja sobre el original. En un parámetro, `int a[]` e `int *a` significan lo mismo.
:::

:::concepto | 6 | Punteros y funciones: modificar variables externas | Elementos aislados, Atención dividida
Es lo que hiciste en el Tema 10, ahora con todo su significado: la función recibe **direcciones** y modifica a través de ellas. Compara con la versión que recibe copias:

<div class="cols eq">
<div>

```c run title="con_puntero.c"
#include <stdio.h>
void intercambiar(int *a, int *b)
{
    int aux = *a;
    *a = *b;
    *b = aux;
}
int main(void)
{
    int x = 3, y = 8;
    intercambiar(&x, &y);   // se envian direcciones
    printf("%d %d\n", x, y);
    return 0;
}
```

</div>
<div>

```c run title="con_copias.c"
#include <stdio.h>
void intercambiar(int a, int b)
{
    int aux = a;
    a = b;
    b = aux;
}
int main(void)
{
    int x = 3, y = 8;
    intercambiar(x, y);     // se envian copias
    printf("%d %d\n", x, y);
    return 0;
}
```

</div>
</div>

La versión de la derecha intercambia **sus copias** y `x`, `y` no cambian. Esta es también la razón del `&` en `scanf("%d", &x)`: `scanf` es una función que necesita escribir en tu variable.
:::

:::concepto | 7 | Punteros a estructuras: el operador flecha `->` | Elementos aislados
```c run title="flecha.c"
#include <stdio.h>
typedef struct { char nombre[30]; double precio; int existencias; } Producto;
void rebajar(Producto *p, double pct)        //> Recibe la dirección del producto
{
    p->precio = p->precio * (1 - pct / 100); //> p->precio es (*p).precio
}
int main(void)
{
    Producto mochila = {"Mochila", 600, 5};
    Producto *ptr = &mochila;
    rebajar(ptr, 25);
    printf("%s ahora cuesta $%.2f\n", ptr->nombre, (*ptr).precio);   //> Ambas formas son equivalentes
    return 0;
}
```
Los paréntesis de `(*ptr).precio` son necesarios: el punto tiene más precedencia que el `*`. Por eso existe `->`.
:::

:::concepto | 8 | Punteros y cadenas: `char s[]` frente a `const char *s` | Elementos aislados
Un texto puede guardarse en un **arreglo propio** o señalarse con un **puntero** a un literal. Se parecen, pero no son lo mismo:

```c run title="cadenas_puntero.c"
#include <stdio.h>
int main(void)
{
    char arreglo[] = "Hola";              //> Arreglo propio: una COPIA modificable de 5 bytes
    const char *literal = "Hola";         //> Puntero a un literal: el texto no se debe modificar
    arreglo[0] = 'B';                     //> Válido
    printf("%s %s\n", arreglo, literal);
    printf("%zu %zu\n", sizeof(arreglo), sizeof(literal));   //> 5 (el arreglo) vs 8 (un puntero)
    literal = "Adios";                    //> Un puntero puede apuntar a otro texto…
    printf("%s\n", literal);              //> …un arreglo no se puede reasignar
    return 0;
}
```

| | `char s[] = "Hola";` | `const char *s = "Hola";` |
|---|---|---|
| ¿Qué es? | un arreglo de 5 `char` | un puntero al primer carácter de un literal |
| ¿Se puede modificar el texto? | sí: `s[0] = 'B';` | no (sin `const`, compila pero es comportamiento indefinido) |
| ¿Se puede reasignar? | no: `s = "Adios";` es error | sí: `s = "Adios";` |
| `sizeof(s)` | 5 | 8 (tamaño de un puntero) |
:::

:::concepto | 9 | Ruta B · Los punteros son peligrosos (y cómo protegerse) | Elementos aislados, Reversión de la experiencia
- **Puntero sin inicializar:** `int *p; *p = 5;` escribe en una dirección al azar → comportamiento indefinido. Inicializa siempre (con una dirección o `NULL`).
- **Desreferenciar `NULL`:** el programa se detiene (*segmentation fault*). Verifica: `if (p != NULL) …` (o simplemente `if (p)`).
- **Salirse del arreglo** con aritmética: `*(a + 10)` en un arreglo de 5.
- **Puntero colgante:** devolver la dirección de una variable local que ya no existe.
- **`const`:** `const int *p` → no puedes modificar `*p`; `int *const p` → no puedes cambiar `p`.
- **`void *`:** un puntero «sin tipo» que puede guardar cualquier dirección (lo devuelve `malloc`, Tema 15); para usar el dato hay que convertirlo a un puntero con tipo.

```c run title="const_punteros.c"
#include <stdio.h>
int buscar(const int *datos, int n, int x)     //> const int *: la función promete NO modificar los datos
{
    for (const int *q = datos; q < datos + n; q++)
        if (*q == x) return (int)(q - datos);  //> Restar punteros da la distancia en elementos
    return -1;
}
int main(void)
{
    int v[] = {4, 8, 15, 16, 23, 42};
    int *p = NULL;
    if (p) printf("%d", *p);                   //> Se protege: no se desreferencia un nulo
    printf("15 esta en la posicion %d\n", buscar(v, 6, 15));
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

```c nolines
int numero = 42;
int *puntero;     // declarado, sin inicializar
```

```diagram mem
vars:
  - {name: numero, type: int, val: 42, addr: "0x100"}
  - {name: puntero, type: "int *", val: "?", addr: "0x108", kind: ptr}
```

*`numero` es una variable de tipo entero con el valor 42; `puntero` está declarado pero aún no apunta a nada válido.*

**Paso 2 · El puntero guarda la dirección de numero**

```c nolines
puntero = &numero;
```

```diagram mem
vars:
  - {name: numero, type: int, val: 42, addr: "0x100"}
  - {name: puntero, type: "int *", val: "0x100", addr: "0x108", to: numero, kind: ptr, hl: true}
```

</div>
<div>

**Paso 3 · Desreferencia del puntero**

```c nolines
int valor = *puntero;
```

```diagram mem
vars:
  - {name: numero, type: int, val: 42, addr: "0x100"}
  - {name: puntero, type: "int *", val: "0x100", to: numero, kind: ptr, addr: "0x108"}
  - {name: valor, type: int, val: 42, addr: "0x10c", hl: true}
```

*Se va a la dirección 0x100 y se copia lo que hay ahí (42) en `valor`.*

**Paso 4 · Modificación a través del puntero**

```c nolines
*puntero = 100;
```

```diagram mem
vars:
  - {name: numero, type: int, val: 100, addr: "0x100", hl: true}
  - {name: puntero, type: "int *", val: "0x100", to: numero, kind: ptr, addr: "0x108"}
  - {name: valor, type: int, val: 42, addr: "0x10c"}
```

*Ahora `numero` vale 100; `valor` conserva 42 porque era una copia.*

</div>
</div>

**Programa completo y verificación:**

```c run title="cuatro_pasos.c"
#include <stdio.h>
int main(void)
{
    int numero = 42;                       //> Paso 1
    int *puntero;
    puntero = &numero;                     //> Paso 2: el puntero guarda la dirección de numero
    int valor = *puntero;                  //> Paso 3: desreferencia (lee 42)
    *puntero = 100;                        //> Paso 4: modifica numero a través del puntero
    printf("numero = %d, valor = %d, *puntero = %d\n", numero, valor, *puntero);
    printf("puntero == &numero: %s\n", puntero == &numero ? "si" : "no");
    return 0;
}
```
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.16; ranksep=0.3;
@term(p, "Puntero\nint *p")
@proc(d, "&x: dirección de x")
@proc(s, "*p: lo apuntado\n(leer / escribir)")
@proc(n, "NULL: no apunta\na nada")
@proc(a, "arreglos: p + i\n*(p + i) == p[i]")
@proc(f, "funciones: f(&x)\nmodifica el original")
@proc(e, "estructuras: p->campo")
@sub(r, "cadenas: char s[]\nfrente a const char *s")
@hl(z, "peligros: sin inicializar,\nnulo, fuera de rango, colgante")
p -> d; p -> s; p -> n; p -> a; p -> f; p -> e; p -> r [style=dashed]; p -> z [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1
| Quiero… | Código | Se lee |
|---|---|---|
| Declarar un puntero a `int` | `int *p = NULL;` | «p es puntero a int, nulo» |
| Guardar la dirección de `x` | `p = &x;` | «p recibe la dirección de x» |
| Leer el valor apuntado | `int v = *p;` | «v recibe lo apuntado por p» |
| Modificar el valor apuntado | `*p = 7;` | «lo apuntado por p recibe 7» |
| Mostrar una dirección | `printf("%p", (void *)p);` | |
| Apuntar al primer elemento | `int *q = arreglo;` | |
| Elemento `i` vía puntero | `*(q + i)` o `q[i]` | |
| Avanzar al siguiente elemento | `q++;` | |
| Distancia entre punteros | `q2 - q1` | en elementos |
| Miembro de estructura apuntada | `ps->campo` | `(*ps).campo` |
| Función que modifica `x` | `void f(int *p)` → `f(&x);` | |
| Verificar que no sea nulo | `if (p != NULL)` / `if (p)` | |
| Apuntar a un texto fijo | `const char *s = "Hola";` | |

**Dibuja siempre** las cajas: una para la variable y otra para el puntero, con una flecha desde el puntero hasta la variable.
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿Inicialicé el puntero (con <code>&amp;variable</code>, un arreglo o <code>NULL</code>)?</li>
<li>¿Uso <code>&amp;</code> para obtener una dirección y <code>*</code> para llegar al valor?</li>
<li>¿El tipo del puntero coincide con el tipo de la variable?</li>
<li>Antes de <code>*p</code>, ¿estoy seguro de que <code>p</code> no es <code>NULL</code>?</li>
<li>Con aritmética, ¿me mantengo dentro del arreglo?</li>
<li>¿Dibujé el diagrama de memoria después de cada asignación a un puntero?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Asignar un valor en lugar de una dirección.**

```c err
int main(void)
{
    int x = 5;
    int *p = x;
    return *p;
}
```
*Corrección:* `int *p = &x;` (gcc anterior a la 14 solo advertía, y el programa fallaba al ejecutarse.)

**b) Tipos que no coinciden.**

```c err
int main(void)
{
    double d = 2.5;
    int *p = &d;
    return *p;
}
```
*Corrección:* `double *p = &d;`.

**c) Olvidar el `*` al usar el valor.** `p = p + 1;` mueve el puntero; `*p = *p + 1;` incrementa el valor apuntado.

**d) Precedencia de `*p++`.** `*p++` incrementa el **puntero** (y lee el valor anterior); para incrementar el valor: `(*p)++`.

```c run
#include <stdio.h>
int main(void)
{
    int a[3] = {10, 20, 30};
    int *p = a;
    (*p)++;              //> Incrementa a[0]: 11
    p++;                 //> Avanza p a a[1] (lo mismo que hace *p++, sin leer el valor)
    printf("%d %d\n", a[0], *p);
    return 0;
}
```

**e) Puntero colgante.** Una función no debe devolver la dirección de su variable local: al terminar la función, esa variable deja de existir.

```c warn
int *crear(void)
{
    int local = 7;
    return &local;
}
int main(void)
{
    int *p = crear();
    return p != 0;
}
```
*Corrección:* devolver el valor (`int crear(void)`) o usar memoria dinámica (Tema 15).
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Recorrer un texto con un puntero | Variabilidad
El mismo recorrido con puntero, ahora sobre una cadena (Tema 12):

```c run title="recorre_texto.c"
#include <stdio.h>
int main(void)
{
    const char *texto = "Punteros";      //> Apunta al primer carácter de la cadena
    int n = 0;
    for (const char *c = texto; *c != '\0'; c++)   //> Avanza hasta el tope
    {
        printf("%c.", *c);
        n++;
    }
    printf("\n%d caracteres\n", n);
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

```c run title="min_max.c"
#include <stdio.h>

void minMax(const int *a, int n, int *menor, int *mayor)   //> menor y mayor: direcciones donde escribir
{
    *menor = a[0];                                          //> Se escribe EN la variable de main
    *mayor = a[0];
    for (int i = 1; i < n; i++)
    {
        if (a[i] < *menor) *menor = a[i];
        if (a[i] > *mayor) *mayor = a[i];
    }
}

int main(void)
{
    int datos[] = {17, 4, 29, 11, 8};
    int mn, mx;
    minMax(datos, 5, &mn, &mx);                            //> Se envían las DIRECCIONES de mn y mx
    printf("Menor: %d  Mayor: %d\n", mn, mx);
    return 0;
}
```

**Paso 2 · Gemelo.** Escribe `void dividir(int a, int b, int *cociente, int *residuo)` que entregue el cociente y el residuo de `a / b`, y úsala desde `main` con 47 y 5.

:::solucion | T1
```c run title="dividir.c"
#include <stdio.h>
void dividir(int a, int b, int *cociente, int *residuo)
{
    *cociente = a / b;
    *residuo = a % b;
}
int main(void)
{
    int c, r;
    dividir(47, 5, &c, &r);
    printf("47 = 5 x %d + %d\n", c, r);
    return 0;
}
```
:::
:::

:::tarea A | T2. Recorrer un arreglo con un puntero (completa con pistas) | 25 min | Problema por completar
**Contexto.** Calcular la suma y el máximo de las lecturas de un sensor recorriendo el arreglo **solo con un puntero** (sin índices).

```c blank title="sensor_puntero.c"
#include <stdio.h>
#define N 6
int main(void)
{
    double lecturas[N] = {21.5, 23.0, 22.8, 25.1, 24.4, 20.9};
    double *p = __1__;                       // 1: direccion del primer elemento
    double suma = 0, maximo = __2__;         // 2: el primer valor, a traves de p
    while (p < __3__)                        // 3: direccion "una despues" del ultimo
    {
        suma += __4__;                       // 4: valor apuntado
        if (*p > maximo) maximo = *p;
        __5__;                               // 5: avanzar al siguiente elemento
    }
    printf("Suma: %.1f  Maximo: %.1f\n", suma, maximo);
    return 0;
}
```

:::solucion | T2
{{c:1}} `lecturas` (o `&lecturas[0]`) · {{c:2}} `*p` · {{c:3}} `lecturas + N` · {{c:4}} `*p` · {{c:5}} `p++`

```c run title="sensor_puntero.c"
#include <stdio.h>
#define N 6
int main(void)
{
    double lecturas[N] = {21.5, 23.0, 22.8, 25.1, 24.4, 20.9};
    double *p = lecturas;
    double suma = 0, maximo = *p;
    while (p < lecturas + N)
    {
        suma += *p;
        if (*p > maximo) maximo = *p;
        p++;
    }
    printf("Suma: %.1f  Maximo: %.1f\n", suma, maximo);
    return 0;
}
```
:::
:::

:::tarea AB | T3. Inventario con punteros a estructuras (completa sin pistas) | 25 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Una función recibe un **puntero** a un producto y registra una venta si hay existencias suficientes; otra devuelve un puntero al producto más caro de un arreglo.

```c blank title="inventario_ptr.c"
#include <stdio.h>
#include <stdbool.h>
typedef struct { char nombre[30]; double precio; int existencias; } Producto;

bool vender(__1__ p, int cant)
{
    if (__2__ < cant) return false;
    __3__ -= cant;
    return true;
}

Producto *masCaro(Producto *a, int n)
{
    Producto *mejor = __4__;
    for (int i = 1; i < n; i++)
        if (a[i].precio > __5__) mejor = __6__;
    return mejor;
}

int main(void)
{
    Producto inv[3] = {{"Lapiz", 8, 50}, {"Mochila", 520, 3}, {"Cuaderno", 45, 20}};
    bool v1 = vender(&inv[1], 2);
    bool v2 = vender(&inv[1], 2);
    printf("%d %d\n", v1, v2);
    Producto *c = masCaro(inv, 3);
    printf("%s quedan %d\n", c->nombre, c->existencias);
    return 0;
}
```

:::solucion | T3
{{c:1}} `Producto *` · {{c:2}} `p->existencias` · {{c:3}} `p->existencias` · {{c:4}} `a` (o `&a[0]`) · {{c:5}} `mejor->precio` · {{c:6}} `&a[i]`

```c run title="inventario_ptr.c"
#include <stdio.h>
#include <stdbool.h>
typedef struct { char nombre[30]; double precio; int existencias; } Producto;

bool vender(Producto *p, int cant)
{
    if (p->existencias < cant) return false;
    p->existencias -= cant;
    return true;
}

Producto *masCaro(Producto *a, int n)
{
    Producto *mejor = a;
    for (int i = 1; i < n; i++)
        if (a[i].precio > mejor->precio) mejor = &a[i];
    return mejor;
}

int main(void)
{
    Producto inv[3] = {{"Lapiz", 8, 50}, {"Mochila", 520, 3}, {"Cuaderno", 45, 20}};
    bool v1 = vender(&inv[1], 2);
    bool v2 = vender(&inv[1], 2);
    printf("%d %d\n", v1, v2);
    Producto *c = masCaro(inv, 3);
    printf("%s quedan %d\n", c->nombre, c->existencias);
    return 0;
}
```
La primera venta se realiza (quedan 1) y la segunda se rechaza: por eso se imprime `1 0`. Las dos ventas van en variables separadas porque en C el orden en que se evalúan los argumentos de `printf` no está definido.
:::
:::

:::tarea AB | T4. Invertir con dos punteros (problema convencional) | 30 min | Variabilidad
**Contexto.** Escribe `void invertir(int *ini, int *fin)` que invierta los elementos entre `ini` y `fin` (inclusive) usando **dos punteros** que avanzan uno hacia el otro e intercambian valores. Luego escribe `int *buscar(int *ini, int *fin, int x)` que devuelva un puntero al primer elemento igual a `x` o `NULL` si no está; úsalo para poner en cero el elemento encontrado.

:::solucion | T4
```c run title="dos_punteros.c"
#include <stdio.h>
void invertir(int *ini, int *fin)
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
int *buscar(int *ini, int *fin, int x)
{
    for (int *p = ini; p <= fin; p++)
        if (*p == x) return p;
    return NULL;
}
int main(void)
{
    int a[7] = {1, 2, 3, 4, 5, 6, 7};
    invertir(a, a + 6);
    int *p = buscar(a, a + 6, 4);
    if (p) *p = 0;
    if (buscar(a, a + 6, 99) == NULL) printf("99 no esta\n");
    for (int i = 0; i < 7; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```
:::
:::

:::tarea A | T5. Todas las formas de llegar al tercer elemento (solución libre) | 20 min | Solución libre
**Contexto.** Con `int a[5] = {2, 4, 6, 8, 10};` e `int *p = a;`, escribe **todas las expresiones distintas que puedas** que lean el tercer elemento (6), y también todas las formas que conozcas de **recorrer** el arreglo completo. Verifica cada una en un programa.

:::solucion | T5
```c run title="formas.c"
#include <stdio.h>
int main(void)
{
    int a[5] = {2, 4, 6, 8, 10};
    int *p = a;
    int *q = &a[2];
    printf("%d %d %d %d %d %d %d\n", a[2], *(a + 2), p[2], *(p + 2),
           *q, 2[a], *(&a[0] + 2));                         // 2[a] es valido (y confuso)
    for (int i = 0; i < 5; i++) printf("%d", a[i]);         // indice
    printf(" ");
    for (int *r = a; r != a + 5; r++) printf("%d", *r);     // puntero
    printf(" ");
    int *s = a;
    while (s < a + 5) printf("%d", *s++);                   // *s++: lee y luego avanza
    printf("\n");
    return 0;
}
```
`2[a]` funciona porque `a[i]` significa `*(a + i)`, y la suma es conmutativa.
:::
:::

:::tarea B | T6. Explica a tu compañero (autoexplicación) | 25 min | Autoexplicación, Reversión de la experiencia
**Contexto.** Un compañero escribió este código y obtiene resultados extraños (a veces el programa se cierra). **Explica con tus palabras qué hace cada bloque, cuál es el error y por qué es peligroso**; propone la corrección.

```c blank title="punteros_bug.c"
// Bloque A
int *p;
*p = 10;
// Bloque B
int x = 5;
int *q = &x;
q = q + 1;
printf("%d", *q);
// Bloque C
int *crear(void)
{
    int local = 7;
    return &local;
}
// Bloque D
int *r = NULL;
printf("%d", *r);
```

{{lineas:5}}

:::solucion | T6
**A:** `p` no está inicializado: contiene una dirección al azar y `*p = 10` escribe en memoria ajena (comportamiento indefinido). Corrección: `int y; int *p = &y;`. **B:** `q + 1` apunta **después** de `x`, que no es un arreglo: leer `*q` es inválido. Para cambiar el valor era `*q = *q + 1`. **C:** devuelve la dirección de una variable local que deja de existir al terminar la función: puntero **colgante**. Corrección: devolver el valor (`int crear(void)`) o usar memoria dinámica (Tema 15). **D:** desreferenciar `NULL` detiene el programa; hay que verificar `if (r)` antes.
:::
:::

:::tarea B | T7. Imagina las flechas (imaginación) | 25 min | Imaginación
**Sin ejecutar**, imagina y dibuja el diagrama de memoria (cajas y flechas) **después de cada línea**; luego escribe la salida y compruébala.

```c check title="imagina_punteros.c"
#include <stdio.h>
int main(void)
{
    int a = 1, b = 2;
    int *p = &a;
    int *q = &b;
    *p = *q + 3;
    p = q;
    *p = *p * 10;
    q = &a;
    *q += *p;
    printf("%d %d %d %d\n", a, b, *p, *q);
    return 0;
}
```

{{lineas:4}}

:::solucion | T7
`*p = *q + 3` → `a = 5`. `p = q` → ahora **ambos** apuntan a `b`. `*p = *p * 10` → `b = 20`. `q = &a` → `q` apunta a `a`. `*q += *p` → `a = 5 + 20 = 25`. Final: `p → b`, `q → a`.

```c run title="imagina_punteros.c"
#include <stdio.h>
int main(void)
{
    int a = 1, b = 2;
    int *p = &a;
    int *q = &b;
    *p = *q + 3;
    p = q;
    *p = *p * 10;
    q = &a;
    *q += *p;
    printf("%d %d %d %d\n", a, b, *p, *q);
    return 0;
}
```
:::
:::

:::tarea AB | T8. Una lista enlazada de vagones (reto colaborativo) | 45 min | Memoria colectiva de trabajo, Variabilidad
**Contexto.** Una estructura puede contener un **puntero a otra estructura de su mismo tipo** (Kernighan y Ritchie, §6.5, las llaman estructuras autorreferenciadas). Con eso se construye la **lista enlazada**: cada **nodo** guarda un dato y un puntero al siguiente. Modelen un tren: cada vagón tiene una carga y apunta al vagón siguiente; el último apunta a `NULL`.

:::colab | Organización
Equipos de 4, niveles mezclados.
- **Integrante 1:** `typedef struct Vagon { char carga[20]; int toneladas; struct Vagon *siguiente; } Vagon;` (dentro de la definición todavía no existe el alias `Vagon`, por eso el miembro usa `struct Vagon *`) y crear 4 vagones como variables locales.
- **Integrante 2:** enlazarlos (`v1.siguiente = &v2; …`) y escribir `void recorrer(const Vagon *inicio)` que muestre el tren hasta llegar a `NULL`.
- **Integrante 3:** `int totalToneladas(const Vagon *inicio)` y `Vagon *buscar(Vagon *inicio, const char carga[])`.
- **Integrante 4:** insertar un vagón **en medio** del tren solo cambiando punteros (sin mover los demás) y verificar con `recorrer`.

Dibujen el tren en el pizarrón (cajas y flechas) antes de programar cada paso.
:::

:::solucion | T8
```c run title="tren.c"
#include <stdio.h>
#include <string.h>
typedef struct Vagon { char carga[20]; int toneladas; struct Vagon *siguiente; } Vagon;

void recorrer(const Vagon *v)
{
    while (v != NULL)
    {
        printf("[%s %dt] -> ", v->carga, v->toneladas);
        v = v->siguiente;
    }
    printf("fin\n");
}
int totalToneladas(const Vagon *v)
{
    int t = 0;
    for (; v; v = v->siguiente) t += v->toneladas;
    return t;
}
Vagon *buscar(Vagon *v, const char carga[])
{
    for (; v; v = v->siguiente)
        if (strcmp(v->carga, carga) == 0) return v;
    return NULL;
}
int main(void)
{
    Vagon v4 = {"Granos", 30, NULL};
    Vagon v3 = {"Acero", 50, &v4};
    Vagon v2 = {"Autos", 20, &v3};
    Vagon v1 = {"Carbon", 40, &v2};
    recorrer(&v1);
    Vagon nuevo = {"Madera", 25, NULL};
    Vagon *acero = buscar(&v1, "Acero");
    if (acero)
    {
        nuevo.siguiente = acero->siguiente;   // el nuevo apunta a lo que seguia de Acero
        acero->siguiente = &nuevo;            // Acero ahora apunta al nuevo
    }
    recorrer(&v1);
    printf("Total: %d toneladas\n", totalToneladas(&v1));
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Encontrar el máximo y modificarlo desde fuera | Modalidad, Ejemplo resuelto
*Guion para narración en audio/video (≈ 4 min). Como en el piloto de la tesis, se presenta con los diagramas de memoria en pantalla y se divide en segmentos que el estudiante puede pausar.*

**Problema:** «Una función debe encontrar el mayor puntaje de un arreglo y permitir que `main` lo **reinicie a cero** (el jugador canjeó sus puntos)».

**Segmento 1 — ¿Qué debe devolver?** {{como}} Si la función devolviera el **valor** máximo (`int`), `main` tendría una copia y no podría cambiar el arreglo. Por eso decido devolver **dónde** está: un `int *`. {{porque}} Con la dirección, `main` puede llegar a la casilla original y modificarla.

**Segmento 2 — Recorrer guardando la mejor dirección.** {{como}} Empiezo con `int *mejor = a;` (la dirección del primero) y en el ciclo, si `a[i] > *mejor`, actualizo `mejor = &a[i]`. {{porque}} Comparo **valores** (`*mejor`), pero guardo **direcciones** (`&a[i]`); mezclar ambas cosas es el error más común.

**Segmento 3 — Usar el resultado con cuidado.** {{como}} En `main` escribo `int *p = maximo(puntos, 5); *p = 0;`. Dibujo la flecha de `p` a la casilla del máximo. {{porque}} El diagrama me confirma que `*p = 0` cambia esa casilla y no otra.

**Segmento 4 — El caso borde.** {{como}} Agrego la validación `if (n <= 0) return NULL;` y en `main` verifico `if (p)` antes de usarlo. {{porque}} Un arreglo vacío no tiene máximo; devolver `NULL` y comprobarlo evita desreferenciar una dirección inválida.

```c run title="maximo_ptr.c"
#include <stdio.h>
int *maximo(int *a, int n)
{
    if (n <= 0) return NULL;
    int *mejor = a;
    for (int i = 1; i < n; i++)
        if (a[i] > *mejor) mejor = &a[i];
    return mejor;
}
int main(void)
{
    int puntos[5] = {120, 340, 95, 410, 260};
    int *p = maximo(puntos, 5);
    if (p)
    {
        printf("Maximo %d en la posicion %d\n", *p, (int)(p - puntos));
        *p = 0;
    }
    for (int i = 0; i < 5; i++) printf("%d ", puntos[i]);
    printf("\n");
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo (opción múltiple, sintaxis, asociación y operaciones)
1. Un puntero es una variable que guarda… a) un valor entero · b) una dirección de memoria · c) un arreglo · d) un tipo de dato
2. ¿Cuál declaración es correcta para un puntero a `double`? a) `double p*;` · b) `*double p;` · c) `double *p;` · d) `ptr double p;`
3. Relaciona: (1) `&x` (2) `*p` (3) `NULL` (4) `p->m` — a) puntero que no apunta a nada · b) dirección de x · c) miembro m de la estructura apuntada · d) valor apuntado por p
4. Con `int x = 8; int *p = &x;` ¿qué valen `*p` y `p == &x`?
5. Verdadero o falso: desreferenciar un puntero `NULL` es seguro, porque «no apunta a nada».
6. Si `int a[4]` empieza en `0x100` e `int` ocupa 4 bytes, ¿qué dirección es `a + 3`?
7. ¿A qué equivale `*(a + i)`?
8. ¿Qué diferencia hay entre `(*p)++` y `*p++`?
9. ¿Qué es un puntero colgante?
10. ¿Qué significa `const int *p`? ¿Qué diferencia hay entre `char s[] = "Hola";` y `const char *s = "Hola";`?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Analiza la salida:**

```c check title="p1.c"
#include <stdio.h>
void f(int *a, int b) { *a = *a + b; b = 0; }
int main(void)
{
    int x = 4, y = 6;
    int *p = &y;
    f(&x, *p);
    *p = x * 2;
    printf("%d %d\n", x, y);
    return 0;
}
```

**P2. Corrige** los errores: `int *p; int v[3] = {1, 2, 3}; p = v[0]; for (int i = 0; i <= 3; i++) printf("%d ", p + i);`

**P3. Implementa** `void cuadrados(int *a, int n)` que reemplace cada elemento por su cuadrado, usando solo aritmética de punteros.

**P4. Desarrolla un programa** pequeño de manipulación de datos: un arreglo de 6 temperaturas; una función `double *masFria(double *t, int n)` que devuelva un puntero a la menor; `main` la muestra, la corrige sumándole 1.5 (por un error de calibración) y muestra el arreglo final.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Explico qué es un puntero con la analogía de las casas y las notas.</li>
<li>Uso <code>&amp;</code>, <code>*</code>, <code>NULL</code> y <code>-&gt;</code> correctamente.</li>
<li>Recorro arreglos con punteros y modifico variables externas desde funciones.</li>
<li>Dibujo el diagrama de memoria de un fragmento con punteros.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
*Al cerrar este tema, el instructor puede aplicar la encuesta de carga cognitiva (anexo A.7 de la tesis) y los cuestionarios CIS e IMMS, como en el estudio piloto.*
:::

:::solucion | Evaluación 5.1 (recall)
1 b · 2 c · 3 (1)-b, (2)-d, (3)-a, (4)-c · 4 `*p` = 8 y `p == &x` es verdadero · 5 Falso: desreferenciar `NULL` detiene el programa; hay que verificarlo antes · 6 `0x10c` (0x100 + 3 × 4) · 7 `a[i]` · 8 `(*p)++` incrementa el valor apuntado; `*p++` avanza el puntero al siguiente elemento · 9 Un puntero que apunta a memoria que ya no es válida (por ejemplo, a una variable local que terminó) · 10 Que a través de `p` no se puede modificar el valor apuntado (aunque `p` sí puede apuntar a otra variable); `char s[]` es un arreglo propio y modificable que no se puede reasignar, mientras que `const char *s` es un puntero a un texto fijo que sí puede apuntar a otro texto.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** `f(&x, *p)` recibe la dirección de `x` y una **copia** de `y` (6): `x = 4 + 6 = 10`; `b = 0` no afecta a `y`. Luego `*p = x * 2` → `y = 20`.

```c run title="p1.c"
#include <stdio.h>
void f(int *a, int b) { *a = *a + b; b = 0; }
int main(void)
{
    int x = 4, y = 6;
    int *p = &y;
    f(&x, *p);
    *p = x * 2;
    printf("%d %d\n", x, y);
    return 0;
}
```

**P2.** `p = v;` (o `&v[0]`), no `v[0]`; el ciclo debe ser `i < 3`; para mostrar el valor: `*(p + i)` (no `p + i`, que es una dirección y no corresponde a `%d`).

**P3.** `void cuadrados(int *a, int n) { for (int *p = a; p < a + n; p++) *p = *p * *p; }`

**P4.**

```c run title="p4.c"
#include <stdio.h>
double *masFria(double *t, int n)
{
    double *m = t;
    for (double *p = t + 1; p < t + n; p++)
        if (*p < *m) m = p;
    return m;
}
int main(void)
{
    double temp[6] = {18.5, 16.2, 19.0, 14.8, 17.3, 15.9};
    double *f = masFria(temp, 6);
    printf("Mas fria: %.1f (posicion %d)\n", *f, (int)(f - temp));
    *f += 1.5;
    for (int i = 0; i < 6; i++) printf("%.1f ", temp[i]);
    printf("\n");
    return 0;
}
```
:::
