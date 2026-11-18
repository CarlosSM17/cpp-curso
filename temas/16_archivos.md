---
num: "16"
archivo: "Tema16_Archivos_de_texto"
titulo: "Almacenamiento en memoria secundaria: archivos de texto"
corto: "Archivos"
lema: "Lo que está en variables se borra al cerrar el programa; lo que está en un archivo te espera mañana."
duracion: "5 h · 3 sesiones"
previos: "Tema 06 (ciclos y centinelas), Tema 12 (cadenas, `fgets`), Tema 13 (estructuras) y Tema 14 (punteros)."
fuentes:
  - "Kernighan, B. W. y Ritchie, D. M. (1988). *The C Programming Language* (2.ª ed.). Prentice Hall. Cap. 7: §7.5 File Access, §7.6 Error Handling—Stderr and Exit, §7.7 Line Input and Output. Apéndice B, §B1 «Input and Output: <stdio.h>»."
  - "King, K. N. (2008). *C Programming: A Modern Approach* (2.ª ed.). W. W. Norton. Cap. 22 «Input/Output»: §22.1 Streams, §22.2 File Operations, §22.3 Formatted I/O, §22.5 Line I/O, §22.6 Block I/O, §22.8 String I/O."
  - "Seacord, R. C. (2020). *Effective C*. No Starch Press. Cap. 8 «Input/Output»."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §7.5: segundo estudio piloto (aplicación web CLT4BP) sobre manejo de archivos de texto en C; Figuras 7.13 y 7.14 (tareas de configuración y registro de estudiantes en archivos)."
objetivos:
  A:
    - "Explicar qué es un archivo, la diferencia entre memoria principal y secundaria y entre archivos de texto y binarios."
    - "Escribir datos en archivos de texto con `fopen` y `fprintf`, creando, sobrescribiendo o agregando (modos `\"w\"` y `\"a\"`)."
    - "Leer archivos de texto con `fscanf` (por datos) y `fgets` (por líneas) hasta el fin del archivo."
    - "Verificar que el archivo se abrió (`NULL`) y cerrarlo con `fclose`."
  B:
    - "Procesar registros con campos separados por comas usando `fgets` y `sscanf`."
    - "Implementar consulta, alta, baja y modificación de registros (archivo temporal + `remove`/`rename`)."
    - "Interpretar el valor de retorno de `fscanf` y `fgets` (y `feof`) para leer de forma robusta."
    - "Guardar y recuperar estructuras en archivos binarios con `fwrite` y `fread`."
