---
num: "02"
archivo: "Tema02_Tipos_variables_constantes_ES"
titulo: "Tipos de datos, variables, constantes y entrada/salida"
corto: "Tipos, variables y E/S"
lema: "Cada dato necesita una caja del tamaño correcto: aprende a elegirla, a nombrarla y a llenarla desde el teclado."
duracion: "4 h · 2 sesiones de 2 h"
previos: "Tema 01 (estructura de un programa, `printf`, compilación)."
fuentes:
  - "Kernighan, B. W. y Ritchie, D. M. (1988). *The C Programming Language* (2.ª ed.). Prentice Hall. Cap. 1: §1.2 Variables and Arithmetic Expressions, §1.4 Symbolic Constants. Cap. 2: §2.1 Variable Names, §2.2 Data Types and Sizes, §2.3 Constants, §2.4 Declarations. Cap. 7: §7.2 Formatted Output—printf, §7.4 Formatted Input—Scanf."
  - "King, K. N. (2008). *C Programming: A Modern Approach* (2.ª ed.). W. W. Norton. Cap. 2: §2.4 Variables and Assignment, §2.5 Reading Input, §2.6 Defining Names for Constants, §2.7 Identifiers. Cap. 3 «Formatted Input/Output». Cap. 7 «Basic Types»."
  - "Seacord, R. C. (2020). *Effective C*. No Starch Press. Cap. 2 «Objects, Functions, and Types». Cap. 3 «Arithmetic Types»."
objetivos:
  A:
    - "Describir una variable por sus cuatro características: nombre, tipo, contenido y dirección de memoria."
    - "Elegir el tipo adecuado (`int`, `double`, `char`, `bool` o un arreglo de `char` para texto) para un dato del mundo real."
    - "Declarar, inicializar y asignar variables con identificadores válidos y significativos."
    - "Mostrar datos con `printf` y leerlos del teclado con `scanf`, usando el especificador de formato de cada tipo."
    - "Declarar constantes con `const` y `#define` y distinguirlas de las variables."
  B:
    - "Comparar tamaños y rangos de los tipos con `sizeof` y predecir desbordamiento y truncamiento."
    - "Explicar por qué `scanf` necesita la dirección (`&`) de cada variable y detectar con `-Wall` los especificadores que no coinciden con el tipo."
    - "Elegir entre `#define` y `const` y justificar la elección."
    - "Relacionar `char` con su código ASCII y resolver el problema del Enter pendiente con `\" %c\"` y `\" %[^\\n]\"`."
