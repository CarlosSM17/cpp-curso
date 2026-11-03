---
num: "10"
archivo: "Tema10_Funciones_parametros_ambito"
titulo: "Funciones: procedimientos, parámetros y ámbito"
corto: "Funciones"
lema: "Divide y vencerás: piezas pequeñas, con nombre, que reciben datos, hacen una tarea y devuelven un resultado."
duracion: "6 h · 3 sesiones de 2 h"
previos: "Temas 03 a 08 (expresiones, decisiones, ciclos y arreglos)."
fuentes:
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Cap. 8: Funciones de usuario (§8.1 Variables globales y locales, §8.2 Procedimiento, §8.3 Función de usuario, paso por valor y por referencia, §8.4 Ejercicios). Cap. 1, §1.4.2 (error de enlace por función sin definir)."
  - "Lospinoso, J. (2019). *C++ Crash Course*. Overture: Function Overloading, References. Cap. 1: Functions. Cap. 3: References. Cap. 4: Automatic and Static Storage Duration. Cap. 9: Function Declarations, Overload Resolution."
objetivos:
  A:
    - "Explicar para qué sirven las funciones: descomponer un problema y reutilizar código."
    - "Declarar (prototipo), definir y llamar funciones con parámetros y valor de retorno."
    - "Distinguir procedimientos (`void`) de funciones que devuelven un valor."
    - "Distinguir variables locales y globales y su ámbito."
    - "Pasar parámetros por valor y por referencia (`&`) y predecir el efecto de cada uno."
  B:
    - "Usar sobrecarga de funciones y argumentos por defecto."
    - "Pasar arreglos a funciones y usar referencias constantes (`const &`)."
    - "Explicar la pila de llamadas y la duración de variables `static` locales."
    - "Diseñar programas modulares cuyas funciones se prueban por separado."