efectos:
  soporte:
    - ["Elementos aislados", "Archivo → FILE * → escribir → modos → verificar → leer datos → leer líneas → registros con campos → binarios."]
    - ["Atención dividida", "El contenido real del archivo se muestra junto al código que lo produce o lo lee."]
    - ["Ejemplo resuelto", "Registro de calificaciones: escribir el archivo y leerlo de nuevo para calcular el promedio."]
    - ["Variabilidad", "Archivos de bitácora, inventario, ventas, configuración y registro escolar."]
  procedimental:
    - ["Variabilidad", "Plantillas de lectura/escritura para distintos formatos."]
    - ["Autoexplicación", "Errores clásicos (`feof`, apertura no verificada) planteados como «¿por qué se repite el último dato?»."]
  tareas:
    - ["Ejemplo resuelto", "T1: bitácora de temperaturas + gemelo (diario de gastos)."]
    - ["Problema por completar", "T2 (estadísticas de un archivo, con pistas) y T3 (contar líneas y palabras, sin pistas)."]
    - ["Desvanecimiento de guía", "T1 → T4."]
    - ["Solución libre", "T5: obtener toda la información posible de un archivo de ventas."]
    - ["Autoexplicación", "T6: errores clásicos con archivos."]
    - ["Imaginación", "T7: imaginar el contenido de un archivo tras varias aperturas."]
    - ["Memoria colectiva de trabajo", "T8: registro de estudiantes con altas, bajas y consultas."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "`fopen`/`fclose`, modos `\"w\"`, `\"a\"` y `\"r\"`, `fprintf`, lectura con `fscanf` y `fgets`, verificación de `NULL`."
    B: "Registros CSV con `sscanf`, bajas con archivo temporal, valor de retorno de las funciones de lectura, archivos binarios."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 abriendo los archivos generados en un editor para comprobarlos."
    B: "T5, T6, T7 autónomas; T8 como responsables del formato del archivo."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Reporte de surtido generado a partir de un inventario (T4)."
    B: "Registro escolar con altas, bajas y consultas persistentes (T8)."
  Entorno:
    comp: "Información procedimental"
    A: "IDE con el explorador de archivos abierto en la carpeta del proyecto."
    B: "Terminal: `cat`/`type` para ver archivos, redirección `programa < datos.txt`."
plan:
  - ["Sesión 1", "Soporte + tareas", "Analogía del cuaderno; conceptos 1–5; ejemplo resuelto; T1.", "100 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–9; T2, T3, T4; Ruta B: T6, T7.", "100 min"]
  - ["Sesión 3", "Tareas + evaluación", "T5, T8 colaborativa; protocolo verbal; tests.", "100 min"]
glosario:
  - ["archivo / fichero", "file", "Conjunto de datos con nombre guardado en memoria secundaria."]
  - ["memoria secundaria", "secondary storage", "Disco, memoria USB…: conserva los datos al apagar."]
  - ["archivo de texto", "text file", "Archivo cuyos bytes representan caracteres legibles."]
  - ["archivo binario", "binary file", "Archivo que guarda los bytes tal como están en memoria."]
  - ["flujo", "stream (`FILE *`)", "Canal de datos entre el programa y un archivo o dispositivo; `stdin`, `stdout` y lo que abre `fopen` son flujos."]
  - ["abrir / cerrar", "open / close (`fopen`, `fclose`)", "Conectar el programa con un archivo y desconectarlo (guardando lo pendiente)."]
  - ["modo de apertura", "open mode", "`\"w\"` (escribir desde cero), `\"a\"` (agregar), `\"r\"` (leer); con `b` para binario."]
  - ["fin de archivo", "end of file (`EOF`)", "Situación en la que ya no quedan datos por leer."]
  - ["valor de retorno de lectura", "return value", "`fscanf` devuelve cuántos datos leyó (o `EOF`); `fgets` devuelve `NULL` al terminar."]
  - ["búfer", "buffer", "Memoria intermedia donde se acumulan datos antes de escribirse al disco."]
  - ["registro", "record", "Conjunto de campos de una misma entidad (una línea de un CSV)."]
  - ["valores separados por comas", "CSV (comma-separated values)", "Formato de texto con un registro por línea y campos separados por comas."]
  - ["lectura desde cadena", "string input (`sscanf`)", "Aplica un formato de `scanf` a una cadena ya leída."]
---

# 1. Información de soporte {.soporte}

:::analogia | El pizarrón y el cuaderno
Lo que escribes en el **pizarrón** del salón (las variables, en la memoria **principal**) es rápido de escribir y borrar, pero al terminar la clase se borra. Lo que copias en tu **cuaderno** (un **archivo**, en la memoria **secundaria**) tarda un poco más, pero sigue ahí mañana. Para usar el cuaderno necesitas **abrirlo**, decidir si vas a **leer** o a **escribir**, y **cerrarlo** al terminar.
:::

:::pregunta
Un videojuego guarda tu partida y al día siguiente continúas en el mismo nivel. **¿Dónde crees que se guardó esa información si el programa se cerró?** ¿Qué datos tendría que guardar?

{{lineas:2}}
:::

:::relevancia
Las partidas guardadas, los archivos de configuración (como el `config.txt` del segundo piloto de la tesis, que se trabajó precisamente en C), las bitácoras de un servidor, las hojas de cálculo exportadas en CSV y los registros que un microcontrolador escribe en una memoria SD son archivos de texto. Saber leerlos y escribirlos permite que tus programas **recuerden** datos y **compartan** información con otros programas. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | Archivos de texto y binarios | Elementos aislados
| | Archivo de **texto** | Archivo **binario** |
|---|---|---|
| Contenido | caracteres legibles (`1`, `2`, `.`, `5`) | bytes tal como están en memoria |
| Se puede abrir con un editor | sí | no (se ven símbolos raros) |
| Ejemplo | `.txt`, `.csv`, `.c`, `.html` | `.exe`, `.jpg`, `.mp3` |
| El número 12.5 ocupa | 4 caracteres | 8 bytes (un `double`) |

En este tema trabajaremos sobre todo con archivos de **texto**; los binarios aparecen en la Ruta B (concepto 9).
:::

:::concepto | 2 | Flujos: `stdin` y `stdout` ya eran flujos | Elementos aislados, Atención dividida
Un **flujo** es un canal de datos. En C se maneja con un puntero `FILE *`. Sin saberlo, ya usabas dos: `printf` escribe en `stdout` (la pantalla) y `scanf` lee de `stdin` (el teclado). Para un archivo, `fopen` abre un flujo nuevo y se usan las **mismas** funciones con una `f` al inicio:

```dot w="85%"
rankdir=LR; nodesep=0.25; ranksep=0.45;
@io(t, "teclado (stdin)")
@term(p, "Programa")
@io(s, "pantalla (stdout)")
@file(fi, "datos.txt")
@file(fo, "reporte.txt")
t -> p [label=" scanf"]; p -> s [label=" printf"];
fi -> p [label=" fscanf · fgets"]; p -> fo [label=" fprintf · fputs"];
```

| Modo de `fopen` | Para | Si el archivo no existe | Si ya existe |
|---|---|---|---|
| `"r"` | leer | `fopen` devuelve `NULL` | lee desde el inicio |
| `"w"` | escribir | lo crea | **lo borra** y empieza de cero |
| `"a"` | agregar al final | lo crea | conserva y escribe al final |

Todo está en `<stdio.h>`.
:::

:::concepto | 3 | Escribir en un archivo con `fopen` y `fprintf` | Elementos aislados, Atención dividida
```c run title="escribir.c" showfile=saludo.txt
#include <stdio.h>
int main(void)
{
    FILE *archivo = fopen("saludo.txt", "w");    //> Abre (o crea) saludo.txt para escribir
    if (archivo == NULL) return 1;               //> Si no se pudo abrir, fopen devuelve NULL
    fprintf(archivo, "Hola desde C\n");          //> Como printf, pero el primer argumento es el archivo
    fprintf(archivo, "Linea %d\n", 2);
    fclose(archivo);                             //> Cierra: asegura que todo se guarde en disco
    printf("Archivo escrito\n");
    return 0;
}
```
El recuadro de abajo muestra el **contenido real** del archivo después de ejecutar el programa. El archivo queda en la **carpeta donde se ejecuta** el programa (en un IDE, normalmente la carpeta del proyecto).
:::

:::concepto | 4 | Modos de apertura: sobrescribir o agregar | Elementos aislados, Atención dividida
`"w"` **borra** el contenido anterior. Para **agregar** al final se usa `"a"` (*append*):

```c run title="modos.c" showfile=bitacora.txt
#include <stdio.h>
int main(void)
{
    FILE *f = fopen("bitacora.txt", "w");        //> Modo "w": crea o BORRA y empieza de cero
    if (f == NULL) return 1;
    fprintf(f, "inicio\n");
    fclose(f);
    f = fopen("bitacora.txt", "a");              //> Modo "a": conserva lo que había y agrega al final
    if (f == NULL) return 1;
    fprintf(f, "evento 1\n");
    fclose(f);
    f = fopen("bitacora.txt", "a");
    if (f == NULL) return 1;
    fprintf(f, "evento 2\n");
    fclose(f);
    return 0;
}
```
:::

:::concepto | 5 | ¿Se abrió? Verificar siempre | Elementos aislados
Abrir puede fallar (el archivo no existe, no hay permisos, la ruta está mal). En ese caso `fopen` devuelve `NULL`, y usar ese puntero detendría el programa. `perror` muestra el motivo que dio el sistema operativo:

```c run rc title="verificar.c"
#include <stdio.h>
int main(void)
{
    FILE *in = fopen("no_existe.txt", "r");
    if (in == NULL)
    {
        perror("no_existe.txt");              //> Escribe el nombre y la causa del error (en stderr)
        return 1;                             //> Terminar (o pedir otro nombre)
    }
    printf("Abierto\n");
    fclose(in);
    return 0;
}
```
:::

:::concepto | 6 | Leer datos hasta el fin del archivo | Elementos aislados, Atención dividida
`fscanf` funciona como `scanf` y **devuelve cuántos datos leyó**: 1 si leyó un número, 0 si encontró algo que no era número, `EOF` si ya no hay nada. Por eso el patrón es **leer en la condición del ciclo**:

```txt file=numeros.txt
12 7 25
9
31 4
```

```c run title="leer_datos.c"
#include <stdio.h>
int main(void)
{
    FILE *in = fopen("numeros.txt", "r");
    if (in == NULL) { printf("No se pudo abrir\n"); return 1; }
    int x, suma = 0, n = 0;
    while (fscanf(in, "%d", &x) == 1)       //> Lee mientras haya un número; espacios y saltos se ignoran
    {
        suma += x;
        n++;
    }
    fclose(in);
    printf("%d numeros, suma %d, promedio %.2f\n", n, suma, (double)suma / n);
    return 0;
}
```
:::

:::concepto | 7 | Leer línea por línea con `fgets` | Elementos aislados, Atención dividida
Cuando cada línea es una unidad (un nombre con espacios, un mensaje), se usa `fgets` (Tema 12), que devuelve `NULL` cuando ya no hay más líneas:

```txt file=lista.txt
Ana Sofia Lopez
Luis Perez
Eva Maria Rios
```

```c run title="leer_lineas.c"
#include <stdio.h>
#include <string.h>
int main(void)
{
    FILE *in = fopen("lista.txt", "r");
    if (in == NULL) return 1;
    char linea[100];
    int num = 1;
    while (fgets(linea, sizeof linea, in) != NULL)    //> Lee una línea completa en cada vuelta
    {
        linea[strcspn(linea, "\n")] = '\0';           //> Quita el salto de línea
        printf("%d. %s (%zu caracteres)\n", num++, linea, strlen(linea));
    }
    fclose(in);
    return 0;
}
```
:::

:::concepto | 8 | Ruta B · Registros con campos (CSV) | Elementos aislados, Reversión de la experiencia
En un archivo CSV cada línea es un **registro** y los **campos** se separan con comas. Se lee la línea completa con `fgets` y luego se separa con `sscanf`, que aplica un formato de `scanf` **a una cadena**. El conjunto `%49[^,]` lee «todo lo que no sea coma» (así el nombre puede tener espacios):

```txt file=alumnos.csv
101,Ana Lopez,9.2
102,Luis Perez,7.8
103,Eva Rios,8.5
```

```c run title="csv.c"
#include <stdio.h>
typedef struct { int id; char nombre[50]; double promedio; } Alumno;
int main(void)
{
    FILE *in = fopen("alumnos.csv", "r");
    if (in == NULL) return 1;
    char linea[120];
    while (fgets(linea, sizeof linea, in) != NULL)
    {
        Alumno a;
        if (sscanf(linea, "%d,%49[^,],%lf", &a.id, a.nombre, &a.promedio) == 3)   //> Tres campos leídos
            printf("%s [%d]: %.1f\n", a.nombre, a.id, a.promedio);
    }
    fclose(in);
    return 0;
}
```
Comparar el resultado de `sscanf` con 3 descarta líneas mal formadas (o vacías) en lugar de procesar basura.
:::

:::concepto | 9 | Ruta B · Archivos binarios con `fwrite` y `fread` | Elementos aislados, Reversión de la experiencia
En modo binario (`"wb"`, `"rb"`) se copian los **bytes** de la memoria tal cual: un arreglo de estructuras completo se guarda con una sola llamada.

```c run title="binario.c"
#include <stdio.h>
typedef struct { int id; double promedio; } Registro;
int main(void)
{
    Registro r[3] = {{101, 9.2}, {102, 7.8}, {103, 8.5}};
    FILE *f = fopen("alumnos.dat", "wb");          //> "wb": escribir en binario
    if (f == NULL) return 1;
    size_t escritos = fwrite(r, sizeof r[0], 3, f);  //> Desde dónde, tamaño de uno, cuántos, a qué archivo
    fclose(f);
    Registro leidos[3];
    f = fopen("alumnos.dat", "rb");
    if (f == NULL) return 1;
    size_t n = fread(leidos, sizeof leidos[0], 3, f);  //> Devuelve cuántos registros leyó
    fclose(f);
    printf("%zu escritos, %zu leidos; el segundo: %d %.1f\n", escritos, n, leidos[1].id, leidos[1].promedio);
    printf("El archivo mide %zu bytes\n", 3 * sizeof(Registro));
    return 0;
}
```
Es rápido y exacto, pero el archivo no se puede leer con un editor y depende de la computadora (tamaño de los tipos, orden de los bytes). Para compartir datos entre programas, el texto (y el CSV) suele ser mejor opción.
:::

## 1.2 Ejemplo resuelto: registro de calificaciones en archivo

:::ejemplo | Escribir registros y leerlos de nuevo | Ejemplo resuelto, Atención dividida
**Problema.** Capturar el nombre (una palabra) y la calificación de `n` alumnos, guardarlos en `calificaciones.txt` (un alumno por línea) y, después, **volver a abrir** el archivo para leerlo y mostrar cada registro, el promedio y el mejor alumno.

**A. Algoritmo:** 1) Abrir el archivo para escribir y verificar. 2) Para cada alumno: leer del teclado y escribir en el archivo. 3) Cerrar. 4) Abrir para leer y verificar. 5) Mientras se pueda leer un registro: mostrarlo, acumular y buscar el mejor. 6) Cerrar y mostrar resultados.

