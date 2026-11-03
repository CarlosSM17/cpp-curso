---
num: "04"
archivo: "Tema04_Estructuras_selectivas_if"
titulo: "Estructuras selectivas: if, if-else y decisiones anidadas"
corto: "if, if-else y anidados"
lema: "Los programas también deciden: si se cumple una condición toman un camino; si no, toman otro."
duracion: "4 h · 2 sesiones de 2 h"
previos: "Tema 03 (operadores relacionales y lógicos, expresiones)."
fuentes:
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Cap. 3: Estructuras selectivas if, if-else, if anidados (§3.1–§3.4). Cap. 2, ej. 3 y 5 (validación y fórmula general)."
  - "Lospinoso, J. (2019). *C++ Crash Course*. Cap. 1: Conditional Statements. Cap. 7: Logical Operators, Ternary Conditional Operator. Cap. 8: Selection Statements (if statements, init-statements)."
objetivos:
  A:
    - "Escribir condiciones con operadores relacionales (`< > <= >= == !=`) y lógicos (`&& || !`)."
    - "Usar `if`, `if-else` y la escalera `if-else if-else` para elegir entre caminos."
    - "Representar decisiones con diagramas de flujo y pseudocódigo (`Si … Entonces … SiNo`)."
    - "Validar datos de entrada y diseñar casos de prueba que recorran todos los caminos."
  B:
    - "Diseñar decisiones anidadas y transformarlas en escaleras o condiciones compuestas equivalentes."
    - "Usar el operador ternario `?:` y el `if` con inicializador de C++17."
    - "Explicar la evaluación en cortocircuito y aplicar las leyes de De Morgan."
    - "Evitar errores clásicos: `=` vs `==`, `;` tras el `if`, *else* colgante, comparación de `double`."