efectos:
  soporte:
    - ["Elementos aislados", "Nueve conceptos presentados uno a uno (variable → tipos → printf → declaración → identificadores → asignación → scanf → constantes → char/ASCII)."]
    - ["Atención dividida", "Diagramas de memoria integrados con el código que los produce; anotaciones junto a cada línea."]
    - ["Ejemplo resuelto", "Ficha de registro de un jugador: algoritmo → pseudocódigo → C → ejecución con datos."]
    - ["Movimiento humano", "Actividad «casilleros humanos»: los estudiantes representan variables y su contenido."]
  procedimental:
    - ["Variabilidad", "Errores frecuentes en contextos distintos (variables no declaradas, `scanf` sin `&`, conversiones con pérdida, Enter pendiente)."]
    - ["Redundancia", "La tarjeta de sintaxis resume sin repetir la teoría."]
    - ["Autoexplicación", "Cada error se presenta primero como pregunta «¿por qué ocurre?»."]
  tareas:
    - ["Ejemplo resuelto", "T1: registro de mascota resuelto + gemelo (registro de libro)."]
    - ["Problema por completar", "T2 con pistas, T3 sin pistas."]
    - ["Desvanecimiento de guía", "Secuencia T1 → T4."]
    - ["Solución libre", "T5: obtener toda la información posible de una variable `char`."]
    - ["Autoexplicación", "T6: explicar salidas sorprendentes (desbordamiento, truncamiento, ASCII)."]
    - ["Imaginación", "T7: imaginar el estado de la memoria línea por línea."]
    - ["Memoria colectiva de trabajo", "T8: diseñar en equipo la ficha de un personaje de videojuego."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Conceptos 1–9 con diagramas de cajas; tipos básicos `int`, `double`, `char`, `bool` y texto en arreglos de `char`."
    B: "Repaso rápido; profundizar en `sizeof`, rangos, conversiones con pérdida (`-Wconversion`), `#define` vs `const` y ASCII."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 en orden, con la tarjeta 2.1 a la vista; pares con Ruta B."
    B: "T3, T6, T7 autónomas; mentores en T8."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Credencial escolar (T4) que lee y muestra datos."
    B: "Explicación escrita de las salidas sorprendentes (T6) y diagrama de memoria (T7)."
  Entorno:
    comp: "Información procedimental"
    A: "IDE con depurador para observar el valor de las variables."
    B: "Terminal con `gcc -Wall -Wextra -Wconversion` para ver advertencias de formato y de conversión."
plan:
  - ["Apertura", "Soporte", "Analogía de los casilleros; pregunta «¿cómo guarda un juego tu puntuación?».", "10 min"]
  - ["Desarrollo 1", "Soporte", "Conceptos 1–6 y actividad de casilleros humanos.", "40 min"]
  - ["Desarrollo 2", "Soporte", "Conceptos 7–9 y ejemplo resuelto 1.2.", "30 min"]
  - ["Práctica guiada", "Tareas + procedimental", "Ruta A: T1 → T3. Ruta B: T3, T6, T7.", "60 min"]
  - ["Colaborativa", "Tareas", "T8 en equipos heterogéneos.", "30 min"]
  - ["Autónoma", "Tareas", "T4 (todos) y T5 (Ruta A).", "30 min"]
  - ["Cierre", "Protocolo + evaluación", "Protocolo verbal, recall y comprehension test, autorregistro.", "40 min"]
glosario:
  - ["variable", "variable", "Espacio de memoria con nombre y tipo cuyo contenido puede cambiar."]
  - ["tipo de dato", "data type", "Define qué valores puede guardar una variable y cuánta memoria ocupa."]
  - ["entero", "integer (`int`)", "Número sin parte decimal."]
  - ["punto flotante", "floating-point (`double`, `float`)", "Número con parte decimal."]
  - ["carácter", "character (`char`)", "Un solo símbolo; internamente, un número (código ASCII)."]
  - ["booleano", "Boolean (`bool`)", "Valor lógico: `true` o `false` (requiere `<stdbool.h>`)."]
  - ["cadena", "string", "Secuencia de caracteres terminada en `'\\0'`; en C se guarda en un arreglo de `char`."]
  - ["declaración", "declaration", "Sentencia que crea una variable indicando su tipo y nombre."]
  - ["inicialización", "initialization", "Dar valor a una variable en el momento de crearla."]
  - ["asignación", "assignment", "Guardar un nuevo valor en una variable existente con `=`."]
  - ["identificador", "identifier", "Nombre que el programador da a una variable, constante o función."]
  - ["palabra reservada", "keyword", "Palabra con significado especial en C (`int`, `return`…); no puede ser identificador."]
  - ["constante", "constant", "Valor con nombre que no puede cambiar (`const`, `#define`)."]
  - ["literal", "literal", "Valor escrito directamente en el código: `42`, `3.5`, `'a'`, `\"hola\"`."]
  - ["entrada estándar", "standard input", "`stdin`: canal por el que llegan los datos del teclado; `scanf` lee de él."]
  - ["especificador de formato", "format specifier", "Marca como `%d`, `%lf`, `%c` o `%s` que indica a `printf` y `scanf` el tipo del dato."]
  - ["dirección de memoria", "memory address", "Número que identifica el lugar de la memoria donde vive la variable; se obtiene con `&x`."]
  - ["conversión con pérdida", "narrowing conversion", "Conversión que puede perder información (p. ej., `double` → `int`)."]
  - ["desbordamiento", "overflow", "Resultado que no cabe en el rango del tipo."]
---

# 1. Información de soporte {.soporte}

:::analogia | Las variables son casilleros
Piensa en los casilleros (*lockers*) de tu escuela. Cada uno tiene **un número** que lo identifica, **una etiqueta** con el nombre de su dueño, **un tamaño** (en uno pequeño no cabe una guitarra) y **un contenido** que puede cambiar cada día.

Una **variable** es exactamente eso, pero en la memoria de la computadora: tiene una **dirección** (el número del casillero), un **nombre** (la etiqueta), un **tipo** (el tamaño y la forma de lo que cabe) y un **contenido** (el valor actual).
:::

:::pregunta
Cuando juegas un videojuego, tu puntuación, tu vida, tu nombre de usuario y si sigues vivo cambian todo el tiempo. **¿Crees que todos esos datos se guardan del mismo modo? ¿En qué se diferencian?**

{{lineas:2}}
:::

:::relevancia
Todo programa trabaja con datos: una app de banco guarda saldos con decimales, un juego guarda vidas enteras y nombres de texto, el microcontrolador de un sensor guarda lecturas. **Elegir mal el tipo** produce errores reales: dinero que pierde centavos, edades negativas o contadores que «dan la vuelta». En C, además, tú decides cuánta memoria ocupa cada dato. Hoy aprendes a elegir, nombrar y llenar cada caja correctamente. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | ¿Qué es una variable? Sus cuatro características | Elementos aislados, Atención dividida
Toda variable tiene **nombre**, **tipo**, **contenido** y **dirección**. El operador `&` («dirección de») permite ver dónde vive. Para mostrar el valor de una variable, `printf` usa un **especificador de formato** (como `%d`) en el lugar del texto donde debe aparecer; los verás en el concepto 3.

```c run
#include <stdio.h>
int main(void)
{
    int edad = 17;                                 //> Crea la caja `edad` (tipo int) con el valor 17
    printf("Contenido: %d\n", edad);               //> `%d` se reemplaza por el **contenido** de `edad`
    printf("Tamano: %zu bytes\n", sizeof(edad));   //> `sizeof` da el tamaño del **tipo** (se muestra con `%zu`)
    printf("Direccion: %p\n", (void *)&edad);      //> `&edad` da la **dirección** (cambia en cada ejecución)
    return 0;
}
```

```diagram mem
vars:
  - {name: edad, type: int, val: 17, addr: "0x7ffd...", note: "4 bytes"}
figcaption: "Figura 1. Las cuatro características de una variable: nombre (edad), tipo (int), contenido (17) y dirección."
```
:::

:::concepto | 2 | Los tipos fundamentales: qué cabe en cada caja | Elementos aislados
| Tipo | Guarda… | Ejemplos de literales | Tamaño típico | Especificador |
|---|---|---|---|---|
| `int` | números enteros | `17`, `-3`, `2026` | 4 bytes | `%d` |
| `long long` | enteros muy grandes | `8000000000LL` | 8 bytes | `%lld` |
| `double` | números con decimales (doble precisión) | `3.1416`, `-0.5`, `6.02e23` | 8 bytes | `%f` al mostrar, `%lf` al leer |
| `float` | decimales con menos precisión | `3.14f` | 4 bytes | `%f` |
| `char` | **un** carácter | `'A'`, `'7'`, `'\n'` | 1 byte | `%c` |
| `bool` | verdadero o falso (`#include <stdbool.h>`) | `true`, `false` | 1 byte | `%d` (muestra 1 o 0) |
| arreglo de `char` | texto (cadena) | `"Ana Lopez"` | 1 byte por letra + 1 | `%s` |

Observa: los caracteres van entre **comillas simples** (`'A'`) y los textos entre **comillas dobles** (`"Ana"`). C no tiene un tipo «texto»: una cadena se guarda en un **arreglo de `char`** que termina con el carácter nulo `'\0'`. Por ejemplo, `char nombre[40];` reserva lugar para 39 letras más ese `'\0'`. Lo estudiarás a fondo en el Tema 12.

```c run
#include <stdio.h>
#include <stdbool.h>
int main(void)
{
    printf("char:      %zu byte\n", sizeof(char));
    printf("bool:      %zu byte\n", sizeof(bool));
    printf("int:       %zu bytes\n", sizeof(int));
    printf("float:     %zu bytes\n", sizeof(float));
    printf("double:    %zu bytes\n", sizeof(double));
    printf("long long: %zu bytes\n", sizeof(long long));
    return 0;
}
```

```diagram bars
items: [[char, 1], [bool, 1], [int, 4], [float, 4], [double, 8], ["long long", 8]]
unit: bytes
figcaption: "Figura 2. Tamaño de cada tipo en este compilador (gcc de 64 bits)."
```
:::

:::concepto | 3 | Mostrar variables con `printf`: los especificadores de formato | Elementos aislados, Atención dividida
Dentro de las comillas de `printf` escribes un **especificador** (empieza con `%`) donde quieres que aparezca cada dato; después de las comillas, separadas por comas, van las variables **en el mismo orden**.

```c run
#include <stdio.h>
int main(void)
{
    int goles = 3;
    double promedio = 1.5;
    char equipo = 'A';
    printf("Goles: %d\n", goles);                  //> `%d` se reemplaza por el valor de `goles`
    printf("Promedio: %f\n", promedio);            //> `%f` muestra un `double` con 6 decimales
    printf("Promedio: %.2f\n", promedio);          //> `%.2f` = exactamente 2 decimales
    printf("Equipo %c: %d goles, %.1f por partido\n",
           equipo, goles, promedio);               //> Varios datos: uno por especificador, en orden
    printf("Efectividad: 75%%\n");                 //> `%%` muestra el símbolo %
    return 0;
}
```
:::

:::concepto | 4 | Declarar e inicializar | Elementos aislados, Atención dividida
**Declarar** es crear la caja; **inicializar** es ponerle su primer valor en el mismo momento.

```c run
#include <stdio.h>
#include <stdbool.h>                 //> Necesaria para `bool`, `true` y `false`
int main(void)
{
    int vidas = 3;                   //> Declaración + inicialización con `=`
    double velocidad = 2.5;
    char inicial = 'M';              //> `char` usa comillas simples
    bool vivo = true;                //> `bool` solo admite `true` o `false`
    char jugador[20] = "Mia";        //> Texto: arreglo de 20 `char`, con comillas dobles
    printf("%s (%c) vidas=%d vel=%.1f vivo=%d\n",
           jugador, inicial, vidas, velocidad, vivo);   //> `vivo` se muestra como 1 (true) o 0 (false)
    return 0;
}
```

:::cuidado | Una variable sin inicializar contiene «basura»
`int puntos;` crea la caja pero **no** la limpia: contiene lo que haya quedado en esa memoria. Inicializa siempre: `int puntos = 0;`.
:::
:::

:::concepto | 5 | Identificadores: cómo nombrar las cajas | Elementos aislados
**Reglas** (obligatorias): solo letras, dígitos y guion bajo `_`; no pueden empezar con dígito; no pueden ser palabras reservadas (`int`, `return`, `while`…); C distingue mayúsculas (`Total` ≠ `total`).
**Buenas prácticas**: nombres que digan qué guardan (`precioUnitario` o `precio_unitario`, no `x1`), sin acentos ni ñ.

| Identificador | ¿Válido? | Motivo |
|---|---|---|
| `edad` | ✔ | letras |
| `nota_final` | ✔ | guion bajo permitido |
| `promedio2` | ✔ | el dígito no está al inicio |
| `2promedio` | ✘ | empieza con dígito |
| `nota final` | ✘ | contiene espacio |
| `return` | ✘ | palabra reservada |
| `año` | ✘ (evítalo) | la ñ y los acentos no son portables |
:::

:::concepto | 6 | Asignación: cambiar el contenido | Elementos aislados, Atención dividida
El operador `=` **no** significa «igual» como en matemáticas: significa «**guarda** el valor de la derecha en la caja de la izquierda». El valor anterior se pierde.

```c run
#include <stdio.h>
int main(void)
{
    int puntos = 10;           //> puntos ← 10
    puntos = 25;               //> puntos ← 25 (el 10 se pierde)
    int bonus = puntos;        //> bonus ← copia del contenido de puntos (25)
    puntos = 0;                //> Cambiar puntos NO cambia bonus
    printf("puntos=%d bonus=%d\n", puntos, bonus);
    return 0;
}
```

```diagram mem
vars:
  - {name: puntos, type: int, val: "10 → 25 → 0", hl: true}
  - {name: bonus, type: int, val: "25", note: "copia independiente"}
figcaption: "Figura 3. Cada asignación sobrescribe el contenido; bonus guarda una copia."
```
:::

:::concepto | 7 | Entrada de datos con `scanf` | Elementos aislados, Atención dividida
`scanf` lee datos del teclado. Usa los mismos especificadores que `printf`, con dos diferencias: para `double` se escribe **`%lf`**, y antes de cada variable va **`&`** (la dirección del concepto 1): `scanf` necesita saber **en qué caja** guardar el dato. **Siempre** muestra antes un mensaje que diga qué escribir.

```c run stdin="Luis\n16 1.72\n"
#include <stdio.h>
int main(void)
{
    char nombre[20];
    int edad;
    double estatura;
    printf("Nombre: ");
    scanf("%19s", nombre);                 //> `%s` lee UNA palabra (se detiene en el espacio); el arreglo no lleva `&`
    printf("Edad y estatura: ");
    scanf("%d %lf", &edad, &estatura);     //> Dos datos: `&` antes de cada variable y `%lf` para double
    printf("%s tiene %d anios y mide %.2f m\n", nombre, edad, estatura);
    return 0;
}
```

El `19` de `%19s` limita la palabra a 19 letras: el arreglo tiene 20 lugares y el último es para `'\0'`. Así el texto nunca se sale de su caja. Los arreglos no llevan `&` porque su nombre ya indica dónde empiezan en memoria (Tema 08).

Para leer un **texto con espacios** (nombre completo, dirección) usa `%[^\n]` («todo lo que no sea Enter»), con un **espacio antes del `%`**:

```c run stdin="Ana Sofia Lopez\n"
#include <stdio.h>
int main(void)
{
    char completo[40];
    printf("Nombre completo: ");
    scanf(" %39[^\n]", completo);      //> Lee toda la línea, con espacios, hasta el Enter (máx. 39 letras)
    printf("Hola, %s\n", completo);
    return 0;
}
```

El espacio inicial le pide a `scanf` que salte los espacios y Enters pendientes antes de leer (verás por qué importa en los errores frecuentes 2.3). En el Tema 12 conocerás también `fgets`.
:::

:::concepto | 8 | Constantes: valores que no deben cambiar | Elementos aislados
Hay valores que nunca cambian (π, el IVA, el número de días de la semana). Darles nombre evita «números mágicos» y errores.

```c run
#include <stdio.h>
#define PI_MACRO 3.1416          //> Constante **simbólica**: el preprocesador la sustituye antes de compilar
#define DIAS_SEMANA 7            //> Sin `=` y sin `;`
const double PI = 3.14159265;    //> Constante con tipo: el compilador la verifica
int main(void)
{
    double radio = 2.0;
    printf("Area (macro): %.4f\n", PI_MACRO * radio * radio);
    printf("Area (const): %.4f\n", PI * radio * radio);
    printf("Dias: %d\n", DIAS_SEMANA);
    // PI = 3;  // ERROR: no se puede asignar a una constante
    return 0;
}
```

Un **literal** es el valor escrito tal cual (`3.1416`); una **constante simbólica** es un nombre para ese valor (`PI`). Por convención, las constantes se escriben en MAYÚSCULAS. En C usarás mucho `#define` para los tamaños de los arreglos (Tema 08).
:::

:::concepto | 9 | `char`, el código ASCII y las secuencias de escape | Elementos aislados, Atención dividida
Un `char` guarda en realidad un **número pequeño**: su código en la tabla ASCII. `'A'` es 65, `'a'` es 97, `'0'` es 48. Por eso el mismo `char` se puede mostrar como letra (`%c`) o como número (`%d`).

```c run
#include <stdio.h>
int main(void)
{
    char letra = 'A';
    printf("%c tiene codigo %d\n", letra, letra);         //> El mismo dato: con `%c` la letra, con `%d` su código
    char siguiente = letra + 1;                            //> 65 + 1 = 66, que es 'B'
    printf("Siguiente: %c\n", siguiente);
    printf("Comillas: \" y apostrofo: \' y barra: \\\n");  //> Secuencias de escape
    return 0;
}
```

| Secuencia | Significado | Secuencia | Significado |
|---|---|---|---|
| `\n` | nueva línea | `\"` | comilla doble |
| `\t` | tabulador | `\'` | comilla simple |
| `\\` | barra invertida | `\0` | carácter nulo (fin de cadena) |
| `\a` | pitido | `\r` | retorno de carro |
:::

:::movimiento | Casilleros humanos (10 min)
Cinco estudiantes pasan al frente con una hoja: arriba escriben un **nombre de variable** y su **tipo**, al reverso pegan un número de «dirección». El instructor dicta sentencias (`int vidas = 3;`, `vidas = vidas - 1;`, `char c = 'B';`, `c = c + 1;`, `scanf("%d", &vidas);`) y cada «casillero» borra y escribe su contenido; para `scanf`, el instructor entrega el dato a quien tenga la **dirección** indicada. El grupo verifica: ¿cabe ese valor en ese tipo? ¿Quién cambió y quién no?
:::

## 1.2 Ejemplo resuelto: ficha de registro de un jugador

:::ejemplo | Ficha de registro de un jugador | Ejemplo resuelto, Atención dividida
**Problema.** Un torneo escolar de videojuegos necesita registrar a cada jugador: nombre completo, edad, promedio de puntos por partida y la letra de su categoría (A, B o C). Al final se muestra la ficha.

**A. Algoritmo**

1. Pedir y leer el nombre completo (puede tener espacios → `" %[^\n]"`).
2. Pedir y leer la edad (entero), el promedio (decimal) y la categoría (un carácter).
3. Mostrar la ficha con etiquetas alineadas.

**B. Pseudocódigo**

```pseudo
Algoritmo FichaJugador
    Definir nombre Como Cadena
    Definir edad Como Entero
    Definir promedio Como Real
    Definir categoria Como Caracter
    Escribir "Nombre completo: "
    Leer nombre
    Escribir "Edad, promedio y categoria: "
    Leer edad, promedio, categoria
    Escribir "Jugador: ", nombre
    Escribir "Edad: ", edad, "  Promedio: ", promedio, "  Categoria: ", categoria
FinAlgoritmo
```

**C. Código en C**

```c run title="ficha_jugador.c" stdin="Diego Ramirez Soto\n15 87.5 B\n"
#include <stdio.h>
int main(void)
{
    char nombre[50];                        //> Texto con espacios: arreglo de char
    int edad;                               //> Entero: no hay edades con decimales
    double promedio;                        //> Decimal: 87.5 puntos
    char categoria;                         //> Una sola letra
    printf("Nombre completo: ");
    scanf(" %49[^\n]", nombre);             //> Paso 1: `%[^\n]` porque el nombre tiene espacios
    printf("Edad, promedio y categoria: ");
    scanf("%d %lf %c", &edad, &promedio, &categoria);   //> Paso 2: tres datos con un solo `scanf`
    printf("\n--- FICHA DEL JUGADOR ---\n"); //> Paso 3: mostrar
    printf("Jugador:\t%s\n", nombre);
    printf("Edad:\t\t%d\n", edad);
    printf("Promedio:\t%.1f\n", promedio);
    printf("Categoria:\t%c\n", categoria);
    return 0;
}
```

**D. Verificación.** Con la entrada `Diego Ramirez Soto`, `15 87.5 B` la ficha muestra los cuatro datos con el tipo correcto: el nombre completo (gracias a `%[^\n]`), la edad entera y el promedio con decimales. El espacio antes de `%c` en `"%d %lf %c"` hace que la categoría no sea el espacio que separa los datos.
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.2; ranksep=0.35;
@term(v, "Variable")
@proc(n, "nombre\n(identificador)")
@proc(t, "tipo\nint · double · char\nbool · char[ ]")
@proc(c, "contenido\n(se asigna con =)")
@proc(d, "dirección\n(&variable)")
v -> n; v -> t; v -> c; v -> d;
@io(e, "scanf(\"%d\", &x)")
@io(s, "printf(\"%d\", x)")
@sub(k, "constantes\nconst · #define")
c -> e [dir=back, label="llenar"]; c -> s [label="mostrar"]; t -> k [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

Consulta esta sección **mientras** resuelves las tareas.

:::sintaxis | Tarjeta de sintaxis 2.1
| Quiero… | Escribo |
|---|---|
| Declarar e inicializar | `int edad = 17;` · `double precio = 25.5;` · `char letra = 'A';` · `bool listo = false;` · `char nombre[30] = "Ana";` |
| Asignar un valor nuevo | `edad = 18;` |
| Mostrar un dato | `printf("Edad: %d\n", edad);` |
| Mostrar con 2 decimales | `printf("%.2f\n", precio);` |
| Leer un número | `scanf("%d", &edad);` · `scanf("%lf", &precio);` |
| Leer varios datos | `scanf("%d %lf", &edad, &precio);` |
| Leer un carácter (tras otra lectura) | `scanf(" %c", &letra);` (con espacio antes de `%c`) |
| Leer una palabra | `scanf("%29s", nombre);` (sin `&`; 29 = tamaño − 1) |
| Leer una línea con espacios | `scanf(" %29[^\n]", nombre);` |
| Constante | `const double IVA = 0.16;` · `#define IVA 0.16` |
| Tamaño de un tipo | `printf("%zu", sizeof(int));` |
| Código ASCII de un `char` | `printf("%d", letra);` |
| Cabeceras | `<stdio.h>` para `printf`/`scanf`, `<stdbool.h>` para `bool` |

**Especificadores:** `%d` int · `%lld` long long · `%f` double al mostrar, `%lf` al leer · `%c` char · `%s` cadena · `%zu` sizeof · `%%` el símbolo %.

**¿Qué tipo elijo?** ¿Puede tener decimales? → `double`. ¿Es un conteo o una cantidad entera? → `int`. ¿Es un solo símbolo? → `char`. ¿Es sí/no? → `bool` (o un `int` 1/0 si lo lees con `scanf`). ¿Es texto? → arreglo de `char`.
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿El tipo de cada variable corresponde a la naturaleza del dato (entero, decimal, carácter, lógico, texto)?</li>
<li>¿Inicialicé todas las variables antes de usarlas?</li>
<li>¿Los nombres dicen qué guardan, sin espacios, acentos ni ñ?</li>
<li>¿Mostré un mensaje (<code>printf</code>) antes de cada lectura (<code>scanf</code>)?</li>
<li>¿Cada especificador coincide con el tipo de su variable (<code>%d</code> int, <code>%lf</code> double en <code>scanf</code>, <code>%c</code> char, <code>%s</code> texto)?</li>
<li>¿Puse <code>&amp;</code> antes de cada variable en <code>scanf</code> (excepto en los arreglos de <code>char</code>)?</li>
<li>¿El texto tiene espacios? Entonces <code>" %[^\n]"</code>. ¿Leo un <code>char</code> después de otro dato? Entonces <code>" %c"</code>.</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Usar una variable que no se declaró.** ¿Por qué el compilador no conoce `total`?

```c err
#include <stdio.h>
int main(void)
{
    total = 5;
    printf("%d\n", total);
    return 0;
}
```
*Corrección:* declarar antes de usar: `int total = 5;`.

**b) Olvidar el `&` en `scanf`.** El programa **compila** (gcc solo advierte), pero al ejecutarse `scanf` guarda el dato en una dirección cualquiera y el programa puede terminar de golpe. ¿Qué recibe `scanf` en lugar de la dirección?

```c warn
#include <stdio.h>
int main(void)
{
    int edad = 0;
    printf("Edad: ");
    scanf("%d", edad);
    printf("Tienes %d anios\n", edad);
    return 0;
}
```
*Corrección:* `scanf("%d", &edad);` — sin `&`, `scanf` recibe el **contenido** (0) en lugar de la **dirección**. Compila siempre con `-Wall` y trata cada advertencia como un error.

**c) Conversión con pérdida.** ¿Qué dato se perdería?

