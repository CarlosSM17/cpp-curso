---
num: "15"
archivo: "Tema15_Memoria_dinamica"
titulo: "Memoria dinámica: malloc, calloc, realloc y free"
corto: "Memoria dinámica"
lema: "Pedir memoria cuando la necesitas, del tamaño que necesitas… y devolverla cuando terminas."
duracion: "5 h · 3 sesiones"
previos: "Tema 14 (punteros, `NULL`, `void *`), Tema 08 (arreglos), Tema 10 (funciones) y Tema 13 (estructuras)."
fuentes:
  - "Kernighan, B. W. y Ritchie, D. M. (1988). *The C Programming Language* (2.ª ed.). Prentice Hall. Cap. 6: §6.5 Self-referential Structures (reserva de nodos). Cap. 7: §7.8.5 Storage Management. Cap. 8: §8.7 Example—A Storage Allocator."
  - "King, K. N. (2008). *C Programming: A Modern Approach* (2.ª ed.). W. W. Norton. Cap. 17 «Advanced Uses of Pointers»: §17.1 Dynamic Storage Allocation, §17.2 Dynamically Allocated Strings, §17.3 Dynamically Allocated Arrays, §17.4 Deallocating Storage, §17.5 Linked Lists."
  - "Seacord, R. C. (2020). *Effective C*. No Starch Press. Cap. 6 «Dynamically Allocated Memory». Cap. 11 «Debugging, Testing, and Analysis» (AddressSanitizer)."
  - "Sandoval Medina, C. (2026). Tesis doctoral, §5.4: el estudio piloto del modelo CLT4BP abarcó estructuras anidadas, punteros y memoria dinámica (objetivo intermedio: «optimización vía asignación dinámica de memoria», Tabla 5.14)."
objetivos:
  A:
    - "Distinguir la memoria automática (pila) de la memoria dinámica (montón)."
    - "Reservar y liberar memoria con `malloc` y `free`, verificando que la reserva no falle (`NULL`)."
    - "Crear arreglos dinámicos con `malloc` y `calloc` cuyo tamaño se decide en ejecución."
    - "Reconocer y evitar fugas de memoria y punteros colgantes."
  B:
    - "Redimensionar un arreglo dinámico con `realloc` y explicar lo que hace por dentro."
    - "Crear estructuras enlazadas con nodos dinámicos y liberarlas por completo."
    - "Reservar matrices dinámicas (arreglo de punteros a filas)."
    - "Detectar fugas con AddressSanitizer y organizar el código en pares crear/destruir."
efectos:
  soporte:
    - ["Elementos aislados", "Duración de almacenamiento → malloc/free de una variable → arreglos dinámicos → fugas → colgantes → funciones que reservan → realloc → nodos → detección de fugas."]
    - ["Atención dividida", "Diagramas de pila y montón integrados con cada línea de código."]
    - ["Ejemplo resuelto", "Calificaciones con arreglo dinámico de tamaño elegido por el usuario."]
    - ["Modalidad", "Guion narrado del protocolo verbal sobre los diagramas de pila/montón."]
  procedimental:
    - ["Variabilidad", "El par reservar/liberar en contextos distintos (arreglos, nodos, matrices)."]
    - ["Autoexplicación", "Lista de verificación «por cada malloc, un free» explicada en voz alta."]
  tareas:
    - ["Ejemplo resuelto", "T1: temperaturas dinámicas + gemelo (precios)."]
    - ["Problema por completar", "T2 (crear arreglo, con pistas) y T3 (agrandar a mano, sin pistas)."]
    - ["Desvanecimiento de guía", "T1 → T4."]
    - ["Solución libre", "T5: todas las formas de tener n datos con n leído en ejecución."]
    - ["Autoexplicación", "T6: fugas, dobles liberaciones y `free` inválidos."]
    - ["Imaginación", "T7: imaginar pila y montón línea por línea."]
    - ["Memoria colectiva de trabajo", "T8: cola de turnos con nodos dinámicos."]
diferenciada:
  Contenido:
    comp: "Información de soporte"
    A: "Pila vs montón, `malloc`/`calloc`/`free`, verificación de `NULL`, fugas y colgantes."
    B: "`realloc`, nodos dinámicos, matrices dinámicas, AddressSanitizer."
  Proceso:
    comp: "Tareas de aprendizaje"
    A: "T1 → T4 dibujando pila y montón."
    B: "T5, T6, T7 autónomas; diseñadores de la estructura en T8."
  Producto:
    comp: "Tareas de aprendizaje"
    A: "Lista de compras que crece (T4) sin fugas."
    B: "Cola de turnos dinámica (T8) que libera todo al terminar."
  Entorno:
    comp: "Información procedimental"
    A: "Hoja de diagramas pila/montón."
    B: "Compilar con `-g -fsanitize=address` (detecta fugas y accesos inválidos); Valgrind como alternativa."
plan:
  - ["Sesión 1", "Soporte + tareas", "Analogía del hotel; conceptos 1–5; ejemplo resuelto; T1, T2.", "100 min"]
  - ["Sesión 2", "Soporte + tareas", "Conceptos 6–9; T3, T4; Ruta B: T6, T7.", "100 min"]
  - ["Sesión 3", "Tareas + evaluación", "T5, T8 colaborativa; protocolo verbal; tests; instrumentos de carga cognitiva.", "100 min"]
glosario:
  - ["memoria dinámica", "dynamic memory", "Memoria que el programa pide y libera en ejecución."]
  - ["montón", "heap", "Zona de memoria para bloques dinámicos."]
  - ["pila", "stack", "Zona de memoria de las variables automáticas (locales)."]
  - ["duración de almacenamiento", "storage duration", "Tiempo de vida de un objeto: automática, estática o dinámica."]
  - ["reservar / asignar", "allocate (`malloc`, `calloc`)", "Pedir memoria al montón; devuelve la dirección del bloque o `NULL`."]
  - ["liberar", "deallocate (`free`)", "Devolver memoria al montón."]
  - ["redimensionar", "reallocate (`realloc`)", "Cambiar el tamaño de un bloque conservando sus datos."]
  - ["arreglo dinámico", "dynamic array", "Arreglo cuyo tamaño se decide en ejecución: `malloc(n * sizeof *a)`."]
  - ["fuga de memoria", "memory leak", "Memoria reservada que ya no se puede liberar porque se perdió su dirección."]
  - ["puntero colgante", "dangling pointer", "Puntero a memoria ya liberada."]
  - ["doble liberación", "double free", "Liberar dos veces el mismo bloque: comportamiento indefinido."]
  - ["nodo", "node", "Estructura con datos y un puntero a otro nodo."]
  - ["AddressSanitizer", "AddressSanitizer / LeakSanitizer", "Herramienta de gcc (`-fsanitize=address`) que detecta accesos inválidos y fugas al ejecutar."]
