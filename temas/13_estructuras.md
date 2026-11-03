---
num: "13"
archivo: "Tema13_Registros_estructuras_enumeraciones"
titulo: "Registros o estructuras (struct) y enumeraciones"
corto: "Estructuras (struct)"
lema: "Datos que viajan juntos deben guardarse juntos: un solo nombre para todos los campos de un objeto real."
duracion: "5 h · 3 sesiones"
previos: "Tema 08 (arreglos), Tema 10 (funciones y paso por referencia) y Tema 12 (string)."
fuentes:
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Cap. 11: Registros o estructuras (§11.1 Concepto, §11.2 Operaciones con estructuras completas: asignación, paso como parámetro, estructuras como valor de retorno; §11.3 Miembros como estructura; §11.4 Operaciones; §11.5 Ejercicios)."
  - "Lospinoso, J. (2019). *C++ Crash Course*. Cap. 2: Enumeration Types (`enum class`), Plain-Old-Data Classes (struct), Unions. Cap. 8: Structured Bindings."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §5.4 y Figura 5.3: material del estudio piloto sobre estructuras anidadas (Empleado con fecha de contrato)."
objetivos:
  A:
    - "Definir estructuras (`struct`) que agrupen datos relacionados de distintos tipos."
    - "Declarar e inicializar variables de tipo estructura y acceder a sus miembros con el operador punto."
    - "Definir y usar estructuras anidadas (una estructura como miembro de otra)."
    - "Manejar arreglos de estructuras para registrar colecciones (alumnos, productos, contactos)."
  B:
    - "Pasar estructuras a funciones (por valor, por referencia y `const &`) y devolverlas como resultado."
    - "Usar `enum class` para miembros con un conjunto fijo de valores."
    - "Ordenar y buscar en arreglos de estructuras por uno de sus campos."
    - "Usar enlaces estructurados (*structured bindings*, C++17)."
efectos:
  soporte:
    - ["Elementos aislados", "Necesidad → definición → acceso con punto → operaciones completas → anidadas → arreglos de estructuras → funciones → enum class (como en el piloto: primero declaración, luego manipulación)."]
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
    B: "Estructuras en funciones, `const &`, `enum class`, ordenamiento por campo, *structured bindings*."
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
    B: "Documentación de *aggregate initialization* y *structured bindings*."
plan:
  - ["Sesión 1", "Soporte + tareas", "Fichas humanas; conceptos 1–5; ejemplo resuelto (anidadas); T1, T2.", "100 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–8; T3, T4; Ruta B: T6, T7.", "100 min"]
  - ["Sesión 3", "Tareas + evaluación", "T5, T8 torneo; protocolo verbal; tests.", "100 min"]
