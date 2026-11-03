---
num: "02"
archivo: "Tema02_Tipos_variables_constantes_ES"
titulo: "Tipos de datos, variables, constantes y entrada/salida"
corto: "Tipos, variables y E/S"
lema: "Cada dato necesita una caja del tamaño correcto: aprende a elegirla, a nombrarla y a llenarla desde el teclado."
duracion: "4 h · 2 sesiones de 2 h"
previos: "Tema 01 (estructura de un programa, `cout`, compilación)."
fuentes:
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Cap. 1: §1.2.2 Datos y tipos, §1.2.4 Constantes simbólicas y literales, §1.2.5 Identificadores, §1.2.9 Variables, §1.2.10 Entrada/Salida, §1.2.11 Asignación, §1.2.12 Palabras reservadas, §1.2.13 Secuencias de escape, §1.2.14 Tabla ASCII."
  - "Lospinoso, J. (2019). *C++ Crash Course*. Cap. 1: The C++ Type System, Declaring Variables, Initializing a Variable's State, printf Format Specifiers. Cap. 2: Fundamental Types (Integer, Floating-Point, Character, Boolean, size_t)."
objetivos:
  A:
    - "Describir una variable por sus cuatro características: nombre, tipo, contenido y dirección de memoria."
    - "Elegir el tipo adecuado (`int`, `double`, `char`, `bool`, `string`) para un dato del mundo real."
    - "Declarar, inicializar y asignar variables con identificadores válidos y significativos."
    - "Leer datos del teclado con `cin` y `getline`, y mostrarlos con `cout`."
    - "Declarar constantes con `const` y distinguirlas de las variables."
  B:
    - "Comparar tamaños y rangos de los tipos con `sizeof` y predecir desbordamiento y truncamiento."
    - "Usar la inicialización con llaves `{}` y explicar cómo detecta conversiones con pérdida (*narrowing*)."
    - "Elegir entre `#define`, `const` y `constexpr` y justificar la elección."
    - "Relacionar `char` con su código ASCII y resolver el problema de `getline` después de `cin >>`."
efectos:
  soporte:
    - ["Elementos aislados", "Ocho conceptos presentados uno a uno (variable → tipos → declaración → identificadores → asignación → entrada → constantes → char/ASCII)."]
    - ["Atención dividida", "Diagramas de memoria integrados con el código que los produce; anotaciones junto a cada línea."]
    - ["Ejemplo resuelto", "Ficha de registro de un jugador: algoritmo → pseudocódigo → C++ → ejecución con datos."]
    - ["Movimiento humano", "Actividad «casilleros humanos»: los estudiantes representan variables y su contenido."]
  procedimental:
    - ["Variabilidad", "Errores frecuentes en contextos distintos (tipos, cin, getline, narrowing)."]
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
    A: "Conceptos 1–8 con diagramas de cajas; tipos básicos `int`, `double`, `char`, `bool`, `string`."
    B: "Repaso rápido; profundizar en `sizeof`, rangos, `{}` y *narrowing*, `constexpr`, ASCII."
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
    B: "Terminal con `g++ -Wall -Wextra` para ver advertencias de conversión."
plan:
  - ["Apertura", "Soporte", "Analogía de los casilleros; pregunta «¿cómo guarda un juego tu puntuación?».", "10 min"]
  - ["Desarrollo 1", "Soporte", "Conceptos 1–5 y actividad de casilleros humanos.", "40 min"]
  - ["Desarrollo 2", "Soporte", "Conceptos 6–8 y ejemplo resuelto 1.3.", "30 min"]
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
  - ["booleano", "Boolean (`bool`)", "Valor lógico: `true` o `false`."]
  - ["cadena", "string", "Secuencia de caracteres (`std::string`)."]
  - ["declaración", "declaration", "Sentencia que crea una variable indicando su tipo y nombre."]
  - ["inicialización", "initialization", "Dar valor a una variable en el momento de crearla."]
  - ["asignación", "assignment", "Guardar un nuevo valor en una variable existente con `=`."]
  - ["identificador", "identifier", "Nombre que el programador da a una variable, constante o función."]
  - ["palabra reservada", "keyword", "Palabra con significado especial en C++ (`int`, `return`…); no puede ser identificador."]
  - ["constante", "constant", "Valor con nombre que no puede cambiar (`const`, `constexpr`)."]
  - ["literal", "literal", "Valor escrito directamente en el código: `42`, `3.5`, `'a'`, `\"hola\"`."]
  - ["flujo de entrada", "input stream", "`cin`: canal por el que llegan los datos del teclado."]
  - ["operador de extracción", "extraction operator", "`>>`: toma un dato de `cin` y lo guarda en una variable."]
  - ["dirección de memoria", "memory address", "Número que identifica el lugar de la memoria donde vive la variable (`&x`)."]
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
Todo programa trabaja con datos: una app de banco guarda saldos con decimales, un juego guarda vidas enteras y nombres de texto, un sensor de Arduino guarda lecturas. **Elegir mal el tipo** produce errores reales: dinero que pierde centavos, edades negativas o contadores que «dan la vuelta». Hoy aprendes a elegir, nombrar y llenar cada caja correctamente. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | ¿Qué es una variable? Sus cuatro características | Elementos aislados, Atención dividida
Toda variable tiene **nombre**, **tipo**, **contenido** y **dirección**. El operador `&` («dirección de») permite ver dónde vive:

```cpp run
#include <iostream>
using namespace std;
int main()
{
    int edad = 17;                         //> Crea la caja `edad` (tipo int) con el valor 17
    cout << "Contenido: " << edad << "\n"; //> Al escribir el nombre obtenemos el **contenido**
    cout << "Tamano: " << sizeof(edad) << " bytes\n"; //> `sizeof` da el tamaño del **tipo**
    cout << "Direccion: " << &edad << "\n";  //> `&edad` da la **dirección** (cambia en cada ejecución)
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
| Tipo | Guarda… | Ejemplos de literales | Tamaño típico |
|---|---|---|---|
| `int` | números enteros | `17`, `-3`, `2026` | 4 bytes |
| `long long` | enteros muy grandes | `8000000000LL` | 8 bytes |
| `double` | números con decimales (doble precisión) | `3.1416`, `-0.5`, `6.02e23` | 8 bytes |
| `float` | decimales con menos precisión | `3.14f` | 4 bytes |
| `char` | **un** carácter | `'A'`, `'7'`, `'\n'` | 1 byte |
| `bool` | verdadero o falso | `true`, `false` | 1 byte |
| `string` | texto (varios caracteres) | `"Ana Lopez"` | variable (requiere `#include <string>`) |

Observa: los caracteres van entre **comillas simples** (`'A'`) y los textos entre **comillas dobles** (`"Ana"`). `string` no es un tipo fundamental: viene de la biblioteca estándar.

```cpp run
#include <iostream>
using namespace std;
int main()
{
    cout << "char:      " << sizeof(char) << " byte\n";
    cout << "bool:      " << sizeof(bool) << " byte\n";
    cout << "int:       " << sizeof(int) << " bytes\n";
    cout << "float:     " << sizeof(float) << " bytes\n";
    cout << "double:    " << sizeof(double) << " bytes\n";
    cout << "long long: " << sizeof(long long) << " bytes\n";
    return 0;
}
```

```diagram bars
items: [[char, 1], [bool, 1], [int, 4], [float, 4], [double, 8], ["long long", 8]]
unit: bytes
figcaption: "Figura 2. Tamaño de cada tipo en este compilador (g++ de 64 bits)."
```
:::

:::concepto | 3 | Declarar e inicializar | Elementos aislados, Atención dividida
**Declarar** es crear la caja; **inicializar** es ponerle su primer valor en el mismo momento.

```cpp run
#include <iostream>
#include <string>
using namespace std;
int main()
{
    int vidas = 3;            //> Declaración + inicialización con `=`
    double velocidad{2.5};    //> Inicialización con llaves `{}` (estilo del C++ Crash Course)
    char inicial = 'M';       //> `char` usa comillas simples
    bool vivo = true;         //> `bool` solo admite `true` o `false`
    string jugador = "Mia";   //> `string` usa comillas dobles y requiere `<string>`
    cout << jugador << " (" << inicial << ") vidas=" << vidas
         << " vel=" << velocidad << " vivo=" << vivo << "\n"; //> `cout` muestra `true` como 1
    return 0;
}
```

:::cuidado | Una variable sin inicializar contiene «basura»
`int puntos;` crea la caja pero **no** la limpia: contiene lo que haya quedado en esa memoria. Inicializa siempre: `int puntos = 0;` o `int puntos{};` (las llaves vacías ponen cero).
:::
:::

:::concepto | 4 | Identificadores: cómo nombrar las cajas | Elementos aislados
**Reglas** (obligatorias): solo letras, dígitos y guion bajo `_`; no pueden empezar con dígito; no pueden ser palabras reservadas (`int`, `return`, `while`…); C++ distingue mayúsculas (`Total` ≠ `total`).
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

