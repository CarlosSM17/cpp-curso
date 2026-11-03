"""Generador del curso web interactivo (sitio estático para GitHub Pages).

Uso:  python3 engine/web.py            → genera docs/ (publicar con GitHub Pages: rama main, carpeta /docs)

Reutiliza el motor de los PDF (render.py) en modo WEB: los programas se compilan y
ejecutan con g++ (con caché), los diagramas salen como SVG en línea y las soluciones
quedan junto a cada tarea, plegadas.
"""
import base64
import html
import json
import re
import shutil
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import render as R  # noqa: E402
import web_diag  # noqa: E402

R.WEB = True
ROOT = R.ROOT
SITE = ROOT / "docs"
ASSETS_SRC = ROOT / "engine" / "web"

BLOQUES = [
    ("I", "Fundamentos", ["01", "02", "03", "04", "05"]),
    ("II", "Repetición y arreglos", ["06", "07", "08", "09"]),
    ("III", "Modularidad y datos", ["10", "11", "12", "13"]),
    ("IV", "Memoria, archivos y objetos", ["14", "15", "16", "17"]),
]
BLOQUE_DE = {n: b for b, _, ns in BLOQUES for n in ns}

PASOS = [
    ("soporte", "Información de soporte", "Soporte",
     "Los conceptos y modelos mentales del tema, uno por uno. Léela antes de las tareas y vuelve a ella cuando la necesites."),
    ("procedimental", "Información procedimental", "Procedimental",
     "Sintaxis, reglas y errores frecuentes. Tenla a la vista mientras resuelves las tareas."),
    ("tareas", "Tareas de aprendizaje", "Tareas",
     "De menor a mayor complejidad: la ayuda se retira tarea con tarea. Intenta cada una antes de abrir la solución."),
    ("protocolo", "Protocolo verbal", "Protocolo verbal",
     "Una experta resuelve un problema en voz alta: qué hace (cómo) y por qué lo hace."),
    ("evaluacion", "Evaluación", "Evaluación",
     "Recall test, comprehension test y autorregistro. Tus respuestas se guardan en este navegador."),
]


# ------------------------------------------------------------------ utilidades
def esc(s):
    return html.escape(str(s), quote=True)


def md_inline(s):
    return R.md_inline(s)


def leer_tema(path):
    src = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", src, re.S)
    return yaml.safe_load(m.group(1)), m.group(2)


def renderizar(path):
    meta, body = leer_tema(path)
    ctx = R.Ctx(path.stem)
    body = R.process_fences(body, ctx)
    body = R.process_boxes(body, ctx)
    h = R.md_to_html(body, ctx)
    return meta, h, ctx


def secciones(h):
    """Parte el HTML por <h1 class="…"> y devuelve [(clase, título, contenido)]."""
    out = []
    ms = list(re.finditer(r'<h1[^>]*class="(\w+)"[^>]*>(.*?)</h1>', h, re.S))
    for i, m in enumerate(ms):
        fin = ms[i + 1].start() if i + 1 < len(ms) else len(h)
        cont = h[m.end():fin]
        cont = re.sub(r'^\s*<p class="h1-sub[^"]*">.*?</p>', "", cont, count=1, flags=re.S)
        out.append((m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip(), cont))
    return out


def slug(s):
    s = re.sub(r"<[^>]+>", "", s).lower()
    tr = str.maketrans("áéíóúüñ", "aeiouun")
    s = s.translate(tr)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60] or "s"


def ids_h2(h, prefijo=""):
    usados = set()
    toc = []

    def rep(m):
        tag, attrs, inner = m.group(1), m.group(2), m.group(3)
        if 'id="' in attrs:
            return m.group(0)
        txt = re.sub(r"<[^>]+>", "", inner)
        base = prefijo + slug(txt)
        k, i = base, 2
        while k in usados:
            k = f"{base}-{i}"
            i += 1
        usados.add(k)
        toc.append((tag, k, txt))
        return f'<{tag} id="{k}"{attrs}>{inner}</{tag}>'
    h = re.sub(r"<(h2|h3)([^>]*)>(.*?)</\1>", rep, h, flags=re.S)
    return h, toc


