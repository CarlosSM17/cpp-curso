---
num: "12"
archivo: "Tema12_Cadenas_de_caracteres"
titulo: "Cadenas de caracteres: arreglos de char y <string.h>"
corto: "Cadenas"
lema: "Un texto es un arreglo de caracteres con un tope al final: se recorre, se compara, se busca y se transforma letra por letra."
duracion: "5 h · 3 sesiones"
previos: "Tema 02 (`char`, ASCII, `%s`, `%[^\\n]`), Tema 08 (arreglos) y Tema 10 (funciones y arreglos como parámetro)."
fuentes:
  - "Kernighan, B. W. y Ritchie, D. M. (1988). *The C Programming Language* (2.ª ed.). Prentice Hall. Cap. 1: §1.9 Character Arrays. Cap. 5: §5.5 Character Pointers and Functions. Apéndice B: §B2 «Character Class Tests: <ctype.h>», §B3 «String Functions: <string.h>»."
  - "King, K. N. (2008). *C Programming: A Modern Approach* (2.ª ed.). W. W. Norton. Cap. 13 «Strings»: §13.1–§13.6. Cap. 23 (encabezados `<ctype.h>` y `<string.h>`)."
  - "Seacord, R. C. (2020). *Effective C*. No Starch Press. Cap. 7 «Characters and Strings»."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §6.1.6: autoexplicación con ejemplos con errores (comparar cadenas sin `strcmp`, `strcpy` ni `strlen`)."
objetivos:
  A:
    - "Explicar cómo se guarda una cadena en C (arreglo de `char` terminado en `'\\0'`) y reservar espacio suficiente."
    - "Leer cadenas (`scanf(\"%s\")`, `fgets`) y acceder a cada carácter por su índice."
    - "Recorrer cadenas para contar y clasificar caracteres con `<ctype.h>` (`isalpha`, `isdigit`, `toupper`…)."
    - "Usar las funciones de `<string.h>`: `strlen`, `strcpy`, `strcat`, `strcmp`, `strchr`, `strstr`."
  B:
    - "Implementar a mano longitud, copia y comparación de cadenas."
    - "Convertir entre texto y números (`atoi`, `atof`, `strtol`, `snprintf`)."
    - "Prevenir desbordamientos de búfer (tamaño del arreglo, `snprintf`, `strncat`)."
    - "Resolver problemas de palabras: invertir, palíndromos, contar palabras, cifrar."