```c warn flags="-Wconversion"
#include <stdio.h>
int main(void)
{
    int precio = 19.99;
    printf("%d\n", precio);
    return 0;
}
```
*Corrección:* usar `double precio = 19.99;`. El programa compila y guarda **19**: la parte decimal se pierde en silencio. Solo la opción `-Wconversion` te avisa, como en este mensaje.

**d) El `char` que «se salta».** El usuario escribe `20` ⏎ y luego `S`, pero el programa no espera la respuesta:

```c run stdin="20\nS\n"
#include <stdio.h>
int main(void)
{
    int edad;
    char beca;
    printf("Edad: ");
    scanf("%d", &edad);           //> `%d` lee 20 pero deja el Enter (`\n`) pendiente
    printf("Tienes beca (S/N)? ");
    scanf("%c", &beca);           //> `%c` toma ese Enter como si fuera la respuesta
    printf("[%c] codigo %d\n", beca, beca);
    return 0;
}
```
*Corrección:* `scanf(" %c", &beca);` — el espacio antes de `%c` descarta el Enter pendiente. Lo mismo ocurre con `%[^\n]`: por eso se escribe `" %[^\n]"`.

**e) Variable sin inicializar.** Compila, pero con `-Wall` gcc advierte; el resultado es impredecible (basura).

