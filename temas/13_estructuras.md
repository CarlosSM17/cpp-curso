---
num: "13"
archivo: "Tema13_Registros_estructuras_enumeraciones"
titulo: "Registros o estructuras (struct) y enumeraciones"
corto: "Estructuras (struct)"
lema: "Datos que viajan juntos deben guardarse juntos: un solo nombre para todos los campos de un objeto real."
duracion: "5 h · 3 sesiones"
previos: "Tema 08 (arreglos), Tema 10 (funciones y paso por dirección) y Tema 12 (cadenas)."
fuentes:
  - "Kernighan, B. W. y Ritchie, D. M. (1988). *The C Programming Language* (2.ª ed.). Prentice Hall. Cap. 6 «Structures»: §6.1 Basics of Structures, §6.2 Structures and Functions, §6.3 Arrays of Structures, §6.4 Pointers to Structures, §6.7 Typedef."
  - "King, K. N. (2008). *C Programming: A Modern Approach* (2.ª ed.). W. W. Norton. Cap. 16 «Structures, Unions, and Enumerations»: §16.1 Structure Variables, §16.2 Structure Types, §16.3 Nested Arrays and Structures, §16.5 Enumerations."
  - "Seacord, R. C. (2020). *Effective C*. No Starch Press. Cap. 2 «Objects, Functions, and Types» (estructuras y tipos derivados)."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §5.4 y Figura 5.3: material del estudio piloto sobre estructuras anidadas (Empleado con fecha de contrato)."
objetivos:
  A:
    - "Definir estructuras (`struct`) que agrupen datos relacionados de distintos tipos."
    - "Declarar e inicializar variables de tipo estructura y acceder a sus miembros con el operador punto."
    - "Definir y usar estructuras anidadas (una estructura como miembro de otra)."
    - "Manejar arreglos de estructuras para registrar colecciones (alumnos, productos, contactos)."
  B:
    - "Pasar estructuras a funciones por valor y por dirección (`Tipo *p` y el operador `->`) y devolverlas como resultado."
    - "Usar `enum` para miembros con un conjunto fijo de valores."
    - "Ordenar y buscar en arreglos de estructuras por uno de sus campos."
    - "Usar `typedef` e inicializadores designados (`.campo = valor`, C99)."