efectos:
  soporte:
    - ["Elementos aislados", "Necesidad → definir/llamar → parámetros → return → prototipos → ámbito → valor vs referencia → pila de llamadas."]
    - ["Atención dividida", "Diagramas de flujo de llamada y de memoria (copia vs alias) integrados con el código."]
    - ["Ejemplo resuelto", "Reloj: segundos → hh:mm:ss con funciones de lectura, conversión (por referencia) y salida."]
    - ["Movimiento humano", "«Llamada telefónica»: un estudiante delega una tarea a otro y espera el resultado."]
  procedimental:
    - ["Variabilidad", "Plantillas de funciones para distintos tipos de tarea (calcular, validar, mostrar, modificar)."]
    - ["Autoexplicación", "Preguntas «¿cambia o no cambia la variable original?»."]
  tareas:
    - ["Ejemplo resuelto", "T1: promedio y letra + gemelo (precio con descuento)."]
    - ["Problema por completar", "T2 (`esPrimo`, con pistas) y T3 (intercambiar y ordenar tres, sin pistas)."]
    - ["Desvanecimiento de guía", "T1 → T4."]
    - ["Solución libre", "T5: todas las funciones posibles sobre un entero."]
    - ["Autoexplicación", "T6: explicar salidas de valor vs referencia y variables globales."]
    - ["Imaginación", "T7: imaginar la pila de llamadas."]
    - ["Memoria colectiva de trabajo", "T8: juego de dados modular con contratos (prototipos) acordados."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Definir, llamar, parámetros, `return`, `void`, local/global, valor/referencia."
    B: "Sobrecarga, valores por defecto, arreglos como parámetro, `const &`, `static`."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4; cada función se prueba sola antes de integrarla."
    B: "T5, T6, T7 autónomas; arquitectos de los prototipos en T8."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Convertidor de unidades refactorizado en funciones (T4)."
    B: "Biblioteca personal de funciones sobre enteros (T5) con pruebas."
  Entorno:
    comp: "Información procedimental"
    A: "Depurador: «entrar» (*step into*) y «salir» (*step out*) de funciones."
    B: "Terminal; pruebas unitarias simples con `assert` (adelanto del cap. 10 del *Crash Course*)."
plan:
  - ["Sesión 1", "Soporte", "Llamada telefónica; conceptos 1–5; ejemplo resuelto; T1, T2.", "120 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–9; T3, T4; Ruta B: T6, T7.", "120 min"]
  - ["Sesión 3", "Tareas + evaluación", "T5, T8 colaborativa; protocolo verbal; tests y autorregistro.", "120 min"]
glosario:
  - ["función", "function", "Bloque de código con nombre que realiza una tarea y puede devolver un valor."]
  - ["procedimiento", "procedure / void function", "Función que no devuelve valor (`void`)."]
  - ["prototipo / declaración", "declaration / prototype", "Firma de la función terminada en `;`: tipo, nombre y parámetros."]
  - ["definición", "definition", "La función completa, con su cuerpo entre llaves."]
  - ["llamada", "call / invocation", "Uso de la función: `area(2.5)`."]
  - ["parámetro", "parameter", "Variable declarada en la definición que recibe un dato."]
  - ["argumento", "argument", "Valor concreto que se envía en la llamada."]
  - ["valor de retorno", "return value", "Resultado que la función devuelve con `return`."]
  - ["paso por valor", "pass by value", "El parámetro recibe una **copia**; el original no cambia."]
  - ["paso por referencia", "pass by reference", "El parámetro es un **alias** del original (`int&`); los cambios se reflejan."]
  - ["ámbito", "scope", "Región del código donde un nombre es visible."]
  - ["variable local / global", "local / global variable", "Declarada dentro de una función / fuera de todas."]
  - ["pila de llamadas", "call stack", "Estructura donde se apilan las llamadas activas con sus variables."]
  - ["sobrecarga", "overloading", "Varias funciones con el mismo nombre y distintos parámetros."]
  - ["argumento por defecto", "default argument", "Valor que toma un parámetro si no se envía."]
---

# 1. Información de soporte {.soporte}

:::analogia | La cocina de un restaurante
El chef principal no hace todo: le pide al encargado de salsas «prepárame 2 litros de salsa verde» y espera. El encargado recibe **datos** (2 litros, verde), hace su **tarea** con su propio equipo y **devuelve** el resultado. Otro cocinero solo emplata (no devuelve nada: **procedimiento**). Un programa con funciones funciona igual: `main` es el chef y **delega** tareas a funciones especializadas.
:::

:::pregunta
En el Tema 07 escribiste varias veces el mismo ciclo para dibujar renglones de asteriscos. **¿Qué pasaría si quisieras cambiar el símbolo en todos lados? ¿Cómo podrías escribir ese ciclo una sola vez y usarlo cuando quieras?**

{{lineas:2}}
:::

:::relevancia
Ningún programa profesional es un `main` gigante: los motores de videojuegos tienen funciones como `dibujarSprite()`, `detectarColision()`, `actualizarPuntaje()`. Las funciones permiten **dividir** el trabajo en equipo, **probar** cada pieza por separado y **reutilizar** código. Son la base de las bibliotecas que ya usas (`sqrt`, `pow`, `getline`). {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | Definir y llamar una función | Elementos aislados, Atención dividida
<div class="cols">
<div>

```cpp run title="saludo.cpp"
#include <iostream>
using namespace std;

void saludar()                     //> **Definición**: tipo de retorno, nombre, ( )
{
    cout << "Hola desde la funcion\n";
}

int main()
{
    cout << "Inicio de main\n";
    saludar();                     //> **Llamada**: salta a la función…
    cout << "De vuelta en main\n"; //> …y al terminar regresa aquí
    saludar();                     //> Se puede llamar las veces que quieras
    return 0;
}
```

</div>
<div>

```dot
rankdir=TB; nodesep=0.3; ranksep=0.2;
@proc(a, "main: Inicio")
@sub(b, "saludar()")
@proc(c, "main: De vuelta")
@sub(d, "saludar()")
@term(e, "fin")
a -> b [label=" llama"]; b -> c [label=" regresa"]; c -> d [label=" llama"]; d -> e [label=" regresa"];
```

</div>
</div>

`void` significa «no devuelve ningún valor»: es un **procedimiento**.
:::

:::concepto | 2 | Parámetros: datos que recibe la función | Elementos aislados, Atención dividida
```cpp run title="linea.cpp"
#include <iostream>
using namespace std;

void linea(int n, char c)          //> Dos **parámetros**: cuántos y qué símbolo
{
    for (int i = 0; i < n; i++)
        cout << c;
    cout << "\n";
}

int main()
{
    linea(10, '*');                //> **Argumentos**: 10 y '*' se copian en n y c
    linea(4, '#');
    int ancho = 7;
    linea(ancho, '=');             //> Un argumento puede ser una variable o expresión
    return 0;
}
```
Los argumentos se asignan a los parámetros **en orden**: el primero al primero, el segundo al segundo. Deben coincidir en número y tipo.
:::

:::concepto | 3 | `return`: devolver un resultado | Elementos aislados, Atención dividida
```cpp run title="area.cpp"
#include <iostream>
using namespace std;

double areaCirculo(double r)       //> `double`: el tipo de lo que devuelve
{
    const double PI = 3.14159265358979;
    return PI * r * r;             //> `return` entrega el valor y TERMINA la función
}

int main()
{
    double a = areaCirculo(2.0);                       //> El valor devuelto se guarda…
    cout << "Area: " << a << "\n";
    cout << "Dos circulos: " << areaCirculo(1) + areaCirculo(3) << "\n";  //> …o se usa en una expresión
    return 0;
}
```
Una función que no es `void` **debe** devolver un valor en todos sus caminos. Puede tener varios `return` (por ejemplo, uno en cada rama de un `if`).
:::

:::movimiento | La llamada telefónica (10 min)
Un estudiante es `main` y tiene una tarjeta con un problema: «¿cuál es el área de un círculo de radio 3?». Llama (de verdad, con un gesto de teléfono) a «areaCirculo», le **dicta** el radio (argumento) y **espera** sin hacer nada más. «areaCirculo» lo anota en su propia hoja (su parámetro: una **copia**), calcula y **responde** el número. `main` lo anota y continúa. Segunda ronda: «areaCirculo» tacha el radio en **su** hoja y escribe otro; ¿cambió la tarjeta de `main`? (No: paso por valor.)
:::

:::concepto | 4 | Prototipos: declarar antes, definir después | Elementos aislados
El compilador lee de arriba hacia abajo: una función debe estar **declarada** antes de llamarse. El estilo de Betancourt y Polanco es poner los **prototipos** antes de `main` y las definiciones al final:

```cpp run title="prototipos.cpp"
#include <iostream>
using namespace std;

int cuadrado(int x);               //> Prototipo: la «promesa» (termina en ;)
void mostrar(int valor);

int main()
{
    mostrar(cuadrado(7));          //> Ya se puede llamar: el compilador conoce las firmas
    return 0;
}

int cuadrado(int x)                //> Definición: cumple la promesa
{
    return x * x;
}

void mostrar(int valor)
{
    cout << "Resultado: " << valor << "\n";
}
```
Si declaras un prototipo y olvidas la definición, el error aparece en el **enlace** (*undefined reference*), como viste en el Tema 01.
:::

:::concepto | 5 | Ámbito: variables locales y globales | Elementos aislados, Atención dividida
```cpp run title="ambito.cpp"
#include <iostream>
using namespace std;

int contadorGlobal = 0;            //> **Global**: visible en todo el archivo (úsala con mucho cuidado)

void incrementar()
{
    int local = 0;                 //> **Local**: nace al entrar y muere al salir de la función
    local++;
    contadorGlobal++;
    cout << "local = " << local << ", global = " << contadorGlobal << "\n";
}

int main()
{
    incrementar();
    incrementar();                 //> `local` vuelve a empezar en 0; la global conserva su valor
    // cout << local;              //> ERROR: `local` no existe en main
    return 0;
}
```
**Buenas prácticas:** comunica los datos con **parámetros y `return`**, no con variables globales; así cada función se entiende y se prueba sola. Dos funciones pueden tener variables locales con el mismo nombre sin conflicto.
:::

:::concepto | 6 | Paso por valor y paso por referencia | Elementos aislados, Atención dividida
<div class="cols eq">
<div>

```cpp run title="por_valor.cpp"
#include <iostream>
using namespace std;
void duplicar(int x)      // copia
{
    x = x * 2;
}
int main()
{
    int n = 5;
    duplicar(n);
    cout << "n = " << n << "\n";
    return 0;
}
```

```diagram mem
regions:
  - name: "main"
    vars:
      - {name: n, type: int, val: 5}
  - name: "duplicar"
    color: "#fefce8"
    vars:
      - {name: x, type: int, val: "5 → 10", hl: true, note: "copia"}
```

</div>
<div>

```cpp run title="por_referencia.cpp"
#include <iostream>
using namespace std;
void duplicar(int& x)     // alias
{
    x = x * 2;
}
int main()
{
    int n = 5;
    duplicar(n);
    cout << "n = " << n << "\n";
    return 0;
}
```

```diagram mem
regions:
  - name: "main"
    vars:
      - {name: n, type: int, val: "5 → 10", hl: true}
  - name: "duplicar"
    color: "#fdf4ff"
    vars:
      - {name: x, type: "int&", val: "alias de n", kind: ref, to: n}
```

</div>
</div>

- **Por valor** (`int x`): la función trabaja con una **copia**; el original no cambia.
- **Por referencia** (`int& x`): el parámetro es **otro nombre** para la misma variable; los cambios se ven en el original. Úsalo cuando la función deba **modificar** datos o **devolver varios** resultados.
:::

:::concepto | 7 | La pila de llamadas | Elementos aislados, Atención dividida
Cada llamada crea un **marco** (*frame*) con sus parámetros y variables locales, que se apila sobre el de quien llamó; al hacer `return`, el marco se destruye.

```cpp run title="pila.cpp"
#include <iostream>
using namespace std;
int doble(int a) { return a * 2; }
int sumaDobles(int x, int y)
{
    int r = doble(x) + doble(y);   //> Mientras corre doble(x), sumaDobles está en pausa
    return r;
}
int main()
{
    int total = sumaDobles(3, 4);
    cout << total << "\n";
    return 0;
}
```

```diagram stack
title: "Pila en el momento en que se ejecuta doble(3)"
frames:
  - {name: "main()", vars: [[total, "?"]]}
  - {name: "sumaDobles(3, 4)", vars: [[x, 3], [y, 4], [r, "?"]], note: "en pausa"}
  - {name: "doble(3)", vars: [[a, 3]], hl: true, note: "en ejecución"}
```
:::

:::concepto | 8 | Ruta B · Sobrecarga, valores por defecto, arreglos y `const &` | Elementos aislados, Reversión de la experiencia
```cpp run title="avanzado.cpp"
#include <iostream>
#include <string>
using namespace std;

int mayor(int a, int b) { return a > b ? a : b; }                  //> Sobrecarga: mismo nombre…
double mayor(double a, double b) { return a > b ? a : b; }         //> …distintos tipos de parámetros
void repetir(const string& txt, int veces = 2)                     //> `const &`: sin copia y sin poder modificar; `veces` tiene valor por defecto
{
    for (int i = 0; i < veces; i++) cout << txt;
    cout << "\n";
}
double promedio(const int datos[], int n)                          //> Un arreglo se pasa junto con su tamaño
{
    int s = 0;
    for (int i = 0; i < n; i++) s += datos[i];
    return static_cast<double>(s) / n;
}
int siguienteTurno()
{
    static int turno = 0;                                          //> `static`: conserva su valor entre llamadas
    return ++turno;
}
int main()
{
    cout << mayor(3, 9) << " " << mayor(2.5, 1.5) << "\n";
    repetir("ab");
    repetir("xyz", 3);
    int v[] = {4, 8, 6};
    cout << promedio(v, 3) << "\n";
    cout << siguienteTurno() << siguienteTurno() << siguienteTurno() << "\n";
    return 0;
}
```
Los arreglos **no se copian** al pasarlos: la función recibe la dirección del primero, así que puede **modificar** el original (por eso se marcan `const` cuando solo se leen).
:::

## 1.2 Ejemplo resuelto: el reloj modular

:::ejemplo | De segundos a hh:mm:ss con tres funciones | Ejemplo resuelto, Atención dividida
**Problema.** Un cronómetro guarda el tiempo en segundos. Leer un número de segundos (no negativo, validado), convertirlo a horas, minutos y segundos, y mostrarlo como `hh:mm:ss`.

**A. Algoritmo (descomposición en funciones)**

1. `leerNoNegativo()`: pedir un entero hasta que sea ≥ 0 y **devolverlo**.
2. `convertir(total, h, m, s)`: calcular las tres partes y **devolverlas por referencia** (son tres resultados).
3. `mostrar(h, m, s)`: imprimir con dos dígitos cada parte (procedimiento `void`).
4. `main`: llamar a las tres en orden.

**B. Pseudocódigo (PSeInt)**

```pseudo
SubProceso convertir(total, h Por Referencia, m Por Referencia, s Por Referencia)
    h <- trunc(total / 3600)
    m <- trunc((total MOD 3600) / 60)
    s <- total MOD 60
FinSubProceso

Algoritmo Reloj
    Repetir
        Leer total
    Hasta Que total >= 0
    convertir(total, h, m, s)
    Escribir h, ":", m, ":", s
FinAlgoritmo
```

**C. Código en C++**

```cpp run title="reloj.cpp" stdin="-20\n4000\n"
#include <iostream>
#include <iomanip>
using namespace std;

int leerNoNegativo();                                   //> Prototipos: el «índice» del programa
void convertir(int total, int& h, int& m, int& s);
void mostrar(int h, int m, int s);

int main()
{
    int total = leerNoNegativo();                       //> 1) devuelve un valor
    int h, m, s;
    convertir(total, h, m, s);                          //> 2) llena h, m y s por referencia
    mostrar(h, m, s);                                   //> 3) solo muestra
    return 0;
}

int leerNoNegativo()
{
    int x;
    do {
        cout << "Segundos: ";
        cin >> x;
    } while (x < 0);
    return x;                                           //> Entrega el dato ya validado
}

void convertir(int total, int& h, int& m, int& s)      //> `total` por valor (solo se lee); h, m, s por referencia (se escriben)
{
    h = total / 3600;
    m = (total % 3600) / 60;
    s = total % 60;
}

void mostrar(int h, int m, int s)
{
    cout << setfill('0') << setw(2) << h << ":" << setw(2) << m << ":" << setw(2) << s << "\n";
}
```

**D. Verificación.** 4000 s = 1 h (3600 s) + 400 s = 1 h + 6 min (360 s) + 40 s → `01:06:40` ✔. Cada función puede probarse sola: por ejemplo, `convertir(59, h, m, s)` debe dar `0, 0, 59`.
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.16; ranksep=0.3;
@term(f, "Función")
@proc(p, "prototipo\ntipo nombre(params);")
@proc(d, "definición\n{ cuerpo }")
@proc(l, "llamada\nnombre(args)")
@proc(r, "return valor\n(o void)")
@proc(v, "por valor: copia")
@proc(rf, "por referencia (&):\nalias, modifica")
@sub(a, "ámbito: local / global\npila de llamadas")
@hl(b, "Ruta B: sobrecarga · defecto\narreglos · const& · static")
f -> p; f -> d; f -> l; d -> r; l -> v; l -> rf; f -> a; f -> b [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1 · Cuatro tipos de funciones | Variabilidad
| La función… | Firma típica | Llamada |
|---|---|---|
| calcula y devuelve | `double area(double b, double h)` | `double a = area(3, 4);` |
| valida (sí/no) | `bool esPar(int n)` | `if (esPar(x)) …` |
| solo muestra | `void mostrarMenu()` | `mostrarMenu();` |
| modifica o devuelve varios | `void intercambiar(int& a, int& b)` | `intercambiar(x, y);` |
| lee y devuelve un dato válido | `int leerEntre(int min, int max)` | `int op = leerEntre(1, 4);` |
| procesa un arreglo | `int suma(const int a[], int n)` | `suma(v, N)` |

**Orden en el archivo:** `#include` → constantes → **prototipos** → `main` → **definiciones**.

**Diseño:** una función = **una** tarea; nombre con verbo (`calcular…`, `mostrar…`, `es…`); de 5 a 25 líneas; sin `cin`/`cout` en las funciones de cálculo (así se pueden reutilizar).
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿Qué <b>recibe</b> la función (parámetros), qué <b>hace</b> y qué <b>devuelve</b>? Escríbelo antes de programarla.</li>
<li>¿El prototipo coincide exactamente con la definición (tipo, nombre, parámetros)?</li>
<li>¿La llamada envía los argumentos en el orden y tipo correctos?</li>
<li>Si la función no es <code>void</code>, ¿todos sus caminos terminan en <code>return</code>?</li>
<li>¿Uso el valor devuelto? (<code>area(3, 4);</code> sola no hace nada visible.)</li>
<li>¿La función necesita modificar el original? Entonces <code>&amp;</code>; si no, por valor (o <code>const &amp;</code> para objetos grandes).</li>
<li>¿Probé la función sola con casos conocidos antes de integrarla?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Llamar antes de declarar.**

```cpp err
#include <iostream>
int main()
{
    std::cout << triple(4);
    return 0;
}
int triple(int x) { return 3 * x; }
```
*Corrección:* agrega el prototipo `int triple(int x);` antes de `main`.

**b) Esperar que el paso por valor modifique el original.** ¿Por qué el saldo no cambia?

```cpp run
#include <iostream>
using namespace std;
void depositar(double saldo, double monto) { saldo += monto; }
int main()
{
    double saldo = 100;
    depositar(saldo, 50);
    cout << "Saldo: " << saldo << "\n";    //> Sigue en 100: se modificó una copia
    return 0;
}
```
*Corrección:* `void depositar(double& saldo, double monto)` o, mejor, `double depositar(double saldo, double monto) { return saldo + monto; }` con `saldo = depositar(saldo, 50);`.

**c) Función sin `return` en algún camino.** Compila con aviso (`-Wreturn-type`) y el resultado es indefinido:

```cpp blank title="sin_return.cpp"
int signo(int x)
{
    if (x > 0) return 1;
    if (x < 0) return -1;
}   // ¿y si x == 0?
```

**d) Número o tipo de argumentos incorrecto.**

