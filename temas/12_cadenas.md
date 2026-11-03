---
num: "12"
archivo: "Tema12_Cadenas_de_caracteres"
titulo: "Cadenas de caracteres: char[] y std::string"
corto: "Cadenas"
lema: "Un texto es un arreglo de caracteres: se recorre, se compara, se busca y se transforma letra por letra."
duracion: "5 h · 3 sesiones"
previos: "Tema 02 (`char`, ASCII, `string`, `getline`), Tema 08 (arreglos) y Tema 10 (funciones)."
fuentes:
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Cap. 10: Cadenas de caracteres (§10.1 Cadena de caracteres, §10.2 Tipo de dato string, §10.3 Entrada y salida, §10.4 Operaciones predefinidas, §10.5 Ejercicios)."
  - "Lospinoso, J. (2019). *C++ Crash Course*. Cap. 2: C-Style Strings. Cap. 15: std::string (Constructing, Element Access, Comparisons, Manipulating Elements, Search, Numeric Conversions)."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §6.1.6: autoexplicación con ejemplos con errores (comparar cadenas sin `strcmp`, `strcpy` ni `strlen`)."
objetivos:
  A:
    - "Distinguir las cadenas de estilo C (`char[]` terminadas en `'\\0'`) y `std::string`."
    - "Leer y mostrar cadenas (`cin >>`, `getline`) y acceder a cada carácter por su índice."
    - "Recorrer cadenas para contar y clasificar caracteres con `<cctype>` (`isalpha`, `isdigit`, `toupper`…)."
    - "Usar las operaciones de `string`: `size`, `+`, `==`, `<`, `substr`, `find`, `insert`, `erase`, `replace`."
  B:
    - "Implementar a mano longitud, copia y comparación de cadenas de C."
    - "Convertir entre texto y números (`stoi`, `stod`, `to_string`)."
    - "Validar formatos de texto (contraseñas, identificadores) con funciones."
    - "Resolver problemas de palabras: invertir, palíndromos, contar palabras, cifrar."