---

# 1. Información de soporte {.soporte}

:::analogia | El hotel y la mochila
Tus variables locales son como lo que llevas en la **mochila**: cabe poco, se organiza solo (lo último que metes es lo primero que sacas) y, al terminar el día (la función), se vacía sola. Cuando necesitas más espacio, o espacio que dure más que un día, **rentas un cuarto de hotel** (el **montón**): pides el cuarto (`malloc`), te dan la **llave con el número de cuarto** (un puntero) y, cuando terminas, **debes entregar el cuarto** (`free`). Si pierdes la llave sin entregarlo, el cuarto queda ocupado para siempre: eso es una **fuga de memoria**.
:::

:::pregunta
En el Tema 08 reservaste `int notas[100]` aunque el grupo tuviera 12 alumnos, y no podías tener más de 100. **¿Cómo crees que una app de fotos guarda 15 fotos hoy y 3 000 mañana sin saber de antemano cuántas habrá?**

{{lineas:2}}
:::

:::relevancia
Las listas que crecen (mensajes de un chat, enemigos que aparecen en un juego, filas que se cargan de un archivo) necesitan memoria cuyo tamaño se decide **mientras el programa corre**. En C esa memoria la administras tú: no hay nada que la libere por ti. Dominar `malloc` y `free` te permite escribir programas que se adaptan a sus datos y evitar los dos errores más costosos de C: las fugas y los punteros colgantes (que también son el origen de muchas fallas de seguridad). {{arcs:Relevancia}}
:::

## 1.1 Conceptos, uno por uno

:::concepto | 1 | ¿Cuánto vive un objeto? Duración de almacenamiento | Elementos aislados, Atención dividida
Los objetos de C se clasifican por su **duración**:

| Duración | Dónde vive | Cuándo nace | Cuándo muere | Ejemplo |
|---|---|---|---|---|
| Automática | pila | al entrar al bloque | al salir del bloque | variables locales, parámetros |
| Estática | zona estática | al iniciar el programa | al terminar el programa | globales, `static` locales |
| **Dinámica** | **montón** | cuando se llama a `malloc` | cuando se llama a `free` | `malloc(n * sizeof(int))` |

```diagram mem
regions:
  - name: "Pila (automática)"
    vars:
      - {name: n, type: int, val: 3}
      - {name: p, type: "int *", val: "0x5a0", kind: ptr, to: bloque}
  - name: "Montón (dinámica)"
    color: "#fdf4ff"
    vars:
      - {name: bloque, type: "int[3]", val: "7 | 8 | 9", addr: "0x5a0"}
figcaption: "Figura 1. El puntero vive en la pila; el bloque que reservó con malloc vive en el montón."
```
:::

:::concepto | 2 | `malloc` y `free`: una variable dinámica | Elementos aislados, Atención dividida
```c run title="malloc_free.c"
#include <stdio.h>
#include <stdlib.h>                     //> malloc y free viven en <stdlib.h>
int main(void)
{
    int *p = malloc(sizeof *p);         //> Reserva espacio para UN int en el montón; devuelve su dirección (o NULL)
    if (p == NULL)                      //> malloc puede fallar (sin memoria): siempre se verifica
        return 1;
    *p = 42;                            //> La memoria de malloc NO viene inicializada: se le da valor
    printf("*p = %d\n", *p);
    *p += 8;                            //> Se usa como cualquier puntero
    printf("*p = %d\n", *p);
    free(p);                            //> Devuelve la memoria al montón (el puntero sigue existiendo)
    p = NULL;                           //> Buena práctica: así no queda «colgando»
    return 0;
}
```
`malloc` recibe **cuántos bytes** reservar; `sizeof *p` calcula el tamaño de aquello a lo que apunta `p`. Devuelve un `void *` (Tema 14), que en C se convierte solo al tipo del puntero. **Regla de oro:** por cada `malloc` (o `calloc`), **exactamente un** `free`.
:::

:::concepto | 3 | Arreglos dinámicos: el tamaño se decide en ejecución | Elementos aislados, Atención dividida
Para `n` elementos se piden `n * sizeof *datos` bytes. `calloc(n, tamaño)` hace lo mismo pero **llena con ceros**. Ambos se liberan con `free`:

```c run title="arreglo_dinamico.c" stdin="4\n10 20 30 40\n"
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int n;
    printf("Cuantos datos? ");
    scanf("%d", &n);
    int *datos = malloc(n * sizeof *datos);    //> Exactamente n enteros en el montón
    double *promedios = calloc(n, sizeof *promedios);   //> n doubles, todos en 0.0
    if (datos == NULL || promedios == NULL)
        return 1;
    for (int i = 0; i < n; i++)
        scanf("%d", &datos[i]);                //> Se usa con índices, igual que un arreglo
    int suma = 0;
    for (int i = 0; i < n; i++) suma += datos[i];
    printf("Suma: %d, primer promedio: %.1f\n", suma, promedios[0]);
    free(datos);                               //> Uno por cada reserva
    free(promedios);
    return 0;
}
```
Esto resuelve el problema del Tema 08 (T2): el tamaño `TAM` del usuario ya no necesita un máximo fijo, y a diferencia de un VLA, si no hay memoria `malloc` lo avisa con `NULL` en lugar de detener el programa.
:::

:::concepto | 4 | Fugas de memoria: perder la llave | Elementos aislados, Atención dividida
Si el único puntero a un bloque se pierde (se reasigna o la función termina) **antes** de `free`, ese bloque queda inaccesible y ocupado hasta que termine el programa:

<div class="cols eq">
<div>

```c nolines
int *p = malloc(1000 * sizeof *p);
p = malloc(1000 * sizeof *p);  // el primer bloque
                               // quedo sin llave
free(p);                       // solo libera el segundo
```

</div>
<div>

```diagram mem
regions:
  - name: "Pila"
    vars:
      - {name: p, type: "int *", val: "0x900", kind: ptr, to: B2}
  - name: "Montón"
    color: "#fdf4ff"
    vars:
      - {name: B1, type: "int[1000]", val: "fuga", kind: dead, addr: "0x500"}
      - {name: B2, type: "int[1000]", val: "...", addr: "0x900"}
```

</div>
</div>