```cpp err
#include <iostream>
double area(double b, double h) { return b * h / 2; }
int main()
{
    std::cout << area(3);
    return 0;
}
```

**e) Pasar un literal a un parámetro por referencia:** `intercambiar(3, 5);` no compila: una referencia `int&` necesita una **variable**.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Validación reutilizable | Variabilidad
La misma idea de `leerNoNegativo` generalizada con parámetros, y usada para leer datos distintos:

```cpp run title="leer_entre.cpp" stdin="15\n12\n0\n7\n"
#include <iostream>
using namespace std;

int leerEntre(int minimo, int maximo)          //> Una sola función sirve para cualquier rango
{
    int x;
    do {
        cout << "Valor (" << minimo << "-" << maximo << "): ";
        cin >> x;
    } while (x < minimo || x > maximo);
    return x;
}

int main()
{
    int mes = leerEntre(1, 12);               //> Rango de meses
    int dia = leerEntre(1, 31);               //> Rango de días
    cout << "Fecha: " << dia << "/" << mes << "\n";
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Antes de programar una función, escribe su «contrato»: qué recibe, qué hace y qué devuelve.

:::tarea A | T1. Promedio y letra: ejemplo y gemelo | 25 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia:**

```cpp run title="promedio_letra.cpp" stdin="8.5 9 7.5\n"
#include <iostream>
using namespace std;

