---
num: "05"
archivo: "Tema05_Estructura_selectiva_switch"
titulo: "Estructura selectiva switch y menús de opciones"
corto: "switch y menús"
lema: "Cuando la pregunta tiene respuestas exactas y conocidas, switch abre directamente la puerta correcta."
duracion: "3 h · 2 sesiones de 1.5 h"
previos: "Tema 04 (if, if-else, escaleras y condiciones)."
fuentes:
  - "Kernighan, B. W. y Ritchie, D. M. (1988). *The C Programming Language* (2.ª ed.). Prentice Hall. Cap. 2: §2.3 Constants (constantes de enumeración). Cap. 3: §3.4 Switch."
  - "King, K. N. (2008). *C Programming: A Modern Approach* (2.ª ed.). W. W. Norton. Cap. 5: §5.3 The switch Statement. Cap. 16: §16.5 Enumerations."
  - "Seacord, R. C. (2020). *Effective C*. No Starch Press. Cap. 2 (tipos enumerados). Cap. 5 «Control Flow»: switch."
objetivos:
  A:
    - "Explicar cuándo conviene `switch` en lugar de una escalera `if-else` (valores discretos y conocidos)."
    - "Escribir `switch` con `case`, `break` y `default` sobre enteros y caracteres."
    - "Construir menús de opciones y agrupar varios `case` para una misma acción."
    - "Representar un `switch` con un diagrama de flujo de selección múltiple y con `Segun` en PSeInt."
  B:
    - "Usar `switch` con `enum` y explicar su ventaja frente a los «números mágicos»."
    - "Explicar la caída (*fall-through*): cuándo es un error y cuándo es intencional (comentario `/* fall through */` que reconoce `-Wextra`)."
    - "Transformar rangos en casos discretos (p. ej., `nota / 10`) y reconocer los límites de `switch`."
    - "Declarar variables dentro de un `case` usando un bloque `{ }`."