En programas que corren mucho tiempo (servidores, juegos), las fugas se acumulan hasta agotar la memoria.
:::

:::concepto | 5 | Punteros colgantes y doble liberación | Elementos aislados
- **Colgante:** usar el puntero **después** de `free`: la memoria ya no es tuya.
- **Doble liberación:** hacer `free` dos veces del mismo bloque: comportamiento indefinido (normalmente el programa aborta).
- **Liberar lo que no vino de `malloc`:** `free` solo acepta direcciones devueltas por `malloc`, `calloc` o `realloc`.

```c blank title="peligros.c"
int *p = malloc(sizeof *p);
*p = 5;
free(p);
printf("%d", *p);   // colgante: lectura invalida
free(p);            // doble liberacion
```
**Protección sencilla:** después de `free(p);` escribe `p = NULL;` (`free(NULL)` no hace nada y `if (p)` detecta que ya no apunta a nada).
:::

:::concepto | 6 | Funciones que reservan memoria: ¿quién la libera? | Elementos aislados, Atención dividida
Una función puede crear un bloque dinámico y devolver su dirección: el bloque **sobrevive** a la función (a diferencia de una variable local, Tema 14, T6). Pero alguien debe liberarlo: se documenta quién es el **dueño**.

```c run title="fabrica.c"
#include <stdio.h>
#include <stdlib.h>

int *crearSecuencia(int n)              //> Devuelve un bloque NUEVO: quien llama se vuelve su dueño
{
    int *a = malloc(n * sizeof *a);
    if (a == NULL) return NULL;
    for (int i = 0; i < n; i++) a[i] = (i + 1) * (i + 1);
    return a;                            //> Correcto: el bloque está en el montón, no en la pila
}

int main(void)
{
    int *cuadrados = crearSecuencia(6);
    if (cuadrados == NULL) return 1;
    for (int i = 0; i < 6; i++) printf("%d ", cuadrados[i]);
    printf("\n");
    free(cuadrados);                     //> El dueño (main) libera
    return 0;
}
```
:::

:::concepto | 7 | Hacer crecer un arreglo dinámico con `realloc` | Elementos aislados, Atención dividida
`realloc(bloque, nuevoTamaño)` hace por ti los cuatro pasos de «crecer»: (1) reservar uno más grande, (2) copiar los datos, (3) liberar el viejo, (4) devolver la nueva dirección (a veces logra crecer en el mismo lugar). Lo habitual es **duplicar** la capacidad cada vez:

```c run title="crecer.c"
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int capacidad = 2, n = 0;
    int *a = malloc(capacidad * sizeof *a);
    if (a == NULL) return 1;
    for (int x = 10; x <= 70; x += 10)                   //> Insertamos 7 datos en un arreglo de capacidad 2
    {
        if (n == capacidad)                              //> ¿Lleno? Crecer
        {
            int *tmp = realloc(a, 2 * capacidad * sizeof *a);   //> El doble; los datos se conservan
            if (tmp == NULL) { free(a); return 1; }      //> Si falla, `a` sigue siendo válido: se libera
            a = tmp;
            capacidad *= 2;
            printf("(crece a %d) ", capacidad);
        }
        a[n++] = x;
    }
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    free(a);
    return 0;
}
```
El resultado de `realloc` se guarda en un puntero **temporal**: si escribieras `a = realloc(a, …)` y fallara, `a` quedaría en `NULL` y el bloque original, sin llave.
:::

:::concepto | 8 | Ruta B · Nodos dinámicos | Elementos aislados, Reversión de la experiencia
En el Tema 14 enlazaste vagones que eran variables locales. Con `malloc`, los nodos se crean **cuando se necesitan**:

```c run title="lista_dinamica.c"
#include <stdio.h>
#include <stdlib.h>
typedef struct Nodo { int dato; struct Nodo *sig; } Nodo;

int main(void)
{
    Nodo *cabeza = NULL;
    for (int x = 1; x <= 4; x++)
    {
        Nodo *nuevo = malloc(sizeof *nuevo);            //> Un nodo nuevo en el montón
        if (nuevo == NULL) return 1;
        nuevo->dato = x * 10;
        nuevo->sig = cabeza;                            //> Se inserta al INICIO: apunta a la cabeza anterior
        cabeza = nuevo;
    }
    for (Nodo *p = cabeza; p != NULL; p = p->sig)
        printf("%d -> ", p->dato);
    printf("NULL\n");
    while (cabeza != NULL)                              //> Liberar TODOS los nodos
    {
        Nodo *siguiente = cabeza->sig;                  //> Guardar el siguiente ANTES de liberar
        free(cabeza);
        cabeza = siguiente;
    }
    return 0;
}
```
:::

:::concepto | 9 | Ruta B · Encontrar fugas con AddressSanitizer | Elementos aislados, Reversión de la experiencia
En C nadie libera la memoria por ti, así que conviene que una herramienta revise. Si compilas con `-g -fsanitize=address`, al terminar el programa se reporta cada fuga y la línea donde se reservó el bloque:

```c run title="detecta_fuga.c" flags="-g -fsanitize=address" rc
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int *p = malloc(10 * sizeof *p);
    p = malloc(10 * sizeof *p);      //> El primer bloque (línea 5) queda sin llave
    free(p);
    printf("Termine\n");
    return 0;
}
```
La salida dice **cuántos bytes** se perdieron (10 enteros de 4 bytes = 40) y **dónde** se reservaron (línea 5). Dos hábitos que evitan llegar ahí: (1) escribir funciones en **pares** `crearX`/`destruirX` (las verás en los módulos del Tema 17) y (2) liberar en el mismo nivel donde se reservó. Otra herramienta muy usada en Linux es Valgrind (`valgrind --leak-check=full ./prog`).
:::

## 1.2 Ejemplo resuelto: calificaciones con arreglo dinámico

:::ejemplo | Arreglo de calificaciones del tamaño exacto del grupo | Ejemplo resuelto, Atención dividida
**Problema.** Leer el número de alumnos `n` (cualquier tamaño positivo) y sus calificaciones; mostrar el promedio y cuántos están por encima de él. Usar exactamente la memoria necesaria y liberarla al final.

**A. Algoritmo:** 1) Leer `n` (validar > 0). 2) Reservar un arreglo dinámico de `n` `double` y verificar la reserva. 3) Leer las calificaciones y sumar. 4) Calcular el promedio y contar las que lo superan (segundo recorrido). 5) Liberar el arreglo.

**B. Pseudocódigo**