```c warn
#include <stdio.h>
int main(void)
{
    int suma;
    suma = suma + 5;
    printf("%d\n", suma);
    return 0;
}
```
*Corrección:* inicializa siempre: `int suma = 0;`.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Mismo patrón, otro contexto | Variabilidad
Leer → guardar en el tipo correcto → mostrar. Ahora con un producto de una tienda en línea:

```c run title="producto.c" stdin="Audifonos inalambricos\n649.90 12\n"
#include <stdio.h>
#define IVA 0.16                  //> Constante con nombre
int main(void)
{
    char producto[40];            //> Texto con espacios → `%[^\n]`
    double precio;                //> Dinero → decimal
    int existencias;              //> Piezas → entero
    printf("Producto: ");
    scanf(" %39[^\n]", producto);
    printf("Precio y existencias: ");
    scanf("%lf %d", &precio, &existencias);
    printf("%s | $%.2f + IVA $%.2f | %d piezas\n",
           producto, precio, precio * IVA, existencias);
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

Resuélvelas en orden; la ayuda disminuye en cada una. {{ef:Desvanecimiento de guía}}

:::tarea A | T1. Registro en la veterinaria: estudia el ejemplo y resuelve su gemelo | 20 min | Ejemplo resuelto, Variabilidad
**Contexto.** Una veterinaria registra a cada mascota que llega. **¿Para qué?** Leer datos de distintos tipos y mostrarlos es la base de cualquier sistema de registro.

**Paso 1 · Estudia:**

```c run title="registro_mascota.c" stdin="Firulais\n4 12.5 S\n"
#include <stdio.h>
int main(void)
{
    char nombre[20];        //> Una palabra → `%19s` basta
    int edad;               //> Años completos → entero
    double peso;            //> Kilogramos con decimales → double
    char vacunado;          //> 'S' o 'N' → char
    printf("Nombre de la mascota: ");
    scanf("%19s", nombre);
    printf("Edad, peso y vacunado (S/N): ");
    scanf("%d %lf %c", &edad, &peso, &vacunado);   //> `&` en cada variable; `%lf` para el double
    printf("\nMascota: %s\nEdad: %d anios\nPeso: %.1f kg\nVacunado: %c\n",
           nombre, edad, peso, vacunado);
    return 0;
}
```

**Paso 2 · Ahora tú (gemelo).** Escribe `registro_libro.c` para una biblioteca: **título** (con espacios), **año de publicación**, **precio** y **sección** (una letra). Muestra la ficha.

:::solucion | T1
```c run title="registro_libro.c" stdin="Cien anios de soledad\n1967 289.50 L\n"
#include <stdio.h>
int main(void)
{
    char titulo[60];
    int anio;
    double precio;
    char seccion;
    printf("Titulo: ");
    scanf(" %59[^\n]", titulo);          // el titulo tiene espacios
    printf("Anio, precio y seccion: ");
    scanf("%d %lf %c", &anio, &precio, &seccion);
    printf("\nLibro: %s\nAnio: %d\nPrecio: $%.2f\nSeccion: %c\n",
           titulo, anio, precio, seccion);
    return 0;
}
```
:::
:::

:::tarea A | T2. Perfil de videojuego (completa con pistas) | 20 min | Problema por completar
**Contexto.** Un juego guarda el perfil del jugador. **¿Para qué?** Elegir el tipo y el especificador correctos evita que la vida pierda sus decimales o que el dato se guarde donde no debe. Como `scanf` no tiene especificador para `bool`, el dato «premium» se lee como `int` (1 = sí, 0 = no).

```c blank title="perfil.c"
#include <stdio.h>
int main(void)
{
    __1__ usuario[20];                      // 1: tipo de cada letra del texto
    int nivel;
    __2__ vida;                             // 2: tipo para 87.5 puntos de vida
    int premium;                            // 1 = si, 0 = no
    printf("Usuario, nivel, vida y premium (1/0): ");
    scanf("%19s %d __3__ %d", usuario, __4__nivel, &vida, &premium);  // 3: especificador para leer vida; 4: «direccion de»
    printf("%s | nivel %d | vida __5__ | premium %d\n",
           usuario, nivel, vida, premium);  // 5: vida con un decimal
    return 0;
}
```

**Prueba con:** `dragon77 12 87.5 1`

:::solucion | T2
{{c:1}} `char` · {{c:2}} `double` · {{c:3}} `%lf` · {{c:4}} `&` · {{c:5}} `%.1f`

```c run title="perfil.c" stdin="dragon77 12 87.5 1\n"
#include <stdio.h>
int main(void)
{
    char usuario[20];
    int nivel;
    double vida;
    int premium;
    printf("Usuario, nivel, vida y premium (1/0): ");
    scanf("%19s %d %lf %d", usuario, &nivel, &vida, &premium);
    printf("%s | nivel %d | vida %.1f | premium %d\n",
           usuario, nivel, vida, premium);
    return 0;
}
```
:::
:::

:::tarea AB | T3. Alta de un producto (completa sin pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Una papelería da de alta productos con nombre (con espacios), precio, existencias y una constante de descuento del 10 %.

```c blank title="alta_producto.c"
#include <stdio.h>
__1__ DESCUENTO 0.10
int main(void)
{
    char nombre[40];
    __2__ precio;
    __3__ existencias;
    printf("Nombre del producto: ");
    scanf(" %39__4__", nombre);
    printf("Precio y existencias: ");
    scanf("%lf %d", __5__precio, &existencias);
    printf("%s: $%.2f (con descuento $%.2f), %d piezas\n",
           nombre, precio, precio - precio * __6__, existencias);
    return 0;
}
```

**Prueba con:** `Cuaderno profesional` · `45 30`

:::solucion | T3
{{c:1}} `#define` · {{c:2}} `double` · {{c:3}} `int` · {{c:4}} `[^\n]` · {{c:5}} `&` · {{c:6}} `DESCUENTO`

