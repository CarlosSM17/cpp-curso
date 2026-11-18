# Entorno para regenerar el sitio y los PDF (gcc, Graphviz, Python, Chromium).
#
#   docker build -t curso-c-clt4bp engine
#   docker run --rm -v "$PWD":/curso -w /curso curso-c-clt4bp python3 engine/web.py
#   docker run --rm -v "$PWD":/curso -w /curso curso-c-clt4bp python3 engine/render.py temas/01_estructura.md
#
# Se usa GCC 14 (la misma serie que el botón de Compiler Explorer): a partir de esa
# versión, llamar a una función sin declararla es un error y no solo una advertencia.
FROM mcr.microsoft.com/playwright/python:v1.48.0-noble

RUN apt-get update \
 && apt-get install -y --no-install-recommends gcc-14 libc6-dev make graphviz fonts-inter fonts-dejavu-core \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --break-system-packages \
        markdown==3.7 pyyaml==6.0.2 pygments==2.18.0 pypdf==5.1.0 playwright==1.48.0

# CC: compilador que usa engine/render.py; LANG: mensajes de gcc con comillas tipográficas.
ENV CC=gcc-14 LANG=C.UTF-8
