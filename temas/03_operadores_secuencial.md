---
num: "03"
archivo: "Tema03_Operadores_expresiones_estructura_secuencial"
titulo: "Operadores, expresiones y estructura secuencial"
corto: "Operadores y secuencia"
lema: "De la fórmula del cuaderno a la línea de código: entrada, proceso y salida, una sentencia tras otra."
duracion: "4 h · 2 sesiones de 2 h"
previos: "Tema 02 (variables, tipos, `cin`/`cout`)."
fuentes:
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Cap. 1: §1.2.8 Operadores, §1.2.11 Asignación. Cap. 2: Estructuras secuenciales (§2.1 Sentencia, §2.2 Estructura secuencial, §2.3 Ejercicios 1–10)."
  - "Lospinoso, J. (2019). *C++ Crash Course*. Cap. 7 «Expressions»: Arithmetic, Assignment, Increment and Decrement, Comparison and Logical Operators, Operator Precedence and Associativity, Implicit Type Conversions, Explicit Type Conversion (`static_cast`), C-Style Casts."
objetivos:
  A:
    - "Traducir fórmulas matemáticas a expresiones en C++ usando `+ - * / %` y paréntesis."
    - "Aplicar la precedencia de operadores para predecir el valor de una expresión."
    - "Usar asignación compuesta (`+=`, `-=`…) e incremento/decremento (`++`, `--`)."
    - "Usar funciones de `<cmath>` (`sqrt`, `pow`, `fabs`) y dar formato con `fixed` y `setprecision`."
    - "Resolver problemas con estructura secuencial: entrada → proceso → salida."
  B:
    - "Predecir resultados con división entera, módulo y mezcla de tipos (conversiones implícitas)."
    - "Usar `static_cast` para conversiones explícitas y explicar por qué es preferible al *cast* estilo C."
    - "Distinguir prefijo y posfijo (`++i` vs `i++`) y evaluar expresiones relacionales y lógicas."
    - "Implementar fórmulas científicas con funciones trigonométricas, convirtiendo grados a radianes."