double promedio(double a, double b, double c)   //> Recibe 3 notas, devuelve su promedio
{
    return (a + b + c) / 3;
}

char letra(double prom)                         //> Recibe un promedio, devuelve una letra
{
    if (prom >= 9) return 'A';                  //> Varios return: uno por camino
    if (prom >= 8) return 'B';
    if (prom >= 6) return 'C';
    return 'F';
}

int main()
{
    double n1, n2, n3;
    cin >> n1 >> n2 >> n3;
    double p = promedio(n1, n2, n3);            //> El resultado de una función…
    cout << "Promedio: " << p << "  Letra: " << letra(p) << "\n";   //> …se pasa a la otra
    return 0;
}
```

**Paso 2 · Gemelo.** Escribe `double precioFinal(double precio, double pctDescuento)` que devuelva el precio con descuento, y `bool esOferta(double pctDescuento)` que devuelva `true` si el descuento es de 30 % o más. En `main`, lee precio y descuento y muestra el precio final y si es oferta.

:::solucion | T1
```cpp run title="precio.cpp" runs="800 35|450 10"
#include <iostream>
using namespace std;

double precioFinal(double precio, double pct)
{
    return precio * (1 - pct / 100);
}

bool esOferta(double pct)
{
    return pct >= 30;
}

int main()
{
    double precio, pct;
    cin >> precio >> pct;
    cout << "Precio final: $" << precioFinal(precio, pct)
         << (esOferta(pct) ? "  (OFERTA!)" : "") << "\n";
    return 0;
}
```
:::
:::

:::tarea A | T2. La función `esPrimo` (completa con pistas) | 25 min | Problema por completar
**Contexto.** En el Tema 07 calculaste primos con ciclos anidados. Ahora encapsula la prueba en una función reutilizable y úsala para mostrar los primos entre dos números.

```cpp blank title="primos_funcion.cpp"
#include <iostream>
using namespace std;