**B. Pseudocódigo**

```pseudo
Algoritmo CalificacionesArchivo
    Abrir "calificaciones.txt" para escribir
    Leer n
    Para i <- 1 Hasta n Hacer
        Leer nombre, cal
        Escribir en archivo nombre, cal
    FinPara
    Cerrar archivo
    Abrir "calificaciones.txt" para leer
    Mientras se pueda leer nombre, cal Hacer
        suma <- suma + cal
        cuantos <- cuantos + 1
    FinMientras
    Cerrar archivo
    Escribir suma / cuantos
FinAlgoritmo
```

**C. Código en C**

```c run title="calificaciones_archivo.c" stdin="3\nAna 9.5\nLuis 7\nEva 8.5\n" showfile=calificaciones.txt
#include <stdio.h>
#include <string.h>
int main(void)
{
    FILE *out = fopen("calificaciones.txt", "w");    //> 1) Abrir para escribir
    if (out == NULL) { printf("Error al crear\n"); return 1; }
    int n;
    printf("Cuantos alumnos? ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)                      //> 2) Teclado → archivo
    {
        char nombre[30];
        double cal;
        scanf("%29s %lf", nombre, &cal);
        fprintf(out, "%s %.1f\n", nombre, cal);      //> Un registro por línea
    }
    fclose(out);                                     //> 3) Cerrar (se guarda en disco)

    FILE *in = fopen("calificaciones.txt", "r");     //> 4) Abrir para leer
    if (in == NULL) { printf("Error al abrir\n"); return 1; }
    char nombre[30], mejor[30] = "";
    double cal, suma = 0, max = -1;
    int cuantos = 0;
    while (fscanf(in, "%29s %lf", nombre, &cal) == 2)   //> 5) Archivo → programa: ¿se leyeron los 2 campos?
    {
        printf("%s\t%.1f\n", nombre, cal);
        suma += cal;
        cuantos++;
        if (cal > max) { max = cal; strcpy(mejor, nombre); }
    }
    fclose(in);                                      //> 6) Cerrar y reportar
    if (cuantos > 0)
        printf("Promedio: %.2f  Mejor: %s\n", suma / cuantos, mejor);
    return 0;
}
```