efectos:
  soporte:
    - ["Elementos aislados", "Ocho conceptos separados: aritmética → precedencia → asignación compuesta → conversiones → `<cmath>` → formato → relacionales/lógicos → estructura secuencial."]
    - ["Atención dividida", "Evaluación paso a paso de expresiones en tablas integradas y árbol de expresión junto al código."]
    - ["Ejemplo resuelto", "Conversión de temperaturas: algoritmo → pseudocódigo → diagrama de flujo → C++ → salida."]
    - ["Movimiento humano", "«Árbol de expresión humano»: los estudiantes se ordenan según la precedencia."]
  procedimental:
    - ["Variabilidad", "Errores frecuentes en contextos de física, finanzas y videojuegos."]
    - ["Autoexplicación", "Cada error lógico se presenta como «¿por qué da ese número?»."]
  tareas:
    - ["Ejemplo resuelto", "T1: calificación ponderada resuelta + gemelo."]
    - ["Problema por completar", "T2 (temperaturas, con pistas) y T3 (escalera, sin pistas)."]
    - ["Desvanecimiento de guía", "T1 → T4 con ayuda decreciente."]
    - ["Solución libre", "T5: calcular todo lo posible a partir de un radio."]
    - ["Autoexplicación", "T6: explicar resultados sorprendentes de expresiones."]
    - ["Imaginación", "T7: imaginar el árbol de la fórmula general antes de programarla."]
    - ["Memoria colectiva de trabajo", "T8: calculadora de nutrientes por equipos."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Operadores aritméticos, precedencia, `<cmath>` básico y formato con dos decimales."
    B: "Conversiones implícitas/explícitas, prefijo/posfijo, trigonometría y radianes."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 con tablas de evaluación paso a paso; trabajo en pares."
    B: "T3, T6, T7 autónomas; T8 como coordinadores de integración."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Programa de cambio en monedas (T4) con pruebas de escritorio."
    B: "Programa de la fórmula general (T7) con explicación del árbol de expresión."
  Entorno:
    comp: "Información procedimental"
    A: "Calculadora a la mano para verificar resultados contra el programa."
    B: "Compilación con `-Wall -Wconversion` para detectar conversiones peligrosas."
plan:
  - ["Apertura", "Soporte", "Pregunta: «¿por qué una app de banco nunca puede equivocarse al dividir?». Analogía de la receta escalada.", "10 min"]
  - ["Desarrollo 1", "Soporte", "Conceptos 1–4 y árbol de expresión humano.", "40 min"]
  - ["Desarrollo 2", "Soporte", "Conceptos 5–8; ejemplo resuelto de temperaturas.", "30 min"]
  - ["Práctica guiada", "Tareas + procedimental", "Ruta A: T1 → T3. Ruta B: T3, T6, T7.", "60 min"]
  - ["Colaborativa", "Tareas", "T8 por equipos.", "30 min"]
  - ["Autónoma", "Tareas", "T4 (todos), T5 (Ruta A).", "30 min"]
  - ["Cierre", "Protocolo + evaluación", "Protocolo verbal (tiro parabólico), tests y autorregistro.", "40 min"]
glosario:
  - ["expresión", "expression", "Combinación de operandos y operadores que produce un valor."]
  - ["operando", "operand", "Valor sobre el que actúa un operador (`a` y `b` en `a + b`)."]
  - ["operador aritmético", "arithmetic operator", "`+ - * / %`."]
  - ["división entera", "integer division", "División entre dos enteros: descarta la parte decimal (`7 / 2` = 3)."]
  - ["módulo / residuo", "modulo / remainder", "`%`: residuo de una división entera (`7 % 2` = 1)."]
  - ["precedencia", "precedence", "Orden en que se aplican los operadores (`*` antes que `+`)."]
  - ["asociatividad", "associativity", "Dirección de evaluación entre operadores de igual precedencia (izquierda → derecha)."]
  - ["asignación compuesta", "compound assignment", "`x += 3` equivale a `x = x + 3`."]
  - ["incremento / decremento", "increment / decrement", "`++` suma 1, `--` resta 1."]
  - ["conversión implícita", "implicit conversion", "Cambio de tipo que hace el compilador automáticamente."]
  - ["conversión explícita", "explicit conversion / cast", "Cambio de tipo indicado por el programador (`static_cast<double>(x)`)."]
  - ["operador relacional", "comparison operator", "`< > <= >= == !=`; produce `true` o `false`."]
  - ["operador lógico", "logical operator", "`&&` (y), `||` (o), `!` (no)."]
  - ["estructura secuencial", "sequential structure", "Sentencias que se ejecutan una tras otra, en orden."]
  - ["prueba de escritorio", "desk check / trace", "Ejecutar a mano el programa anotando el valor de cada variable."]
---

# 1. Información de soporte {.soporte}

:::analogia | Una fórmula es una receta que se escala
Una receta para 4 personas pide 300 g de harina. Para 10 personas calculas `300 / 4 * 10`. Si haces las operaciones en otro orden, o si redondeas a mitad del camino, el pastel sale mal. Programar fórmulas es igual: **el orden de las operaciones y el tipo de los números** deciden si el resultado es correcto.
:::

:::pregunta
Escribe en tu calculadora `7 / 2`. Ahora piensa: **¿qué crees que responde C++ a `7 / 2`?** ¿Y a `7.0 / 2`? Anota tu predicción y compruébala en el concepto 1.

{{lineas:2}}
:::

:::relevancia
Una app bancaria calcula intereses, un juego calcula la trayectoria de un proyectil, un termostato convierte grados. Todos son programas **secuenciales**: leen datos, aplican fórmulas y muestran resultados. Un error en una división entera puede costar dinero real o hacer que un personaje atraviese una pared. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | Operadores aritméticos y la trampa de la división entera | Elementos aislados, Atención dividida
| Operador | Operación | Ejemplo | Resultado |
|---|---|---|---|
| `+` | suma | `8 + 3` | `11` |
| `-` | resta | `8 - 3` | `5` |
| `*` | multiplicación | `8 * 3` | `24` |
| `/` | división | `8 / 3` | `2` (¡enteros!) |
| `/` | división | `8.0 / 3` | `2.66667` |
| `%` | residuo (solo enteros) | `8 % 3` | `2` |

```cpp run
#include <iostream>
using namespace std;
int main()
{
    cout << "7 / 2   = " << 7 / 2 << "\n";     //> int / int → int: se DESCARTA el .5
    cout << "7.0 / 2 = " << 7.0 / 2 << "\n";   //> Si un operando es double, el resultado es double
    cout << "7 % 2   = " << 7 % 2 << "\n";     //> Residuo: 7 = 2·3 + **1**
    cout << "10 % 5  = " << 10 % 5 << "\n";    //> Residuo 0 → 10 es múltiplo de 5
    return 0;
}
```

**Regla:** si los dos operandos de `/` son enteros, el resultado es entero. Para obtener decimales, al menos uno debe ser `double`.
:::

:::concepto | 2 | Precedencia y asociatividad: ¿qué se calcula primero? | Elementos aislados, Atención dividida
Como en matemáticas: primero lo que está entre **paréntesis**, luego `*`, `/`, `%` y al final `+`, `-`. Entre operadores del mismo nivel, de **izquierda a derecha**.

<div class="cols">
<div>

| Paso | Expresión | Qué se resolvió |
|---|---|---|
| 0 | `2 + 3 * 4 - 6 / 2` | — |
| 1 | `2 + 12 - 6 / 2` | `3 * 4` |
| 2 | `2 + 12 - 3` | `6 / 2` |
| 3 | `14 - 3` | `2 + 12` (izq. → der.) |
| 4 | `11` | `14 - 3` |

</div>
<div>

```dot
rankdir=TB; nodesep=0.25; ranksep=0.25;
node [shape=circle, width=0.42, fixedsize=true, fontsize=13];
m [label="−", fillcolor="#fde68a", color="#d97706"];
p [label="+"]; d [label="/"]; x [label="*"];
n2 [label="2", fillcolor="#fff", color="#94a3b8"]; n3 [label="3", fillcolor="#fff", color="#94a3b8"];
n4 [label="4", fillcolor="#fff", color="#94a3b8"]; n6 [label="6", fillcolor="#fff", color="#94a3b8"]; n2b [label="2", fillcolor="#fff", color="#94a3b8"];
m -> p; m -> d; p -> n2; p -> x; x -> n3; x -> n4; d -> n6; d -> n2b;
```

</div>
</div>

El **árbol de expresión** muestra el orden: se calcula de las hojas hacia la raíz; la raíz (`−`) es la última operación.

:::cuidado | Los paréntesis cambian el significado
El promedio de `a` y `b` es `(a + b) / 2`, **no** `a + b / 2` (eso suma `a` con la mitad de `b`). Ante la duda, usa paréntesis: no cuestan nada y aclaran la intención.
:::
:::

:::movimiento | Árbol de expresión humano (10 min)
Siete estudiantes reciben tarjetas: `2`, `+`, `3`, `*`, `4`, `-`, `1`. Se forman en fila en el orden de la expresión `2 + 3 * 4 - 1`. El grupo indica qué operador «actúa» primero: ese estudiante toma de la mano a sus dos vecinos, los tres se convierten en un solo valor (escriben `12` en una hoja nueva) y regresan a la fila. Se repite hasta quedar un solo estudiante con el resultado. Después se repite con `(2 + 3) * (4 - 1)`.
:::

:::concepto | 3 | Asignación compuesta, incremento y decremento | Elementos aislados, Atención dividida
```cpp run
#include <iostream>
using namespace std;
int main()
{
    int puntos = 10;
    puntos += 5;     //> puntos = puntos + 5  → 15
    puntos -= 3;     //> puntos = puntos - 3  → 12
    puntos *= 2;     //> puntos = puntos * 2  → 24
    puntos /= 5;     //> puntos = puntos / 5  → 4 (división entera)
    puntos %= 3;     //> puntos = puntos % 3  → 1
    puntos++;        //> puntos = puntos + 1  → 2
    puntos--;        //> puntos = puntos - 1  → 1
    cout << "puntos = " << puntos << "\n";
    return 0;
}
```

:::nota | Ruta B · prefijo vs posfijo
`++x` incrementa **y luego** entrega el valor; `x++` entrega el valor **y luego** incrementa. Solo importa cuando se usan dentro de otra expresión: con `int x = 5;`, `int a = x++;` deja `a = 5, x = 6`, mientras que `int b = ++x;` deja `b = 7, x = 7`. Para evitar confusiones, úsalos solos en su propia sentencia.
:::
:::

:::concepto | 4 | Conversiones de tipo: implícitas y explícitas | Elementos aislados, Atención dividida
Cuando se mezclan tipos, C++ convierte **automáticamente** al tipo «más amplio» (`int` → `double`). Al **asignar** un `double` a un `int`, la parte decimal se **trunca**.

```cpp run
#include <iostream>
using namespace std;
int main()
{
    int suma = 17, n = 4;
    double malo = suma / n;                         //> 17/4 se calcula como enteros = 4, y LUEGO se guarda como 4.0
    double bueno = static_cast<double>(suma) / n;   //> Convertimos `suma` ANTES de dividir → 4.25
    int truncado = 9.99;                            //> double → int: se trunca a 9 (no redondea)
    cout << "malo = " << malo << "\nbueno = " << bueno
         << "\ntruncado = " << truncado << "\n";
    return 0;
}
```

`static_cast<tipo>(valor)` es la **conversión explícita** recomendada por el *C++ Crash Course*; la forma de C, `(double)suma`, también funciona, pero es menos visible y permite conversiones peligrosas sin aviso.
:::

:::concepto | 5 | Funciones matemáticas de `<cmath>` | Elementos aislados
| Función | Calcula | Ejemplo | Resultado |
|---|---|---|---|
| `sqrt(x)` | raíz cuadrada | `sqrt(25.0)` | `5` |
| `pow(b, e)` | potencia bᵉ | `pow(2, 10)` | `1024` |
| `fabs(x)` | valor absoluto | `fabs(-3.5)` | `3.5` |
| `sin(x)`, `cos(x)`, `tan(x)` | trigonométricas (**x en radianes**) | `cos(0.0)` | `1` |
| `round(x)`, `floor(x)`, `ceil(x)` | redondear, piso, techo | `round(2.5)` | `3` |

:::cuidado | `^` NO es potencia en C++
`3 ^ 2` no es 9: el operador `^` es el «o exclusivo» de bits y da `1`. Para potencias usa `pow(3, 2)` o simplemente `3 * 3`.
:::

**Grados a radianes:** `radianes = grados * PI / 180`, con `const double PI = 3.14159265358979;`.
:::

:::concepto | 6 | Dar formato a los decimales con `<iomanip>` | Elementos aislados, Atención dividida
```cpp run
#include <iostream>
#include <iomanip>                        //> Biblioteca de manipuladores de formato
using namespace std;
int main()
{
    double precio = 1234.5678;
    cout << precio << "\n";                               //> Formato por defecto: 6 cifras significativas
    cout << fixed << setprecision(2) << precio << "\n";   //> `fixed` + `setprecision(2)`: exactamente 2 decimales
    cout << "[" << setw(10) << precio << "]\n";           //> `setw(10)`: ocupa 10 espacios (alinea columnas)
    return 0;
}
```
`fixed` y `setprecision` **se quedan activos** para todo lo que se muestre después.
:::

:::concepto | 7 | Operadores relacionales y lógicos (adelanto del Tema 04) | Elementos aislados
Comparan valores y producen `true` (1) o `false` (0):

| Relacionales | Significado | Lógicos | Significado |
|---|---|---|---|
| `<`, `>` | menor, mayor | `&&` | Y: ambas verdaderas |
| `<=`, `>=` | menor o igual, mayor o igual | `\|\|` | O: al menos una verdadera |
| `==` | igual (¡dos signos!) | `!` | NO: invierte |
| `!=` | diferente | | |

```cpp run
#include <iostream>
using namespace std;
int main()
{
    int edad = 16;
    cout << boolalpha;                                       //> Muestra true/false en lugar de 1/0
    cout << "edad >= 18: " << (edad >= 18) << "\n";
    cout << "edad == 16: " << (edad == 16) << "\n";
    cout << "13 <= edad && edad <= 19: " << (13 <= edad && edad <= 19) << "\n"; //> ¿Es adolescente?
    return 0;
}
```
:::

:::concepto | 8 | La estructura secuencial: entrada → proceso → salida | Elementos aislados, Atención dividida
Una **estructura secuencial** es un bloque de sentencias que se ejecutan **una después de otra**, en el orden escrito, sin saltos. Casi todos los problemas de fórmulas siguen el mismo esquema:

```dot w="62%"
rankdir=LR; nodesep=0.2; ranksep=0.3;
@term(i, "Inicio")
@io(e, "ENTRADA\nleer datos")
@proc(p, "PROCESO\naplicar fórmulas")
@io(s, "SALIDA\nmostrar resultados")
@term(f, "Fin")
i -> e -> p -> s -> f;
```
:::

## 1.2 Ejemplo resuelto: conversión de temperaturas

:::ejemplo | Conversión de temperaturas (adaptado de Betancourt y Polanco, cap. 2, ej. 3) | Ejemplo resuelto, Atención dividida
**Problema.** Leer una temperatura en grados Celsius y mostrarla en Fahrenheit, Kelvin y Rankine, con dos decimales. Fórmulas: `F = 9/5 · C + 32`, `K = C + 273.15`, `R = F + 459.67`.

**A. Algoritmo:** 1) Leer `C`. 2) Calcular `F`, luego `K`, luego `R` (`R` necesita `F`: el orden importa). 3) Mostrar las cuatro escalas.

