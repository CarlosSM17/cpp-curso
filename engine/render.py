"""Motor de render CLT4BP: Markdown con directivas -> HTML -> PDF (Chromium).

Uso: python3 engine/render.py temas/08_vectores.md [--html]
"""
import hashlib
import html
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
import yaml
from pygments.lexers import CLexer
from pygments.token import STANDARD_TYPES

sys.path.insert(0, str(Path(__file__).parent))
import diagrams  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
CACHE = BUILD / "cache"
OUT = ROOT / "out"
CACHE.mkdir(parents=True, exist_ok=True)
OUT.mkdir(exist_ok=True)

CC = os.environ.get("CC", "gcc")                 # en el contenedor de engine/Dockerfile: gcc-14
CFLAGS = ["-std=c17", "-Wall", "-Wextra"]
ECHO = ROOT / "engine" / "echo_stdin.c"         # eco de la entrada (solo para generar las salidas)

CIRC = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"

EF_NUEVO = {"ejemplo resuelto", "problema por completar", "modalidad", "variabilidad",
            "elementos aislados", "redundancia", "atención dividida", "información transitoria",
            "interactividad", "interactividad de elementos"}
EF_REF = {"autoexplicación", "auto-explicación", "imaginación", "solución libre", "memoria colectiva",
          "memoria colectiva de trabajo", "desvanecimiento de guía", "reversión de la experiencia"}

LOG = []
WEB = False          # True cuando lo usa el generador del sitio web (engine/web.py)


def log(*a):
    s = " ".join(str(x) for x in a)
    LOG.append(s)
    print(s, file=sys.stderr)


# ------------------------------------------------------------------ inline
def ef_badge(name):
    n = name.strip()
    k = n.lower()
    fam = "ef-n" if k in EF_NUEVO else ("ef-r" if k in EF_REF else "ef-x")
    return f'<span class="ef {fam}">{html.escape(n)}</span>'


def inline_macros(s):
    s = s.replace("{{A}}", '<span class="ruta ra">Ruta A</span>')
    s = s.replace("{{B}}", '<span class="ruta rb">Ruta B</span>')
    s = s.replace("{{AB}}", '<span class="ruta ra">Ruta A</span> <span class="ruta rb">Ruta B</span>')
    s = re.sub(r"\{\{ef:([^}]+)\}\}", lambda m: " ".join(ef_badge(x) for x in m.group(1).split(",")), s)
    s = re.sub(r"\{\{arcs:([^}]+)\}\}", lambda m: f'<span class="arcs">ARCS · {html.escape(m.group(1).strip())}</span>', s)
    if WEB:
        s = re.sub(r"\{\{lineas:(\d+)\}\}", lambda m: f'<textarea class="resp" rows="{max(2, int(m.group(1)) + 1)}" placeholder="Escribe aquí tu respuesta. Se guarda en este navegador."></textarea>', s)
        s = s.replace("{{salto}}", "")
        s = s.replace("{{como}}", '<span class="tag-como">Cómo</span>')
        s = s.replace("{{porque}}", '<span class="tag-porque">Por qué</span>')
    s = re.sub(r"\{\{lineas:(\d+)\}\}", lambda m: f'<div class="lineas" style="height:{int(m.group(1)) * 26}px"></div>', s)
    s = s.replace("{{salto}}", '<div class="pb"></div>')
    s = s.replace("{{como}}", '<span class="tag-como">CÓMO</span>')
    s = s.replace("{{porque}}", '<span class="tag-porque">POR QUÉ</span>')
    s = s.replace("{{hueco}}", '<span class="blank"></span>')
    def plantilla(m):
        n, heads = int(m.group(1)), [h.strip() for h in m.group(2).split("|")]
        th = "".join(f"<th>{md_inline(h)}</th>" for h in heads)
        tr = "<tr>" + "<td></td>" * len(heads) + "</tr>"
        return f'<table class="tb plantilla"><thead><tr>{th}</tr></thead><tbody>{tr * n}</tbody></table>'
    s = re.sub(r"\{\{plantilla:(\d+):([^}]+)\}\}", plantilla, s)
    s = re.sub(r"\{\{c:(\d+)\}\}", lambda m: f'<span class="circ">{CIRC[int(m.group(1)) - 1]}</span>', s)
    return s


def md_inline(s):
    """Markdown en línea mínimo (para celdas de tablas generadas y anotaciones)."""
    s = html.escape(str(s), quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![*\w])\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    s = s.replace("&lt;br&gt;", "<br>")
    return inline_macros(s)


# ------------------------------------------------------------------ código
def tok_class(tt):
    while tt not in STANDARD_TYPES:
        tt = tt.parent
    return STANDARD_TYPES[tt]


def highlight_lines(code, lang="c"):
    if lang != "c":
        return [html.escape(l) for l in code.split("\n")]
    lexer = CLexer(stripnl=False, ensurenl=False)
    lines = [[]]
    for tt, val in lexer.get_tokens(code):
        cls = tok_class(tt)
        parts = val.split("\n")
        for i, p in enumerate(parts):
            if i > 0:
                lines.append([])
            if p:
                e = html.escape(p)
                lines[-1].append(f'<span class="{cls}">{e}</span>' if cls else e)
    out = ["".join(l) for l in lines]
    return out


PSEUDO_KW = ["Algoritmo", "FinAlgoritmo", "Proceso", "FinProceso", "Inicio", "Fin", "Leer", "Escribir",
             "Si", "Entonces", "SiNo", "FinSi", "Mientras", "Hacer", "FinMientras", "Para", "Hasta",
             "Con Paso", "FinPara", "Repetir", "Hasta Que", "Segun", "FinSegun", "De Otro Modo",
             "Funcion", "FinFuncion", "SubProceso", "FinSubProceso", "Definir", "Como", "Entero", "Real",
             "Caracter", "Cadena", "Logico", "Dimension", "Retornar", "Y", "O", "NO", "MOD", "Verdadero", "Falso",
             "Por Referencia", "Por Valor", "Registro", "FinRegistro", "Abrir", "Cerrar", "Mostrar"]