efectos:
  soporte:
    - ["Elementos aislados", "Condición → `if` → `if-else` → bloques → escalera → anidados → condiciones compuestas → ternario."]
    - ["Atención dividida", "Cada forma de `if` se presenta con su diagrama de flujo al lado del código equivalente."]
    - ["Ejemplo resuelto", "Fórmula general con discriminante: tres caminos, con ejecuciones para cada caso."]
    - ["Movimiento humano", "Diagrama de flujo en el piso: los estudiantes «caminan» los caminos con tarjetas de datos."]
  procedimental:
    - ["Variabilidad", "Errores frecuentes con ejemplos en distintos contextos (temperaturas, edades, rangos)."]
    - ["Autoexplicación", "Preguntas «¿qué camino toma?» antes de mostrar la ejecución."]
  tareas:
    - ["Ejemplo resuelto", "T1: aprobado/reprobado resuelto + gemelo (subir de nivel)."]
    - ["Problema por completar", "T2 (tarifa de cine, con pistas) y T3 (año bisiesto, sin pistas)."]
    - ["Desvanecimiento de guía", "T1 → T4."]
    - ["Solución libre", "T5: el mayor de tres números con todas las soluciones posibles."]
    - ["Autoexplicación", "T6: explicar y corregir un clasificador con errores."]
    - ["Imaginación", "T7: imaginar el camino de varios datos en `if` anidados."]
    - ["Memoria colectiva de trabajo", "T8: sistema de costos de envío por equipos."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "`if`, `if-else`, escalera y anidados básicos, siempre con diagrama de flujo."
    B: "Cortocircuito, De Morgan, ternario, `if` con inicializador, comparación de `double`."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 con tabla de casos de prueba guiada; pares mixtos."
    B: "T5 (variantes avanzadas), T6, T7 autónomas; mentores en T8."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Clasificador de triángulos (T4) con tabla de pruebas que cubre todos los caminos."
    B: "Versión anidada y versión escalera del mismo programa (T7) con justificación."
  Entorno:
    comp: "Información procedimental"
    A: "Diagramas de flujo en papel antes de codificar; depurador con puntos de interrupción."
    B: "Compilar con `-Wall` para detectar `=` en condiciones y paréntesis sospechosos."
plan:
  - ["Apertura", "Soporte", "Pregunta: «¿cómo decide un semáforo inteligente cuándo cambiar?». Analogía del cruce de caminos.", "10 min"]
  - ["Desarrollo 1", "Soporte", "Conceptos 1–4 con diagramas de flujo; diagrama de flujo en el piso.", "40 min"]
  - ["Desarrollo 2", "Soporte", "Conceptos 5–8; ejemplo resuelto de la fórmula general.", "30 min"]
  - ["Práctica guiada", "Tareas + procedimental", "Ruta A: T1 → T3. Ruta B: T3, T6, T7.", "60 min"]
  - ["Colaborativa", "Tareas", "T8 en equipos.", "30 min"]
  - ["Autónoma", "Tareas", "T4 (todos) y T5.", "30 min"]
  - ["Cierre", "Protocolo + evaluación", "Protocolo verbal, tests y autorregistro.", "40 min"]
glosario:
  - ["estructura selectiva", "selection statement", "Sentencia que elige qué código ejecutar según una condición."]
  - ["condición", "condition", "Expresión que se evalúa como `true` o `false`."]
  - ["rama / camino", "branch", "Cada bloque alternativo de una decisión."]
  - ["bloque", "block / compound statement", "Grupo de sentencias entre llaves `{ }`."]
  - ["decisión anidada", "nested if", "Un `if` dentro de otro `if`."]
  - ["escalera if-else", "else-if chain", "Secuencia `if … else if … else` para rangos o casos excluyentes."]
  - ["operador ternario", "ternary conditional operator", "`condicion ? valor1 : valor2`."]
  - ["cortocircuito", "short-circuit evaluation", "`&&` y `||` dejan de evaluar en cuanto conocen el resultado."]
  - ["tabla de verdad", "truth table", "Resultado de un operador lógico para todas las combinaciones."]
  - ["caso de prueba", "test case", "Entrada concreta con su salida esperada."]
  - ["valor frontera", "boundary value", "Valor justo en el límite de un rango (p. ej., 6 al aprobar con 6)."]
  - ["validación", "input validation", "Comprobar que los datos de entrada tienen sentido antes de usarlos."]
---

# 1. Información de soporte {.soporte}

:::analogia | Un cruce de caminos con letrero
Vas en bicicleta y llegas a un cruce con un letrero: «**Si** llueve, toma el camino techado; **si no**, toma el parque». No recorres ambos caminos: **evalúas** la condición (¿llueve?) y eliges **uno**. Después, los dos caminos se vuelven a unir y sigues tu recorrido. Una estructura selectiva hace exactamente eso con las sentencias de un programa.
:::

:::pregunta
Un videojuego muestra «GAME OVER» cuando tu vida llega a cero. **¿Cómo crees que el programa «sabe» en qué momento mostrarlo?** ¿Qué tendría que comparar?

{{lineas:2}}
:::

:::relevancia
Validar una contraseña, aplicar un descuento solo a clientes frecuentes, decidir si un sensor de temperatura debe encender un ventilador, determinar si un personaje fue golpeado: **toda la lógica de los programas reales se construye con decisiones**. Como dice el modelo ARCS, los condicionales son esenciales en inteligencia artificial y en videojuegos. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | La condición: una pregunta de sí o no | Elementos aislados
Una **condición** es una expresión que vale `true` o `false`. Se construye con operadores relacionales y lógicos (Tema 03):

| Condición en C++ | Se lee | Con `x = 7` |
|---|---|---|
| `x > 5` | x es mayor que 5 | `true` |
| `x == 10` | x es igual a 10 | `false` |
| `x % 2 == 0` | x es par | `false` |
| `x >= 1 && x <= 10` | x está entre 1 y 10 | `true` |
| `x < 0 \|\| x > 100` | x está fuera de 0..100 | `false` |
| `!(x == 7)` | x **no** es 7 | `false` |
:::

:::concepto | 2 | `if`: hacer algo solo si se cumple | Elementos aislados, Atención dividida
<div class="cols">
<div>

```cpp run runs="38.7|36.2"
#include <iostream>
using namespace std;
int main()
{
    double temp;
    cout << "Temperatura: ";
    cin >> temp;
    if (temp > 38.0)                //> Condición entre paréntesis
    {
        cout << "Tienes fiebre\n";  //> Solo si la condición es true
    }
    cout << "Fin de la revision\n"; //> Siempre se ejecuta
    return 0;
}
```

</div>
<div>

```dot
rankdir=TB; nodesep=0.3; ranksep=0.25;
@io(l, "Leer temp")
@dec(d, "temp > 38?")
@proc(s, "Mostrar\n\"Tienes fiebre\"")
@pt(j)
@io(f, "Mostrar\n\"Fin de la revision\"")
l -> d; d -> s [label=" Sí"]; s -> j [arrowhead=none]; d -> j [label=" No", arrowhead=none]; j -> f;
```

</div>
</div>
:::

:::concepto | 3 | `if-else`: elegir entre dos caminos | Elementos aislados, Atención dividida
<div class="cols">
<div>

```cpp run runs="8|13"
#include <iostream>
using namespace std;
int main()
{
    int n;
    cout << "Numero: ";
    cin >> n;
    if (n % 2 == 0)            //> ¿El residuo entre 2 es cero?
    {
        cout << n << " es PAR\n";   //> Camino del Sí
    }
    else
    {
        cout << n << " es IMPAR\n"; //> Camino del No
    }
    return 0;
}
```

</div>
<div>

```dot
rankdir=TB; nodesep=0.4; ranksep=0.28;
@io(l, "Leer n")
@dec(d, "n % 2 == 0?")
@proc(p, "Mostrar PAR")
@proc(i, "Mostrar IMPAR")
@pt(j)
@term(f, "Fin")
l -> d; d -> p [label=" Sí"]; d -> i [label=" No"]; p -> j [arrowhead=none]; i -> j [arrowhead=none]; j -> f;
```

</div>
</div>

En pseudocódigo (PSeInt): `Si n MOD 2 = 0 Entonces … SiNo … FinSi`.
:::

:::concepto | 4 | Bloques y llaves: ¿qué pertenece al `if`? | Elementos aislados
Sin llaves, el `if` controla **solo la siguiente sentencia**. La indentación no cuenta para el compilador:

```cpp run
#include <iostream>
using namespace std;
int main()
{
    int vida = 50;
    if (vida <= 0)
        cout << "GAME OVER\n";           //> Esta línea SÍ pertenece al if
        cout << "Reiniciando nivel...\n"; //> Esta NO: se ejecuta siempre, aunque esté indentada
    return 0;
}
```

**Regla del curso:** usa siempre llaves `{ }`, aunque el bloque tenga una sola sentencia.
:::

:::concepto | 5 | La escalera `if-else if-else`: rangos y casos excluyentes | Elementos aislados, Atención dividida
Cuando hay más de dos caminos, se encadenan decisiones. Se evalúan **de arriba abajo** y se ejecuta **solo el primer** bloque cuya condición sea verdadera.

<div class="cols">
<div>

```cpp run runs="9.5|7.8|6|4.5"
#include <iostream>
using namespace std;
int main()
{
    double nota;
    cout << "Calificacion (0-10): ";
    cin >> nota;
    if (nota >= 9)                 //> 1.ª pregunta
        cout << "Excelente\n";
    else if (nota >= 8)            //> Solo se pregunta si NO fue >= 9
        cout << "Muy bien\n";
    else if (nota >= 6)            //> Aquí ya sabemos que nota < 8
        cout << "Aprobado\n";
    else                           //> Todos los demás casos
        cout << "Reprobado\n";
    return 0;
}
```

</div>
<div>

```dot
rankdir=TB; nodesep=0.25; ranksep=0.2;
@dec(a, "nota >= 9?")
@dec(b, "nota >= 8?")
@dec(c, "nota >= 6?")
@proc(e, "Excelente")
@proc(m, "Muy bien")
@proc(ap, "Aprobado")
@proc(r, "Reprobado")
a -> e [label=" Sí"]; a -> b [label=" No"];
b -> m [label=" Sí"]; b -> c [label=" No"];
c -> ap [label=" Sí"]; c -> r [label=" No"];
{rank=same; a; e;} {rank=same; b; m;} {rank=same; c; ap;}
```

</div>
</div>

Observa que la condición de «Muy bien» no necesita `nota < 9`: si llegó ahí, ya se sabe.
:::

:::concepto | 6 | Decisiones anidadas: una decisión dentro de otra | Elementos aislados, Atención dividida
A veces la segunda pregunta **solo tiene sentido** si la primera fue verdadera:

```cpp run runs="S 19|S 15|N 20"
#include <iostream>
using namespace std;
int main()
{
    char boleto;
    int edad;
    cout << "Tiene boleto (S/N) y edad: ";
    cin >> boleto >> edad;
    if (boleto == 'S')                          //> Decisión externa
    {
        if (edad >= 18)                         //> Decisión interna: solo se evalúa si hay boleto
            cout << "Acceso a zona general\n";
        else
            cout << "Acceso con acompaniante\n";
    }
    else
    {
        cout << "Primero compra tu boleto\n";
    }
    return 0;
}
```

```dot w="60%"
rankdir=TB; nodesep=0.35; ranksep=0.3;
@dec(b, "boleto == 'S'?")
@dec(e, "edad >= 18?")
@proc(g, "Zona general")
@proc(a, "Con acompañante")
@proc(c, "Compra boleto")
b -> e [label="Sí"]; b -> c [label="No"]; e -> g [label="Sí"]; e -> a [label="No"];
```
:::

:::concepto | 7 | Condiciones compuestas y cortocircuito | Elementos aislados
| A | B | `A && B` | `A \|\| B` | `!A` |
|---|---|---|---|---|
| true | true | true | true | false |
| true | false | false | true | false |
| false | true | false | true | true |
| false | false | false | false | true |

**Cortocircuito:** en `A && B`, si `A` es falso, `B` **ni se evalúa** (el resultado ya es falso). En `A || B`, si `A` es verdadero, `B` no se evalúa. Por eso `if (d != 0 && n / d > 2)` es seguro: nunca divide entre cero.

**Rangos:** en matemáticas se escribe `0 < x < 10`; en C++ **debe** escribirse `0 < x && x < 10`.

**De Morgan (Ruta B):** `!(A && B)` equivale a `!A || !B`; `!(A || B)` equivale a `!A && !B`.
:::

:::concepto | 8 | Ruta B · Operador ternario e `if` con inicializador | Elementos aislados, Reversión de la experiencia
El **operador ternario** elige entre dos **valores**: `condicion ? valor_si : valor_no`. El *C++ Crash Course* (cap. 8) muestra además el `if` con inicializador de C++17, que limita la variable al `if`:

```cpp run stdin="15\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    int n;
    cin >> n;
    string tipo = (n % 2 == 0) ? "par" : "impar";       //> Ternario: elige un valor
    cout << n << " es " << tipo << "\n";
    if (int resto = n % 3; resto == 0)                  //> `resto` solo existe dentro de este if/else
        cout << "multiplo de 3\n";
    else
        cout << "residuo " << resto << " al dividir entre 3\n";
    return 0;
}
```
:::

:::movimiento | Diagrama de flujo en el piso (15 min)
Con cinta adhesiva, dibuja en el piso el diagrama de la escalera de calificaciones (concepto 5): rombos para las decisiones y rectángulos para los mensajes. Cada estudiante recibe una tarjeta con una calificación (9.5, 8, 7.9, 6, 5.99…) y **camina** el diagrama: en cada rombo lee la condición en voz alta y decide hacia dónde avanzar. El grupo verifica en qué rectángulo termina cada uno. Las tarjetas con valores frontera (8, 6) son las más interesantes.
:::

## 1.2 Ejemplo resuelto: la fórmula general, ahora con decisiones

:::ejemplo | Raíces de una ecuación cuadrática según el discriminante | Ejemplo resuelto, Atención dividida
**Problema.** En el Tema 03 (T7) supusimos que `b² − 4ac ≥ 0`. Ahora el programa debe decidir: si el discriminante es **positivo** hay dos raíces reales; si es **cero**, una raíz doble; si es **negativo**, raíces complejas. Además, si `a = 0` no es cuadrática.

**A. Algoritmo:** 1) Leer `a, b, c`. 2) Si `a = 0`, avisar y terminar. 3) Calcular `d = b² − 4ac`. 4) Según el signo de `d`, calcular y mostrar las raíces que correspondan.