__1__ esPrimo(int n);                     // 1: tipo de retorno (si/no)

int main()
{
    int a, b;
    cin >> a >> b;
    for (int x = a; x <= b; x++)
        if (__2__)                        // 2: llamada a la funcion con x
            cout << x << " ";
    cout << "\n";
    return 0;
}

bool esPrimo(int n)
{
    if (n < 2)
        return __3__;                     // 3: 0 y 1 no son primos
    for (int d = 2; d * d <= n; d++)
        if (n % d == 0)
            __4__;                        // 4: encontramos un divisor
    __5__;                                // 5: no hubo divisores
}
```

:::solucion | T2
{{c:1}} `bool` · {{c:2}} `esPrimo(x)` · {{c:3}} `false` · {{c:4}} `return false` · {{c:5}} `return true`

```cpp run title="primos_funcion.cpp" stdin="10 50\n"
#include <iostream>
using namespace std;

bool esPrimo(int n);

int main()
{
    int a, b;
    cin >> a >> b;
    for (int x = a; x <= b; x++)
        if (esPrimo(x))
            cout << x << " ";
    cout << "\n";
    return 0;
}

bool esPrimo(int n)
{
    if (n < 2)
        return false;
    for (int d = 2; d * d <= n; d++)
        if (n % d == 0)
            return false;
    return true;
}
```
Observa que `return false` dentro del ciclo hace el trabajo del `break` y de la bandera del Tema 07.
:::
:::

:::tarea AB | T3. Intercambiar y ordenar tres valores (completa sin pistas) | 25 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Un juego necesita ordenar los puntajes del podio. Escribe `intercambiar` y úsala dentro de `ordenarTres`, que deja `a ≤ b ≤ c`.

```cpp blank title="ordenar_tres.cpp"
#include <iostream>
using namespace std;

void intercambiar(__1__ x, __2__ y)
{
    int aux = x;
    __3__;
    __4__;
}