:::concepto | 5 | Asignación: cambiar el contenido | Elementos aislados, Atención dividida
El operador `=` **no** significa «igual» como en matemáticas: significa «**guarda** el valor de la derecha en la caja de la izquierda». El valor anterior se pierde.

```cpp run
#include <iostream>
using namespace std;
int main()
{
    int puntos = 10;           //> puntos ← 10
    puntos = 25;               //> puntos ← 25 (el 10 se pierde)
    int bonus = puntos;        //> bonus ← copia del contenido de puntos (25)
    puntos = 0;                //> Cambiar puntos NO cambia bonus
    cout << "puntos=" << puntos << " bonus=" << bonus << "\n";
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

:::concepto | 6 | Entrada de datos con `cin` y `getline` | Elementos aislados, Atención dividida
`cin` (*character input*) es el teclado. El operador `>>` («extraer de») toma un dato y lo guarda en la variable. **Siempre** muestra antes un mensaje que diga qué escribir.

```cpp run stdin="Luis\n16 1.72\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string nombre;
    int edad;
    double estatura;
    cout << "Nombre: ";
    cin >> nombre;                    //> `>>` lee UNA palabra (se detiene en el espacio)
    cout << "Edad y estatura: ";
    cin >> edad >> estatura;          //> Se pueden encadenar; los datos se separan con espacio o Enter
    cout << nombre << " tiene " << edad << " anios y mide " << estatura << " m\n";
    return 0;
}
```

Para leer un **texto con espacios** (nombre completo, dirección) usa `getline(cin, variable);`:

```cpp run stdin="Ana Sofia Lopez\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string completo;
    cout << "Nombre completo: ";
    getline(cin, completo);          //> Lee toda la línea, con espacios, hasta el Enter
    cout << "Hola, " << completo << "\n";
    return 0;
}
```
:::

:::concepto | 7 | Constantes: valores que no deben cambiar | Elementos aislados
Hay valores que nunca cambian (π, el IVA, el número de días de la semana). Darles nombre evita «números mágicos» y errores.

```cpp run
#include <iostream>
using namespace std;
#define PI_MACRO 3.1416          //> Constante **simbólica** del preprocesador (estilo C, la usa el libro de Betancourt)
const double PI = 3.14159265;    //> Constante con tipo: el compilador la verifica (recomendada)
constexpr int DIAS_SEMANA = 7;   //> Constante calculada en compilación (C++11 en adelante)
int main()
{
    double radio = 2.0;
    cout << "Area (macro): " << PI_MACRO * radio * radio << "\n";
    cout << "Area (const): " << PI * radio * radio << "\n";
    cout << "Dias: " << DIAS_SEMANA << "\n";
    // PI = 3;  // ERROR: no se puede asignar a una constante
    return 0;
}
```

Un **literal** es el valor escrito tal cual (`3.1416`); una **constante simbólica** es un nombre para ese valor (`PI`). Por convención, las constantes se escriben en MAYÚSCULAS.
:::

:::concepto | 8 | `char`, el código ASCII y las secuencias de escape | Elementos aislados, Atención dividida
Un `char` guarda en realidad un **número pequeño**: su código en la tabla ASCII. `'A'` es 65, `'a'` es 97, `'0'` es 48.

```cpp run
#include <iostream>
using namespace std;
int main()
{
    char letra = 'A';
    cout << letra << " tiene codigo " << int(letra) << "\n";    //> `int(letra)` muestra el número
    char siguiente = letra + 1;                                 //> 65 + 1 = 66, que es 'B'
    cout << "Siguiente: " << siguiente << "\n";
    cout << "Comillas: \" y apostrofo: \' y barra: \\\n";       //> Secuencias de escape
    return 0;
}
```

| Secuencia | Significado | Secuencia | Significado |
|---|---|---|---|
| `\n` | nueva línea | `\"` | comilla doble |
| `\t` | tabulador | `\'` | comilla simple |
| `\\` | barra invertida | `\0` | carácter nulo (fin de cadena en C) |
| `\a` | pitido | `\r` | retorno de carro |
:::

:::movimiento | Casilleros humanos (10 min)
Cinco estudiantes pasan al frente con una hoja: arriba escriben un **nombre de variable** y su **tipo**, al reverso pegan un número de «dirección». El instructor dicta sentencias (`int vidas = 3;`, `vidas = vidas - 1;`, `char c = 'B';`, `c = c + 1;`) y cada «casillero» borra y escribe su contenido. El grupo verifica: ¿cabe ese valor en ese tipo? ¿Quién cambió y quién no?
:::

## 1.2 Ejemplo resuelto: ficha de registro de un jugador