<div class="cols">
<div>

**B. Pseudocódigo**

```pseudo
Algoritmo Cuadratica
    Leer a, b, c
    Si a = 0 Entonces
        Escribir "No es cuadratica"
    SiNo
        d <- b^2 - 4*a*c
        Si d > 0 Entonces
            Escribir (-b+RC(d))/(2*a), (-b-RC(d))/(2*a)
        SiNo
            Si d = 0 Entonces
                Escribir -b/(2*a)
            SiNo
                Escribir "Raices complejas"
            FinSi
        FinSi
    FinSi
FinAlgoritmo
```

</div>
<div>

**Diagrama de flujo**

```dot
rankdir=TB; nodesep=0.22; ranksep=0.22;
@io(l, "Leer a, b, c")
@dec(q, "a == 0?")
@proc(nq, "No es cuadrática")
@proc(dd, "d ← b² − 4ac")
@dec(p, "d > 0?")
@proc(dos, "Dos raíces reales")
@dec(z, "d == 0?")
@proc(una, "Raíz doble")
@proc(cx, "Raíces complejas")
l -> q; q -> nq [label=" Sí"]; q -> dd [label=" No"]; dd -> p;
p -> dos [label=" Sí"]; p -> z [label=" No"]; z -> una [label=" Sí"]; z -> cx [label=" No"];
```