<div class="cols">
<div>

**B. Pseudocódigo**

```pseudo
Algoritmo Temperaturas
    Definir C, F, K, R Como Real
    Escribir "Celsius: "
    Leer C
    F <- 9 / 5 * C + 32
    K <- C + 273.15
    R <- F + 459.67
    Escribir F, K, R
FinAlgoritmo
```

</div>
<div>

**Diagrama de flujo**

```dot
rankdir=TB; nodesep=0.2; ranksep=0.22;
@term(i, "Inicio")
@io(l, "Leer C")
@proc(f, "F ← 9.0/5 · C + 32")
@proc(k, "K ← C + 273.15")
@proc(r, "R ← F + 459.67")
@io(s, "Mostrar F, K, R")
@term(fin, "Fin")
i -> l -> f -> k -> r -> s -> fin;
```

</div>
</div>

**C. Código en C++**

```cpp run title="temperaturas.cpp" stdin="36.5\n"
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    double c, f, k, r;
    cout << "Temperatura en Celsius: ";
    cin >> c;                          //> ENTRADA
    f = 9.0 / 5 * c + 32;              //> PROCESO. ¡Ojo! `9.0`: con `9 / 5` daría 1 (división entera)
    k = c + 273.15;
    r = f + 459.67;                    //> Usa `f`, por eso se calcula después de `f`
    cout << fixed << setprecision(2);  //> SALIDA con 2 decimales
    cout << "Fahrenheit: " << f << "\nKelvin:     " << k
         << "\nRankine:    " << r << "\n";
    return 0;
}
```