```pseudo
Algoritmo CalificacionesDinamicas
    Repetir
        Leer n
    Hasta Que n > 0
    Dimension cal[n]
    suma <- 0
    Para i <- 1 Hasta n Hacer
        Leer cal[i]
        suma <- suma + cal[i]
    FinPara
    prom <- suma / n
    Escribir prom
FinAlgoritmo
```

**C. Código en C**

```c run title="calificaciones_dinamicas.c" stdin="0\n5\n8 9.5 6 7 10\n"
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int n;
    do {
        printf("Numero de alumnos: ");
        scanf("%d", &n);
    } while (n <= 0);                            //> 1) Validar
    double *cal = malloc(n * sizeof *cal);       //> 2) Reservar EXACTAMENTE n (en el montón)…
    if (cal == NULL)                             //>    …y verificar
    {
        printf("Sin memoria\n");
        return 1;
    }
    double suma = 0;
    for (int i = 0; i < n; i++)                  //> 3) Leer y acumular
    {
        scanf("%lf", &cal[i]);
        suma += cal[i];
    }
    double prom = suma / n;                      //> 4) Promedio y segundo recorrido
    int arriba = 0;
    for (int i = 0; i < n; i++)
        if (cal[i] > prom) arriba++;
    printf("Promedio: %.1f, por encima: %d\n", prom, arriba);
    free(cal);                                   //> 5) Liberar: un malloc → un free
    cal = NULL;
    return 0;
}
```

```diagram mem
regions:
  - name: "Pila de main"
    vars:
      - {name: n, type: int, val: 5}
      - {name: cal, type: "double *", val: "0x7a0", kind: ptr, to: bloque}
      - {name: prom, type: double, val: 8.1}
  - name: "Montón"
    color: "#fdf4ff"
    vars:
      - {name: bloque, type: "double[5]", val: "8 | 9.5 | 6 | 7 | 10", addr: "0x7a0"}
figcaption: "Figura 2. Estado antes de free: el bloque mide exactamente lo que pidió el usuario."
```

**D. Verificación.** (8 + 9.5 + 6 + 7 + 10) / 5 = 8.1; superan el promedio 9.5 y 10 → 2 ✔. El programa tiene un `malloc` y un `free`.
:::

:::resumen | Mapa del tema
```dot
rankdir=LR; nodesep=0.16; ranksep=0.3;
@term(m, "Memoria dinámica\n(montón) · <stdlib.h>")
@proc(a, "malloc(sizeof *p)  →  free(p)")
@proc(b, "malloc(n * sizeof *a)\ncalloc(n, sizeof *a)")
@proc(c, "tamaño decidido\nen ejecución · verificar NULL")
@proc(g, "crecer: realloc\n(con puntero temporal)")
@proc(nd, "nodos: malloc por nodo\nliberar todos")
@hl(e, "errores: fuga · colgante\ndoble free · free inválido")
@sub(r, "-fsanitize=address\npares crear / destruir")
m -> a; m -> b; b -> c; b -> g; m -> nd; m -> e [style=dashed]; m -> r [style=dashed];
```
:::

# 2. Información procedimental {.procedimental}

:::sintaxis | Tarjeta de sintaxis 2.1
| Quiero… | Reservar | Liberar |
|---|---|---|
| Un valor | `T *p = malloc(sizeof *p);` | `free(p); p = NULL;` |
| Un arreglo de `n` | `T *a = malloc(n * sizeof *a);` | `free(a); a = NULL;` |
| Un arreglo en ceros | `T *a = calloc(n, sizeof *a);` | `free(a);` |
| Agrandar a `m` elementos | `T *tmp = realloc(a, m * sizeof *a); if (tmp) a = tmp;` | (el mismo `free(a)`) |
| Una estructura | `Nodo *x = malloc(sizeof *x);` | `free(x);` |
| Una matriz `f × c` | `T **m = malloc(f * sizeof *m); for (i…) m[i] = malloc(c * sizeof *m[i]);` | `for (i…) free(m[i]); free(m);` |

**Siempre:** `#include <stdlib.h>` y verificar que el resultado no sea `NULL` antes de usarlo.
:::

:::checklist | Guía de preguntas de rutina 2.2 · «Por cada malloc, un free»
<ul class="checks">
<li>¿Cuento mis <code>malloc</code>/<code>calloc</code> y mis <code>free</code>? ¿Coinciden?</li>
<li>¿Multipliqué por <code>sizeof</code> (pido <b>bytes</b>, no elementos)?</li>
<li>¿Verifiqué que la reserva no devolvió <code>NULL</code>?</li>
<li>¿Hay algún camino (un <code>return</code> temprano, un <code>break</code>) que salte el <code>free</code>?</li>
<li>¿Reasigno un puntero que todavía es el único que conoce un bloque? (Fuga.)</li>
<li>Después de <code>free</code>, ¿puse el puntero en <code>NULL</code> y ya no lo uso?</li>
<li>Si una función devuelve memoria dinámica, ¿está claro quién la libera?</li>
<li>¿Guardo el resultado de <code>realloc</code> en un puntero temporal?</li>
</ul>
:::

:::errores | Errores frecuentes 2.3 | Variabilidad, Autoexplicación
**a) Olvidar `sizeof`.** `int *a = malloc(10);` reserva **10 bytes**, no 10 enteros (que ocupan 40): escribir `a[5]` ya se sale del bloque. Escribe siempre `malloc(10 * sizeof *a)`.

**b) Fuga dentro de un ciclo.** Cada vuelta reserva y nunca libera:

```c blank title="fuga_ciclo.c"
for (int i = 0; i < 1000; i++)
{
    double *temp = malloc(500 * sizeof *temp);
    // ... usa temp ...
}           // falta free(temp); -> 1000 bloques perdidos
```

**c) Usar un bloque después de liberarlo** (colgante) o liberarlo dos veces: pon el puntero en `NULL` tras el `free`.

**d) Liberar memoria que no vino de `malloc`.** `x` vive en la pila; gcc incluso lo detecta al compilar:

```c warn
#include <stdlib.h>
int main(void)
{
    int x = 5;
    int *p = &x;
    free(p);
    return 0;
}
```

**e) Liberar una lista «de golpe».** `free(cabeza);` libera solo el primer nodo; los demás quedan como fuga. Hay que recorrer guardando el siguiente (concepto 8).

**f) `a = realloc(a, …)` directo.** Si `realloc` falla devuelve `NULL`: pierdes la única dirección del bloque original (fuga). Usa un puntero temporal (concepto 7).
:::