efectos:
  soporte:
    - ["Elementos aislados", "Necesidad → definición → typedef e inicialización → operaciones completas → anidadas → arreglos de estructuras → funciones y `->` → enum (como en el piloto: primero declaración, luego manipulación)."]
    - ["Atención dividida", "Diagrama del registro que se llena paso a paso junto al código (como la Figura 5.3 de la tesis)."]
    - ["Ejemplo resuelto", "Empleado con fecha de contrato: definición, declaración, acceso y modificación paso a paso."]
    - ["Movimiento humano", "«Fichas humanas»: equipos de estudiantes forman un registro; cada uno es un campo."]
  procedimental:
    - ["Variabilidad", "Estructuras para productos, libros, contactos, equipos y fechas."]
    - ["Autoexplicación", "Errores típicos con estructuras planteados como «¿por qué no compila?»."]
  tareas:
    - ["Ejemplo resuelto", "T1: producto de inventario + gemelo (libro)."]
    - ["Problema por completar", "T2 (arreglo de alumnos, con pistas) y T3 (fechas válidas, sin pistas)."]
    - ["Desvanecimiento de guía", "T1 → T4."]
    - ["Solución libre", "T5: diseñar todas las estructuras de una app de música."]
    - ["Autoexplicación", "T6: errores comunes con struct."]
    - ["Imaginación", "T7: imaginar copias y modificaciones de estructuras anidadas."]
    - ["Memoria colectiva de trabajo", "T8: tabla de posiciones de un torneo."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Definir, declarar, acceder, anidar y hacer arreglos de estructuras."
    B: "Estructuras en funciones con punteros y `->`, `enum` como miembro, ordenamiento por campo, inicializadores designados."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 con diagramas de registros en papel."
    B: "T5, T6, T7 autónomas; T8 como diseñadores de la estructura."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Agenda de contactos con menú (T4)."
    B: "Diseño documentado de estructuras (T5) y tabla del torneo (T8)."
  Entorno:
    comp: "Información procedimental"
    A: "Depurador mostrando los miembros de cada variable."
    B: "Documentación de `typedef` e inicializadores designados (C99)."
plan:
  - ["Sesión 1", "Soporte + tareas", "Fichas humanas; conceptos 1–5; ejemplo resuelto (anidadas); T1, T2.", "100 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–8; T3, T4; Ruta B: T6, T7.", "100 min"]
  - ["Sesión 3", "Tareas + evaluación", "T5, T8 torneo; protocolo verbal; tests.", "100 min"]
glosario:
  - ["registro / estructura", "struct / record", "Tipo definido por el programador que agrupa datos (miembros) de distintos tipos."]
  - ["miembro / campo", "member / field", "Cada dato dentro de una estructura."]
  - ["operador punto", "member access operator (`.`)", "Accede a un miembro: `alumno.nombre`."]
  - ["operador flecha", "arrow operator (`->`)", "Accede a un miembro a través de un puntero: `p->nombre` equivale a `(*p).nombre`."]
  - ["estructura anidada", "nested struct", "Estructura que tiene como miembro a otra estructura."]
  - ["arreglo de estructuras", "array of structs", "Colección de registros del mismo tipo."]
  - ["tipo definido por el usuario", "user-defined type", "Tipo creado con `struct`, `union` o `enum`."]
  - ["alias de tipo", "typedef", "Da un nombre nuevo a un tipo: `typedef struct {…} Alumno;`."]
  - ["enumeración", "enumeration (`enum`)", "Tipo con un conjunto fijo de constantes enteras con nombre: `MAGO`."]
  - ["inicialización con llaves", "brace initialization", "Inicializar una estructura con valores en orden: `{1, \"Ana\"}`."]
  - ["inicializador designado", "designated initializer", "Inicializa miembros por nombre: `{.edad = 17}` (C99)."]
---

# 1. Información de soporte {.soporte}

:::analogia | La ficha de inscripción
En la escuela, cada alumno tiene una **ficha**: nombre, número de control, fecha de nacimiento, promedio. Nadie guarda los nombres en un cajón, las fechas en otro y los promedios en un tercero: la ficha mantiene **juntos** todos los datos de **una** persona. Una **estructura** (`struct`) es el formato de esa ficha; cada variable de ese tipo es una ficha llena.
:::

:::pregunta
Con lo que sabes, para 30 alumnos usarías un arreglo de nombres, otro de promedios y otro de edades. **¿Qué tendrías que hacer para ordenar a los alumnos por promedio sin que se mezclen los datos de unos con otros?**

{{lineas:2}}
:::

:::relevancia
Un personaje de videojuego (nombre, vida, posición, inventario), un producto de una tienda en línea (código, precio, existencias), un punto en 3D (x, y, z), un mensaje de chat (autor, hora, texto): los programas reales modelan **objetos** con varios datos. En C, las estructuras son la herramienta principal de modelado: los sistemas operativos describen cada archivo y cada proceso con un `struct`, y son la base de los tipos abstractos de datos de la programación modular (Tema 17). {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | El problema de los arreglos paralelos | Elementos aislados
```c check title="paralelos.c"
#include <stdio.h>
int main(void)
{
    const char *nombre[3] = {"Ana", "Luis", "Eva"};
    double promedio[3] = {8.7, 9.4, 7.9};
    int edad[3] = {16, 17, 16};
    // Para ordenar por promedio hay que intercambiar en LOS TRES arreglos a la vez;
    // si olvidas uno, los datos de una persona se mezclan con los de otra.
    printf("%s %.1f %d\n", nombre[1], promedio[1], edad[1]);
    return 0;
}
```
Los datos de «Luis» están dispersos en tres arreglos unidos solo por el índice 1. Una estructura los **agrupa**.
:::

:::concepto | 2 | Definir una estructura | Elementos aislados, Atención dividida
```c run title="definir.c"
#include <stdio.h>
#include <string.h>

struct Alumno                  //> Define un TIPO nuevo: struct Alumno (el «formato de la ficha»)
{
    char nombre[30];           //> Miembros: pueden ser de tipos distintos
    int edad;
    double promedio;
};                             //> ¡La definición termina con punto y coma!

int main(void)
{
    struct Alumno a;           //> Una VARIABLE de tipo struct Alumno (una ficha concreta)
    strcpy(a.nombre, "Luis");  //> Operador punto: variable.miembro (el texto, con strcpy)
    a.edad = 17;
    a.promedio = 9.4;
    printf("%s (%d): %.1f\n", a.nombre, a.edad, a.promedio);
    return 0;
}
```

```diagram struct
var: a
type: "struct Alumno"
fields:
  - {name: nombre, val: '"Luis"'}
  - {name: edad, val: 17}
  - {name: promedio, val: 9.4}
figcaption: "Figura 1. Una variable de tipo struct Alumno: tres miembros guardados juntos."
```
En C, el nombre completo del tipo es `struct Alumno` (con la palabra `struct`). Por convención, el nombre del tipo empieza con **mayúscula** y el de la variable con minúscula.
:::

:::concepto | 3 | `typedef` e inicialización con llaves | Elementos aislados
Escribir `struct` cada vez es largo: `typedef` le da al tipo un nombre corto. Al declarar, la estructura se puede **inicializar con llaves** en el orden de sus miembros, o por **nombre** de miembro (inicializadores designados, C99):

```c run title="inicializar.c" stdin="Eva Rios\n16 7.9\n"
#include <stdio.h>

typedef struct                         //> typedef: desde aquí el tipo se llama simplemente Alumno
{
    char nombre[30];
    int edad;
    double promedio;
} Alumno;

int main(void)
{
    Alumno a = {"Ana", 16, 8.7};                        //> Llaves: valores en el ORDEN de los miembros
    Alumno c = {.promedio = 9.1, .nombre = "Iker"};     //> Designados: por nombre; lo que falta queda en 0
    Alumno b = {0};                                     //> Todos los miembros en cero
    scanf(" %29[^\n]", b.nombre);                       //> Cada miembro se lee como una variable normal
    scanf("%d %lf", &b.edad, &b.promedio);              //> `&b.edad`: la dirección de ESE miembro
    printf("%s | %s %d | %s %d %.1f\n", a.nombre, c.nombre, c.edad, b.nombre, b.edad, b.promedio);
    return 0;
}
```
:::

:::concepto | 4 | Operaciones con la estructura completa | Elementos aislados, Atención dividida
Esto es lo que se puede hacer con el registro **completo**:

| Operación | ¿Se puede? | Ejemplo |
|---|---|---|
| Asignar (copiar todos los miembros) | ✔ | `b = a;` |
| Pasar como parámetro | ✔ | `mostrar(a);` |
| Devolver desde una función | ✔ | `Alumno crear(void);` |
| Comparar con `==` | ✘ (error de compilación) | compara miembro por miembro |
| Mostrar con un solo `printf` | ✘ | escribe una función `mostrar` |

```c run title="copia.c"
#include <stdio.h>
#include <stdbool.h>
typedef struct { int x, y; } Punto;
int main(void)
{
    Punto p = {2, 5};
    Punto q = p;                   //> Copia COMPLETA: q es independiente de p
    q.x = 10;                      //> Cambiar q no afecta a p
    printf("p = (%d, %d)  q = (%d, %d)\n", p.x, p.y, q.x, q.y);
    bool iguales = (p.x == q.x && p.y == q.y);   //> Comparar: miembro por miembro
    printf("iguales: %s\n", iguales ? "si" : "no");
    return 0;
}
```
Curiosidad: aunque un arreglo **suelto** no se puede asignar (Tema 08), un arreglo **dentro** de una estructura sí se copia completo con `b = a;`.
:::

:::movimiento | Fichas humanas (10 min)
Equipos de 3: cada estudiante es un **miembro** de una estructura `Alumno` (uno sostiene «nombre», otro «edad», otro «promedio») y entre los tres son **una variable**. El instructor dicta: «`b = a;`» (el equipo b copia en sus hojas los valores del equipo a), «`b.edad = 18;`» (¿cambió el equipo a?), «crea un arreglo de 3 alumnos» (tres equipos en fila: `grupo[0]`, `grupo[1]`, `grupo[2]`), «`grupo[1].nombre`» (¿quién responde?).
:::

:::concepto | 5 | Estructuras anidadas | Elementos aislados, Atención dividida
Un miembro puede ser **otra estructura**. Para llegar al dato interior se encadenan puntos:

```c run title="anidada.c"
#include <stdio.h>
typedef struct { int dia, mes, anio; } Fecha;
typedef struct
{
    int id;
    char nombre[40];
    Fecha contrato;               //> Miembro de tipo Fecha: estructura anidada
} Empleado;
int main(void)
{
    Empleado e = {101, "Ana Lopez", {15, 3, 2023}};   //> Llaves dentro de llaves
    printf("%s contratada el %d/%d/%d\n", e.nombre,
           e.contrato.dia, e.contrato.mes, e.contrato.anio);   //> Dos puntos: e → contrato → dia
    e.contrato.anio = 2024;                           //> Se modifica igual
    printf("Nuevo anio: %d\n", e.contrato.anio);
    return 0;
}
```
:::

:::concepto | 6 | Arreglos de estructuras | Elementos aislados, Atención dividida
Un arreglo cuyos elementos son estructuras: `grupo[i].miembro`.

```c run title="arreglo_struct.c"
#include <stdio.h>
#define N 4
typedef struct { char nombre[20]; double promedio; } Alumno;
int main(void)
{
    Alumno grupo[N] = {{"Ana", 8.7}, {"Luis", 9.4}, {"Eva", 7.9}, {"Iker", 9.1}};
    int mejor = 0;
    double suma = 0;
    for (int i = 0; i < N; i++)
    {
        suma += grupo[i].promedio;                    //> Índice del arreglo, luego punto del miembro
        if (grupo[i].promedio > grupo[mejor].promedio) mejor = i;
    }
    printf("Promedio del grupo: %.2f\n", suma / N);
    printf("Mejor: %s (%.1f)\n", grupo[mejor].nombre, grupo[mejor].promedio);
    return 0;
}
```

```diagram arr
name: grupo
type: "Alumno[4]"
vals: ["Ana 8.7", "Luis 9.4", "Eva 7.9", "Iker 9.1"]
hl: [1]
cw: 86
figcaption: "Figura 2. Cada casilla del arreglo guarda un registro completo; grupo[1].nombre es «Luis»."
```
:::

:::concepto | 7 | Estructuras y funciones: el operador flecha `->` | Elementos aislados, Atención dividida
Pasar una estructura **por valor** copia todos sus miembros. Para que una función la **modifique** (o para no copiar una estructura grande) se pasa su **dirección**, como en el Tema 10. Dentro de la función, `p->miembro` significa «el miembro de la estructura a la que apunta `p`» (es lo mismo que `(*p).miembro`):

```c run title="struct_funciones.c"
#include <stdio.h>
#include <string.h>
typedef struct { char nombre[30]; double precio; int existencias; } Producto;

void mostrar(const Producto *p)                 //> Puntero a const: sin copia y sin poder modificar
{
    printf("%s $%.2f (%d)\n", p->nombre, p->precio, p->existencias);   //> `->`: miembro a través de un puntero
}
void vender(Producto *p, int cantidad)          //> Puntero: la venta debe modificar el original
{
    if (cantidad <= p->existencias) p->existencias -= cantidad;
}
Producto crear(const char nombre[], double precio)   //> Devuelve una estructura completa
{
    Producto p = {"", precio, 0};
    strcpy(p.nombre, nombre);
    return p;
}
int main(void)
{
    Producto lapiz = crear("Lapiz", 8.5);
    lapiz.existencias = 40;
    vender(&lapiz, 12);                         //> Se envía la dirección
    mostrar(&lapiz);
    return 0;
}
```
:::

:::concepto | 8 | Ruta B · `enum` como miembro y estructuras que se describen solas | Elementos aislados, Reversión de la experiencia
Una enumeración (Tema 05) es ideal para un miembro con valores fijos; combinada con inicializadores designados, el código se lee casi como una ficha:

```c run title="enum_struct.c"
#include <stdio.h>
enum clase { GUERRERO, MAGO, ARQUERO };            //> Solo tres valores posibles
typedef struct { char nombre[20]; enum clase clase; int nivel; } Personaje;

const char *nombreClase(enum clase c)              //> Devuelve un texto fijo según el valor
{
    switch (c)
    {
        case GUERRERO: return "Guerrero";
        case MAGO:     return "Mago";
        case ARQUERO:  return "Arquero";
    }
    return "?";
}

int main(void)
{
    Personaje p = {.nombre = "Lyra", .clase = MAGO, .nivel = 7};    //> Cada valor dice a qué miembro va
    printf("%s es %s de nivel %d\n", p.nombre, nombreClase(p.clase), p.nivel);
    return 0;
}
```
Si mañana agregas `SANADOR` al `enum` y olvidas su `case`, `gcc -Wall` te lo avisa.
:::

## 1.2 Ejemplo resuelto: el empleado y su fecha de contrato (tesis, Figura 5.3)

:::ejemplo | Estructura anidada paso a paso | Ejemplo resuelto, Atención dividida
**Problema.** Registrar a un empleado con su identificador, su nombre y su fecha de contrato, y mostrar sus datos. (Es el material que se usó con estudiantes novatos en el estudio piloto del modelo CLT4BP.)

**Explicación paso a paso**

1. Primero definimos una estructura llamada `Fecha` con los campos `dia`, `mes` y `anio`.
2. Después definimos la estructura `Empleado` con los campos `id` y `nombre`.
3. Dentro de `Empleado` agregamos el campo `contrato`, de tipo `Fecha`.
4. Declaramos la variable `empleado1` (sus campos aún sin valor).
5. Llenamos `id` y `nombre` (este con `strcpy`, porque es texto); luego, con doble punto, los campos de la fecha.

<div class="cols eq">
<div>

```diagram struct
var: "Empleado empleado1;"
fields:
  - {name: id, val: "?"}
  - {name: nombre, val: '"?"'}
  - name: contrato
    type: Fecha
    fields:
      - {name: dia, val: "?"}
      - {name: mes, val: "?"}
      - {name: anio, val: "?"}
```

```diagram struct
var: "empleado1.id = 101; .nombre = ..."
fields:
  - {name: id, val: 101, hl: true}
  - {name: nombre, val: '"Ana Lopez"', hl: true}
  - name: contrato
    type: Fecha
    fields:
      - {name: dia, val: "?"}
      - {name: mes, val: "?"}
      - {name: anio, val: "?"}
```

```diagram struct
var: "empleado1.contrato.dia = 15; ..."
fields:
  - {name: id, val: 101}
  - {name: nombre, val: '"Ana Lopez"'}
  - name: contrato
    type: Fecha
    fields:
      - {name: dia, val: 15, hl: true}
      - {name: mes, val: 3, hl: true}
      - {name: anio, val: 2023, hl: true}
```

</div>
<div>

```c run title="empleado.c"
#include <stdio.h>
#include <string.h>

typedef struct               //> Paso 1
{
    int dia;
    int mes;
    int anio;
} Fecha;

typedef struct               //> Paso 2
{
    int id;
    char nombre[40];
    Fecha contrato;          //> Paso 3: anidada
} Empleado;

int main(void)
{
    Empleado empleado1;                    //> Paso 4
    empleado1.id = 101;                    //> Paso 5
    strcpy(empleado1.nombre, "Ana Lopez");
    empleado1.contrato.dia = 15;
    empleado1.contrato.mes = 3;
    empleado1.contrato.anio = 2023;
    printf("%d - %s - %d/%d/%d\n",
           empleado1.id,
           empleado1.nombre,
           empleado1.contrato.dia,
           empleado1.contrato.mes,
           empleado1.contrato.anio);
    return 0;
}
```

</div>
</div>

**Verificación.** Cada diagrama corresponde a un bloque del código: declaración (sin valores), asignación de los campos simples y asignación de los campos anidados con doble punto.
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.16; ranksep=0.3;
@term(s, "typedef struct { miembros } Tipo;")
@proc(v, "variable: Tipo x;\ninicializar {…} o {.campo = …}")
@proc(p, "x.miembro\n(operador punto)")
@proc(o, "asignar · pasar · devolver\n(no ==, no printf directo)")
@proc(n, "anidada:\nx.fecha.dia")
@proc(a, "arreglo:\ngrupo[i].miembro")
@sub(f, "funciones: por valor\no Tipo *p → p->miembro")
@hl(e, "enum como miembro")
s -> v -> p; v -> o; s -> n; s -> a; o -> f; s -> e [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1
```c run title="plantilla_struct.c"
#include <stdio.h>
#define MAX 50

typedef struct { int dia, mes, anio; } Fecha;  // 1) definir (antes de main y de las funciones)
typedef struct
{
    char nombre[40];
    char telefono[15];
    Fecha cumple;                              // 2) anidar
} Contacto;

void mostrar(const Contacto *c)                // 3) funcion que solo lee: puntero a const
{
    printf("%s %s %d/%d\n", c->nombre, c->telefono, c->cumple.dia, c->cumple.mes);
}

int main(void)
{
    Contacto c1 = {"Ana", "4491234567", {12, 5, 2008}};   // 4) inicializar
    Contacto agenda[MAX];                                 // 5) arreglo de estructuras
    int n = 0;
    agenda[n++] = c1;                                     // 6) asignar registro completo
    for (int i = 0; i < n; i++) mostrar(&agenda[i]);
    return 0;
}
```

| Quiero… | Escribo |
|---|---|
| Acceder a un miembro | `variable.miembro` |
| Miembro de una anidada | `variable.anidada.miembro` |
| Miembro de un elemento del arreglo | `arreglo[i].miembro` |
| Miembro a través de un puntero | `p->miembro` (= `(*p).miembro`) |
| Guardar texto en un miembro | `strcpy(a.nombre, "Ana");` |
| Intercambiar dos registros | `Tipo aux = a[i]; a[i] = a[j]; a[j] = aux;` |
| Comparar dos registros | `a.x == b.x && a.y == b.y` (miembro a miembro) |
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿La definición del <code>struct</code> termina en <code>};</code> (o en <code>} Tipo;</code> con <code>typedef</code>) y está antes de donde se usa?</li>
<li>¿Uso <code>struct Alumno</code> o definí el alias con <code>typedef</code>?</li>
<li>¿Distingo el <b>tipo</b> (<code>Alumno</code>) de la <b>variable</b> (<code>a</code>)? Los puntos van en la variable.</li>
<li>En un arreglo, ¿puse el índice antes del punto: <code>grupo[i].nombre</code>?</li>
<li>¿Los miembros de texto se copian con <code>strcpy</code> (no con <code>=</code>)?</li>
<li>¿La función debe modificar el registro? Parámetro <code>Tipo *p</code>, <code>p-&gt;miembro</code> y llamada con <code>&amp;</code>.</li>
<li>Al ordenar, ¿intercambio el registro <b>completo</b> (no solo el campo de la comparación)?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Olvidar el `;` al final de la definición.**

```c err
struct Libro
{
    char titulo[50];
    int paginas;
}
int main(void)
{
    struct Libro l;
    return 0;
}
```

**b) Usar el nombre corto sin `typedef`.** Si se definió `struct Alumno { … };`, el tipo se llama `struct Alumno`:

```c err
#include <stdio.h>
struct Alumno { char nombre[30]; int edad; };
int main(void)
{
    Alumno a = {"Ana", 16};
    printf("%s\n", a.nombre);
    return 0;
}
```
*Corrección:* `struct Alumno a = …;` o definir `typedef struct { … } Alumno;`.

**c) Usar el tipo como si fuera una variable.** `Alumno.edad = 16;` no tiene sentido: primero hay que declarar una variable `Alumno a;` y usar `a.edad`.

**d) Comparar estructuras completas con `==`.**

```c err
typedef struct { int x, y; } Punto;
int main(void)
{
    Punto p = {1, 2}, q = {1, 2};
    if (p == q) return 1;
    return 0;
}
```
*Corrección:* `p.x == q.x && p.y == q.y`, o una función `bool iguales(Punto a, Punto b)`.

**e) Olvidar el índice del arreglo.** `grupo.nombre` no existe; es `grupo[i].nombre`.

**f) Modificar una copia.** `void subirNivel(Personaje p) { p.nivel++; }` no cambia al personaje original: usa `void subirNivel(Personaje *p) { p->nivel++; }` y llama con `subirNivel(&pj);`.

**g) Asignar texto a un miembro con `=`.** `a.nombre = "Ana";` no compila (es un arreglo, Tema 12): `strcpy(a.nombre, "Ana");`.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Inventario de una tienda | Variabilidad
```c run title="inventario.c"
#include <stdio.h>
typedef struct { int codigo; char nombre[30]; double precio; int existencias; } Producto;
int main(void)
{
    Producto inv[] = {{101, "Cuaderno", 45, 30}, {102, "Pluma", 12, 120}, {103, "Mochila", 520, 4}};
    int n = sizeof(inv) / sizeof(inv[0]);                //> Número de registros (Tema 08)
    double valorTotal = 0;
    for (int i = 0; i < n; i++)
    {
        double valor = inv[i].precio * inv[i].existencias;
        valorTotal += valor;
        printf("%d %s: $%.2f%s\n", inv[i].codigo, inv[i].nombre, valor,
               inv[i].existencias < 5 ? "  (surtir!)" : "");
    }
    printf("Valor del inventario: $%.2f\n", valorTotal);
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Antes de programar, dibuja la estructura como una ficha con sus campos.

:::tarea A | T1. Ficha de producto: ejemplo y gemelo | 20 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia:**

```c run title="producto.c" stdin="205\nAudifonos gamer\n899.50 7\n"
#include <stdio.h>