:::ejemplo | Ficha de registro de un jugador | Ejemplo resuelto, Atención dividida
**Problema.** Un torneo escolar de videojuegos necesita registrar a cada jugador: nombre completo, edad, promedio de puntos por partida y la letra de su categoría (A, B o C). Al final se muestra la ficha.

**A. Algoritmo**

1. Pedir y leer el nombre completo (puede tener espacios → `getline`).
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

**C. Código en C++**

```cpp run title="ficha_jugador.cpp" stdin="Diego Ramirez Soto\n15 87.5 B\n"
#include <iostream>
#include <string>                       //> Necesaria para `string`
using namespace std;
int main()
{
    string nombre;                      //> Texto con espacios
    int edad;                           //> Entero: no hay edades con decimales
    double promedio;                    //> Decimal: 87.5 puntos
    char categoria;                     //> Una sola letra
    cout << "Nombre completo: ";
    getline(cin, nombre);               //> Paso 1: `getline` porque el nombre tiene espacios
    cout << "Edad, promedio y categoria: ";
    cin >> edad >> promedio >> categoria;   //> Paso 2: tres datos con un solo `cin`
    cout << "\n--- FICHA DEL JUGADOR ---\n";  //> Paso 3: mostrar
    cout << "Jugador:\t" << nombre << "\n";
    cout << "Edad:\t\t" << edad << "\n";
    cout << "Promedio:\t" << promedio << "\n";
    cout << "Categoria:\t" << categoria << "\n";
    return 0;
}
```

**D. Verificación.** Con la entrada `Diego Ramirez Soto`, `15 87.5 B` la ficha muestra los cuatro datos con el tipo correcto: el nombre completo (gracias a `getline`), la edad entera y el promedio con decimales.
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.2; ranksep=0.35;
@term(v, "Variable")
@proc(n, "nombre\n(identificador)")
@proc(t, "tipo\nint · double · char\nbool · string")
@proc(c, "contenido\n(se asigna con =)")
@proc(d, "dirección\n(&variable)")
v -> n; v -> t; v -> c; v -> d;
@io(e, "cin >>  ·  getline")
@io(s, "cout <<")
@sub(k, "constantes\nconst · constexpr · #define")
c -> e [dir=back, label="llenar"]; c -> s [label="mostrar"]; t -> k [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

Consulta esta sección **mientras** resuelves las tareas.

:::sintaxis | Tarjeta de sintaxis 2.1
| Quiero… | Escribo |
|---|---|
| Declarar e inicializar | `int edad = 17;` · `double precio{25.5};` · `char letra = 'A';` · `bool listo = false;` · `string nombre = "Ana";` |
| Poner en cero | `int contador{};` |
| Asignar un valor nuevo | `edad = 18;` |
| Leer una palabra o número | `cin >> edad;` |
| Leer varios datos | `cin >> a >> b >> c;` |
| Leer una línea con espacios | `getline(cin, nombre);` |
| Leer línea después de `cin >>` | `cin.ignore();` y luego `getline(cin, nombre);` |
| Constante | `const double IVA = 0.16;` |
| Tamaño de un tipo | `sizeof(int)` |
| Código ASCII de un `char` | `int(letra)` |
| Bibliotecas | `<iostream>` para `cin`/`cout`, `<string>` para `string` |

**¿Qué tipo elijo?** ¿Puede tener decimales? → `double`. ¿Es un conteo o una cantidad entera? → `int`. ¿Es un solo símbolo? → `char`. ¿Es sí/no? → `bool`. ¿Es texto? → `string`.
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿El tipo de cada variable corresponde a la naturaleza del dato (entero, decimal, carácter, lógico, texto)?</li>
<li>¿Inicialicé todas las variables antes de usarlas?</li>
<li>¿Los nombres dicen qué guardan, sin espacios, acentos ni ñ?</li>
<li>¿Mostré un mensaje (<code>cout</code>) antes de cada lectura (<code>cin</code>)?</li>
<li>¿La flecha va bien? <code>cin &gt;&gt;</code> (hacia la variable) y <code>cout &lt;&lt;</code> (hacia la pantalla).</li>
<li>¿El texto tiene espacios? Entonces <code>getline</code>. ¿Hubo un <code>cin &gt;&gt;</code> antes? Entonces <code>cin.ignore()</code>.</li>
<li>¿Incluí <code>&lt;string&gt;</code> si uso <code>string</code>?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Usar una variable que no se declaró.** ¿Por qué el compilador no conoce `total`?

```cpp err
#include <iostream>
using namespace std;
int main()
{
    total = 5;
    cout << total;
    return 0;
}
```
*Corrección:* declarar antes de usar: `int total = 5;`.

**b) La flecha al revés en `cin`.**

