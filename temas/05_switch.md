---
num: "05"
archivo: "Tema05_Estructura_selectiva_switch"
titulo: "Estructura selectiva switch y menús de opciones"
corto: "switch y menús"
lema: "Cuando la pregunta tiene respuestas exactas y conocidas, switch abre directamente la puerta correcta."
duracion: "3 h · 2 sesiones de 1.5 h"
previos: "Tema 04 (if, if-else, escaleras y condiciones)."
fuentes:
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Cap. 4: Estructura selectiva switch (§4.1) y ejercicios resueltos (§4.2)."
  - "Lospinoso, J. (2019). *C++ Crash Course*. Cap. 2: Enumeration Types (enum class con switch). Cap. 8: switch Statements; Attributes (`[[fallthrough]]`)."
objetivos:
  A:
    - "Explicar cuándo conviene `switch` en lugar de una escalera `if-else` (valores discretos y conocidos)."
    - "Escribir `switch` con `case`, `break` y `default` sobre enteros y caracteres."
    - "Construir menús de opciones y agrupar varios `case` para una misma acción."
    - "Representar un `switch` con un diagrama de flujo de selección múltiple y con `Segun` en PSeInt."
  B:
    - "Usar `switch` con `enum class` y explicar su ventaja frente a los «números mágicos»."
    - "Explicar el *fall-through*: cuándo es un error y cuándo es intencional (`[[fallthrough]]`)."
    - "Transformar rangos en casos discretos (p. ej., `nota / 10`) y reconocer los límites de `switch`."
    - "Declarar variables dentro de un `case` usando un bloque `{ }`."