efectos:
  soporte:
    - ["Elementos aislados", "Motivación → anatomía → break → default → agrupar casos → char → límites → enum."]
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
    - ["Imaginación", "T7: predecir una caída intencional y reescribirla con `enum`."]
    - ["Memoria colectiva de trabajo", "T8: cajero automático por equipos."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Anatomía de `switch`, `break`, `default`, casos agrupados, menús con números y letras."
    B: "`enum`, caída intencional marcada, bloques en `case`, transformación de rangos."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 con diagrama de flujo; pares mixtos."
    B: "T5 (versiones), T6, T7 autónomas; mentores en T8."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Convertidor de unidades con menú (T4)."
    B: "Versión con `enum` de un menú (T7) y explicación de la caída."
  Entorno:
    comp: "Información procedimental"
    A: "Plantilla de menú impresa; prueba de cada opción y de una opción inválida."
    B: "Compilación con `-Wall -Wextra` (avisa la caída implícita con `-Wimplicit-fallthrough` y los valores de `enum` sin `case` con `-Wswitch`)."
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
  - ["enumeración", "enumeration (`enum`)", "Tipo con un conjunto fijo de constantes enteras con nombre."]
  - ["número mágico", "magic number", "Literal sin nombre cuyo significado no es evidente (`if (op == 3)`)."]
  - ["menú", "menu", "Lista de opciones que el usuario elige por número o letra."]
  - ["expresión de control", "controlling expression", "Valor entero o carácter que evalúa el `switch`."]
  - ["expresión constante", "constant expression", "Valor que el compilador conoce al compilar: literales, `#define` y constantes de `enum`."]
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
Menús de cajeros, máquinas expendedoras, opciones de un videojuego, comandos de un robot («A» avanza, «I» gira a la izquierda), estados de un semáforo: cuando las respuestas son **valores exactos y conocidos**, `switch` produce código más claro y fácil de ampliar que una larga escalera de `if`. En los sistemas embebidos escritos en C, casi todas las «máquinas de estados» se programan con `switch`. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | ¿Por qué `switch`? Compara dos versiones | Elementos aislados, Atención dividida
<div class="cols eq">
<div>

```c check title="con escalera if"
#include <stdio.h>
int main(void)
{
    int op = 2;
    if (op == 1)
        printf("Saldo\n");
    else if (op == 2)
        printf("Deposito\n");
    else if (op == 3)
        printf("Retiro\n");
    else
        printf("Invalida\n");
    return 0;
}
```

</div>
<div>

```c check title="con switch"
#include <stdio.h>
int main(void)
{
    int op = 2;
    switch (op)
    {
        case 1: printf("Saldo\n");    break;
        case 2: printf("Deposito\n"); break;
        case 3: printf("Retiro\n");   break;
        default: printf("Invalida\n");
    }
    return 0;
}
```

</div>
</div>

Ambas hacen lo mismo. Con `switch`, la variable `op` se escribe **una sola vez** y cada opción queda alineada como en el menú real.
:::

:::concepto | 2 | Anatomía de `switch` | Elementos aislados, Atención dividida
```c run title="semaforo.c" runs="V|A|R|X"
#include <stdio.h>
int main(void)
{
    char luz;
    printf("Luz del semaforo (V/A/R): ");
    scanf(" %c", &luz);
    switch (luz)                       //> Expresión de control: entero o carácter
    {                                  //> Las llaves agrupan todos los casos
        case 'V':                      //> `case` + valor CONSTANTE + dos puntos
            printf("Avanza\n");
            break;                     //> `break` sale del switch
        case 'A':
            printf("Precaucion\n");
            break;
        case 'R':
            printf("Alto\n");
            break;
        default:                       //> Si ningún case coincide
            printf("Luz desconocida\n");
    }
    printf("Fin\n");                   //> Después de `break` se continúa aquí
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

```c run stdin="2\n"
#include <stdio.h>
int main(void)
{
    int op;
    scanf("%d", &op);
    switch (op)
    {
        case 1: printf("Uno\n");     //> Sin break
        case 2: printf("Dos\n");     //> Entra aquí con op = 2...
        case 3: printf("Tres\n");    //> ...y sigue cayendo
        default: printf("Otro\n");   //> ...hasta el final
    }
    return 0;
}
```
**Regla:** termina cada `case` con `break`, salvo que quieras la caída a propósito (concepto 5 y Ruta B). Con `-Wextra`, gcc avisa en cada caída: *this statement may fall through*.
:::

:::movimiento | El switch humano (10 min)
Cuatro estudiantes se paran en fila como «puertas»: `case 1`, `case 2`, `case 3`, `default`. Algunos llevan un letrero de **break**. Otro estudiante, el «valor», recibe una tarjeta (por ejemplo, 2), entra por la puerta con su número y cumple la acción de esa puerta (aplaudir, saltar…). Si la puerta **no** tiene letrero de *break*, debe seguir a la siguiente puerta y hacer también su acción. El grupo predice antes qué hará el «valor».
:::

:::concepto | 4 | `default`: la opción para todo lo demás | Elementos aislados
`default` se ejecuta si **ningún** `case` coincide. Es opcional, pero en menús es tu oportunidad de avisar «opción inválida». Normalmente va al final (y entonces no necesita `break`).
:::

:::concepto | 5 | Varios casos, una misma acción | Elementos aislados, Atención dividida
Escribir varias etiquetas seguidas es una caída **intencional** muy útil (gcc no avisa cuando las etiquetas están juntas, sin sentencias entre ellas):

```c run runs="e|K|U"
#include <stdio.h>
int main(void)
{
    char c;
    printf("Letra: ");
    scanf(" %c", &c);
    switch (c)
    {
        case 'a': case 'e': case 'i': case 'o': case 'u':   //> Cinco etiquetas, un solo camino
        case 'A': case 'E': case 'I': case 'O': case 'U':   //> Mayúsculas también
            printf("Vocal\n");
            break;
        default:
            printf("No es vocal\n");
    }
    return 0;
}
```
:::

:::concepto | 6 | Lo que `switch` no puede hacer | Elementos aislados
- La expresión debe ser **entera** (`int`, `char`, `enum`): **no** `double` ni cadenas de texto.
- Cada `case` lleva un valor **constante** (un literal, una constante de `#define` o de `enum`) y **único**: no variables, no rangos (`case nota >= 9:` no existe).
- Para rangos usa `if-else`… o **transforma** el rango en un número: con calificaciones de 0 a 100, `nota / 10` produce 0…10 (ver T5).

```c err
#include <stdio.h>
int main(void)
{
    char cmd[10] = "start";
    switch (cmd)
    {
        case "start": printf("Inicio\n"); break;
    }
    return 0;
}
```
:::

:::concepto | 7 | Ruta B · `switch` con `enum` | Elementos aislados, Reversión de la experiencia
Una **enumeración** es un tipo con un conjunto fijo de **constantes enteras con nombre**: elimina los números mágicos y combina perfecto con `switch`.

```c run
#include <stdio.h>
enum raza { DINOSAURIO, MAMUT, HUMANO };       //> Tres constantes con nombre: valen 0, 1 y 2

int main(void)
{
    enum raza r = MAMUT;                       //> Variable del tipo `enum raza`
    switch (r)
    {
        case DINOSAURIO: printf("Extinto hace 66 millones de anios\n"); break;
        case MAMUT:      printf("Extinto hace 4 mil anios\n");          break;
        case HUMANO:     printf("Aun por aqui\n");                      break;
    }
    printf("MAMUT vale %d\n", MAMUT);          //> En C, un enum es un entero con nombre
    return 0;
}
```

Si olvidas un valor del `enum` en el `switch`, `-Wall` te avisa (*enumeration value not handled in switch*). Si quieres una caída intencional entre casos con sentencias, escribe el comentario `/* fall through */` justo antes del siguiente `case`: gcc con `-Wextra` lo reconoce y deja de advertir (C23 añade además `[[fallthrough]];`). Y si necesitas declarar una variable dentro de un `case`, encierra ese `case` en llaves `{ }`.
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

**C. Código en C**

```c run title="calculadora.c" runs="12 + 5|12 / 5|7 / 0|3 ^ 2"
#include <stdio.h>
int main(void)
{
    double a, b;
    char op;
    printf("Operacion (ej. 12 + 5): ");
    scanf("%lf %c %lf", &a, &op, &b);            //> Número, carácter (el espacio salta los blancos) y número
    switch (op)
    {
        case '+': printf("= %.2f\n", a + b); break;
        case '-': printf("= %.2f\n", a - b); break;
        case '*': printf("= %.2f\n", a * b); break;
        case '/':
            if (b != 0)                            //> Un if DENTRO de un case: decisiones combinadas
                printf("= %.2f\n", a / b);
            else
                printf("Error: division entre cero\n");
            break;
        default:
            printf("Operador invalido: %c\n", op);
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
@hl(no, "No: double, cadenas,\nrangos, variables")
@sub(e, "enum\n/* fall through */")
s -> c; c -> b; s -> d; c -> g; s -> no [style=dashed]; s -> e [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1 · Plantilla de menú
```c run title="plantilla_menu.c" stdin="2\n"
#include <stdio.h>
int main(void)
{
    int opcion;
    printf("1. Opcion uno\n2. Opcion dos\n3. Salir\nElige: ");
    scanf("%d", &opcion);
    switch (opcion)
    {
        case 1:
            printf("Elegiste uno\n");
            break;
        case 2:
            printf("Elegiste dos\n");
            break;
        case 3:
            printf("Hasta luego\n");
            break;
        default:
            printf("Opcion invalida\n");
    }
    return 0;
}
```

| Situación | Patrón |
|---|---|
| Opción con número | `case 1:` |
| Opción con letra, sin importar mayúsculas | `case 'a': case 'A':` (lee con `scanf(" %c", &c)`) |
| Etiqueta con nombre | `#define SALIR 4` … `case SALIR:` · o `enum { SALDO = 1, DEPOSITO, RETIRO, SALIR };` |
| Rango 0–100 en bloques de 10 | `switch (nota / 10) { case 10: case 9: … }` |
| Variable local dentro de un caso | `case 2: { int x = 5; … break; }` |
| Caída intencional | `/* fall through */` antes del siguiente `case` |
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿La expresión del <code>switch</code> es entera o <code>char</code> (no <code>double</code> ni cadena)?</li>
<li>¿Cada <code>case</code> tiene un valor constante, distinto de los demás, y termina en dos puntos?</li>
<li>¿Cada <code>case</code> termina con <code>break</code> (salvo caída intencional)?</li>
<li>¿Hay un <code>default</code> para opciones inválidas?</li>
<li>¿Los caracteres van entre comillas simples: <code>case 'A':</code>?</li>
<li>¿Probé cada opción y al menos una opción inválida?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Olvidar `break` (error de lógica).** ¿Por qué con la opción 1 aparecen dos mensajes?

```c run stdin="1\n"
#include <stdio.h>
int main(void)
{
    int op;
    scanf("%d", &op);
    switch (op)
    {
        case 1: printf("Cafe: $30\n");   //> Falta break
        case 2: printf("Te: $25\n");  break;
        default: printf("No disponible\n");
    }
    return 0;
}
```
*Corrección:* `break;` al final del `case 1`. `gcc -Wextra` lo habría señalado: *this statement may fall through*.

**b) Valor repetido en dos `case`.**