**D. Verificación (prueba de escritorio).** Con `C = 36.5`: `F = 1.8 · 36.5 + 32 = 97.70`; `K = 309.65`; `R = 97.70 + 459.67 = 557.37`. Coincide con la salida.
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.18; ranksep=0.3;
@term(ex, "Expresión")
@proc(ar, "aritméticos\n+ - * / %")
@proc(as, "asignación\n= += -= ++ --")
@proc(re, "relacionales y lógicos\n< == != && || !")
@hl(pr, "precedencia:\n( )  →  * / %  →  + -")
@sub(cv, "conversiones\nimplícita · static_cast")
@sub(cm, "<cmath>: sqrt pow sin\n<iomanip>: fixed setprecision")
@io(sq, "Estructura secuencial:\nentrada → proceso → salida")
ex -> ar; ex -> as; ex -> re; ex -> pr; ex -> cv; ex -> cm; ar -> sq [style=dashed]; cm -> sq [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1
| Fórmula | En C++ |
|---|---|
| a + b / 2 (promedio) | `(a + b) / 2.0` |
| x² | `x * x` o `pow(x, 2)` |
| √x | `sqrt(x)` |
| aᵇ | `pow(a, b)` |
| \|x\| | `fabs(x)` |
| sen(α), α en grados | `sin(alfa * PI / 180)` |
| ¿n es par? | `n % 2 == 0` |
| promedio exacto de enteros | `static_cast<double>(suma) / n` |
| 2 decimales | `cout << fixed << setprecision(2);` |
| bibliotecas | `<cmath>` (funciones), `<iomanip>` (formato) |

**Precedencia (de mayor a menor):** `()` → `++ -- !` (unarios) → `* / %` → `+ -` → `< <= > >=` → `== !=` → `&&` → `||` → `= += -= *= /=`.
:::

:::checklist | Guía de preguntas de rutina 2.2 · Antes de escribir una fórmula
<ul class="checks">
<li>¿Escribí la fórmula en papel e identifiqué datos de entrada, resultados y constantes?</li>
<li>¿Hay alguna división en la que ambos operandos sean enteros? ¿Debería dar decimales?</li>
<li>¿Puse paréntesis en numeradores y denominadores completos?</li>
<li>¿Las funciones trigonométricas reciben radianes?</li>
<li>¿Calculo cada resultado <b>después</b> de los valores que necesita?</li>
<li>¿Verifiqué el resultado con una calculadora (prueba de escritorio)?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) División entera escondida (error de lógica).** ¿Por qué el promedio de 7, 8 y 8 sale 7?