def highlight_pseudo(code):
    out = []
    kw = sorted(PSEUDO_KW, key=len, reverse=True)
    pat = re.compile(r"\b(" + "|".join(re.escape(k) for k in kw) + r")\b")
    for l in code.split("\n"):
        # comentarios //
        cpos = l.find("//")
        main, com = (l[:cpos], l[cpos:]) if cpos >= 0 else (l, "")
        parts = re.split(r'("[^"]*")', main)
        res = []
        for p in parts:
            if p.startswith('"'):
                res.append(f'<span class="s">{html.escape(p)}</span>')
            else:
                res.append(pat.sub(lambda m: f'<span class="k">{m.group(1)}</span>', html.escape(p)))
        if com:
            res.append(f'<span class="c1">{html.escape(com)}</span>')
        out.append("".join(res))
    return out


def parse_ranges(s):
    r = set()
    if not s:
        return r
    for part in str(s).split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            r.update(range(int(a), int(b) + 1))
        elif part:
            r.add(int(part))
    return r


def holes(h):
    def rep(m):
        k = m.group(1)
        if WEB:
            n = "" if k == "?" else f' data-n="{k}"'
            lab = "Hueco" if k == "?" else f"Hueco {k}"
            return (f'<input class="hole"{n} aria-label="{lab}" autocomplete="off" autocapitalize="off" '
                    f'spellcheck="false" placeholder="{CIRC[int(k) - 1] if k.isdigit() and int(k) <= 20 else "?"}">')
        if k == "?":
            return '<span class="hueco">&nbsp;?&nbsp;</span>'
        try:
            return f'<span class="hueco">{CIRC[int(k) - 1]}</span>'
        except (ValueError, IndexError):
            return f'<span class="hueco">{k}</span>'
    return re.sub(r"__(\d+|\?)__", rep, h)


def code_table(code, lang, attrs):
    raw_lines = code.split("\n")
    anns = []
    clean = []
    for l in raw_lines:
        m = re.match(r"^(.*?)\s*//>\s?(.*)$", l)
        if m and lang in ("c", "pseudo"):
            clean.append(m.group(1).rstrip())
            anns.append(m.group(2))
        else:
            clean.append(l)
            anns.append(None)
    has_ann = any(a is not None for a in anns)
    if lang == "c":
        hls = highlight_lines("\n".join(clean), "c")
    elif lang == "pseudo":
        hls = highlight_pseudo("\n".join(clean))
    else:
        hls = [html.escape(l) for l in clean]
    hl = parse_ranges(attrs.get("hl"))
    lines_on = "nolines" not in attrs
    rows = []
    for i, (h, a) in enumerate(zip(hls, anns), start=1):
        h = holes(h)
        cls = ' class="hl"' if i in hl else ""
        ln = f'<td class="ln">{i}</td>' if lines_on else ""
        an = ""
        if has_ann:
            an = f'<td class="an">{md_inline(a) if a else ""}</td>'
        rows.append(f"<tr{cls}>{ln}<td class=\"cl\">{h or '&#8203;'}</td>{an}</tr>")
    title = attrs.get("title")
    kind = {"c": "C", "pseudo": "Pseudocódigo (PSeInt)", "txt": "Texto"}.get(lang, lang)
    cap = ""
    has_holes = bool(re.search(r"__(\d+|\?)__", code))
    if title or lang == "pseudo" or "blank" in attrs:
        badge = '<span class="cbadge">' + kind + "</span>"
        if "blank" in attrs and has_holes:
            badge += '<span class="cbadge cb-blank">por completar</span>'
        elif "blank" in attrs:
            badge += '<span class="cbadge cb-frag">fragmento</span>'
        cap = f'<div class="code-t"><span>{md_inline(title) if title else ""}</span><span>{badge}</span></div>'
    cls = "code" + (" anot" if has_ann else "") + (" pseudo" if lang == "pseudo" else "")
    if len(raw_lines) <= 16:
        cls += " keep"
    return f'<figure class="{cls}">{cap}<table class="src">{"".join(rows)}</table></figure>', "\n".join(clean)


def compile_run(code, mode, stdin="", files=None, allow_rc=False, showfile=None, timeout=8, flags=(), link=()):
    """mode: run (compila y ejecuta), check (solo compila), err (debe fallar), warn (debe compilar con advertencia).
    link: otros .c del tema (registrados con ```c file=...```) que se compilan y enlazan junto con main.c."""
    files = files or {}
    flags = list(flags)
    link = list(link)
    for n in link:
        if n not in files:
            raise RuntimeError(f"link={n}: ese archivo no se ha definido antes con ```c file={n}```")
    k = ["c1", CC, code, mode, stdin, sorted(files.items()), showfile, flags]
    if link:
        k.append(link)
    key = hashlib.sha256(json.dumps(k).encode()).hexdigest()[:24]
    cf = CACHE / f"{key}.json"
    if cf.exists():
        return json.loads(cf.read_text())
    d = Path(tempfile.mkdtemp(prefix="c_", dir=BUILD))
    for n, c in files.items():
        (d / n).write_text(c)
    (d / "main.c").write_text(code)
    cmd = [CC, *CFLAGS, *flags, "-o", "prog", "main.c", *link]
    if mode == "run":
        cmd.append(str(ECHO))
    cmd.append("-lm")
    p = subprocess.run(cmd, cwd=d, capture_output=True, text=True)
    res = {"compile_rc": p.returncode, "stderr": p.stderr, "stdout": "", "rc": None, "file": None}
    if mode == "err":
        if p.returncode == 0:
            raise RuntimeError("Se esperaba error de compilación y compiló:\n" + code)
    elif mode == "warn":
        if p.returncode != 0:
            raise RuntimeError("Se esperaba solo una advertencia y no compiló:\n" + p.stderr + "\n----\n" + code)
        if ": warning:" not in p.stderr:
            raise RuntimeError("Se esperaba una advertencia de gcc y compiló sin avisos:\n" + code)
    else:
        if p.returncode != 0:
            raise RuntimeError("Error de compilación:\n" + p.stderr + "\n----\n" + code)
        if p.stderr.strip():
            for l in p.stderr.split("\n"):
                if ": warning:" in l:
                    log("  [aviso gcc]", l.strip()[:200])
        if mode == "run":
            try:
                r = subprocess.run(["./prog"], cwd=d, input=stdin, capture_output=True, text=True, timeout=timeout)
            except subprocess.TimeoutExpired:
                raise RuntimeError("Timeout ejecutando:\n" + code)
            err = r.stderr or ""
            if any(f.startswith("-fsanitize") for f in flags):
                err = simplify_asan(err)
            res["stdout"] = r.stdout + err
            res["rc"] = r.returncode
            if r.returncode != 0 and not allow_rc:
                raise RuntimeError(f"Código de salida {r.returncode}:\n{r.stdout}\n{r.stderr}\n----\n{code}")
            if showfile:
                fp = d / showfile
                res["file"] = fp.read_text() if fp.exists() else "(no se creó el archivo)"
    shutil.rmtree(d, ignore_errors=True)
    cf.write_text(json.dumps(res))
    return res