:::isomorfo | Ejemplo isomórfico 2.4 · Copia exacta de un texto | Variabilidad
El mismo patrón (medir → reservar exacto → usar → liberar), ahora con una cadena:

```c run title="copia_texto.c"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void)
{
    const char *original = "Memoria dinamica";
    size_t n = strlen(original);
    char *copia = malloc(n + 1);          //> +1 para el '\0' (sizeof(char) es 1)
    if (copia == NULL) return 1;
    strcpy(copia, original);
    copia[0] = 'm';
    printf("%s | %s\n", original, copia);
    free(copia);
    return 0;
}
```
:::

# 3. Tareas de aprendizaje {.tareas}

{{ef:Desvanecimiento de guía}} En cada tarea, dibuja la pila y el montón y verifica «por cada `malloc`, un `free`».

:::tarea A | T1. Temperaturas dinámicas: ejemplo y gemelo | 20 min | Ejemplo resuelto, Variabilidad
**Paso 1 · Estudia:**

```c run title="temperaturas_dinamicas.c" stdin="4\n18.5 22 25.5 20\n"
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int dias;
    scanf("%d", &dias);
    double *t = malloc(dias * sizeof *t);     //> Tantos días como diga el usuario
    if (t == NULL) return 1;
    double max = -1000;
    for (int i = 0; i < dias; i++)
    {
        scanf("%lf", &t[i]);
        if (t[i] > max) max = t[i];
    }
    printf("Maxima: %.1f\nDias con la maxima:", max);
    for (int i = 0; i < dias; i++)
        if (t[i] == max) printf(" %d", i + 1);
    printf("\n");
    free(t);                                  //> Liberar
    return 0;
}
```

**Paso 2 · Gemelo.** Lee `n` precios en un arreglo dinámico, aplica un descuento del 15 % a los mayores de $500, muestra los precios finales y el total; libera la memoria.

:::solucion | T1
```c run title="precios_dinamicos.c" stdin="4\n350 899 120 1500\n"
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int n;
    scanf("%d", &n);
    double *p = malloc(n * sizeof *p);
    if (p == NULL) return 1;
    double total = 0;
    for (int i = 0; i < n; i++)
    {
        scanf("%lf", &p[i]);
        if (p[i] > 500) p[i] *= 0.85;
        total += p[i];
    }
    for (int i = 0; i < n; i++) printf("%.2f ", p[i]);
    printf("\nTotal: %.2f\n", total);
    free(p);
    return 0;
}
```
:::
:::

:::tarea A | T2. Una función que crea arreglos (completa con pistas) | 20 min | Problema por completar
```c blank title="crear_arreglo.c"
#include <stdio.h>
#include <stdlib.h>

__1__ crearArreglo(int n, int valor)       // 1: tipo de retorno: direccion de un bloque de int
{
    int *a = __2__;                        // 2: reservar n enteros
    if (a == NULL) return NULL;
    for (int i = 0; i < n; i++)
        a[i] = valor;
    return a;
}

void mostrar(const int *a, int n)
{
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void)
{
    int *unos = crearArreglo(5, 1);
    int *sietes = crearArreglo(3, 7);
    if (unos == NULL || sietes == NULL) return 1;
    mostrar(unos, 5);
    mostrar(sietes, 3);
    __3__;                                 // 3: liberar unos
    __4__;                                 // 4: liberar sietes
    return 0;
}
```

:::solucion | T2
{{c:1}} `int *` · {{c:2}} `malloc(n * sizeof *a)` · {{c:3}} `free(unos)` · {{c:4}} `free(sietes)`

```c run title="crear_arreglo.c"
#include <stdio.h>
#include <stdlib.h>

int *crearArreglo(int n, int valor)
{
    int *a = malloc(n * sizeof *a);
    if (a == NULL) return NULL;
    for (int i = 0; i < n; i++)
        a[i] = valor;
    return a;
}

void mostrar(const int *a, int n)
{
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void)
{
    int *unos = crearArreglo(5, 1);
    int *sietes = crearArreglo(3, 7);
    if (unos == NULL || sietes == NULL) return 1;
    mostrar(unos, 5);
    mostrar(sietes, 3);
    free(unos);
    free(sietes);
    return 0;
}
```
:::
:::

:::tarea AB | T3. Agrandar un arreglo a mano (completa sin pistas) | 25 min | Problema por completar, Desvanecimiento de guía
**Contexto.** Para entender qué hace `realloc` por dentro, escribe tu propia versión **sin usarlo**: reservar uno nuevo, copiar, rellenar con ceros, liberar el viejo y devolver el nuevo.

```c blank title="agrandar.c"
#include <stdio.h>
#include <stdlib.h>

int *agrandar(int *viejo, int n, int nuevoN)
{
    int *nuevo = __1__;
    if (nuevo == NULL) return NULL;
    for (int i = 0; i < __2__; i++)
        nuevo[i] = __3__;
    for (int i = n; i < nuevoN; i++)
        nuevo[i] = 0;
    __4__;
    return __5__;
}

int main(void)
{
    int n = 3;
    int *a = malloc(n * sizeof *a);
    if (a == NULL) return 1;
    a[0] = 4; a[1] = 5; a[2] = 6;
    a = agrandar(a, n, 6);
    if (a == NULL) return 1;
    n = 6;
    a[3] = 7;
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    __6__;
    return 0;
}
```

:::solucion | T3
{{c:1}} `malloc(nuevoN * sizeof *nuevo)` · {{c:2}} `n` · {{c:3}} `viejo[i]` · {{c:4}} `free(viejo)` · {{c:5}} `nuevo` · {{c:6}} `free(a)`

```c run title="agrandar.c"
#include <stdio.h>
#include <stdlib.h>

int *agrandar(int *viejo, int n, int nuevoN)
{
    int *nuevo = malloc(nuevoN * sizeof *nuevo);
    if (nuevo == NULL) return NULL;
    for (int i = 0; i < n; i++)
        nuevo[i] = viejo[i];
    for (int i = n; i < nuevoN; i++)
        nuevo[i] = 0;
    free(viejo);
    return nuevo;
}

int main(void)
{
    int n = 3;
    int *a = malloc(n * sizeof *a);
    if (a == NULL) return 1;
    a[0] = 4; a[1] = 5; a[2] = 6;
    a = agrandar(a, n, 6);
    if (a == NULL) return 1;
    n = 6;
    a[3] = 7;
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    free(a);
    return 0;
}
```
`a = agrandar(a, …)` no produce fuga porque la función libera el bloque viejo antes de devolver el nuevo. (Un detalle: si `agrandar` fallara, el bloque viejo no se liberaría; `realloc` tiene el mismo comportamiento, por eso se usa con un puntero temporal.)
:::
:::