```c err
#include <stdio.h>
int main(void)
{
    int op = 1;
    switch (op)
    {
        case 1: printf("A\n"); break;
        case 1: printf("B\n"); break;
    }
    return 0;
}
```

**c) Usar una variable como etiqueta.** Las etiquetas deben conocerse al compilar.

```c err
#include <stdio.h>
int main(void)
{
    int op = 1, limite = 3;
    switch (op)
    {
        case limite: printf("Limite\n"); break;
    }
    return 0;
}
```
*Corrección:* `#define LIMITE 3` (o una constante de `enum`) o una escalera `if`. Ojo: en C, ni siquiera `const int limite = 3;` sirve como etiqueta, porque `const` crea una variable de solo lectura, no una constante del compilador.

**d) Declarar una variable justo después de un `case`.** En C17 estándar una etiqueta debe ir seguida de una *sentencia*, y una declaración no lo es. gcc lo acepta como extensión, pero con `-Wpedantic` (que exige el estándar) lo señala; además, `doble` sería visible, sin inicializar, en los demás casos.

```c warn flags="-Wpedantic"
#include <stdio.h>
int main(void)
{
    int op = 2;
    switch (op)
    {
        case 1:
            int doble = op * 2;
            printf("%d\n", doble);
            break;
        case 2:
            printf("dos\n");
            break;
    }
    return 0;
}
```
*Corrección:* `case 1: { int doble = op * 2; printf("%d\n", doble); break; }`. Las llaves crean un bloque: la variable existe solo dentro de su caso. (En C23 la declaración tras la etiqueta ya es válida, pero las llaves siguen siendo la forma más clara.)