</div>
</div>

**C. Código en C++**

```cpp run title="cuadratica_v2.cpp" runs="1 -3 2|1 2 1|1 1 1|0 2 3"
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    double a, b, c;
    cout << "Coeficientes a b c: ";
    cin >> a >> b >> c;
    if (a == 0)                                   //> Validación: sin `a` no hay término cuadrático
    {
        cout << "No es una ecuacion cuadratica\n";
    }
    else
    {
        double d = b * b - 4 * a * c;             //> Solo se calcula si a != 0
        if (d > 0)                                //> Escalera con los tres casos del discriminante
        {
            double x1 = (-b + sqrt(d)) / (2 * a);
            double x2 = (-b - sqrt(d)) / (2 * a);
            cout << "Dos raices reales: " << x1 << " y " << x2 << "\n";
        }
        else if (d == 0)
        {
            cout << "Raiz doble: " << -b / (2 * a) << "\n";
        }
        else
        {
            double re = -b / (2 * a), im = sqrt(-d) / (2 * a);   //> sqrt de un número positivo: -d > 0
            cout << "Raices complejas: " << re << " +/- " << im << "i\n";
        }
    }
    return 0;
}
```

**D. Verificación.** Se eligió **un caso de prueba por cada camino** del diagrama: `d > 0`, `d = 0`, `d < 0` y `a = 0`. Así se comprueba que todas las ramas funcionan.
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.18; ranksep=0.3;
@term(s, "Estructuras\nselectivas")
@proc(c, "Condición\nrelacionales + lógicos")
@proc(i1, "if\n(un camino opcional)")
@proc(i2, "if-else\n(dos caminos)")
@proc(i3, "escalera else-if\n(rangos excluyentes)")
@proc(i4, "anidados\n(decisión dentro de decisión)")
@sub(t, "ternario ?:\nif con inicializador")
@hl(p, "Probar cada camino\n+ valores frontera")
s -> c; s -> i1; s -> i2; s -> i3; s -> i4; s -> t; i3 -> p [style=dashed]; i4 -> p [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1
```cpp check title="formas_if.cpp"
#include <iostream>
int main()
{
    int x = 5;
    // 1) if simple
    if (x > 0) {
        std::cout << "positivo\n";
    }
    // 2) if-else
    if (x % 2 == 0) {
        std::cout << "par\n";
    } else {
        std::cout << "impar\n";
    }
    // 3) escalera
    if (x < 0) {
        std::cout << "negativo\n";
    } else if (x == 0) {
        std::cout << "cero\n";
    } else {
        std::cout << "positivo\n";
    }
    // 4) ternario
    int absx = (x < 0) ? -x : x;
    std::cout << absx << "\n";
    return 0;
}
```

| En lenguaje natural | En C++ |
|---|---|
| x está entre 10 y 20 (inclusive) | `x >= 10 && x <= 20` |
| x está fuera de 10..20 | `x < 10 \|\| x > 20` |
| c es una vocal minúscula | `c == 'a' \|\| c == 'e' \|\| c == 'i' \|\| c == 'o' \|\| c == 'u'` |
| n es múltiplo de 3 y de 5 | `n % 3 == 0 && n % 5 == 0` |
| dos `double` son «iguales» | `fabs(a - b) < 1e-9` |
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿Dibujé el diagrama de flujo o escribí la tabla de casos antes de codificar?</li>
<li>¿Comparo con <code>==</code> (dos signos) y no con <code>=</code>?</li>
<li>¿Hay un <code>;</code> justo después del paréntesis del <code>if</code>? (No debe haberlo.)</li>
<li>¿Cada bloque tiene llaves <code>{ }</code>?</li>
<li>En una escalera, ¿los rangos no se traslapan ni dejan huecos? ¿Está el caso más restrictivo primero?</li>
<li>¿Escribí los rangos como <code>a &lt; x &amp;&amp; x &lt; b</code>?</li>
<li>¿Probé <b>un caso por camino</b> y los <b>valores frontera</b> (justo en el límite)?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) `=` en lugar de `==`.** ¿Por qué dice «aprobado» con un 4?