def compile_module(name, files):
    """Verifica un archivo de un programa de varios archivos: un .c se compila con -c (sin enlazar)
    y un .h se revisa solo (-fsyntax-only), para comprobar que no depende de lo que se incluya antes."""
    key = hashlib.sha256(json.dumps(["m1", CC, name, sorted(files.items())]).encode()).hexdigest()[:24]
    cf = CACHE / f"{key}.json"
    if cf.exists():
        return
    d = Path(tempfile.mkdtemp(prefix="m_", dir=BUILD))
    for n, c in files.items():
        (d / n).write_text(c)
    p = subprocess.run([CC, *CFLAGS, "-fsyntax-only" if name.endswith(".h") else "-c", name],
                       cwd=d, capture_output=True, text=True)
    shutil.rmtree(d, ignore_errors=True)
    if p.returncode != 0:
        raise RuntimeError(f"El archivo {name} no compila:\n{p.stderr}")
    for l in p.stderr.split("\n"):
        if ": warning:" in l:
            log("  [aviso gcc]", l.strip()[:200])
    cf.write_text("{}")


def run_console(script, files, allow_rc=False, timeout=15):
    """Ejecuta de verdad las órdenes «$ ...» de un bloque ```console run``` en una carpeta con los
    archivos del tema; devuelve la transcripción (cada orden marcada como lo que se teclea).
    `gcc` es el compilador del motor (CC); sin rc, cualquier orden que falle detiene la generación."""
    key = hashlib.sha256(json.dumps(["sh1", CC, script, sorted(files.items())]).encode()).hexdigest()[:24]
    cf = CACHE / f"{key}.json"
    if cf.exists():
        return json.loads(cf.read_text())
    d = Path(tempfile.mkdtemp(prefix="sh_"))     # disco del contenedor: fechas exactas para make
    for n, c in files.items():
        (d / n).write_text(c)
    binp = d / ".bin"
    binp.mkdir()
    (binp / "gcc").symlink_to(shutil.which(CC) or CC)
    env = dict(os.environ, PATH=f"{binp}:{os.environ.get('PATH', '')}")
    out, fallas = [], 0
    for line in script.split("\n"):
        if not line.startswith("$ "):
            raise RuntimeError("En ```console run``` cada línea debe ser una orden «$ ...»:\n" + line)
        orden = line[2:]
        try:
            p = subprocess.run(["sh", "-c", orden], cwd=d, env=env, text=True, timeout=timeout,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except subprocess.TimeoutExpired:
            raise RuntimeError("Timeout en la orden: " + orden)
        o = re.sub(r"\x1b\[[0-9;]*m", "", p.stdout).replace(str(d) + "/", "")
        out.append("$ \x01" + orden + "\n\x02" + o)
        if p.returncode != 0:
            fallas += 1
            if not allow_rc:
                raise RuntimeError(f"Falló la orden «{orden}» (código {p.returncode}):\n{o}")
    if allow_rc and not fallas:
        raise RuntimeError("Se marcó rc pero ninguna orden falló:\n" + script)
    shutil.rmtree(d, ignore_errors=True)
    res = {"out": "".join(out)}
    cf.write_text(json.dumps(res))
    return res


def simplify_err(err, desde=": error:"):
    err = re.sub(r"\x1b\[[0-9;]*m", "", err)
    if "/usr/bin/ld" in err:
        err = re.sub(r"(?:/[\w.+-]+)+/([\w.+-]+\.o)", r"\1", err)
        err = re.sub(r"\S*main\.c\b", "main.c", err)
        lines = [l for l in err.split("\n") if l.strip()]
        return "\n".join(lines[:4])
    err = re.sub(r"\S*main\.c\b", "main.c", err)
    lines = err.split("\n")
    keep = []
    started = False
    for i, l in enumerate(lines):
        if (desde in l or (desde == ": error:" and ": fatal error:" in l)) and not started:
            started = True
            j = i                       # conserva la cadena «In file included from … / from …»
            while j > 0 and re.match(r"(In file included from|\s+from) ", lines[j - 1]):
                j -= 1
            keep.extend(lines[j:i])
        if started:
            if "note:" in l and len(keep) > 2 and not re.search(r"forget|include", l):
                break
            keep.append(l)
        if len(keep) >= 5:
            break
    out = "\n".join(keep).rstrip()
    out = re.sub(r"\x1b\[[0-9;]*m", "", out)
    return out


def simplify_asan(err):
    """Deja lo esencial de un informe de AddressSanitizer/LeakSanitizer: el error, cada fuga
    con la línea de main.c donde se reservó y el resumen (sin direcciones ni rutas)."""
    keep = []
    for l in err.split("\n"):
        s = l.strip()
        if "ERROR:" in s:
            keep.append(re.sub(r"^==\d+==", "", s))
        elif re.match(r"(Direct|Indirect) leak|SUMMARY:", s):
            keep.append(s)
        else:
            m = re.match(r"#\d+ 0x[0-9a-f]+ in (\w+) \S*main\.c:(\d+)", s)
            if m:
                keep.append(f"    en {m.group(1)} (main.c:{m.group(2)})")
    return "\n".join(keep) + ("\n" if keep else "")


def file_box(name, content):
    return (f'<div class="filebox"><div class="file-t">📄 {html.escape(name)}</div>'
            f'<pre>{html.escape(content.rstrip())}</pre></div>')


def echo_html(out):
    out = out.replace("\x02\x01", "")
    h = html.escape(out)
    h = h.replace("\x01", '<span class="kin">').replace("\x02", "</span>")
    h = re.sub(r'<span class="kin">\n</span>', "\n", h)
    h = re.sub(r'\n</span>', '</span>\n', h)
    return h


def term_box(out, stdin=None, title="Salida en consola"):
    sin = ""
    if stdin and stdin.strip():
        sin = '<span class="term-in"><b>resaltado</b> = lo que se teclea</span>'
    out = out.rstrip("\n").rstrip("\x02").rstrip("\n")
    if out.endswith("\x01"):
        out = out[:-1]
    if out.count("\x01") > out.count("\x02"):      # la última orden tecleada no produjo salida
        out += "\x02"
    return (f'<div class="term"><div class="term-t"><span>▶ {title}</span>{sin}</div>'
            f'<pre>{echo_html(out) if out else "&nbsp;"}</pre></div>')


class Ctx:
    def __init__(self, name):
        self.name = name
        self.ph = {}
        self.files = {}
        self.solutions = []
        self.n = 0
        self.stats = {"run": 0, "check": 0, "err": 0, "warn": 0, "display": 0}

    def put(self, h):
        self.n += 1
        k = f"@@PH{self.n:04d}@@"
        self.ph[k] = h
        return k


FENCE = re.compile(r"^```([\w+-]*)[ \t]*([^\n]*)\n(.*?)\n```[ \t]*$", re.M | re.S)


def parse_attrs(s):
    attrs = {}
    try:
        toks = shlex.split(s)
    except ValueError:
        toks = s.split()
    for tk in toks:
        if "=" in tk:
            k, v = tk.split("=", 1)
            attrs[k] = v
        else:
            attrs[tk] = True
    return attrs


def process_fences(body, ctx):
    # Archivos de módulos que se definen más adelante (p. ej., en la columna de al lado):
    # un bloque con link= puede usar el siguiente que aparezca si aún no se ha visto ninguno.
    futuros = []
    for fm in FENCE.finditer(body):
        fa = parse_attrs(fm.group(2))
        if fm.group(1) == "c" and fa.get("file"):
            limpio = [re.sub(r"\s*//>.*$", "", l) for l in fm.group(3).split("\n")]
            futuros.append((fm.start(), fa["file"], "\n".join(limpio) + "\n"))

    def rep(m):
        lang, info, code = m.group(1) or "txt", m.group(2), m.group(3)
        attrs = parse_attrs(info)
        if lang == "dot":
            svg = diagrams.dot_svg(code)
            cap = attrs.get("caption")
            capb = f'<figcaption>{md_inline(cap)}</figcaption>' if cap else ""
            w = attrs.get("w")
            st = f' style="max-width:{w}"' if w else ""
            return "\n" + ctx.put(f'<figure class="fig"{st}>{svg}{capb}</figure>') + "\n"
        if lang == "diagram":
            kind = info.split()[0]
            spec = yaml.safe_load(code) or {}
            svg = diagrams.GENS[kind](spec)
            cap = spec.get("figcaption")
            capb = f'<figcaption>{md_inline(cap)}</figcaption>' if cap else ""
            return "\n" + ctx.put(f'<figure class="fig">{svg}{capb}</figure>') + "\n"
        if lang in ("txt", "text") and attrs.get("file"):
            ctx.files[attrs["file"]] = code + "\n"
            return "\n" + ctx.put(file_box(attrs["file"], code)) + "\n"
        if lang == "console":
            if "run" in attrs:
                ctx.stats["run"] += 1
                res = run_console(code, dict(ctx.files), "rc" in attrs)
                return "\n" + ctx.put(term_box(res["out"], "órdenes", title=attrs.get("title", "Terminal"))) + "\n"
            return "\n" + ctx.put(term_box(code, title=attrs.get("title", "Terminal"))) + "\n"
        if lang == "c":
            fname = attrs.get("file")              # archivo de un programa de varios archivos (.h / .c)
            if fname and "title" not in attrs:
                attrs["title"] = fname
            tbl, clean = code_table(code, "c", attrs)
            if fname:
                ctx.files[fname] = clean + "\n"
            link = attrs.get("link", "").split()
            archivos = dict(ctx.files)
            for n in link:
                if n not in archivos:
                    sig = next((c for pos, nm, c in futuros if nm == n and pos > m.start()), None)
                    if sig is not None:
                        archivos[n] = sig
            INCL = re.compile(r'^\s*#include\s+"([^"]+)"', re.M)   # módulos propios (no los comentarios)
            usa_mod = bool(link) or bool(INCL.search(clean))
            extra = ""
            stdin = attrs.get("stdin", "").replace("\\n", "\n")
            if stdin and not stdin.endswith("\n"):
                stdin += "\n"
            if "runs" in attrs:
                ctx.stats["run"] += 1
                parts = []
                ins = [x.replace("\\n", "\n") for x in attrs["runs"].split("|")]
                for k, sin in enumerate(ins, 1):
                    if not sin.endswith("\n"):
                        sin += "\n"
                    res = compile_run(clean, "run", sin, archivos, "rc" in attrs, link=link)
                    o = res["stdout"].rstrip("\n")
                    parts.append(f'<div class="run-sep">Ejecución {k}</div>'
                                 f'<pre>{echo_html(o)}</pre>')
                extra = ('<div class="term multi"><div class="term-t"><span>▶ Salida en consola · '
                         f'{len(ins)} ejecuciones</span><span class="term-in"><b>resaltado</b> = lo que se teclea</span></div>' + "".join(parts) + "</div>")
            elif "run" in attrs:
                ctx.stats["run"] += 1
                res = compile_run(clean, "run", stdin, archivos, "rc" in attrs, attrs.get("showfile"),
                                  flags=attrs.get("flags", "").split(), link=link)
                if attrs.get("out") != "0":
                    extra = term_box(res["stdout"], stdin)
                if res.get("file") is not None:
                    extra += file_box(attrs["showfile"], res["file"])
            elif "check" in attrs:
                ctx.stats["check"] += 1
                compile_run(clean, "check", files=archivos, link=link)
            elif "err" in attrs:
                ctx.stats["err"] += 1
                res = compile_run(clean, "err", files=archivos if usa_mod else None, link=link)
                extra = term_box(simplify_err(res["stderr"]), title="Mensaje del compilador (gcc)").replace(
                    'class="term"', 'class="term err"')
            elif "warn" in attrs:
                ctx.stats["warn"] += 1
                res = compile_run(clean, "warn", files=archivos if usa_mod else None,
                                  flags=attrs.get("flags", "").split(), link=link)
                extra = term_box(simplify_err(res["stderr"], ": warning:"), title="Advertencia del compilador (gcc)").replace(
                    'class="term"', 'class="term err"')
            elif fname and fname.endswith((".c", ".h")):
                ctx.stats["check"] += 1
                compile_module(fname, archivos)
            else:
                ctx.stats["display"] += 1
            if WEB:
                import base64
                mode = next((k for k in ("runs", "run", "err", "warn", "check") if k in attrs), "display")
                b64 = lambda t: base64.b64encode(t.encode()).decode()
                first_in = stdin
                if "runs" in attrs:
                    first_in = attrs["runs"].split("|")[0].replace("\\n", "\n")
                dat = f' data-mode="{mode}" data-src="{b64(clean)}"'
                if attrs.get("flags"):
                    dat += f' data-flags="{html.escape(attrs["flags"])}"'
                if first_in.strip():
                    dat += f' data-stdin="{b64(first_in if first_in.endswith(chr(10)) else first_in + chr(10))}"'
                if "blank" in attrs and re.search(r"__(\d+|\?)__", code):
                    dat += ' data-blank="1"'
                datos = [f for f in ctx.files if not f.endswith((".c", ".h"))]
                if datos and mode in ("run", "runs", "check") and re.search(r"\bfopen\b", clean):
                    dat += f' data-files="{html.escape(", ".join(datos))}"'
                if usa_mod and mode != "display":
                    incl = set(INCL.findall(clean))
                    for n in link:
                        incl |= set(INCL.findall(archivos[n]))
                    t = attrs.get("title", "")
                    mods = [fname or (t if t.endswith(".c") else "main.c")] + link + sorted(incl - set(link))
                    dat += f' data-modulos="{html.escape(", ".join(mods))}"'
                elif (fname and mode == "display") or "modulo" in attrs:
                    dat += ' data-modulo="1"'
                if attrs.get("title"):
                    dat += f' data-title="{html.escape(attrs["title"])}"'
                return "\n" + ctx.put(f'<div class="codewrap"{dat}>{tbl}{extra}</div>') + "\n"
            return "\n" + ctx.put(f'<div class="codewrap">{tbl}{extra}</div>') + "\n"
        if lang == "pseudo":
            tbl, _ = code_table(code, "pseudo", attrs)
            return "\n" + ctx.put(tbl) + "\n"
        tbl, _ = code_table(code, "txt", attrs)
        return "\n" + ctx.put(tbl) + "\n"
    return FENCE.sub(rep, body)


# ------------------------------------------------------------------ cajas
BOX_TITLES = {
    "analogia": "Analogía", "pregunta": "Pregunta para pensar", "relevancia": "¿Por qué y para qué?",
    "nota": "Nota", "cuidado": "¡Cuidado!", "tip": "Consejo", "concepto": "Concepto",
    "sintaxis": "Tarjeta de sintaxis", "checklist": "Guía de preguntas de rutina", "errores": "Errores frecuentes",
    "resumen": "Resumen visual", "ejemplo": "Ejemplo resuelto", "colab": "Reto colaborativo",
    "autog": "Autogestión: mejora este material", "movimiento": "Actividad en el aula · movimiento humano",
    "protocolo": "Protocolo verbal", "recall": "Recall test", "compr": "Comprehension test",
    "def": "Definición", "checkpoint": "Checkpoint", "autoexp": "Autoexplícalo", "isomorfo": "Ejemplo isomórfico",
    "imagina": "Imagínalo", "reto": "Reto extra", "registro": "Autorregistro", "plan": "Plan",
}
BOX_ICON = {
    "analogia": "💡", "pregunta": "❓", "relevancia": "🎯", "nota": "📝", "cuidado": "⚠️", "tip": "✔",
    "sintaxis": "⌨", "checklist": "☑", "errores": "🐞", "resumen": "🗺", "ejemplo": "✎", "colab": "👥",
    "autog": "🛠", "movimiento": "🙋", "protocolo": "🎙", "def": "📌", "checkpoint": "🚩", "autoexp": "💬",
    "isomorfo": "⇄", "imagina": "🧠", "reto": "⭐", "registro": "📊",
}


def box_open(kind, fields, ctx):
    fields = [f.strip() for f in fields]
    if kind == "tarea":
        ruta = fields[0] if fields else ""
        title = fields[1] if len(fields) > 1 else ""
        dur = fields[2] if len(fields) > 2 else ""
        efs = fields[3] if len(fields) > 3 else ""
        rb = {"A": "{{A}}", "B": "{{B}}", "AB": "{{AB}}"}.get(ruta, "")
        head = (f'<div class="tarea-h"><div class="tarea-t">{md_inline(title)}</div>'
                f'<div class="tarea-m">{inline_macros(rb)}'
                + (f'<span class="dur">⏱ {html.escape(dur)}</span>' if dur else "")
                + "</div>"
                + (f'<div class="tarea-e">{" ".join(ef_badge(e) for e in efs.split(",") if e.strip())}</div>' if efs else "")
                + "</div>")
        if WEB:
            mt = re.match(r"\s*(T\d+)", title)
            tid = mt.group(1).lower() if mt else f"t{len(ctx.ph)}"
            return f'\n<div class="caja c-tarea" id="{tid}" data-ruta="{html.escape(ruta)}" markdown="1">\n{head}\n\n'
        return f'\n<div class="caja c-tarea" markdown="1">\n{head}\n\n'
    if kind == "concepto":
        num = fields[0] if fields else ""
        title = fields[1] if len(fields) > 1 else ""
        efs = fields[2] if len(fields) > 2 else ""
        efh = f'<span class="h-ef">{" ".join(ef_badge(e) for e in efs.split(",") if e.strip())}</span>' if efs else ""
        head = f'<div class="caja-h"><span class="cnum">{html.escape(num)}</span><span>{md_inline(title)}</span>{efh}</div>'
        return f'\n<div class="caja c-concepto" markdown="1">\n{head}\n\n'
    deft = BOX_TITLES.get(kind, kind.capitalize())
    title = fields[0] if fields and fields[0] else ""
    efs = fields[1] if len(fields) > 1 else ""
    icon = BOX_ICON.get(kind, "")
    efh = f'<span class="h-ef">{" ".join(ef_badge(e) for e in efs.split(",") if e.strip())}</span>' if efs else ""
    if title and title.lower() != deft.lower():
        tt = f'<span class="kick">{html.escape(deft)}</span><span>{md_inline(title)}</span>'
    else:
        tt = f'<span>{html.escape(deft)}</span>'
    head = f'<div class="caja-h"><span class="ico">{icon}</span>{tt}{efh}</div>'
    return f'\n<div class="caja c-{kind}" markdown="1">\n{head}\n\n'


def process_boxes(body, ctx):
    lines = body.split("\n")
    out = []
    stack = []
    cap = None  # captura de solución
    capdepth = 0
    caplabel = ""
    for line in lines:
        m = re.match(r"^:::(\w+)\s*(.*)$", line)
        close = re.match(r"^:::\s*$", line)
        if cap is not None:
            if m:
                capdepth += 1
                cap.append(line)
                continue
            if close:
                if capdepth == 0:
                    ctx.solutions.append((caplabel, "\n".join(cap)))
                    out.append(f'\n<p class="solref">✓ Solución: <b>Anexo · {html.escape(caplabel)}</b></p>\n')
                    cap = None
                    continue
                capdepth -= 1
                cap.append(line)
                continue
            cap.append(line)
            continue
        if m:
            kind, rest = m.group(1), m.group(2).strip()
            if rest.startswith("|"):
                rest = rest[1:]
            fields = rest.split("|") if rest else []
            if kind == "solucion" and WEB:
                label = fields[0].strip() if fields else f"S{len(ctx.solutions) + 1}"
                stack.append(kind)
                out.append(f'\n<div class="sol" data-label="{html.escape(label)}" markdown="1">\n')
                continue
            if kind == "solucion":
                cap = []
                capdepth = 0
                caplabel = fields[0].strip() if fields else f"S{len(ctx.solutions) + 1}"
                continue
            stack.append(kind)
            out.append(box_open(kind, fields, ctx))
            continue
        if close:
            if not stack:
                raise RuntimeError(f"Cierre ::: sin apertura en {ctx.name}")
            stack.pop()
            out.append("\n</div>\n")
            continue
        if re.match(r'^<div( class="[^"]*")?>\s*$', line):
            line = line.rstrip()[:-1] + ' markdown="1">'
        out.append(line)
    if stack:
        raise RuntimeError(f"Cajas sin cerrar en {ctx.name}: {stack}")
    if cap is not None:
        raise RuntimeError(f"Solución sin cerrar en {ctx.name}")
    return "\n".join(out)


MD_EXT = ["extra", "sane_lists", "md_in_html"]

H1_SUB = {
    "soporte": "Componente 4C/ID · <b>Información de soporte</b> — se presenta antes de las tareas y permanece disponible todo el tema.",
    "procedimental": "Componente 4C/ID · <b>Información procedimental</b> — tenla a la vista y consúltala «justo a tiempo» mientras resuelves las tareas.",
    "tareas": "Componente 4C/ID · <b>Tareas de aprendizaje</b> — de menor a mayor complejidad; la ayuda se desvanece tarea con tarea.",
    "protocolo": "Componente 4C/ID · <b>Información procedimental: protocolo verbal</b> — el CÓMO y el POR QUÉ de un experto, en voz alta.",
    "evaluacion": "Fase 3 · <b>Aplicación y evaluación</b> — recall test (conocimiento declarativo) y comprehension test (conocimiento procedimental).",
    "glosario": "Términos clave en español e inglés, para consultar a Kernighan y Ritchie, a King, a Seacord y la documentación.",
    "anexo": "Soluciones de las tareas y de la evaluación. Intenta cada ejercicio antes de consultarlas.",
}


def md_to_html(text, ctx):
    text = inline_macros(text)
    h = markdown.markdown(text, extensions=MD_EXT, output_format="html5")
    for k, v in ctx.ph.items():
        h = h.replace(f"<p>{k}</p>", v).replace(k, v)
    # subtítulo de componente bajo cada h1 con clase
    def h1sub(m):
        cls = m.group(1)
        sub = H1_SUB.get(cls)
        return m.group(0) + (f'<p class="h1-sub s-{cls}">{sub}</p>' if sub else "")
    h = re.sub(r'<h1[^>]*class="(\w+)"[^>]*>.*?</h1>', h1sub, h, flags=re.S)
    return h


def table(headers, rows, cls=""):
    th = "".join(f"<th>{md_inline(x)}</th>" for x in headers)
    trs = []
    for r in rows:
        trs.append("<tr>" + "".join(f"<td>{md_inline(c) if not str(c).startswith('<') else c}</td>" for c in r) + "</tr>")
    return f'<table class="tb {cls}"><thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table>'


def ul(items):
    return "<ul>" + "".join(f"<li>{md_inline(i)}</li>" for i in items) + "</ul>"


COMP_NAMES = {"soporte": "Información de soporte", "procedimental": "Información procedimental",
              "tareas": "Tareas de aprendizaje", "protocolo": "Protocolo verbal"}


def ficha_html(meta):
    o = meta.get("objetivos", {})
    parts = ['<h1 class="ficha" id="ficha">0. Ficha de diseño instruccional</h1>',
             '<p class="h1-sub s-ficha">Fases 1 y 2 del mapa de ruta CLT4BP · <b>para el instructor</b>: '
             'qué se enseña, cómo se evalúa, qué efectos de la TCC se aplican y cómo se diferencia la instrucción.</p>']
    kv = [("Tema", f'{meta["num"]}. {meta["titulo"]}'), ("Duración sugerida", meta.get("duracion", "")),
          ("Conocimientos previos", meta.get("previos", "")), ]
    parts.append('<div class="kv">' + "".join(f'<div><span>{k}</span><b>{md_inline(v)}</b></div>' for k, v in kv) + "</div>")
    parts.append("<h2>1. Objetivos de aprendizaje por nivel</h2>")
    parts.append('<p class="mini">Ruta A: estudiantes <b>sin</b> conocimientos previos del tema · Ruta B: estudiantes <b>con</b> conocimientos previos '
                 '(el diagnóstico de la Fase 1 decide la ruta; ver Tema 00).</p>')
    parts.append(f'<table class="tb obj"><thead><tr><th><span class="ruta ra">Ruta A</span> Al terminar podrás…</th>'
                 f'<th><span class="ruta rb">Ruta B</span> Al terminar podrás…</th></tr></thead>'
                 f'<tbody><tr><td>{ul(o.get("A", []))}</td><td>{ul(o.get("B", []))}</td></tr></tbody></table>')
    parts.append("<h2>2. Métodos de evaluación</h2>")
    parts.append(table(["Instrumento", "Tipo de conocimiento", "Contenido en este tema"], [
        ["**Recall test** (sección 5.1)", "Declarativo", meta.get("eval_recall", "Reactivos de opción múltiple, relación y verdadero/falso sobre conceptos y sintaxis.")],
        ["**Comprehension test** (sección 5.2)", "Procedimental (transferencia cercana)", meta.get("eval_compr", "Predecir salidas, corregir errores y escribir un programa nuevo.")],
        ["Carga cognitiva, CIS, IMMS y MSLQ", "Percepción y motivación", "Al cerrar el bloque de temas; instrumentos en los anexos A.1, A.4, A.5 y A.7 de la tesis (ver Tema 00)."],
    ]))
    parts.append("<h2>3. Preselección de efectos de la TCC por componente 4C/ID</h2>")
    rows = []
    for comp, lst in meta.get("efectos", {}).items():
        first = True
        for ef, how in lst:
            rows.append([f"**{COMP_NAMES.get(comp, comp)}**" if first else "", ef_badge(ef), how])
            first = False
    parts.append(table(["Componente", "Efecto", "Cómo se aplica en este tema"], rows, "efx"))
    parts.append("<h2>4. Matriz de instrucción diferenciada (Tomlinson × 4C/ID)</h2>")
    rows = []
    for el, d in meta.get("diferenciada", {}).items():
        rows.append([f"**{el}**", d.get("comp", ""), d.get("A", ""), d.get("B", "")])
    parts.append(table(["Elemento", "Componente 4C/ID", "Ruta A · sin previos", "Ruta B · con previos"], rows, "dif"))
    parts.append("<h2>5. Plan de implementación (Fase 3)</h2>")
    parts.append(table(["Momento", "Componente", "Actividad", "Tiempo"], meta.get("plan", []), "plan"))
    return '<div class="ficha-wrap">' + "\n".join(parts) + "</div>"


def glosario_html(meta):
    g = meta.get("glosario")
    if not g:
        return ""
    rows = [[f"**{a}**", f"*{b}*", c] for a, b, c in g]
    return ('<h1 class="glosario">Glosario bilingüe</h1>' + f'<p class="h1-sub s-glosario">{H1_SUB["glosario"]}</p>'
            + table(["Español", "English", "Significado"], rows, "glos"))


def fuentes_html(meta):
    f = meta.get("fuentes", [])
    if not f:
        return ""
    return '<div class="fuentes"><h3>Fuentes del tema</h3>' + ul(f) + "</div>"


def build_doc(path, make_pdf=True):
    src = Path(path).read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", src, re.S)
    meta = yaml.safe_load(m.group(1))
    body = m.group(2)
    ctx = Ctx(Path(path).stem)
    body = process_fences(body, ctx)
    body = process_boxes(body, ctx)
    main_html = md_to_html(body, ctx)
    sol_parts = []
    for label, txt in ctx.solutions:
        sh = md_to_html(process_boxes(txt, ctx), ctx)
        sol_parts.append(f'<div class="sol"><div class="sol-h">Solución · {html.escape(label)}</div>{sh}</div>')
    anexo = ""
    if sol_parts:
        anexo = ('<h1 class="anexo">Anexo · Soluciones</h1>' + f'<p class="h1-sub s-anexo">{H1_SUB["anexo"]}</p>'
                 + "".join(sol_parts))
    is_guide = meta.get("tipo") == "guia"
    ficha = "" if is_guide else ficha_html(meta)
    content = ficha + main_html + glosario_html(meta) + fuentes_html(meta) + anexo
    css = (ROOT / "engine" / "style.css").read_text()
    doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{html.escape(meta['titulo'])}</title>
<style>{css}</style></head><body class="doc">{content}</body></html>"""
    stem = Path(path).stem
    (BUILD / f"{stem}.html").write_text(doc)
    cover = cover_html(meta, css)
    (BUILD / f"{stem}_cover.html").write_text(cover)
    log(f"[{stem}] código: {ctx.stats}  soluciones: {len(ctx.solutions)}")
    return meta, stem


def cover_html(meta, css):
    num = meta["num"]
    fuentes = "".join(f"<li>{md_inline(f)}</li>" for f in meta.get("fuentes", []))
    ruta = meta.get("ruta_portada", True)
    steps = [("soporte", "Información<br>de soporte"), ("procedimental", "Información<br>procedimental"),
             ("tareas", "Tareas de<br>aprendizaje"), ("protocolo", "Protocolo<br>verbal"), ("evaluacion", "Evaluación")]
    if meta.get("pasos_portada"):
        steps = [(k, v) for k, v in meta["pasos_portada"]]
    stepsh = "".join(f'<div class="cs cs-{k}"><span>{i + 1}</span>{v}</div>' + ('<div class="ca">→</div>' if i < len(steps) - 1 else "")
                     for i, (k, v) in enumerate(steps))
    kicker = meta.get("kicker", f"Tema {num}")
    rutas = ""
    if ruta:
        rutas = ('<div class="cov-rutas"><div><span class="ruta ra">Ruta A</span> sin conocimientos previos: ejemplos resueltos, problemas por completar, guía que se desvanece.</div>'
                 '<div><span class="ruta rb">Ruta B</span> con conocimientos previos: autoexplicación, imaginación, solución libre y retos colaborativos.</div></div>')
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head>
<body class="cover"><div class="cov">
<div class="cov-top"><div class="cov-brand">Programación básica en C</div><div class="cov-model">Material instruccional · Mapa de ruta CLT4BP</div></div>
<div class="cov-num">{html.escape(str(num))}</div>
<div class="cov-kicker">{html.escape(kicker)}</div>
<div class="cov-title">{md_inline(meta['titulo'])}</div>
<div class="cov-lema">{md_inline(meta.get('lema', ''))}</div>
{'<div class="cov-steps">' + stepsh + '</div>' if ruta else ''}
{rutas}
<div class="cov-foot"><div class="cov-src"><b>Fuentes</b><ul>{fuentes}</ul></div>
<div class="cov-model2">Diseñado con el modelo instruccional <b>Mapa de ruta CLT4BP</b> (Cognitive Load Theory for Basic Programming): Teoría de la Carga Cognitiva · 4C/ID · Diez pasos · ARCS · Instrucción diferenciada · Protocolos verbales.<br>Sandoval Medina, C. (2026). Tesis doctoral, Universidad Autónoma de Aguascalientes.</div></div>
</div></body></html>"""


def to_pdf(stems_meta):
    from playwright.sync_api import sync_playwright
    from pypdf import PdfReader, PdfWriter
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        for meta, stem in stems_meta:
            short = meta.get("corto", meta["titulo"])
            header = (f'<div style="font-family:Inter,sans-serif;font-size:7.5pt;color:#64748b;width:100%;'
                      f'padding:0 16mm;display:flex;justify-content:space-between;">'
                      f'<span>Programación básica en C · Mapa de ruta CLT4BP</span>'
                      f'<span>{html.escape(meta.get("kicker", "Tema " + str(meta["num"])))} · {html.escape(short)}</span></div>')
            footer = ('<div style="font-family:Inter,sans-serif;font-size:7.5pt;color:#64748b;width:100%;text-align:center;">'
                      '<span class="pageNumber"></span> / <span class="totalPages"></span></div>')
            pg.goto((BUILD / f"{stem}.html").as_uri())
            pg.wait_for_timeout(150)
            body_pdf = BUILD / f"{stem}_body.pdf"
            pg.pdf(path=str(body_pdf), format="Letter", print_background=True, display_header_footer=True,
                   header_template=header, footer_template=footer,
                   margin={"top": "17mm", "bottom": "15mm", "left": "16mm", "right": "16mm"})
            pg.goto((BUILD / f"{stem}_cover.html").as_uri())
            pg.wait_for_timeout(100)
            cov_pdf = BUILD / f"{stem}_cov.pdf"
            pg.pdf(path=str(cov_pdf), format="Letter", print_background=True,
                   margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
            w = PdfWriter()
            for f in (cov_pdf, body_pdf):
                for page in PdfReader(str(f)).pages:
                    w.add_page(page)
            kick = meta.get("kicker", "Tema " + str(meta["num"]))
            w.add_metadata({"/Title": meta["titulo"] if meta["titulo"].startswith(kick) else f'{kick}. {meta["titulo"]}',
                            "/Author": "Material instruccional CLT4BP",
                            "/Subject": "Programación básica en C — Mapa de ruta CLT4BP"})
            fname = meta.get("archivo", stem) + ".pdf"
            with open(OUT / fname, "wb") as fh:
                w.write(fh)
            n = len(PdfReader(str(OUT / fname)).pages)
            log(f"[{stem}] PDF: out/{fname} ({n} páginas)")
        b.close()


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    only_html = "--html" in sys.argv
    built = []
    for a in args:
        built.append(build_doc(a))
    if not only_html:
        to_pdf(built)