efectos:
  soporte:
    - ["Elementos aislados", "char[] y '\\0' → <string.h> → lectura → recorrido → <ctype.h> → búsqueda → conversiones → funciones a mano."]
    - ["Atención dividida", "Casillas del texto (con índices y '\\0') junto a cada operación."]
    - ["Ejemplo resuelto", "Analizador de frases: vocales, consonantes, dígitos, espacios y palabras."]
    - ["Movimiento humano", "«Cadena humana»: cada estudiante es una letra; mover el tope cambia dónde termina el texto."]
  procedimental:
    - ["Variabilidad", "Mismas operaciones aplicadas a nombres, contraseñas, frases y mensajes cifrados."]
    - ["Autoexplicación", "Errores con cadenas presentados como casos para explicar."]
  tareas:
    - ["Ejemplo resuelto", "T1: iniciales de un nombre + gemelo (nombre de usuario)."]
    - ["Problema por completar", "T2 (palíndromo, con pistas) y T3 (contraseña segura, sin pistas)."]
    - ["Desvanecimiento de guía", "T1 → T4."]
    - ["Solución libre", "T5: descubrir todo lo posible sobre una frase."]
    - ["Autoexplicación", "T6: comparar cadenas sin funciones de biblioteca (ejemplo con errores de la tesis §6.1.6)."]
    - ["Imaginación", "T7: imaginar el contenido de dos cadenas (y su `'\\0'`) tras varias operaciones."]
    - ["Memoria colectiva de trabajo", "T8: el juego del ahorcado por equipos."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Arreglos de `char`, `'\\0'`, recorrido, `<ctype.h>`, `strlen`/`strcpy`/`strcat`/`strcmp`."
    B: "Búsqueda con `strchr`/`strstr` (punteros), conversiones numéricas, desbordamiento de búfer."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4, dibujando las casillas del texto en papel (con su `'\\0'`)."
    B: "T5, T6, T7 autónomas; T8 como integradores."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Cifrado César (T4)."
    B: "Comparador de cadenas propio con explicación (T6)."
  Entorno:
    comp: "Información procedimental"
    A: "Tabla ASCII impresa a la mano."
    B: "Manual de la biblioteca de C (`man 3 strcpy` o cppreference, sección C) y `-fsanitize=address` para detectar desbordamientos."
plan:
  - ["Sesión 1", "Soporte + tareas", "Cadena humana; conceptos 1–5; ejemplo resuelto; T1, T2.", "100 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–8; T3, T4; Ruta B: T6, T7.", "100 min"]
  - ["Sesión 3", "Tareas + evaluación", "T5, T8 ahorcado; protocolo verbal; tests.", "100 min"]
glosario:
  - ["cadena de caracteres", "string", "Secuencia de caracteres que representa un texto; en C, un arreglo de `char` terminado en `'\\0'`."]
  - ["carácter nulo", "null terminator", "`'\\0'`: marca el final de una cadena."]
  - ["literal de cadena", "string literal", "Texto entre comillas dobles; en C es un arreglo de `char` que no debe modificarse."]
  - ["longitud", "length", "Número de caracteres antes del `'\\0'`: `strlen(s)`."]
  - ["concatenar", "concatenate", "Unir cadenas: `strcat(destino, origen)`."]
  - ["subcadena", "substring", "Parte de una cadena; en C se copia con `strncpy` o un ciclo y se cierra con `'\\0'`."]
  - ["buscar", "search", "`strchr` (un carácter) y `strstr` (un texto) devuelven un puntero a la posición o `NULL`."]
  - ["orden lexicográfico", "lexicographic order", "Orden de diccionario, carácter por carácter según su código; lo calcula `strcmp`."]
  - ["clasificación de caracteres", "character classification", "Funciones de `<ctype.h>`: `isalpha`, `isdigit`, `isspace`…"]
  - ["conversión numérica", "numeric conversion", "`atoi`, `atof`, `strtol` (texto → número); `snprintf` (número → texto)."]
  - ["desbordamiento de búfer", "buffer overflow", "Escribir más caracteres de los que caben en el arreglo; daña otras variables."]
  - ["palíndromo", "palindrome", "Texto que se lee igual al derecho y al revés."]
---

# 1. Información de soporte {.soporte}

:::analogia | Un collar de cuentas con letras y un tope
Imagina un collar de cuentas, cada una con una letra: H-O-L-A. Puedes contar las cuentas, mirar la tercera, cambiar una o agregar cuentas al final. En un collar **de C** hay además una cuenta especial, un **tope** (`'\0'`), que indica dónde termina el texto: lo que haya después del tope no cuenta. Una cadena de caracteres es eso: un **arreglo de `char`** con su tope, y un juego de funciones para manipularlo.
:::

:::pregunta
Cuando una página web te dice «tu contraseña debe tener al menos 8 caracteres, una mayúscula y un número», **¿cómo crees que lo verifica el programa?** ¿Qué tendría que revisar y cómo?

{{lineas:2}}
:::

:::relevancia
Casi todo lo que hace un usuario es texto: nombres, correos, contraseñas, mensajes de chat, comandos de un juego, búsquedas. Validar un formulario, buscar una palabra en un documento, generar nombres de usuario o cifrar un mensaje son tareas de **procesamiento de cadenas**. En C, además, manejar bien el tamaño de cada cadena es una cuestión de **seguridad**: muchos ataques informáticos históricos aprovecharon cadenas que se desbordaban. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | Cadenas de C: arreglos de `char` con tope | Elementos aislados, Atención dividida
En C no existe un tipo «texto»: un texto se guarda en un arreglo de `char` que termina con el carácter nulo `'\0'`.

```c run title="cadena.c"
#include <stdio.h>
int main(void)
{
    char saludo[] = "Hola";                         //> El compilador reserva 5 casillas: 4 letras + '\0'
    printf("%s\n", saludo);                         //> `%s` muestra hasta encontrar '\0'
    printf("Tamanio del arreglo: %zu\n", sizeof(saludo));
    saludo[0] = 'B';                                //> Cada casilla es un char modificable
    printf("%s\n", saludo);
    return 0;
}
```

```diagram arr
name: saludo
type: "char[5]"
vals: ["'B'", "'o'", "'l'", "'a'", "'\\0'"]
hl: [0]
figcaption: "Figura 1. Cuatro letras y el tope '\\0'. Sin el tope, printf seguiría leyendo memoria ajena."
```
:::

:::concepto | 2 | Las funciones básicas de `<string.h>` | Elementos aislados, Atención dividida
Con arreglos de `char` **no** se puede usar `=` para copiar, `+` para unir ni `==` para comparar. Para eso existe la cabecera `<string.h>`:

```c run title="string_basico.c"
#include <stdio.h>
#include <string.h>
int main(void)
{
    char nombre[30] = "Ada";
    char completo[60];
    strcpy(completo, nombre);                       //> Copia: completo ← "Ada" (el destino va primero)
    strcat(completo, " Lovelace");                  //> Concatena: agrega al final de completo
    printf("%s tiene %zu caracteres\n", completo, strlen(completo));   //> strlen: letras antes del '\0'
    printf("Primera: %c, ultima: %c\n", completo[0], completo[strlen(completo) - 1]);
    completo[0] = 'a';                              //> Acceso por índice, como en cualquier arreglo
    printf("%s\n", completo);
    printf("%d %d\n", strcmp(nombre, "Ada"), strcmp("abc", "abd") < 0);  //> strcmp: 0 = iguales; negativo = va antes
    return 0;
}
```
`strcmp(a, b)` compara en **orden de diccionario** según el código ASCII: devuelve 0 si son iguales, un número negativo si `a` va antes y uno positivo si va después. Las mayúsculas (65–90) van antes que las minúsculas (97–122). **Responsabilidad tuya:** el destino de `strcpy` y `strcat` debe tener espacio para todo el texto **más** el `'\0'`.
:::

:::concepto | 3 | Leer texto: palabra o línea | Elementos aislados
`scanf("%29s", s)` lee **una palabra** (se detiene en el espacio). Para leer **la línea completa** está `fgets(s, tamaño, stdin)`, que respeta el tamaño del arreglo pero **guarda también el Enter** (`'\n'`) al final: se quita con `strcspn`.

```c run title="lectura.c" stdin="25\nCalle Juarez 104\n"
#include <stdio.h>
#include <string.h>
int main(void)
{
    int edad;
    char direccion[50];
    printf("Edad: ");
    scanf("%d", &edad);
    getchar();                                      //> Descarta el '\n' que dejó scanf
    printf("Direccion: ");
    fgets(direccion, sizeof direccion, stdin);      //> Lee la línea, como máximo 49 caracteres + '\0'
    direccion[strcspn(direccion, "\n")] = '\0';     //> strcspn da la posición del '\n': ahí se pone el tope
    printf("[%s] (%zu caracteres)\n", direccion, strlen(direccion));
    return 0;
}
```
Si no te importa conservar espacios al inicio, `scanf(" %49[^\n]", direccion)` del Tema 02 también funciona y no guarda el Enter.
:::

:::concepto | 4 | Recorrer una cadena carácter por carácter | Elementos aislados, Atención dividida
Igual que un arreglo, pero sin necesitar el tamaño: se avanza **hasta encontrar el tope**.

```c run title="recorrer.c"
#include <stdio.h>
int main(void)
{
    char frase[] = "Murcielago";
    int vocales = 0;
    for (int i = 0; frase[i] != '\0'; i++)         //> Termina al llegar al '\0'
    {
        char c = frase[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
            vocales++;
    }
    printf("Vocales: %d\n", vocales);
    for (int i = 0; frase[i] != '\0'; i++)
        printf("%c-", frase[i]);
    printf("\n");
    return 0;
}
```
Escribir `i < strlen(frase)` también funciona, pero recalcula la longitud en cada vuelta; comparar con `'\0'` es la forma idiomática en C.
:::

:::movimiento | La cadena humana (10 min)
Cinco estudiantes forman la palabra `GATOS` con tarjetas; un sexto sostiene un letrero `'\0'` al final. El instructor pide operaciones y el grupo predice antes qué pasará: «`s[1] = 'O'`» (un estudiante cambia su tarjeta), «`s[3] = '\0'`» (el estudiante de la posición 3 cambia su tarjeta por un tope: ¿qué texto «se lee» ahora?), «`strcat(s, "IN")`» (¿dónde se colocan las nuevas letras?), «¿dónde está la `T`?» (`strchr`). Pregunta final: ¿qué pasa si alguien olvida su letrero de tope?
:::

:::concepto | 5 | Clasificar y transformar caracteres con `<ctype.h>` | Elementos aislados
| Función | Devuelve verdadero si `c` es… | Función | Hace |
|---|---|---|---|
| `isalpha(c)` | letra | `toupper(c)` | mayúscula de `c` |
| `isdigit(c)` | dígito `0`–`9` | `tolower(c)` | minúscula de `c` |
| `isalnum(c)` | letra o dígito | | |
| `isspace(c)` | espacio, tabulador, salto | | |
| `isupper(c)` / `islower(c)` | mayúscula / minúscula | | |
| `ispunct(c)` | signo de puntuación | | |

```c run title="ctype.c"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(void)
{
    char s[] = "Hola Mundo 2026!";
    char grito[30];
    strcpy(grito, s);
    for (int i = 0; grito[i] != '\0'; i++)       //> Se modifica cada casilla del arreglo
        grito[i] = toupper(grito[i]);
    int letras = 0, digitos = 0;
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (isalpha(s[i])) letras++;
        else if (isdigit(s[i])) digitos++;
    }
    printf("%s | letras: %d, digitos: %d\n", grito, letras, digitos);
    return 0;
}
```
:::

:::concepto | 6 | Buscar y extraer: `strchr`, `strstr` y `strncpy` | Elementos aislados, Atención dividida
`strchr(s, c)` busca un carácter y `strstr(s, texto)` busca un texto. Ambas devuelven un **puntero** a la posición encontrada (una dirección dentro de `s`) o `NULL` si no lo encuentran. Restar `p - s` da el índice. (Los punteros se estudian en el Tema 14.)

```c run title="buscar.c"
#include <stdio.h>
#include <string.h>
int main(void)
{
    char s[] = "programar en C es divertido";
    char *p = strchr(s, 'C');                       //> Puntero a la primera 'C', o NULL
    if (p != NULL)
        printf("C en la posicion %d\n", (int)(p - s));   //> p - s: cuántas casillas desde el inicio
    char *q = strstr(s, "es");
    if (q != NULL)
        printf("Desde \"es\": %s\n", q);           //> Un puntero dentro de una cadena también es una cadena: muestra el resto
    if (strstr(s, "Python") == NULL)               //> NULL = «no se encontró»
        printf("No menciona Python\n");
    char primera[10];
    strncpy(primera, s, 9);                        //> Copia como máximo 9 caracteres…
    primera[9] = '\0';                             //> …pero strncpy no pone el tope: hay que ponerlo
    printf("%s\n", primera);
    return 0;
}
```
:::

:::concepto | 7 | Ruta B · De texto a número y de número a texto | Elementos aislados, Reversión de la experiencia
```c run title="conversiones.c"
#include <stdio.h>
#include <stdlib.h>                                //> atoi, atof, strtol
int main(void)
{
    char edadTxt[] = "17", precioTxt[] = "249.90";
    int edad = atoi(edadTxt);                      //> texto → int
    double precio = atof(precioTxt);               //> texto → double
    printf("%d %.2f\n", edad + 1, precio * 2);
    char folio[20];
    snprintf(folio, sizeof folio, "PED-%d", 1000 + edad);   //> número → texto: «printf hacia una cadena»
    printf("%s\n", folio);
    char *fin;
    long n = strtol("42abc", &fin, 10);            //> strtol dice además dónde se detuvo
    printf("%ld, sobro: \"%s\"\n", n, fin);
    return 0;
}
```
`atoi("abc")` devuelve 0 sin avisar del error; cuando necesites validar, usa `strtol` y revisa dónde se detuvo.
:::

:::concepto | 8 | Ruta B · Funciones de cadena a mano y el desbordamiento de búfer | Elementos aislados, Reversión de la experiencia
Las funciones de `<string.h>` no hacen magia: recorren el arreglo hasta el `'\0'`. Programarlas a mano ayuda a entenderlas:

```c run title="cadenas_mano.c"
#include <stdio.h>
#include <string.h>
int longitud(const char s[])
{
    int n = 0;
    while (s[n] != '\0') n++;          //> Cuenta hasta encontrar el tope
    return n;
}
void copiar(char destino[], const char origen[])
{
    int i = 0;
    while (origen[i] != '\0')
    {
        destino[i] = origen[i];
        i++;
    }
    destino[i] = '\0';                 //> ¡El tope también se copia!
}
int main(void)
{
    char a[20] = "gato", b[20];
    copiar(b, a);
    printf("%d %zu %d\n", longitud(a), strlen(b), strcmp(a, b));   //> strcmp: 0 si son iguales
    char corto[5];
    snprintf(corto, sizeof corto, "%s", "computadora");             //> Copia segura: corta el texto para que quepa
    printf("[%s]\n", corto);
    return 0;
}
```

Con `snprintf`, gcc incluso avisa al compilar que el texto no cabe (*directive output truncated*): la función lo corta a 4 letras más el `'\0'` sin dañar la memoria.

:::cuidado | Desbordamiento de búfer
`strcpy` y `strcat` **no revisan** el tamaño del destino: `char corto[5]; strcpy(corto, "computadora");` escribe 12 bytes en un arreglo de 5 y daña la memoria vecina. Es el origen de muchas fallas de seguridad. Calcula siempre el espacio (`strlen + 1`), usa `snprintf` o `strncat` cuando el texto venga del usuario y prueba con `-fsanitize=address`.
:::
:::

## 1.2 Ejemplo resuelto: analizador de frases

:::ejemplo | Contar vocales, consonantes, dígitos, espacios y palabras | Ejemplo resuelto, Atención dividida
**Problema.** Leer una frase y mostrar cuántas vocales, consonantes, dígitos y espacios tiene, cuántas palabras, y la frase en mayúsculas.

**A. Algoritmo:** 1) Leer la frase completa. 2) Recorrerla carácter por carácter: si es letra, decidir si es vocal o consonante; si es dígito, contarlo; si es espacio, contarlo. 3) Contar palabras: una palabra empieza cuando hay un carácter que no es espacio y el anterior era espacio (o es el inicio). 4) Mostrar los conteos y la frase en mayúsculas.

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

