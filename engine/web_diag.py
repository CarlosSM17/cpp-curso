"""Diagnóstico interactivo por bloque (versión web de la prueba diagnóstica del Tema 00).

Cada bloque tiene 8 reactivos de opción múltiple: 5 de conocimiento declarativo (recall)
y 3 de lectura de código (comprehension). Los reactivos con programa se compilan y
ejecutan al generar el sitio para comprobar que la opción correcta coincide con la salida real.
"""

INC = "#include <stdio.h>\n"

BLOQUES = {
    "I": [
        dict(q="¿Con qué función empieza a ejecutarse todo programa en C?",
             opts=["`start()`", "`main()`", "`#include`", "`printf()`"], ok=1,
             exp="La ejecución siempre comienza en `main`; `#include` es una directiva del preprocesador y `printf` es una función de la biblioteca estándar."),
        dict(q="¿Qué tipo de dato usarías para guardar un precio como 3.75?",
             opts=["`int`", "`char`", "`double`", "`bool`"], ok=2,
             exp="`double` guarda números con parte decimal; un `int` la truncaría."),
        dict(q="¿Cuánto vale la expresión `17 % 5`?",
             opts=["3", "3.4", "2", "5"], ok=2,
             exp="`%` es el residuo de la división entera: 17 = 3 × 5 + 2."),
        dict(q="Si `a` y `b` son `int`, con `a = 7` y `b = 2`, ¿cuánto vale `a / b`?",
             opts=["3.5", "3", "4", "1"], ok=1,
             exp="Entre enteros, `/` es división entera: se descarta la parte decimal."),
        dict(q="¿Qué ocurre con `if (x = 5)`?",
             opts=["Compara `x` con 5", "Asigna 5 a `x` y la condición resulta verdadera",
                   "No compila", "Compara y después asigna"], ok=1,
             exp="`=` asigna; el valor de la asignación (5) es distinto de cero y cuenta como verdadero. Para comparar se usa `==` (gcc con `-Wall` lo advierte)."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int main(void)
{
    int op = 2;
    switch (op)
    {
        case 1: printf("A");
        case 2: printf("B");
        case 3: printf("C"); break;
        default: printf("D");
    }
    printf("\\n");
    return 0;
}""", opts=["B", "BC", "BCD", "D"], ok=1, check=True,
             exp="Entra por `case 2` y, como no hay `break`, cae en `case 3`; ahí el `break` termina el `switch`."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int main(void)
{
    double nota = 7.5;
    if (nota >= 9)
        printf("Excelente");
    else if (nota >= 7)
        printf("Bien");
    else if (nota >= 6)
        printf("Suficiente");
    else
        printf("Reprobado");
    printf("\\n");
    return 0;
}""", opts=["Excelente", "Bien", "Suficiente", "Bien Suficiente"], ok=1, check=True,
             exp="La escalera se evalúa de arriba abajo y solo se ejecuta el primer bloque verdadero: 7.5 ≥ 7."),
        dict(q="¿Cuántos errores de sintaxis tiene este programa?",
             code=INC + """int main(void)
{
    int edad
    printf("Edad: ");
    scanf("%d", &edad);
    printf("Tienes %d anios\\n", edad)
    return 0;
}""", opts=["Ninguno", "1", "2", "3"], ok=2, err=True,
             exp="Faltan dos `;`: al final de `int edad` y al final del segundo `printf`."),
    ],
    "II": [
        dict(q="¿Cuántas veces se repite el cuerpo de `for (int i = 0; i < 4; i++)`?",
             opts=["3", "4", "5", "Infinitas"], ok=1,
             exp="`i` toma los valores 0, 1, 2 y 3; con 4 la condición es falsa."),
        dict(q="¿Qué distingue a `do-while` de `while`?",
             opts=["`do-while` no necesita condición", "El cuerpo de `do-while` se ejecuta al menos una vez",
                   "`while` siempre se ejecuta al menos una vez", "Solo `do-while` admite `break`"], ok=1,
             exp="`do-while` evalúa la condición al final; `while`, antes de entrar."),
        dict(q="En `int a[5];`, ¿cuál es el índice del último elemento?",
             opts=["5", "4", "6", "0"], ok=1,
             exp="Los índices van de 0 a tamaño − 1."),
        dict(q="¿Qué valor queda en una variable acumuladora `suma` que no se inicializó antes del ciclo?",
             opts=["Siempre 0", "Un valor impredecible (basura)", "El tamaño del ciclo", "No compila"], ok=1,
             exp="Una variable local sin inicializar contiene lo que haya quedado en esa memoria: inicializa siempre `suma = 0`."),
        dict(q="¿Qué instrucción termina de inmediato el ciclo que la contiene?",
             opts=["`continue`", "`return 0` dentro de un `if`", "`break`", "`exit`"], ok=2,
             exp="`break` termina el ciclo más interno; `continue` salta a la siguiente vuelta."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int main(void)
{
    int suma = 0;
    for (int i = 1; i <= 6; i++)
    {
        if (i % 2 == 0)
            suma += i;
        else
            printf("%d ", i);
    }
    printf("| %d\\n", suma);
    return 0;
}""", opts=["1 3 5 | 12", "2 4 6 | 9", "1 3 5 | 21", "1 2 3 4 5 6 | 12"], ok=0, check=True,
             exp="Muestra los impares y acumula los pares: 2 + 4 + 6 = 12."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int main(void)
{
    int v[5] = {4, 1, 3, 5, 2};
    for (int i = 0; i < 4; i++)
        if (v[i] > v[i + 1])
        {
            int t = v[i];
            v[i] = v[i + 1];
            v[i + 1] = t;
        }
    for (int i = 0; i < 5; i++)
        printf("%d ", v[i]);
    printf("\\n");
    return 0;
}""", opts=["1 2 3 4 5", "1 3 4 2 5", "4 1 3 5 2", "1 4 3 2 5"], ok=1, check=True,
             exp="Es una sola pasada de la burbuja: el mayor (5) llega al final, pero el resto aún no está ordenado."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int main(void)
{
    int m[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int s = 0;
    for (int i = 0; i < 3; i++)
        s += m[i][i];
    printf("%d\\n", s);
    return 0;
}""", opts=["45", "15", "6", "24"], ok=1, check=True,
             exp="Suma la diagonal principal: 1 + 5 + 9 = 15."),
    ],
    "III": [
        dict(q="¿Qué significa que una función sea `void`?",
             opts=["Que no recibe parámetros", "Que no devuelve ningún valor", "Que es recursiva", "Que es global"], ok=1,
             exp="`void` indica que la función no devuelve valor (es un procedimiento)."),
        dict(q="¿Qué necesita toda función recursiva para terminar?",
             opts=["Un ciclo `for`", "Un caso base", "Una variable global", "Un parámetro puntero"], ok=1,
             exp="El caso base se resuelve sin llamarse de nuevo; cada llamada debe acercarse a él."),
        dict(q="Si `a` es una variable `Alumno` con un miembro `nac` de tipo `Fecha`, ¿cómo se accede al año?",
             opts=["`a.anio`", "`a.nac.anio`", "`a->nac->anio`", "`Fecha.anio`"], ok=1,
             exp="Con estructuras anidadas se encadenan los puntos: variable.miembro.miembro."),
        dict(q="¿Qué devuelve `strcmp(\"ana\", \"ana\")`?",
             opts=["1", "0", "`true`", "3, la longitud de las cadenas"], ok=1,
             exp="`strcmp` devuelve 0 cuando las cadenas son iguales (un valor negativo o positivo, según el orden alfabético, cuando no lo son). Por eso se escribe `if (strcmp(a, b) == 0)`."),
        dict(q="Una variable declarada dentro de una función…",
             opts=["Existe en todo el programa", "Solo existe mientras se ejecuta esa función",
                   "Conserva su valor entre llamadas", "Es visible en `main`"], ok=1,
             exp="Es local: se crea al entrar a la función y se destruye al salir (salvo que sea `static`)."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """void f(int a, int *b)
{
    a++;
    (*b)++;
}
int main(void)
{
    int x = 1, y = 1;
    f(x, &y);
    printf("%d %d\\n", x, y);
    return 0;
}""", opts=["1 1", "2 2", "1 2", "2 1"], ok=2, check=True,
             exp="`a` recibe una copia de `x` (por valor); `b` recibe la dirección de `y`, y `(*b)++` modifica a `y`."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int s(int n)
{
    if (n == 0) return 0;
    return n + s(n - 1);
}
int main(void)
{
    printf("%d\\n", s(4));
    return 0;
}""", opts=["4", "10", "24", "0"], ok=1, check=True,
             exp="s(4) = 4 + 3 + 2 + 1 + 0 = 10."),
        dict(q="¿Qué imprime este programa?",
             code=INC + "#include <string.h>\n" + """int main(void)
{
    char s[] = "programa";
    printf("%zu %zu\\n", strlen(s), sizeof s);
    return 0;
}""", opts=["8 9", "8 8", "9 9", "9 8"], ok=0, check=True,
             exp="`strlen` cuenta los caracteres anteriores al `'\\0'` (8); `sizeof` mide el arreglo completo, incluido el `'\\0'` (9)."),
    ],
    "IV": [
        dict(q="Un puntero es una variable que guarda…",
             opts=["un valor entero", "una dirección de memoria", "un arreglo completo", "un tipo de dato"], ok=1,
             exp="El contenido de un puntero es la dirección de otra variable."),
        dict(q="¿Cómo se libera la memoria reservada con `int *a = malloc(10 * sizeof *a);`?",
             opts=["`delete a;`", "`free(a);`", "`free(*a);`", "`a = NULL;`"], ok=1,
             exp="Todo bloque obtenido con `malloc`, `calloc` o `realloc` se libera una sola vez con `free`, pasándole el puntero que devolvió la reserva."),
        dict(q="¿Qué es una fuga de memoria?",
             opts=["Leer fuera de un arreglo", "Memoria reservada cuya dirección se perdió sin liberarla",
                   "Un puntero nulo", "Una variable global"], ok=1,
             exp="Si se pierde el único puntero a un bloque antes del `free`, ese bloque queda ocupado e inaccesible."),
        dict(q="¿Qué modo de `fopen` agrega datos al final de un archivo sin borrar lo que ya tenía?",
             opts=["`\"w\"`", "`\"r\"`", "`\"a\"`", "`\"wb\"`"], ok=2,
             exp="`\"a\"` (append) escribe al final; `\"w\"` borra el contenido anterior."),
        dict(q="En un módulo, una función definida como `static` en `pila.c`…",
             opts=["solo puede usarse dentro de `pila.c`", "se puede llamar desde `main.c` si se declara su prototipo",
                   "conserva sus variables locales entre llamadas", "debe declararse en `pila.h`"], ok=0,
             exp="`static` fuera de una función da enlace interno: el nombre solo existe en ese archivo y el enlazador no lo ofrece a otros módulos."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int main(void)
{
    int a = 5;
    int *p = &a;
    *p = *p + 3;
    printf("%d\\n", a);
    return 0;
}""", opts=["5", "8", "3", "La dirección de a"], ok=1, check=True,
             exp="`*p` es «lo apuntado por p», es decir, `a`: se modifica a través del puntero."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int main(void)
{
    int v[4] = {10, 20, 30, 40};
    int *p = v;
    p += 2;
    printf("%d %d\\n", *p, *(p - 1));
    return 0;
}""", opts=["30 20", "20 10", "12 11", "30 40"], ok=0, check=True,
             exp="Sumar 2 al puntero lo mueve dos elementos: apunta a `v[2]`; `p - 1` apunta a `v[1]`."),
        dict(q="¿Qué imprime este programa?",
             code=INC + "#include <stdlib.h>\n" + """typedef struct { int x, y; } Punto;
int main(void)
{
    Punto *p = malloc(2 * sizeof *p);
    if (p == NULL) return 1;
    p[0].x = 1;
    p[0].y = 2;
    p[1] = p[0];
    p[1].y += 5;
    printf("%d %d\\n", (p + 1)->x, p[1].y);
    free(p);
    return 0;
}""", opts=["1 7", "1 2", "2 7", "7 1"], ok=0, check=True,
             exp="`p[1] = p[0]` copia la estructura completa; después solo cambia `p[1].y` (2 + 5). `(p + 1)->x` es lo mismo que `p[1].x`."),
    ],
}

NOMBRES = {"I": "Fundamentos (temas 01 a 05)", "II": "Repetición y arreglos (temas 06 a 09)",
           "III": "Modularidad y datos (temas 10 a 13)", "IV": "Memoria, archivos y módulos (temas 14 a 17)"}


def verificar(compile_run):
    """Compila y ejecuta los reactivos con código; falla si la opción correcta no coincide con la salida."""
    n = 0
    for b, items in BLOQUES.items():
        for i, it in enumerate(items, 1):
            if it.get("err"):
                compile_run(it["code"], "err")
                n += 1
            elif it.get("check"):
                out = compile_run(it["code"], "run")["stdout"].strip()
                esperado = it["opts"][it["ok"]].strip("`")
                if out != esperado:
                    raise RuntimeError(f"Diagnóstico {b}.{i}: salida real {out!r} ≠ opción correcta {esperado!r}")
                otros = [o.strip("`") for k, o in enumerate(it["opts"]) if k != it["ok"]]
                if out in otros:
                    raise RuntimeError(f"Diagnóstico {b}.{i}: dos opciones coinciden con la salida")
                n += 1
    return n