efectos:
  soporte:
    - ["Elementos aislados", "char[] y '\\0' → string → lectura → recorrido → cctype → operaciones → conversiones → C-strings a mano."]
    - ["Atención dividida", "Casillas del texto (con índices y '\\0') junto a cada operación."]
    - ["Ejemplo resuelto", "Analizador de frases: vocales, consonantes, dígitos, espacios y palabras."]
    - ["Movimiento humano", "«Cadena humana»: cada estudiante es una letra; insertar y borrar los obliga a moverse."]
  procedimental:
    - ["Variabilidad", "Mismas operaciones aplicadas a nombres, contraseñas, frases y mensajes cifrados."]
    - ["Autoexplicación", "Errores con cadenas presentados como casos para explicar."]
  tareas:
    - ["Ejemplo resuelto", "T1: iniciales de un nombre + gemelo (nombre de usuario)."]
    - ["Problema por completar", "T2 (palíndromo, con pistas) y T3 (contraseña segura, sin pistas)."]
    - ["Desvanecimiento de guía", "T1 → T4."]
    - ["Solución libre", "T5: descubrir todo lo posible sobre una frase."]
    - ["Autoexplicación", "T6: comparar cadenas sin funciones de biblioteca (ejemplo con errores de la tesis §6.1.6)."]
    - ["Imaginación", "T7: imaginar el estado de un `string` tras varias operaciones."]
    - ["Memoria colectiva de trabajo", "T8: el juego del ahorcado por equipos."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "`string`, índices, recorrido, `<cctype>`, `find`/`substr`."
    B: "Cadenas de C y su manejo manual, conversiones numéricas, `string::npos`."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4, dibujando las casillas del texto en papel."
    B: "T5, T6, T7 autónomas; T8 como integradores."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Cifrado César (T4)."
    B: "Comparador de cadenas propio con explicación (T6)."
  Entorno:
    comp: "Información procedimental"
    A: "Tabla ASCII impresa a la mano."
    B: "Documentación de `std::string` (cppreference) para explorar más operaciones."
plan:
  - ["Sesión 1", "Soporte + tareas", "Cadena humana; conceptos 1–5; ejemplo resuelto; T1, T2.", "100 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–8; T3, T4; Ruta B: T6, T7.", "100 min"]
  - ["Sesión 3", "Tareas + evaluación", "T5, T8 ahorcado; protocolo verbal; tests.", "100 min"]
glosario:
  - ["cadena de caracteres", "string", "Secuencia de caracteres que representa un texto."]
  - ["cadena estilo C", "C-style string", "Arreglo de `char` terminado con el carácter nulo `'\\0'`."]
  - ["carácter nulo", "null terminator", "`'\\0'`: marca el final de una cadena de C."]
  - ["literal de cadena", "string literal", "Texto entre comillas dobles; en C++ es un arreglo de `const char`."]
  - ["longitud", "length / size", "Número de caracteres (`s.size()`, `strlen(c)`)."]
  - ["concatenar", "concatenate", "Unir cadenas: `s1 + s2`."]
  - ["subcadena", "substring", "Parte de una cadena: `s.substr(pos, n)`."]
  - ["buscar", "find", "`s.find(x)` devuelve la posición o `string::npos`."]
  - ["orden lexicográfico", "lexicographic order", "Orden de diccionario, carácter por carácter según su código."]
  - ["clasificación de caracteres", "character classification", "Funciones de `<cctype>`: `isalpha`, `isdigit`, `isspace`…"]
  - ["conversión numérica", "numeric conversion", "`stoi`, `stod` (texto → número), `to_string` (número → texto)."]
  - ["palíndromo", "palindrome", "Texto que se lee igual al derecho y al revés."]
---

# 1. Información de soporte {.soporte}

:::analogia | Un collar de cuentas con letras
Imagina un collar de cuentas, cada una con una letra: H-O-L-A. Puedes contar las cuentas, mirar la tercera, cambiar una, añadir cuentas al final o cortar un trozo. En un collar **de C** hay además una cuenta especial al final, un **tope** (`'\0'`), que indica dónde termina. Una cadena de caracteres es eso: un **arreglo de `char`** con operaciones para manipularlo.
:::

:::pregunta
Cuando una página web te dice «tu contraseña debe tener al menos 8 caracteres, una mayúscula y un número», **¿cómo crees que lo verifica el programa?** ¿Qué tendría que revisar y cómo?

{{lineas:2}}
:::

:::relevancia
Casi todo lo que hace un usuario es texto: nombres, correos, contraseñas, mensajes de chat, comandos de un juego, búsquedas. Validar un formulario, buscar una palabra en un documento, generar nombres de usuario o cifrar un mensaje son tareas de **procesamiento de cadenas**. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | Cadenas de C: arreglos de `char` con tope | Elementos aislados, Atención dividida
El *C++ Crash Course* (cap. 2) recuerda que, heredado de C, un texto puede guardarse en un arreglo de `char` que termina con el carácter nulo `'\0'`:

```cpp run title="cstring.cpp"
#include <iostream>
using namespace std;
int main()
{
    char saludo[] = "Hola";                     //> El compilador reserva 5 casillas: 4 letras + '\0'
    cout << saludo << "\n";                     //> cout muestra hasta encontrar '\0'
    cout << "Tamanio del arreglo: " << sizeof(saludo) << "\n";
    saludo[0] = 'B';                            //> Cada casilla es un char modificable
    cout << saludo << "\n";
    return 0;
}
```

```diagram arr
name: saludo
type: "char[5]"
vals: ["'B'", "'o'", "'l'", "'a'", "'\\0'"]
hl: [0]
figcaption: "Figura 1. Cuatro letras y el tope '\\0'. Sin el tope, cout seguiría leyendo memoria ajena."
```
:::

:::concepto | 2 | `std::string`: el texto «inteligente» | Elementos aislados, Atención dividida
`std::string` (biblioteca `<string>`) administra su memoria, conoce su tamaño y permite operar con `+`, `==`, `<`:

```cpp run title="string_basico.cpp"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string nombre = "Ada";
    string apellido = "Lovelace";
    string completo = nombre + " " + apellido;           //> `+` concatena
    cout << completo << " tiene " << completo.size() << " caracteres\n";  //> `.size()` (o `.length()`)
    cout << "Primera letra: " << completo[0] << ", ultima: " << completo[completo.size() - 1] << "\n";
    completo[0] = 'a';                                   //> Acceso por índice, como en un arreglo
    cout << completo << "\n";
    cout << boolalpha << (nombre == "Ada") << " " << (string("abc") < "abd") << "\n";  //> Comparan contenido
    return 0;
}
```
Las comparaciones `<` y `>` siguen el **orden de diccionario** según el código ASCII: las mayúsculas (65–90) van antes que las minúsculas (97–122).
:::

:::concepto | 3 | Leer texto: palabra o línea | Elementos aislados
Repaso del Tema 02: `cin >> s` lee **una palabra** (se detiene en el espacio); `getline(cin, s)` lee **la línea completa**. Si antes hubo un `cin >>`, usa `cin.ignore()` para descartar el Enter pendiente.

```cpp run title="lectura.cpp" stdin="25\nCalle Juarez 104\n"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    int edad;
    string direccion;
    cout << "Edad: ";
    cin >> edad;
    cin.ignore();                       //> Descarta el '\n' que dejó `cin >>`
    cout << "Direccion: ";
    getline(cin, direccion);            //> Lee con espacios
    cout << "[" << direccion << "] (" << direccion.size() << " caracteres)\n";
    return 0;
}
```
:::

:::concepto | 4 | Recorrer una cadena carácter por carácter | Elementos aislados, Atención dividida
Igual que un arreglo: índice de `0` a `size() − 1`, o el `for` de rango.

```cpp run title="recorrer.cpp"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string frase = "Murcielago";
    int vocales = 0;
    for (int i = 0; i < static_cast<int>(frase.size()); i++)   //> Recorrido con índice
    {
        char c = frase[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
            vocales++;
    }
    cout << "Vocales: " << vocales << "\n";
    for (char c : frase)                                       //> for de rango: cada carácter
        cout << c << '-';
    cout << "\n";
    return 0;
}
```
`size()` devuelve un entero **sin signo**; por eso se convierte con `static_cast<int>` al compararlo con `i` (evita avisos del compilador).
:::

:::movimiento | La cadena humana (10 min)
Cinco estudiantes forman la palabra `GATOS` con tarjetas; un sexto sostiene un letrero `'\0'` al final. El instructor pide operaciones y el grupo predice antes qué pasará: «`s[1] = 'O'`» (un estudiante cambia su tarjeta), «insertar `R` en la posición 2» (todos los de la derecha deben **recorrerse** un lugar), «borrar la posición 0» (todos se recorren a la izquierda), «¿dónde está la `T`?» (*find*). Pregunta final: ¿qué operaciones son «caras» porque obligan a mover a muchos?
:::

:::concepto | 5 | Clasificar y transformar caracteres con `<cctype>` | Elementos aislados
| Función | Devuelve verdadero si `c` es… | Función | Hace |
|---|---|---|---|
| `isalpha(c)` | letra | `toupper(c)` | mayúscula de `c` |
| `isdigit(c)` | dígito `0`–`9` | `tolower(c)` | minúscula de `c` |
| `isalnum(c)` | letra o dígito | | |
| `isspace(c)` | espacio, tabulador, salto | | |
| `isupper(c)` / `islower(c)` | mayúscula / minúscula | | |
| `ispunct(c)` | signo de puntuación | | |

```cpp run title="cctype.cpp"
#include <iostream>
#include <string>
#include <cctype>
using namespace std;
int main()
{
    string s = "Hola Mundo 2026!";
    string grito = s;
    for (char& c : grito)                 //> `char&`: referencia, para MODIFICAR cada carácter
        c = toupper(c);
    int letras = 0, digitos = 0;
    for (char c : s)
    {
        if (isalpha(c)) letras++;
        else if (isdigit(c)) digitos++;
    }
    cout << grito << " | letras: " << letras << ", digitos: " << digitos << "\n";
    return 0;
}
```
:::

:::concepto | 6 | Operaciones predefinidas de `string` | Elementos aislados, Atención dividida
```cpp run title="operaciones.cpp"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string s = "programar en C es divertido";
    cout << s.substr(0, 9) << "\n";              //> substr(pos, n): 9 caracteres desde la posición 0
    size_t p = s.find("C");                      //> find: posición de la primera aparición
    cout << "C en la posicion " << p << "\n";
    s.replace(p, 1, "C++");                      //> replace(pos, n, nuevo): cambia 1 carácter por "C++"
    s.insert(0, "Me gusta ");                    //> insert(pos, texto)
    s.erase(s.size() - 9, 9);                    //> erase(pos, n): borra "divertido"
    s += "genial";                               //> += agrega al final
    cout << s << "\n";
    if (s.find("Python") == string::npos)        //> npos = «no se encontró»
        cout << "No menciona Python\n";
    return 0;
}
```
:::

:::concepto | 7 | Ruta B · De texto a número y de número a texto | Elementos aislados, Reversión de la experiencia
```cpp run title="conversiones.cpp"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string edadTxt = "17", precioTxt = "249.90";
    int edad = stoi(edadTxt);                  //> string → int
    double precio = stod(precioTxt);           //> string → double
    cout << edad + 1 << " " << precio * 2 << "\n";
    string folio = "PED-" + to_string(1000 + edad);   //> número → string, para armar textos
    cout << folio << "\n";
    cout << "17" + string("1") << " vs " << 17 + 1 << "\n";   //> Con texto, `+` concatena; con números, suma
    return 0;
}
```
:::

:::concepto | 8 | Ruta B · Cadenas de C a mano y `<cstring>` | Elementos aislados, Reversión de la experiencia
Con arreglos de `char` no existen `+` ni `==`: se usan funciones de `<cstring>` (`strlen`, `strcpy`, `strcmp`, `strcat`) o se programan recorriendo hasta `'\0'`:

```cpp run title="cstring_mano.cpp"
#include <iostream>
#include <cstring>
using namespace std;
int longitud(const char s[])
{
    int n = 0;
    while (s[n] != '\0') n++;          //> Cuenta hasta encontrar el tope
    return n;
}
int main()
{
    char a[20] = "gato", b[20];
    strcpy(b, a);                      //> Copia a en b (b debe tener espacio suficiente)
    cout << longitud(a) << " " << strlen(b) << " " << strcmp(a, b) << "\n";  //> strcmp: 0 si son iguales
    cout << (a == b ? "== compara direcciones" : "a == b es falso aunque el texto sea igual") << "\n";
    return 0;
}
```
Por eso en C++ moderno se prefiere `std::string`: evita desbordamientos y compara contenido con `==`.
:::

## 1.2 Ejemplo resuelto: analizador de frases

:::ejemplo | Contar vocales, consonantes, dígitos, espacios y palabras | Ejemplo resuelto, Atención dividida
**Problema.** Leer una frase y mostrar cuántas vocales, consonantes, dígitos y espacios tiene, cuántas palabras, y la frase en mayúsculas.

**A. Algoritmo:** 1) Leer la frase completa. 2) Recorrerla carácter por carácter: si es letra, decidir si es vocal o consonante; si es dígito, contarlo; si es espacio, contarlo. 3) Contar palabras: una palabra empieza cuando hay una letra o dígito y el carácter anterior era espacio (o es el inicio). 4) Mostrar los conteos y la frase en mayúsculas.

