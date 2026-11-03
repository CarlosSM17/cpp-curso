---
num: "16"
archivo: "Tema16_Archivos_de_texto"
titulo: "Almacenamiento en memoria secundaria: archivos de texto"
corto: "Archivos"
lema: "Lo que está en variables se borra al cerrar el programa; lo que está en un archivo te espera mañana."
duracion: "5 h · 3 sesiones"
previos: "Tema 06 (ciclos y centinelas), Tema 12 (cadenas y getline), Tema 13 (estructuras)."
fuentes:
  - "Betancourt Uscátegui, J. F. y Polanco Guzmán, I. Y. (2021). *115 ejercicios resueltos de programación C++*. Cap. 12: Almacenamiento en memoria secundaria: ficheros o archivos (§12.1 Archivos de texto y binarios, §12.2 Flujos de entrada y salida asociados a archivos, §12.3 Entrada de datos desde archivos de texto, §12.4 Ejercicios: visualización, consulta, eliminación y adición de registros)."
  - "Lospinoso, J. (2019). *C++ Crash Course*. Cap. 16 «Streams»: Stream Classes, Stream State, Buffering and Flushing, Manipulators, String Streams, File Streams (opening files, modes)."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §7.5: segundo estudio piloto (aplicación web CLT4BP) sobre manejo de archivos de texto en C; Figuras 7.13 y 7.14 (tareas de configuración y registro de estudiantes en archivos)."
objetivos:
  A:
    - "Explicar qué es un archivo, la diferencia entre memoria principal y secundaria y entre archivos de texto y binarios."
    - "Escribir datos en archivos de texto con `ofstream`, creando, sobrescribiendo o agregando (`ios::app`)."
    - "Leer archivos de texto con `ifstream` por datos (`>>`) y por líneas (`getline`) hasta el fin del archivo."
    - "Verificar que el archivo se abrió y cerrarlo correctamente."
  B:
    - "Procesar registros con campos separados por comas usando `getline` con delimitador y `stringstream`."
    - "Implementar consulta, alta, baja y modificación de registros (archivo temporal + reescritura)."
    - "Interpretar el estado del flujo (`good`, `fail`, `eof`) para leer de forma robusta."
    - "Comparar los flujos de C++ con la API de C (`FILE*`, `fopen`, `fprintf`, `fclose`) del segundo piloto de la tesis."
