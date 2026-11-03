// Inyectado con -include solo para generar el material: emula una terminal.
// Cada linea de entrada se "teclea" (y se muestra marcada) cuando el programa
// necesita leer de ella, como ocurre en una consola real.
#include <iostream>
#include <cstdio>
#include <streambuf>
#include <string>
namespace clt4bp_echo {
struct EchoBuf : std::streambuf {
    std::string linea;
    int_type underflow() override {
        linea.clear();
        int c;
        while ((c = std::fgetc(stdin)) != EOF) {
            linea.push_back(static_cast<char>(c));
            if (c == '\n') break;
        }
        if (linea.empty()) return traits_type::eof();
        std::cout.put('\x01');
        std::cout.write(linea.data(), static_cast<std::streamsize>(linea.size()));
        std::cout.put('\x02');
        setg(&linea[0], &linea[0], &linea[0] + linea.size());
        return traits_type::to_int_type(linea[0]);
    }
};
struct Installer { EchoBuf buf; Installer() { std::cin.rdbuf(&buf); } };
static Installer instalador;
}