typedef struct                      //> El «formato» de la ficha
{
    int codigo;
    char nombre[40];
    double precio;
    int existencias;
} Producto;

int main(void)
{
    Producto p;                     //> Una ficha concreta
    scanf("%d", &p.codigo);
    scanf(" %39[^\n]", p.nombre);   //> Texto con espacios (Tema 02); el arreglo no lleva &
    scanf("%lf %d", &p.precio, &p.existencias);
    printf("[%d] %s\n", p.codigo, p.nombre);
    printf("Precio: $%.2f  Existencias: %d\n", p.precio, p.existencias);
    printf("Valor en almacen: $%.2f\n", p.precio * p.existencias);   //> Los miembros se usan en expresiones
    return 0;
}
```

**Paso 2 · Gemelo.** Define una estructura `Libro` con ISBN (texto), título, autor, año y precio; lee un libro y muestra su ficha y cuántos años tiene de publicado (respecto a 2026).

:::solucion | T1
```c run title="libro.c" stdin="978-607-1\nRayuela\nJulio Cortazar\n1963 320\n"
#include <stdio.h>
typedef struct { char isbn[20], titulo[60], autor[40]; int anio; double precio; } Libro;
int main(void)
{
    Libro l;
    scanf(" %19[^\n]", l.isbn);
    scanf(" %59[^\n]", l.titulo);
    scanf(" %39[^\n]", l.autor);
    scanf("%d %lf", &l.anio, &l.precio);
    printf("%s (%s, %d)\nISBN %s | $%.2f | %d anios de publicado\n",
           l.titulo, l.autor, l.anio, l.isbn, l.precio, 2026 - l.anio);
    return 0;
}
```
:::
:::

:::tarea A | T2. Lista de alumnos (completa con pistas) | 25 min | Problema por completar
**Contexto.** Registrar `n` alumnos (nombre y tres calificaciones), calcular el promedio de cada uno y mostrar al de mejor promedio.

```c blank title="lista_alumnos.c"
#include <stdio.h>
typedef struct
{
    char nombre[30];
    double cal[3];                       // un arreglo como miembro
    double promedio;
} Alumno __1__                           // 1: fin de la definicion
int main(void)
{
    Alumno grupo[30];
    int n, mejor = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%29s", __2__);            // 2: nombre del alumno i (es un arreglo: sin &)
        double s = 0;
        for (int k = 0; k < 3; k++)
        {
            scanf("%lf", __3__);         // 3: direccion de la calificacion k del alumno i
            s += grupo[i].cal[k];
        }
        grupo[i].promedio = __4__;       // 4: promedio
        if (grupo[i].promedio > __5__)   // 5: promedio del mejor hasta ahora
            mejor = i;
    }
    printf("Mejor: %s %.2f\n", grupo[mejor].nombre, grupo[mejor].promedio);
    return 0;
}
```

:::solucion | T2
{{c:1}} `;` · {{c:2}} `grupo[i].nombre` · {{c:3}} `&grupo[i].cal[k]` · {{c:4}} `s / 3` · {{c:5}} `grupo[mejor].promedio`

```c run title="lista_alumnos.c" stdin="3\nAna 9 8 10\nLuis 7 9 8\nEva 10 9 9.5\n"
#include <stdio.h>
typedef struct
{
    char nombre[30];
    double cal[3];
    double promedio;
} Alumno;
int main(void)
{
    Alumno grupo[30];
    int n, mejor = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%29s", grupo[i].nombre);
        double s = 0;
        for (int k = 0; k < 3; k++)
        {
            scanf("%lf", &grupo[i].cal[k]);
            s += grupo[i].cal[k];
        }
        grupo[i].promedio = s / 3;
        if (grupo[i].promedio > grupo[mejor].promedio)
            mejor = i;
    }
    printf("Mejor: %s %.2f\n", grupo[mejor].nombre, grupo[mejor].promedio);
    return 0;
}
```
:::
:::

:::tarea AB | T3. ¿Fecha válida? ¿Cuál es anterior? (completa sin pistas) | 25 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Una agenda necesita validar fechas y saber cuál de dos es anterior. Reutiliza la lógica de días del mes (Tema 05). Una `Fecha` es pequeña, así que se pasa por valor.

```c blank title="fechas.c"
#include <stdio.h>
#include <stdbool.h>
typedef struct { int dia, mes, anio; } Fecha;