```c run title="alta_producto.c" stdin="Cuaderno profesional\n45 30\n"
#include <stdio.h>
#define DESCUENTO 0.10
int main(void)
{
    char nombre[40];
    double precio;
    int existencias;
    printf("Nombre del producto: ");
    scanf(" %39[^\n]", nombre);
    printf("Precio y existencias: ");
    scanf("%lf %d", &precio, &existencias);
    printf("%s: $%.2f (con descuento $%.2f), %d piezas\n",
           nombre, precio, precio - precio * DESCUENTO, existencias);
    return 0;
}
```
:::
:::

:::tarea AB | T4. Credencial escolar (problema convencional) | 30 min | Variabilidad
**Contexto.** Control escolar imprime credenciales. **Requisitos:** leer nombre completo, número de control (entero), grupo (una letra), semestre (entero) y promedio (decimal); declarar una constante con el nombre de la escuela; mostrar la credencial con bordes y datos alineados. Elige y justifica cada tipo en un comentario.

**Ejemplo de ejecución** (entrada: `Valeria Torres Gil` · `20261045 B 3 9.2`):

```console title="Salida esperada (aproximada)"
=================================
 ESCUELA PREPARATORIA TECNICA
=================================
Alumno:     Valeria Torres Gil
Control:    20261045
Grupo:      B     Semestre: 3
Promedio:   9.2
=================================
```