```cpp err
#include <iostream>
using namespace std;
int main()
{
    int edad;
    cin << edad;
    return 0;
}
```
*Corrección:* `cin >> edad;` — los datos «fluyen» del teclado **hacia** la variable.

**c) Conversión con pérdida detectada por las llaves.** ¿Qué dato se perdería?

```cpp err
#include <iostream>
int main()
{
    int precio{19.99};
    std::cout << precio;
    return 0;
}
```
*Corrección:* usar `double precio{19.99};`. Con `int precio = 19.99;` el programa compila, pero guarda **19**: la parte decimal se pierde en silencio. Las llaves te protegen.

**d) `getline` que «se salta».** El usuario escribe `20` ⏎ y luego su nombre, pero el programa no espera el nombre:

```cpp run stdin="20\nCarla Ruiz\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    int edad;
    string nombre;
    cout << "Edad: ";
    cin >> edad;                 //> `>>` lee 20 pero deja el Enter (`\n`) en el teclado
    cout << "Nombre: ";
    getline(cin, nombre);        //> `getline` encuentra ese Enter y termina de inmediato: línea vacía
    cout << "[" << nombre << "]\n";
    return 0;
}
```
*Corrección:* `cin.ignore();` entre ambas lecturas para descartar el Enter pendiente.

**e) Variable sin inicializar.** Compila, pero con `-Wall` g++ advierte; el resultado es impredecible (basura). Inicializa siempre: `int suma = 0;`.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Mismo patrón, otro contexto | Variabilidad
Leer → guardar en el tipo correcto → mostrar. Ahora con un producto de una tienda en línea:

```cpp run title="producto.cpp" stdin="Audifonos inalambricos\n649.90 12\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string producto;          //> texto con espacios → getline
    double precio;            //> dinero → decimal
    int existencias;          //> piezas → entero
    const double IVA = 0.16;  //> constante con nombre
    cout << "Producto: ";
    getline(cin, producto);
    cout << "Precio y existencias: ";
    cin >> precio >> existencias;
    cout << producto << " | $" << precio << " + IVA $" << precio * IVA
         << " | " << existencias << " piezas\n";
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

Resuélvelas en orden; la ayuda disminuye en cada una. {{ef:Desvanecimiento de guía}}

:::tarea A | T1. Registro en la veterinaria: estudia el ejemplo y resuelve su gemelo | 20 min | Ejemplo resuelto, Variabilidad
**Contexto.** Una veterinaria registra a cada mascota que llega. **¿Para qué?** Leer datos de distintos tipos y mostrarlos es la base de cualquier sistema de registro.

**Paso 1 · Estudia:**

```cpp run title="registro_mascota.cpp" stdin="Firulais\n4 12.5 S\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string nombre;          //> Una palabra → `cin >>` basta
    int edad;               //> Años completos → entero
    double peso;            //> Kilogramos con decimales → double
    char vacunado;          //> 'S' o 'N' → char
    cout << "Nombre de la mascota: ";
    cin >> nombre;
    cout << "Edad, peso y vacunado (S/N): ";
    cin >> edad >> peso >> vacunado;
    cout << "\nMascota: " << nombre << "\nEdad: " << edad
         << " anios\nPeso: " << peso << " kg\nVacunado: " << vacunado << "\n";
    return 0;
}
```

**Paso 2 · Ahora tú (gemelo).** Escribe `registro_libro.cpp` para una biblioteca: **título** (con espacios), **año de publicación**, **precio** y **sección** (una letra). Muestra la ficha.

:::solucion | T1
```cpp run title="registro_libro.cpp" stdin="Cien anios de soledad\n1967 289.50 L\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string titulo;
    int anio;
    double precio;
    char seccion;
    cout << "Titulo: ";
    getline(cin, titulo);          // el titulo tiene espacios
    cout << "Anio, precio y seccion: ";
    cin >> anio >> precio >> seccion;
    cout << "\nLibro: " << titulo << "\nAnio: " << anio
         << "\nPrecio: $" << precio << "\nSeccion: " << seccion << "\n";
    return 0;
}
```
:::
:::

:::tarea A | T2. Perfil de videojuego (completa con pistas) | 20 min | Problema por completar
**Contexto.** Un juego guarda el perfil del jugador. **¿Para qué?** Elegir el tipo correcto evita que la vida tenga decimales perdidos o que el nivel sea un texto.

```cpp blank title="perfil.cpp"
#include <iostream>
#include __1__                       // 1: biblioteca para usar string
using namespace std;
int main()
{
    __2__ usuario;                   // 2: tipo para un texto
    int nivel;
    __3__ vida;                      // 3: tipo para 87.5 puntos de vida
    __4__ premium;                   // 4: tipo para si/no (1 o 0)
    cout << "Usuario, nivel, vida y premium (1/0): ";
    cin __5__ usuario >> nivel >> vida >> premium;   // 5: operador de extraccion
    cout << usuario << " | nivel " << nivel << " | vida " << vida
         << " | premium " << premium << "\n";
    return 0;
}
```

**Prueba con:** `dragon77 12 87.5 1`

:::solucion | T2
{{c:1}} `<string>` · {{c:2}} `string` · {{c:3}} `double` · {{c:4}} `bool` · {{c:5}} `>>`

```cpp run title="perfil.cpp" stdin="dragon77 12 87.5 1\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string usuario;
    int nivel;
    double vida;
    bool premium;
    cout << "Usuario, nivel, vida y premium (1/0): ";
    cin >> usuario >> nivel >> vida >> premium;
    cout << usuario << " | nivel " << nivel << " | vida " << vida
         << " | premium " << premium << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T3. Alta de un producto (completa sin pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Una papelería da de alta productos con nombre (con espacios), precio, existencias y una constante de descuento del 10 %.

```cpp blank title="alta_producto.cpp"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    __1__ double DESCUENTO = 0.10;
    string nombre;
    __2__ precio;
    __3__ existencias;
    cout << "Nombre del producto: ";
    __4__(cin, nombre);
    cout << "Precio y existencias: ";
    cin >> precio __5__ existencias;
    cout << nombre << ": $" << precio << " (con descuento $"
         << precio - precio * __6__ << "), " << existencias << " piezas\n";
    return 0;
}
```

**Prueba con:** `Cuaderno profesional` · `45 30`

:::solucion | T3
{{c:1}} `const` · {{c:2}} `double` · {{c:3}} `int` · {{c:4}} `getline` · {{c:5}} `>>` · {{c:6}} `DESCUENTO`

```cpp run title="alta_producto.cpp" stdin="Cuaderno profesional\n45 30\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    const double DESCUENTO = 0.10;
    string nombre;
    double precio;
    int existencias;
    cout << "Nombre del producto: ";
    getline(cin, nombre);
    cout << "Precio y existencias: ";
    cin >> precio >> existencias;
    cout << nombre << ": $" << precio << " (con descuento $"
         << precio - precio * DESCUENTO << "), " << existencias << " piezas\n";
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
```cpp run title="credencial.cpp" stdin="Valeria Torres Gil\n20261045 B 3 9.2\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    const string ESCUELA = "ESCUELA PREPARATORIA TECNICA"; // no cambia
    string nombre;      // texto con espacios
    int control;        // numero entero sin decimales
    char grupo;         // una sola letra
    int semestre;       // conteo entero
    double promedio;    // puede tener decimales
    cout << "Nombre completo: ";
    getline(cin, nombre);
    cout << "Control, grupo, semestre y promedio: ";
    cin >> control >> grupo >> semestre >> promedio;
    cout << "\n=================================\n";
    cout << " " << ESCUELA << "\n";
    cout << "=================================\n";
    cout << "Alumno:\t\t" << nombre << "\n";
    cout << "Control:\t" << control << "\n";
    cout << "Grupo:\t\t" << grupo << "\tSemestre: " << semestre << "\n";
    cout << "Promedio:\t" << promedio << "\n";
    cout << "=================================\n";
    return 0;
}
```
:::
:::

:::tarea A | T5. Todo lo que puedas saber de una letra (solución libre) | 15 min | Solución libre
**Contexto.** Tienes la variable `char letra = 'G';`. **No hay una pregunta única:** escribe un programa que muestre **toda la información que puedas obtener** de esa variable con lo que sabes hoy (su código ASCII, la letra anterior y la siguiente, su tamaño en memoria, su dirección, su minúscula sabiendo que la distancia entre `'A'` y `'a'` es 32…). Cuantos más datos descubras, mejor.

:::solucion | T5
Una exploración posible (hay muchas otras válidas):

```cpp run title="explora_letra.cpp" out=1
#include <iostream>
using namespace std;
int main()
{
    char letra = 'G';
    cout << "Letra: " << letra << "\n";
    cout << "Codigo ASCII: " << int(letra) << "\n";
    cout << "Anterior: " << char(letra - 1) << "  Siguiente: " << char(letra + 1) << "\n";
    cout << "Minuscula: " << char(letra + 32) << "\n";
    cout << "Posicion en el alfabeto: " << letra - 'A' + 1 << "\n";
    cout << "Tamano: " << sizeof(letra) << " byte\n";
    return 0;
}
```
:::
:::

:::tarea B | T6. Salidas sorprendentes (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
**Contexto.** Un compañero ejecutó este programa y no entiende las líneas 2, 3 y 4 de la salida. **Explica con tus palabras** por qué ocurre cada una.

```cpp run title="sorpresas.cpp"
#include <iostream>
using namespace std;
int main()
{
    short pequeno = 32767;       // valor maximo de short
    pequeno = pequeno + 1;
    int dividido = 7.9;          // compila (con aviso), pero...
    char c = 'a' + 2;
    cout << "sizeof(short) = " << sizeof(short) << "\n";
    cout << "pequeno = " << pequeno << "\n";
    cout << "dividido = " << dividido << "\n";
    cout << "c = " << c << " (" << int(c) << ")\n";
    return 0;
}
```

{{lineas:4}}

:::solucion | T6
- **`pequeno = -32768`**: un `short` ocupa 2 bytes y su máximo es 32767. Al sumar 1 se produce **desbordamiento** y el valor «da la vuelta» al mínimo del rango.
- **`dividido = 7`**: asignar un `double` a un `int` **trunca** (elimina) la parte decimal; no redondea. Con `int dividido{7.9};` el compilador lo habría rechazado.
- **`c = c (99)`**: `'a'` vale 97 en ASCII; 97 + 2 = 99, que corresponde a la letra `c`.
:::
:::

:::tarea B | T7. Imagina la memoria (imaginación) | 15 min | Imaginación
**Sin ejecutar** el programa, imagina las cajas de memoria y **dibuja su contenido después de cada línea** (como en la Figura 3). Luego ejecútalo para comprobar la salida final.

```cpp check title="imagina.cpp"
#include <iostream>
using namespace std;
int main()
{
    int a = 4;
    int b = a * 2;
    a = b - 1;
    b = a + b;
    char inicial = 'K';
    inicial = inicial + 2;
    cout << a << " " << b << " " << inicial << "\n";
    return 0;
}
```

{{lineas:3}}

:::solucion | T7
| Después de la línea | `a` | `b` | `inicial` |
|---|---|---|---|
| 5 | 4 | — | — |
| 6 | 4 | 8 | — |
| 7 | 7 | 8 | — |
| 8 | 7 | 15 | — |
| 9 | 7 | 15 | `'K'` |
| 10 | 7 | 15 | `'M'` |

```cpp run title="imagina.cpp"
#include <iostream>
using namespace std;
int main()
{
    int a = 4;
    int b = a * 2;
    a = b - 1;
    b = a + b;
    char inicial = 'K';
    inicial = inicial + 2;
    cout << a << " " << b << " " << inicial << "\n";
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
3. **Integrante 3:** estado (¿vivo? ¿tiene montura? → `bool`) y constantes del juego (`NIVEL_MAXIMO = 99`).
4. **Todos:** integran el programa que lee los datos y muestra la ficha; justifican cada tipo en un comentario y presentan su diseño a otro equipo.

:::solucion | T8
Una solución posible:

```cpp run title="personaje.cpp" stdin="Lyra Vientoalto\nM 7 5 9 64.5 120.0 1 0\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    const int NIVEL_MAXIMO = 99;          // regla fija del juego
    string nombre;                        // texto con espacios
    char clase;                           // G, M o A
    int nivel, fuerza, agilidad;          // valores enteros
    double vida, mana;                    // pueden tener decimales
    bool vivo, montura;                   // si/no
    cout << "Nombre: ";
    getline(cin, nombre);
    cout << "Clase nivel fuerza agilidad vida mana vivo montura: ";
    cin >> clase >> nivel >> fuerza >> agilidad >> vida >> mana >> vivo >> montura;
    cout << "\n== " << nombre << " [" << clase << "] ==\n";
    cout << "Nivel " << nivel << "/" << NIVEL_MAXIMO << "\n";
    cout << "Fuerza " << fuerza << "  Agilidad " << agilidad << "\n";
    cout << "Vida " << vida << "  Mana " << mana << "\n";
    cout << "Vivo: " << vivo << "  Montura: " << montura << "\n";
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Un experto programa un formulario de inscripción | Modalidad, Ejemplo resuelto
*Guion para narrar en 4 segmentos breves (≈ 3 min en total), mostrando el código en pantalla. El estudiante controla el ritmo (pausar/repetir) para evitar el efecto de información transitoria.*

**Problema:** «Inscribir a un participante a un torneo de ajedrez: nombre completo, edad, rating (puede tener decimales) y si es socio del club».

**Segmento 1 — Tipos primero.** {{como}} Antes de escribir código hago una lista de datos y les pongo tipo: nombre → `string`; edad → `int`; rating → `double`; socio → `bool`. {{porque}} El tipo decide qué valores son válidos y cuánta memoria uso; si me equivoco aquí, todo lo demás falla.

**Segmento 2 — El orden de lectura importa.** {{como}} Leo primero el nombre con `getline`, porque tiene espacios, y después los números con `cin >>`. {{porque}} Si leyera la edad primero, el Enter que queda pendiente haría que `getline` regresara una línea vacía; leyendo en este orden evito necesitar `cin.ignore()`.

**Segmento 3 — Mensajes claros.** {{como}} Antes de cada lectura escribo qué debe teclear el usuario, incluso el formato: «socio (1 = si, 0 = no)». {{porque}} El usuario no ve mis variables; si no sabe qué escribir, mete un texto donde va un número y `cin` falla.

**Segmento 4 — Probar con datos reales.** {{como}} Compilo con `-Wall`, pruebo con `Ana Paula Ríos`, `16`, `1450.5`, `1` y reviso que cada dato aparezca igual que lo escribí. {{porque}} Probar con un nombre de varias palabras y un decimal confirma justamente las dos decisiones que tomé.

```cpp run title="inscripcion.cpp" stdin="Ana Paula Rios\n16 1450.5 1\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string nombre;
    int edad;
    double rating;
    bool socio;
    cout << "Nombre completo: ";
    getline(cin, nombre);
    cout << "Edad, rating y socio (1 = si, 0 = no): ";
    cin >> edad >> rating >> socio;
    cout << "Inscrito: " << nombre << " (" << edad << " anios), rating "
         << rating << ", socio: " << socio << "\n";
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
6. ¿Qué instrucción lee un texto completo con espacios?
7. ¿Qué palabra hace que una variable no pueda modificarse?
8. ¿Cuántos bytes ocupa normalmente un `char`? ¿Y un `double`?
9. ¿Qué código ASCII tiene `'A'`?
10. ¿Qué secuencia de escape muestra una comilla doble dentro de un texto?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida:**

```cpp check title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int x = 3;
    int y = x + 4;
    x = y * 2;
    char c = 'D';
    c = c - 1;
    cout << x << " " << y << " " << c << "\n";
    return 0;
}
```

**P2. Corrige** los errores (hay cuatro) y explica cada uno:

```cpp blank title="p2.cpp"
#include <iostream>
using namespace std;
int main()
{
    int 2edad;
    double promedio = "8.5";
    string nombre;
    cin << nombre;
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
<li>Leo números con <code>cin &gt;&gt;</code> y textos con espacios con <code>getline</code>.</li>
<li>Uso constantes con nombre en lugar de números mágicos.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 Nombre, tipo, contenido y dirección de memoria · 2 c · 3 c (empieza con dígito) · 4 `'A'` es un `char` (un carácter); `"A"` es una cadena de texto · 5 Falso: `=` asigna (guarda) el valor; `x` puede cambiar después · 6 `getline(cin, variable);` · 7 `const` (o `constexpr`) · 8 1 byte y 8 bytes · 9 65 · 10 `\"`
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.**

```cpp run title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int x = 3;
    int y = x + 4;
    x = y * 2;
    char c = 'D';
    c = c - 1;
    cout << x << " " << y << " " << c << "\n";
    return 0;
}
```

**P2.** (1) `2edad` empieza con dígito → `edad2`. (2) `"8.5"` es texto; un `double` necesita `8.5` sin comillas. (3) Falta `#include <string>` para usar `string`. (4) `cin << nombre` → `cin >> nombre`.

**P3.** hermanos → `int` (conteo); boleto → `double` (dinero); beca → `bool`; grupo → `char`; correo → `string`; población de México (≈ 130 millones) → `int` alcanza (máx. ≈ 2 147 millones), pero `long long` da margen para cifras mayores.

**P4.**

```cpp run title="p4.cpp" stdin="Jorge Mendez\n70.5 1.75\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    const string CLINICA = "Clinica Salud Joven";
    string nombre;
    double peso, estatura;
    cout << "Nombre completo: ";
    getline(cin, nombre);
    cout << "Peso (kg) y estatura (m): ";
    cin >> peso >> estatura;
    cout << CLINICA << "\nPaciente: " << nombre << "\nPeso: " << peso
         << " kg\nEstatura: " << estatura << " m\n";
    return 0;
}
```
:::