bool bisiesto(int a) { return (a % 4 == 0 && a % 100 != 0) || a % 400 == 0; }

int diasDelMes(int m, int a)
{
    if (m == 2) return __1__;
    if (m == 4 || m == 6 || m == 9 || m == 11) return 30;
    return 31;
}

bool esValida(Fecha f)
{
    return f.mes >= 1 && f.mes <= 12 && __2__ && __3__;
}

bool esAnterior(Fecha a, Fecha b)
{
    if (a.anio != b.anio) return __4__;
    if (a.mes != b.mes) return __5__;
    return __6__;
}

int main(void)
{
    Fecha x, y;
    scanf("%d %d %d %d %d %d", &x.dia, &x.mes, &x.anio, &y.dia, &y.mes, &y.anio);
    printf("x valida: %d, y valida: %d\n", esValida(x), esValida(y));
    printf("x anterior a y: %d\n", esAnterior(x, y));
    return 0;
}
```

:::solucion | T3
{{c:1}} `bisiesto(a) ? 29 : 28` · {{c:2}} `f.dia >= 1` · {{c:3}} `f.dia <= diasDelMes(f.mes, f.anio)` · {{c:4}} `a.anio < b.anio` · {{c:5}} `a.mes < b.mes` · {{c:6}} `a.dia < b.dia`

```c run title="fechas.c" runs="29 2 2024 1 3 2024|29 2 2023 15 8 2022"
#include <stdio.h>
#include <stdbool.h>
typedef struct { int dia, mes, anio; } Fecha;

bool bisiesto(int a) { return (a % 4 == 0 && a % 100 != 0) || a % 400 == 0; }

int diasDelMes(int m, int a)
{
    if (m == 2) return bisiesto(a) ? 29 : 28;
    if (m == 4 || m == 6 || m == 9 || m == 11) return 30;
    return 31;
}