efectos:
  soporte:
    - ["Elementos aislados", "Motivación → anatomía → break → default → agrupar casos → char → límites → enum class."]
    - ["Atención dividida", "Diagrama de selección múltiple al lado del código; anotaciones en línea."]
    - ["Ejemplo resuelto", "Calculadora con menú de operador, incluida la división entre cero."]
    - ["Movimiento humano", "«switch humano»: el valor recorre puertas y se detiene donde hay un `break`."]
  procedimental:
    - ["Variabilidad", "Errores de compilación y de lógica en menús distintos."]
    - ["Autoexplicación", "«¿Qué se imprime sin `break`?» antes de cada corrección."]
  tareas:
    - ["Ejemplo resuelto", "T1: día de la semana + gemelo (nombre del mes)."]
    - ["Problema por completar", "T2 (cafetería, con pistas) y T3 (días del mes, sin pistas)."]
    - ["Desvanecimiento de guía", "T1 → T4."]
    - ["Solución libre", "T5: de calificación numérica a letra, de todas las formas posibles."]
    - ["Autoexplicación", "T6: máquina expendedora con errores de `break`."]
    - ["Imaginación", "T7: predecir un *fall-through* intencional y reescribirlo con `enum class`."]
    - ["Memoria colectiva de trabajo", "T8: cajero automático por equipos."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Anatomía de `switch`, `break`, `default`, casos agrupados, menús con números y letras."
    B: "`enum class`, `[[fallthrough]]`, bloques en `case`, transformación de rangos."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 con diagrama de flujo; pares mixtos."
    B: "T5 (versiones), T6, T7 autónomas; mentores en T8."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Convertidor de unidades con menú (T4)."
    B: "Versión con `enum class` de un menú (T7) y explicación del *fall-through*."
  Entorno:
    comp: "Información procedimental"
    A: "Plantilla de menú impresa; prueba de cada opción y de una opción inválida."
    B: "Compilación con `-Wall -Wextra` (avisa *fall-through* implícito con `-Wimplicit-fallthrough`)."
plan:
  - ["Apertura", "Soporte", "Pregunta: «¿cómo sabe un elevador a qué piso ir?». Comparar escalera vs switch.", "10 min"]
  - ["Desarrollo", "Soporte", "Conceptos 1–7; switch humano; ejemplo resuelto.", "50 min"]
  - ["Práctica guiada", "Tareas + procedimental", "Ruta A: T1 → T3. Ruta B: T5, T6, T7.", "50 min"]
  - ["Colaborativa", "Tareas", "T8 cajero automático.", "30 min"]
  - ["Autónoma", "Tareas", "T4 (todos).", "20 min"]
  - ["Cierre", "Protocolo + evaluación", "Protocolo verbal, tests y autorregistro.", "30 min"]
glosario:
  - ["selección múltiple", "multiway selection", "Elegir uno entre varios caminos según el valor de una expresión."]
  - ["etiqueta case", "case label", "Valor constante que marca la entrada a un camino del `switch`."]
  - ["caso por omisión", "default case", "Camino que se toma si ningún `case` coincide."]
  - ["romper", "break", "Sentencia que termina el `switch` (o un ciclo) inmediatamente."]
  - ["caída", "fall-through", "Continuar ejecutando el siguiente `case` por no haber `break`."]
  - ["enumeración", "enumeration (`enum class`)", "Tipo con un conjunto fijo de valores con nombre."]
  - ["número mágico", "magic number", "Literal sin nombre cuyo significado no es evidente (`if (op == 3)`)."]
  - ["menú", "menu", "Lista de opciones que el usuario elige por número o letra."]
  - ["expresión de control", "controlling expression", "Valor entero o carácter que evalúa el `switch`."]
  - ["atributo", "attribute", "Indicación al compilador entre `[[ ]]`, como `[[fallthrough]]`."]
---

# 1. Información de soporte {.soporte}

:::analogia | El tablero del elevador
En un elevador no preguntas «¿es el piso 1? ¿no? ¿es el 2? ¿no? ¿es el 3?…». Presionas el botón **4** y el elevador va **directo** al piso 4. Si presionas un botón que no existe, no pasa nada (o suena una alarma). `switch` funciona así: compara un valor con una lista de opciones **exactas** y salta directamente a la que coincide.
:::

:::pregunta
Piensa en el menú de un cajero automático: «1. Consultar saldo 2. Depositar 3. Retirar 4. Salir». **¿Cómo lo programarías con lo que sabes del Tema 04? ¿Cuántas comparaciones haría el programa en el peor caso?**

{{lineas:2}}
:::

:::relevancia
Menús de cajeros, máquinas expendedoras, opciones de un videojuego, comandos de un robot («A» avanza, «I» gira a la izquierda), estados de un semáforo: cuando las respuestas son **valores exactos y conocidos**, `switch` produce código más claro y fácil de ampliar que una larga escalera de `if`. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | ¿Por qué `switch`? Compara dos versiones | Elementos aislados, Atención dividida
<div class="cols eq">
<div>

```cpp check title="con escalera if"
#include <iostream>
int main()
{
    int op = 2;
    if (op == 1)
        std::cout << "Saldo\n";
    else if (op == 2)
        std::cout << "Deposito\n";
    else if (op == 3)
        std::cout << "Retiro\n";
    else
        std::cout << "Invalida\n";
    return 0;
}
```

</div>
<div>

```cpp check title="con switch"
#include <iostream>
int main()
{
    int op = 2;
    switch (op)
    {
        case 1: std::cout << "Saldo\n";    break;
        case 2: std::cout << "Deposito\n"; break;
        case 3: std::cout << "Retiro\n";   break;
        default: std::cout << "Invalida\n";
    }
    return 0;
}
```

</div>
</div>

Ambas hacen lo mismo. Con `switch`, la variable `op` se escribe **una sola vez** y cada opción queda alineada como en el menú real.
:::

:::concepto | 2 | Anatomía de `switch` | Elementos aislados, Atención dividida
```cpp run title="semaforo.cpp" runs="V|A|R|X"
#include <iostream>
using namespace std;
int main()
{
    char luz;
    cout << "Luz del semaforo (V/A/R): ";
    cin >> luz;
    switch (luz)                       //> Expresión de control: entero o carácter
    {                                  //> Las llaves agrupan todos los casos
        case 'V':                      //> `case` + valor CONSTANTE + dos puntos
            cout << "Avanza\n";
            break;                     //> `break` sale del switch
        case 'A':
            cout << "Precaucion\n";
            break;
        case 'R':
            cout << "Alto\n";
            break;
        default:                       //> Si ningún case coincide
            cout << "Luz desconocida\n";
    }
    cout << "Fin\n";                   //> Después de `break` se continúa aquí
    return 0;
}
```

```dot w="80%"
rankdir=TB; nodesep=0.3; ranksep=0.3;
@dec(s, "luz")
@proc(v, "Avanza")
@proc(a, "Precaución")
@proc(r, "Alto")
@proc(d, "Luz desconocida")
@pt(j)
@io(f, "Fin")
s -> v [label=" 'V'"]; s -> a [label=" 'A'"]; s -> r [label=" 'R'"]; s -> d [label=" default"];
v -> j [arrowhead=none]; a -> j [arrowhead=none]; r -> j [arrowhead=none]; d -> j [arrowhead=none]; j -> f;
```
:::

:::concepto | 3 | `break` y la «caída» (*fall-through*) | Elementos aislados, Atención dividida
`case` **no** es un bloque cerrado: es solo una **etiqueta de entrada**. Si no hay `break`, la ejecución **sigue cayendo** a los casos de abajo.

```cpp run stdin="2\n"
#include <iostream>
using namespace std;
int main()
{
    int op;
    cin >> op;
    switch (op)
    {
        case 1: cout << "Uno\n";     //> Sin break
        case 2: cout << "Dos\n";     //> Entra aquí con op = 2...
        case 3: cout << "Tres\n";    //> ...y sigue cayendo
        default: cout << "Otro\n";   //> ...hasta el final
    }
    return 0;
}
```
**Regla:** termina cada `case` con `break`, salvo que quieras la caída a propósito (concepto 5 y Ruta B).
:::

:::movimiento | El switch humano (10 min)
Cuatro estudiantes se paran en fila como «puertas»: `case 1`, `case 2`, `case 3`, `default`. Algunos llevan un letrero de **break**. Otro estudiante, el «valor», recibe una tarjeta (por ejemplo, 2), entra por la puerta con su número y cumple la acción de esa puerta (aplaudir, saltar…). Si la puerta **no** tiene letrero de *break*, debe seguir a la siguiente puerta y hacer también su acción. El grupo predice antes qué hará el «valor».
:::

:::concepto | 4 | `default`: la opción para todo lo demás | Elementos aislados
`default` se ejecuta si **ningún** `case` coincide. Es opcional, pero en menús es tu oportunidad de avisar «opción inválida». Normalmente va al final (y entonces no necesita `break`).
:::

:::concepto | 5 | Varios casos, una misma acción | Elementos aislados, Atención dividida
Escribir varias etiquetas seguidas es una caída **intencional** muy útil:

```cpp run runs="e|K|U"
#include <iostream>
using namespace std;
int main()
{
    char c;
    cout << "Letra: ";
    cin >> c;
    switch (c)
    {
        case 'a': case 'e': case 'i': case 'o': case 'u':   //> Cinco etiquetas, un solo camino
        case 'A': case 'E': case 'I': case 'O': case 'U':   //> Mayúsculas también
            cout << "Vocal\n";
            break;
        default:
            cout << "No es vocal\n";
    }
    return 0;
}
```
:::

:::concepto | 6 | Lo que `switch` no puede hacer | Elementos aislados
- La expresión debe ser **entera** (`int`, `char`, `bool`, `enum`): **no** `double` ni `string`.
- Cada `case` lleva un valor **constante** y **único**: no variables, no rangos (`case nota >= 9:` no existe).
- Para rangos usa `if-else`… o **transforma** el rango en un número: con calificaciones de 0 a 100, `nota / 10` produce 0…10 (ver T5).

```cpp err
#include <iostream>
#include <string>
int main()
{
    std::string cmd = "start";
    switch (cmd)
    {
        case "start": std::cout << "Inicio\n"; break;
    }
    return 0;
}
```
:::

:::concepto | 7 | Ruta B · `switch` con `enum class` | Elementos aislados, Reversión de la experiencia
El *C++ Crash Course* (cap. 2 y 8) combina `switch` con **enumeraciones**: tipos con un conjunto fijo de valores **con nombre**, que eliminan los números mágicos.

```cpp run
#include <iostream>
using namespace std;
enum class Raza { Dinosaurio, Mamut, Humano };      //> Tres valores posibles con nombre

int main()
{
    Raza r = Raza::Mamut;                           //> Se usa con el prefijo `Raza::`
    switch (r)
    {
        case Raza::Dinosaurio: cout << "Extinto hace 66 millones de anios\n"; break;
        case Raza::Mamut:      cout << "Extinto hace 4 mil anios\n";          break;
        case Raza::Humano:     cout << "Aun por aqui\n";                     break;
    }
    return 0;
}
```

Si quieres una caída intencional, márcala con `[[fallthrough]];` antes del siguiente `case`: el compilador ya no la tomará como un olvido. Y si necesitas declarar una variable dentro de un `case`, encierra ese `case` en llaves `{ }`.
:::

## 1.2 Ejemplo resuelto: calculadora con menú de operador

:::ejemplo | Calculadora de cuatro operaciones | Ejemplo resuelto, Atención dividida
**Problema.** Leer dos números y un operador (`+`, `-`, `*`, `/`) y mostrar el resultado. Si el operador no es válido, avisar. Si se divide entre cero, avisar en lugar de calcular.

**A. Algoritmo:** 1) Leer `a`, `op`, `b`. 2) Según `op`: sumar, restar, multiplicar o (si `b ≠ 0`) dividir. 3) En otro caso, «operador inválido».