glosario:
  - ["registro / estructura", "struct / record", "Tipo definido por el programador que agrupa datos (miembros) de distintos tipos."]
  - ["miembro / campo", "member / field", "Cada dato dentro de una estructura."]
  - ["operador punto", "member access operator (`.`)", "Accede a un miembro: `alumno.nombre`."]
  - ["estructura anidada", "nested struct", "Estructura que tiene como miembro a otra estructura."]
  - ["arreglo de estructuras", "array of structs", "Colección de registros del mismo tipo."]
  - ["tipo definido por el usuario", "user-defined type", "Tipo creado con `struct`, `class` o `enum`."]
  - ["clase de datos simples", "plain-old-data (POD) class", "Estructura que solo contiene datos (sin métodos), según el *Crash Course*."]
  - ["enumeración con ámbito", "scoped enumeration (`enum class`)", "Tipo con valores fijos con nombre: `Color::Rojo`."]
  - ["inicialización por agregado", "aggregate initialization", "Inicializar una estructura con llaves en orden: `{1, \"Ana\"}`."]
  - ["enlace estructurado", "structured binding", "`auto [a, b] = registro;` descompone sus miembros (C++17)."]
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
Un personaje de videojuego (nombre, vida, posición, inventario), un producto de una tienda en línea (código, precio, existencias), un punto en 3D (x, y, z), un mensaje de chat (autor, hora, texto): los programas reales modelan **objetos** con varios datos. Las estructuras son ese primer paso de modelado y el puente hacia las clases de la programación orientada a objetos (Tema 17). {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | El problema de los arreglos paralelos | Elementos aislados
```cpp check title="paralelos.cpp"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string nombre[3] = {"Ana", "Luis", "Eva"};
    double promedio[3] = {8.7, 9.4, 7.9};
    int edad[3] = {16, 17, 16};
    // Para ordenar por promedio hay que intercambiar en LOS TRES arreglos a la vez;
    // si olvidas uno, los datos de una persona se mezclan con los de otra.
    cout << nombre[1] << " " << promedio[1] << " " << edad[1] << "\n";
    return 0;
}
```
Los datos de «Luis» están dispersos en tres arreglos unidos solo por el índice 1. Una estructura los **agrupa**.
:::

:::concepto | 2 | Definir una estructura | Elementos aislados, Atención dividida
```cpp run title="definir.cpp"
#include <iostream>
#include <string>
using namespace std;

struct Alumno                  //> Define un TIPO nuevo llamado Alumno (el «formato de la ficha»)
{
    string nombre;             //> Miembros: pueden ser de tipos distintos
    int edad;
    double promedio;
};                             //> ¡La definición termina con punto y coma!

int main()
{
    Alumno a;                  //> Una VARIABLE de tipo Alumno (una ficha concreta)
    a.nombre = "Luis";         //> Operador punto: variable.miembro
    a.edad = 17;
    a.promedio = 9.4;
    cout << a.nombre << " (" << a.edad << "): " << a.promedio << "\n";
    return 0;
}
```

```diagram struct
var: a
type: Alumno
fields:
  - {name: nombre, val: '"Luis"'}
  - {name: edad, val: 17}
  - {name: promedio, val: 9.4}
figcaption: "Figura 1. Una variable de tipo Alumno: tres miembros guardados juntos."
```
Por convención, el nombre del tipo empieza con **mayúscula** (`Alumno`) y el de la variable con minúscula (`a`).
:::

:::concepto | 3 | Inicializar con llaves y leer miembros | Elementos aislados
```cpp run title="inicializar.cpp" stdin="Eva Rios\n16 7.9\n"
#include <iostream>
#include <string>
using namespace std;
struct Alumno { string nombre; int edad; double promedio; };

int main()
{
    Alumno a = {"Ana", 16, 8.7};          //> Inicialización por agregado: en el ORDEN de los miembros
    Alumno b{};                           //> Todos los miembros en su valor por defecto ("", 0, 0.0)
    getline(cin, b.nombre);               //> Cada miembro se lee como una variable normal
    cin >> b.edad >> b.promedio;
    cout << a.nombre << " | " << b.nombre << " " << b.edad << " " << b.promedio << "\n";
    return 0;
}
```
:::

:::concepto | 4 | Operaciones con la estructura completa | Elementos aislados, Atención dividida
Betancourt y Polanco (§11.2) distinguen lo que se puede hacer con el registro **completo**:

| Operación | ¿Se puede? | Ejemplo |
|---|---|---|
| Asignar (copiar todos los miembros) | ✔ | `b = a;` |
| Pasar como parámetro | ✔ | `mostrar(a);` |
| Devolver desde una función | ✔ | `Alumno crear();` |
| Comparar con `==` | ✘ (no por defecto) | compara miembro por miembro |
| Mostrar con `cout << a` | ✘ (no por defecto) | escribe una función `mostrar` |

```cpp run title="copia.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Punto { int x, y; };
int main()
{
    Punto p = {2, 5};
    Punto q = p;                   //> Copia COMPLETA: q es independiente de p
    q.x = 10;                      //> Cambiar q no afecta a p
    cout << "p = (" << p.x << ", " << p.y << ")  q = (" << q.x << ", " << q.y << ")\n";
    bool iguales = (p.x == q.x && p.y == q.y);   //> Comparar: miembro por miembro
    cout << boolalpha << iguales << "\n";
    return 0;
}
```
:::

:::movimiento | Fichas humanas (10 min)
Equipos de 3: cada estudiante es un **miembro** de una estructura `Alumno` (uno sostiene «nombre», otro «edad», otro «promedio») y entre los tres son **una variable**. El instructor dicta: «`b = a;`» (el equipo b copia en sus hojas los valores del equipo a), «`b.edad = 18;`» (¿cambió el equipo a?), «crea un arreglo de 3 alumnos» (tres equipos en fila: `grupo[0]`, `grupo[1]`, `grupo[2]`), «`grupo[1].nombre`» (¿quién responde?).
:::

:::concepto | 5 | Estructuras anidadas | Elementos aislados, Atención dividida
Un miembro puede ser **otra estructura** (Betancourt y Polanco, §11.3). Para llegar al dato interior se encadenan puntos:

```cpp run title="anidada.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Fecha { int dia, mes, anio; };
struct Empleado
{
    int id;
    string nombre;
    Fecha contrato;               //> Miembro de tipo Fecha: estructura anidada
};
int main()
{
    Empleado e = {101, "Ana Lopez", {15, 3, 2023}};   //> Llaves dentro de llaves
    cout << e.nombre << " contratada el " << e.contrato.dia << "/" << e.contrato.mes
         << "/" << e.contrato.anio << "\n";            //> Dos puntos: e → contrato → dia
    e.contrato.anio = 2024;                           //> Se modifica igual
    cout << "Nuevo anio: " << e.contrato.anio << "\n";
    return 0;
}
```
:::

:::concepto | 6 | Arreglos de estructuras | Elementos aislados, Atención dividida
Un arreglo cuyos elementos son estructuras: `grupo[i].miembro`.

```cpp run title="arreglo_struct.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Alumno { string nombre; double promedio; };
int main()
{
    const int N = 4;
    Alumno grupo[N] = {{"Ana", 8.7}, {"Luis", 9.4}, {"Eva", 7.9}, {"Iker", 9.1}};
    int mejor = 0;
    double suma = 0;
    for (int i = 0; i < N; i++)
    {
        suma += grupo[i].promedio;                    //> Índice del arreglo, luego punto del miembro
        if (grupo[i].promedio > grupo[mejor].promedio) mejor = i;
    }
    cout << "Promedio del grupo: " << suma / N << "\n";
    cout << "Mejor: " << grupo[mejor].nombre << " (" << grupo[mejor].promedio << ")\n";
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

:::concepto | 7 | Estructuras y funciones | Elementos aislados, Atención dividida
```cpp run title="struct_funciones.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Producto { string nombre; double precio; int existencias; };

void mostrar(const Producto& p)                 //> const &: sin copia y sin modificar
{
    cout << p.nombre << " $" << p.precio << " (" << p.existencias << ")\n";
}
void vender(Producto& p, int cantidad)          //> &: la venta debe modificar el original
{
    if (cantidad <= p.existencias) p.existencias -= cantidad;
}
Producto crear(string n, double pr)             //> Devuelve una estructura completa
{
    Producto p = {n, pr, 0};
    return p;
}
int main()
{
    Producto lapiz = crear("Lapiz", 8.5);
    lapiz.existencias = 40;
    vender(lapiz, 12);
    mostrar(lapiz);
    return 0;
}
```
:::

:::concepto | 8 | Ruta B · `enum class` y enlaces estructurados | Elementos aislados, Reversión de la experiencia
El *C++ Crash Course* (cap. 2) usa `enum class` para miembros con valores fijos, y (cap. 8) los *structured bindings* para «desempacar» una estructura:

```cpp run title="enum_struct.cpp"
#include <iostream>
#include <string>
using namespace std;
enum class Clase { Guerrero, Mago, Arquero };     //> Solo tres valores posibles
struct Personaje { string nombre; Clase clase; int nivel; };

string nombreClase(Clase c)
{
    switch (c)
    {
        case Clase::Guerrero: return "Guerrero";
        case Clase::Mago:     return "Mago";
        case Clase::Arquero:  return "Arquero";
    }
    return "?";
}

int main()
{
    Personaje p = {"Lyra", Clase::Mago, 7};
    auto [nom, cla, niv] = p;                     //> Enlace estructurado: copia cada miembro en una variable
    cout << nom << " es " << nombreClase(cla) << " de nivel " << niv << "\n";
    return 0;
}
```
:::

## 1.2 Ejemplo resuelto: el empleado y su fecha de contrato (tesis, Figura 5.3)

:::ejemplo | Estructura anidada paso a paso | Ejemplo resuelto, Atención dividida
**Problema.** Registrar a un empleado con su identificador, su nombre y su fecha de contrato, y mostrar sus datos. (Es el material que se usó con estudiantes novatos en el estudio piloto del modelo CLT4BP.)

**Explicación paso a paso**

1. Primero definimos una estructura llamada `Fecha` con los campos `dia`, `mes` y `anio`.
2. Después definimos la estructura `Empleado` con los campos `id` y `nombre`.
3. Dentro de `Empleado` agregamos el campo `contrato`, de tipo `Fecha`.
4. Declaramos la variable `empleado1` (todos sus campos vacíos).
5. Llenamos `id` y `nombre`; luego, con doble punto, los campos de la fecha.

<div class="cols eq">
<div>

```diagram struct
var: "Empleado empleado1;"
fields:
  - {name: id, val: "?"}
  - {name: nombre, val: '""'}
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

```cpp run title="empleado.cpp"
#include <iostream>
#include <string>
using namespace std;

struct Fecha                 //> Paso 1
{
    int dia;
    int mes;
    int anio;
};

struct Empleado              //> Paso 2
{
    int id;
    string nombre;
    Fecha contrato;          //> Paso 3: anidada
};

int main()
{
    Empleado empleado1;                    //> Paso 4
    empleado1.id = 101;                    //> Paso 5
    empleado1.nombre = "Ana Lopez";
    empleado1.contrato.dia = 15;
    empleado1.contrato.mes = 3;
    empleado1.contrato.anio = 2023;
    cout << empleado1.id << " - "
         << empleado1.nombre << " - "
         << empleado1.contrato.dia << "/"
         << empleado1.contrato.mes << "/"
         << empleado1.contrato.anio << "\n";
    return 0;
}
```

</div>
</div>

**Verificación.** Cada diagrama corresponde a un bloque del código: declaración (todo vacío), asignación de los campos simples y asignación de los campos anidados con doble punto.
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.16; ranksep=0.3;
@term(s, "struct Tipo { miembros };")
@proc(v, "variable: Tipo x;\ninicializar {…}")
@proc(p, "x.miembro\n(operador punto)")
@proc(o, "asignar · pasar · devolver\n(no ==, no cout <<)")
@proc(n, "anidada:\nx.fecha.dia")
@proc(a, "arreglo:\ngrupo[i].miembro")
@sub(f, "funciones: valor · & · const&")
@hl(e, "enum class · auto [a, b]")
s -> v -> p; v -> o; s -> n; s -> a; o -> f; s -> e [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1
```cpp run title="plantilla_struct.cpp"
#include <iostream>
#include <string>
using namespace std;

struct Fecha { int dia, mes, anio; };          // 1) definir (antes de main y de las funciones)
struct Contacto
{
    string nombre;
    string telefono;
    Fecha cumple;                              // 2) anidar
};

void mostrar(const Contacto& c)                // 3) funcion que solo lee
{
    cout << c.nombre << " " << c.telefono << " " << c.cumple.dia << "/" << c.cumple.mes << "\n";
}

int main()
{
    Contacto c1 = {"Ana", "4491234567", {12, 5, 2008}};   // 4) inicializar
    Contacto agenda[50];                                  // 5) arreglo de estructuras
    int n = 0;
    agenda[n++] = c1;                                     // 6) asignar registro completo
    for (int i = 0; i < n; i++) mostrar(agenda[i]);
    return 0;
}
```

| Quiero… | Escribo |
|---|---|
| Acceder a un miembro | `variable.miembro` |
| Miembro de una anidada | `variable.anidada.miembro` |
| Miembro de un elemento del arreglo | `arreglo[i].miembro` |
| Intercambiar dos registros | `Tipo aux = a[i]; a[i] = a[j]; a[j] = aux;` |
| Comparar dos registros | `a.x == b.x && a.y == b.y` (miembro a miembro) |
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿La definición del <code>struct</code> termina en <code>};</code> y está antes de donde se usa?</li>
<li>¿Distingo el <b>tipo</b> (<code>Alumno</code>) de la <b>variable</b> (<code>a</code>)? Los puntos van en la variable.</li>
<li>En un arreglo, ¿puse el índice antes del punto: <code>grupo[i].nombre</code>?</li>
<li>¿Inicialicé en el mismo orden en que declaré los miembros?</li>
<li>¿La función debe modificar el registro? <code>&amp;</code>. ¿Solo leerlo? <code>const &amp;</code>.</li>
<li>Al ordenar, ¿intercambio el registro <b>completo</b> (no solo el campo de la comparación)?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Olvidar el `;` al final de la definición.**

```cpp err
#include <string>
struct Libro
{
    std::string titulo;
    int paginas;
}
int main()
{
    Libro l;
    return 0;
}
```

**b) Usar el tipo como si fuera una variable.** `Alumno.nombre = "Ana";` no tiene sentido: primero hay que declarar una variable `Alumno a;` y usar `a.nombre`.