:::solucion | T4
```c run title="credencial.c" stdin="Valeria Torres Gil\n20261045 B 3 9.2\n"
#include <stdio.h>
#define ESCUELA "ESCUELA PREPARATORIA TECNICA"   // no cambia
int main(void)
{
    char nombre[50];    // texto con espacios
    int control;        // numero entero sin decimales
    char grupo;         // una sola letra
    int semestre;       // conteo entero
    double promedio;    // puede tener decimales
    printf("Nombre completo: ");
    scanf(" %49[^\n]", nombre);
    printf("Control, grupo, semestre y promedio: ");
    scanf("%d %c %d %lf", &control, &grupo, &semestre, &promedio);
    printf("\n=================================\n");
    printf(" %s\n", ESCUELA);
    printf("=================================\n");
    printf("Alumno:\t\t%s\n", nombre);
    printf("Control:\t%d\n", control);
    printf("Grupo:\t\t%c\tSemestre: %d\n", grupo, semestre);
    printf("Promedio:\t%.1f\n", promedio);
    printf("=================================\n");
    return 0;
}
```
:::
:::

:::tarea A | T5. Todo lo que puedas saber de una letra (solución libre) | 15 min | Solución libre
**Contexto.** Tienes la variable `char letra = 'G';`. **No hay una pregunta única:** escribe un programa que muestre **toda la información que puedas obtener** de esa variable con lo que sabes hoy (su código ASCII, la letra anterior y la siguiente, su tamaño en memoria, su dirección, su minúscula sabiendo que la distancia entre `'A'` y `'a'` es 32…). Cuantos más datos descubras, mejor.