<div class="cols">
<div>

**B. Pseudocódigo (PSeInt)**

```pseudo
Algoritmo Calculadora
    Leer a, op, b
    Segun op Hacer
        "+": Escribir a + b
        "-": Escribir a - b
        "*": Escribir a * b
        "/": Si b <> 0 Entonces
                 Escribir a / b
             SiNo
                 Escribir "Division entre cero"
             FinSi
        De Otro Modo:
            Escribir "Operador invalido"
    FinSegun
FinAlgoritmo
```

</div>
<div>

**Diagrama de flujo**

```dot
rankdir=TB; nodesep=0.15; ranksep=0.3;
@io(l, "Leer a, op, b")
@dec(s, "op")
@proc(su, "a + b")
@proc(re, "a − b")
@proc(mu, "a · b")
@dec(z, "b ≠ 0?")
@proc(di, "a / b")
@proc(e0, "Error: ÷0")
@proc(inv, "Inválido")
l -> s; s -> su [label="+"]; s -> re [label="−"]; s -> mu [label="*"]; s -> z [label="/"]; s -> inv [label="otro"];
z -> di [label="Sí"]; z -> e0 [label="No"];
```

</div>
</div>

**C. Código en C++**

```cpp run title="calculadora.cpp" runs="12 + 5|12 / 5|7 / 0|3 ^ 2"
#include <iostream>
using namespace std;
int main()
{
    double a, b;
    char op;
    cout << "Operacion (ej. 12 + 5): ";
    cin >> a >> op >> b;                  //> `cin` separa número, carácter y número
    switch (op)
    {
        case '+': cout << "= " << a + b << "\n"; break;
        case '-': cout << "= " << a - b << "\n"; break;
        case '*': cout << "= " << a * b << "\n"; break;
        case '/':
            if (b != 0)                         //> Un if DENTRO de un case: decisiones combinadas
                cout << "= " << a / b << "\n";
            else
                cout << "Error: division entre cero\n";
            break;
        default:
            cout << "Operador invalido: " << op << "\n";
    }
    return 0;
}
```