**c) Comparar estructuras completas con `==`.**

```cpp err
struct Punto { int x, y; };
int main()
{
    Punto p{1, 2}, q{1, 2};
    if (p == q) return 1;
    return 0;
}
```
*Corrección:* `p.x == q.x && p.y == q.y` (o definir el operador `==`, Ruta B avanzada).

**d) Olvidar el índice del arreglo.** `grupo.nombre` no existe; es `grupo[i].nombre`.

**e) Modificar una copia.** `void subirNivel(Personaje p) { p.nivel++; }` no cambia al personaje original: usa `Personaje& p`.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Inventario de una tienda | Variabilidad
```cpp run title="inventario.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Producto { int codigo; string nombre; double precio; int existencias; };
int main()
{
    Producto inv[] = {{101, "Cuaderno", 45, 30}, {102, "Pluma", 12, 120}, {103, "Mochila", 520, 4}};
    double valorTotal = 0;
    for (const Producto& p : inv)                        //> for de rango sobre un arreglo de estructuras
    {
        double valor = p.precio * p.existencias;
        valorTotal += valor;
        cout << p.codigo << " " << p.nombre << ": $" << valor << (p.existencias < 5 ? "  (surtir!)" : "") << "\n";
    }
    cout << "Valor del inventario: $" << valorTotal << "\n";
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Antes de programar, dibuja la estructura como una ficha con sus campos.

:::tarea A | T1. Ficha de producto: ejemplo y gemelo | 20 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia:**

```cpp run title="producto.cpp" stdin="205\nAudifonos gamer\n899.50 7\n"
#include <iostream>
#include <string>
using namespace std;