**D. Verificación.** El recuadro final muestra el archivo creado: tres líneas con el formato `nombre calificación`. El promedio (9.5 + 7 + 8.5) / 3 = 8.33 ✔. Si se ejecuta otra vez, el archivo se **sobrescribe** (modo `"w"`).
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.16; ranksep=0.3;
@term(a, "Archivo de texto\nFILE *f")
@proc(o, "fopen(\"x.txt\", \"w\")\nfprintf(f, …)")
@proc(m, "modos: \"w\" (sobrescribe)\n\"a\" (agrega) · \"r\" (lee)")
@proc(i, "fopen(\"x.txt\", \"r\")")
@proc(d, "while (fscanf(f, …) == n)\npor datos")
@proc(l, "while (fgets(s, tam, f))\npor líneas")
@hl(v, "if (f == NULL) … verificar\nfclose(f)")
@sub(c, "CSV: fgets + sscanf\nbinario: fwrite / fread")
a -> o -> m; a -> i; i -> d; i -> l; a -> v [style=dashed]; l -> c [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1
```c run title="plantillas_archivo.c" showfile=salida.txt
#include <stdio.h>
int main(void)
{
    // ESCRIBIR (crea o sobrescribe)
    FILE *out = fopen("salida.txt", "w");
    if (out == NULL) return 1;
    fprintf(out, "manzana 3\npera 5\n");
    fclose(out);
    // AGREGAR al final
    FILE *app = fopen("salida.txt", "a");
    if (app == NULL) return 1;
    fprintf(app, "uva 12\n");
    fclose(app);
    // LEER por datos
    FILE *in = fopen("salida.txt", "r");
    if (in == NULL) return 1;
    char fruta[20];
    int cant, total = 0;
    while (fscanf(in, "%19s %d", fruta, &cant) == 2) total += cant;
    fclose(in);
    printf("Total: %d\n", total);
    return 0;
}
```

| Quiero… | Patrón |
|---|---|
| Leer todos los números | `while (fscanf(in, "%d", &x) == 1) { … }` |
| Leer registros de varios campos | `while (fscanf(in, "%29s %d", n, &c) == 2) { … }` |
| Leer líneas completas | `while (fgets(linea, sizeof linea, in) != NULL) { … }` |
| Separar una línea CSV | `sscanf(linea, "%d,%49[^,],%lf", &id, nombre, &prom)` |
| Escribir una línea de texto | `fputs("texto\n", out);` |
| Borrar un registro | leer el original → escribir los que se quedan en `temp.txt` → `remove("orig.txt"); rename("temp.txt", "orig.txt");` |
| Ruta en Windows | `"C:\\datos\\x.txt"` (barras dobles) o `"C:/datos/x.txt"` |
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿Verifiqué con <code>if (f == NULL)</code> que el archivo se abrió?</li>
<li>¿Quiero sobrescribir (<code>"w"</code>) o agregar (<code>"a"</code>)?</li>
<li>¿Leo en la condición del ciclo y comparo con el número de datos esperados (<code>== 1</code>, <code>== 2</code>), en lugar de usar <code>while (!feof(in))</code>?</li>
<li>¿El formato con que escribo es el mismo con que después leo (separadores, orden de campos)?</li>
<li>¿Cerré el archivo con <code>fclose</code> antes de abrirlo de nuevo para leer?</li>
<li>¿Cada <code>fopen</code> exitoso tiene su <code>fclose</code>?</li>
<li>¿Revisé el archivo generado con un editor de texto?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) `while (!feof(in))`: el último dato se procesa dos veces.** `feof` solo se vuelve verdadero **después** de un intento fallido de lectura:

```txt file=tres.txt
10
20
30
```

```c run title="feof_bug.c"
#include <stdio.h>
int main(void)
{
    FILE *in = fopen("tres.txt", "r");
    if (in == NULL) return 1;
    int x, suma = 0;
    while (!feof(in))          //> Tras leer 30 aún no es fin (falta leer el salto final)
    {
        fscanf(in, "%d", &x);  //> Esta lectura falla, pero x conserva 30…
        suma += x;             //> …y se suma otra vez
    }
    fclose(in);
    printf("Suma: %d (deberia ser 60)\n", suma);
    return 0;
}
```
*Corrección:* `while (fscanf(in, "%d", &x) == 1) suma += x;`

**b) No verificar la apertura.** Si el archivo no existe, `fopen` devuelve `NULL` y el primer `fscanf(NULL, …)` detiene el programa con *segmentation fault*.

**c) Sobrescribir sin querer.** Abrir con `fopen("datos.txt", "w")` para «agregar» borra todo: usa `"a"`.

**d) Mezclar `fscanf` y `fgets`.** Después de `fscanf(in, "%d", &n)`, el `fgets` siguiente lee el resto de la línea (vacío): consume el salto pendiente o lee todo por líneas con `fgets` + `sscanf`.

**e) Ruta equivocada.** El archivo se busca en la carpeta de **ejecución**, que en algunos IDE no es la del `.c`. Usa `perror` para ver un mensaje claro cuando falla la apertura.

**f) Olvidar `fclose`.** Lo escrito puede quedarse en el búfer y no llegar al disco si el programa termina mal; además, cada sistema permite un número limitado de archivos abiertos a la vez.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Copiar un archivo en mayúsculas | Variabilidad
El mismo patrón (abrir dos archivos → leer → transformar → escribir), con otro propósito:

```c run title="mayusculas.c" showfile=LISTA.txt
#include <stdio.h>
#include <ctype.h>
int main(void)
{
    FILE *in = fopen("lista.txt", "r");
    FILE *out = fopen("LISTA.txt", "w");
    if (in == NULL || out == NULL) return 1;
    char linea[100];
    while (fgets(linea, sizeof linea, in) != NULL)
    {
        for (int i = 0; linea[i] != '\0'; i++) linea[i] = toupper(linea[i]);
        fputs(linea, out);         //> fputs escribe la cadena tal cual (con su '\n')
    }
    fclose(in);
    fclose(out);
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} Después de cada ejecución, **abre el archivo** en un editor y comprueba su contenido.

:::tarea A | T1. Bitácora de temperaturas: ejemplo y gemelo | 25 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia:** cada ejecución **agrega** lecturas a la bitácora y luego muestra el historial completo.

```txt file=temperaturas.txt
lunes 21.5
martes 23.0
```

```c run title="bitacora.c" stdin="miercoles 24.5\njueves 22.0\nfin 0\n" showfile=temperaturas.txt
#include <stdio.h>
#include <string.h>
int main(void)
{
    FILE *out = fopen("temperaturas.txt", "a");      //> "a": conserva las lecturas anteriores
    if (out == NULL) return 1;
    char dia[20];
    double t;
    printf("Dia y temperatura (fin 0 para terminar): ");
    while (scanf("%19s %lf", dia, &t) == 2 && strcmp(dia, "fin") != 0)
    {
        fprintf(out, "%s %.1f\n", dia, t);
        printf("Dia y temperatura (fin 0 para terminar): ");
    }
    fclose(out);                                      //> Cerrar antes de releer
    FILE *in = fopen("temperaturas.txt", "r");
    if (in == NULL) return 1;
    double suma = 0;
    int n = 0;
    while (fscanf(in, "%19s %lf", dia, &t) == 2) { suma += t; n++; }
    fclose(in);
    printf("%d lecturas en total, promedio %.2f\n", n, suma / n);
    return 0;
}
```

**Paso 2 · Gemelo.** Programa un **diario de gastos**: cada ejecución agrega gastos (`concepto monto`) a `gastos.txt` hasta escribir `fin 0`, y después muestra el total acumulado de **todos** los gastos guardados y el gasto más alto.

:::solucion | T1
```txt file=gastos.txt
cafe 35
```

```c run title="gastos.c" stdin="comida 120\npasaje 18\nfin 0\n" showfile=gastos.txt
#include <stdio.h>
#include <string.h>
int main(void)
{
    FILE *out = fopen("gastos.txt", "a");
    if (out == NULL) return 1;
    char c[30], cmax[30] = "";
    double m;
    while (scanf("%29s %lf", c, &m) == 2 && strcmp(c, "fin") != 0)
        fprintf(out, "%s %.2f\n", c, m);
    fclose(out);
    FILE *in = fopen("gastos.txt", "r");
    if (in == NULL) return 1;
    double total = 0, max = 0;
    while (fscanf(in, "%29s %lf", c, &m) == 2)
    {
        total += m;
        if (m > max) { max = m; strcpy(cmax, c); }
    }
    fclose(in);
    printf("Total: $%.2f  Mayor: %s ($%.2f)\n", total, cmax, max);
    return 0;
}
```
:::
:::

:::tarea A | T2. Estadísticas de un archivo de puntajes (completa con pistas) | 20 min | Problema por completar
```txt file=puntajes.txt
340 125 980 410
75 660
512 290 830
```

```c blank title="puntajes.c"
#include <stdio.h>
int main(void)
{
    FILE *in = __1__;                   // 1: abrir puntajes.txt para LEER
    if (__2__)                          // 2: ¿fallo la apertura?
    {
        printf("No se encontro el archivo\n");
        return 1;
    }
    int p, n = 0, suma = 0, mayor = 0;
    while (__3__)                       // 3: leer un puntaje en la condicion
    {
        suma += p;
        n++;
        if (p > mayor) mayor = p;
    }
    __4__;                              // 4: cerrar
    printf("%d puntajes, promedio %d, mayor %d\n", n, suma / n, mayor);
    return 0;
}
```

:::solucion | T2
{{c:1}} `fopen("puntajes.txt", "r")` · {{c:2}} `in == NULL` · {{c:3}} `fscanf(in, "%d", &p) == 1` · {{c:4}} `fclose(in)`

```c run title="puntajes.c"
#include <stdio.h>
int main(void)
{
    FILE *in = fopen("puntajes.txt", "r");
    if (in == NULL)
    {
        printf("No se encontro el archivo\n");
        return 1;
    }
    int p, n = 0, suma = 0, mayor = 0;
    while (fscanf(in, "%d", &p) == 1)
    {
        suma += p;
        n++;
        if (p > mayor) mayor = p;
    }
    fclose(in);
    printf("%d puntajes, promedio %d, mayor %d\n", n, suma / n, mayor);
    return 0;
}
```
:::
:::

:::tarea AB | T3. Contar líneas, palabras y caracteres (completa sin pistas) | 25 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Como el comando `wc` de Linux: para un archivo de texto, cuenta líneas, palabras y caracteres (sin contar los saltos de línea), y muestra la línea más larga.

```txt file=poema.txt
Programar es pensar
paso a paso,
con paciencia y con calma,
hasta que el codigo compila.
```

```c blank title="contar.c"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(void)
{
    FILE *in = fopen("poema.txt", "r");
    if (__1__) return 1;
    char linea[200], larga[200] = "";
    int lineas = 0, palabras = 0, caracteres = 0;
    while (__2__)
    {
        linea[strcspn(linea, "\n")] = '\0';
        lineas++;
        caracteres += __3__;
        if (strlen(linea) > strlen(larga)) __4__;
        for (int i = 0; linea[i] != '\0'; i++)
            if (__5__) palabras++;
    }
    fclose(in);
    printf("%d lineas, %d palabras, %d caracteres\n", lineas, palabras, caracteres);
    printf("Mas larga: %s\n", larga);
    return 0;
}
```

:::solucion | T3
{{c:1}} `in == NULL` · {{c:2}} `fgets(linea, sizeof linea, in) != NULL` · {{c:3}} `strlen(linea)` · {{c:4}} `strcpy(larga, linea)` · {{c:5}} `!isspace(linea[i]) && (i == 0 || isspace(linea[i - 1]))`

```c run title="contar.c"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(void)
{
    FILE *in = fopen("poema.txt", "r");
    if (in == NULL) return 1;
    char linea[200], larga[200] = "";
    int lineas = 0, palabras = 0, caracteres = 0;
    while (fgets(linea, sizeof linea, in) != NULL)
    {
        linea[strcspn(linea, "\n")] = '\0';
        lineas++;
        caracteres += strlen(linea);
        if (strlen(linea) > strlen(larga)) strcpy(larga, linea);
        for (int i = 0; linea[i] != '\0'; i++)
            if (!isspace(linea[i]) && (i == 0 || isspace(linea[i - 1]))) palabras++;
    }
    fclose(in);
    printf("%d lineas, %d palabras, %d caracteres\n", lineas, palabras, caracteres);
    printf("Mas larga: %s\n", larga);
    return 0;
}
```
El conteo de palabras reutiliza la idea del Tema 12: contar **inicios** de palabra.
:::
:::

:::tarea AB | T4. Inventario CSV y reporte de surtido (problema convencional) | 35 min | Variabilidad
**Contexto.** El archivo `productos.csv` tiene `codigo,nombre,precio,existencias`. Lee todos los productos, muestra el valor total del inventario y **genera** el archivo `surtir.txt` con los productos que tienen menos de 10 piezas (código, nombre y cuántas faltan para llegar a 25).

```txt file=productos.csv
101,Cuaderno profesional,45.5,30
102,Pluma azul,12,8
103,Mochila escolar,520,3
104,Regla 30 cm,18,40
105,Calculadora,350,6
```

:::solucion | T4
```c run title="inventario_csv.c" showfile=surtir.txt
#include <stdio.h>
int main(void)
{
    FILE *in = fopen("productos.csv", "r");
    FILE *out = fopen("surtir.txt", "w");
    if (in == NULL || out == NULL) { printf("Error de archivos\n"); return 1; }
    char linea[120], nom[50];
    int cod, exist, surtir = 0;
    double precio, total = 0;
    while (fgets(linea, sizeof linea, in) != NULL)
    {
        if (sscanf(linea, "%d,%49[^,],%lf,%d", &cod, nom, &precio, &exist) != 4)
            continue;                                   // linea mal formada: se ignora
        total += precio * exist;
        if (exist < 10)
        {
            fprintf(out, "%d %s: faltan %d\n", cod, nom, 25 - exist);
            surtir++;
        }
    }
    fclose(in);
    fclose(out);
    printf("Valor del inventario: $%.2f\n%d productos por surtir (ver surtir.txt)\n", total, surtir);
    return 0;
}
```
:::
:::

:::tarea A | T5. Todo lo que dice un archivo de ventas (solución libre) | 25 min | Solución libre
**Contexto.** El archivo `ventas.txt` tiene, por línea, `vendedor mes monto`. **No hay preguntas específicas:** escribe un programa que obtenga **toda la información que puedas** (total, promedio, venta mayor y menor, cuántas ventas hizo cada vendedor, el mes con más ventas…).

```txt file=ventas.txt
ana 1 1200
luis 1 800
ana 2 1500
eva 2 950
luis 3 1700
ana 3 600
eva 3 1100
```

:::solucion | T5
Una exploración posible:

```c run title="explora_ventas.c"
#include <stdio.h>
#include <string.h>
int main(void)
{
    FILE *in = fopen("ventas.txt", "r");
    if (in == NULL) return 1;
    char v[20], vMax[20] = "";
    int mes, n = 0, porMes[13] = {0}, cAna = 0, cLuis = 0, cEva = 0;
    double monto, total = 0, mx = -1, mn = 1e18;
    double totalMes[13] = {0};
    while (fscanf(in, "%19s %d %lf", v, &mes, &monto) == 3)
    {
        n++; total += monto; totalMes[mes] += monto; porMes[mes]++;
        if (monto > mx) { mx = monto; strcpy(vMax, v); }
        if (monto < mn) mn = monto;
        if (strcmp(v, "ana") == 0) cAna++;
        else if (strcmp(v, "luis") == 0) cLuis++;
        else if (strcmp(v, "eva") == 0) cEva++;
    }
    fclose(in);
    int mejorMes = 1;
    for (int m = 2; m <= 12; m++) if (totalMes[m] > totalMes[mejorMes]) mejorMes = m;
    printf("%d ventas, total %.2f, promedio %.2f\n", n, total, total / n);
    printf("Mayor %.2f (%s), menor %.2f\n", mx, vMax, mn);
    printf("Ventas por vendedor: ana %d, luis %d, eva %d\n", cAna, cLuis, cEva);
    printf("Mejor mes: %d ($%.2f, %d ventas)\n", mejorMes, totalMes[mejorMes], porMes[mejorMes]);
    return 0;
}
```
:::
:::

:::tarea B | T6. Cuatro errores con archivos (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
**Explica** qué ocurre en cada fragmento y por qué; propón la corrección.

```c blank title="archivos_bug.c"
// A: el usuario quiere AGREGAR un registro a clientes.txt
FILE *f = fopen("clientes.txt", "w");
fprintf(f, "Nuevo cliente\n");