**C. Código en C**

```c run title="analizador.c" stdin="En 2026 programo  en C con 3 amigos\n"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool esVocal(char c)                                   //> Función auxiliar: una tarea, un nombre
{
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main(void)
{
    char frase[100];
    fgets(frase, sizeof frase, stdin);                 //> 1) La frase tiene espacios
    frase[strcspn(frase, "\n")] = '\0';
    int vocales = 0, consonantes = 0, digitos = 0, espacios = 0, palabras = 0;
    for (int i = 0; frase[i] != '\0'; i++)             //> 2) Recorrido hasta el tope
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
    char mayus[100];
    strcpy(mayus, frase);
    for (int i = 0; mayus[i] != '\0'; i++)              //> 4) Transformación
        mayus[i] = toupper(mayus[i]);
    printf("Vocales %d, consonantes %d, digitos %d, espacios %d, palabras %d\n%s\n",
           vocales, consonantes, digitos, espacios, palabras, mayus);
    return 0;
}
```

**D. Verificación.** La frase tiene **dos** espacios seguidos entre «programo» y «en»: hay 8 espacios y 8 palabras. Si contáramos «espacios + 1» obtendríamos 9 palabras (incorrecto); por eso una palabra se cuenta solo donde **empieza**: un carácter que no es espacio precedido por un espacio (o al inicio).
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.16; ranksep=0.3;
@term(t, "Cadena en C\nchar s[N] + '\\0'")
@proc(f, "<string.h>: strlen strcpy\nstrcat strcmp")
@io(l, "scanf(\"%s\") (palabra)\nfgets (línea)")
@proc(r, "recorrido hasta '\\0'\nfor (i = 0; s[i] != '\\0'; i++)")
@sub(cc, "<ctype.h>: isalpha isdigit\ntoupper tolower")
@sub(b, "buscar: strchr · strstr\n(puntero o NULL)")
@hl(cv, "atoi · strtol · snprintf\n¡cuidado con el tamaño!")
t -> f; t -> l; t -> r; r -> cc; f -> b; t -> cv [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1 · Cadenas en C
| Quiero… | Código | Ejemplo con `s` = `"Hola mundo"` |
|---|---|---|
| Declarar | `char s[50] = "Hola mundo";` | 50 casillas, 11 usadas |
| Longitud | `strlen(s)` | `10` |
| Carácter en `i` | `s[i]` | `s[0]` → `'H'` |
| Último carácter | `s[strlen(s) - 1]` | `'o'` |
| Copiar | `strcpy(d, s);` · seguro: `snprintf(d, sizeof d, "%s", s);` | |
| Unir | `strcat(d, "!");` | `"Hola mundo!"` |
| Comparar | `strcmp(a, b)` → `0` iguales · `< 0` antes · `> 0` después | `strcmp("ana", "beto") < 0` |
| Buscar carácter | `strchr(s, 'm')` → puntero o `NULL`; índice `p - s` | `5` |
| Buscar texto | `strstr(s, "mu")` → puntero o `NULL` | |
| Leer palabra | `scanf("%49s", s);` | |
| Leer línea | `fgets(s, sizeof s, stdin); s[strcspn(s, "\n")] = '\0';` | |
| Texto → número | `atoi("42")`, `atof("3.5")`, `strtol(…)` | `42` |
| Número → texto | `snprintf(buf, sizeof buf, "%d", x);` | |
| A mayúsculas | `for (int i = 0; s[i] != '\0'; i++) s[i] = toupper(s[i]);` | `"HOLA MUNDO"` |

Cabeceras: `<string.h>` (cadenas), `<ctype.h>` (clasificar caracteres), `<stdlib.h>` (`atoi`, `strtol`).
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿El arreglo tiene espacio para todo el texto <b>más</b> el <code>'\0'</code>?</li>
<li>¿El texto puede tener espacios? Entonces <code>fgets</code> (y quitar el <code>'\n'</code>), o <code>" %[^\n]"</code>.</li>
<li>¿Mis recorridos terminan en <code>s[i] != '\0'</code>? ¿Uso <code>s[i + 1]</code> sin salirme?</li>
<li>¿Considero mayúsculas y minúsculas? (Normaliza con <code>tolower</code> antes de comparar.)</li>
<li>¿Reviso que <code>strchr</code>/<code>strstr</code> no hayan devuelto <code>NULL</code> antes de usar el resultado?</li>
<li>¿Distingo <code>'a'</code> (un <code>char</code>) de <code>"a"</code> (una cadena)?</li>
<li>¿Copio con <code>strcpy</code> y comparo con <code>strcmp</code>, nunca con <code>=</code> ni <code>==</code>?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Comparar un `char` con una cadena.** `"c"` es un texto (la dirección de un arreglo), no un carácter:

```c warn
#include <stdio.h>
int main(void)
{
    char s[] = "casa";
    if (s[0] == "c")
        printf("Empieza con c\n");
    return 0;
}
```
*Corrección:* `s[0] == 'c'` (comillas simples).

**b) Asignar texto con `=`.** Un arreglo no se puede asignar completo (Tema 08):