**B. Pseudocódigo**

```pseudo
Algoritmo Analizador
    Leer frase
    Para i <- 0 Hasta Longitud(frase) - 1 Hacer
        c <- Minusculas(Subcadena(frase, i, i))
        Si c es letra Entonces
            Si c es vocal Entonces vocales <- vocales + 1 SiNo consonantes <- consonantes + 1 FinSi
        SiNo
            Si c es digito Entonces digitos <- digitos + 1 FinSi
            Si c = " " Entonces espacios <- espacios + 1 FinSi
        FinSi
    FinPara
    Escribir vocales, consonantes, digitos, espacios
FinAlgoritmo
```

**C. Código en C++**

```cpp run title="analizador.cpp" stdin="En 2026 programo  en C++ con 3 amigos\n"
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

bool esVocal(char c)                                   //> Función auxiliar: una tarea, un nombre
{
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main()
{
    string frase;
    getline(cin, frase);                               //> 1) La frase tiene espacios
    int vocales = 0, consonantes = 0, digitos = 0, espacios = 0, palabras = 0;
    for (int i = 0; i < static_cast<int>(frase.size()); i++)   //> 2) Recorrido
    {
        char c = frase[i];
        if (isalpha(c))
        {
            if (esVocal(c)) vocales++;
            else consonantes++;
        }
        else if (isdigit(c)) digitos++;
        else if (c == ' ') espacios++;
        bool inicioPalabra = !isspace(c) && (i == 0 || isspace(frase[i - 1]));  //> 3) Empieza palabra
        if (inicioPalabra) palabras++;
    }
    string mayus = frase;
    for (char& c : mayus) c = toupper(c);              //> 4) Transformación
    cout << "Vocales " << vocales << ", consonantes " << consonantes << ", digitos " << digitos
         << ", espacios " << espacios << ", palabras " << palabras << "\n" << mayus << "\n";
    return 0;
}
```