struct Producto                     //> El «formato» de la ficha
{
    int codigo;
    string nombre;
    double precio;
    int existencias;
};

int main()
{
    Producto p;                     //> Una ficha concreta
    cin >> p.codigo;
    cin.ignore();                   //> Antes de getline (Tema 02)
    getline(cin, p.nombre);
    cin >> p.precio >> p.existencias;
    cout << "[" << p.codigo << "] " << p.nombre << "\n";
    cout << "Precio: $" << p.precio << "  Existencias: " << p.existencias << "\n";
    cout << "Valor en almacen: $" << p.precio * p.existencias << "\n";   //> Los miembros se usan en expresiones
    return 0;
}
```

**Paso 2 · Gemelo.** Define `struct Libro` con ISBN (texto), título, autor, año y precio; lee un libro y muestra su ficha y cuántos años tiene de publicado (respecto a 2026).

:::solucion | T1
```cpp run title="libro.cpp" stdin="978-607-1\nRayuela\nJulio Cortazar\n1963 320\n"
#include <iostream>
#include <string>
using namespace std;
struct Libro { string isbn, titulo, autor; int anio; double precio; };
int main()
{
    Libro l;
    getline(cin, l.isbn);
    getline(cin, l.titulo);
    getline(cin, l.autor);
    cin >> l.anio >> l.precio;
    cout << l.titulo << " (" << l.autor << ", " << l.anio << ")\nISBN " << l.isbn
         << " | $" << l.precio << " | " << 2026 - l.anio << " anios de publicado\n";
    return 0;
}
```
:::
:::

:::tarea A | T2. Lista de alumnos (completa con pistas) | 25 min | Problema por completar
**Contexto.** Registrar `n` alumnos (nombre y tres calificaciones), calcular el promedio de cada uno y mostrar al de mejor promedio.

```cpp blank title="lista_alumnos.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Alumno
{
    string nombre;
    double cal[3];                       // un arreglo como miembro
    double promedio;
}__1__                                   // 1: fin de la definicion
int main()
{
    Alumno grupo[30];
    int n, mejor = 0;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> __2__;                    // 2: nombre del alumno i
        double s = 0;
        for (int k = 0; k < 3; k++)
        {
            cin >> __3__;                // 3: calificacion k del alumno i
            s += grupo[i].cal[k];
        }
        grupo[i].promedio = __4__;       // 4: promedio
        if (grupo[i].promedio > __5__)   // 5: promedio del mejor hasta ahora
            mejor = i;
    }
    cout << "Mejor: " << grupo[mejor].nombre << " " << grupo[mejor].promedio << "\n";
    return 0;
}
```

:::solucion | T2
{{c:1}} `;` · {{c:2}} `grupo[i].nombre` · {{c:3}} `grupo[i].cal[k]` · {{c:4}} `s / 3` · {{c:5}} `grupo[mejor].promedio`

```cpp run title="lista_alumnos.cpp" stdin="3\nAna 9 8 10\nLuis 7 9 8\nEva 10 9 9.5\n"
#include <iostream>
#include <string>
using namespace std;
struct Alumno
{
    string nombre;
    double cal[3];
    double promedio;
};
int main()
{
    Alumno grupo[30];
    int n, mejor = 0;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> grupo[i].nombre;
        double s = 0;
        for (int k = 0; k < 3; k++)
        {
            cin >> grupo[i].cal[k];
            s += grupo[i].cal[k];
        }
        grupo[i].promedio = s / 3;
        if (grupo[i].promedio > grupo[mejor].promedio)
            mejor = i;
    }
    cout << "Mejor: " << grupo[mejor].nombre << " " << grupo[mejor].promedio << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T3. ¿Fecha válida? ¿Cuál es anterior? (completa sin pistas) | 25 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Una agenda necesita validar fechas y saber cuál de dos es anterior. Reutiliza la lógica de días del mes (Tema 05).