bool esValida(Fecha f)
{
    return f.mes >= 1 && f.mes <= 12 && f.dia >= 1 && f.dia <= diasDelMes(f.mes, f.anio);
}

bool esAnterior(Fecha a, Fecha b)
{
    if (a.anio != b.anio) return a.anio < b.anio;
    if (a.mes != b.mes) return a.mes < b.mes;
    return a.dia < b.dia;
}

int main(void)
{
    Fecha x, y;
    scanf("%d %d %d %d %d %d", &x.dia, &x.mes, &x.anio, &y.dia, &y.mes, &y.anio);
    printf("x valida: %d, y valida: %d\n", esValida(x), esValida(y));
    printf("x anterior a y: %d\n", esAnterior(x, y));
    return 0;
}
```
`esValida` aprovecha el cortocircuito: si el mes es inválido, nunca se llama a `diasDelMes` con él.
:::
:::

:::tarea AB | T4. Agenda de contactos (problema convencional) | 40 min | Variabilidad
**Contexto.** Programa una agenda con un arreglo de hasta 50 contactos (`nombre`, `telefono`, `correo`, `cumple` de tipo `Fecha`) y un menú: **1** agregar, **2** buscar por nombre (mostrar todos los que **contengan** el texto buscado), **3** listar todos, **4** cumpleañeros de un mes dado, **5** salir. Usa una función por opción.

:::solucion | T4
```c run title="agenda.c" stdin="1\nAna Lopez\n4491112233 ana@mail.com 12 5\n1\nLuis Ana Perez\n4494445566 luis@mail.com 3 9\n2\nAna\n4\n9\n3\n5\n"
#include <stdio.h>
#include <string.h>
#define MAX 50
typedef struct { int dia, mes; } Fecha;
typedef struct { char nombre[40], telefono[15], correo[40]; Fecha cumple; } Contacto;

void agregar(Contacto ag[], int *n)               // n por direccion: la funcion lo incrementa
{
    if (*n == MAX) { printf("Agenda llena\n"); return; }
    Contacto *c = &ag[*n];
    scanf(" %39[^\n]", c->nombre);
    scanf("%14s %39s %d %d", c->telefono, c->correo, &c->cumple.dia, &c->cumple.mes);
    (*n)++;
}
void mostrar(const Contacto *c)
{
    printf("  %s | %s | %s | %d/%d\n", c->nombre, c->telefono, c->correo, c->cumple.dia, c->cumple.mes);
}
void buscar(const Contacto ag[], int n)
{
    char t[40];
    scanf(" %39[^\n]", t);
    for (int i = 0; i < n; i++)
        if (strstr(ag[i].nombre, t) != NULL) mostrar(&ag[i]);
}
void cumpleaneros(const Contacto ag[], int n)
{
    int m;
    scanf("%d", &m);
    for (int i = 0; i < n; i++)
        if (ag[i].cumple.mes == m) mostrar(&ag[i]);
}
int main(void)
{
    Contacto agenda[MAX];
    int n = 0, op;
    do {
        printf("1) Agregar 2) Buscar 3) Listar 4) Cumpleanieros 5) Salir: ");
        scanf("%d", &op);
        switch (op)
        {
            case 1: agregar(agenda, &n); break;
            case 2: buscar(agenda, n); break;
            case 3: for (int i = 0; i < n; i++) mostrar(&agenda[i]); break;
            case 4: cumpleaneros(agenda, n); break;
        }
    } while (op != 5);
    return 0;
}
```
`(*n)++` lleva paréntesis: incrementa el entero al que apunta `n`. `&c->cumple.dia` es la dirección del día dentro de la fecha del contacto.
:::
:::

:::tarea A | T5. Diseña las estructuras de una app de música (solución libre) | 25 min | Solución libre
**Contexto.** Una app de música necesita guardar información. **Diseña todas las estructuras que creas necesarias** (canción, álbum, artista, lista de reproducción, usuario…), con sus miembros y tipos, e indica cuáles se anidan dentro de otras. No hay un único diseño correcto: justifica cada decisión. Después programa al menos dos estructuras y muestra un ejemplo.

:::solucion | T5
Un diseño posible (hay muchos válidos):

```c run title="musica.c"
#include <stdio.h>
typedef struct { int minutos, segundos; } Duracion;
typedef struct { char titulo[40], artista[40]; Duracion dur; int reproducciones; } Cancion;
typedef struct
{
    char nombre[40];
    Cancion canciones[20];
    int n;
} Lista;
int main(void)
{
    Lista l = {"Para programar", {{"Lo-fi 1", "Beats", {3, 12}, 1500}, {"Focus", "Calma", {4, 5}, 980}}, 2};
    int totalSeg = 0;
    for (int i = 0; i < l.n; i++)
        totalSeg += l.canciones[i].dur.minutos * 60 + l.canciones[i].dur.segundos;
    printf("%s: %d canciones, %d min %d s\n", l.nombre, l.n, totalSeg / 60, totalSeg % 60);
    return 0;
}
```
Otras estructuras posibles: `Artista` (nombre, país, género), `Album` (título, año, artista, arreglo de canciones), `Usuario` (nombre, plan, listas). Una decisión de diseño interesante: ¿la canción guarda el **nombre** del artista o una estructura `Artista` completa? (Copiar todo el artista en cada canción repite datos.)
:::
:::

:::tarea B | T6. ¿Por qué no funciona? (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
Explica **cada** error y por qué el compilador (o la ejecución) se comporta así; luego escribe la versión correcta.

```c blank title="struct_bugs.c"
struct Jugador { char nombre[20]; int puntos; }
void sumar(struct Jugador j, int p) { j.puntos += p; }
int main(void)
{
    struct Jugador equipo[3];
    Jugador.nombre = "Ana";
    equipo.puntos = 0;
    struct Jugador a = {"Luis", 10}, b = {"Luis", 10};
    if (a == b) printf("iguales");
    sumar(a, 5);
    printf("%d", a.puntos);     // esperaba 15
}
```

{{lineas:5}}

:::solucion | T6
1. Falta `;` al final de la definición del `struct` (y `#include <stdio.h>` y `<string.h>`).
2. `Jugador.nombre`: `Jugador` es un **tipo**, no una variable; además, el texto se copia con `strcpy` → `strcpy(equipo[0].nombre, "Ana");`.
3. `equipo.puntos`: `equipo` es un arreglo; falta el índice → `equipo[0].puntos`.
4. `a == b`: las estructuras no se comparan con `==` (error de compilación) → comparar miembro por miembro (`strcmp` para el nombre).
5. `sumar(a, 5)` recibe una **copia**: `a.puntos` sigue en 10 → parámetro `struct Jugador *j`, `j->puntos += p` y llamada `sumar(&a, 5)`.