```cpp run stdin="4\n"
#include <iostream>
using namespace std;
int main()
{
    int nota;
    cin >> nota;
    if (nota = 10)                   //> ASIGNA 10 a nota; el valor 10 (≠ 0) cuenta como true
        cout << "Calificacion perfecta: " << nota << "\n";
    return 0;
}
```
*Corrección:* `if (nota == 10)`. Con `-Wall`, g++ advierte: *suggest parentheses around assignment used as truth value*.

**b) Punto y coma después del `if`.** El `;` es una sentencia vacía: el bloque siguiente se ejecuta siempre.

```cpp run stdin="25\n"
#include <iostream>
using namespace std;
int main()
{
    int temp;
    cin >> temp;
    if (temp > 30);                  //> Este `;` termina el if: no controla nada
    {
        cout << "Hace calor\n";      //> Se ejecuta siempre, aun con 25
    }
    return 0;
}
```

**c) Rango al estilo matemático.** `0 < x < 10` compila, pero se evalúa como `(0 < x) < 10`; `0 < x` vale 0 o 1, y ambos son menores que 10: **siempre verdadero**.

```cpp run stdin="50\n"
#include <iostream>
using namespace std;
int main()
{
    int x;
    cin >> x;
    if (0 < x < 10)                  //> (0 < 50) es 1, y 1 < 10 es true
        cout << x << " esta entre 0 y 10 (?)\n";
    return 0;
}
```
*Corrección:* `if (0 < x && x < 10)`.

**d) Orden equivocado en la escalera.** Si la primera pregunta es `nota >= 6`, nadie llega a «Excelente»: pon primero el caso **más restrictivo**.

**e) `else` sin `if`.** Un `;` o una llave mal puesta separa el `else` de su `if`:

```cpp err
#include <iostream>
int main()
{
    int x = 3;
    if (x > 0);
        std::cout << "positivo\n";
    else
        std::cout << "no positivo\n";
    return 0;
}
```
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Costo de envío por peso | Variabilidad
Mismo patrón que la escalera de calificaciones, otro contexto:

```cpp run title="envio.cpp" runs="0.8|3|12.5|-1"
#include <iostream>
using namespace std;
int main()
{
    double kg;
    cout << "Peso del paquete (kg): ";
    cin >> kg;
    if (kg <= 0)                     //> Validación primero
        cout << "Peso invalido\n";
    else if (kg <= 1)
        cout << "Costo: $99\n";
    else if (kg <= 5)
        cout << "Costo: $149\n";
    else
        cout << "Costo: $149 + $20 por kg extra = $" << 149 + (kg - 5) * 20 << "\n";
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Para cada tarea, escribe primero tu **tabla de casos de prueba**: una fila por camino y otra por cada valor frontera.

:::tarea A | T1. ¿Aprobado o reprobado? Estudia y resuelve el gemelo | 20 min | Ejemplo resuelto, Variabilidad
**Contexto.** El sistema escolar muestra si un alumno aprobó (calificación mínima: 6). **¿Para qué?** Es la decisión más simple: una condición, dos caminos.

```cpp run title="aprobado.cpp" runs="7.5|6|5.9"
#include <iostream>
using namespace std;
int main()
{
    const double MINIMA = 6.0;                //> Constante: el criterio puede cambiar sin tocar la lógica
    double cal;
    cout << "Calificacion: ";
    cin >> cal;
    if (cal >= MINIMA)                        //> `>=`: el 6 exacto también aprueba (valor frontera)
    {
        cout << "APROBADO\n";
    }
    else
    {
        cout << "REPROBADO, te faltan " << MINIMA - cal << " puntos\n";
    }
    return 0;
}
```

**Gemelo.** En un videojuego, el jugador **sube de nivel** si su experiencia es de al menos 1000 puntos; si no, se le muestra cuántos le faltan. Prueba con 1500, 1000 y 730.

:::solucion | T1
```cpp run title="nivel.cpp" runs="1500|1000|730"
#include <iostream>
using namespace std;
int main()
{
    const int EXP_NIVEL = 1000;
    int exp;
    cout << "Experiencia: ";
    cin >> exp;
    if (exp >= EXP_NIVEL)
    {
        cout << "SUBISTE DE NIVEL!\n";
    }
    else
    {
        cout << "Te faltan " << EXP_NIVEL - exp << " puntos\n";
    }
    return 0;
}
```
:::
:::

:::tarea A | T2. Tarifa del cine (completa con pistas) | 20 min | Problema por completar
**Contexto.** Un cine cobra $50 a menores de 12 años, $40 a personas de 60 años o más y $80 al resto. Las edades negativas son inválidas.

```cpp blank title="cine.cpp"
#include <iostream>
using namespace std;
int main()
{
    int edad;
    cout << "Edad: ";
    cin >> edad;
    if (__1__)                      // 1: primero valida (edad negativa)
        cout << "Edad invalida\n";
    else if (__2__)                 // 2: ninos
        cout << "Boleto: $50\n";
    __3__ (edad >= 60)              // 3: palabra(s) para continuar la escalera
        cout << "Boleto: $40\n";
    __4__                           // 4: todos los demas casos
        cout << "Boleto: $80\n";
    return 0;
}
```

**Casos de prueba:** −3, 0, 11, 12, 59, 60, 75.

:::solucion | T2
{{c:1}} `edad < 0` · {{c:2}} `edad < 12` · {{c:3}} `else if` · {{c:4}} `else`

```cpp run title="cine.cpp" runs="-3|11|12|59|60"
#include <iostream>
using namespace std;
int main()
{
    int edad;
    cout << "Edad: ";
    cin >> edad;
    if (edad < 0)
        cout << "Edad invalida\n";
    else if (edad < 12)
        cout << "Boleto: $50\n";
    else if (edad >= 60)
        cout << "Boleto: $40\n";
    else
        cout << "Boleto: $80\n";
    return 0;
}
```
:::
:::

:::tarea AB | T3. ¿Año bisiesto? (completa sin pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Un año es bisiesto si es divisible entre 4 **y no** entre 100, **o bien** si es divisible entre 400. Las apps de calendario lo usan para saber si febrero tiene 29 días.

```cpp blank title="bisiesto.cpp"
#include <iostream>
using namespace std;
int main()
{
    int anio;
    cout << "Anio: ";
    cin >> anio;
    bool bisiesto = (anio % 4 __1__ 0 __2__ anio % 100 __3__ 0) __4__ anio % 400 == 0;
    __5__ (bisiesto)
        cout << anio << " es bisiesto: febrero tiene 29 dias\n";
    __6__
        cout << anio << " no es bisiesto: febrero tiene 28 dias\n";
    return 0;
}
```

**Casos de prueba:** 2024 (sí), 2023 (no), 1900 (no), 2000 (sí).

:::solucion | T3
{{c:1}} `==` · {{c:2}} `&&` · {{c:3}} `!=` · {{c:4}} `||` · {{c:5}} `if` · {{c:6}} `else`

```cpp run title="bisiesto.cpp" runs="2024|2023|1900|2000"
#include <iostream>
using namespace std;
int main()
{
    int anio;
    cout << "Anio: ";
    cin >> anio;
    bool bisiesto = (anio % 4 == 0 && anio % 100 != 0) || anio % 400 == 0;
    if (bisiesto)
        cout << anio << " es bisiesto: febrero tiene 29 dias\n";
    else
        cout << anio << " no es bisiesto: febrero tiene 28 dias\n";
    return 0;
}
```
:::
:::

:::tarea AB | T4. Clasificador de triángulos (problema convencional) | 30 min | Variabilidad
**Contexto.** Una app de geometría recibe tres lados. Primero debe **validar** que formen un triángulo (cada lado menor que la suma de los otros dos y todos positivos). Si lo forman, lo clasifica en **equilátero** (3 lados iguales), **isósceles** (exactamente 2 iguales) o **escaleno** (todos distintos).

Entrega: diagrama de flujo, tabla de casos de prueba (al menos 5, incluyendo uno inválido) y el programa.

:::solucion | T4
```cpp run title="triangulos.cpp" runs="3 3 3|5 5 8|4 5 6|1 2 10"
#include <iostream>
using namespace std;
int main()
{
    double a, b, c;
    cout << "Lados a b c: ";
    cin >> a >> b >> c;
    bool valido = a > 0 && b > 0 && c > 0 && a < b + c && b < a + c && c < a + b;
    if (!valido)
    {
        cout << "No forman un triangulo\n";
    }
    else
    {
        if (a == b && b == c)
            cout << "Equilatero\n";
        else if (a == b || b == c || a == c)
            cout << "Isosceles\n";
        else
            cout << "Escaleno\n";
    }
    return 0;
}
```
Observa que «isósceles» no necesita excluir explícitamente el equilátero: ese caso ya se atendió antes en la escalera.
:::
:::

:::tarea A | T5. El mayor de tres: todas las soluciones que puedas (solución libre) | 25 min | Solución libre
**Contexto.** Lee tres enteros y muestra el mayor. **No hay una solución única:** escribe **todas las versiones distintas que se te ocurran** (con `if` anidados, con escalera y `&&`, con una variable auxiliar que «recuerda» el mayor, con el operador ternario…). Después compáralas: ¿cuál tiene menos comparaciones? ¿cuál es más fácil de extender a cuatro números?

:::solucion | T5
Tres de las muchas soluciones posibles:

```cpp run title="mayor_tres.cpp" stdin="7 19 4\n"
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int a, b, c;
    cin >> a >> b >> c;
    // Version 1: escalera con condiciones compuestas
    if (a >= b && a >= c)
        cout << "V1: " << a << "\n";
    else if (b >= a && b >= c)
        cout << "V1: " << b << "\n";
    else
        cout << "V1: " << c << "\n";
    // Version 2: variable auxiliar (la mas facil de extender)
    int mayor = a;
    if (b > mayor) mayor = b;
    if (c > mayor) mayor = c;
    cout << "V2: " << mayor << "\n";
    // Version 3: ternario anidado y std::max de la biblioteca
    int m3 = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
    cout << "V3: " << m3 << "  max: " << max({a, b, c}) << "\n";
    return 0;
}
```
:::
:::

:::tarea B | T6. El clasificador de temperaturas con errores (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
**Contexto.** Un compañero programó un clasificador: «congelación» (≤ 0), «frío» (1–15), «templado» (16–25), «calor» (> 25). Con 20 °C el programa muestra mensajes incorrectos. Encuentra **los cuatro errores**, explica por qué cada uno produce el comportamiento observado y corrígelos.

```cpp run title="clasificador_bug.cpp" stdin="20\n"
#include <iostream>
using namespace std;
int main()
{
    int t;
    cin >> t;
    if (t <= 0);
        cout << "Congelacion\n";
    if (1 <= t <= 15)
        cout << "Frio\n";
    else if (t >= 15 && t <= 25)
        cout << "Templado\n";
    else if (t = 26)
        cout << "Calor\n";
    return 0;
}
```

{{lineas:4}}

:::solucion | T6
1. Línea 7: `;` después del `if` → «Congelación» se muestra siempre.
2. Línea 9: `1 <= t <= 15` es siempre verdadera (se compara 0/1 con 15) → muestra «Frío» con 20 y el resto de la escalera nunca se evalúa.
3. Línea 11: el rango de templado empieza en 15 y se traslapa con frío; debe ser `t >= 16` (o simplemente `else if (t <= 25)`).
4. Línea 13: `t = 26` asigna; además «calor» es `t > 25`. Basta un `else`.

```cpp run title="clasificador.cpp" runs="-4|10|20|31"
#include <iostream>
using namespace std;
int main()
{
    int t;
    cin >> t;
    if (t <= 0)
        cout << "Congelacion\n";
    else if (t <= 15)
        cout << "Frio\n";
    else if (t <= 25)
        cout << "Templado\n";
    else
        cout << "Calor\n";
    return 0;
}
```
:::
:::

:::tarea B | T7. ¿Qué camino toma? (imaginación) | 20 min | Imaginación
**Sin ejecutar**, imagina el recorrido de cada entrada por las decisiones y escribe la salida esperada. Luego **reescribe** el programa como una escalera `if-else if` sin anidamiento y verifica que ambas versiones den lo mismo.

```cpp check title="caminos.cpp"
#include <iostream>
using namespace std;
int main()
{
    int x, y;
    cin >> x >> y;
    if (x > 0)
    {
        if (y > 0)
            cout << "Cuadrante I\n";
        else
            cout << "Cuadrante IV o eje\n";
    }
    else
    {
        if (y > 0)
            cout << "Cuadrante II o eje\n";
        else
            cout << "Cuadrante III o eje\n";
    }
    return 0;
}
```

Entradas: `3 5` · `3 -2` · `-1 4` · `0 0` · `-2 -2`

{{lineas:3}}

:::solucion | T7
`3 5` → I · `3 -2` → IV o eje · `-1 4` → II o eje · `0 0` → III o eje · `-2 -2` → III o eje. Versión en escalera con condiciones compuestas:

```cpp run title="caminos_escalera.cpp" runs="3 5|3 -2|-1 4|0 0|-2 -2"
#include <iostream>
using namespace std;
int main()
{
    int x, y;
    cin >> x >> y;
    if (x > 0 && y > 0)
        cout << "Cuadrante I\n";
    else if (x > 0)
        cout << "Cuadrante IV o eje\n";
    else if (y > 0)
        cout << "Cuadrante II o eje\n";
    else
        cout << "Cuadrante III o eje\n";
    return 0;
}
```
:::
:::

:::tarea AB | T8. Sistema de costos de envío (reto colaborativo) | 35 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Equipos de 3–4, niveles mezclados. Cada integrante diseña **una dimensión** de la decisión y la explica al equipo antes de integrarla.
:::

**Reglas del negocio:**

- **Peso:** hasta 1 kg $100; hasta 5 kg $180; más de 5 kg $180 + $25 por kg adicional.
- **Destino:** `N` nacional (sin recargo) o `I` internacional (+80 % sobre el costo por peso).
- **Servicio express** (`S`/`N`): +$150 fijos.
- **Validación:** peso ≤ 0 o destino distinto de N/I → «Datos inválidos».

**Producto del equipo:** diagrama de flujo, tabla con **al menos 8 casos de prueba** que recorran todos los caminos y el programa integrado. Intercambien tablas con otro equipo y ejecuten sus casos.

:::solucion | T8
```cpp run title="envios.cpp" runs="0.5 N N|3 I S|8 N S|-2 N N|2 X N"
#include <iostream>
using namespace std;
int main()
{
    double kg;
    char destino, express;
    cout << "Peso, destino (N/I) y express (S/N): ";
    cin >> kg >> destino >> express;
    if (kg <= 0 || (destino != 'N' && destino != 'I'))
    {
        cout << "Datos invalidos\n";
    }
    else
    {
        double costo;
        if (kg <= 1)
            costo = 100;
        else if (kg <= 5)
            costo = 180;
        else
            costo = 180 + (kg - 5) * 25;
        if (destino == 'I')
            costo = costo * 1.80;
        if (express == 'S')
            costo += 150;
        cout << "Costo total: $" << costo << "\n";
    }
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Una experta programa los descuentos de una tienda | Modalidad, Ejemplo resuelto
*Guion para narración segmentada (≈ 3–4 min), con el diagrama de flujo y el código en pantalla.*

**Problema:** «Si la compra supera $1000 y el cliente es frecuente: 20 % de descuento. Si solo supera $1000: 10 %. Si es frecuente pero compra $1000 o menos: 5 %. En otro caso, sin descuento».

**Segmento 1 — Tabla antes que código.** {{como}} Hago una tabla con las dos preguntas (¿> 1000? ¿frecuente?) y sus cuatro combinaciones, y escribo el descuento de cada una. {{porque}} Dos condiciones de sí/no producen exactamente cuatro casos; la tabla me garantiza que no olvido ninguno.

**Segmento 2 — Orden de la escalera.** {{como}} Pongo primero el caso más restrictivo: `monto > 1000 && frecuente`. Luego `monto > 1000`, después `frecuente` y al final `else`. {{porque}} En una escalera gana la primera condición verdadera; si preguntara primero `monto > 1000`, un cliente frecuente con $1500 recibiría solo 10 %.

**Segmento 3 — Leer el «sí/no».** {{como}} Leo la respuesta como `char` y la convierto en `bool frecuente = (resp == 'S' || resp == 's');`. {{porque}} Así la escalera queda legible y acepto mayúscula o minúscula.

**Segmento 4 — Probar fronteras.** {{como}} Pruebo $1500 S, $1500 N, $1000 S (¡justo en el límite!) y $800 N. {{porque}} El valor 1000 decide si se usa `>` o `>=`; el enunciado dice «supera», así que 1000 **no** recibe el descuento por monto.

```cpp run title="descuentos.cpp" runs="1500 S|1500 N|1000 S|800 N"
#include <iostream>
using namespace std;
int main()
{
    double monto;
    char resp;
    cout << "Monto y cliente frecuente (S/N): ";
    cin >> monto >> resp;
    bool frecuente = (resp == 'S' || resp == 's');
    double pct;
    if (monto > 1000 && frecuente)
        pct = 0.20;
    else if (monto > 1000)
        pct = 0.10;
    else if (frecuente)
        pct = 0.05;
    else
        pct = 0.0;
    cout << "Descuento: " << pct * 100 << "%  Total: $" << monto * (1 - pct) << "\n";
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. ¿Qué diferencia hay entre `=` y `==`?
2. ¿Cuántos bloques se ejecutan, como máximo, en una escalera `if-else if-else`?
3. Escribe la condición «`x` está entre 1 y 100, inclusive».
4. Completa la tabla: `true && false` = \_\_\_ · `true || false` = \_\_\_ · `!true` = \_\_\_
5. Verdadero o falso: sin llaves, un `if` controla todas las líneas indentadas debajo de él.
6. ¿Qué es la evaluación en cortocircuito?
7. ¿Qué símbolo representa una decisión en un diagrama de flujo?
8. ¿Qué valor guarda `r` en `int r = (5 > 3) ? 10 : 20;`?
9. ¿Qué es un valor frontera y por qué conviene probarlo?
10. ¿Cómo se escribe en PSeInt la estructura `if-else`?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida** para `n = 15` y para `n = 8`:

```cpp check title="p1.cpp"
#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    if (n % 3 == 0 && n % 5 == 0)
        cout << "FizzBuzz\n";
    else if (n % 3 == 0)
        cout << "Fizz\n";
    else if (n % 5 == 0)
        cout << "Buzz\n";
    else
        cout << n << "\n";
    return 0;
}
```

**P2. Corrige** (tres errores) el programa que debe mostrar «Puede votar» si `edad >= 18` y «No puede votar» en otro caso:

```cpp blank title="p2.cpp"
int edad;
cin >> edad;
if (edad => 18);
    cout << "Puede votar\n";