**D. Verificación.** Se probó una opción normal, una división, la división entre cero y un operador inválido: todos los caminos del diagrama.
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.18; ranksep=0.3;
@term(s, "switch (expresión entera)")
@proc(c, "case CONSTANTE:")
@proc(b, "break;\nsale del switch")
@proc(d, "default:\nningún case coincidió")
@proc(g, "case agrupados\n(caída intencional)")
@hl(no, "No: double, string,\nrangos, variables")
@sub(e, "enum class\n[[fallthrough]]")
s -> c; c -> b; s -> d; c -> g; s -> no [style=dashed]; s -> e [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1 · Plantilla de menú
```cpp run title="plantilla_menu.cpp" stdin="2\n"
#include <iostream>
using namespace std;
int main()
{
    int opcion;
    cout << "1. Opcion uno\n2. Opcion dos\n3. Salir\nElige: ";
    cin >> opcion;
    switch (opcion)
    {
        case 1:
            cout << "Elegiste uno\n";
            break;
        case 2:
            cout << "Elegiste dos\n";
            break;
        case 3:
            cout << "Hasta luego\n";
            break;
        default:
            cout << "Opcion invalida\n";
    }
    return 0;
}
```

| Situación | Patrón |
|---|---|
| Opción con número | `case 1:` |
| Opción con letra, sin importar mayúsculas | `case 'a': case 'A':` |
| Rango 0–100 en bloques de 10 | `switch (nota / 10) { case 10: case 9: … }` |
| Variable local dentro de un caso | `case 2: { int x = 5; … break; }` |
| Caída intencional (C++17) | `[[fallthrough]];` |
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿La expresión del <code>switch</code> es entera o <code>char</code> (no <code>double</code> ni <code>string</code>)?</li>
<li>¿Cada <code>case</code> tiene un valor constante, distinto de los demás, y termina en dos puntos?</li>
<li>¿Cada <code>case</code> termina con <code>break</code> (salvo caída intencional)?</li>
<li>¿Hay un <code>default</code> para opciones inválidas?</li>
<li>¿Los caracteres van entre comillas simples: <code>case 'A':</code>?</li>
<li>¿Probé cada opción y al menos una opción inválida?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Olvidar `break` (error de lógica).** ¿Por qué con la opción 1 aparecen dos mensajes?

```cpp run stdin="1\n"
#include <iostream>
using namespace std;
int main()
{
    int op;
    cin >> op;
    switch (op)
    {
        case 1: cout << "Cafe: $30\n";   //> Falta break
        case 2: cout << "Te: $25\n";  break;
        default: cout << "No disponible\n";
    }
    return 0;
}
```

**b) Valor repetido en dos `case`.**

```cpp err
#include <iostream>
int main()
{
    int op = 1;
    switch (op)
    {
        case 1: std::cout << "A\n"; break;
        case 1: std::cout << "B\n"; break;
    }
    return 0;
}
```

**c) Usar una variable como etiqueta.** Las etiquetas deben conocerse al compilar.

```cpp err
#include <iostream>
int main()
{
    int op = 1, limite = 3;
    switch (op)
    {
        case limite: std::cout << "Limite\n"; break;
    }
    return 0;
}
```
*Corrección:* `const int limite = 3;` o una escalera `if`.

**d) Declarar una variable en un `case` sin llaves.**

```cpp err
#include <iostream>
int main()
{
    int op = 2;
    switch (op)
    {
        case 1:
            int doble = op * 2;
            std::cout << doble;
            break;
        case 2:
            std::cout << "dos";
            break;
    }
    return 0;
}
```
*Corrección:* `case 1: { int doble = op * 2; std::cout << doble; break; }`.