:::solucion | T5
Una exploración posible (hay muchas otras válidas):

```c run title="explora_letra.c"
#include <stdio.h>
int main(void)
{
    char letra = 'G';
    printf("Letra: %c\n", letra);
    printf("Codigo ASCII: %d\n", letra);
    printf("Anterior: %c  Siguiente: %c\n", letra - 1, letra + 1);
    printf("Minuscula: %c\n", letra + 32);
    printf("Posicion en el alfabeto: %d\n", letra - 'A' + 1);
    printf("Tamano: %zu byte\n", sizeof(letra));
    return 0;
}
```
:::
:::

:::tarea B | T6. Salidas sorprendentes (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
**Contexto.** Un compañero ejecutó este programa y no entiende las líneas 2, 3 y 4 de la salida. **Explica con tus palabras** por qué ocurre cada una.

```c run title="sorpresas.c"
#include <stdio.h>
int main(void)
{
    short pequeno = 32767;       // valor maximo de short
    pequeno = pequeno + 1;
    int dividido = 7.9;          // compila sin avisos con -Wall, pero...
    char c = 'a' + 2;
    printf("sizeof(short) = %zu\n", sizeof(short));
    printf("pequeno = %d\n", pequeno);
    printf("dividido = %d\n", dividido);
    printf("c = %c (%d)\n", c, c);
    return 0;
}
```

{{lineas:4}}

:::solucion | T6
- **`pequeno = -32768`**: un `short` ocupa 2 bytes y su máximo es 32767. Al sumar 1 el resultado no cabe (**desbordamiento**) y el valor «da la vuelta» al mínimo del rango.
- **`dividido = 7`**: asignar un `double` a un `int` **trunca** (elimina) la parte decimal; no redondea. Con `gcc -Wconversion` el compilador te habría avisado de esta conversión y de la anterior.
- **`c = c (99)`**: `'a'` vale 97 en ASCII; 97 + 2 = 99, que corresponde a la letra `c`.
:::
:::

:::tarea B | T7. Imagina la memoria (imaginación) | 15 min | Imaginación
**Sin ejecutar** el programa, imagina las cajas de memoria y **dibuja su contenido después de cada línea** (como en la Figura 3). Luego ejecútalo para comprobar la salida final.

```c check title="imagina.c"
#include <stdio.h>
int main(void)
{
    int a = 4;
    int b = a * 2;
    a = b - 1;
    b = a + b;
    char inicial = 'K';
    inicial = inicial + 2;
    printf("%d %d %c\n", a, b, inicial);
    return 0;
}
```

{{lineas:3}}

:::solucion | T7
| Después de la línea | `a` | `b` | `inicial` |
|---|---|---|---|
| 4 | 4 | — | — |
| 5 | 4 | 8 | — |
| 6 | 7 | 8 | — |
| 7 | 7 | 15 | — |
| 8 | 7 | 15 | `'K'` |
| 9 | 7 | 15 | `'M'` |

```c run title="imagina.c"
#include <stdio.h>
int main(void)
{
    int a = 4;
    int b = a * 2;
    a = b - 1;
    b = a + b;
    char inicial = 'K';
    inicial = inicial + 2;
    printf("%d %d %c\n", a, b, inicial);
    return 0;
}
```
:::
:::

:::tarea AB | T8. La ficha de un personaje (reto colaborativo) | 35 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Equipos de 3–4 integrantes **con niveles mezclados**. Cada integrante se encarga de un grupo de datos y lo explica a los demás antes de integrarlo.
:::

**Contexto.** Su equipo diseña un juego de rol y necesita la ficha de un personaje.

1. **Integrante 1:** identidad (nombre con espacios, clase como letra: G=guerrero, M=mago, A=arquero).
2. **Integrante 2:** estadísticas (nivel, fuerza, agilidad → enteros; vida y maná → decimales).
3. **Integrante 3:** estado (¿vivo? ¿tiene montura? → enteros 1/0, porque `scanf` no lee `bool`) y constantes del juego (`NIVEL_MAXIMO = 99`).
4. **Todos:** integran el programa que lee los datos y muestra la ficha; justifican cada tipo y cada especificador en un comentario y presentan su diseño a otro equipo.

:::solucion | T8
Una solución posible:

```c run title="personaje.c" stdin="Lyra Vientoalto\nM 7 5 9 64.5 120.0 1 0\n"
#include <stdio.h>
#define NIVEL_MAXIMO 99                   // regla fija del juego
int main(void)
{
    char nombre[40];                      // texto con espacios
    char clase;                           // G, M o A
    int nivel, fuerza, agilidad;          // valores enteros
    double vida, mana;                    // pueden tener decimales
    int vivo, montura;                    // 1 = si, 0 = no
    printf("Nombre: ");
    scanf(" %39[^\n]", nombre);
    printf("Clase nivel fuerza agilidad vida mana vivo montura: ");
    scanf(" %c %d %d %d %lf %lf %d %d", &clase, &nivel, &fuerza, &agilidad,
          &vida, &mana, &vivo, &montura);
    printf("\n== %s [%c] ==\n", nombre, clase);
    printf("Nivel %d/%d\n", nivel, NIVEL_MAXIMO);
    printf("Fuerza %d  Agilidad %d\n", fuerza, agilidad);
    printf("Vida %.1f  Mana %.1f\n", vida, mana);
    printf("Vivo: %d  Montura: %d\n", vivo, montura);
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Un experto programa un formulario de inscripción | Modalidad, Ejemplo resuelto
*Guion para narrar en 4 segmentos breves (≈ 3 min en total), mostrando el código en pantalla. El estudiante controla el ritmo (pausar/repetir) para evitar el efecto de información transitoria.*

**Problema:** «Inscribir a un participante a un torneo de ajedrez: nombre completo, edad, rating (puede tener decimales) y si es socio del club».

**Segmento 1 — Tipos primero.** {{como}} Antes de escribir código hago una lista de datos y les pongo tipo y especificador: nombre → arreglo de `char` con `%s`; edad → `int` con `%d`; rating → `double` con `%lf` al leer y `%.1f` al mostrar; socio → `int` 1/0 con `%d`, porque `scanf` no lee `bool`. {{porque}} El tipo decide qué valores son válidos y cuánta memoria uso; y en C el especificador **tiene** que coincidir con el tipo, o el dato se guarda mal.

**Segmento 2 — Leer sin tropezar con el Enter.** {{como}} Para el nombre uso `scanf(" %49[^\n]", nombre)` y para los números `scanf("%d %lf %d", &edad, &rating, &socio)`, con `&` delante de cada variable. {{porque}} El espacio inicial descarta cualquier Enter pendiente y `%[^\n]` toma la línea completa; sin `&`, `scanf` no sabría en qué caja guardar cada número.

**Segmento 3 — Mensajes claros.** {{como}} Antes de cada lectura escribo qué debe teclear el usuario, incluso el formato: «socio (1 = si, 0 = no)». {{porque}} El usuario no ve mis variables; si no sabe qué escribir, mete un texto donde va un número y `scanf` falla.

**Segmento 4 — Probar con datos reales.** {{como}} Compilo con `-Wall`, que revisa que cada especificador coincida con su variable; pruebo con `Ana Paula Ríos`, `16`, `1450.5`, `1` y reviso que cada dato aparezca igual que lo escribí. {{porque}} Probar con un nombre de varias palabras y un decimal confirma justamente las decisiones que tomé.

```c run title="inscripcion.c" stdin="Ana Paula Rios\n16 1450.5 1\n"
#include <stdio.h>
int main(void)
{
    char nombre[50];
    int edad;
    double rating;
    int socio;
    printf("Nombre completo: ");
    scanf(" %49[^\n]", nombre);
    printf("Edad, rating y socio (1 = si, 0 = no): ");
    scanf("%d %lf %d", &edad, &rating, &socio);
    printf("Inscrito: %s (%d anios), rating %.1f, socio: %d\n",
           nombre, edad, rating, socio);
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. Menciona las cuatro características de toda variable.
2. ¿Qué tipo usarías para guardar la temperatura de una ciudad (por ejemplo, 23.7 °C)?
   a) `int` · b) `char` · c) `double` · d) `bool`