```c err
#include <stdio.h>
int main(void)
{
    char nombre[20];
    nombre = "Ana";
    printf("%s\n", nombre);
    return 0;
}
```
*Corrección:* `strcpy(nombre, "Ana");` o inicializar al declarar: `char nombre[20] = "Ana";`.

**c) Comparar cadenas con `==`.** Compara **direcciones**, no contenido: usa `strcmp(a, b) == 0`.

**d) Olvidar el espacio del `'\0'`.** `char c[4] = {'H', 'o', 'l', 'a'};` no tiene tope y `printf("%s", c)` sigue leyendo memoria. En C, incluso `char c[4] = "Hola";` compila sin aviso: el `'\0'` no cabe y se omite en silencio. Debe ser `char c[5] = "Hola";` (o `char c[] = "Hola";`).

**e) Usar el resultado de `strstr` sin verificar `NULL`.** Si no se encuentra, `p - s` no tiene sentido y `printf("%s", p)` puede detener el programa. Verifica: `if (p != NULL) …`.

**f) `fgets` que guarda el Enter.** Sin `s[strcspn(s, "\n")] = '\0';`, el texto incluye un `'\n'` y comparaciones como `strcmp(s, "si")` fallan.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Censurar palabras | Variabilidad
Mismo patrón (buscar y reemplazar en ciclo), otro contexto: un chat que censura una palabra.