void ordenarTres(int& a, int& b, int& c)
{
    if (a > b) __5__;
    if (b > c) __6__;
    if (a > b) __7__;
}

int main()
{
    int p, q, r;
    cin >> p >> q >> r;
    ordenarTres(p, q, r);
    cout << p << " " << q << " " << r << "\n";
    return 0;
}
```

:::solucion | T3
{{c:1}} `int&` · {{c:2}} `int&` · {{c:3}} `x = y` · {{c:4}} `y = aux` · {{c:5}} `intercambiar(a, b)` · {{c:6}} `intercambiar(b, c)` · {{c:7}} `intercambiar(a, b)`

```cpp run title="ordenar_tres.cpp" runs="9 2 5|3 3 1|1 2 3"
#include <iostream>
using namespace std;

void intercambiar(int& x, int& y)
{
    int aux = x;
    x = y;
    y = aux;
}

void ordenarTres(int& a, int& b, int& c)
{
    if (a > b) intercambiar(a, b);
    if (b > c) intercambiar(b, c);
    if (a > b) intercambiar(a, b);
}

int main()
{
    int p, q, r;
    cin >> p >> q >> r;
    ordenarTres(p, q, r);
    cout << p << " " << q << " " << r << "\n";
    return 0;
}
```
Son tres pasos de una burbuja (Tema 08) sobre tres variables.
:::
:::

:::tarea AB | T4. Convertidor modular (problema convencional) | 35 min | Variabilidad
**Contexto.** Retoma el convertidor de unidades del Tema 05 (T4) y **refactorízalo**: una función por conversión (`kmAMillas`, `kgALibras`, `celsiusAFahrenheit`, `litrosAGalones`), una función `mostrarMenu()`, una función `leerOpcion()` que valide 1–5 y un ciclo que repita hasta elegir 5 (salir). Ninguna función de conversión debe usar `cin` ni `cout`.

:::solucion | T4
```cpp run title="convertidor_modular.cpp" stdin="1\n10\n3\n100\n9\n5\n"
#include <iostream>
using namespace std;

double kmAMillas(double km) { return km * 0.621371; }
double kgALibras(double kg) { return kg * 2.20462; }
double celsiusAFahrenheit(double c) { return 9.0 / 5 * c + 32; }
double litrosAGalones(double l) { return l * 0.264172; }

void mostrarMenu()
{
    cout << "1) km->mi 2) kg->lb 3) C->F 4) L->gal 5) Salir\n";
}

int leerOpcion()
{
    int op;
    do {
        cout << "Opcion: ";
        cin >> op;
    } while (op < 1 || op > 5);
    return op;
}