```cpp blank title="fechas.cpp"
#include <iostream>
using namespace std;
struct Fecha { int dia, mes, anio; };

bool bisiesto(int a) { return (a % 4 == 0 && a % 100 != 0) || a % 400 == 0; }

int diasDelMes(int m, int a)
{
    if (m == 2) return __1__;
    if (m == 4 || m == 6 || m == 9 || m == 11) return 30;
    return 31;
}

bool esValida(const Fecha& f)
{
    return f.mes >= 1 && f.mes <= 12 && __2__ && __3__;
}

bool esAnterior(const Fecha& a, const Fecha& b)
{
    if (a.anio != b.anio) return __4__;
    if (a.mes != b.mes) return __5__;
    return __6__;
}

int main()
{
    Fecha x, y;
    cin >> x.dia >> x.mes >> x.anio >> y.dia >> y.mes >> y.anio;
    cout << "x valida: " << esValida(x) << ", y valida: " << esValida(y) << "\n";
    cout << "x anterior a y: " << esAnterior(x, y) << "\n";
    return 0;
}
```

:::solucion | T3
{{c:1}} `bisiesto(a) ? 29 : 28` · {{c:2}} `f.dia >= 1` · {{c:3}} `f.dia <= diasDelMes(f.mes, f.anio)` · {{c:4}} `a.anio < b.anio` · {{c:5}} `a.mes < b.mes` · {{c:6}} `a.dia < b.dia`

```cpp run title="fechas.cpp" runs="29 2 2024 1 3 2024|29 2 2023 15 8 2022"
#include <iostream>
using namespace std;
struct Fecha { int dia, mes, anio; };

bool bisiesto(int a) { return (a % 4 == 0 && a % 100 != 0) || a % 400 == 0; }

int diasDelMes(int m, int a)
{
    if (m == 2) return bisiesto(a) ? 29 : 28;
    if (m == 4 || m == 6 || m == 9 || m == 11) return 30;
    return 31;
}

bool esValida(const Fecha& f)
{
    return f.mes >= 1 && f.mes <= 12 && f.dia >= 1 && f.dia <= diasDelMes(f.mes, f.anio);
}

bool esAnterior(const Fecha& a, const Fecha& b)
{
    if (a.anio != b.anio) return a.anio < b.anio;
    if (a.mes != b.mes) return a.mes < b.mes;
    return a.dia < b.dia;
}

int main()
{
    Fecha x, y;
    cin >> x.dia >> x.mes >> x.anio >> y.dia >> y.mes >> y.anio;
    cout << "x valida: " << esValida(x) << ", y valida: " << esValida(y) << "\n";
    cout << "x anterior a y: " << esAnterior(x, y) << "\n";
    return 0;
}
```
`esValida(f.mes >= 1 && …)` aprovecha el cortocircuito: si el mes es inválido, nunca se llama a `diasDelMes` con él.
:::
:::

:::tarea AB | T4. Agenda de contactos (problema convencional) | 40 min | Variabilidad
**Contexto.** Programa una agenda con un arreglo de hasta 50 contactos (`nombre`, `telefono`, `correo`, `cumple` de tipo `Fecha`) y un menú: **1** agregar, **2** buscar por nombre (mostrar todos los que **contengan** el texto buscado), **3** listar todos, **4** cumpleañeros de un mes dado, **5** salir. Usa una función por opción.