:::tarea AB | T4. Lista de compras que crece (problema convencional) | 35 min | Variabilidad
**Contexto.** Lee artículos (una palabra cada uno) hasta escribir `fin`. Guárdalos en un arreglo dinámico de `Articulo` (`typedef struct { char nombre[30]; } Articulo;`) que empieza con capacidad 2 y **duplica** su capacidad con `realloc` cuando se llena (informa cada crecimiento). Al final muestra la lista numerada, el número de artículos y la capacidad final; libera la memoria.

:::solucion | T4
```c run title="compras.c" stdin="leche\npan\nhuevo\nfruta\narroz\nfin\n"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct { char nombre[30]; } Articulo;
int main(void)
{
    int cap = 2, n = 0;
    Articulo *lista = malloc(cap * sizeof *lista);
    if (lista == NULL) return 1;
    char art[30];
    while (scanf("%29s", art) == 1 && strcmp(art, "fin") != 0)
    {
        if (n == cap)
        {
            Articulo *tmp = realloc(lista, 2 * cap * sizeof *lista);
            if (tmp == NULL) { free(lista); return 1; }
            lista = tmp;
            cap *= 2;
            printf("(capacidad: %d)\n", cap);
        }
        strcpy(lista[n++].nombre, art);
    }
    for (int i = 0; i < n; i++) printf("%d. %s\n", i + 1, lista[i].nombre);
    printf("%d articulos, capacidad %d\n", n, cap);
    free(lista);
    return 0;
}
```
:::
:::

:::tarea A | T5. n datos, n decidido en ejecución: ¿de cuántas formas? (solución libre) | 25 min | Solución libre
**Contexto.** Necesitas guardar `n` enteros, con `n` leído del teclado. **Escribe todas las soluciones que conozcas** y compáralas en una tabla (¿es C estándar?, ¿hay límite?, ¿quién libera?, ¿puede crecer?): arreglo con tamaño máximo, arreglo de longitud variable (VLA), `malloc`, `calloc`…

:::solucion | T5
```c run title="cuatro_formas.c" stdin="4\n"
#include <stdio.h>
#include <stdlib.h>
#define MAX 100
int main(void)
{
    int n;
    scanf("%d", &n);
    if (n < 1 || n > MAX) return 1;
    int fijo[MAX];                              // 1) maximo fijo
    int vla[n];                                 // 2) VLA
    int *din = malloc(n * sizeof *din);         // 3) malloc (sin inicializar)
    int *ceros = calloc(n, sizeof *ceros);      // 4) calloc (en ceros)
    if (din == NULL || ceros == NULL) return 1;
    for (int i = 0; i < n; i++) fijo[i] = vla[i] = din[i] = i * i;
    printf("%d %d %d %d\n", fijo[n - 1], vla[n - 1], din[n - 1], ceros[n - 1]);
    free(din);
    free(ceros);
    return 0;
}
```
| Forma | ¿Estándar? | ¿Límite? | ¿Quién libera? | ¿Crece? |
|---|---|---|---|---|
| `int a[MAX]` | sí | sí (MAX) | automático | no |
| `int a[n]` (VLA) | C99 (opcional desde C11) | pila pequeña, sin aviso de error | automático | no |
| `malloc(n * sizeof(int))` | sí | memoria disponible (avisa con `NULL`) | tú (`free`) | sí, con `realloc` |
| `calloc(n, sizeof(int))` | sí, y en ceros | memoria disponible (avisa con `NULL`) | tú (`free`) | sí, con `realloc` |
:::
:::

:::tarea B | T6. Encuentra las fugas (autoexplicación) | 25 min | Autoexplicación, Reversión de la experiencia
**Explica** qué está mal en cada función, qué consecuencia tiene y cómo corregirla.

```c blank title="fugas.c"
void a(void)
{
    int *p = malloc(50 * sizeof *p);
    if (p[0] > 10) return;
    free(p);
}
void b(void)
{
    int *q = malloc(sizeof *q);
    int *r = malloc(sizeof *r);
    q = r;
    free(q);
    free(r);
}
void c(void)
{
    double *m = malloc(8 * sizeof *m);
    m++;
    free(m);
}
```

{{lineas:5}}

:::solucion | T6
**a:** el `return` temprano salta el `free` → fuga cuando `p[0] > 10` (además `p[0]` no está inicializado y no se verificó `NULL`). Liberar antes de cada `return`. **b:** `q = r` pierde el primer bloque (fuga) y luego `free(q)` y `free(r)` liberan **dos veces** el segundo (doble liberación). Corrección: `free(q); q = r;` y un solo `free` final. **c:** después de `m++`, `m` ya no es la dirección que devolvió `malloc`: `free(m)` es comportamiento indefinido (y el bloque original se fuga). Conserva el puntero original para liberarlo.
:::
:::

:::tarea B | T7. Pila y montón, línea por línea (imaginación) | 25 min | Imaginación
**Sin ejecutar**, dibuja la pila y el montón después de cada línea marcada. Al final: ¿cuántos bloques quedan sin liberar? ¿qué imprime?

```c check title="imagina_heap.c"
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int *a = malloc(sizeof *a);       // (1)
    *a = 5;
    int *b = malloc(3 * sizeof *b);   // (2)
    b[0] = 1; b[1] = 2; b[2] = 3;
    int *c = a;                       // (3)
    *c = *c + b[2];                   // (4)
    free(a);                          // (5)
    a = malloc(sizeof *a);            // (6)
    *a = *b;
    c = NULL;                         // (7)
    printf("%d %d\n", *a, b[1]);
    free(b);
    return 0;
}
```

{{lineas:4}}

:::solucion | T7
(1) bloque X = 5 apuntado por `a`. (2) bloque Y = {1, 2, 3} apuntado por `b`. (3) `c` también apunta a X. (4) X = 5 + 3 = 8. (5) X se libera: `c` queda **colgante**. (6) nuevo bloque Z = `*b` = 1, apuntado por `a`. (7) `c` deja de colgar. Imprime `1 2`. Al final se libera Y, pero **Z nunca se libera**: queda 1 bloque (un `int`) sin liberar. (Por brevedad, este ejemplo no verifica `NULL`.)

