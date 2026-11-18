/* Se enlaza solo para generar el material: emula una terminal.
   Cada línea de entrada se «teclea» (y se muestra marcada entre \x01 y \x02)
   cuando el programa necesita leerla, como ocurre en una consola real.
   Reemplaza stdin por un FILE propio (fopencookie, glibc) antes de main;
   scanf, getchar y fgets leen de él sin cambiar el programa del alumno. */
#define _GNU_SOURCE
#include <stdio.h>
#include <sys/types.h>

static FILE *clt4bp_entrada_real;

static ssize_t clt4bp_leer(void *cookie, char *buf, size_t size)
{
    (void)cookie;
    size_t n = 0;
    int c;
    while (n < size && (c = fgetc(clt4bp_entrada_real)) != EOF) {
        buf[n++] = (char)c;
        if (c == '\n')
            break;
    }
    if (n == 0)
        return 0;
    fflush(stdout);              /* lo que el programa imprimió antes de leer va primero */
    fputc('\x01', stdout);
    fwrite(buf, 1, n, stdout);
    fputc('\x02', stdout);
    fflush(stdout);
    return (ssize_t)n;
}

__attribute__((constructor)) static void clt4bp_instalar(void)
{
    /* Búfer por línea: si el programa termina con _exit (p. ej., al reportar
       LeakSanitizer una fuga), lo ya impreso no se pierde. */
    setvbuf(stdout, NULL, _IOLBF, 0);
    cookie_io_functions_t f = {.read = clt4bp_leer};
    FILE *eco = fopencookie(NULL, "r", f);
    if (eco) {
        clt4bp_entrada_real = stdin;
        stdin = eco;
    }
}