:::solucion | T4
```cpp run title="agenda.cpp" stdin="1\nAna Lopez\n4491112233 ana@mail.com 12 5\n1\nLuis Ana Perez\n4494445566 luis@mail.com 3 9\n2\nAna\n4\n9\n3\n5\n"
#include <iostream>
#include <string>
using namespace std;
struct Fecha { int dia, mes; };
struct Contacto { string nombre, telefono, correo; Fecha cumple; };

void agregar(Contacto ag[], int& n)
{
    if (n == 50) { cout << "Agenda llena\n"; return; }
    cin.ignore();
    getline(cin, ag[n].nombre);
    cin >> ag[n].telefono >> ag[n].correo >> ag[n].cumple.dia >> ag[n].cumple.mes;
    n++;
}
void mostrar(const Contacto& c)
{
    cout << "  " << c.nombre << " | " << c.telefono << " | " << c.correo
         << " | " << c.cumple.dia << "/" << c.cumple.mes << "\n";
}
void buscar(const Contacto ag[], int n)
{
    string t;
    cin.ignore();
    getline(cin, t);
    for (int i = 0; i < n; i++)
        if (ag[i].nombre.find(t) != string::npos) mostrar(ag[i]);
}
void cumpleaneros(const Contacto ag[], int n)
{
    int m;
    cin >> m;
    for (int i = 0; i < n; i++)
        if (ag[i].cumple.mes == m) mostrar(ag[i]);
}
int main()
{
    Contacto agenda[50];
    int n = 0, op;
    do {
        cout << "1) Agregar 2) Buscar 3) Listar 4) Cumpleanieros 5) Salir: ";
        cin >> op;
        switch (op)
        {
            case 1: agregar(agenda, n); break;
            case 2: buscar(agenda, n); break;
            case 3: for (int i = 0; i < n; i++) mostrar(agenda[i]); break;
            case 4: cumpleaneros(agenda, n); break;
        }
    } while (op != 5);
    return 0;
}
```
:::
:::

:::tarea A | T5. Diseña las estructuras de una app de música (solución libre) | 25 min | Solución libre
**Contexto.** Una app de música necesita guardar información. **Diseña todas las estructuras que creas necesarias** (canción, álbum, artista, lista de reproducción, usuario…), con sus miembros y tipos, e indica cuáles se anidan dentro de otras. No hay un único diseño correcto: justifica cada decisión. Después programa al menos dos estructuras y muestra un ejemplo.

:::solucion | T5
Un diseño posible (hay muchos válidos):

```cpp run title="musica.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Duracion { int minutos, segundos; };
struct Cancion { string titulo, artista; Duracion dur; int reproducciones; };
struct Lista
{
    string nombre;
    Cancion canciones[20];
    int n;
};
int main()
{
    Lista l = {"Para programar", {{"Lo-fi 1", "Beats", {3, 12}, 1500}, {"Focus", "Calma", {4, 5}, 980}}, 2};
    int totalSeg = 0;
    for (int i = 0; i < l.n; i++)
        totalSeg += l.canciones[i].dur.minutos * 60 + l.canciones[i].dur.segundos;
    cout << l.nombre << ": " << l.n << " canciones, " << totalSeg / 60 << " min "
         << totalSeg % 60 << " s\n";
    return 0;
}
```
Otras estructuras posibles: `Artista` (nombre, país, género), `Album` (título, año, artista, arreglo de canciones), `Usuario` (nombre, plan, listas). Una decisión de diseño interesante: ¿la canción guarda el **nombre** del artista o una estructura `Artista` completa? (Copiar todo el artista en cada canción repite datos.)
:::
:::