```c run title="imagina_heap.c"
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int *a = malloc(sizeof *a);
    *a = 5;
    int *b = malloc(3 * sizeof *b);
    b[0] = 1; b[1] = 2; b[2] = 3;
    int *c = a;
    *c = *c + b[2];
    free(a);
    a = malloc(sizeof *a);
    *a = *b;
    c = NULL;
    printf("%d %d\n", *a, b[1]);
    free(b);
    return 0;
}
```
:::
:::

:::tarea AB | T8. Cola de turnos de una clínica (reto colaborativo) | 45 min | Memoria colectiva de trabajo, Variabilidad
:::colab | Organización
Equipos de 4, niveles mezclados. Una cola: los pacientes **llegan al final** y se **atienden por el frente**. `typedef struct Turno { int numero; char nombre[20]; struct Turno *sig; } Turno;` y `typedef struct { Turno *frente, *final; int creados, liberados; } Cola;`. Las funciones reciben la cola **por dirección** (`Cola *c`) para poder modificar sus punteros.
- **Integrante 1:** `void llegar(Cola *c, int num, const char nombre[])` (crea el nodo con `malloc` y lo enlaza al final).
- **Integrante 2:** `bool atender(Cola *c)` (muestra y libera el primero con `free`; cuidado si la cola queda vacía).
- **Integrante 3:** `void mostrar(const Cola *c)` y el menú (`L nombre`, `A`, `M`, `S`).
- **Integrante 4:** `void vaciar(Cola *c)` al salir: liberar **todos** los turnos pendientes y verificar con los contadores que hubo tantos `free` como `malloc`.
:::

:::solucion | T8
```c run title="cola_turnos.c" stdin="L Ana\nL Beto\nL Carla\nA\nM\nL Dario\nA\nS\n"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
typedef struct Turno { int numero; char nombre[20]; struct Turno *sig; } Turno;
typedef struct { Turno *frente, *final; int creados, liberados; } Cola;

void llegar(Cola *c, int num, const char nombre[])
{
    Turno *t = malloc(sizeof *t);
    if (t == NULL) return;
    t->numero = num;
    strcpy(t->nombre, nombre);
    t->sig = NULL;
    c->creados++;
    if (c->final == NULL) c->frente = c->final = t;
    else { c->final->sig = t; c->final = t; }
}
bool atender(Cola *c)
{
    if (c->frente == NULL) return false;
    Turno *t = c->frente;
    printf("Atendiendo turno %d: %s\n", t->numero, t->nombre);
    c->frente = t->sig;
    if (c->frente == NULL) c->final = NULL;
    free(t);
    c->liberados++;
    return true;
}
void mostrar(const Cola *c)
{
    printf("En espera:");
    for (const Turno *t = c->frente; t; t = t->sig) printf(" [%d %s]", t->numero, t->nombre);
    printf("\n");
}
void vaciar(Cola *c)
{
    while (c->frente) { Turno *s = c->frente->sig; free(c->frente); c->liberados++; c->frente = s; }
    c->final = NULL;
}
int main(void)
{
    Cola cola = {NULL, NULL, 0, 0};
    int siguiente = 1;
    char op;
    while (scanf(" %c", &op) == 1 && op != 'S')
    {
        if (op == 'L') { char n[20]; scanf("%19s", n); llegar(&cola, siguiente++, n); }
        else if (op == 'A') { if (!atender(&cola)) printf("No hay pacientes\n"); }
        else if (op == 'M') mostrar(&cola);
    }
    vaciar(&cola);
    printf("malloc: %d  free: %d\n", cola.creados, cola.liberados);
    return 0;
}
```
:::
:::

# 4. Protocolo verbal {.protocolo}

:::protocolo | Protocolo verbal · Una matriz dinámica: reservar y liberar en el orden correcto | Modalidad, Ejemplo resuelto
*Guion para narración (≈ 4 min) sobre el diagrama de pila y montón, segmentado para que el estudiante controle el ritmo.*

**Problema:** «Crear una matriz de `f × c` enteros con tamaño leído en ejecución, llenarla con `i * c + j`, mostrarla y liberarla sin fugas».

**Segmento 1 — Dibujar la forma.** {{como}} Dibujo en el montón un arreglo de `f` **punteros** (uno por fila) y, para cada uno, una fila de `c` enteros. En la pila solo queda `int **m`. {{porque}} Una matriz dinámica no es un bloque único: son `f + 1` bloques. Verlo me dice que necesitaré `f + 1` llamadas a `free`.

**Segmento 2 — Reservar de afuera hacia adentro.** {{como}} Primero `m = malloc(f * sizeof *m);`, luego en un ciclo `m[i] = malloc(c * sizeof *m[i]);`. {{porque}} No puedo guardar la dirección de una fila en `m[i]` si el arreglo `m` todavía no existe. (`sizeof *m` es el tamaño de un puntero a fila; `sizeof *m[i]`, el de un `int`.)

**Segmento 3 — Liberar de adentro hacia afuera.** {{como}} Primero cada fila: `for (i…) free(m[i]);`, y al final `free(m);`. {{porque}} Si liberara primero `m`, perdería las direcciones de las filas: serían `f` fugas. Es el orden inverso al de la reserva, como quitarse la ropa al revés de como uno se vistió.

**Segmento 4 — Contar para verificar.** {{como}} Cuento: hubo `1 + f` llamadas a `malloc` y `f + 1` a `free`. Además compilo con `-g -fsanitize=address` para que la herramienta confirme que no hay fugas. {{porque}} Con memoria dinámica, «funciona» no es suficiente: un programa con fugas también imprime bien.

```c run title="matriz_dinamica.c" stdin="3 4\n"
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int f, c;
    scanf("%d %d", &f, &c);
    int **m = malloc(f * sizeof *m);       // arreglo de f punteros a fila
    if (m == NULL) return 1;
    for (int i = 0; i < f; i++)
        m[i] = malloc(c * sizeof *m[i]);   // cada fila: c enteros (por brevedad no se verifica NULL)
    for (int i = 0; i < f; i++)
        for (int j = 0; j < c; j++)
            m[i][j] = i * c + j;
    for (int i = 0; i < f; i++)
    {
        for (int j = 0; j < c; j++) printf("%4d", m[i][j]);
        printf("\n");
    }
    for (int i = 0; i < f; i++)
        free(m[i]);                        // primero las filas
    free(m);                               // despues el arreglo de punteros
    return 0;
}
```
:::

# 5. Evaluación {.evaluacion}