```cpp run
#include <iostream>
using namespace std;
int main()
{
    int a = 7, b = 8, c = 8;
    double promedio = (a + b + c) / 3;       //> 23 / 3 entre enteros = 7
    cout << "Promedio: " << promedio << "\n";
    return 0;
}
```
*Corrección:* `(a + b + c) / 3.0` o `static_cast<double>(a + b + c) / 3`.

**b) `^` como potencia (error de lógica).** El programa compila y calcula mal:

```cpp run
#include <iostream>
using namespace std;
int main()
{
    int lado = 3;
    cout << "Area: " << (lado ^ 2) << "\n";    //> ^ es XOR de bits: 3 XOR 2 = 1
    return 0;
}
```
*Corrección:* `lado * lado` o `pow(lado, 2)`.

**c) `%` con decimales (error de compilación).**

```cpp err
#include <iostream>
int main()
{
    double x = 7.5;
    std::cout << x % 2;
    return 0;
}
```
*Corrección:* `%` solo funciona con enteros; para decimales existe `fmod(x, 2)` de `<cmath>`.

**d) Precedencia olvidada.** `a + b / 2` no es el promedio; `9 / 5 * c` da `c`, no `1.8 · c`. Revisa la tabla de precedencia y usa paréntesis.

**e) Grados en lugar de radianes.** `cos(60)` no es 0.5: interpreta 60 **radianes**. Usa `cos(60 * PI / 180)`.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Distancia entre dos puntos | Variabilidad
El mismo esquema secuencial con otra fórmula: `d = √((x₂−x₁)² + (y₂−y₁)²)`.