```c run title="struct_ok.c"
#include <stdio.h>
#include <string.h>
struct Jugador { char nombre[20]; int puntos; };
void sumar(struct Jugador *j, int p) { j->puntos += p; }
int main(void)
{
    struct Jugador equipo[3];
    strcpy(equipo[0].nombre, "Ana");
    equipo[0].puntos = 0;
    struct Jugador a = {"Luis", 10}, b = {"Luis", 10};
    if (strcmp(a.nombre, b.nombre) == 0 && a.puntos == b.puntos) printf("iguales\n");
    sumar(&a, 5);
    printf("%d\n", a.puntos);
    return 0;
}
```
:::
:::

:::tarea B | T7. Copias y anidamiento (imaginación) | 20 min | Imaginación
**Sin ejecutar**, imagina (dibuja) el contenido de `x`, `y` y `z` después de cada línea y escribe la salida.

```c check title="imagina_struct.c"
#include <stdio.h>
typedef struct { int a; int b; } P;
typedef struct { P p; int c; } Q;
int main(void)
{
    Q x = {{1, 2}, 3};
    Q y = x;
    y.p.a = 10;
    P z = y.p;
    z.b = 20;
    x.c = z.a + z.b;
    printf("%d %d %d | %d %d %d | %d %d\n", x.p.a, x.p.b, x.c, y.p.a, y.p.b, y.c, z.a, z.b);
    return 0;
}
```

{{lineas:3}}

:::solucion | T7
`y` es una copia **independiente** de `x`; cambiar `y.p.a` no afecta a `x`. `z` copia `y.p` = {10, 2} y luego `z.b = 20`. Finalmente `x.c = 10 + 20 = 30`.

```c run title="imagina_struct.c"
#include <stdio.h>
typedef struct { int a; int b; } P;
typedef struct { P p; int c; } Q;
int main(void)
{
    Q x = {{1, 2}, 3};
    Q y = x;
    y.p.a = 10;
    P z = y.p;
    z.b = 20;
    x.c = z.a + z.b;
    printf("%d %d %d | %d %d %d | %d %d\n", x.p.a, x.p.b, x.c, y.p.a, y.p.b, y.c, z.a, z.b);
    return 0;
}
```
:::
:::

:::tarea AB | T8. Tabla de posiciones de un torneo (reto colaborativo) | 45 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Equipos de 4, niveles mezclados. `typedef struct { char nombre[20]; int pj, pg, pe, pp, gf, gc, pts; } Equipo;` para 4 equipos. Se capturan resultados (`local goles visitante goles`, con índices de equipo) hasta `-1`.
- **Integrante 1:** definición de las estructuras e inicialización de los 4 equipos.
- **Integrante 2:** función `registrar(Equipo *loc, Equipo *vis, int gl, int gv)` que actualiza partidos, goles y puntos (3 por victoria, 1 por empate).
- **Integrante 3:** ordenar la tabla por puntos y, en empate, por diferencia de goles (intercambiando registros completos).
- **Integrante 4:** mostrar la tabla con anchos de campo (`%-10s`, `%4d`) y anunciar al líder.
:::

:::solucion | T8
```c run title="torneo.c" stdin="0 2 1 1\n2 0 3 3\n0 1 2 2\n3 3 1 0\n1 2 0 1\n2 1 3 0\n-1\n"
#include <stdio.h>
#include <stdbool.h>
#define N 4
typedef struct { char nombre[20]; int pj, pg, pe, pp, gf, gc, pts; } Equipo;

void registrar(Equipo *l, Equipo *v, int gl, int gv)
{
    l->pj++; v->pj++;
    l->gf += gl; l->gc += gv; v->gf += gv; v->gc += gl;
    if (gl > gv) { l->pg++; v->pp++; l->pts += 3; }
    else if (gv > gl) { v->pg++; l->pp++; v->pts += 3; }
    else { l->pe++; v->pe++; l->pts++; v->pts++; }
}
bool vaAntes(const Equipo *a, const Equipo *b)
{
    if (a->pts != b->pts) return a->pts > b->pts;
    return (a->gf - a->gc) > (b->gf - b->gc);
}
int main(void)
{
    Equipo t[N] = {{.nombre = "Aguilas"}, {.nombre = "Halcones"},   // designados: el resto de miembros en 0
                   {.nombre = "Linces"}, {.nombre = "Toros"}};
    int l, gl, v, gv;
    while (scanf("%d", &l) == 1 && l != -1)
    {
        scanf("%d %d %d", &gl, &v, &gv);
        registrar(&t[l], &t[v], gl, gv);
    }
    for (int p = 1; p < N; p++)
        for (int j = 0; j < N - p; j++)
            if (vaAntes(&t[j + 1], &t[j])) { Equipo aux = t[j]; t[j] = t[j + 1]; t[j + 1] = aux; }
    printf("%-10s%4s%4s%4s%4s%5s%5s\n", "Equipo", "PJ", "G", "E", "P", "DG", "PTS");
    for (int i = 0; i < N; i++)
        printf("%-10s%4d%4d%4d%4d%5d%5d\n", t[i].nombre, t[i].pj, t[i].pg, t[i].pe,
               t[i].pp, t[i].gf - t[i].gc, t[i].pts);
    printf("Lider: %s\n", t[0].nombre);
    return 0;
}
```
`scanf("%d", &l) == 1` comprueba que sí se leyó un número antes de compararlo con `-1`.
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Ordenar alumnos por promedio sin mezclar sus datos | Modalidad, Ejemplo resuelto
*Guion segmentado (≈ 3 min), con el arreglo de fichas en pantalla.*

**Problema:** «Ordenar un arreglo de alumnos de mayor a menor promedio y mostrar el ranking».

**Segmento 1 — Reutilizar lo que ya sé.** {{como}} Tomo la burbuja del Tema 08 y la adapto: en lugar de comparar `v[j] > v[j + 1]` comparo `g[j].promedio < g[j + 1].promedio`. {{porque}} El algoritmo es el mismo; solo cambia **qué** se compara y el sentido (descendente).

**Segmento 2 — Intercambiar la ficha completa.** {{como}} El auxiliar es de tipo `Alumno`, no `double`: `Alumno aux = g[j]; g[j] = g[j + 1]; g[j + 1] = aux;`. {{porque}} Si intercambiara solo los promedios, los nombres quedarían con promedios ajenos: justo el problema de los arreglos paralelos que las estructuras resuelven.