def envolver_tablas(h):
    """Envuelve las tablas de contenido (no las de código) en un contenedor con desplazamiento horizontal."""
    out, pila, pos = [], [], 0
    for m in re.finditer(r"<table\b[^>]*>|</table>", h):
        out.append(h[pos:m.start()])
        tok = m.group(0)
        if tok.startswith("</"):
            out.append(tok + ("</div>" if pila and pila.pop() else ""))
        else:
            envuelve = 'class="src"' not in tok and "tabla-scroll" not in h[max(0, m.start() - 40):m.start()]
            pila.append(envuelve)
            out.append(('<div class="tabla-scroll">' if envuelve else "") + tok)
        pos = m.end()
    out.append(h[pos:])
    return "".join(out)


def pdf_de(meta):
    return f"pdf/{meta['archivo']}.pdf"


# ------------------------------------------------------------------ plantilla
ICONO = """<svg class="logo" viewBox="0 0 40 40" aria-hidden="true"><path d="M2 15.5 H38" stroke="var(--ra)" stroke-width="4.5" stroke-linecap="round"/><path d="M2 24.5 H38" stroke="var(--rb)" stroke-width="4.5" stroke-linecap="round"/><rect x="13" y="7" width="14" height="26" rx="7" fill="var(--surface)" stroke="var(--ink)" stroke-width="3"/></svg>"""

NAV = [("index.html", "Mapa del curso", "mapa"), ("diagnostico.html", "Diagnóstico", "diagnostico"),
       ("progreso.html", "Mi progreso", "progreso"), ("glosario.html", "Glosario", "glosario"),
       ("guia.html", "Guía docente", "guia")]