:::recall | 5.1 Recall test · conocimiento declarativo
1. ¿En qué zona de memoria viven las variables locales y en cuál los bloques creados con `malloc`?
2. ¿Qué devuelve `malloc(10 * sizeof(int))`? ¿Y si no hay memoria suficiente?
3. ¿Con qué función se libera un bloque creado con `malloc` o `calloc`?
4. ¿Qué es una fuga de memoria?
5. ¿Qué es un puntero colgante?
6. Verdadero o falso: un bloque creado con `malloc` dentro de una función se libera automáticamente al terminar la función.
7. ¿Por qué conviene asignar `NULL` a un puntero después de `free`?
8. ¿Qué diferencia hay entre `malloc` y `calloc`?
9. ¿En qué orden se liberan las filas y el arreglo de punteros de una matriz dinámica?
10. ¿Por qué el resultado de `realloc` se guarda en un puntero temporal?
:::

:::compr | 5.2 Comprehension test · conocimiento procedimental
**P1. Analiza la salida** y di cuántos bloques quedan sin liberar:

```c check title="p1.c"
#include <stdio.h>
#include <stdlib.h>
int *f(int n)
{
    int *a = malloc(n * sizeof *a);
    for (int i = 0; i < n; i++) a[i] = n - i;
    return a;
}
int main(void)
{
    int *x = f(3);
    int *y = f(2);
    printf("%d\n", x[0] + y[1]);
    x = y;
    free(x);
    return 0;
}
```

**P2. Corrige:** `int *v = malloc(n); for (int i = 0; i <= n; i++) v[i] = i; free(v); v[0] = 1;`

**P3.** Escribe `double *copiaInvertida(const double *a, int n)` que devuelva un **nuevo** arreglo dinámico con los elementos en orden inverso, y el `main` que la use y libere todo.

**P4. Desarrolla** un programa que lea `n` nombres en un arreglo dinámico (`typedef struct { char s[20]; } Nombre;`), elimine los repetidos creando un **segundo** arreglo dinámico del tamaño justo, muestre ambos y libere toda la memoria.
:::

:::registro | 5.3 Autorregistro
<ul class="checks">
<li>Distingo pila y montón y sé cuánto vive cada objeto.</li>
<li>Reservo con <code>malloc</code>/<code>calloc</code> (multiplicando por <code>sizeof</code>), verifico <code>NULL</code> y libero con <code>free</code>.</li>
<li>Detecto fugas, punteros colgantes y dobles liberaciones.</li>
<li>Hago crecer un arreglo con <code>realloc</code> sin perder el bloque original.</li>
</ul>
**Esfuerzo mental invertido** (1 = muy, muy bajo · 9 = muy, muy alto):
<div class="escala"><span><b>1</b></span><span><b>2</b></span><span><b>3</b></span><span><b>4</b></span><span><b>5</b></span><span><b>6</b></span><span><b>7</b></span><span><b>8</b></span><span><b>9</b></span></div>
:::

:::solucion | Evaluación 5.1 (recall)
1 Pila; montón · 2 La dirección (un `void *`) del primero de 10 enteros reservados en el montón; si no hay memoria, `NULL` · 3 `free` · 4 Memoria reservada que ya no puede liberarse porque se perdió su dirección · 5 Un puntero que apunta a memoria ya liberada (o que ya no es válida) · 6 Falso: solo el puntero local desaparece; el bloque sigue reservado · 7 Para que no quede colgante: `free(NULL)` no hace nada y `if (p)` detecta que ya no apunta a nada · 8 `malloc(bytes)` deja la memoria sin inicializar; `calloc(n, tamaño)` reserva `n` elementos y los pone en cero · 9 Primero cada fila y después el arreglo de punteros · 10 Porque si `realloc` falla devuelve `NULL` y el bloque original sigue reservado; asignarlo directo perdería su única dirección.
:::

:::solucion | Evaluación 5.2 (comprehension)
**P1.** `x = {3, 2, 1}`, `y = {2, 1}`; imprime `3 + 1 = 4`. Después `x = y` pierde el bloque de 3 elementos (fuga) y se libera solo el de `y`: **1 bloque** sin liberar.

```c run title="p1.c"
#include <stdio.h>
#include <stdlib.h>
int *f(int n)
{
    int *a = malloc(n * sizeof *a);
    for (int i = 0; i < n; i++) a[i] = n - i;
    return a;
}
int main(void)
{
    int *x = f(3);
    int *y = f(2);
    printf("%d\n", x[0] + y[1]);
    x = y;
    free(x);
    return 0;
}
```

**P2.** `malloc(n)` reserva `n` **bytes**: debe ser `malloc(n * sizeof *v)` (y verificar `NULL`); el ciclo debe ser `i < n` (con `<=` escribe fuera del bloque); `v[0] = 1` después de `free` usa un puntero colgante: hay que eliminarlo o moverlo antes del `free`.

**P3.**

```c run title="p3.c"
#include <stdio.h>
#include <stdlib.h>
double *copiaInvertida(const double *a, int n)
{
    double *r = malloc(n * sizeof *r);
    if (r == NULL) return NULL;
    for (int i = 0; i < n; i++) r[i] = a[n - 1 - i];
    return r;
}
int main(void)
{
    double v[4] = {1.5, 2.5, 3.5, 4.5};
    double *inv = copiaInvertida(v, 4);
    if (inv == NULL) return 1;
    for (int i = 0; i < 4; i++) printf("%.1f ", inv[i]);
    printf("\n");
    free(inv);
    return 0;
}
```

**P4.**

```c run title="p4.c" stdin="6\nAna Luis Ana Eva Luis Mia\n"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
typedef struct { char s[20]; } Nombre;
bool estaAntes(const Nombre *a, int i)
{
    for (int j = 0; j < i; j++)
        if (strcmp(a[j].s, a[i].s) == 0) return true;
    return false;
}
int main(void)
{
    int n;
    scanf("%d", &n);
    Nombre *a = malloc(n * sizeof *a);
    if (a == NULL) return 1;
    for (int i = 0; i < n; i++) scanf("%19s", a[i].s);
    int unicos = 0;
    for (int i = 0; i < n; i++)
        if (!estaAntes(a, i)) unicos++;
    Nombre *b = malloc(unicos * sizeof *b);
    if (b == NULL) { free(a); return 1; }
    int k = 0;
    for (int i = 0; i < n; i++)
        if (!estaAntes(a, i)) b[k++] = a[i];        // una estructura se copia con =
    for (int i = 0; i < n; i++) printf("%s ", a[i].s);
    printf("| ");
    for (int i = 0; i < unicos; i++) printf("%s ", b[i].s);
    printf("\n");
    free(a);
    free(b);
    return 0;
}
```
:::