**e) Comparar con `'1'` cuando se leyó un `int`** (o al revés): si `op` es `int` (`%d`), usa `case 1:`; si es `char` (`%c`), usa `case '1':`.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Comandos de un robot | Variabilidad
```c run title="robot.c" runs="A|i|X"
#include <stdio.h>
int main(void)
{
    char cmd;
    printf("Comando (A=avanzar, R=retroceder, I=izq, D=der): ");
    scanf(" %c", &cmd);
    switch (cmd)
    {
        case 'A': case 'a': printf("Motores hacia adelante\n"); break;
        case 'R': case 'r': printf("Motores en reversa\n");     break;
        case 'I': case 'i': printf("Girando a la izquierda\n"); break;
        case 'D': case 'd': printf("Girando a la derecha\n");   break;
        default:            printf("Comando desconocido\n");
    }
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Prueba **todas** las opciones de cada menú y al menos una inválida.

:::tarea A | T1. Día de la semana: estudia el ejemplo y resuelve el gemelo | 15 min | Ejemplo resuelto, Variabilidad
**Contexto.** Una app de calendario recibe el número de día (1 = lunes … 7 = domingo).

```c run title="dia.c" runs="3|7|9"
#include <stdio.h>
int main(void)
{
    int d;
    printf("Dia (1-7): ");
    scanf("%d", &d);
    switch (d)
    {
        case 1: printf("Lunes\n");     break;   //> Una línea por caso: se lee como una tabla
        case 2: printf("Martes\n");    break;
        case 3: printf("Miercoles\n"); break;
        case 4: printf("Jueves\n");    break;
        case 5: printf("Viernes\n");   break;
        case 6: printf("Sabado\n");    break;
        case 7: printf("Domingo\n");   break;
        default: printf("Dia invalido\n");      //> Cualquier otro número
    }
    return 0;
}
```

**Gemelo.** Escribe `mes.c`: lee un número de mes (1–12) y muestra su nombre; si no existe, «Mes inválido».

:::solucion | T1
```c run title="mes.c" runs="2|12|13"
#include <stdio.h>
int main(void)
{
    int m;
    printf("Mes (1-12): ");
    scanf("%d", &m);
    switch (m)
    {
        case 1:  printf("Enero\n");      break;
        case 2:  printf("Febrero\n");    break;
        case 3:  printf("Marzo\n");      break;
        case 4:  printf("Abril\n");      break;
        case 5:  printf("Mayo\n");       break;
        case 6:  printf("Junio\n");      break;
        case 7:  printf("Julio\n");      break;
        case 8:  printf("Agosto\n");     break;
        case 9:  printf("Septiembre\n"); break;
        case 10: printf("Octubre\n");    break;
        case 11: printf("Noviembre\n");  break;
        case 12: printf("Diciembre\n");  break;
        default: printf("Mes invalido\n");
    }
    return 0;
}
```
:::
:::

:::tarea A | T2. Menú de la cafetería (completa con pistas) | 20 min | Problema por completar
**Contexto.** La cafetería escolar quiere un menú en su pantalla táctil. El cliente elige producto y cantidad; el programa muestra el total.

```c blank title="cafeteria.c"
#include <stdio.h>
int main(void)
{
    int opcion, cantidad;
    double precio = 0;
    printf("1. Torta $35\n2. Jugo $20\n3. Fruta $15\nOpcion y cantidad: ");
    scanf("%d %d", &opcion, &cantidad);
    __1__ (opcion)                         // 1: palabra clave de seleccion multiple
    {
        case 1: precio = 35; __2__;        // 2: termina este caso
        __3__ 2: precio = 20; break;       // 3: etiqueta
        case 3: precio = 15; break;
        __4__:                             // 4: opcion por omision
            printf("Opcion invalida\n");
    }
    if (precio > 0)
        printf("Total: $%.2f\n", __5__);  // 5: expresion del total
    return 0;
}
```

:::solucion | T2
{{c:1}} `switch` · {{c:2}} `break` · {{c:3}} `case` · {{c:4}} `default` · {{c:5}} `precio * cantidad`

```c run title="cafeteria.c" runs="1 2|3 4|5 1"
#include <stdio.h>
int main(void)
{
    int opcion, cantidad;
    double precio = 0;
    printf("1. Torta $35\n2. Jugo $20\n3. Fruta $15\nOpcion y cantidad: ");
    scanf("%d %d", &opcion, &cantidad);
    switch (opcion)
    {
        case 1: precio = 35; break;
        case 2: precio = 20; break;
        case 3: precio = 15; break;
        default:
            printf("Opcion invalida\n");
    }
    if (precio > 0)
        printf("Total: $%.2f\n", precio * cantidad);
    return 0;
}
```
:::
:::

:::tarea AB | T3. ¿Cuántos días tiene el mes? (completa sin pistas) | 20 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Una agenda necesita saber cuántos días tiene un mes. Usa casos **agrupados** y reutiliza la condición de año bisiesto del Tema 04 (T3).

```c blank title="dias_mes.c"
#include <stdio.h>
int main(void)
{
    int mes, anio;
    printf("Mes y anio: ");
    scanf("%d %d", &mes, &anio);
    switch (mes)
    {
        case 1: case 3: case 5: case 7: __1__ case 10: case 12:
            printf("31 dias\n");
            __2__
        case 4: case 6: __3__ case 11:
            printf("30 dias\n");
            break;
        case 2:
            if (__4__)
                printf("29 dias\n");
            else
                printf("28 dias\n");
            break;
        __5__
            printf("Mes invalido\n");
    }
    return 0;
}
```

:::solucion | T3
{{c:1}} `case 8:` · {{c:2}} `break;` · {{c:3}} `case 9:` · {{c:4}} `(anio % 4 == 0 && anio % 100 != 0) || anio % 400 == 0` · {{c:5}} `default:`

```c run title="dias_mes.c" runs="8 2025|9 2025|2 2024|2 1900|14 2025"
#include <stdio.h>
int main(void)
{
    int mes, anio;
    printf("Mes y anio: ");
    scanf("%d %d", &mes, &anio);
    switch (mes)
    {
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            printf("31 dias\n");
            break;
        case 4: case 6: case 9: case 11:
            printf("30 dias\n");
            break;
        case 2:
            if ((anio % 4 == 0 && anio % 100 != 0) || anio % 400 == 0)
                printf("29 dias\n");
            else
                printf("28 dias\n");
            break;
        default:
            printf("Mes invalido\n");
    }
    return 0;
}
```
:::
:::

:::tarea AB | T4. Convertidor de unidades (problema convencional) | 30 min | Variabilidad
**Contexto.** Diseña un convertidor con menú: `1` kilómetros → millas (× 0.621371), `2` kilogramos → libras (× 2.20462), `3` Celsius → Fahrenheit, `4` litros → galones (× 0.264172). El usuario elige la opción y escribe el valor; el programa muestra el resultado con dos decimales o «Opción inválida». Usa constantes para los factores.

:::solucion | T4
```c run title="convertidor.c" runs="1 42.195|3 36.5|4 50|7 1"
#include <stdio.h>
#define KM_MI 0.621371
#define KG_LB 2.20462
#define L_GAL 0.264172
int main(void)
{
    int op;
    double v;
    printf("1) km->mi 2) kg->lb 3) C->F 4) L->gal\nOpcion y valor: ");
    scanf("%d %lf", &op, &v);
    switch (op)
    {
        case 1: printf("%.2f km = %.2f mi\n", v, v * KM_MI); break;
        case 2: printf("%.2f kg = %.2f lb\n", v, v * KG_LB); break;
        case 3: printf("%.2f C = %.2f F\n", v, 9.0 / 5 * v + 32); break;
        case 4: printf("%.2f L = %.2f gal\n", v, v * L_GAL); break;
        default: printf("Opcion invalida\n");
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

```c run title="letra.c" runs="100|87|60|42"
#include <stdio.h>
int main(void)
{
    int nota;
    scanf("%d", &nota);
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
    printf("Escalera: %c  switch: %c\n", l1, l2);
    return 0;
}
```
:::
:::

:::tarea B | T6. La máquina expendedora rebelde (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
**Contexto.** Con la opción `B` la máquina entrega papas **y** galletas **y** dice «opción inválida». Con la `c` minúscula no entrega nada. **Explica** cada comportamiento y corrige el programa.

```c run title="expendedora_bug.c" runs="B|c"
#include <stdio.h>
int main(void)
{
    char sel;
    printf("Seleccion: ");
    scanf(" %c", &sel);
    switch (sel)
    {
        case 'A': printf("Refresco\n"); break;
        case 'B': printf("Papas\n");
        case 'C': printf("Galletas\n");
        default: printf("Opcion invalida\n");
    }
    return 0;
}
```

{{lineas:3}}

:::solucion | T6
Con `B` entra en `case 'B'` y, sin `break`, **cae** en `case 'C'` y en `default`. Con `c` no coincide con `'C'` (C distingue mayúsculas) y llega a `default`… que en la salida sí aparece: «Opción inválida», pero el usuario esperaba galletas. Corrección: `break` en cada caso y etiquetas para minúsculas.

```c run title="expendedora.c" runs="B|c|z"
#include <stdio.h>
int main(void)
{
    char sel;
    printf("Seleccion: ");
    scanf(" %c", &sel);
    switch (sel)
    {
        case 'A': case 'a': printf("Refresco\n"); break;
        case 'B': case 'b': printf("Papas\n");    break;
        case 'C': case 'c': printf("Galletas\n"); break;
        default: printf("Opcion invalida\n");
    }
    return 0;
}
```
:::
:::

:::tarea B | T7. Niveles de acceso (imaginación + `enum`) | 25 min | Imaginación
**Contexto.** En un juego, cada rol tiene los permisos de los roles inferiores **más** los suyos. El programa usa una caída **intencional**.

1. **Imagina** (sin ejecutar) qué imprime para `nivel = 2`, `nivel = 0` y `nivel = 5`.
2. Reescríbelo con `enum rol { INVITADO, JUGADOR, MODERADOR, ADMIN };` y marca las caídas con el comentario `/* fall through */`.

```c check title="permisos.c"
#include <stdio.h>
int main(void)
{
    int nivel;
    scanf("%d", &nivel);
    switch (nivel)
    {
        case 3: printf("- Borrar servidores\n");
        case 2: printf("- Expulsar jugadores\n");
        case 1: printf("- Chatear\n");
        case 0: printf("- Ver partidas\n"); break;
        default: printf("Nivel desconocido\n");
    }
    return 0;
}
```

{{lineas:3}}

:::solucion | T7
`nivel = 2` → Expulsar, Chatear, Ver partidas · `nivel = 0` → Ver partidas · `nivel = 5` → Nivel desconocido. Con los comentarios, `gcc -Wextra` compila esta versión sin avisos:

```c run title="permisos_enum.c"
#include <stdio.h>
enum rol { INVITADO, JUGADOR, MODERADOR, ADMIN };
int main(void)
{
    enum rol r = MODERADOR;
    switch (r)
    {
        case ADMIN:
            printf("- Borrar servidores\n");
            /* fall through */
        case MODERADOR:
            printf("- Expulsar jugadores\n");
            /* fall through */
        case JUGADOR:
            printf("- Chatear\n");
            /* fall through */
        case INVITADO:
            printf("- Ver partidas\n");
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
```c run title="cajero.c" runs="1|2 800|3 120|3 3000|3 500|9"
#include <stdio.h>
int main(void)
{
    double saldo = 2500, monto;
    int op;
    printf("1) Saldo 2) Depositar 3) Retirar 4) Salir: ");
    scanf("%d", &op);
    switch (op)
    {
        case 1:
            printf("Saldo: $%.2f\n", saldo);
            break;
        case 2:
            scanf("%lf", &monto);
            if (monto > 0) { saldo += monto; printf("Nuevo saldo: $%.2f\n", saldo); }
            else printf("Monto invalido\n");
            break;
        case 3:
            scanf("%lf", &monto);
            if (monto <= 0 || (int)monto % 50 != 0)
                printf("El retiro debe ser positivo y multiplo de 50\n");
            else if (monto > saldo)
                printf("Fondos insuficientes\n");
            else { saldo -= monto; printf("Retire su efectivo. Saldo: $%.2f\n", saldo); }
            break;
        case 4:
            printf("Gracias por su visita\n");
            break;
        default:
            printf("Opcion invalida\n");
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

**Segmento 2 — Lecturas dentro de cada caso.** {{como}} Cada figura pide datos distintos, así que pongo los `scanf` **dentro** de su `case` y declaro las variables antes del `switch`. {{porque}} En C17 estándar una etiqueta como `case 3:` no puede ir seguida de una declaración, y una variable declarada en un caso sería visible, sin inicializar, en los demás; declararlas antes evita ambos problemas.

**Segmento 3 — No olvidar `break`.** {{como}} Escribo el `break` de cada caso **antes** de escribir su contenido. {{porque}} Es el error más común en `switch`: sin él, el cuadrado también calcularía el rectángulo con datos basura.

**Segmento 4 — La opción que nadie elige.** {{como}} Agrego `default` y pruebo con 1, 2, 3 y 8. {{porque}} Los usuarios se equivocan; un menú sin `default` simplemente no responde y parece descompuesto.

```c run title="areas.c" runs="1 4|2 3 5|3 2|8"
#include <stdio.h>
int main(void)
{
    const double PI = 3.14159265358979;
    int fig;
    double a, b;
    printf("1) Cuadrado 2) Rectangulo 3) Circulo: ");
    scanf("%d", &fig);
    switch (fig)
    {
        case 1:
            scanf("%lf", &a);
            printf("Area: %.2f\n", a * a);
            break;
        case 2:
            scanf("%lf %lf", &a, &b);
            printf("Area: %.2f\n", a * b);
            break;
        case 3:
            scanf("%lf", &a);
            printf("Area: %.2f\n", PI * a * a);
            break;
        default:
            printf("Figura invalida\n");
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
8. ¿Cómo indicas en C17 que una caída entre casos es intencional, para que `gcc -Wextra` no avise?
9. Menciona una ventaja de `enum` sobre usar números (1, 2, 3) como opciones.
10. ¿Por qué `switch (nota / 10)` permite trabajar con rangos de calificaciones?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida** para `x = 2` y para `x = 4`:

```c check title="p1.c"
#include <stdio.h>
int main(void)
{
    int x;
    scanf("%d", &x);
    switch (x)
    {
        case 1: printf("A");
        case 2: printf("B");
        case 3: printf("C"); break;
        case 4: printf("D");
        default: printf("E");
    }
    printf("\n");
    return 0;
}
```

**P2. Corrige** los tres errores:

```c blank title="p2.c"
char t;
scanf(" %c", &t);
switch (t) {
    case "a": printf("alfa"); break;
    case 'b' printf("beta"); break;
    case 'a': printf("otra alfa"); break;
}
```

**P3. Convierte a `switch`** esta escalera: `if (c == 'x' || c == 'X') printf("salir"); else if (c == 'g') printf("guardar"); else printf("?");`

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
1 Enteros: `int`, `char`, `long`, enumeraciones (no `double` ni cadenas) · 2 Termina el `switch` y continúa después de su llave de cierre · 3 La ejecución «cae» al siguiente `case` · 4 Cuando ningún `case` coincide · 5 Falso: los `case` llevan valores constantes, no condiciones · 6 `case 's': case 'S':` seguidos · 7 `Segun … Hacer … FinSegun` · 8 Con el comentario `/* fall through */` justo antes del siguiente `case` (en C23 también con `[[fallthrough]];`) · 9 Los valores tienen nombre (`ADMIN`), el código se autodocumenta y `-Wall` avisa si un valor no tiene `case` · 10 La división entera convierte cada rango de 10 en un solo número exacto (87 → 8).
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.**

```c run title="p1.c" runs="2|4"
#include <stdio.h>
int main(void)
{
    int x;
    scanf("%d", &x);
    switch (x)
    {
        case 1: printf("A");
        case 2: printf("B");
        case 3: printf("C"); break;
        case 4: printf("D");
        default: printf("E");
    }
    printf("\n");
    return 0;
}
```

**P2.** `"a"` es cadena → `'a'`; falta `:` en `case 'b'`; `case 'a'` está repetido (eliminar o cambiar el valor).

**P3.** `switch (c) { case 'x': case 'X': printf("salir"); break; case 'g': printf("guardar"); break; default: printf("?"); }`

**P4.**

```c run title="ppt.c" runs="P|r|T|Z"
#include <stdio.h>
int main(void)
{
    char j;
    printf("Tu jugada (R=piedra, P=papel, T=tijera): ");
    scanf(" %c", &j);
    printf("La computadora eligio piedra. ");
    switch (j)
    {
        case 'R': case 'r': printf("Empate\n"); break;
        case 'P': case 'p': printf("Ganaste: papel envuelve piedra\n"); break;
        case 'T': case 't': printf("Perdiste: piedra rompe tijera\n"); break;
        default: printf("Jugada invalida\n");
    }
    return 0;
}
```
:::