int main()
{
    int op;
    do {
        mostrarMenu();
        op = leerOpcion();
        if (op != 5)
        {
            double v;
            cout << "Valor: ";
            cin >> v;
            switch (op)
            {
                case 1: cout << kmAMillas(v) << " mi\n"; break;
                case 2: cout << kgALibras(v) << " lb\n"; break;
                case 3: cout << celsiusAFahrenheit(v) << " F\n"; break;
                case 4: cout << litrosAGalones(v) << " gal\n"; break;
            }
        }
    } while (op != 5);
    return 0;
}
```
:::
:::

:::tarea A | T5. Tu biblioteca de funciones para enteros (solución libre) | 30 min | Solución libre
**Contexto.** Escribe **todas las funciones que se te ocurran** que reciban un entero `n` y calculen o decidan algo sobre él: `esPar`, `cuadrado`, `sumaDigitos`, `cuantosDigitos`, `invertir`, `factorial`, `esPrimo`, `esPalindromo`, `esPerfecto`… Pruébalas todas desde `main` con varios valores. No hay un número mínimo: mientras más funciones correctas, mejor.

:::solucion | T5
Una biblioteca posible (las pruebas usan un solo `main`):

```cpp run title="biblioteca_enteros.cpp"
#include <iostream>
using namespace std;
bool esPar(int n) { return n % 2 == 0; }
int sumaDigitos(int n) { int s = 0; while (n > 0) { s += n % 10; n /= 10; } return s; }
int cuantosDigitos(int n) { int c = 1; while (n >= 10) { n /= 10; c++; } return c; }
int invertir(int n) { int r = 0; while (n > 0) { r = r * 10 + n % 10; n /= 10; } return r; }
bool esPalindromo(int n) { return n == invertir(n); }
long long factorial(int n) { long long f = 1; for (int i = 2; i <= n; i++) f *= i; return f; }
int main()
{
    int pruebas[] = {7, 121, 2026};
    for (int n : pruebas)
        cout << n << ": par=" << esPar(n) << " sumaDig=" << sumaDigitos(n)
             << " digitos=" << cuantosDigitos(n) << " invertido=" << invertir(n)
             << " palindromo=" << esPalindromo(n) << "\n";
    cout << "10! = " << factorial(10) << "\n";
    return 0;
}
```
Observa que `esPalindromo` **reutiliza** a `invertir`.
:::
:::

:::tarea B | T6. ¿Cambió o no cambió? (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
Explica **línea por línea** la salida del programa: ¿por qué `a` cambia y `b` no? ¿Qué `x` modifica cada función? ¿Por qué no hay conflicto entre las dos variables llamadas `x`?

```cpp run title="cambio.cpp"
#include <iostream>
using namespace std;
int x = 100;
void f(int a, int& b) { a = a + 1; b = b + 1; x = x + 1; }
void g() { int x = 5; x = x * 2; cout << "g: x = " << x << "\n"; }
int main()
{
    int a = 1, b = 1;
    f(a, b);
    g();
    cout << "a = " << a << ", b = " << b << ", x = " << x << "\n";
    return 0;
}
```

{{lineas:4}}

:::solucion | T6
En la llamada `f(a, b)`, el **primer** parámetro de `f` recibe una copia de `a` (por valor): incrementarla no afecta a la `a` de `main` → `a = 1`. El segundo es una referencia a la `b` de `main` → `b = 2`. Dentro de `f`, `x` es la **global** (no hay otra `x` local) → pasa de 100 a 101. En `g`, `int x = 5` es una variable **local** que **oculta** a la global: se duplica a 10 y desaparece al salir; la global sigue en 101.
:::
:::

:::tarea B | T7. Dibuja la pila (imaginación) | 25 min | Imaginación
**Sin ejecutar**, imagina la pila de llamadas: dibuja los marcos (con sus variables) en el momento en que se ejecuta la línea marcada y escribe la salida completa.

```cpp check title="pila_imagina.cpp"
#include <iostream>
using namespace std;
int cubo(int n)
{
    int r = n * n * n;     // <-- dibuja la pila aqui (la primera vez)
    return r;
}
int sumaCubos(int a, int b)
{
    return cubo(a) + cubo(b);
}
int main()
{
    int x = 2;
    int y = sumaCubos(x, x + 1);
    cout << y << " " << cubo(y % 10) << "\n";
    return 0;
}
```

{{lineas:3}}

:::solucion | T7
La primera vez que se ejecuta la línea marcada: `main (x = 2, y = ?)` → `sumaCubos (a = 2, b = 3)` → `cubo (n = 2, r = 8)` en la cima. `sumaCubos` devuelve 8 + 27 = 35; luego `cubo(35 % 10) = cubo(5) = 125`.

```cpp run title="pila_imagina.cpp"
#include <iostream>
using namespace std;
int cubo(int n)
{
    int r = n * n * n;
    return r;
}
int sumaCubos(int a, int b)
{
    return cubo(a) + cubo(b);
}
int main()
{
    int x = 2;
    int y = sumaCubos(x, x + 1);
    cout << y << " " << cubo(y % 10) << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T8. Juego de dados modular (reto colaborativo) | 45 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización: primero el contrato
Equipos de 4, niveles mezclados. **Antes de programar**, el equipo acuerda y escribe los **prototipos** (el contrato) en el pizarrón; después cada integrante programa y prueba **su** función por separado:
- **Integrante 1:** `int lanzarDado()` → número aleatorio 1–6.
- **Integrante 2:** `void dibujarDado(int valor)` → muestra el dado con asteriscos (3 × 3).
- **Integrante 3:** `int ganadorRonda(int j1, int j2)` → 1, 2 o 0 (empate).
- **Integrante 4:** `main` → juega 3 rondas, lleva el marcador y anuncia al ganador.

Al integrar, si algo falla, el contrato dice de quién es la pieza. Reflexionen: ¿qué ventaja tuvo acordar los prototipos primero?
:::

:::solucion | T8
```cpp run title="dados.cpp"
#include <iostream>
#include <cstdlib>
using namespace std;

int lanzarDado() { return rand() % 6 + 1; }

void dibujarDado(int v)
{
    // posiciones de los puntos en una cuadricula 3x3 (fila por fila)
    bool p[7][9] = {{}, {0,0,0,0,1,0,0,0,0}, {1,0,0,0,0,0,0,0,1}, {1,0,0,0,1,0,0,0,1},
                    {1,0,1,0,0,0,1,0,1}, {1,0,1,0,1,0,1,0,1}, {1,0,1,1,0,1,1,0,1}};
    for (int f = 0; f < 3; f++)
    {
        cout << "  ";
        for (int c = 0; c < 3; c++) cout << (p[v][f * 3 + c] ? '*' : '.');
        cout << "\n";
    }
}

int ganadorRonda(int j1, int j2)
{
    if (j1 > j2) return 1;
    if (j2 > j1) return 2;
    return 0;
}

int main()
{
    srand(7);
    int m1 = 0, m2 = 0;
    for (int r = 1; r <= 3; r++)
    {
        int a = lanzarDado(), b = lanzarDado();
        cout << "Ronda " << r << ": J1 saca " << a << ", J2 saca " << b << "\n";
        dibujarDado(a);
        int g = ganadorRonda(a, b);
        if (g == 1) m1++;
        else if (g == 2) m2++;
    }
    cout << "Marcador " << m1 << "-" << m2 << ": "
         << (m1 > m2 ? "gana J1" : (m2 > m1 ? "gana J2" : "empate")) << "\n";
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Un experto convierte un `main` largo en funciones | Modalidad, Ejemplo resuelto
*Guion segmentado (≈ 4 min), con el código «antes» y «después» lado a lado.*

**Problema:** «Un programa de 60 líneas lee las calificaciones de un grupo, valida cada una con el mismo `do-while`, calcula promedio, máximo y mínimo, y dibuja una barra de asteriscos por alumno. Funciona, pero nadie lo entiende».

**Segmento 1 — Buscar lo repetido y lo nombrable.** {{como}} Leo el código y marco con colores los bloques que hacen **una** cosa: «validar una nota», «calcular el promedio», «dibujar una barra». {{porque}} Si puedo describir un bloque con un verbo y un objeto, ese bloque es candidato a función.

**Segmento 2 — Decidir el contrato de cada pieza.** {{como}} Para «dibujar una barra» me pregunto: ¿qué necesita? la longitud y el símbolo; ¿devuelve algo? no → `void barra(int n, char c)`. Para «promedio»: necesita el arreglo y su tamaño, devuelve un `double` → `double promedio(const double a[], int n)`. {{porque}} Los parámetros salen de las variables que el bloque **lee**; el retorno, de la variable que **produce**.

**Segmento 3 — Mover, compilar, probar, una por una.** {{como}} Extraigo **una** función, compilo y ejecuto con los mismos datos de siempre; solo entonces extraigo la siguiente. {{porque}} Si muevo todo a la vez y algo falla, no sabré qué cambio lo rompió.

**Segmento 4 — Leer `main` como un índice.** {{como}} Al final, `main` queda en pocas líneas que se leen como el algoritmo: leer, calcular, mostrar. {{porque}} Ese es el objetivo: que el programa explique lo que hace sin necesidad de comentarios largos.

{{salto}}

```cpp run title="refactorizado.cpp" stdin="4\n8 11 6.5 9 10\n"
#include <iostream>
using namespace std;

double leerNota()
{
    double x;
    do { cin >> x; } while (x < 0 || x > 10);
    return x;
}
double promedio(const double a[], int n)
{
    double s = 0;
    for (int i = 0; i < n; i++) s += a[i];
    return s / n;
}
void barra(int n, char c)
{
    for (int i = 0; i < n; i++) cout << c;
    cout << "\n";
}
int main()
{
    const int MAX = 40;
    double notas[MAX];
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) notas[i] = leerNota();
    cout << "Promedio: " << promedio(notas, n) << "\n";
    for (int i = 0; i < n; i++) barra(static_cast<int>(notas[i]), '#');
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. ¿Qué diferencia hay entre un parámetro y un argumento?
2. ¿Qué significa `void` como tipo de retorno?
3. ¿Para qué sirve un prototipo y cómo termina?
4. ¿Qué hace `return` además de devolver un valor?
5. Verdadero o falso: una variable local de una función puede usarse en `main`.
6. ¿Qué símbolo indica paso por referencia?
7. ¿Cuándo conviene el paso por referencia?
8. ¿Qué es la pila de llamadas?
9. ¿Qué es la sobrecarga de funciones?
10. ¿Por qué se recomienda evitar las variables globales?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida:**

```cpp check title="p1.cpp"
#include <iostream>
using namespace std;
int f(int a, int& b)
{
    a = a * 2;
    b = b + a;
    return a + b;
}
int main()
{
    int x = 3, y = 4;
    int z = f(x, y);
    cout << x << " " << y << " " << z << "\n";
    return 0;
}
```

**P2. Corrige** (tres errores): `void mayor(int a, int b); int main() { int m = mayor(3, 8); cout << m; } int mayor(int a, int b) { if (a > b) return a; }`

**P3. Escribe** la firma (prototipo) adecuada para: a) calcular la hipotenusa de un triángulo; b) decidir si un año es bisiesto; c) llenar un arreglo con ceros; d) devolver el mínimo y el máximo de un arreglo.