:::tarea B | T6. ¿Por qué no funciona? (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
Explica **cada** error y por qué el compilador (o la ejecución) se comporta así; luego escribe la versión correcta.

```cpp blank title="struct_bugs.cpp"
struct Jugador { string nombre; int puntos; }
void sumar(Jugador j, int p) { j.puntos += p; }
int main()
{
    Jugador equipo[3];
    Jugador.nombre = "Ana";
    equipo.puntos = 0;
    Jugador a = {"Luis", 10}, b = {"Luis", 10};
    if (a == b) cout << "iguales";
    sumar(a, 5);
    cout << a.puntos;     // esperaba 15
}
```

{{lineas:5}}

:::solucion | T6
1. Falta `;` al final de la definición del `struct` (y `#include <iostream>`, `<string>`, `using namespace std;`).
2. `Jugador.nombre`: `Jugador` es un **tipo**, no una variable → `equipo[0].nombre = "Ana";`.
3. `equipo.puntos`: `equipo` es un arreglo; falta el índice → `equipo[0].puntos`.
4. `a == b`: las estructuras no se comparan con `==` por defecto → comparar miembro por miembro.
5. `sumar(a, 5)` recibe una **copia**: `a.puntos` sigue en 10 → parámetro `Jugador& j`.

```cpp run title="struct_ok.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Jugador { string nombre; int puntos; };
void sumar(Jugador& j, int p) { j.puntos += p; }
int main()
{
    Jugador equipo[3];
    equipo[0].nombre = "Ana";
    equipo[0].puntos = 0;
    Jugador a = {"Luis", 10}, b = {"Luis", 10};
    if (a.nombre == b.nombre && a.puntos == b.puntos) cout << "iguales\n";
    sumar(a, 5);
    cout << a.puntos << "\n";
    return 0;
}
```
:::
:::

:::tarea B | T7. Copias y anidamiento (imaginación) | 20 min | Imaginación
**Sin ejecutar**, imagina (dibuja) el contenido de `x`, `y` y `z` después de cada línea y escribe la salida.

```cpp check title="imagina_struct.cpp"
#include <iostream>
using namespace std;
struct P { int a; int b; };
struct Q { P p; int c; };
int main()
{
    Q x = {{1, 2}, 3};
    Q y = x;
    y.p.a = 10;
    P z = y.p;
    z.b = 20;
    x.c = z.a + z.b;
    cout << x.p.a << " " << x.p.b << " " << x.c << " | "
         << y.p.a << " " << y.p.b << " " << y.c << " | " << z.a << " " << z.b << "\n";
    return 0;
}
```

{{lineas:3}}

:::solucion | T7
`y` es una copia **independiente** de `x`; cambiar `y.p.a` no afecta a `x`. `z` copia `y.p` = {10, 2} y luego `z.b = 20`. Finalmente `x.c = 10 + 20 = 30`.

```cpp run title="imagina_struct.cpp"
#include <iostream>
using namespace std;
struct P { int a; int b; };
struct Q { P p; int c; };
int main()
{
    Q x = {{1, 2}, 3};
    Q y = x;
    y.p.a = 10;
    P z = y.p;
    z.b = 20;
    x.c = z.a + z.b;
    cout << x.p.a << " " << x.p.b << " " << x.c << " | "
         << y.p.a << " " << y.p.b << " " << y.c << " | " << z.a << " " << z.b << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T8. Tabla de posiciones de un torneo (reto colaborativo) | 45 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Equipos de 4, niveles mezclados. `struct Equipo { string nombre; int pj, pg, pe, pp, gf, gc, pts; };` para 4 equipos. Se capturan resultados (`local goles visitante goles`, con índices de equipo) hasta `-1`.
- **Integrante 1:** definición de las estructuras e inicialización de los 4 equipos.
- **Integrante 2:** función `registrar(Equipo& loc, Equipo& vis, int gl, int gv)` que actualiza partidos, goles y puntos (3 por victoria, 1 por empate).
- **Integrante 3:** ordenar la tabla por puntos y, en empate, por diferencia de goles (intercambiando registros completos).
- **Integrante 4:** mostrar la tabla con `setw` y anunciar al líder.
:::

:::solucion | T8
```cpp run title="torneo.cpp" stdin="0 2 1 1\n2 0 3 3\n0 1 2 2\n3 3 1 0\n1 2 0 1\n2 1 3 0\n-1\n"
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;
struct Equipo { string nombre; int pj, pg, pe, pp, gf, gc, pts; };

void registrar(Equipo& l, Equipo& v, int gl, int gv)
{
    l.pj++; v.pj++;
    l.gf += gl; l.gc += gv; v.gf += gv; v.gc += gl;
    if (gl > gv) { l.pg++; v.pp++; l.pts += 3; }
    else if (gv > gl) { v.pg++; l.pp++; v.pts += 3; }
    else { l.pe++; v.pe++; l.pts++; v.pts++; }
}
bool vaAntes(const Equipo& a, const Equipo& b)
{
    if (a.pts != b.pts) return a.pts > b.pts;
    return (a.gf - a.gc) > (b.gf - b.gc);
}
int main()
{
    const int N = 4;
    Equipo t[N] = {{"Aguilas"}, {"Halcones"}, {"Linces"}, {"Toros"}};   // el resto de miembros en 0
    int l, gl, v, gv;
    while (cin >> l && l != -1)
    {
        cin >> gl >> v >> gv;
        registrar(t[l], t[v], gl, gv);
    }
    for (int p = 1; p < N; p++)
        for (int j = 0; j < N - p; j++)
            if (vaAntes(t[j + 1], t[j])) { Equipo aux = t[j]; t[j] = t[j + 1]; t[j + 1] = aux; }
    cout << left << setw(10) << "Equipo" << right << setw(4) << "PJ" << setw(4) << "G" << setw(4) << "E"
         << setw(4) << "P" << setw(5) << "DG" << setw(5) << "PTS" << "\n";
    for (const Equipo& e : t)
        cout << left << setw(10) << e.nombre << right << setw(4) << e.pj << setw(4) << e.pg << setw(4)
             << e.pe << setw(4) << e.pp << setw(5) << e.gf - e.gc << setw(5) << e.pts << "\n";
    cout << "Lider: " << t[0].nombre << "\n";
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Ordenar alumnos por promedio sin mezclar sus datos | Modalidad, Ejemplo resuelto
*Guion segmentado (≈ 3 min), con el arreglo de fichas en pantalla.*

**Problema:** «Ordenar un arreglo de alumnos de mayor a menor promedio y mostrar el ranking».

**Segmento 1 — Reutilizar lo que ya sé.** {{como}} Tomo la burbuja del Tema 08 y la adapto: en lugar de comparar `v[j] > v[j + 1]` comparo `g[j].promedio < g[j + 1].promedio`. {{porque}} El algoritmo es el mismo; solo cambia **qué** se compara y el sentido (descendente).

**Segmento 2 — Intercambiar la ficha completa.** {{como}} El auxiliar es de tipo `Alumno`, no `double`: `Alumno aux = g[j]; g[j] = g[j + 1]; g[j + 1] = aux;`. {{porque}} Si intercambiara solo los promedios, los nombres quedarían con promedios ajenos: justo el problema de los arreglos paralelos que las estructuras resuelven.

**Segmento 3 — Una función que compara.** {{como}} Escribo `bool vaAntes(const Alumno& a, const Alumno& b)`. {{porque}} Si mañana el criterio cambia (por ejemplo, desempatar por nombre), solo modifico esa función y el ordenamiento queda intacto.

**Segmento 4 — Verificar que nadie se «mezcló».** {{como}} Antes de ordenar imprimo la lista; después reviso que cada nombre siga con **su** promedio. {{porque}} Comprobar la integridad de los registros es más importante que comprobar el orden.

```cpp run title="ranking.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Alumno { string nombre; double promedio; };
bool vaAntes(const Alumno& a, const Alumno& b)
{
    if (a.promedio != b.promedio) return a.promedio > b.promedio;
    return a.nombre < b.nombre;                     // desempate alfabetico
}
int main()
{
    const int N = 5;
    Alumno g[N] = {{"Eva", 8.9}, {"Ana", 9.4}, {"Iker", 8.9}, {"Luis", 7.5}, {"Mia", 9.8}};
    for (int p = 1; p < N; p++)
        for (int j = 0; j < N - p; j++)
            if (vaAntes(g[j + 1], g[j]))
            {
                Alumno aux = g[j];
                g[j] = g[j + 1];
                g[j + 1] = aux;
            }
    for (int i = 0; i < N; i++)
        cout << i + 1 << ". " << g[i].nombre << " " << g[i].promedio << "\n";
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
6. Verdadero o falso: dos estructuras del mismo tipo se pueden comparar con `==` sin hacer nada más.
7. ¿Cómo se escribe el nombre del tercer alumno de `Alumno grupo[30];`?
8. ¿Qué tipo de parámetro conviene para una función que solo **muestra** una estructura?
9. ¿Para qué sirve `enum class`?
10. Menciona una ventaja de un arreglo de estructuras sobre varios arreglos paralelos.
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida:**

```cpp check title="p1.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Item { string n; int c; };
void doble(Item it) { it.c *= 2; }
void triple(Item& it) { it.c *= 3; }
int main()
{
    Item a = {"x", 2};
    Item b = a;
    doble(a);
    triple(b);
    b.n = "y";
    cout << a.n << a.c << " " << b.n << b.c << "\n";
    return 0;
}
```

**P2.** Define las estructuras para guardar un **vuelo**: código, origen, destino, fecha y hora de salida (estructuras anidadas) y número de asientos libres.

**P3. Corrige:** `struct Punto { double x, y } ; Punto p; p->x = 3; cout << p;`

**P4. Escribe un programa** que lea 5 productos (nombre, precio, existencias) en un arreglo de estructuras y muestre el producto más caro, el valor total del inventario y los productos con menos de 10 piezas.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Defino estructuras con miembros de distintos tipos y las inicializo con llaves.</li>
<li>Accedo a miembros simples, anidados y de elementos de un arreglo.</li>
<li>Paso estructuras a funciones con el tipo de parámetro adecuado.</li>
<li>Ordeno arreglos de estructuras intercambiando registros completos.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 Un tipo definido por el programador que agrupa datos de distintos tipos bajo un nombre; un arreglo agrupa datos del mismo tipo accesibles por índice · 2 `};` · 3 El punto (`.`) · 4 `p.nac.anio` · 5 Verdadero · 6 Falso · 7 `grupo[2].nombre` · 8 `const Tipo&` · 9 Para definir un tipo con un conjunto fijo de valores con nombre (`Clase::Mago`), evitando números mágicos · 10 Los datos de cada elemento se mantienen juntos: al ordenar o copiar no se mezclan.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** `doble` recibe una copia (a sigue con 2); `triple` modifica `b` (6).

```cpp run title="p1.cpp"
#include <iostream>
#include <string>
using namespace std;
struct Item { string n; int c; };
void doble(Item it) { it.c *= 2; }
void triple(Item& it) { it.c *= 3; }
int main()
{
    Item a = {"x", 2};
    Item b = a;
    doble(a);
    triple(b);
    b.n = "y";
    cout << a.n << a.c << " " << b.n << b.c << "\n";
    return 0;
}
```

**P2.** `struct Fecha { int dia, mes, anio; }; struct Hora { int h, m; }; struct Vuelo { string codigo, origen, destino; Fecha fecha; Hora salida; int libres; };`

**P3.** Falta `;` después de `double x, y`; con una variable (no puntero) se usa `p.x` (la flecha `->` es para punteros, Tema 14); `cout << p` no está definido: `cout << p.x << ", " << p.y;`.

**P4.**

```cpp run title="p4.cpp" stdin="Cuaderno 45 30\nMochila 520 4\nPluma 12 120\nRegla 18 8\nCompas 95 15\n"
#include <iostream>
#include <string>
using namespace std;
struct Prod { string nombre; double precio; int exist; };
int main()
{
    const int N = 5;
    Prod p[N];
    for (int i = 0; i < N; i++) cin >> p[i].nombre >> p[i].precio >> p[i].exist;
    int caro = 0;
    double total = 0;
    for (int i = 0; i < N; i++)
    {
        if (p[i].precio > p[caro].precio) caro = i;
        total += p[i].precio * p[i].exist;
    }
    cout << "Mas caro: " << p[caro].nombre << "\nInventario: $" << total << "\nPor surtir:";
    for (int i = 0; i < N; i++) if (p[i].exist < 10) cout << " " << p[i].nombre;
    cout << "\n";
    return 0;
}
```
:::