efectos:
  soporte:
    - ["Elementos aislados", "Archivo → flujos → escribir → modos → verificar → leer datos → leer líneas → registros con campos → API de C."]
    - ["Atención dividida", "El contenido real del archivo se muestra junto al código que lo produce o lo lee."]
    - ["Ejemplo resuelto", "Registro de calificaciones: escribir el archivo y leerlo de nuevo para calcular el promedio."]
    - ["Variabilidad", "Archivos de bitácora, inventario, ventas, configuración y registro escolar."]
  procedimental:
    - ["Variabilidad", "Plantillas de lectura/escritura para distintos formatos."]
    - ["Autoexplicación", "Errores clásicos (`eof`, apertura no verificada) planteados como «¿por qué se repite el último dato?»."]
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
    A: "`ofstream`, `ifstream`, `ios::app`, lectura por datos y por líneas, verificación de apertura."
    B: "Registros CSV, `stringstream`, bajas con archivo temporal, estado del flujo, API de C."
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
  - ["flujo", "stream", "Canal de datos entre el programa y un dispositivo o archivo."]
  - ["flujo de entrada de archivo", "input file stream (`ifstream`)", "Lee datos desde un archivo."]
  - ["flujo de salida de archivo", "output file stream (`ofstream`)", "Escribe datos en un archivo."]
  - ["modo de apertura", "open mode", "`ios::out` (sobrescribir), `ios::app` (agregar), `ios::in` (leer)."]
  - ["fin de archivo", "end of file (EOF)", "Situación en la que ya no quedan datos por leer."]
  - ["estado del flujo", "stream state", "Indicadores `good`, `fail`, `eof`, `bad`."]
  - ["búfer", "buffer", "Memoria intermedia donde se acumulan datos antes de escribirse."]
  - ["registro", "record", "Conjunto de campos de una misma entidad (una línea de un CSV)."]
  - ["valores separados por comas", "CSV (comma-separated values)", "Formato de texto con un registro por línea y campos separados por comas."]
  - ["flujo de cadena", "string stream (`stringstream`)", "Flujo que lee o escribe sobre un `string`."]
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
Las partidas guardadas, los archivos de configuración (como el `config.txt` del segundo piloto de la tesis), las bitácoras de un servidor, las hojas de cálculo exportadas en CSV y los registros de un sensor Arduino en una memoria SD son archivos de texto. Saber leerlos y escribirlos permite que tus programas **recuerden** datos y **compartan** información con otros programas. {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | Archivos de texto y binarios | Elementos aislados
| | Archivo de **texto** | Archivo **binario** |
|---|---|---|
| Contenido | caracteres legibles (`1`, `2`, `.`, `5`) | bytes tal como están en memoria |
| Se puede abrir con un editor | sí | no (se ven símbolos raros) |
| Ejemplo | `.txt`, `.csv`, `.cpp`, `.html` | `.exe`, `.jpg`, `.mp3` |
| El número 12.5 ocupa | 4 caracteres | 8 bytes (un `double`) |

En este tema trabajaremos con archivos de **texto**, como Betancourt y Polanco (§12.1–12.3).
:::

:::concepto | 2 | Flujos: `cin`/`cout` ya eran flujos | Elementos aislados, Atención dividida
Un **flujo** (*stream*) es un canal de datos. `cout` es un flujo hacia la pantalla y `cin`, desde el teclado. La biblioteca `<fstream>` ofrece flujos hacia y desde **archivos** que se usan **con los mismos operadores** `<<` y `>>` (*C++ Crash Course*, cap. 16):

```dot w="85%"
rankdir=LR; nodesep=0.25; ranksep=0.45;
@io(t, "teclado")
@term(p, "Programa")
@io(s, "pantalla")
@file(fi, "datos.txt")
@file(fo, "reporte.txt")
t -> p [label=" cin >>"]; p -> s [label=" cout <<"];
fi -> p [label=" ifstream >>"]; p -> fo [label=" ofstream <<"];
```

| Clase | Para | Biblioteca |
|---|---|---|
| `ofstream` | escribir en un archivo | `<fstream>` |
| `ifstream` | leer de un archivo | `<fstream>` |
| `fstream` | leer y escribir | `<fstream>` |
:::

:::concepto | 3 | Escribir en un archivo con `ofstream` | Elementos aislados, Atención dividida
```cpp run title="escribir.cpp" showfile=saludo.txt
#include <iostream>
#include <fstream>                       //> Biblioteca de flujos de archivo
using namespace std;
int main()
{
    ofstream archivo("saludo.txt");      //> Abre (o crea) saludo.txt para escribir
    archivo << "Hola desde C++\n";       //> Igual que cout, pero va al archivo
    archivo << "Linea " << 2 << "\n";
    archivo.close();                     //> Cierra: asegura que todo se guarde en disco
    cout << "Archivo escrito\n";
    return 0;
}
```
El recuadro de abajo muestra el **contenido real** del archivo después de ejecutar el programa. El archivo queda en la **carpeta donde se ejecuta** el programa (en un IDE, normalmente la carpeta del proyecto).
:::

:::concepto | 4 | Modos de apertura: sobrescribir o agregar | Elementos aislados, Atención dividida
Por defecto, `ofstream` **borra** el contenido anterior. Para **agregar** al final se usa `ios::app` (*append*):

```cpp run title="modos.cpp" showfile=bitacora.txt
#include <fstream>
using namespace std;
int main()
{
    ofstream a("bitacora.txt");                  //> Modo normal: crea o BORRA y empieza de cero
    a << "inicio\n";
    a.close();
    ofstream b("bitacora.txt", ios::app);        //> Modo append: conserva lo que había y agrega al final
    b << "evento 1\n";
    b.close();
    ofstream c("bitacora.txt", ios::app);
    c << "evento 2\n";
    c.close();
    return 0;
}
```
:::

:::concepto | 5 | ¿Se abrió? Verificar siempre | Elementos aislados
Abrir puede fallar (el archivo no existe, no hay permisos, la ruta está mal). El flujo se evalúa como `false` si falló:

```cpp run rc title="verificar.cpp"
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream in("no_existe.txt");
    if (!in)                                  //> También: if (!in.is_open())
    {
        cout << "No se pudo abrir el archivo\n";
        return 1;                             //> Terminar (o pedir otro nombre)
    }
    cout << "Abierto\n";
    return 0;
}
```
:::

:::concepto | 6 | Leer datos hasta el fin del archivo | Elementos aislados, Atención dividida
`in >> x` devuelve el flujo; si la lectura falla (porque se acabó el archivo o el dato no es válido), el flujo se vuelve `false`. Por eso el patrón es **leer en la condición del ciclo**:

```txt file=numeros.txt
12 7 25
9
31 4
```

```cpp run title="leer_datos.cpp"
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream in("numeros.txt");
    if (!in) { cout << "No se pudo abrir\n"; return 1; }
    int x, suma = 0, n = 0;
    while (in >> x)                     //> Lee mientras haya un número; espacios y saltos se ignoran
    {
        suma += x;
        n++;
    }
    in.close();
    cout << n << " numeros, suma " << suma << ", promedio " << static_cast<double>(suma) / n << "\n";
    return 0;
}
```
:::

:::concepto | 7 | Leer línea por línea | Elementos aislados, Atención dividida
Cuando cada línea es una unidad (un nombre con espacios, un mensaje), se usa `getline`:

```txt file=lista.txt
Ana Sofia Lopez
Luis Perez
Eva Maria Rios
```

```cpp run title="leer_lineas.cpp"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    ifstream in("lista.txt");
    if (!in) return 1;
    string linea;
    int num = 1;
    while (getline(in, linea))              //> Lee una línea completa en cada vuelta
        cout << num++ << ". " << linea << " (" << linea.size() << " caracteres)\n";
    return 0;
}
```
:::

:::concepto | 8 | Ruta B · Registros con campos (CSV) | Elementos aislados, Reversión de la experiencia
En un archivo CSV cada línea es un **registro** y los **campos** se separan con comas. Se lee la línea completa y luego se separa con un `stringstream` (*C++ Crash Course*, cap. 16) y `getline` con delimitador:

```txt file=alumnos.csv
101,Ana Lopez,9.2
102,Luis Perez,7.8
103,Eva Rios,8.5
```

```cpp run title="csv.cpp"
#include <iostream>
#include <fstream>
#include <sstream>                              //> stringstream
#include <string>
using namespace std;
struct Alumno { int id; string nombre; double promedio; };
int main()
{
    ifstream in("alumnos.csv");
    if (!in) return 1;
    string linea;
    while (getline(in, linea))
    {
        stringstream ss(linea);                 //> Un flujo que lee DE la cadena
        string campo;
        Alumno a;
        getline(ss, campo, ',');  a.id = stoi(campo);         //> Hasta la primera coma
        getline(ss, a.nombre, ',');                            //> Hasta la segunda coma
        getline(ss, campo, ',');  a.promedio = stod(campo);   //> El resto
        cout << a.nombre << " [" << a.id << "]: " << a.promedio << "\n";
    }
    return 0;
}
```
:::

:::concepto | 9 | Ruta B · La misma idea con la API de C (segundo piloto de la tesis) | Elementos aislados, Reversión de la experiencia
El segundo estudio piloto de la tesis trabajó archivos en **C**. La lógica es idéntica; cambian los nombres:

| Tarea | C++ (`<fstream>`) | C (`<cstdio>`) |
|---|---|---|
| Abrir para escribir | `ofstream f("a.txt");` | `FILE* f = fopen("a.txt", "w");` |
| Abrir para agregar | `ofstream f("a.txt", ios::app);` | `fopen("a.txt", "a")` |
| Abrir para leer | `ifstream f("a.txt");` | `fopen("a.txt", "r")` |
| Verificar | `if (!f)` | `if (f == NULL)` |
| Escribir | `f << x << "\n";` | `fprintf(f, "%d\n", x);` |
| Leer | `f >> x` | `fscanf(f, "%d", &x)` |
| Cerrar | `f.close();` (o al salir del ámbito) | `fclose(f);` (obligatorio) |

```cpp run title="api_c.cpp" showfile=config.txt
#include <cstdio>
int main()
{
    FILE* f = fopen("config.txt", "w");
    if (f == NULL) return 1;
    fprintf(f, "nombre=Ana\nedad=%d\nlenguaje=%s\n", 17, "C++");
    fclose(f);
    f = fopen("config.txt", "r");
    char linea[100];
    while (fgets(linea, sizeof(linea), f) != NULL)
        printf("> %s", linea);
    fclose(f);
    return 0;
}
```
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

**C. Código en C++**

```cpp run title="calificaciones_archivo.cpp" stdin="3\nAna 9.5\nLuis 7\nEva 8.5\n" showfile=calificaciones.txt
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    ofstream out("calificaciones.txt");              //> 1) Abrir para escribir
    if (!out) { cout << "Error al crear\n"; return 1; }
    int n;
    cout << "Cuantos alumnos? ";
    cin >> n;
    for (int i = 0; i < n; i++)                      //> 2) Teclado → archivo
    {
        string nombre;
        double cal;
        cin >> nombre >> cal;
        out << nombre << " " << cal << "\n";         //> Un registro por línea
    }
    out.close();                                     //> 3) Cerrar (se guarda en disco)

    ifstream in("calificaciones.txt");               //> 4) Abrir para leer
    if (!in) { cout << "Error al abrir\n"; return 1; }
    string nombre, mejor;
    double cal, suma = 0, max = -1;
    int cuantos = 0;
    while (in >> nombre >> cal)                      //> 5) Archivo → programa, hasta el fin
    {
        cout << nombre << "\t" << cal << "\n";
        suma += cal;
        cuantos++;
        if (cal > max) { max = cal; mejor = nombre; }
    }
    in.close();                                      //> 6) Cerrar y reportar
    if (cuantos > 0)
        cout << "Promedio: " << suma / cuantos << "  Mejor: " << mejor << "\n";
    return 0;
}
```

**D. Verificación.** El recuadro final muestra el archivo creado: tres líneas con el formato `nombre calificación`. El promedio (9.5 + 7 + 8.5) / 3 = 8.33 ✔. Si se ejecuta otra vez, el archivo se **sobrescribe** (modo normal).
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.16; ranksep=0.3;
@term(a, "Archivo de texto")
@proc(o, "ofstream f(\"x.txt\")\nf << dato")
@proc(m, "modos: normal (sobrescribe)\nios::app (agrega)")
@proc(i, "ifstream f(\"x.txt\")")
@proc(d, "while (f >> x)\npor datos")
@proc(l, "while (getline(f, s))\npor líneas")
@hl(v, "if (!f) … verificar\nf.close()")
@sub(c, "CSV: stringstream +\ngetline(ss, campo, ',')")
a -> o -> m; a -> i; i -> d; i -> l; a -> v [style=dashed]; l -> c [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1
```cpp run title="plantillas_archivo.cpp" showfile=salida.txt
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    // ESCRIBIR (crea o sobrescribe)
    ofstream out("salida.txt");
    if (!out) return 1;
    out << "manzana 3\npera 5\n";
    out.close();
    // AGREGAR al final
    ofstream app("salida.txt", ios::app);
    app << "uva 12\n";
    app.close();
    // LEER por datos
    ifstream in("salida.txt");
    string fruta;
    int cant, total = 0;
    while (in >> fruta >> cant) total += cant;
    in.close();
    cout << "Total: " << total << "\n";
    return 0;
}
```

| Quiero… | Patrón |
|---|---|
| Leer todos los números | `while (in >> x) { … }` |
| Leer registros de varios campos | `while (in >> a >> b >> c) { … }` |
| Leer líneas completas | `while (getline(in, linea)) { … }` |
| Separar una línea CSV | `stringstream ss(linea); getline(ss, campo, ',');` |
| Borrar un registro | leer el original → escribir los que se quedan en `temp.txt` → `remove("orig.txt"); rename("temp.txt", "orig.txt");` |
| Ruta en Windows | `"C:\\datos\\x.txt"` (barras dobles) o `"C:/datos/x.txt"` |
:::

:::checklist | Guía de preguntas de rutina 2.2
<ul class="checks">
<li>¿Incluí <code>&lt;fstream&gt;</code> (y <code>&lt;sstream&gt;</code> si separo campos)?</li>
<li>¿Verifiqué con <code>if (!f)</code> que el archivo se abrió?</li>
<li>¿Quiero sobrescribir o agregar? (<code>ios::app</code>)</li>
<li>¿Leo en la condición del ciclo (<code>while (in &gt;&gt; x)</code>) y no con <code>while (!in.eof())</code>?</li>
<li>¿El formato con que escribo es el mismo con que después leo (separadores, orden de campos)?</li>
<li>¿Cerré el archivo de escritura antes de abrirlo para leer?</li>
<li>¿Revisé el archivo generado con un editor de texto?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) `while (!in.eof())`: el último dato se procesa dos veces.** `eof` solo se activa **después** de un intento fallido de lectura:

```txt file=tres.txt
10
20
30
```

```cpp run title="eof_bug.cpp"
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream in("tres.txt");
    int x, suma = 0;
    while (!in.eof())          //> Tras leer 30 aún no es eof (falta leer el salto final)
    {
        in >> x;               //> Esta lectura falla, pero x conserva 30…
        suma += x;             //> …y se suma otra vez
    }
    cout << "Suma: " << suma << " (deberia ser 60)\n";
    return 0;
}
```
*Corrección:* `while (in >> x) suma += x;`

**b) No verificar la apertura.** Si el archivo no existe, `in >> x` falla en silencio y el programa reporta 0 datos (o divide entre cero).