**D. Verificación.** La frase tiene **dos** espacios seguidos entre «programo» y «en»: hay 8 espacios y 8 palabras. Si contáramos «espacios + 1» obtendríamos 9 palabras (incorrecto); por eso una palabra se cuenta solo donde **empieza**: un carácter que no es espacio precedido por un espacio (o al inicio).
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.16; ranksep=0.3;
@term(t, "Cadena")
@proc(c, "estilo C: char[] + '\\0'\n<cstring>: strlen strcpy strcmp")
@proc(s, "std::string\nsize · [i] · + · == · <")
@io(l, "cin >> (palabra)\ngetline (línea)")
@proc(r, "recorrido carácter\npor carácter")
@sub(cc, "<cctype>: isalpha isdigit\ntoupper tolower")
@sub(op, "substr · find · insert\nerase · replace · npos")
@hl(cv, "stoi · stod · to_string")
t -> c; t -> s; s -> l; s -> r; r -> cc; s -> op; s -> cv [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1 · `std::string`
| Quiero… | Código | Ejemplo con `s = "Hola mundo"` |
|---|---|---|
| Longitud | `s.size()` | `10` |
| Carácter en `i` | `s[i]` · `s.at(i)` (verifica rango) | `s[0]` → `'H'` |
| Último carácter | `s[s.size() - 1]` o `s.back()` | `'o'` |
| Unir | `s + "!"` · `s += "!"` | `"Hola mundo!"` |
| Subcadena | `s.substr(pos, n)` | `s.substr(5, 5)` → `"mundo"` |
| Buscar | `s.find("mu")` | `5` (o `string::npos`) |
| Insertar | `s.insert(pos, txt)` | `s.insert(4, ",")` → `"Hola, mundo"` |
| Borrar | `s.erase(pos, n)` | `s.erase(0, 5)` → `"mundo"` |
| Reemplazar | `s.replace(pos, n, txt)` | `s.replace(0, 4, "Adios")` |
| Comparar | `==`, `!=`, `<`, `>` | `"ana" < "beto"` → `true` |
| Vacía | `s.empty()` · `s = ""` | |
| Texto → número | `stoi(s)`, `stod(s)` | `stoi("42")` → `42` |
| Número → texto | `to_string(x)` | `to_string(7)` → `"7"` |
| A mayúsculas | `for (char& c : s) c = toupper(c);` | `"HOLA MUNDO"` |

Bibliotecas: `<string>`, `<cctype>` (clasificar caracteres), `<cstring>` (cadenas de C).
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿El texto puede tener espacios? Entonces <code>getline</code> (y <code>cin.ignore()</code> si antes hubo <code>cin &gt;&gt;</code>).</li>
<li>¿Mis índices van de <code>0</code> a <code>size() − 1</code>? ¿Uso <code>s[i + 1]</code> sin salirme?</li>
<li>¿Considero mayúsculas y minúsculas? (Normaliza con <code>tolower</code> antes de comparar.)</li>
<li>¿Comparo el resultado de <code>find</code> con <code>string::npos</code> antes de usarlo?</li>
<li>¿Distingo <code>'a'</code> (un <code>char</code>) de <code>"a"</code> (una cadena)?</li>
<li>Con cadenas de C: ¿hay espacio para el <code>'\0'</code>? ¿Uso <code>strcmp</code> en lugar de <code>==</code>?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Comparar un `char` con una cadena.** `"a"` es un texto, no un carácter:

```cpp err
#include <string>
int main()
{
    std::string s = "casa";
    if (s[0] == "c")
        return 1;
    return 0;
}
```
*Corrección:* `s[0] == 'c'` (comillas simples).

**b) Usar `find` sin verificar `npos`.** Si no se encuentra, `find` devuelve un número enorme y `substr` falla en ejecución. Verifica: `if (p != string::npos) …`.