// B: sumar los numeros de datos.txt
FILE *in = fopen("datos.txt", "r");
int x, s = 0;
while (!feof(in)) { fscanf(in, "%d", &x); s += x; }

// C: escribir y luego leer el mismo archivo
FILE *o = fopen("temp.txt", "w");
fprintf(o, "%d", 42);
FILE *i = fopen("temp.txt", "r");
int y; fscanf(i, "%d", &y);           // y no vale 42

// D: leer la cantidad y luego un nombre con espacios
FILE *g = fopen("alumno.txt", "r");   // contiene: "3\nAna Lopez\n"
int n; char nombre[40];
fscanf(g, "%d", &n);
fgets(nombre, sizeof nombre, g);      // nombre queda vacio ("\n")
```

{{lineas:5}}

:::solucion | T6
**A:** el modo `"w"` **borra** el archivo: se pierden todos los clientes. → `fopen("clientes.txt", "a")` (y verificar `NULL` y cerrar). **B:** con `!feof(in)` el último número se suma dos veces; además no se verificó la apertura (si el archivo no existe, `fscanf(NULL, …)` detiene el programa). → `if (in == NULL) …; while (fscanf(in, "%d", &x) == 1) s += x;`. **C:** el 42 puede seguir en el **búfer** de `o` (aún no se escribió al disco) cuando `i` lee. → `fclose(o);` antes de abrir para leer. **D:** `fscanf` deja el `'\n'` de la primera línea; `fgets` lee esa línea vacía. → consumir el salto (`fgetc(g)`) o leer ambas líneas con `fgets` y convertir la primera con `sscanf`.
:::
:::

:::tarea B | T7. ¿Qué contiene el archivo? (imaginación) | 20 min | Imaginación
**Sin ejecutar**, imagina el contenido de `log.txt` después de cada línea y escribe el contenido final. (Por brevedad, este ejemplo no verifica `NULL`.)

```c check title="imagina_log.c"
#include <stdio.h>
int main(void)
{
    FILE *f;
    f = fopen("log.txt", "w"); fprintf(f, "A\n");    fclose(f);
    f = fopen("log.txt", "a"); fprintf(f, "B\nC\n"); fclose(f);
    f = fopen("log.txt", "w"); fprintf(f, "D\n");    fclose(f);
    f = fopen("log.txt", "a"); fprintf(f, "E\n");    fclose(f);
    f = fopen("log.txt", "a"); fprintf(f, "F");      fclose(f);
    return 0;
}
```

{{lineas:3}}

:::solucion | T7
Línea 1 → `A`. Línea 2 (agrega) → `A B C`. Línea 3 (modo `"w"`: **borra**) → `D`. Líneas 4 y 5 (agregan) → `D E F`. El archivo final tiene tres líneas: `D`, `E` y `F` (la última sin salto de línea).

```c run title="imagina_log.c" out=0 showfile=log.txt
#include <stdio.h>
int main(void)
{
    FILE *f;
    f = fopen("log.txt", "w"); fprintf(f, "A\n");    fclose(f);
    f = fopen("log.txt", "a"); fprintf(f, "B\nC\n"); fclose(f);
    f = fopen("log.txt", "w"); fprintf(f, "D\n");    fclose(f);
    f = fopen("log.txt", "a"); fprintf(f, "E\n");    fclose(f);
    f = fopen("log.txt", "a"); fprintf(f, "F");      fclose(f);
    return 0;
}
```
:::
:::

:::tarea AB | T8. Registro de estudiantes con archivo (reto colaborativo) | 45 min | Memoria colectiva de trabajo, Variabilidad
**Contexto.** Como en la Figura 7.14 de la tesis («Sistema de registro de estudiantes»): un programa que guarda estudiantes (matrícula, nombre de una palabra, calificación) en `estudiantes.txt` y permite **alta**, **consulta** por matrícula, **listado** y **baja**. Los datos deben persistir entre ejecuciones.

:::colab | Organización
Equipos de 4, niveles mezclados. Primero acuerden el **formato** del archivo (una línea por estudiante: `matricula nombre calificacion`).
- **Integrante 1:** `void alta(…)` con modo `"a"` (rechaza matrículas repetidas consultando el archivo).
- **Integrante 2:** `bool consulta(int mat, bool mostrar)` y `void listado(void)`.
- **Integrante 3:** `bool baja(int mat)`: copia a `temp.txt` todos menos el buscado y reemplaza el original (`remove` / `rename`, también de `<stdio.h>`).
- **Integrante 4:** menú y pruebas: alta de 3, baja de 1, listado; volver a ejecutar y comprobar que los datos siguen ahí.
:::

:::solucion | T8
```txt file=estudiantes.txt
2001 Ana 9.1
2002 Luis 7.4
```

```c run title="registro_estudiantes.c" stdin="1 2003 Eva 8.8\n1 2001 Repetido 5\n2 2002\n4 2002\n3\n0\n" showfile=estudiantes.txt
#include <stdio.h>
#include <stdbool.h>
#define ARCH "estudiantes.txt"