```c run title="censura.c"
#include <stdio.h>
#include <string.h>
int main(void)
{
    char msg[] = "eres un tonto, muy tonto";
    const char *mala = "tonto";
    size_t n = strlen(mala);
    char *p = strstr(msg, mala);
    while (p != NULL)                                  //> Mientras siga apareciendo…
    {
        for (size_t k = 0; k < n; k++)
            p[k] = '*';                                //> …reemplaza sus letras por asteriscos
        p = strstr(msg, mala);                         //> La ya censurada no vuelve a coincidir
    }
    printf("%s\n", msg);
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Cuando dudes, escribe el texto en casillas con sus índices y su `'\0'`.

:::tarea A | T1. Iniciales de un nombre: ejemplo y gemelo | 20 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia:**

```c run title="iniciales.c" stdin="ana sofia lopez\n"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(void)
{
    char nombre[60], ini[20];
    int k = 0;                                                     //> Siguiente casilla libre de ini
    fgets(nombre, sizeof nombre, stdin);
    nombre[strcspn(nombre, "\n")] = '\0';
    for (int i = 0; nombre[i] != '\0'; i++)
    {
        if (nombre[i] != ' ' && (i == 0 || nombre[i - 1] == ' '))  //> Inicio de palabra
        {
            ini[k++] = toupper(nombre[i]);                         //> Agrega la letra en mayúscula
            ini[k++] = '.';
        }
    }
    ini[k] = '\0';                                                 //> Cerramos la cadena construida
    printf("Iniciales: %s\n", ini);
    return 0;
}
```

**Paso 2 · Gemelo.** Genera un **nombre de usuario**: primera letra del nombre + primer apellido completo, todo en minúsculas, + los dos últimos dígitos de un año que se lee después. Ejemplo: `Luis Perez Gil` y `2026` → `lperez26`.

:::solucion | T1
```c run title="usuario.c" stdin="Luis Perez Gil\n2026\n"
#include <stdio.h>
#include <ctype.h>
int main(void)
{
    char nombre[20], apellido[20], usuario[50];
    int anio;
    scanf("%19s %19s %*s %d", nombre, apellido, &anio);   // %*s lee el segundo apellido y lo descarta
    snprintf(usuario, sizeof usuario, "%c%s%02d", nombre[0], apellido, anio % 100);
    for (int i = 0; usuario[i] != '\0'; i++)
        usuario[i] = tolower(usuario[i]);
    printf("%s\n", usuario);
    return 0;
}
```
`snprintf` arma el texto con el mismo formato de `printf`, pero lo guarda en `usuario`.
:::
:::

:::tarea A | T2. ¿Es palíndromo? (completa con pistas) | 25 min | Problema por completar
**Contexto.** «Anita lava la tina» se lee igual al revés si se ignoran espacios y mayúsculas. Primero se **limpia** la frase (solo letras, en minúsculas) y luego se compara cada extremo.

```c blank title="palindromo.c"
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
int main(void)
{
    char frase[100], limpia[100];
    int n = 0;
    fgets(frase, sizeof frase, stdin);
    for (int i = 0; frase[i] != '\0'; i++)
        if (__1__)                                   // 1: solo letras
            limpia[n++] = __2__;                     // 2: en minuscula
    limpia[n] = '\0';
    bool es = true;
    for (int i = 0; i < __3__; i++)                  // 3: basta revisar la mitad
        if (limpia[i] != limpia[__4__])              // 4: el caracter "espejo" de i
        {
            es = false;
            __5__;                                   // 5: ya no hace falta seguir
        }
    printf(es ? "Es palindromo\n" : "No es palindromo\n");
    return 0;
}
```

:::solucion | T2
{{c:1}} `isalpha(frase[i])` · {{c:2}} `tolower(frase[i])` · {{c:3}} `n / 2` · {{c:4}} `n - 1 - i` · {{c:5}} `break`

```c run title="palindromo.c" runs="Anita lava la tina|Programar es divertido"
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
int main(void)
{
    char frase[100], limpia[100];
    int n = 0;
    fgets(frase, sizeof frase, stdin);
    for (int i = 0; frase[i] != '\0'; i++)
        if (isalpha(frase[i]))
            limpia[n++] = tolower(frase[i]);
    limpia[n] = '\0';
    bool es = true;
    for (int i = 0; i < n / 2; i++)
        if (limpia[i] != limpia[n - 1 - i])
        {
            es = false;
            break;
        }
    printf(es ? "Es palindromo\n" : "No es palindromo\n");
    return 0;
}
```
Aquí no hace falta quitar el `'\n'` de `fgets`: `isalpha` lo descarta junto con los espacios.
:::
:::

:::tarea AB | T3. ¿Contraseña segura? (completa sin pistas) | 25 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Una contraseña es segura si tiene al menos 8 caracteres, una mayúscula, una minúscula, un dígito y un símbolo (cualquier carácter que no sea letra ni dígito). La función escribe en `faltan` qué requisitos no se cumplen.

```c blank title="password.c"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
bool segura(const char p[], char faltan[])
{
    bool may = false, min = false, dig = false, sim = false;
    for (int i = 0; p[i] != '\0'; i++)
    {
        if (__1__) may = true;
        else if (__2__) min = true;
        else if (__3__) dig = true;
        else __4__;
    }
    faltan[0] = '\0';
    if (__5__) strcat(faltan, " longitud");
    if (!may) strcat(faltan, " mayuscula");
    if (!min) strcat(faltan, " minuscula");
    if (!dig) strcat(faltan, " digito");
    if (!sim) strcat(faltan, " simbolo");
    return __6__;
}
int main(void)
{
    char p[50], faltan[80];
    scanf("%49s", p);
    if (segura(p, faltan)) printf("Segura\n");
    else printf("Insegura, falta:%s\n", faltan);
    return 0;
}
```

:::solucion | T3
{{c:1}} `isupper(p[i])` · {{c:2}} `islower(p[i])` · {{c:3}} `isdigit(p[i])` · {{c:4}} `sim = true` · {{c:5}} `strlen(p) < 8` · {{c:6}} `faltan[0] == '\0'`

```c run title="password.c" runs="hola123|Gato#2026|ABCdefgh"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
bool segura(const char p[], char faltan[])
{
    bool may = false, min = false, dig = false, sim = false;
    for (int i = 0; p[i] != '\0'; i++)
    {
        if (isupper(p[i])) may = true;
        else if (islower(p[i])) min = true;
        else if (isdigit(p[i])) dig = true;
        else sim = true;
    }
    faltan[0] = '\0';
    if (strlen(p) < 8) strcat(faltan, " longitud");
    if (!may) strcat(faltan, " mayuscula");
    if (!min) strcat(faltan, " minuscula");
    if (!dig) strcat(faltan, " digito");
    if (!sim) strcat(faltan, " simbolo");
    return faltan[0] == '\0';
}
int main(void)
{
    char p[50], faltan[80];
    scanf("%49s", p);
    if (segura(p, faltan)) printf("Segura\n");
    else printf("Insegura, falta:%s\n", faltan);
    return 0;
}
```
`faltan[0] = '\0'` deja la cadena **vacía** (tope en la primera casilla) para que `strcat` empiece desde ahí.
:::
:::

:::tarea AB | T4. Cifrado César (problema convencional) | 35 min | Variabilidad
**Contexto.** Julio César cifraba sus mensajes desplazando cada letra `k` posiciones en el alfabeto (con `k = 3`: A→D, B→E, …, X→A, Y→B, Z→C). Escribe `void cifrar(char msg[], int k)` que modifique el texto respetando mayúsculas y minúsculas, deje igual lo que no sea letra y dé la vuelta al llegar a la Z. Descifra usando la misma función con `26 − k`. Prueba con «Ataque al amanecer, 7am».

:::solucion | T4
```c run title="cesar.c"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
void cifrar(char msg[], int k)
{
    for (int i = 0; msg[i] != '\0'; i++)
    {
        if (isupper(msg[i])) msg[i] = 'A' + (msg[i] - 'A' + k) % 26;
        else if (islower(msg[i])) msg[i] = 'a' + (msg[i] - 'a' + k) % 26;
    }
}
int main(void)
{
    char secreto[50];
    strcpy(secreto, "Ataque al amanecer, 7am");
    cifrar(secreto, 3);                  // el arreglo se modifica en su lugar
    printf("%s\n", secreto);
    cifrar(secreto, 26 - 3);
    printf("%s\n", secreto);
    return 0;
}
```
`msg[i] - 'A'` convierte la letra en su posición (0–25); `% 26` da la vuelta; `'A' + …` la convierte de nuevo en letra. Como los arreglos se pasan por dirección (Tema 10), la función modifica el texto original.
:::
:::

:::tarea A | T5. Todo sobre una frase (solución libre) | 25 min | Solución libre
**Contexto.** Dada la frase `"Programar en C es divertido desde 2026"`, **descubre y muestra todo lo que puedas**: longitud, número de palabras, la palabra más larga, la frase al revés, cuántas veces aparece cada vocal, si contiene «en C», la frase sin espacios, en formato «Título» (cada palabra con mayúscula inicial)… No hay lista obligatoria.

:::solucion | T5
Una exploración posible:

```c run title="explora_frase.c"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(void)
{
    char f[] = "Programar en C es divertido desde 2026";
    int n = strlen(f);
    char reves[60], sinEsp[60], titulo[60];
    int k = 0, palabras = 0, cuenta[5] = {0};
    int iniLarga = 0, lenLarga = 0, iniActual = 0;
    const char *voc = "aeiou";
    strcpy(titulo, f);
    for (int i = 0; i < n; i++)
    {
        char c = f[i];
        reves[n - 1 - i] = c;
        if (c != ' ') sinEsp[k++] = c;
        char *v = strchr(voc, tolower(c));
        if (v != NULL) cuenta[v - voc]++;               // posicion de la vocal en "aeiou"
        if (c != ' ' && (i == 0 || f[i - 1] == ' '))
        {
            palabras++;
            titulo[i] = toupper(c);
            iniActual = i;
        }
        if (c != ' ' && (i == n - 1 || f[i + 1] == ' ') && i - iniActual + 1 > lenLarga)
        {
            lenLarga = i - iniActual + 1;               // fin de palabra: ¿es la mas larga?
            iniLarga = iniActual;
        }
    }
    reves[n] = '\0';
    sinEsp[k] = '\0';
    printf("Longitud %d, palabras %d, mas larga: %.*s\n", n, palabras, lenLarga, f + iniLarga);
    printf("Al reves: %s\nSin espacios: %s\nTitulo: %s\n", reves, sinEsp, titulo);
    for (int j = 0; j < 5; j++) printf("%c=%d ", voc[j], cuenta[j]);
    printf("\nContiene \"en C\": %s\n", strstr(f, "en C") != NULL ? "si" : "no");
    return 0;
}
```
`%.*s` muestra solo `lenLarga` caracteres a partir de `f + iniLarga`: una forma de imprimir una subcadena sin copiarla.
:::
:::

:::tarea B | T6. Comparar cadenas sin `strcmp` (autoexplicación, tesis §6.1.6) | 25 min | Autoexplicación, Reversión de la experiencia
**Contexto.** «La maestra dejó un ejercicio del tema de cadenas visto en la clase: realizar un programa que, dadas dos cadenas de caracteres, las compare y diga si son **iguales o diferentes** (sin utilizar las funciones `strcmp`, `strcpy` y `strlen`). Uno de tus compañeros ya programó su solución, pero no funciona adecuadamente. **¿Puedes identificar cuál es el error (o errores), explicar por qué no funciona, y proponer una solución con su explicación?**»

```c run title="compara_bug.c"
#include <stdio.h>
#include <stdbool.h>
int main(void)
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
    printf(iguales ? "Iguales\n" : "Diferentes\n");
    return 0;
}
```

{{lineas:5}}

:::solucion | T6
**Errores:** (1) el ciclo solo recorre `a`: si `b` es más larga pero empieza igual («programa» / «programas»), nunca detecta la diferencia; hay que verificar que **ambas** terminen al mismo tiempo. (2) `a == b` compara las **direcciones** de los arreglos, no su contenido; aquí es falso y no afecta, pero es un error conceptual (y si fuera verdadero, ocultaría diferencias). Con `-Wall`, gcc lo señala: *comparison between two arrays*. (3) No se detiene en la primera diferencia (no es un error, pero hace trabajo de más).

```c run title="compara.c"
#include <stdio.h>
#include <stdbool.h>
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
int main(void)
{
    char a[30] = "programa", b[30] = "programas", c[30] = "programa";
    printf("%s / %s\n", sonIguales(a, b) ? "Iguales" : "Diferentes",
           sonIguales(a, c) ? "Iguales" : "Diferentes");
    return 0;
}
```
:::
:::

:::tarea B | T7. ¿Cómo quedan las cadenas? (imaginación) | 20 min | Imaginación
**Sin ejecutar**, imagina el contenido de `s` y de `t` después de **cada** línea (dibuja las casillas **con** su `'\0'`) y la salida final. Después compruébalo.

```c check title="imagina_cadena.c"
#include <stdio.h>
#include <string.h>
int main(void)
{
    char s[20] = "MESA";
    char t[20];
    strcat(s, "TERO");
    s[4] = '\0';
    s[0] = 'P';
    strcpy(t, s);
    strcat(t, "DO");
    t[1] = t[3];
    printf("%s %s %zu %zu %zu\n", s, t, strlen(s), strlen(t), sizeof(s));
    return 0;
}
```

{{lineas:4}}

:::solucion | T7
`s = "MESA"` → `strcat` → `"MESATERO"` → `s[4] = '\0'` → se lee `"MESA"` (las letras `TERO` siguen en memoria, pero después del tope ya no cuentan) → `s[0] = 'P'` → `"PESA"` → `strcpy(t, s)`: `t = "PESA"` (copia independiente) → `strcat(t, "DO")` → `"PESADO"` → `t[1] = t[3]` → `"PASADO"`; `s` no cambia. `strlen` cuenta letras (4 y 6); `sizeof` mide el arreglo completo (20).

```c run title="imagina_cadena.c"
#include <stdio.h>
#include <string.h>
int main(void)
{
    char s[20] = "MESA";
    char t[20];
    strcat(s, "TERO");
    s[4] = '\0';
    s[0] = 'P';
    strcpy(t, s);
    strcat(t, "DO");
    t[1] = t[3];
    printf("%s %s %zu %zu %zu\n", s, t, strlen(s), strlen(t), sizeof(s));
    return 0;
}
```
:::
:::

:::tarea AB | T8. El ahorcado (reto colaborativo) | 45 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Equipos de 4, niveles mezclados. Palabra secreta fija (por ejemplo, `"compilador"`), 6 vidas.
- **Integrante 1:** `void mascara(const char secreta[], const char usadas[], char m[])` → `c o _ _ _ _ _ _ o _`.
- **Integrante 2:** procesar un intento: validar que sea letra, que no se haya usado antes, y si no está en la palabra, restar una vida.
- **Integrante 3:** detectar victoria (no quedan `_`) y derrota (vidas = 0).
- **Integrante 4:** el ciclo del juego y los mensajes; probar con una partida ganada y una perdida.
:::

:::solucion | T8
Partida simulada (entrada: `o a c x i l z m p r d`):

```c run title="ahorcado.c" stdin="o\na\nc\nx\ni\nl\nz\nm\np\nr\nd\n"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
void mascara(const char secreta[], const char usadas[], char m[])
{
    int k = 0;
    for (int i = 0; secreta[i] != '\0'; i++)
    {
        m[k++] = strchr(usadas, secreta[i]) != NULL ? secreta[i] : '_';
        m[k++] = ' ';
    }
    m[k] = '\0';
}
int main(void)
{
    const char secreta[] = "compilador";
    char usadas[30] = "", m[30];
    int nu = 0, vidas = 6;
    while (vidas > 0)
    {
        mascara(secreta, usadas, m);
        if (strchr(m, '_') == NULL) { printf("%s\nGanaste!\n", m); return 0; }
        printf("%s (vidas: %d) letra: ", m, vidas);
        char c;
        scanf(" %c", &c);
        c = tolower(c);
        if (!isalpha(c) || strchr(usadas, c) != NULL) { printf("No valida o repetida\n"); continue; }
        usadas[nu++] = c;
        usadas[nu] = '\0';
        if (strchr(secreta, c) == NULL) vidas--;
    }
    printf("\nPerdiste. Era: %s\n", secreta);
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

**Segmento 3 — Cuidar el borde izquierdo y el Enter.** {{como}} Escribo la condición `i == 0 || isspace(f[i - 1])` con el `i == 0` **primero**, y uso `isspace` para que el `'\n'` que guarda `fgets` cuente como espacio. {{porque}} Por el cortocircuito de `||`, si `i` es 0 nunca se evalúa `f[-1]`, que estaría fuera de la cadena.

**Segmento 4 — Probar los casos extremos.** {{como}} Pruebo la frase normal, la de espacios de más y una de una sola palabra. {{porque}} Los errores en cadenas casi siempre están en los extremos: inicio, final y texto vacío.

```c run title="contar_palabras.c" runs="Hola mundo cruel|   hola    mundo  |unica"
#include <stdio.h>
#include <ctype.h>
int contarPalabras(const char f[])
{
    int n = 0;
    for (int i = 0; f[i] != '\0'; i++)
        if (!isspace(f[i]) && (i == 0 || isspace(f[i - 1])))
            n++;
    return n;
}
int main(void)
{
    char f[100];
    fgets(f, sizeof f, stdin);
    printf("%d palabras\n", contarPalabras(f));
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. ¿Qué carácter marca el final de una cadena en C?
2. ¿Cuántas casillas ocupa `char x[] = "Sol";`?
3. ¿Qué diferencia hay entre `scanf("%49s", s)` y `fgets(s, 50, stdin)`?
4. ¿Qué devuelve `strstr(s, "x")` cuando no encuentra el texto?
5. ¿Qué devuelve `strcmp(a, b)` cuando las dos cadenas son iguales?
6. ¿Qué hace `toupper('m')`?
7. Verdadero o falso: con cadenas de C, `a == b` compara el texto.
8. ¿Qué función convierte `"42"` en el entero 42?
9. ¿Por qué `strcmp("Zorro", "abeja")` es negativo?
10. ¿Por qué no se puede escribir `nombre = "Ana";` si `nombre` es `char nombre[20]`? ¿Qué se escribe en su lugar?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Predice la salida:**

```c check title="p1.c"
#include <stdio.h>
#include <string.h>
int main(void)
{
    char s[] = "computadora";
    printf("%zu %c %s ", strlen(s), s[3], strstr(s, "dora"));
    printf("%d %d\n", (int)(strchr(s, 'o') - s), strcmp(s, "computador") > 0);
    return 0;
}
```

**P2.** Escribe una función `void invertir(const char s[], char r[])` que deje en `r` el texto de `s` al revés, sin usar funciones de biblioteca.

**P3. Corrige:** `char s[20]; scanf("%19s", s); for (int i = 0; i <= strlen(s); i++) if (s[i] == "a") s[i] = 'A';`

**P4. Escribe un programa** que lea un correo electrónico y valide que tenga exactamente una `@`, al menos un carácter antes de ella y un punto después de ella; si es válido, muestra el usuario (antes de la `@`) y el dominio (después).
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Explico cómo se guarda una cadena en C y por qué existe el <code>'\0'</code>.</li>
<li>Recorro cadenas y clasifico caracteres con <code>&lt;ctype.h&gt;</code>.</li>
<li>Uso <code>strlen</code>, <code>strcpy</code>, <code>strcat</code>, <code>strcmp</code>, <code>strchr</code> y <code>strstr</code> sin desbordar los arreglos.</li>
<li>Pruebo mis programas con textos vacíos, con espacios de más y con mayúsculas.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 `'\0'` · 2 4 (3 letras + `'\0'`) · 3 `scanf("%s")` lee hasta el primer espacio; `fgets` lee la línea completa (con su `'\n'`) sin pasarse del tamaño · 4 `NULL` · 5 `0` · 6 Devuelve `'M'` · 7 Falso: compara direcciones · 8 `atoi` (o `strtol`) · 9 Porque se compara por código ASCII y `'Z'` (90) es menor que `'a'` (97) · 10 Porque un arreglo no se puede asignar completo; se usa `strcpy(nombre, "Ana");`.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** `strstr` devuelve un puntero a `"dora"` (y `%s` muestra desde ahí); la primera `'o'` está en la posición 1; `"computadora"` va después de `"computador"` porque es más larga con el mismo inicio.

```c run title="p1.c"
#include <stdio.h>
#include <string.h>
int main(void)
{
    char s[] = "computadora";
    printf("%zu %c %s ", strlen(s), s[3], strstr(s, "dora"));
    printf("%d %d\n", (int)(strchr(s, 'o') - s), strcmp(s, "computador") > 0);
    return 0;
}
```

**P2.** `void invertir(const char s[], char r[]) { int n = 0; while (s[n] != '\0') n++; for (int i = 0; i < n; i++) r[i] = s[n - 1 - i]; r[n] = '\0'; }`

**P3.** Recorre hasta el tope (`s[i] != '\0'`) en lugar de `i <= strlen(s)` (que además mezcla `int` con `size_t`), y usa `'a'` con comillas simples: `for (int i = 0; s[i] != '\0'; i++) if (s[i] == 'a') s[i] = 'A';`

**P4.**

```c run title="correo.c" runs="ana.lopez@escuela.edu.mx|sin_arroba.com|@dominio.com"
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
int main(void)
{
    char c[80];
    scanf("%79s", c);
    char *a = strchr(c, '@');
    bool valido = a != NULL && a != c                 // hay @ y no esta al inicio
                  && strchr(a + 1, '@') == NULL       // no hay otra @ despues
                  && strchr(a + 1, '.') != NULL;      // hay un punto despues
    if (valido)
        printf("Usuario: %.*s  Dominio: %s\n", (int)(a - c), c, a + 1);
    else
        printf("Correo invalido\n");
    return 0;
}
```
:::
