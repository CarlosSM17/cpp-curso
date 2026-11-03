"""Diagnóstico interactivo por bloque (versión web de la prueba diagnóstica del Tema 00).

Cada bloque tiene 8 reactivos de opción múltiple: 5 de conocimiento declarativo (recall)
y 3 de lectura de código (comprehension). Los reactivos con programa se compilan y
ejecutan al generar el sitio para comprobar que la opción correcta coincide con la salida real.
"""

INC = "#include <iostream>\nusing namespace std;\n"

BLOQUES = {
    "I": [
        dict(q="¿Con qué función empieza a ejecutarse todo programa en C++?",
             opts=["`start()`", "`main()`", "`#include`", "`cout`"], ok=1,
             exp="La ejecución siempre comienza en `main`; `#include` es una directiva del preprocesador y `cout` es el flujo de salida."),
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
             exp="`=` asigna; el valor de la asignación (5) es distinto de cero y cuenta como verdadero. Para comparar se usa `==`."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int main()
{
    int op = 2;
    switch (op)
    {
        case 1: cout << "A";
        case 2: cout << "B";
        case 3: cout << "C"; break;
        default: cout << "D";
    }
    cout << "\\n";
    return 0;
}""", opts=["B", "BC", "BCD", "D"], ok=1, check=True,
             exp="Entra por `case 2` y, como no hay `break`, cae en `case 3`; ahí el `break` termina el `switch`."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int main()
{
    double nota = 7.5;
    if (nota >= 9)
        cout << "Excelente";
    else if (nota >= 7)
        cout << "Bien";
    else if (nota >= 6)
        cout << "Suficiente";
    else
        cout << "Reprobado";
    cout << "\\n";
    return 0;
}""", opts=["Excelente", "Bien", "Suficiente", "Bien Suficiente"], ok=1, check=True,
             exp="La escalera se evalúa de arriba abajo y solo se ejecuta el primer bloque verdadero: 7.5 ≥ 7."),
        dict(q="¿Cuántos errores de sintaxis tiene este programa?",
             code=INC + """int main()
{
    int edad
    cout << "Edad: ";
    cin >> edad;
    cout << "Tienes " << edad << " anios\\n"
    return 0;
}""", opts=["Ninguno", "1", "2", "3"], ok=2, err=True,
             exp="Faltan dos `;`: al final de `int edad` y al final de la segunda línea con `cout`."),
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
             code=INC + """int main()
{
    int suma = 0;
    for (int i = 1; i <= 6; i++)
    {
        if (i % 2 == 0)
            suma += i;
        else
            cout << i << " ";
    }
    cout << "| " << suma << "\\n";
    return 0;
}""", opts=["1 3 5 | 12", "2 4 6 | 9", "1 3 5 | 21", "1 2 3 4 5 6 | 12"], ok=0, check=True,
             exp="Muestra los impares y acumula los pares: 2 + 4 + 6 = 12."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int main()
{
    int v[5] = {4, 1, 3, 5, 2};
    for (int i = 0; i < 4; i++)
        if (v[i] > v[i + 1])
        {
            int t = v[i];
            v[i] = v[i + 1];
            v[i + 1] = t;
        }
    for (int x : v) cout << x << " ";
    cout << "\\n";
    return 0;
}""", opts=["1 2 3 4 5", "1 3 4 2 5", "4 1 3 5 2", "1 4 3 2 5"], ok=1, check=True,
             exp="Es una sola pasada de la burbuja: el mayor (5) llega al final, pero el resto aún no está ordenado."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int main()
{
    int m[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int s = 0;
    for (int i = 0; i < 3; i++)
        s += m[i][i];
    cout << s << "\\n";
    return 0;
}""", opts=["45", "15", "6", "24"], ok=1, check=True,
             exp="Suma la diagonal principal: 1 + 5 + 9 = 15."),
    ],
    "III": [
        dict(q="¿Qué significa que una función sea `void`?",
             opts=["Que no recibe parámetros", "Que no devuelve ningún valor", "Que es recursiva", "Que es global"], ok=1,
             exp="`void` indica que la función no devuelve valor (es un procedimiento)."),
        dict(q="¿Qué necesita toda función recursiva para terminar?",
             opts=["Un ciclo `for`", "Un caso base", "Una variable global", "Un parámetro por referencia"], ok=1,
             exp="El caso base se resuelve sin llamarse de nuevo; cada llamada debe acercarse a él."),
        dict(q="Si `a` es una variable `Alumno` con un miembro `nac` de tipo `Fecha`, ¿cómo se accede al año?",
             opts=["`a.anio`", "`a.nac.anio`", "`a->nac->anio`", "`Fecha.anio`"], ok=1,
             exp="Con estructuras anidadas se encadenan los puntos: variable.miembro.miembro."),
        dict(q="¿Qué devuelve `s.find(\"x\")` si la cadena `s` no contiene `x`?",
             opts=["0", "-1 convertido en `int`", "`string::npos`", "Una excepción"], ok=2,
             exp="`find` devuelve `string::npos` cuando no encuentra el texto."),
        dict(q="Una variable declarada dentro de una función…",
             opts=["Existe en todo el programa", "Solo existe mientras se ejecuta esa función",
                   "Conserva su valor entre llamadas", "Es visible en `main`"], ok=1,
             exp="Es local: se crea al entrar a la función y se destruye al salir (salvo que sea `static`)."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """void f(int a, int& b)
{
    a++;
    b++;
}
int main()
{
    int x = 1, y = 1;
    f(x, y);
    cout << x << " " << y << "\\n";
    return 0;
}""", opts=["1 1", "2 2", "1 2", "2 1"], ok=2, check=True,
             exp="`a` recibe una copia de `x` (por valor); `b` es otro nombre de `y` (por referencia)."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int s(int n)
{
    if (n == 0) return 0;
    return n + s(n - 1);
}
int main()
{
    cout << s(4) << "\\n";
    return 0;
}""", opts=["4", "10", "24", "0"], ok=1, check=True,
             exp="s(4) = 4 + 3 + 2 + 1 + 0 = 10."),
        dict(q="¿Qué imprime este programa?",
             code="#include <iostream>\n#include <string>\nusing namespace std;\n" + """int main()
{
    string s = "programa";
    cout << s.size() << " " << s[0] << s.substr(3, 4) << "\\n";
    return 0;
}""", opts=["8 pgram", "8 pogra", "9 pgram", "8 prog"], ok=0, check=True,
             exp="Tiene 8 caracteres; `s[0]` es `p` y `substr(3, 4)` toma 4 caracteres desde el índice 3: `gram`."),
    ],
    "IV": [
        dict(q="Un puntero es una variable que guarda…",
             opts=["un valor entero", "una dirección de memoria", "un arreglo completo", "un tipo de dato"], ok=1,
             exp="El contenido de un puntero es la dirección de otra variable."),
        dict(q="¿Cómo se libera la memoria reservada con `int* a = new int[10];`?",
             opts=["`delete a;`", "`delete[] a;`", "`free(a);`", "`a = nullptr;`"], ok=1,
             exp="Lo que se reserva con `new[]` se libera con `delete[]`."),
        dict(q="¿Qué es una fuga de memoria?",
             opts=["Leer fuera de un arreglo", "Memoria reservada cuya dirección se perdió sin liberarla",
                   "Un puntero nulo", "Una variable global"], ok=1,
             exp="Si se pierde el único puntero a un bloque antes del `delete`, ese bloque queda ocupado e inaccesible."),
        dict(q="¿Qué modo de apertura agrega datos al final de un archivo sin borrar lo que ya tenía?",
             opts=["`ios::out`", "`ios::in`", "`ios::app`", "`ios::trunc`"], ok=2,
             exp="`ios::app` (append) escribe al final; `ofstream` sin modo borra el contenido anterior."),
        dict(q="En una clase, los miembros declarados después de `private:`…",
             opts=["solo se usan dentro de la clase", "se pueden usar desde `main`",
                   "son constantes", "se pueden modificar desde fuera con `objeto.miembro`"], ok=0,
             exp="El encapsulamiento protege los datos: solo los métodos de la clase acceden a lo privado."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int main()
{
    int a = 5;
    int* p = &a;
    *p = *p + 3;
    cout << a << "\\n";
    return 0;
}""", opts=["5", "8", "3", "La dirección de a"], ok=1, check=True,
             exp="`*p` es «lo apuntado por p», es decir, `a`: se modifica a través del puntero."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """int main()
{
    int v[4] = {10, 20, 30, 40};
    int* p = v;
    p += 2;
    cout << *p << " " << *(p - 1) << "\\n";
    return 0;
}""", opts=["30 20", "20 10", "12 11", "30 40"], ok=0, check=True,
             exp="Sumar 2 al puntero lo mueve dos elementos: apunta a `v[2]`; `p - 1` apunta a `v[1]`."),
        dict(q="¿Qué imprime este programa?",
             code=INC + """class T
{
public:
    T(char c) : id{c} { cout << "+" << id; }
    ~T() { cout << "-" << id; }
private:
    char id;
};
int main()
{
    T a{'a'};
    {
        T b{'b'};
    }
    cout << "|";
    return 0;
}""", opts=["+a+b-b|-a", "+a+b|-b-a", "+a+b-a-b|", "+a-a+b-b|"], ok=0, check=True,
             exp="`b` se destruye al cerrar su bloque; `a`, al terminar `main` (después de imprimir `|`)."),
    ],
}

NOMBRES = {"I": "Fundamentos (temas 01 a 05)", "II": "Repetición y arreglos (temas 06 a 09)",
           "III": "Modularidad y datos (temas 10 a 13)", "IV": "Memoria, archivos y objetos (temas 14 a 17)"}


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