else
    cout << "No puede votar\n"
```

**P3. Reescribe sin anidar** usando una sola condición compuesta: `if (a > 0) { if (b > 0) { cout << "ambos positivos"; } }`

**P4. Escribe un programa** que lea el consumo mensual de agua (m³) y calcule el pago: hasta 10 m³ a $8 cada uno; de 11 a 30 m³, los primeros 10 a $8 y el resto a $12; más de 30, los primeros 30 como antes y el resto a $18. Valida consumos negativos.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Escribo condiciones simples y compuestas correctamente (incluyendo rangos).</li>
<li>Elijo entre <code>if</code>, <code>if-else</code>, escalera o anidamiento según el problema.</li>
<li>Dibujo el diagrama de flujo de una decisión.</li>
<li>Diseño casos de prueba que recorren todos los caminos y los valores frontera.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 `=` asigna un valor; `==` compara · 2 Uno · 3 `x >= 1 && x <= 100` · 4 `false`, `true`, `false` · 5 Falso: solo controla la siguiente sentencia · 6 `&&` y `||` dejan de evaluar en cuanto el resultado está decidido (p. ej., si el lado izquierdo de `&&` es falso) · 7 El rombo · 8 `10` · 9 Un valor justo en el límite de un rango (p. ej., 6 para aprobar); ahí se esconden los errores de `>` contra `>=` · 10 `Si condicion Entonces … SiNo … FinSi`
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.**

```cpp run title="p1.cpp" runs="15|8"
#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    if (n % 3 == 0 && n % 5 == 0)
        cout << "FizzBuzz\n";
    else if (n % 3 == 0)
        cout << "Fizz\n";
    else if (n % 5 == 0)
        cout << "Buzz\n";
    else
        cout << n << "\n";
    return 0;
}
```

**P2.** `=>` debe ser `>=`; sobra el `;` después del `if` (además deja al `else` sin `if`); falta `;` al final de la última línea.

**P3.** `if (a > 0 && b > 0) { cout << "ambos positivos"; }`

**P4.**

```cpp run title="agua.cpp" runs="7|25|42|-3"
#include <iostream>
using namespace std;
int main()
{
    double m3;
    cout << "Consumo (m3): ";
    cin >> m3;
    double pago;
    if (m3 < 0)
    {
        cout << "Consumo invalido\n";
        return 0;
    }
    else if (m3 <= 10)
        pago = m3 * 8;
    else if (m3 <= 30)
        pago = 10 * 8 + (m3 - 10) * 12;
    else
        pago = 10 * 8 + 20 * 12 + (m3 - 30) * 18;
    cout << "Pago: $" << pago << "\n";
    return 0;
}
```
:::