**e) Comparar con `'1'` cuando se leyó un `int`** (o al revés): si `op` es `int`, usa `case 1:`; si es `char`, usa `case '1':`.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Comandos de un robot | Variabilidad
```cpp run title="robot.cpp" runs="A|i|X"
#include <iostream>
using namespace std;
int main()
{
    char cmd;
    cout << "Comando (A=avanzar, R=retroceder, I=izq, D=der): ";
    cin >> cmd;
    switch (cmd)
    {
        case 'A': case 'a': cout << "Motores hacia adelante\n"; break;
        case 'R': case 'r': cout << "Motores en reversa\n";     break;
        case 'I': case 'i': cout << "Girando a la izquierda\n"; break;
        case 'D': case 'd': cout << "Girando a la derecha\n";   break;
        default:            cout << "Comando desconocido\n";
    }
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Prueba **todas** las opciones de cada menú y al menos una inválida.

:::tarea A | T1. Día de la semana: estudia el ejemplo y resuelve el gemelo | 15 min | Ejemplo resuelto, Variabilidad
**Contexto.** Una app de calendario recibe el número de día (1 = lunes … 7 = domingo).

```cpp run title="dia.cpp" runs="3|7|9"
#include <iostream>
using namespace std;
int main()
{
    int d;
    cout << "Dia (1-7): ";
    cin >> d;
    switch (d)
    {
        case 1: cout << "Lunes\n";     break;   //> Una línea por caso: se lee como una tabla
        case 2: cout << "Martes\n";    break;
        case 3: cout << "Miercoles\n"; break;
        case 4: cout << "Jueves\n";    break;
        case 5: cout << "Viernes\n";   break;
        case 6: cout << "Sabado\n";    break;
        case 7: cout << "Domingo\n";   break;
        default: cout << "Dia invalido\n";      //> Cualquier otro número
    }
    return 0;
}
```

**Gemelo.** Escribe `mes.cpp`: lee un número de mes (1–12) y muestra su nombre; si no existe, «Mes inválido».

:::solucion | T1
```cpp run title="mes.cpp" runs="2|12|13"
#include <iostream>
using namespace std;
int main()
{
    int m;
    cout << "Mes (1-12): ";
    cin >> m;
    switch (m)
    {
        case 1:  cout << "Enero\n";      break;
        case 2:  cout << "Febrero\n";    break;
        case 3:  cout << "Marzo\n";      break;
        case 4:  cout << "Abril\n";      break;
        case 5:  cout << "Mayo\n";       break;
        case 6:  cout << "Junio\n";      break;
        case 7:  cout << "Julio\n";      break;
        case 8:  cout << "Agosto\n";     break;
        case 9:  cout << "Septiembre\n"; break;
        case 10: cout << "Octubre\n";    break;
        case 11: cout << "Noviembre\n";  break;
        case 12: cout << "Diciembre\n";  break;
        default: cout << "Mes invalido\n";
    }
    return 0;
}
```
:::
:::

:::tarea A | T2. Menú de la cafetería (completa con pistas) | 20 min | Problema por completar
**Contexto.** La cafetería escolar quiere un menú en su pantalla táctil. El cliente elige producto y cantidad; el programa muestra el total.

```cpp blank title="cafeteria.cpp"
#include <iostream>
using namespace std;
int main()
{
    int opcion, cantidad;
    double precio = 0;
    cout << "1. Torta $35\n2. Jugo $20\n3. Fruta $15\nOpcion y cantidad: ";
    cin >> opcion >> cantidad;
    __1__ (opcion)                         // 1: palabra clave de seleccion multiple
    {
        case 1: precio = 35; __2__;        // 2: termina este caso
        __3__ 2: precio = 20; break;       // 3: etiqueta
        case 3: precio = 15; break;
        __4__:                             // 4: opcion por omision
            cout << "Opcion invalida\n";
    }
    if (precio > 0)
        cout << "Total: $" << __5__ << "\n";   // 5: expresion del total
    return 0;
}
```

:::solucion | T2
{{c:1}} `switch` · {{c:2}} `break` · {{c:3}} `case` · {{c:4}} `default` · {{c:5}} `precio * cantidad`

```cpp run title="cafeteria.cpp" runs="1 2|3 4|5 1"
#include <iostream>
using namespace std;
int main()
{
    int opcion, cantidad;
    double precio = 0;
    cout << "1. Torta $35\n2. Jugo $20\n3. Fruta $15\nOpcion y cantidad: ";
    cin >> opcion >> cantidad;
    switch (opcion)
    {
        case 1: precio = 35; break;
        case 2: precio = 20; break;
        case 3: precio = 15; break;
        default:
            cout << "Opcion invalida\n";
    }
    if (precio > 0)
        cout << "Total: $" << precio * cantidad << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T3. ¿Cuántos días tiene el mes? (completa sin pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Una agenda necesita saber cuántos días tiene un mes. Usa casos **agrupados** y reutiliza la condición de año bisiesto del Tema 04 (T3).

```cpp blank title="dias_mes.cpp"
#include <iostream>
using namespace std;
int main()
{
    int mes, anio;
    cout << "Mes y anio: ";
    cin >> mes >> anio;
    switch (mes)
    {
        case 1: case 3: case 5: case 7: __1__ case 10: case 12:
            cout << "31 dias\n";
            __2__
        case 4: case 6: __3__ case 11:
            cout << "30 dias\n";
            break;
        case 2:
            if (__4__)
                cout << "29 dias\n";
            else
                cout << "28 dias\n";
            break;
        __5__
            cout << "Mes invalido\n";
    }
    return 0;
}
```

:::solucion | T3
{{c:1}} `case 8:` · {{c:2}} `break;` · {{c:3}} `case 9:` · {{c:4}} `(anio % 4 == 0 && anio % 100 != 0) || anio % 400 == 0` · {{c:5}} `default:`

```cpp run title="dias_mes.cpp" runs="8 2025|9 2025|2 2024|2 1900|14 2025"
#include <iostream>
using namespace std;
int main()
{
    int mes, anio;
    cout << "Mes y anio: ";
    cin >> mes >> anio;
    switch (mes)
    {
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            cout << "31 dias\n";
            break;
        case 4: case 6: case 9: case 11:
            cout << "30 dias\n";
            break;
        case 2:
            if ((anio % 4 == 0 && anio % 100 != 0) || anio % 400 == 0)
                cout << "29 dias\n";
            else
                cout << "28 dias\n";
            break;
        default:
            cout << "Mes invalido\n";
    }
    return 0;
}
```
:::
:::

:::tarea AB | T4. Convertidor de unidades (problema convencional) | 30 min | Variabilidad
**Contexto.** Diseña un convertidor con menú: `1` kilómetros → millas (× 0.621371), `2` kilogramos → libras (× 2.20462), `3` Celsius → Fahrenheit, `4` litros → galones (× 0.264172). El usuario elige la opción y escribe el valor; el programa muestra el resultado con dos decimales o «Opción inválida». Usa constantes para los factores.

:::solucion | T4
```cpp run title="convertidor.cpp" runs="1 42.195|3 36.5|4 50|7 1"
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    const double KM_MI = 0.621371, KG_LB = 2.20462, L_GAL = 0.264172;
    int op;
    double v;
    cout << "1) km->mi 2) kg->lb 3) C->F 4) L->gal\nOpcion y valor: ";
    cin >> op >> v;
    cout << fixed << setprecision(2);
    switch (op)
    {
        case 1: cout << v << " km = " << v * KM_MI << " mi\n"; break;
        case 2: cout << v << " kg = " << v * KG_LB << " lb\n"; break;
        case 3: cout << v << " C = " << 9.0 / 5 * v + 32 << " F\n"; break;
        case 4: cout << v << " L = " << v * L_GAL << " gal\n"; break;
        default: cout << "Opcion invalida\n";
    }
    return 0;
}
```
:::
:::

:::tarea A | T5. De número a letra: todas las formas (solución libre) | 25 min | Solución libre
**Contexto.** Una calificación de 0 a 100 se convierte en letra: 90–100 → A, 80–89 → B, 70–79 → C, 60–69 → D, menos de 60 → F. **Encuentra todas las soluciones que puedas**: con escalera `if`, con `switch` usando un truco para convertir rangos en valores exactos, con casos agrupados… Compara: ¿cuál te parece más clara?

:::solucion | T5
Dos de las soluciones posibles. La clave del `switch` es `nota / 10`: 87 / 10 = 8 (división entera).

```cpp run title="letra.cpp" runs="100|87|60|42"
#include <iostream>
using namespace std;
int main()
{
    int nota;
    cin >> nota;
    // Version 1: escalera
    char l1;
    if (nota >= 90) l1 = 'A';
    else if (nota >= 80) l1 = 'B';
    else if (nota >= 70) l1 = 'C';
    else if (nota >= 60) l1 = 'D';
    else l1 = 'F';
    // Version 2: switch sobre nota / 10 con casos agrupados
    char l2;
    switch (nota / 10)
    {
        case 10: case 9: l2 = 'A'; break;
        case 8: l2 = 'B'; break;
        case 7: l2 = 'C'; break;
        case 6: l2 = 'D'; break;
        default: l2 = 'F';
    }
    cout << "Escalera: " << l1 << "  switch: " << l2 << "\n";
    return 0;
}
```
:::
:::

:::tarea B | T6. La máquina expendedora rebelde (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
**Contexto.** Con la opción `B` la máquina entrega papas **y** galletas **y** dice «opción inválida». Con la `c` minúscula no entrega nada. **Explica** cada comportamiento y corrige el programa.

```cpp run title="expendedora_bug.cpp" runs="B|c"
#include <iostream>
using namespace std;
int main()
{
    char sel;
    cout << "Seleccion: ";
    cin >> sel;
    switch (sel)
    {
        case 'A': cout << "Refresco\n"; break;
        case 'B': cout << "Papas\n";
        case 'C': cout << "Galletas\n";
        default: cout << "Opcion invalida\n";
    }
    return 0;
}
```

{{lineas:3}}

:::solucion | T6
Con `B` entra en `case 'B'` y, sin `break`, **cae** en `case 'C'` y en `default`. Con `c` no coincide con `'C'` (C++ distingue mayúsculas) y llega a `default`… que en la salida sí aparece: «Opción inválida», pero el usuario esperaba galletas. Corrección: `break` en cada caso y etiquetas para minúsculas.

```cpp run title="expendedora.cpp" runs="B|c|z"
#include <iostream>
using namespace std;
int main()
{
    char sel;
    cout << "Seleccion: ";
    cin >> sel;
    switch (sel)
    {
        case 'A': case 'a': cout << "Refresco\n"; break;
        case 'B': case 'b': cout << "Papas\n";    break;
        case 'C': case 'c': cout << "Galletas\n"; break;
        default: cout << "Opcion invalida\n";
    }
    return 0;
}
```
:::
:::

:::tarea B | T7. Niveles de acceso (imaginación + `enum class`) | 25 min | Imaginación
**Contexto.** En un juego, cada rol tiene los permisos de los roles inferiores **más** los suyos. El programa usa una caída **intencional**.

1. **Imagina** (sin ejecutar) qué imprime para `nivel = 2`, `nivel = 0` y `nivel = 5`.
2. Reescríbelo con `enum class Rol { Invitado, Jugador, Moderador, Admin };` y marca las caídas con `[[fallthrough]];`.

```cpp check title="permisos.cpp"
#include <iostream>
using namespace std;
int main()
{
    int nivel;
    cin >> nivel;
    switch (nivel)
    {
        case 3: cout << "- Borrar servidores\n";
        case 2: cout << "- Expulsar jugadores\n";
        case 1: cout << "- Chatear\n";
        case 0: cout << "- Ver partidas\n"; break;
        default: cout << "Nivel desconocido\n";
    }
    return 0;
}
```

{{lineas:3}}

:::solucion | T7
`nivel = 2` → Expulsar, Chatear, Ver partidas · `nivel = 0` → Ver partidas · `nivel = 5` → Nivel desconocido.

```cpp run title="permisos_enum.cpp"
#include <iostream>
using namespace std;
enum class Rol { Invitado, Jugador, Moderador, Admin };
int main()
{
    Rol r = Rol::Moderador;
    switch (r)
    {
        case Rol::Admin:
            cout << "- Borrar servidores\n";
            [[fallthrough]];
        case Rol::Moderador:
            cout << "- Expulsar jugadores\n";
            [[fallthrough]];
        case Rol::Jugador:
            cout << "- Chatear\n";
            [[fallthrough]];
        case Rol::Invitado:
            cout << "- Ver partidas\n";
            break;
    }
    return 0;
}
```
:::
:::

:::tarea AB | T8. Cajero automático (reto colaborativo) | 30 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Equipos de 4 con niveles mezclados. Saldo inicial: `double saldo = 2500;`. Cada integrante programa **una opción** del menú y la explica al equipo: **1** consultar saldo, **2** depositar (rechaza montos ≤ 0), **3** retirar (rechaza montos ≤ 0, mayores al saldo o no múltiplos de 50), **4** salir. El equipo integra las opciones en un solo `switch`, diseña una tabla de casos de prueba (al menos 7) y la intercambia con otro equipo.
:::

*En el Tema 06 este cajero repetirá el menú hasta elegir «Salir».*

:::solucion | T8
```cpp run title="cajero.cpp" runs="1|2 800|3 120|3 3000|3 500|9"
#include <iostream>
using namespace std;
int main()
{
    double saldo = 2500, monto;
    int op;
    cout << "1) Saldo 2) Depositar 3) Retirar 4) Salir: ";
    cin >> op;
    switch (op)
    {
        case 1:
            cout << "Saldo: $" << saldo << "\n";
            break;
        case 2:
            cin >> monto;
            if (monto > 0) { saldo += monto; cout << "Nuevo saldo: $" << saldo << "\n"; }
            else cout << "Monto invalido\n";
            break;
        case 3:
            cin >> monto;
            if (monto <= 0 || static_cast<int>(monto) % 50 != 0)
                cout << "El retiro debe ser positivo y multiplo de 50\n";
            else if (monto > saldo)
                cout << "Fondos insuficientes\n";
            else { saldo -= monto; cout << "Retire su efectivo. Saldo: $" << saldo << "\n"; }
            break;
        case 4:
            cout << "Gracias por su visita\n";
            break;
        default:
            cout << "Opcion invalida\n";
    }
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Calculadora de áreas con menú | Modalidad, Ejemplo resuelto
*Guion segmentado para narración (≈ 3 min) con el código en pantalla.*

**Problema:** «Menú: 1 cuadrado, 2 rectángulo, 3 círculo. Según la figura, pedir sus medidas y mostrar el área».

**Segmento 1 — ¿switch o if?** {{como}} Veo que la decisión depende de un **número exacto** (1, 2 o 3), no de rangos. {{porque}} Eso es justo lo que `switch` hace mejor: cada opción del menú se convierte en un `case` y el código se lee como el menú.

**Segmento 2 — Lecturas dentro de cada caso.** {{como}} Cada figura pide datos distintos, así que pongo los `cin` **dentro** de su `case` y declaro las variables antes del `switch`. {{porque}} Si declarara `double r` dentro del `case 3` sin llaves, el compilador se quejaría de que otros casos «saltan» su inicialización.

**Segmento 3 — No olvidar `break`.** {{como}} Escribo el `break` de cada caso **antes** de escribir su contenido. {{porque}} Es el error más común en `switch`: sin él, el cuadrado también calcularía el rectángulo con datos basura.

**Segmento 4 — La opción que nadie elige.** {{como}} Agrego `default` y pruebo con 1, 2, 3 y 8. {{porque}} Los usuarios se equivocan; un menú sin `default` simplemente no responde y parece descompuesto.

```cpp run title="areas.cpp" runs="1 4|2 3 5|3 2|8"
#include <iostream>
using namespace std;
int main()
{
    const double PI = 3.14159265358979;
    int fig;
    double a, b;
    cout << "1) Cuadrado 2) Rectangulo 3) Circulo: ";
    cin >> fig;
    switch (fig)
    {
        case 1:
            cin >> a;
            cout << "Area: " << a * a << "\n";
            break;
        case 2:
            cin >> a >> b;
            cout << "Area: " << a * b << "\n";
            break;
        case 3:
            cin >> a;
            cout << "Area: " << PI * a * a << "\n";
            break;
        default:
            cout << "Figura invalida\n";
    }
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. ¿De qué tipos puede ser la expresión de un `switch`?
2. ¿Qué hace `break` dentro de un `switch`?
3. ¿Qué ocurre si un `case` no termina con `break`?
4. ¿Cuándo se ejecuta `default`?
5. Verdadero o falso: se puede escribir `case nota >= 90:`.
6. ¿Cómo haces que las opciones `'s'` y `'S'` ejecuten lo mismo?
7. ¿Qué palabra usa PSeInt para la selección múltiple?
8. ¿Para qué sirve `[[fallthrough]];`?
9. Menciona una ventaja de `enum class` sobre usar números (1, 2, 3) como opciones.
10. ¿Por qué `switch (nota / 10)` permite trabajar con rangos de calificaciones?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida** para `x = 2` y para `x = 4`:

```cpp check title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int x;
    cin >> x;
    switch (x)
    {
        case 1: cout << "A";
        case 2: cout << "B";
        case 3: cout << "C"; break;
        case 4: cout << "D";
        default: cout << "E";
    }
    cout << "\n";
    return 0;
}
```

**P2. Corrige** los tres errores:

```cpp blank title="p2.cpp"
char t;
cin >> t;
switch (t) {
    case "a": cout << "alfa"; break;
    case 'b' cout << "beta"; break;
    case 'a': cout << "otra alfa"; break;
}
```

**P3. Convierte a `switch`** esta escalera: `if (c == 'x' || c == 'X') cout << "salir"; else if (c == 'g') cout << "guardar"; else cout << "?";`

**P4. Escribe un programa** de «piedra, papel o tijera» contra la computadora, que siempre elige **piedra**: el usuario teclea `R`, `P` o `T` y el programa dice si gana, pierde o empata (o «jugada inválida»).
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Decido cuándo usar <code>switch</code> y cuándo una escalera <code>if</code>.</li>
<li>Escribo menús con <code>case</code>, <code>break</code> y <code>default</code>.</li>
<li>Agrupo casos y entiendo la caída cuando falta <code>break</code>.</li>
<li>Pruebo todas las opciones y una inválida.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 Enteros: `int`, `char`, `bool`, `long`, enumeraciones · 2 Termina el `switch` y continúa después de su llave de cierre · 3 La ejecución «cae» al siguiente `case` · 4 Cuando ningún `case` coincide · 5 Falso: los `case` llevan valores constantes, no condiciones · 6 `case 's': case 'S':` seguidos · 7 `Segun … Hacer … FinSegun` · 8 Indica que la caída al siguiente caso es intencional (evita el aviso del compilador) · 9 Los valores tienen nombre (`Rol::Admin`), el código se autodocumenta y el compilador detecta valores inválidos · 10 La división entera convierte cada rango de 10 en un solo número exacto (87 → 8).
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.**

```cpp run title="p1.cpp" runs="2|4"
#include <iostream>
using namespace std;
int main()
{
    int x;
    cin >> x;
    switch (x)
    {
        case 1: cout << "A";
        case 2: cout << "B";
        case 3: cout << "C"; break;
        case 4: cout << "D";
        default: cout << "E";
    }
    cout << "\n";
    return 0;
}
```

**P2.** `"a"` es cadena → `'a'`; falta `:` en `case 'b'`; `case 'a'` está repetido (eliminar o cambiar el valor).

**P3.** `switch (c) { case 'x': case 'X': cout << "salir"; break; case 'g': cout << "guardar"; break; default: cout << "?"; }`

**P4.**

```cpp run title="ppt.cpp" runs="P|r|T|Z"
#include <iostream>
using namespace std;
int main()
{
    char j;
    cout << "Tu jugada (R=piedra, P=papel, T=tijera): ";
    cin >> j;
    cout << "La computadora eligio piedra. ";
    switch (j)
    {
        case 'R': case 'r': cout << "Empate\n"; break;
        case 'P': case 'p': cout << "Ganaste: papel envuelve piedra\n"; break;
        case 'T': case 't': cout << "Perdiste: piedra rompe tijera\n"; break;
        default: cout << "Jugada invalida\n";
    }
    return 0;
}
```
:::