bool consulta(int mat, bool mostrar)
{
    FILE *in = fopen(ARCH, "r");
    if (in == NULL) return false;
    int m; char n[30]; double c;
    bool hallado = false;
    while (!hallado && fscanf(in, "%d %29s %lf", &m, n, &c) == 3)
        if (m == mat)
        {
            hallado = true;
            if (mostrar) printf("  %d %s %.1f\n", m, n, c);
        }
    fclose(in);
    return hallado;
}
void alta(int mat, const char nom[], double cal)
{
    if (consulta(mat, false)) { printf("  Matricula repetida\n"); return; }
    FILE *out = fopen(ARCH, "a");
    if (out == NULL) return;
    fprintf(out, "%d %s %.1f\n", mat, nom, cal);
    fclose(out);
    printf("  Alta de %s\n", nom);
}
void listado(void)
{
    FILE *in = fopen(ARCH, "r");
    if (in == NULL) return;
    int m; char n[30]; double c;
    while (fscanf(in, "%d %29s %lf", &m, n, &c) == 3) printf("  %d %s %.1f\n", m, n, c);
    fclose(in);
}
bool baja(int mat)
{
    FILE *in = fopen(ARCH, "r");
    FILE *tmp = fopen("temp.txt", "w");
    if (in == NULL || tmp == NULL) return false;
    int m; char n[30]; double c;
    bool hallado = false;
    while (fscanf(in, "%d %29s %lf", &m, n, &c) == 3)
    {
        if (m == mat) hallado = true;
        else fprintf(tmp, "%d %s %.1f\n", m, n, c);
    }
    fclose(in);
    fclose(tmp);
    remove(ARCH);
    rename("temp.txt", ARCH);
    return hallado;
}
int main(void)
{
    int op;
    while (scanf("%d", &op) == 1 && op != 0)
    {
        int mat; char nom[30]; double cal;
        switch (op)
        {
            case 1: scanf("%d %29s %lf", &mat, nom, &cal); alta(mat, nom, cal); break;
            case 2: scanf("%d", &mat); if (!consulta(mat, true)) printf("  No existe\n"); break;
            case 3: listado(); break;
            case 4: scanf("%d", &mat); printf(baja(mat) ? "  Baja realizada\n" : "  No existe\n"); break;
        }
    }
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Modificar un registro dentro de un archivo | Modalidad, Ejemplo resuelto
*Guion segmentado (≈ 3 min), con el archivo original y el temporal en pantalla, lado a lado.*

**Problema:** «En `precios.txt` (producto y precio por línea) aumentar un 10 % el precio de un producto dado».

**Segmento 1 — Por qué no «editar en su lugar».** {{como}} Descarto escribir directamente en medio del archivo de texto. {{porque}} En un archivo de texto, «45.50» y «50.05» pueden ocupar distinto número de caracteres que el precio original: si sobrescribo en el lugar, piso el inicio de la línea siguiente.

**Segmento 2 — Leer uno, escribir otro.** {{como}} Abro `precios.txt` con `"r"` y `temp.txt` con `"w"`; copio cada registro tal cual, excepto el buscado, que escribo con su nuevo precio. {{porque}} Así el archivo nuevo se construye completo y correcto, línea por línea.

**Segmento 3 — Reemplazar con seguridad.** {{como}} Cierro **ambos** archivos con `fclose` y solo entonces hago `remove("precios.txt")` y `rename("temp.txt", "precios.txt")`. {{porque}} Si borrara el original antes de terminar de escribir el temporal y algo fallara, perdería los datos.

**Segmento 4 — Avisar y verificar.** {{como}} Llevo una bandera `encontrado` para avisar si el producto no existía y, al final, muestro el archivo resultante. {{porque}} Un programa que modifica datos debe confirmar lo que hizo; y ver el archivo final es la prueba definitiva.

{{salto}}

```txt file=precios.txt
lapiz 8
cuaderno 45.5
mochila 520
```

```c run title="modificar.c" stdin="cuaderno\n" showfile=precios.txt
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
int main(void)
{
    char buscado[30];
    printf("Producto a aumentar: ");
    scanf("%29s", buscado);
    FILE *in = fopen("precios.txt", "r");
    FILE *tmp = fopen("temp.txt", "w");
    if (in == NULL || tmp == NULL) return 1;
    char p[30];
    double precio;
    bool encontrado = false;
    while (fscanf(in, "%29s %lf", p, &precio) == 2)
    {
        if (strcmp(p, buscado) == 0) { precio *= 1.10; encontrado = true; }
        fprintf(tmp, "%s %.2f\n", p, precio);
    }
    fclose(in);
    fclose(tmp);
    remove("precios.txt");
    rename("temp.txt", "precios.txt");
    printf(encontrado ? "Precio actualizado\n" : "No se encontro el producto\n");
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. ¿Qué diferencia hay entre memoria principal y memoria secundaria?
2. Menciona una diferencia entre un archivo de texto y uno binario.
3. ¿Qué cabecera declara `fopen`, `fprintf` y `fclose`?
4. ¿Qué ocurre si abres con `fopen("x.txt", "w")` un archivo que ya tenía datos?
5. ¿Cómo se abre un archivo para agregar al final?
6. ¿Cómo se verifica que un archivo se abrió correctamente?
7. ¿Por qué se recomienda `while (fscanf(in, "%d", &x) == 1)` en lugar de `while (!feof(in))`?
8. ¿Qué función lee una línea completa de un archivo? ¿Qué devuelve cuando ya no hay más líneas?
9. ¿Qué devuelve `fscanf`?
10. ¿Para qué sirve `sscanf` al leer un CSV?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Analiza la salida** si `nums.txt` contiene `4 8 15 16 23 42`:

```c check title="p1.c"
#include <stdio.h>
int main(void)
{
    FILE *in = fopen("nums.txt", "r");
    if (in == NULL) return 1;
    int x, pares = 0, ultimo = 0;
    while (fscanf(in, "%d", &x) == 1)
    {
        if (x % 2 == 0) pares++;
        ultimo = x;
    }
    fclose(in);
    printf("%d %d\n", pares, ultimo);
    return 0;
}
```

**P2. Corrige:** `FILE *out = fopen("reporte.txt", "r"); fprintf(out, "Total: %d\n", t); while (!feof(out)) {...}`

**P3. Implementa** un programa que lea `temps.txt` (un número por línea) y escriba en `alertas.txt` solo las mayores de 30, numeradas.

**P4. Desarrolla** un programa de manipulación de datos: lee `alumnos.csv` (`id,nombre,promedio`), genera `aprobados.csv` y `reprobados.csv` (promedio ≥ 6 o < 6) con el mismo formato e informa cuántos registros escribió en cada uno.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Escribo archivos creando o agregando según lo que necesito.</li>
<li>Leo archivos por datos y por líneas sin procesar dos veces el último dato.</li>
<li>Verifico la apertura (<code>NULL</code>) y cierro los archivos (<code>fclose</code>) en el momento correcto.</li>
<li>Proceso registros con campos y hago bajas o modificaciones con un archivo temporal.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 La principal (RAM) es rápida pero se borra al terminar el programa o apagar; la secundaria (disco, USB) conserva los datos · 2 El de texto contiene caracteres legibles y se abre con un editor; el binario guarda bytes tal como están en memoria · 3 `<stdio.h>` · 4 Se borra el contenido anterior (modo `"w"`) · 5 `fopen("x.txt", "a")` · 6 `if (f == NULL)` (y `perror` para ver la causa) · 7 Porque `feof` se vuelve verdadero solo después de una lectura fallida y el último dato se procesaría dos veces; el valor de retorno de `fscanf` dice si la lectura funcionó · 8 `fgets(cadena, tamaño, archivo)`; devuelve `NULL` · 9 Cuántos datos logró leer y guardar, o `EOF` si se acabó el archivo antes de leer alguno · 10 Para separar los campos de una línea ya leída con `fgets`, con un formato como `"%d,%49[^,],%lf"`.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.**

```txt file=nums.txt
4 8 15 16 23 42
```

```c run title="p1.c"
#include <stdio.h>
int main(void)
{
    FILE *in = fopen("nums.txt", "r");
    if (in == NULL) return 1;
    int x, pares = 0, ultimo = 0;
    while (fscanf(in, "%d", &x) == 1)
    {
        if (x % 2 == 0) pares++;
        ultimo = x;
    }
    fclose(in);
    printf("%d %d\n", pares, ultimo);
    return 0;
}
```

**P2.** Para escribir se abre con `"w"` (no `"r"`); verificar que `out` no sea `NULL`; el ciclo con `feof` sobra (y no tiene sentido al escribir); cerrar con `fclose(out)`.

**P3.**

```txt file=temps.txt
28.5
31.2
29.9
33.0
30.1
```

```c run title="alertas.c" showfile=alertas.txt
#include <stdio.h>
int main(void)
{
    FILE *in = fopen("temps.txt", "r");
    FILE *out = fopen("alertas.txt", "w");
    if (in == NULL || out == NULL) return 1;
    double t;
    int k = 0;
    while (fscanf(in, "%lf", &t) == 1)
        if (t > 30) fprintf(out, "%d. %.1f\n", ++k, t);
    fclose(in);
    fclose(out);
    return 0;
}
```

**P4.** Se reutiliza el patrón del concepto 8 (CSV con `fgets` + `sscanf`) y dos archivos abiertos con `"w"`; por cada línea se decide en cuál escribir con `if (promedio >= 6)` y se lleva un contador por archivo.
:::