**c) Sobrescribir sin querer.** Abrir con `ofstream f("datos.txt");` para «agregar» borra todo: usa `ios::app`.

**d) Mezclar `>>` y `getline`.** Después de `in >> n`, el `getline` siguiente lee el resto de la línea (vacío): usa `in.ignore()` como con `cin`.

**e) Ruta equivocada.** El archivo se busca en la carpeta de **ejecución**, que en algunos IDE no es la del `.cpp`. Imprime un mensaje claro cuando falla la apertura.
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Copiar un archivo en mayúsculas | Variabilidad
El mismo patrón (abrir dos flujos → leer → transformar → escribir), con otro propósito:

```cpp run title="mayusculas.cpp" showfile=LISTA.txt
#include <fstream>
#include <string>
#include <cctype>
using namespace std;
int main()
{
    ifstream in("lista.txt");
    ofstream out("LISTA.txt");
    if (!in || !out) return 1;
    string linea;
    while (getline(in, linea))
    {
        for (char& c : linea) c = toupper(c);
        out << linea << "\n";
    }
    return 0;          //> Los flujos se cierran solos al salir de main (RAII)
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

```cpp run title="bitacora.cpp" stdin="miercoles 24.5\njueves 22.0\nfin 0\n" showfile=temperaturas.txt
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    ofstream out("temperaturas.txt", ios::app);      //> app: conserva las lecturas anteriores
    if (!out) return 1;
    string dia;
    double t;
    cout << "Dia y temperatura (fin 0 para terminar): ";
    while (cin >> dia >> t && dia != "fin")
    {
        out << dia << " " << t << "\n";
        cout << "Dia y temperatura (fin 0 para terminar): ";
    }
    out.close();                                      //> Cerrar antes de releer
    ifstream in("temperaturas.txt");
    double suma = 0;
    int n = 0;
    while (in >> dia >> t) { suma += t; n++; }
    cout << n << " lecturas en total, promedio " << suma / n << "\n";
    return 0;
}
```

**Paso 2 · Gemelo.** Programa un **diario de gastos**: cada ejecución agrega gastos (`concepto monto`) a `gastos.txt` hasta escribir `fin 0`, y después muestra el total acumulado de **todos** los gastos guardados y el gasto más alto.

:::solucion | T1
```txt file=gastos.txt
cafe 35
```

```cpp run title="gastos.cpp" stdin="comida 120\npasaje 18\nfin 0\n" showfile=gastos.txt
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    ofstream out("gastos.txt", ios::app);
    string c;
    double m;
    while (cin >> c >> m && c != "fin") out << c << " " << m << "\n";
    out.close();
    ifstream in("gastos.txt");
    double total = 0, max = 0;
    string cmax;
    while (in >> c >> m)
    {
        total += m;
        if (m > max) { max = m; cmax = c; }
    }
    cout << "Total: $" << total << "  Mayor: " << cmax << " ($" << max << ")\n";
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