def pagina(titulo, cuerpo, actual, data, desc=""):
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{u}"{cur if k == actual else ""}>{t}</a>' for u, t, k in NAV)
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc(desc or 'Curso interactivo de programación básica en C++ diseñado con el mapa de ruta CLT4BP.')}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/fuentes.css">
<link rel="stylesheet" href="assets/curso.css">
<script>try{{var t=localStorage.getItem('clt4bp-tema');if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}document.documentElement.classList.add('js');</script>
</head>
<body>
<a class="saltar" href="#contenido">Saltar al contenido</a>
<header class="sitio">
  <a class="marca" href="index.html">{ICONO}<span><b>Programación básica en C++</b><small>Curso interactivo con el mapa de ruta CLT4BP</small></span></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-principal">Menú</button>
  <nav id="nav-principal" class="nav" aria-label="Secciones del curso">{nav}
    <button class="tema-btn" type="button" title="Cambiar entre modo claro y oscuro"><span class="tema-ico" aria-hidden="true"></span><span class="tema-txt">Tema</span></button>
  </nav>
</header>
<main id="contenido">
{cuerpo}
</main>
<footer class="pie">
  <p>Material diseñado con el modelo instruccional <b>mapa de ruta CLT4BP</b> (Sandoval Medina, 2026): teoría de la carga cognitiva, 4C/ID, ARCS, instrucción diferenciada y protocolos verbales.</p>
  <p>Fuentes: Betancourt Uscátegui y Polanco Guzmán (2021), <i>115 ejercicios resueltos de programación C++</i>; Lospinoso (2019), <i>C++ Crash Course</i>. Los programas se compilaron con g++ (C++20) y sus salidas son reales.</p>
  <p>Tu progreso se guarda solo en este navegador. Puedes exportarlo desde <a href="progreso.html">Mi progreso</a>.</p>
</footer>
<script src="assets/datos.js"></script>
<script>window.PAGE={json.dumps(data, ensure_ascii=False)};</script>
<script src="assets/curso.js"></script>
</body>
</html>
"""


# ------------------------------------------------------------------ tema
def tareas_de(md):
    out = []
    for m in re.finditer(r"^:::tarea\s+(A|B|AB)\s*\|\s*(T\d+)\.\s*([^|]+?)\s*\|", md, re.M):
        out.append({"id": m.group(2).lower(), "ruta": m.group(1), "titulo": m.group(3).strip()})
    return out


def glosario_tabla(gl, con_tema=None):
    filas = []
    for es, en, sig in gl:
        filas.append(f"<tr><td><b>{md_inline(es)}</b></td><td><i>{md_inline(en)}</i></td><td>{md_inline(sig)}</td></tr>")
    return ('<div class="tabla-scroll"><table class="tb glos"><thead><tr><th>Español</th><th>English</th><th>Significado</th></tr></thead>'
            f'<tbody>{"".join(filas)}</tbody></table></div>')


def construir_tema(path, temas, i):
    meta, h, ctx = renderizar(path)
    h = h.replace("(ver Tema 00)", '(ver la <a href="guia.html">guía docente</a>)')
    h = envolver_tablas(h)
    num = meta["num"]
    bloque = BLOQUE_DE[num]
    secs = {c: (t, cont) for c, t, cont in secciones(h)}
    md = path.read_text()
    tareas = tareas_de(md)

    rail = []
    paneles = []
    for k, (clave, titulo, corto, desc) in enumerate(PASOS, 1):
        if clave not in secs:
            continue
        cont = secs[clave][1]
        rail.append(f'<li><a href="#{clave}" data-paso="{clave}" class="est est-{clave}"><span class="est-pt" aria-hidden="true"></span>'
                    f'<span class="est-t"><small>Paso {k}</small>{corto}</span></a></li>')
        sig = ""
        if k < len(PASOS):
            nk, nt = PASOS[k][0], PASOS[k][1]
            sig = f'<a class="btn btn-sig" href="#{nk}" data-ir="{nk}">Siguiente paso: {nt}</a>'
        else:
            sig = '<a class="btn btn-sig" href="#glosario" data-ir="glosario">Ver glosario y fuentes</a>'
        extra = ""
        if clave == "tareas":
            extra = '<div class="aviso-ruta" data-bloque="' + bloque + '"></div>'
        paneles.append(f"""<section class="panel p-{clave}" id="{clave}" data-paso="{clave}" aria-labelledby="h-{clave}">
<header class="panel-h"><p class="panel-n">Paso {k} de 5</p><h2 id="h-{clave}">{titulo}</h2><p>{desc}</p></header>
{extra}<div class="contenido">{cont}</div>
<footer class="panel-f"><button class="btn btn-hecho" type="button" data-paso="{clave}" aria-pressed="false">Marcar este paso como terminado</button>{sig}</footer>
</section>""")

    fuentes = "".join(f"<li>{md_inline(f)}</li>" for f in meta.get("fuentes", []))
    paneles.append(f"""<section class="panel p-glosario" id="glosario" data-paso="glosario" aria-labelledby="h-glosario">
<header class="panel-h"><h2 id="h-glosario">Glosario y fuentes</h2><p>Términos clave en español e inglés, útiles para leer el <i>C++ Crash Course</i> y la documentación.</p></header>
<div class="contenido">{glosario_tabla(meta.get('glosario', []))}<h3>Fuentes del tema</h3><ul class="fuentes">{fuentes}</ul></div>
</section>""")
    ficha = R.ficha_html(meta)
    ficha = re.sub(r'<h1[^>]*>.*?</h1>\s*<p class="h1-sub[^"]*">.*?</p>', "", ficha, count=1, flags=re.S)
    ficha = envolver_tablas(ficha.replace("<h2>", "<h3>").replace("</h2>", "</h3>"))
    ficha = ficha.replace("(el diagnóstico de la Fase 1 decide la ruta; ver Tema 00)", '(el <a href="diagnostico.html">diagnóstico</a> de la Fase 1 decide la ruta; ver la <a href="guia.html">guía docente</a>)')
    paneles.append(f"""<section class="panel p-docente" id="docente" data-paso="docente" aria-labelledby="h-docente">
<header class="panel-h"><h2 id="h-docente">Ficha de diseño instruccional</h2><p>Para el docente: objetivos por ruta, evaluación, efectos de la teoría de la carga cognitiva por componente, instrucción diferenciada y plan de implementación (Fases 1 a 3 del modelo).</p></header>
<div class="contenido">{ficha}</div>
</section>""")
    rail_extra = ('<ul class="rail-extra"><li><a href="#glosario" data-paso="glosario">Glosario y fuentes</a></li>'
                  '<li><a href="#docente" data-paso="docente">Ficha docente</a></li>'
                  f'<li><a href="{pdf_de(meta)}" download>Descargar PDF</a></li></ul>')

    prev = temas[i - 1] if i > 0 else None
    nxt = temas[i + 1] if i + 1 < len(temas) else None
    navt = '<nav class="tema-nav" aria-label="Temas vecinos">'
    navt += (f'<a class="prev" href="tema-{prev["num"]}.html"><small>Tema anterior</small>{prev["num"]}. {esc(prev["corto"])}</a>' if prev else "<span></span>")
    navt += (f'<a class="next" href="tema-{nxt["num"]}.html"><small>Tema siguiente</small>{nxt["num"]}. {esc(nxt["corto"])}</a>' if nxt else '<a class="next" href="progreso.html"><small>Final del curso</small>Revisa tu progreso</a>')
    navt += "</nav>"
    bnom = next(n for b, n, _ in BLOQUES if b == bloque)
    cuerpo = f"""<div class="tema" data-num="{num}" data-bloque="{bloque}">
<section class="tema-hero">
  <div class="hero-est" aria-hidden="true"><span>{num}</span></div>
  <div class="hero-txt">
    <p class="hero-bloque"><a href="index.html#bloque-{bloque}">Bloque {bloque}: {bnom}</a></p>
    <h1>{md_inline(meta['titulo'])}</h1>
    <p class="lema">{md_inline(meta.get('lema', ''))}</p>
    <dl class="hero-meta"><div><dt>Duración sugerida</dt><dd>{esc(meta.get('duracion', ''))}</dd></div><div><dt>Antes de empezar</dt><dd>{md_inline(meta.get('previos', ''))}</dd></div></dl>
    <div class="selector-ruta" data-bloque="{bloque}"></div>
  </div>
</section>
<div class="tema-cuerpo">
  <nav class="rail" aria-label="Pasos del tema"><p class="rail-t">Ruta del tema</p><ol>{''.join(rail)}</ol>{rail_extra}</nav>
  <div class="paneles">{''.join(paneles)}</div>
</div>
{navt}
</div>"""
    data = {"tipo": "tema", "num": num, "bloque": bloque}
    return pagina(f"Tema {num}. {meta['corto']} · Programación básica en C++", cuerpo, "", data,
                  f"Tema {num}: {meta['titulo']}"), meta, tareas, ctx


# ------------------------------------------------------------------ portada
def construir_inicio(temas):
    filas = []
    for b, nom, nums in BLOQUES:
        items = []
        for t in temas:
            if t["num"] not in nums:
                continue
            items.append(f"""<li class="fila-tema" data-num="{t['num']}"><a href="tema-{t['num']}.html">
<span class="ft-num">{t['num']}</span><span class="ft-t"><b>{esc(t['corto'])}</b><small>{md_inline(t['titulo'])}</small></span>
<span class="ft-dur">{esc(t['duracion'].split('·')[0].strip())}</span><span class="ft-prog" aria-hidden="true"><i></i></span><span class="ft-estado"></span></a>
<a class="ft-pdf" href="{t['pdf']}" download title="Descargar el PDF del tema {t['num']}">PDF</a></li>""")
        filas.append(f"""<section class="bloque" id="bloque-{b}"><header><h3>Bloque {b}: {nom}</h3><p class="bloque-ruta" data-bloque="{b}"></p></header><ol class="lista-temas">{''.join(items)}</ol></section>""")
    pasos = "".join(f'<li class="paso-{k}"><b>{t}</b><span>{d}</span></li>' for k, t, _, d in PASOS)
    noscript = "".join(f'<li><a href="tema-{t["num"]}.html">{t["num"]}. {esc(t["corto"])}</a></li>' for t in temas)
    cuerpo = f"""<section class="inicio-hero">
  <div class="letrero"><p>17 paradas, 2 rutas</p><h1>Programación básica en C++</h1></div>
  <p class="lede">Un recorrido de la primera línea de código a las clases y objetos. Cada tema es una parada con cinco pasos; el diagnóstico de cada bloque te sugiere la ruta que más te conviene según lo que ya sabes.</p>
  <div class="acciones" id="acciones-inicio"><a class="btn btn-primario" href="diagnostico.html">Hacer el diagnóstico</a><a class="btn" href="tema-01.html">Empezar por el Tema 01</a></div>
</section>
<section class="mapa-sec" aria-labelledby="h-mapa">
  <h2 id="h-mapa" class="vh">Mapa de ruta del curso</h2>
  <div id="mapa" class="mapa"><noscript><ol>{noscript}</ol></noscript></div>
  <ul class="leyenda">
    <li><i class="ley-ra"></i><span><b>Ruta A</b> sin conocimientos previos: ejemplos resueltos, problemas por completar y guía que se retira poco a poco.</span></li>
    <li><i class="ley-rb"></i><span><b>Ruta B</b> con conocimientos previos: autoexplicación, imaginación, solución libre y retos colaborativos.</span></li>
    <li><i class="ley-est"></i><span>Parada: vacía sin empezar, con borde en curso, rellena al terminar sus cinco pasos.</span></li>
    <li><i class="ley-diag"></i><span>Diagnóstico al inicio de cada bloque: sugiere tu ruta.</span></li>
  </ul>
</section>
<section class="como" aria-labelledby="h-como">
  <h2 id="h-como">Cómo se recorre cada tema</h2>
  <p>Los cinco pasos siguen el modelo 4C/ID adaptado por el mapa de ruta CLT4BP. Marca cada paso como terminado al acabarlo: así se rellena la parada en el mapa.</p>
  <ol class="cinco">{pasos}</ol>
</section>
<section class="temas-sec" aria-labelledby="h-temas">
  <h2 id="h-temas">Los 17 temas</h2>
  {''.join(filas)}
</section>
<section class="docentes" aria-labelledby="h-doc">
  <h2 id="h-doc">Para docentes</h2>
  <p>Cada tema incluye su <b>ficha de diseño instruccional</b> (pestaña «Ficha docente»): objetivos por ruta, efectos de la carga cognitiva por componente, matriz de instrucción diferenciada y plan de implementación. La <a href="guia.html">guía docente</a> explica cómo aplicar las tres fases del modelo al curso, con los formatos de registro de la tesis.</p>
  <p>Los alumnos pueden exportar su progreso desde <a href="progreso.html">Mi progreso</a> (JSON o CSV) para entregarlo; incluye desempeño, esfuerzo mental y la encuesta de carga cognitiva de cada bloque.</p>
</section>"""
    return pagina("Programación básica en C++ · Curso interactivo CLT4BP", cuerpo, "mapa", {"tipo": "inicio"})


# ------------------------------------------------------------------ diagnóstico
def construir_diagnostico():
    bloques = []
    for b, nom, nums in BLOQUES:
        items = []
        for k, it in enumerate(web_diag.BLOQUES[b], 1):
            code = ""
            if it.get("code"):
                tbl, _ = R.code_table(it["code"], "cpp", {"nolines": False})
                code = f'<div class="codewrap">{tbl}</div>'
            opts = "".join(f'<li><label><input type="radio" name="d{b}-{k}" value="{j}"><span>{md_inline(o)}</span></label></li>' for j, o in enumerate(it["opts"]))
            tipo = "Lectura de código" if it.get("code") else "Concepto"
            items.append(f"""<li class="reactivo" data-ok="{it['ok']}"><fieldset><legend><span class="r-n">{k}</span><span class="r-tipo">{tipo}</span><span class="r-q">{md_inline(it['q'])}</span></legend>
{code}<ol class="opciones" type="a">{opts}</ol><p class="r-exp" hidden>{md_inline(it['exp'])}</p></fieldset></li>""")
        bloques.append(f"""<section class="diag-bloque" id="bloque-{b}" data-bloque="{b}">
<header><h2>Bloque {b}: {nom}</h2><p>Temas {nums[0]} a {nums[-1]} · 8 reactivos · unos 10 minutos</p><p class="diag-estado" data-bloque="{b}"></p></header>
<form class="diag-form" data-bloque="{b}"><ol class="reactivos">{''.join(items)}</ol>
<div class="diag-acciones"><button class="btn btn-primario" type="submit">Calificar el bloque {b}</button><button class="btn" type="reset">Borrar respuestas</button></div>
<div class="diag-res" role="status" aria-live="polite"></div></form>
</section>""")
    tabs = "".join(f'<a href="#bloque-{b}" class="diag-tab" data-bloque="{b}"><b>Bloque {b}</b><small>{nom}</small></a>' for b, nom, _ in BLOQUES)
    cuerpo = f"""<section class="pagina-h">
  <h1>Diagnóstico por bloque</h1>
  <p class="lede">Responde el diagnóstico de un bloque antes de empezarlo. Con 6 aciertos o más de 8 (70 %) te sugerimos la <b>Ruta B</b>; con menos, la <b>Ruta A</b>. La ruta solo cambia qué tareas ves primero: puedes cambiarla cuando quieras en cada tema.</p>
  <p class="nota-diag">Es la versión en línea, calificada automáticamente, de la prueba diagnóstica de la <a href="guia.html#3-3-prueba-diagnostica-de-entrada-bloques-i-y-ii">guía docente</a> (Fase 1 del modelo: conocimientos previos). Responde sin consultar el material: el objetivo es saber desde dónde empiezas.</p>
</section>
<nav class="diag-tabs" aria-label="Bloques del diagnóstico">{tabs}</nav>
{''.join(bloques)}"""
    return pagina("Diagnóstico · Programación básica en C++", cuerpo, "diagnostico", {"tipo": "diagnostico"})


# ------------------------------------------------------------------ progreso
ENCUESTA = [
    "Los temas tratados en la actividad fueron muy complejos.",
    "La actividad abordó código de programa que percibí como muy complejo.",
    "La actividad abordó conceptos y definiciones que percibí como muy complejos.",
    "Las instrucciones o explicaciones durante la actividad fueron muy confusas.",
    "Las instrucciones o explicaciones fueron, en términos de aprendizaje, muy ineficaces.",
    "Las instrucciones o explicaciones estaban llenas de lenguaje confuso.",
    "La actividad mejoró significativamente mi comprensión del/de los tema(s) tratado(s).",
    "La actividad mejoró significativamente mis conocimientos y comprensión de programación.",
    "La actividad mejoró significativamente mi comprensión del código de programa tratado.",
    "La actividad mejoró significativamente mi comprensión de los conceptos y definiciones.",
]


def construir_progreso():
    blq = []
    for b, nom, nums in BLOQUES:
        its = "".join(f"""<li><p>{esc(t)}</p><div class="escala10" role="radiogroup" aria-label="Respuesta al enunciado {k}">{''.join(f'<label><input type="radio" name="e{b}-{k}" value="{v}"><span>{v}</span></label>' for v in range(11))}</div></li>""" for k, t in enumerate(ENCUESTA, 1))
        blq.append(f"""<details class="encuesta" data-bloque="{b}"><summary><b>Bloque {b}: {nom}</b><span class="enc-res" data-bloque="{b}"></span></summary>
<form class="enc-form" data-bloque="{b}"><p class="enc-esc"><span>0: nada de acuerdo</span><span>10: totalmente de acuerdo</span></p><ol class="enc-items">{its}</ol>
<button class="btn btn-primario" type="submit">Guardar respuestas del bloque {b}</button><p class="enc-ok" role="status" aria-live="polite"></p></form></details>""")
    cuerpo = f"""<section class="pagina-h">
  <h1>Mi progreso</h1>
  <p class="lede">Tu avance, tu desempeño y tu esfuerzo mental en cada tema. Todo se guarda solo en este navegador: exporta el archivo si quieres entregarlo o continuar en otra computadora.</p>
</section>
<section class="prog-resumen" id="prog-resumen" aria-live="polite"></section>
<section class="prog-tabla-sec"><h2>Tema por tema</h2><div class="tabla-scroll"><table class="tb prog-tabla" id="prog-tabla"><thead><tr><th>Tema</th><th>Ruta</th><th>Pasos</th><th>Tareas</th><th>Huecos</th><th>Recall</th><th>Comprensión</th><th>Esfuerzo</th></tr></thead><tbody></tbody></table></div></section>
<section class="prog-graf-sec"><h2>Desempeño y esfuerzo mental</h2><p>Cada punto es un tema con recall test y esfuerzo registrados. Arriba a la izquierda queda lo que aprendiste con poco esfuerzo (alta eficiencia); abajo a la derecha, lo que más te costó: vale la pena repasarlo.</p><div id="grafica" class="grafica"></div></section>
<section class="prog-enc"><h2>Encuesta de carga cognitiva</h2><p>Al terminar cada bloque, indica qué tan de acuerdo estás con cada enunciado. Los enunciados 1 a 3 miden la carga intrínseca; 4 a 6, la extrínseca; 7 a 10, la pertinente (instrumento del anexo A.7 de la tesis, adaptado de Morrison, Dorn y Guzdial, 2014).</p>{''.join(blq)}</section>
<section class="prog-datos"><h2>Exportar o importar</h2>
<div class="acciones"><button class="btn btn-primario" type="button" id="exp-json">Descargar mi progreso (JSON)</button><button class="btn" type="button" id="exp-csv">Descargar resumen (CSV)</button>
<label class="btn"><input type="file" id="imp-json" accept="application/json,.json" hidden>Importar progreso (JSON)</label><button class="btn btn-peligro" type="button" id="borrar">Borrar todo mi progreso</button></div>
<p class="datos-msg" role="status" aria-live="polite"></p></section>"""
    return pagina("Mi progreso · Programación básica en C++", cuerpo, "progreso", {"tipo": "progreso"})


# ------------------------------------------------------------------ glosario
def construir_glosario(temas_meta):
    vistos = {}
    for meta in temas_meta:
        for es, en, sig in meta.get("glosario", []):
            k = es.lower()
            if k not in vistos:
                vistos[k] = [es, en, sig, []]
            vistos[k][3].append(meta["num"])
    filas = []
    for es, en, sig, nums in sorted(vistos.values(), key=lambda r: re.sub(r"[`*]", "", r[0]).lower().translate(str.maketrans("áéíóú", "aeiou"))):
        links = " ".join(f'<a href="tema-{n}.html#glosario">{n}</a>' for n in nums)
        texto = re.sub(r"[`*<>]", "", f"{es} {en} {sig}").lower()
        filas.append(f'<tr data-q="{esc(texto)}" data-temas="{" ".join(nums)}"><td><b>{md_inline(es)}</b></td><td><i>{md_inline(en)}</i></td><td>{md_inline(sig)}</td><td class="g-temas">{links}</td></tr>')
    opts = "".join(f'<option value="{m["num"]}">{m["num"]}. {esc(m["corto"])}</option>' for m in temas_meta)
    cuerpo = f"""<section class="pagina-h"><h1>Glosario bilingüe</h1>
<p class="lede">{len(filas)} términos de los 17 temas, en español e inglés. Escribe para filtrar o elige un tema.</p></section>
<div class="glos-filtros"><label><span>Buscar</span><input type="search" id="g-q" placeholder="puntero, loop, arreglo…" autocomplete="off"></label>
<label><span>Tema</span><select id="g-tema"><option value="">Todos los temas</option>{opts}</select></label><p id="g-n" role="status" aria-live="polite"></p></div>
<div class="tabla-scroll"><table class="tb glos glos-todo"><thead><tr><th>Español</th><th>English</th><th>Significado</th><th>Temas</th></tr></thead><tbody>{''.join(filas)}</tbody></table></div>"""
    return pagina("Glosario · Programación básica en C++", cuerpo, "glosario", {"tipo": "glosario"})


# ------------------------------------------------------------------ guía docente
def construir_guia(temas):
    path = ROOT / "temas" / "00_guia.md"
    meta, h, ctx = renderizar(path)
    secs = secciones(envolver_tablas(h))
    partes = []
    toc = []
    for cls, titulo, cont in secs:
        sid = slug(titulo)
        cont, sub = ids_h2(cont, "")
        toc.append((sid, titulo, [(k, t) for tag, k, t in sub if tag == "h2"]))
        partes.append(f'<section class="guia-sec" id="{sid}"><h2>{esc(titulo)}</h2>{cont}</section>')
    # fichas de los temas y PDF
    fichas = "".join(f'<li><a href="tema-{t["num"]}.html#docente">{t["num"]}. {esc(t["corto"])}</a> · <a href="{t["pdf"]}" download>PDF</a></li>' for t in temas)
    partes.append(f"""<section class="guia-sec" id="fichas-y-pdf"><h2>Fichas de diseño y cuadernillos PDF</h2>
<p>La ficha de cada tema está en su pestaña «Ficha docente». Los cuadernillos PDF son la versión imprimible del mismo material, con todas las soluciones en un anexo.</p>
<ul class="lista-fichas">{fichas}<li><a href="pdf/{meta['archivo']}.pdf" download>Esta guía en PDF</a></li></ul></section>""")
    toc_h = "".join(f'<li><a href="#{sid}">{esc(t)}</a>' + ("<ol>" + "".join(f'<li><a href="#{k}">{esc(x)}</a></li>' for k, x in sub) + "</ol>" if sub else "") + "</li>" for sid, t, sub in toc)
    toc_h += '<li><a href="#fichas-y-pdf">Fichas de diseño y cuadernillos PDF</a></li>'
    web = """<div class="caja c-nota guia-web"><div class="caja-h"><span class="ico">📝</span><span>En la versión web</span></div>
<ul><li>El <a href="diagnostico.html">diagnóstico</a> es una versión calificada automáticamente de la prueba de la sección 3.3: 8 reactivos por bloque y el mismo criterio de 70 % para sugerir la Ruta B.</li>
<li>En cada tema, las tareas de la otra ruta aparecen plegadas, los problemas por completar se califican al instante y las soluciones están junto a cada tarea.</li>
<li>El recall test, el comprehension test, el autorregistro (escala de esfuerzo mental de Paas) y la encuesta de carga cognitiva del anexo A.7 se responden en línea. Cada alumno puede exportar sus resultados en JSON o CSV desde «Mi progreso» para alimentar las tablas 5.2 y 5.13.</li></ul></div>"""
    cuerpo = f"""<section class="pagina-h"><h1>Guía docente</h1><p class="lede">{md_inline(meta['titulo'])}</p></section>
<div class="guia"><nav class="guia-toc" aria-label="Contenido de la guía"><p class="rail-t">Contenido</p><ol>{toc_h}</ol></nav>
<article class="guia-art contenido">{web}{''.join(partes)}</article></div>"""
    return pagina("Guía docente · Programación básica en C++", cuerpo, "guia", {"tipo": "guia"})


# ------------------------------------------------------------------ main
def main():
    if SITE.exists():  # se conserva docs/pdf por si out/ no está disponible
        for c in SITE.iterdir():
            if c.name != "pdf":
                shutil.rmtree(c) if c.is_dir() else c.unlink()
    (SITE / "assets" / "fonts").mkdir(parents=True, exist_ok=True)
    (SITE / "pdf").mkdir(exist_ok=True)
    paths = sorted(p for p in (ROOT / "temas").glob("[01][0-9]_*.md") if not p.name.startswith("00_"))
    temas = []
    for p in paths:
        meta, _ = leer_tema(p)
        temas.append({"num": meta["num"], "titulo": meta["titulo"], "corto": meta["corto"], "duracion": meta.get("duracion", ""),
                      "bloque": BLOQUE_DE[meta["num"]], "pdf": pdf_de(meta), "lema": meta.get("lema", ""),
                      "tareas": tareas_de(p.read_text())})
    metas = []
    stats = {}
    for i, p in enumerate(paths):
        doc, meta, tareas, ctx = construir_tema(p, temas, i)
        (SITE / f"tema-{meta['num']}.html").write_text(doc)
        metas.append(meta)
        stats[meta["num"]] = ctx.stats
        R.log(f"[web] tema-{meta['num']}.html  {ctx.stats}")
    n = web_diag.verificar(R.compile_run)
    R.log(f"[web] diagnóstico: {n} reactivos con código verificados")
    (SITE / "index.html").write_text(construir_inicio(temas))
    (SITE / "diagnostico.html").write_text(construir_diagnostico())
    (SITE / "progreso.html").write_text(construir_progreso())
    (SITE / "glosario.html").write_text(construir_glosario(metas))
    (SITE / "guia.html").write_text(construir_guia(temas))
    datos = {"bloques": [{"id": b, "nombre": n, "temas": ns} for b, n, ns in BLOQUES],
             "pasos": [{"id": k, "titulo": t, "corto": c} for k, t, c, _ in PASOS],
             "temas": temas}
    (SITE / "assets" / "datos.js").write_text("window.COURSE=" + json.dumps(datos, ensure_ascii=False) + ";\n")
    for f in ("curso.css", "curso.js", "favicon.svg", "fuentes.css"):
        shutil.copy(ASSETS_SRC / f, SITE / "assets" / f)
    for f in (ASSETS_SRC / "fonts").glob("*"):
        shutil.copy(f, SITE / "assets" / "fonts" / f.name)
    for nombre in [Path(t["pdf"]).name for t in temas] + ["Tema00_Guia_del_instructor_CLT4BP.pdf"]:
        src = ROOT / "out" / nombre
        if src.exists():
            shutil.copy(src, SITE / "pdf")
        elif not (SITE / "pdf" / nombre).exists():
            R.log(f"[web] AVISO: falta el PDF {nombre} (genéralo con engine/render.py)")
    (SITE / ".nojekyll").write_text("")
    R.log(f"[web] sitio listo en {SITE}")


if __name__ == "__main__":
    main()