**c) Comparar cadenas de C con `==`.** Compara **direcciones**, no contenido (concepto 8): usa `strcmp(a, b) == 0` o `std::string`.

**d) Olvidar el `'\0'` al construir una cadena de C a mano.** `char c[4] = {'H', 'o', 'l', 'a'};` no tiene tope: `cout << c` sigue leyendo memoria. Debe ser `char c[5] = "Hola";`.

**e) `getline` después de `cin >>` sin `cin.ignore()`:** devuelve una línea vacía (Tema 02).
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Censurar palabras | Variabilidad
Mismo patrón (buscar y reemplazar en ciclo), otro contexto: un chat que censura una palabra.

```cpp run title="censura.cpp"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string msg = "eres un tonto, muy tonto";
    string mala = "tonto";
    size_t p = msg.find(mala);
    while (p != string::npos)                          //> Mientras siga apareciendo…
    {
        msg.replace(p, mala.size(), string(mala.size(), '*'));   //> …reemplaza por asteriscos
        p = msg.find(mala, p + 1);                     //> Busca la siguiente, después de la actual
    }
    cout << msg << "\n";
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Cuando dudes, escribe el texto en casillas con sus índices.

:::tarea A | T1. Iniciales de un nombre: ejemplo y gemelo | 20 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia:**

```cpp run title="iniciales.cpp" stdin="ana sofia lopez\n"
#include <iostream>
#include <string>
#include <cctype>
using namespace std;
int main()
{
    string nombre, ini;
    getline(cin, nombre);
    for (int i = 0; i < static_cast<int>(nombre.size()); i++)
    {
        if (nombre[i] != ' ' && (i == 0 || nombre[i - 1] == ' '))   //> Inicio de palabra
        {
            ini += static_cast<char>(toupper(nombre[i]));          //> Agrega la letra en mayúscula
            ini += '.';
        }
    }
    cout << "Iniciales: " << ini << "\n";
    return 0;
}
```

**Paso 2 · Gemelo.** Genera un **nombre de usuario**: primera letra del nombre + primer apellido completo, todo en minúsculas, + los dos últimos dígitos de un año que se lee después. Ejemplo: `Luis Perez Gil` y `2026` → `lperez26`.

:::solucion | T1
```cpp run title="usuario.cpp" stdin="Luis Perez Gil\n2026\n"
#include <iostream>
#include <string>
#include <cctype>
using namespace std;
int main()
{
    string nombre;
    int anio;
    getline(cin, nombre);
    cin >> anio;
    size_t esp1 = nombre.find(' ');
    size_t esp2 = nombre.find(' ', esp1 + 1);
    string apellido = nombre.substr(esp1 + 1, esp2 - esp1 - 1);
    string usuario = string(1, nombre[0]) + apellido + to_string(anio % 100);
    for (char& c : usuario) c = tolower(c);
    cout << usuario << "\n";
    return 0;
}
```
:::
:::

:::tarea A | T2. ¿Es palíndromo? (completa con pistas) | 25 min | Problema por completar
**Contexto.** «Anita lava la tina» se lee igual al revés si se ignoran espacios y mayúsculas. Primero se **limpia** la frase (solo letras, en minúsculas) y luego se compara cada extremo.

```cpp blank title="palindromo.cpp"
#include <iostream>
#include <string>
#include <cctype>
using namespace std;
int main()
{
    string frase, limpia;
    getline(cin, frase);
    for (char c : frase)
        if (__1__)                                   // 1: solo letras
            limpia += static_cast<char>(__2__);      // 2: en minuscula
    bool es = true;
    int n = limpia.size();
    for (int i = 0; i < __3__; i++)                  // 3: basta revisar la mitad
        if (limpia[i] != limpia[__4__])              // 4: el caracter "espejo" de i
        {
            es = false;
            __5__;                                   // 5: ya no hace falta seguir
        }
    cout << (es ? "Es palindromo\n" : "No es palindromo\n");
    return 0;
}
```

:::solucion | T2
{{c:1}} `isalpha(c)` · {{c:2}} `tolower(c)` · {{c:3}} `n / 2` · {{c:4}} `n - 1 - i` · {{c:5}} `break`

```cpp run title="palindromo.cpp" runs="Anita lava la tina|Programar es divertido"
#include <iostream>
#include <string>
#include <cctype>
using namespace std;
int main()
{
    string frase, limpia;
    getline(cin, frase);
    for (char c : frase)
        if (isalpha(c))
            limpia += static_cast<char>(tolower(c));
    bool es = true;
    int n = limpia.size();
    for (int i = 0; i < n / 2; i++)
        if (limpia[i] != limpia[n - 1 - i])
        {
            es = false;
            break;
        }
    cout << (es ? "Es palindromo\n" : "No es palindromo\n");
    return 0;
}
```
:::
:::

:::tarea AB | T3. ¿Contraseña segura? (completa sin pistas) | 25 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Una contraseña es segura si tiene al menos 8 caracteres, una mayúscula, una minúscula, un dígito y un símbolo (cualquier carácter que no sea letra ni dígito). El programa muestra qué requisitos faltan.

```cpp blank title="password.cpp"
#include <iostream>
#include <string>
#include <cctype>
using namespace std;
bool segura(const string& p, string& faltan)
{
    bool may = false, min = false, dig = false, sim = false;
    for (char c : p)
    {
        if (__1__) may = true;
        else if (__2__) min = true;
        else if (__3__) dig = true;
        else __4__;
    }
    faltan = "";
    if (__5__) faltan += " longitud";
    if (!may) faltan += " mayuscula";
    if (!min) faltan += " minuscula";
    if (!dig) faltan += " digito";
    if (!sim) faltan += " simbolo";
    return __6__;
}
int main()
{
    string p, faltan;
    cin >> p;
    if (segura(p, faltan)) cout << "Segura\n";
    else cout << "Insegura, falta:" << faltan << "\n";
    return 0;
}
```

:::solucion | T3
{{c:1}} `isupper(c)` · {{c:2}} `islower(c)` · {{c:3}} `isdigit(c)` · {{c:4}} `sim = true` · {{c:5}} `p.size() < 8` · {{c:6}} `faltan.empty()`

```cpp run title="password.cpp" runs="hola123|Gato#2026|ABCdefgh"
#include <iostream>
#include <string>
#include <cctype>
using namespace std;
bool segura(const string& p, string& faltan)
{
    bool may = false, min = false, dig = false, sim = false;
    for (char c : p)
    {
        if (isupper(c)) may = true;
        else if (islower(c)) min = true;
        else if (isdigit(c)) dig = true;
        else sim = true;
    }
    faltan = "";
    if (p.size() < 8) faltan += " longitud";
    if (!may) faltan += " mayuscula";
    if (!min) faltan += " minuscula";
    if (!dig) faltan += " digito";
    if (!sim) faltan += " simbolo";
    return faltan.empty();
}
int main()
{
    string p, faltan;
    cin >> p;
    if (segura(p, faltan)) cout << "Segura\n";
    else cout << "Insegura, falta:" << faltan << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T4. Cifrado César (problema convencional) | 35 min | Variabilidad
**Contexto.** Julio César cifraba sus mensajes desplazando cada letra `k` posiciones en el alfabeto (con `k = 3`: A→D, B→E, …, X→A, Y→B, Z→C). Escribe `string cifrar(string msg, int k)` que respete mayúsculas y minúsculas, deje igual lo que no sea letra y dé la vuelta al llegar a la Z. Descifra usando la misma función con `26 − k`. Prueba con «Ataque al amanecer, 7am».

:::solucion | T4
```cpp run title="cesar.cpp"
#include <iostream>
#include <string>
#include <cctype>
using namespace std;
string cifrar(string msg, int k)
{
    for (char& c : msg)
    {
        if (isupper(c)) c = static_cast<char>('A' + (c - 'A' + k) % 26);
        else if (islower(c)) c = static_cast<char>('a' + (c - 'a' + k) % 26);
    }
    return msg;
}
int main()
{
    string original = "Ataque al amanecer, 7am";
    string secreto = cifrar(original, 3);
    cout << secreto << "\n" << cifrar(secreto, 26 - 3) << "\n";
    return 0;
}
```
`c - 'A'` convierte la letra en su posición (0–25); `% 26` da la vuelta; `'A' + …` la convierte de nuevo en letra.
:::
:::

:::tarea A | T5. Todo sobre una frase (solución libre) | 25 min | Solución libre
**Contexto.** Dada la frase `"Programar en C++ es divertido desde 2026"`, **descubre y muestra todo lo que puedas**: longitud, número de palabras, la palabra más larga, la frase al revés, cuántas veces aparece cada vocal, si contiene «C++», la frase sin espacios, en formato «Título» (cada palabra con mayúscula inicial)… No hay lista obligatoria.

:::solucion | T5
Una exploración posible:

```cpp run title="explora_frase.cpp"
#include <iostream>
#include <string>
#include <cctype>
using namespace std;
int main()
{
    string f = "Programar en C++ es divertido desde 2026";
    string reves(f.rbegin(), f.rend()), sinEsp, titulo = f, palabra, larga;
    int cuenta[5] = {}, palabras = 0;
    string voc = "aeiou";
    for (int i = 0; i < static_cast<int>(f.size()); i++)
    {
        char c = f[i];
        if (c != ' ') sinEsp += c;
        size_t v = voc.find(static_cast<char>(tolower(c)));
        if (v != string::npos) cuenta[v]++;
        if (c != ' ' && (i == 0 || f[i - 1] == ' ')) { palabras++; titulo[i] = static_cast<char>(toupper(c)); }
        if (c != ' ') palabra += c;
        if (c == ' ' || i == static_cast<int>(f.size()) - 1)
        {
            if (palabra.size() > larga.size()) larga = palabra;
            palabra = "";
        }
    }
    cout << "Longitud " << f.size() << ", palabras " << palabras << ", mas larga: " << larga << "\n";
    cout << "Al reves: " << reves << "\nSin espacios: " << sinEsp << "\nTitulo: " << titulo << "\n";
    for (int k = 0; k < 5; k++) cout << voc[k] << "=" << cuenta[k] << " ";
    cout << "\nContiene C++: " << (f.find("C++") != string::npos ? "si" : "no") << "\n";
    return 0;
}
```
:::
:::

:::tarea B | T6. Comparar cadenas sin `strcmp` (autoexplicación, tesis §6.1.6) | 25 min | Autoexplicación, Reversión de la experiencia
**Contexto.** «La maestra dejó un ejercicio del tema de cadenas visto en la clase: realizar un programa que, dadas dos cadenas de caracteres, las compare y diga si son **iguales o diferentes** (sin utilizar las funciones `strcmp`, `strcpy` y `strlen`). Uno de tus compañeros ya programó su solución, pero no funciona adecuadamente. **¿Puedes identificar cuál es el error (o errores), explicar por qué no funciona, y proponer una solución con su explicación?**»

```cpp run title="compara_bug.cpp"
#include <iostream>
using namespace std;
int main()
{
    char a[30] = "programa", b[30] = "programas";
    bool iguales = true;
    int i = 0;
    while (a[i] != '\0')
    {
        if (a[i] != b[i])
            iguales = false;
        i++;
    }
    if (a == b) iguales = true;
    cout << (iguales ? "Iguales\n" : "Diferentes\n");
    return 0;
}
```

{{lineas:5}}

:::solucion | T6
**Errores:** (1) el ciclo solo recorre `a`: si `b` es más larga pero empieza igual («programa» / «programas»), nunca detecta la diferencia; hay que verificar que **ambas** terminen al mismo tiempo. (2) `a == b` compara **direcciones** de los arreglos, no su contenido; aquí es falso y no afecta, pero es un error conceptual (y si fuera verdadero, ocultaría diferencias). (3) No se detiene en la primera diferencia (no es un error, pero hace trabajo de más).

```cpp run title="compara.cpp"
#include <iostream>
using namespace std;
bool sonIguales(const char a[], const char b[])
{
    int i = 0;
    while (a[i] != '\0' && b[i] != '\0')
    {
        if (a[i] != b[i]) return false;   // primera diferencia: ya sabemos
        i++;
    }
    return a[i] == b[i];                 // iguales solo si AMBAS terminaron
}
int main()
{
    char a[30] = "programa", b[30] = "programas", c[30] = "programa";
    cout << (sonIguales(a, b) ? "Iguales" : "Diferentes") << " / "
         << (sonIguales(a, c) ? "Iguales" : "Diferentes") << "\n";
    return 0;
}
```
:::
:::

:::tarea B | T7. ¿Cómo queda la cadena? (imaginación) | 20 min | Imaginación
**Sin ejecutar**, imagina el contenido de `s` después de **cada** línea (dibuja las casillas) y la salida final. Después compruébalo.

```cpp check title="imagina_string.cpp"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string s = "MESA";
    s.insert(2, "TE");
    s.erase(0, 1);
    s.replace(s.find("T"), 2, "ND");
    s += s.substr(0, 2);
    cout << s << " " << s.size() << "\n";
    return 0;
}
```

{{lineas:4}}

:::solucion | T7
`"MESA"` → `insert(2, "TE")` → `"METESA"` → `erase(0, 1)` → `"ETESA"` → `find("T")` = 1, `replace(1, 2, "ND")` → `"ENDSA"` → `+= "EN"` → `"ENDSAEN"`, tamaño 7.

```cpp run title="imagina_string.cpp"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string s = "MESA";
    s.insert(2, "TE");
    s.erase(0, 1);
    s.replace(s.find("T"), 2, "ND");
    s += s.substr(0, 2);
    cout << s << " " << s.size() << "\n";
    return 0;
}
```
:::
:::

:::tarea AB | T8. El ahorcado (reto colaborativo) | 45 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Equipos de 4, niveles mezclados. Palabra secreta fija (por ejemplo, `"compilador"`), 6 vidas.
- **Integrante 1:** `string mascara(const string& secreta, const string& usadas)` → `c o _ _ _ _ _ _ o _`.
- **Integrante 2:** procesar un intento: validar que sea letra, que no se haya usado antes, y si no está en la palabra, restar una vida.
- **Integrante 3:** detectar victoria (no quedan `_`) y derrota (vidas = 0).
- **Integrante 4:** el ciclo del juego y los mensajes; probar con una partida ganada y una perdida.
:::

:::solucion | T8
Partida simulada (entrada: `o a c x i l z m p r d`):

```cpp run title="ahorcado.cpp" stdin="o\na\nc\nx\ni\nl\nz\nm\np\nr\nd\n"
#include <iostream>
#include <string>
#include <cctype>
using namespace std;
string mascara(const string& secreta, const string& usadas)
{
    string m;
    for (char c : secreta)
    {
        m += (usadas.find(c) != string::npos) ? c : '_';
        m += ' ';
    }
    return m;
}
int main()
{
    const string secreta = "compilador";
    string usadas;
    int vidas = 6;
    while (vidas > 0)
    {
        string m = mascara(secreta, usadas);
        if (m.find('_') == string::npos) { cout << m << "\nGanaste!\n"; return 0; }
        cout << m << " (vidas: " << vidas << ") letra: ";
        char c;
        cin >> c;
        c = static_cast<char>(tolower(c));
        if (!isalpha(c) || usadas.find(c) != string::npos) { cout << "No valida o repetida\n"; continue; }
        usadas += c;
        if (secreta.find(c) == string::npos) vidas--;
    }
    cout << "\nPerdiste. Era: " << secreta << "\n";
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Contar palabras aunque haya espacios de más | Modalidad, Ejemplo resuelto
*Guion segmentado (≈ 3 min), con la frase en casillas en pantalla.*

**Problema:** «Contar las palabras de una frase escrita por el usuario, que puede tener espacios al inicio, al final o varios seguidos».

**Segmento 1 — La idea ingenua y su falla.** {{como}} Mi primera idea es contar espacios y sumar 1. La pruebo mentalmente con `"  hola   mundo "`: hay 6 espacios y solo 2 palabras. {{porque}} Probar la idea con un caso «feo» antes de programarla me ahorra escribir algo que no sirve.

**Segmento 2 — Cambiar la pregunta.** {{como}} En lugar de contar espacios, cuento **inicios de palabra**: un carácter que no es espacio y cuyo anterior sí lo es (o que está en la posición 0). {{porque}} Cada palabra tiene exactamente un inicio, sin importar cuántos espacios haya alrededor.

**Segmento 3 — Cuidar el borde izquierdo.** {{como}} Escribo la condición `i == 0 || isspace(f[i - 1])` con el `i == 0` **primero**. {{porque}} Por el cortocircuito de `||`, si `i` es 0 nunca se evalúa `f[-1]`, que estaría fuera de la cadena.

**Segmento 4 — Probar los casos extremos.** {{como}} Pruebo la frase normal, la de espacios de más, una frase vacía y una de una sola palabra. {{porque}} Los errores en cadenas casi siempre están en los extremos: inicio, final y texto vacío.

```cpp run title="contar_palabras.cpp" runs="Hola mundo cruel|   hola    mundo  |unica"
#include <iostream>
#include <string>
#include <cctype>
using namespace std;
int contarPalabras(const string& f)
{
    int n = 0;
    for (int i = 0; i < static_cast<int>(f.size()); i++)
        if (!isspace(f[i]) && (i == 0 || isspace(f[i - 1])))
            n++;
    return n;
}
int main()
{
    string f;
    getline(cin, f);
    cout << contarPalabras(f) << " palabras\n";
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. ¿Qué carácter marca el final de una cadena de C?
2. ¿Cuántas casillas ocupa `char x[] = "Sol";`?
3. ¿Qué diferencia hay entre `cin >> s` y `getline(cin, s)`?
4. ¿Qué devuelve `s.find("x")` cuando no encuentra el texto?
5. Escribe la instrucción que obtiene los 3 primeros caracteres de `s`.
6. ¿Qué hace `toupper('m')`?
7. Verdadero o falso: con cadenas de C, `a == b` compara el texto.
8. ¿Qué función convierte `"42"` en el entero 42?
9. ¿Por qué `"Zorro" < "abeja"` es verdadero?
10. ¿Para qué sirve el `char&` en `for (char& c : s) c = toupper(c);`?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida:**

```cpp check title="p1.cpp"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string s = "computadora";
    cout << s.size() << " " << s[3] << " " << s.substr(4, 3) << " ";
    cout << s.find('o') << " " << s.find("dora") << "\n";
    return 0;
}
```

**P2.** Escribe una función `string invertir(const string& s)` sin usar funciones de biblioteca.

**P3. Corrige:** `string s; cin >> s; for (int i = 0; i <= s.size(); i++) if (s[i] == "a") s[i] = 'A';`

**P4. Escribe un programa** que lea un correo electrónico y valide que tenga exactamente una `@`, al menos un carácter antes de ella y un punto después de ella; si es válido, muestra el usuario (antes de la `@`) y el dominio (después).
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Distingo cadenas de C y <code>std::string</code>, y sé por qué existe el <code>'\0'</code>.</li>
<li>Recorro cadenas y clasifico caracteres con <code>&lt;cctype&gt;</code>.</li>
<li>Uso <code>substr</code>, <code>find</code>, <code>insert</code>, <code>erase</code> y <code>replace</code>.</li>
<li>Pruebo mis programas con textos vacíos, con espacios de más y con mayúsculas.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 `'\0'` · 2 4 (3 letras + `'\0'`) · 3 `cin >>` lee hasta el primer espacio; `getline` lee la línea completa · 4 `string::npos` · 5 `s.substr(0, 3)` · 6 Devuelve `'M'` · 7 Falso: compara direcciones · 8 `stoi` · 9 Porque se compara por código ASCII y `'Z'` (90) es menor que `'a'` (97) · 10 Para modificar cada carácter de la cadena original (sin `&` se modificaría una copia).
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.**

```cpp run title="p1.cpp"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string s = "computadora";
    cout << s.size() << " " << s[3] << " " << s.substr(4, 3) << " ";
    cout << s.find('o') << " " << s.find("dora") << "\n";
    return 0;
}
```

**P2.** `string invertir(const string& s) { string r; for (int i = s.size() - 1; i >= 0; i--) r += s[i]; return r; }`

**P3.** `i < s.size()` (no `<=`) y `'a'` con comillas simples: `for (int i = 0; i < (int)s.size(); i++) if (s[i] == 'a') s[i] = 'A';`

**P4.**

```cpp run title="correo.cpp" runs="ana.lopez@escuela.edu.mx|sin_arroba.com|@dominio.com"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string c;
    cin >> c;
    size_t a = c.find('@');
    bool valido = a != string::npos && a > 0 && c.find('@', a + 1) == string::npos
                  && c.find('.', a + 1) != string::npos;
    if (valido)
        cout << "Usuario: " << c.substr(0, a) << "  Dominio: " << c.substr(a + 1) << "\n";
    else
        cout << "Correo invalido\n";
    return 0;
}
```
:::