```cpp blank title="puntajes.cpp"
#include <iostream>
#include __1__                          // 1: biblioteca de flujos de archivo
using namespace std;
int main()
{
    __2__ in("puntajes.txt");           // 2: flujo para LEER
    if (__3__)                          // 3: ¿fallo la apertura?
    {
        cout << "No se encontro el archivo\n";
        return 1;
    }
    int p, n = 0, suma = 0, mayor = 0;
    while (__4__)                       // 4: leer un puntaje en la condicion
    {
        suma += p;
        n++;
        if (p > mayor) mayor = p;
    }
    __5__;                              // 5: cerrar
    cout << n << " puntajes, promedio " << suma / n << ", mayor " << mayor << "\n";
    return 0;
}
```

:::solucion | T2
{{c:1}} `<fstream>` · {{c:2}} `ifstream` · {{c:3}} `!in` · {{c:4}} `in >> p` · {{c:5}} `in.close()`

```cpp run title="puntajes.cpp"
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream in("puntajes.txt");
    if (!in)
    {
        cout << "No se encontro el archivo\n";
        return 1;
    }
    int p, n = 0, suma = 0, mayor = 0;
    while (in >> p)
    {
        suma += p;
        n++;
        if (p > mayor) mayor = p;
    }
    in.close();
    cout << n << " puntajes, promedio " << suma / n << ", mayor " << mayor << "\n";
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

```cpp blank title="contar.cpp"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;
int main()
{
    ifstream in("poema.txt");
    if (__1__) return 1;
    string linea, larga;
    int lineas = 0, palabras = 0, caracteres = 0;
    while (__2__)
    {
        lineas++;
        caracteres += __3__;
        if (linea.size() > larga.size()) __4__;
        stringstream ss(linea);
        string p;
        while (__5__) palabras++;
    }
    cout << lineas << " lineas, " << palabras << " palabras, " << caracteres << " caracteres\n";
    cout << "Mas larga: " << larga << "\n";
    return 0;
}
```

:::solucion | T3
{{c:1}} `!in` · {{c:2}} `getline(in, linea)` · {{c:3}} `linea.size()` · {{c:4}} `larga = linea` · {{c:5}} `ss >> p`

```cpp run title="contar.cpp"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;
int main()
{
    ifstream in("poema.txt");
    if (!in) return 1;
    string linea, larga;
    int lineas = 0, palabras = 0, caracteres = 0;
    while (getline(in, linea))
    {
        lineas++;
        caracteres += linea.size();
        if (linea.size() > larga.size()) larga = linea;
        stringstream ss(linea);
        string p;
        while (ss >> p) palabras++;
    }
    cout << lineas << " lineas, " << palabras << " palabras, " << caracteres << " caracteres\n";
    cout << "Mas larga: " << larga << "\n";
    return 0;
}
```
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
```cpp run title="inventario_csv.cpp" showfile=surtir.txt
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;
int main()
{
    ifstream in("productos.csv");
    ofstream out("surtir.txt");
    if (!in || !out) { cout << "Error de archivos\n"; return 1; }
    string linea;
    double total = 0;
    int surtir = 0;
    while (getline(in, linea))
    {
        stringstream ss(linea);
        string cod, nom, campo;
        getline(ss, cod, ',');
        getline(ss, nom, ',');
        getline(ss, campo, ',');
        double precio = stod(campo);
        getline(ss, campo, ',');
        int exist = stoi(campo);
        total += precio * exist;
        if (exist < 10)
        {
            out << cod << " " << nom << ": faltan " << 25 - exist << "\n";
            surtir++;
        }
    }
    cout << "Valor del inventario: $" << total << "\n" << surtir << " productos por surtir (ver surtir.txt)\n";
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

```cpp run title="explora_ventas.cpp"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    ifstream in("ventas.txt");
    if (!in) return 1;
    string v, vMax;
    int mes, n = 0, porMes[13] = {}, cAna = 0, cLuis = 0, cEva = 0;
    double monto, total = 0, mx = -1, mn = 1e18;
    double totalMes[13] = {};
    while (in >> v >> mes >> monto)
    {
        n++; total += monto; totalMes[mes] += monto; porMes[mes]++;
        if (monto > mx) { mx = monto; vMax = v; }
        if (monto < mn) mn = monto;
        if (v == "ana") cAna++; else if (v == "luis") cLuis++; else if (v == "eva") cEva++;
    }
    int mejorMes = 1;
    for (int m = 2; m <= 12; m++) if (totalMes[m] > totalMes[mejorMes]) mejorMes = m;
    cout << n << " ventas, total " << total << ", promedio " << total / n << "\n";
    cout << "Mayor " << mx << " (" << vMax << "), menor " << mn << "\n";
    cout << "Ventas por vendedor: ana " << cAna << ", luis " << cLuis << ", eva " << cEva << "\n";
    cout << "Mejor mes: " << mejorMes << " ($" << totalMes[mejorMes] << ", " << porMes[mejorMes] << " ventas)\n";
    return 0;
}
```
:::
:::

:::tarea B | T6. Cuatro errores con archivos (autoexplicación) | 20 min | Autoexplicación, Reversión de la experiencia
**Explica** qué ocurre en cada fragmento y por qué; propón la corrección.

```cpp blank title="archivos_bug.cpp"
// A: el usuario quiere AGREGAR un registro a clientes.txt
ofstream f("clientes.txt");
f << "Nuevo cliente\n";

// B: sumar los numeros de datos.txt
ifstream in("datos.txt");
int x, s = 0;
while (!in.eof()) { in >> x; s += x; }

// C: escribir y luego leer el mismo archivo
ofstream o("temp.txt");
o << 42;
ifstream i("temp.txt");
int y; i >> y;           // y no vale 42

// D: leer la cantidad y luego un nombre con espacios
ifstream g("alumno.txt");   // contiene: "3\nAna Lopez\n"
int n; string nombre;
g >> n;
getline(g, nombre);         // nombre queda vacio
```

{{lineas:5}}

:::solucion | T6
**A:** `ofstream` sin `ios::app` **borra** el archivo: se pierden todos los clientes. → `ofstream f("clientes.txt", ios::app);`. **B:** con `!in.eof()` el último número se suma dos veces (y si el archivo no existe, ciclo con basura); además no se verificó la apertura. → `if (!in) …; while (in >> x) s += x;`. **C:** el 42 puede seguir en el **búfer** de `o` (no se ha escrito al disco) cuando `i` lee. → `o.close();` antes de abrir para leer. **D:** `g >> n` deja el `'\n'`; `getline` lee esa línea vacía. → `g.ignore();` antes de `getline`.
:::
:::

:::tarea B | T7. ¿Qué contiene el archivo? (imaginación) | 20 min | Imaginación
**Sin ejecutar**, imagina el contenido de `log.txt` después de cada bloque y escribe el contenido final.

```cpp check title="imagina_log.cpp"
#include <fstream>
using namespace std;
int main()
{
    { ofstream f("log.txt");              f << "A\n"; }
    { ofstream f("log.txt", ios::app);    f << "B\nC\n"; }
    { ofstream f("log.txt");              f << "D\n"; }
    { ofstream f("log.txt", ios::app);    f << "E\n"; }
    { ofstream f("log.txt", ios::app);    f << "F"; }
    return 0;
}
```

{{lineas:3}}

:::solucion | T7
Bloque 1 → `A`. Bloque 2 (agrega) → `A B C`. Bloque 3 (modo normal: **borra**) → `D`. Bloques 4 y 5 (agregan) → `D E F`. El archivo final tiene tres líneas: `D`, `E` y `F` (la última sin salto de línea). Cada bloque `{ }` cierra el archivo automáticamente al terminar, porque el flujo se destruye (RAII).

```cpp run title="imagina_log.cpp" out=0 showfile=log.txt
#include <fstream>
using namespace std;
int main()
{
    { ofstream f("log.txt");              f << "A\n"; }
    { ofstream f("log.txt", ios::app);    f << "B\nC\n"; }
    { ofstream f("log.txt");              f << "D\n"; }
    { ofstream f("log.txt", ios::app);    f << "E\n"; }
    { ofstream f("log.txt", ios::app);    f << "F"; }
    return 0;
}
```
:::
:::

:::tarea AB | T8. Registro de estudiantes con archivo (reto colaborativo) | 45 min | Memoria colectiva de trabajo, Variabilidad
**Contexto.** Como en la Figura 7.14 de la tesis («Sistema de registro de estudiantes»): un programa que guarda estudiantes (matrícula, nombre de una palabra, calificación) en `estudiantes.txt` y permite **alta**, **consulta** por matrícula, **listado** y **baja**. Los datos deben persistir entre ejecuciones.

:::colab | Organización
Equipos de 4, niveles mezclados. Primero acuerden el **formato** del archivo (una línea por estudiante: `matricula nombre calificacion`).
- **Integrante 1:** `void alta(…)` con `ios::app` (rechaza matrículas repetidas consultando el archivo).
- **Integrante 2:** `bool consulta(int mat)` y `void listado()`.
- **Integrante 3:** `bool baja(int mat)`: copia a `temp.txt` todos menos el buscado y reemplaza el original (`remove` / `rename` de `<cstdio>`).
- **Integrante 4:** menú y pruebas: alta de 3, baja de 1, listado; volver a ejecutar y comprobar que los datos siguen ahí.
:::

:::solucion | T8
```txt file=estudiantes.txt
2001 Ana 9.1
2002 Luis 7.4
```

```cpp run title="registro_estudiantes.cpp" stdin="1 2003 Eva 8.8\n1 2001 Repetido 5\n2 2002\n4 2002\n3\n0\n" showfile=estudiantes.txt
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
using namespace std;
const string ARCH = "estudiantes.txt";

bool consulta(int mat, bool mostrar)
{
    ifstream in(ARCH);
    int m; string n; double c;
    while (in >> m >> n >> c)
        if (m == mat) { if (mostrar) cout << "  " << m << " " << n << " " << c << "\n"; return true; }
    return false;
}
void alta(int mat, const string& nom, double cal)
{
    if (consulta(mat, false)) { cout << "  Matricula repetida\n"; return; }
    ofstream out(ARCH, ios::app);
    out << mat << " " << nom << " " << cal << "\n";
    cout << "  Alta de " << nom << "\n";
}
void listado()
{
    ifstream in(ARCH);
    int m; string n; double c;
    while (in >> m >> n >> c) cout << "  " << m << " " << n << " " << c << "\n";
}
bool baja(int mat)
{
    ifstream in(ARCH);
    ofstream tmp("temp.txt");
    int m; string n; double c;
    bool hallado = false;
    while (in >> m >> n >> c)
    {
        if (m == mat) hallado = true;
        else tmp << m << " " << n << " " << c << "\n";
    }
    in.close(); tmp.close();
    remove(ARCH.c_str());
    rename("temp.txt", ARCH.c_str());
    return hallado;
}
int main()
{
    int op;
    while (cin >> op && op != 0)
    {
        int mat; string nom; double cal;
        switch (op)
        {
            case 1: cin >> mat >> nom >> cal; alta(mat, nom, cal); break;
            case 2: cin >> mat; if (!consulta(mat, true)) cout << "  No existe\n"; break;
            case 3: listado(); break;
            case 4: cin >> mat; cout << (baja(mat) ? "  Baja realizada\n" : "  No existe\n"); break;
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

**Segmento 1 — Por qué no «editar en su lugar».** {{como}} Descarto escribir directamente en medio del archivo de texto. {{porque}} En un archivo de texto, «45.5» y «50.05» ocupan distinto número de caracteres: si sobrescribo en el lugar, piso el inicio de la línea siguiente.

**Segmento 2 — Leer uno, escribir otro.** {{como}} Abro `precios.txt` para leer y `temp.txt` para escribir; copio cada registro tal cual, excepto el buscado, que escribo con su nuevo precio. {{porque}} Así el archivo nuevo se construye completo y correcto, línea por línea.

**Segmento 3 — Reemplazar con seguridad.** {{como}} Cierro **ambos** flujos y solo entonces hago `remove("precios.txt")` y `rename("temp.txt", "precios.txt")`. {{porque}} Si borrara el original antes de terminar de escribir el temporal y algo fallara, perdería los datos.

**Segmento 4 — Avisar y verificar.** {{como}} Llevo una bandera `encontrado` para avisar si el producto no existía y, al final, muestro el archivo resultante. {{porque}} Un programa que modifica datos debe confirmar lo que hizo; y ver el archivo final es la prueba definitiva.

{{salto}}

```txt file=precios.txt
lapiz 8
cuaderno 45.5
mochila 520
```

```cpp run title="modificar.cpp" stdin="cuaderno\n" showfile=precios.txt
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
using namespace std;
int main()
{
    string buscado;
    cout << "Producto a aumentar: ";
    cin >> buscado;
    ifstream in("precios.txt");
    ofstream tmp("temp.txt");
    if (!in || !tmp) return 1;
    string p;
    double precio;
    bool encontrado = false;
    while (in >> p >> precio)
    {
        if (p == buscado) { precio *= 1.10; encontrado = true; }
        tmp << p << " " << precio << "\n";
    }
    in.close();
    tmp.close();
    remove("precios.txt");
    rename("temp.txt", "precios.txt");
    cout << (encontrado ? "Precio actualizado\n" : "No se encontro el producto\n");
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. ¿Qué diferencia hay entre memoria principal y memoria secundaria?
2. Menciona una diferencia entre un archivo de texto y uno binario.
3. ¿Qué biblioteca contiene `ifstream` y `ofstream`?
4. ¿Qué ocurre si abres con `ofstream f("x.txt");` un archivo que ya tenía datos?
5. ¿Cómo se abre un archivo para agregar al final?
6. ¿Cómo se verifica que un archivo se abrió correctamente?
7. ¿Por qué se recomienda `while (in >> x)` en lugar de `while (!in.eof())`?
8. ¿Qué función lee una línea completa de un archivo?
9. ¿Para qué sirve un `stringstream` al leer un CSV?
10. ¿Cuál es el equivalente en C de `ofstream f("a.txt", ios::app);`?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Analiza la salida** si `nums.txt` contiene `4 8 15 16 23 42`:

```cpp check title="p1.cpp"
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream in("nums.txt");
    int x, pares = 0, ultimo = 0;
    while (in >> x)
    {
        if (x % 2 == 0) pares++;
        ultimo = x;
    }
    cout << pares << " " << ultimo << "\n";
    return 0;
}
```

**P2. Corrige:** `ifstream out("reporte.txt"); out << "Total: " << t; while (!out.eof()) {...}`

**P3. Implementa** un programa que lea `temperaturas.txt` (un número por línea) y escriba en `alertas.txt` solo las mayores de 30, numeradas.

**P4. Desarrolla** un programa de manipulación de datos: lee `alumnos.csv` (`id,nombre,promedio`), genera `aprobados.csv` y `reprobados.csv` (promedio ≥ 6 o < 6) con el mismo formato e informa cuántos registros escribió en cada uno.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Escribo archivos creando o agregando según lo que necesito.</li>
<li>Leo archivos por datos y por líneas sin procesar dos veces el último dato.</li>
<li>Verifico la apertura y cierro los archivos en el momento correcto.</li>
<li>Proceso registros con campos y hago bajas o modificaciones con un archivo temporal.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 La principal (RAM) es rápida pero se borra al terminar el programa o apagar; la secundaria (disco, USB) conserva los datos · 2 El de texto contiene caracteres legibles y se abre con un editor; el binario guarda bytes tal como están en memoria · 3 `<fstream>` · 4 Se borra el contenido anterior (modo normal) · 5 `ofstream f("x.txt", ios::app);` · 6 `if (!f)` o `if (!f.is_open())` · 7 Porque `eof` se activa solo después de una lectura fallida y el último dato se procesaría dos veces · 8 `getline(flujo, cadena)` · 9 Para tratar la línea como un flujo y separar sus campos con `getline(ss, campo, ',')` · 10 `FILE* f = fopen("a.txt", "a");`
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.**

```txt file=nums.txt
4 8 15 16 23 42
```

```cpp run title="p1.cpp"
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream in("nums.txt");
    int x, pares = 0, ultimo = 0;
    while (in >> x)
    {
        if (x % 2 == 0) pares++;
        ultimo = x;
    }
    cout << pares << " " << ultimo << "\n";
    return 0;
}
```

**P2.** Para escribir se usa `ofstream` (no `ifstream`); verificar la apertura; el ciclo con `eof` sobra (y no tiene sentido en un flujo de salida); cerrar al final.

**P3.**

```txt file=temps.txt
28.5
31.2
29.9
33.0
30.1
```

```cpp run title="alertas.cpp" showfile=alertas.txt
#include <fstream>
using namespace std;
int main()
{
    ifstream in("temps.txt");
    ofstream out("alertas.txt");
    if (!in || !out) return 1;
    double t;
    int k = 0;
    while (in >> t)
        if (t > 30) out << ++k << ". " << t << "\n";
    return 0;
}
```

**P4.** Se reutiliza el patrón del concepto 8 (CSV con `stringstream`) y dos `ofstream`; por cada línea se decide en cuál escribir con `if (promedio >= 6)` y se lleva un contador por archivo.
:::