3. ¿Cuál de estos identificadores es **inválido**? a) `total_2` · b) `_contador` · c) `3lugar` · d) `precioFinal`
4. ¿Qué diferencia hay entre `'A'` y `"A"`?
5. Verdadero o falso: `x = 5;` significa que `x` y `5` son iguales para siempre.
6. ¿Por qué en `scanf("%d", &edad);` se escribe `&` antes de `edad`?
7. Escribe la sentencia que lee un `double` llamado `precio` y la que lo muestra con dos decimales.
8. ¿Qué palabra hace que una variable no pueda modificarse? ¿Qué directiva del preprocesador también define constantes?
9. ¿Cuántos bytes ocupa normalmente un `char`? ¿Y un `double`? ¿Qué código ASCII tiene `'A'`?
10. ¿Qué secuencia de escape muestra una comilla doble dentro de un texto? ¿Cómo muestra `printf` el símbolo `%`?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida:**

```c check title="p1.c"
#include <stdio.h>
int main(void)
{
    int x = 3;
    int y = x + 4;
    x = y * 2;
    char c = 'D';
    c = c - 1;
    printf("%d %d %c\n", x, y, c);
    return 0;
}
```

**P2. Corrige** los errores (hay cuatro) y explica cada uno:

```c blank title="p2.c"
#include <stdio.h>
int main(void)
{
    int 2edad;
    double promedio = "8.5";
    int grupo;
    scanf("%d", grupo);
    printf("Promedio: %d\n", promedio);
    return 0;
}
```

**P3. Elige el tipo** para cada dato y justifica: número de hermanos, precio de un boleto, respuesta a «¿tienes beca?», grupo escolar (letra), correo electrónico, población de México.

**P4. Escribe un programa** que lea el nombre completo de una persona, su peso (kg) y su estatura (m), y muestre los tres datos con etiquetas. Declara una constante con el nombre de la clínica.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Elijo el tipo correcto para cada dato y lo justifico.</li>
<li>Declaro, inicializo y asigno variables sin errores.</li>
<li>Uso el especificador correcto en <code>printf</code> y en <code>scanf</code>, y no olvido el <code>&amp;</code>.</li>
<li>Leo palabras con <code>%s</code> y textos con espacios con <code>" %[^\n]"</code>.</li>
<li>Uso constantes con nombre en lugar de números mágicos.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 Nombre, tipo, contenido y dirección de memoria · 2 c · 3 c (empieza con dígito) · 4 `'A'` es un `char` (un carácter); `"A"` es una cadena: un arreglo con `'A'` y `'\0'` · 5 Falso: `=` asigna (guarda) el valor; `x` puede cambiar después · 6 Porque `scanf` necesita la **dirección** de la variable para guardar ahí el dato; sin `&` recibiría su contenido · 7 `scanf("%lf", &precio);` y `printf("%.2f\n", precio);` · 8 `const`; `#define` · 9 1 byte y 8 bytes; 65 · 10 `\"`; con `%%`
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.**

```c run title="p1.c"
#include <stdio.h>
int main(void)
{
    int x = 3;
    int y = x + 4;
    x = y * 2;
    char c = 'D';
    c = c - 1;
    printf("%d %d %c\n", x, y, c);
    return 0;
}
```

**P2.** (1) `2edad` empieza con dígito → `edad2` (error de compilación). (2) `"8.5"` es texto; un `double` necesita `8.5` sin comillas (error de compilación). (3) `scanf("%d", grupo)` → `scanf("%d", &grupo)`: falta la dirección (gcc advierte y el programa puede fallar al ejecutarse). (4) `%d` con un `double` → `%.1f` (gcc advierte y muestra un valor sin sentido).

**P3.** hermanos → `int` (conteo); boleto → `double` (dinero); beca → `bool` (o `int` 1/0 si se lee con `scanf`); grupo → `char`; correo → arreglo de `char` (por ejemplo, `char correo[60]`); población de México (≈ 130 millones) → `int` alcanza (máx. ≈ 2 147 millones), pero `long long` (`%lld`) da margen para cifras mayores.

**P4.**

```c run title="p4.c" stdin="Jorge Mendez\n70.5 1.75\n"
#include <stdio.h>
#define CLINICA "Clinica Salud Joven"
int main(void)
{
    char nombre[50];
    double peso, estatura;
    printf("Nombre completo: ");
    scanf(" %49[^\n]", nombre);
    printf("Peso (kg) y estatura (m): ");
    scanf("%lf %lf", &peso, &estatura);
    printf("%s\nPaciente: %s\nPeso: %.1f kg\nEstatura: %.2f m\n",
           CLINICA, nombre, peso, estatura);
    return 0;
}
```
:::