```cpp run title="distancia.cpp" stdin="1 2\n4 6\n"
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    double x1, y1, x2, y2;
    cout << "Punto 1 (x y): ";
    cin >> x1 >> y1;                      //> Entrada
    cout << "Punto 2 (x y): ";
    cin >> x2 >> y2;
    double dx = x2 - x1;                  //> Proceso por partes: más fácil de verificar
    double dy = y2 - y1;
    double d = sqrt(dx * dx + dy * dy);
    cout << "Distancia: " << d << "\n";   //> Salida
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Ayuda completa en T1, parcial en T2–T3, ninguna en T4.

:::tarea A | T1. Calificación final ponderada: ejemplo y gemelo | 20 min | Ejemplo resuelto, Variabilidad
**Contexto.** (Adaptado de Betancourt y Polanco, cap. 2, ej. 6.) Las tres notas parciales valen 25 %, 30 % y 45 %. **¿Para qué?** Los promedios ponderados aparecen en calificaciones, encuestas y videojuegos.

**Paso 1 · Estudia:**

```cpp run title="nota_final.cpp" stdin="Mariana Diaz\n8.5 7 9.2\n"
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;
int main()
{
    const double P1 = 0.25, P2 = 0.30, P3 = 0.45;  //> Ponderaciones como constantes (suman 1)
    string nombre;
    double n1, n2, n3;
    cout << "Nombre: ";
    getline(cin, nombre);
    cout << "Tres notas parciales: ";
    cin >> n1 >> n2 >> n3;
    double final = n1 * P1 + n2 * P2 + n3 * P3;      //> Cada nota por su peso; `*` antes que `+`
    cout << fixed << setprecision(2);
    cout << nombre << ": nota final = " << final << "\n";
    return 0;
}
```

**Paso 2 · Gemelo.** En un juego de carreras, la puntuación de un auto es `50 %` velocidad, `30 %` manejo y `20 %` aceleración (cada valor de 0 a 100). Lee el nombre del auto y los tres valores, y muestra la puntuación con un decimal.

:::solucion | T1
```cpp run title="puntuacion_auto.cpp" stdin="Rayo Azul\n90 75 60\n"
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;
int main()
{
    const double PV = 0.50, PM = 0.30, PA = 0.20;
    string auto_nombre;
    double vel, man, ace;
    cout << "Nombre del auto: ";
    getline(cin, auto_nombre);
    cout << "Velocidad, manejo y aceleracion: ";
    cin >> vel >> man >> ace;
    double puntuacion = vel * PV + man * PM + ace * PA;
    cout << fixed << setprecision(1);
    cout << auto_nombre << ": " << puntuacion << " puntos\n";
    return 0;
}
```
:::
:::

:::tarea A | T2. Conversor de temperaturas inverso (completa con pistas) | 20 min | Problema por completar
**Contexto.** Una estación meteorológica de EE. UU. reporta en Fahrenheit y tu app debe mostrar Celsius y Kelvin. Fórmulas: `C = (F − 32) · 5/9`, `K = C + 273.15`.

```cpp blank title="fahrenheit.cpp"
#include <iostream>
#include __1__                          // 1: biblioteca de setprecision
using namespace std;
int main()
{
    double f, c, k;
    cout << "Temperatura en Fahrenheit: ";
    cin >> f;
    c = __2__ * 5 / 9.0;                // 2: la resta debe hacerse ANTES (parentesis)
    k = __3__;                          // 3: Kelvin a partir de Celsius
    cout << __4__ << setprecision(1);   // 4: manipulador para decimales fijos
    cout << "Celsius: " << c << "\nKelvin: " << k << "\n";
    return 0;
}
```

**Prueba:** `F = 98.6` → `C = 37.0`, `K = 310.1` (310.15 redondeado a un decimal).

:::solucion | T2
{{c:1}} `<iomanip>` · {{c:2}} `(f - 32)` · {{c:3}} `c + 273.15` · {{c:4}} `fixed`

```cpp run title="fahrenheit.cpp" stdin="98.6\n"
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    double f, c, k;
    cout << "Temperatura en Fahrenheit: ";
    cin >> f;
    c = (f - 32) * 5 / 9.0;
    k = c + 273.15;
    cout << fixed << setprecision(1);
    cout << "Celsius: " << c << "\nKelvin: " << k << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T3. La escalera y el edificio (completa sin pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** (Adaptado de Betancourt y Polanco, cap. 2, ej. 2.) Una escalera de longitud `h` (hipotenusa) se apoya en un edificio formando un ángulo `α` con el suelo. La distancia de la base de la escalera al edificio es `d = h · cos(α)`. Lee `h` en metros y `α` en grados.

```cpp blank title="escalera.cpp"
#include <iostream>
#include __1__
#include <iomanip>
using namespace std;
int main()
{
    const double PI = 3.14159265358979;
    double h, grados;
    cout << "Longitud de la escalera (m) y angulo (grados): ";
    cin >> h >> grados;
    double radianes = __2__;
    double d = __3__;
    cout << fixed << __4__;
    cout << "Distancia al edificio: " << d << " m\n";
    __5__
}
```

**Prueba:** `h = 5`, `α = 60°` → `d = 2.50 m`.

:::solucion | T3
{{c:1}} `<cmath>` · {{c:2}} `grados * PI / 180` · {{c:3}} `h * cos(radianes)` · {{c:4}} `setprecision(2)` · {{c:5}} `return 0;`

```cpp run title="escalera.cpp" stdin="5 60\n"
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main()
{
    const double PI = 3.14159265358979;
    double h, grados;
    cout << "Longitud de la escalera (m) y angulo (grados): ";
    cin >> h >> grados;
    double radianes = grados * PI / 180;
    double d = h * cos(radianes);
    cout << fixed << setprecision(2);
    cout << "Distancia al edificio: " << d << " m\n";
    return 0;
}
```
:::
:::

:::tarea AB | T4. Cambio en monedas (problema convencional) | 30 min | Variabilidad
**Contexto.** Una máquina expendedora devuelve el cambio con el **menor número de monedas** de $10, $5, $2 y $1. Lee la cantidad de cambio (entero) y muestra cuántas monedas de cada tipo entrega. **Pista conceptual:** `/` da cuántas caben; `%` da lo que sobra.

**Ejemplo:** cambio `38` → 3 de $10, 1 de $5, 1 de $2, 1 de $1.

Haz la **prueba de escritorio** con 38 y con 99 antes de ejecutar.

:::solucion | T4
```cpp run title="cambio.cpp" stdin="38\n"
#include <iostream>
using namespace std;
int main()
{
    int cambio;
    cout << "Cambio a entregar: $";
    cin >> cambio;
    int m10 = cambio / 10;   cambio = cambio % 10;   // 38 -> 3 monedas, quedan 8
    int m5  = cambio / 5;    cambio = cambio % 5;    // 8  -> 1 moneda,  quedan 3
    int m2  = cambio / 2;    cambio = cambio % 2;    // 3  -> 1 moneda,  queda 1
    int m1  = cambio;                                // 1  -> 1 moneda
    cout << "$10: " << m10 << "\n$5:  " << m5 << "\n$2:  " << m2 << "\n$1:  " << m1 << "\n";
    return 0;
}
```
Prueba de escritorio con 99: 9 de $10 (sobran 9), 1 de $5 (sobran 4), 2 de $2 (sobra 0), 0 de $1.
:::
:::

:::tarea A | T5. Todo lo que puedas calcular con un radio (solución libre) | 20 min | Solución libre
**Contexto.** Te dan solo esto: `double r = 5.0;` (centímetros). **Calcula y muestra todo lo que puedas** a partir de ese radio: diámetro, perímetro de la circunferencia, área del círculo, área de la superficie de una esfera, volumen de la esfera, volumen de un cilindro de altura igual al diámetro… No hay una lista obligatoria: cuantas más magnitudes encuentres (y verifiques con calculadora), mejor.

:::solucion | T5
Una solución posible:

```cpp run title="radio.cpp"
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    const double PI = 3.14159265358979;
    double r = 5.0;
    cout << fixed << setprecision(2);
    cout << "Diametro:           " << 2 * r << " cm\n";
    cout << "Perimetro:          " << 2 * PI * r << " cm\n";
    cout << "Area del circulo:   " << PI * r * r << " cm2\n";
    cout << "Superficie esfera:  " << 4 * PI * r * r << " cm2\n";
    cout << "Volumen esfera:     " << 4.0 / 3 * PI * r * r * r << " cm3\n";
    cout << "Volumen cilindro:   " << PI * r * r * (2 * r) << " cm3\n";
    return 0;
}
```
Observa `4.0 / 3`: con `4 / 3` el volumen saldría como `PI * r³` (error de división entera).
:::
:::

:::tarea B | T6. ¿Por qué da ese número? (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
Explica **cada** resultado de la salida. ¿Cuáles sorprenderían a alguien que solo sabe matemáticas?

```cpp run title="expresiones.cpp"
#include <iostream>
using namespace std;
int main()
{
    int x = 5;
    cout << 1 / 2 * 4.0 << "\n";
    cout << 4.0 * 1 / 2 << "\n";
    cout << 17 % 5 * 2 << "\n";
    cout << -7 / 2 << " " << -7 % 2 << "\n";
    int a = x++;
    int b = ++x;
    cout << a << " " << b << " " << x << "\n";
    cout << static_cast<int>(3.99) + 0.5 << "\n";
    return 0;
}
```

{{lineas:5}}

:::solucion | T6
1. `1 / 2 * 4.0` → `1 / 2` se evalúa primero entre enteros = `0`; `0 * 4.0 = 0`.
2. `4.0 * 1 / 2` → izquierda a derecha: `4.0 * 1 = 4.0`; `4.0 / 2 = 2`. Mismo operandos, otro orden, otro resultado.
3. `17 % 5 * 2` → igual precedencia, izquierda a derecha: `2 * 2 = 4`.
4. `-7 / 2 = -3` (la división entera trunca hacia cero) y `-7 % 2 = -1` (el residuo conserva el signo del dividendo).
5. `a = x++` guarda 5 y luego `x = 6`; `b = ++x` primero `x = 7` y guarda 7 → `5 7 7`.
6. `static_cast<int>(3.99)` trunca a `3`; `3 + 0.5 = 3.5`.
:::
:::

:::tarea B | T7. Imagina la fórmula general (imaginación) | 25 min | Imaginación
**Contexto.** (Adaptado de Betancourt y Polanco, cap. 2, ej. 5.) Las raíces de `ax² + bx + c = 0` son `x = (−b ± √(b² − 4ac)) / 2a`.

1. **Sin escribir código**, imagina y dibuja el **árbol de expresión** de `x₁`. ¿Cuál es la última operación? ¿Dónde hacen falta paréntesis en C++?
2. Imagina qué pasa si escribes `-b + sqrt(b*b - 4*a*c) / 2*a`. ¿Qué calcula realmente?
3. Programa el cálculo de ambas raíces (supón que `b² − 4ac ≥ 0`; en el Tema 04 aprenderás a verificarlo). Prueba con `a=1, b=−3, c=2`.

{{lineas:3}}

:::solucion | T7
1. La última operación es la **división** entre `(-b ± raíz)` y `(2a)`: ambos deben ir entre paréntesis.
2. `-b + sqrt(...) / 2*a` divide solo la raíz entre 2 y **multiplica** por `a`, y luego suma `-b`: es otra fórmula.

```cpp run title="cuadratica.cpp" stdin="1 -3 2\n"
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    double a, b, c;
    cout << "Coeficientes a b c: ";
    cin >> a >> b >> c;
    double disc = b * b - 4 * a * c;          // discriminante (se supone >= 0)
    double x1 = (-b + sqrt(disc)) / (2 * a);
    double x2 = (-b - sqrt(disc)) / (2 * a);
    cout << "x1 = " << x1 << "\nx2 = " << x2 << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T8. Calculadora de nutrientes (reto colaborativo) | 35 min | Memoria colectiva de trabajo, Variabilidad
**Contexto.** (Adaptado de Betancourt y Polanco, cap. 2, ej. 8.) En una dieta, los carbohidratos aportan el 55 % de las calorías, los lípidos el 30 % y las proteínas el 15 %. Cada gramo de carbohidrato aporta 4 kcal, de lípido 9 kcal y de proteína 4 kcal. Dada la dieta diaria en kcal, calcular los **gramos** de cada nutriente.

:::colab | Organización
Equipos de 3 con niveles mezclados. **Integrante 1:** carbohidratos; **2:** lípidos; **3:** proteínas. Cada uno escribe su fórmula en papel (`gramos = kcal_totales · porcentaje / kcal_por_gramo`), la explica al equipo y verifica con calculadora para 2000 kcal. Luego integran un solo programa con constantes para todos los porcentajes y aportes, y comparan con otro equipo.
:::

:::solucion | T8
```cpp run title="nutrientes.cpp" stdin="2000\n"
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    const double PCT_CARB = 0.55, PCT_LIP = 0.30, PCT_PROT = 0.15;
    const double KCAL_G_CARB = 4, KCAL_G_LIP = 9, KCAL_G_PROT = 4;
    double dieta;
    cout << "Dieta diaria (kcal): ";
    cin >> dieta;
    double carb = dieta * PCT_CARB / KCAL_G_CARB;
    double lip  = dieta * PCT_LIP  / KCAL_G_LIP;
    double prot = dieta * PCT_PROT / KCAL_G_PROT;
    cout << fixed << setprecision(1);
    cout << "Carbohidratos: " << carb << " g\nLipidos:       " << lip
         << " g\nProteinas:     " << prot << " g\n";
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Tiro parabólico (adaptado de Betancourt y Polanco, cap. 2, ej. 7) | Modalidad, Ejemplo resuelto
*Guion para narración segmentada (4 partes, ≈ 3–4 min). Mostrar en pantalla solo las fórmulas y el código; el estudiante controla la reproducción.*

**Problema:** «Calcular el alcance máximo `x = v² · sen(2α) / g` y la altura máxima `h = v² · sen²(α) / (2g)` de un proyectil, dados `v` (m/s) y `α` (grados)».

**Segmento 1 — Identificar entrada, proceso y salida.** {{como}} Subrayo en la fórmula lo que el usuario da (`v`, `α`), lo que es fijo (`g = 9.81`, `π`) y lo que debo mostrar (`x`, `h`). {{porque}} Así sé qué variables leer, cuáles declarar como constantes y cuáles calcular.

**Segmento 2 — La trampa de los grados.** {{como}} Antes de usar `sin`, convierto: `rad = alfa * PI / 180`. {{porque}} `sin` de `<cmath>` trabaja en radianes; si le paso 45 grados directamente calcula el seno de 45 radianes y el resultado no tiene sentido físico.

**Segmento 3 — Traducir sin ambigüedad.** {{como}} Escribo `sen²(α)` como `sin(rad) * sin(rad)` y el denominador completo entre paréntesis: `/ (2 * G)`. {{porque}} Sin paréntesis, `/ 2 * G` dividiría entre 2 y **multiplicaría** por `G`. Calcular `s = sin(rad)` una sola vez además hace el código más legible.

**Segmento 4 — Verificar con un caso conocido.** {{como}} Pruebo `v = 20`, `α = 45°`. Sé de física que a 45° el alcance es máximo: `400 · 1 / 9.81 ≈ 40.77 m`, y la altura, `400 · 0.5 / 19.62 ≈ 10.19 m`. {{porque}} Un caso cuya respuesta conozco me dice si el programa está bien antes de confiar en él con otros datos.

```cpp run title="proyectil.cpp" stdin="20 45\n"
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main()
{
    const double PI = 3.14159265358979, G = 9.81;
    double v, alfa;
    cout << "Velocidad inicial (m/s) y angulo (grados): ";
    cin >> v >> alfa;
    double rad = alfa * PI / 180;
    double s = sin(rad);
    double alcance = v * v * sin(2 * rad) / G;
    double altura = v * v * s * s / (2 * G);
    cout << fixed << setprecision(2);
    cout << "Alcance maximo: " << alcance << " m\nAltura maxima:  " << altura << " m\n";
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. ¿Cuánto vale `17 / 5` en C++? ¿Y `17 % 5`?
2. Ordena de mayor a menor precedencia: `+`, `()`, `*`, `=`.
3. ¿Qué biblioteca contiene `sqrt` y `pow`?
4. ¿A qué equivale `x *= 3`?
5. Verdadero o falso: `2 ^ 3` calcula 2 elevado a 3.
6. ¿Qué hacen `fixed` y `setprecision(2)` juntos?
7. ¿En qué unidad reciben su argumento `sin`, `cos` y `tan`?
8. ¿Qué escribe `static_cast<double>(7) / 2`?
9. ¿Qué operador lógico es verdadero solo si ambas condiciones lo son?
10. Describe con tus palabras qué es una estructura secuencial.
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida:**

```cpp check title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int a = 10, b = 4;
    double c = a / b;
    double d = a / 4.0;
    a += b * 2;
    b %= 3;
    cout << c << " " << d << " " << a << " " << b << "\n";
    return 0;
}
```

**P2. Traduce a C++** (usa `<cmath>` cuando haga falta): a) `y = (3x² − 2x + 1) / (x − 1)`; b) `r = √(a² + b²)`; c) el área de un triángulo con fórmula de Herón `A = √(s(s−a)(s−b)(s−c))`, con `s = (a+b+c)/2`.

**P3. Encuentra el error de lógica** y corrígelo: `double promedio = (n1 + n2 + n3 + n4) / 4;` con `n1…n4` enteros.

**P4. Escribe un programa** que lea el precio de un producto y el porcentaje de descuento, y muestre el monto del descuento, el subtotal, el IVA (16 % sobre el subtotal) y el total a pagar, con dos decimales.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Predigo el resultado de expresiones con división entera y residuo.</li>
<li>Traduzco fórmulas con paréntesis y funciones de <code>&lt;cmath&gt;</code>.</li>
<li>Muestro resultados con el número de decimales que pide el problema.</li>
<li>Organizo mis programas en entrada → proceso → salida y los verifico con una prueba de escritorio.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 `3` y `2` · 2 `()` → `*` → `+` → `=` · 3 `<cmath>` · 4 `x = x * 3` · 5 Falso (`^` es XOR; usa `pow(2, 3)`) · 6 Muestran los decimales en notación fija con exactamente 2 cifras decimales · 7 Radianes · 8 `3.5` · 9 `&&` · 10 Un conjunto de sentencias que se ejecutan una tras otra, en el orden escrito, sin decisiones ni repeticiones.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.**

```cpp run title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int a = 10, b = 4;
    double c = a / b;
    double d = a / 4.0;
    a += b * 2;
    b %= 3;
    cout << c << " " << d << " " << a << " " << b << "\n";
    return 0;
}
```

**P2.** a) `y = (3 * x * x - 2 * x + 1) / (x - 1);` b) `r = sqrt(a * a + b * b);` c) `s = (a + b + c) / 2.0; A = sqrt(s * (s - a) * (s - b) * (s - c));`

**P3.** División entera: usar `/ 4.0` o `static_cast<double>(n1 + n2 + n3 + n4) / 4`.

**P4.**

```cpp run title="p4.cpp" stdin="1200 15\n"
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    const double IVA = 0.16;
    double precio, pct;
    cout << "Precio y % de descuento: ";
    cin >> precio >> pct;
    double descuento = precio * pct / 100;
    double subtotal = precio - descuento;
    double iva = subtotal * IVA;
    double total = subtotal + iva;
    cout << fixed << setprecision(2);
    cout << "Descuento: $" << descuento << "\nSubtotal:  $" << subtotal
         << "\nIVA:       $" << iva << "\nTotal:     $" << total << "\n";
    return 0;
}
```
:::