**P4. Escribe un programa** con una función `double potencia(double base, int exp)` (sin usar `pow`, admitiendo exponentes negativos) y una función `void tablaPotencias(double base, int n)` que muestre `base^0` hasta `base^n`.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Defino, declaro y llamo funciones con parámetros y <code>return</code>.</li>
<li>Elijo entre <code>void</code> y una función que devuelve valor.</li>
<li>Predigo si una variable cambia según el paso por valor o por referencia.</li>
<li>Divido un problema en funciones pequeñas y las pruebo por separado.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 El parámetro es la variable de la definición; el argumento es el valor que se envía en la llamada · 2 Que la función no devuelve ningún valor · 3 Declara la función (tipo, nombre, parámetros) para poder llamarla antes de su definición; termina en `;` · 4 Termina la ejecución de la función · 5 Falso · 6 `&` · 7 Cuando la función debe modificar el original, devolver varios resultados o evitar copiar objetos grandes · 8 La estructura donde se apilan los marcos de las funciones activas (parámetros y variables locales) · 9 Varias funciones con el mismo nombre y distintos parámetros · 10 Cualquier función puede modificarlas, lo que vuelve difícil seguir y probar el programa.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** `a` (copia de `x`) vale 6; `b` es `y`: 4 + 6 = 10; devuelve 16. `x` no cambia.

```cpp run title="p1.cpp"
#include <iostream>
using namespace std;
int f(int a, int& b)
{
    a = a * 2;
    b = b + a;
    return a + b;
}
int main()
{
    int x = 3, y = 4;
    int z = f(x, y);
    cout << x << " " << y << " " << z << "\n";
    return 0;
}
```

**P2.** El prototipo dice `void` pero se usa (y define) como `int`; falta `return b;` cuando `a <= b`; falta `#include <iostream>` / `using namespace std;`.

**P3.** a) `double hipotenusa(double a, double b);` b) `bool esBisiesto(int anio);` c) `void llenarCeros(int a[], int n);` d) `void minMax(const int a[], int n, int& mn, int& mx);`

**P4.**

```cpp run title="potencias.cpp"
#include <iostream>
using namespace std;
double potencia(double base, int exp)
{
    double r = 1;
    int e = exp < 0 ? -exp : exp;
    for (int i = 0; i < e; i++) r *= base;
    return exp < 0 ? 1 / r : r;
}
void tablaPotencias(double base, int n)
{
    for (int i = 0; i <= n; i++)
        cout << base << "^" << i << " = " << potencia(base, i) << "\n";
}
int main()
{
    tablaPotencias(2, 5);
    cout << "2^-3 = " << potencia(2, -3) << "\n";
    return 0;
}
```
:::