**Segmento 3 — Una función que compara.** {{como}} Escribo `bool vaAntes(const Alumno *a, const Alumno *b)` y desempato por nombre con `strcmp`. {{porque}} Si mañana el criterio cambia, solo modifico esa función y el ordenamiento queda intacto; recibir punteros a `const` evita copiar cada ficha en cada comparación.

**Segmento 4 — Verificar que nadie se «mezcló».** {{como}} Antes de ordenar imprimo la lista; después reviso que cada nombre siga con **su** promedio. {{porque}} Comprobar la integridad de los registros es más importante que comprobar el orden.

```c run title="ranking.c"
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#define N 5
typedef struct { char nombre[20]; double promedio; } Alumno;
bool vaAntes(const Alumno *a, const Alumno *b)
{
    if (a->promedio != b->promedio) return a->promedio > b->promedio;
    return strcmp(a->nombre, b->nombre) < 0;         // desempate alfabetico
}
int main(void)
{
    Alumno g[N] = {{"Eva", 8.9}, {"Ana", 9.4}, {"Iker", 8.9}, {"Luis", 7.5}, {"Mia", 9.8}};
    for (int p = 1; p < N; p++)
        for (int j = 0; j < N - p; j++)
            if (vaAntes(&g[j + 1], &g[j]))
            {
                Alumno aux = g[j];
                g[j] = g[j + 1];
                g[j + 1] = aux;
            }
    for (int i = 0; i < N; i++)
        printf("%d. %s %.1f\n", i + 1, g[i].nombre, g[i].promedio);
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. ¿Qué es una estructura y en qué se diferencia de un arreglo?
2. ¿Con qué símbolo termina la definición de un `struct`?
3. ¿Qué operador se usa para acceder a un miembro?
4. ¿Cómo se accede al año de la fecha de nacimiento `nac` de la variable `p`?
5. Verdadero o falso: dos estructuras del mismo tipo se pueden asignar con `=`.
6. Verdadero o falso: dos estructuras del mismo tipo se pueden comparar con `==`.
7. ¿Cómo se escribe el nombre del tercer alumno de `Alumno grupo[30];`?
8. ¿Qué tipo de parámetro conviene para una función que solo **muestra** una estructura grande, sin copiarla?
9. ¿Qué significa `p->nombre` y cuándo se usa?
10. ¿Para qué sirve el `typedef` en `typedef struct { … } Alumno;`?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida:**

```c check title="p1.c"
#include <stdio.h>
typedef struct { char n; int c; } Item;
void doble(Item it) { it.c *= 2; }
void triple(Item *it) { it->c *= 3; }
int main(void)
{
    Item a = {'x', 2};
    Item b = a;
    doble(a);
    triple(&b);
    b.n = 'y';
    printf("%c%d %c%d\n", a.n, a.c, b.n, b.c);
    return 0;
}
```

**P2.** Define las estructuras para guardar un **vuelo**: código, origen, destino, fecha y hora de salida (estructuras anidadas) y número de asientos libres.

**P3. Corrige:** `struct Punto { double x, y } ; Punto p; p->x = 3; printf("%f", p);`

**P4. Escribe un programa** que lea 5 productos (nombre, precio, existencias) en un arreglo de estructuras y muestre el producto más caro, el valor total del inventario y los productos con menos de 10 piezas.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Defino estructuras (con <code>typedef</code>) con miembros de distintos tipos y las inicializo con llaves.</li>
<li>Accedo a miembros simples, anidados y de elementos de un arreglo.</li>
<li>Paso estructuras a funciones por valor o por dirección, usando <code>-&gt;</code>.</li>
<li>Ordeno arreglos de estructuras intercambiando registros completos.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 Un tipo definido por el programador que agrupa datos de distintos tipos bajo un nombre; un arreglo agrupa datos del mismo tipo accesibles por índice · 2 `};` (o `} Tipo;` con `typedef`) · 3 El punto (`.`) · 4 `p.nac.anio` · 5 Verdadero · 6 Falso: es un error de compilación · 7 `grupo[2].nombre` · 8 Un puntero a `const`: `const Tipo *p` · 9 Accede al miembro `nombre` de la estructura a la que apunta `p`; equivale a `(*p).nombre` y se usa cuando se tiene la dirección de la estructura (por ejemplo, en un parámetro `Tipo *p`) · 10 Da al tipo el nombre corto `Alumno`, para no escribir `struct` en cada declaración.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** `doble` recibe una copia (a sigue con 2); `triple` modifica `b` a través de su dirección (6).

```c run title="p1.c"
#include <stdio.h>
typedef struct { char n; int c; } Item;
void doble(Item it) { it.c *= 2; }
void triple(Item *it) { it->c *= 3; }
int main(void)
{
    Item a = {'x', 2};
    Item b = a;
    doble(a);
    triple(&b);
    b.n = 'y';
    printf("%c%d %c%d\n", a.n, a.c, b.n, b.c);
    return 0;
}
```

**P2.** `typedef struct { int dia, mes, anio; } Fecha; typedef struct { int h, m; } Hora; typedef struct { char codigo[10], origen[40], destino[40]; Fecha fecha; Hora salida; int libres; } Vuelo;`

**P3.** Falta `;` después de `double x, y`; sin `typedef` el tipo es `struct Punto`; con una variable (no un puntero) se usa `p.x` (la flecha `->` es para punteros); `printf` no sabe mostrar una estructura completa: `printf("%f, %f", p.x, p.y);`.

**P4.**

```c run title="p4.c" stdin="Cuaderno 45 30\nMochila 520 4\nPluma 12 120\nRegla 18 8\nCompas 95 15\n"
#include <stdio.h>
#define N 5
typedef struct { char nombre[30]; double precio; int exist; } Prod;
int main(void)
{
    Prod p[N];
    for (int i = 0; i < N; i++) scanf("%29s %lf %d", p[i].nombre, &p[i].precio, &p[i].exist);
    int caro = 0;
    double total = 0;
    for (int i = 0; i < N; i++)
    {
        if (p[i].precio > p[caro].precio) caro = i;
        total += p[i].precio * p[i].exist;
    }
    printf("Mas caro: %s\nInventario: $%.2f\nPor surtir:", p[caro].nombre, total);
    for (int i = 0; i < N; i++) if (p[i].exist < 10) printf(" %s", p[i].nombre);
    printf("\n");
    return 0;
}
```
:::
