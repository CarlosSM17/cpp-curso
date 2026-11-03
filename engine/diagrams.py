"""Generadores de diagramas SVG para el material CLT4BP.

Cada función recibe un dict (YAML ya parseado) y devuelve una cadena <svg>.
Tipos: mem, arr, mat, stack, struct, bars. Además: dot (Graphviz) con macros
de diagrama de flujo (@term, @proc, @io, @dec, @sub, @pt, @note).
"""
import html
import re
import subprocess

INK = "#1f2937"
MUTED = "#64748b"
LINE = "#94a3b8"
BOXF = "#ffffff"
BLUE = "#2563eb"
BLUEL = "#dbeafe"
HL = "#fde68a"
HLS = "#d97706"
VIO = "#7c3aed"
VIOL = "#ede9fe"
GRN = "#059669"
GRNL = "#d1fae5"
RED = "#dc2626"
MONO = "DejaVu Sans Mono, monospace"
SANS = "Inter, sans-serif"


def esc(s):
    return html.escape(str(s), quote=True)


def text_w(s, size=12, mono=False):
    s = str(s)
    k = 0.61 if mono else 0.56
    return len(s) * size * k


def svg_wrap(w, h, body, extra_defs=""):
    defs = f"""<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>
<marker id="ahb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{BLUE}"/></marker>
<marker id="ahr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>
<marker id="ahv" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{VIO}"/></marker>
{extra_defs}</defs>"""
    return (f'<svg class="dg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" '
            f'width="{w:.0f}" height="{h:.0f}" font-family="{SANS}">{defs}{body}</svg>')


def t(x, y, s, size=12, anchor="middle", weight="normal", fill=INK, mono=False, italic=False):
    fam = MONO if mono else SANS
    st = ' font-style="italic"' if italic else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" '
            f'font-weight="{weight}" fill="{fill}" font-family="{fam}"{st}>{esc(s)}</text>')


# ---------------------------------------------------------------- mem
def mem(spec):
    """Variables como cajas de memoria, con flechas de puntero.

    spec: {regions: [{name, vars:[...]}]} o {vars:[...]}
    var: {name, type, val, addr, to, hl, note, kind: 'ptr'|'ref'|'dead'}
    """
    regions = spec.get("regions") or [{"name": None, "vars": spec.get("vars", [])}]
    gap = spec.get("gap", 26)
    rgap = 40
    pos = {}
    x = 16
    top = 34 if any(r.get("name") for r in regions) else 14
    body = []
    box_h = 40
    maxy = 0
    region_boxes = []
    for r in regions:
        rx0 = x
        vx = x + (14 if r.get("name") else 0)
        for v in r["vars"]:
            val = str(v.get("val", ""))
            name = str(v.get("name", ""))
            typ = str(v.get("type", ""))
            w = max(76, text_w(val, 13, True) + 26, text_w(name, 12.5) + 14, text_w(typ, 11, True) + 14)
            y = top + 34
            pos[name] = (vx, y, w, box_h)
            vx += w + gap
        rw = vx - gap - rx0 + (14 if r.get("name") else 0)
        region_boxes.append((rx0, rw, r))
        x = rx0 + rw + rgap
    width = x - rgap + 16
    nptr = sum(1 for r in regions for v in r["vars"] if v.get("to"))
    anyaddr = any(v.get("addr") for r in regions for v in r["vars"])
    anynote = any(v.get("note") for r in regions for v in r["vars"])
    height = top + 34 + box_h + (20 if anyaddr else 6) + (15 if anynote else 0) + (nptr * 14 + 16 if nptr else 4)
    if spec.get("caption"):
        height += 20
    # regiones
    for rx0, rw, r in region_boxes:
        if r.get("name"):
            col = r.get("color", "#f1f5f9")
            body.append(f'<rect x="{rx0}" y="{top - 22}" width="{rw}" height="{height - top - (20 if spec.get("caption") else 0) + 10}" rx="10" fill="{col}" stroke="{LINE}" stroke-dasharray="4 3"/>')
            body.append(t(rx0 + 12, top - 6, r["name"], 11.5, "start", "600", MUTED))
    # cajas
    for r in regions:
        for v in r["vars"]:
            name = str(v.get("name", ""))
            bx, by, bw, bh = pos[name]
            kind = v.get("kind")
            fill = HL if v.get("hl") else (BLUEL if kind in ("ptr",) else BOXF)
            stroke = HLS if v.get("hl") else (BLUE if kind == "ptr" else INK)
            dash = ' stroke-dasharray="5 3"' if kind == "dead" else ""
            if kind == "ref":
                stroke = VIO
                fill = VIOL
            body.append(f'<rect x="{bx:.1f}" y="{by}" width="{bw:.1f}" height="{bh}" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="1.6"{dash}/>')
            body.append(t(bx + bw / 2, by - 18, name, 12.5, weight="700"))
            if v.get("type"):
                body.append(t(bx + bw / 2, by - 5, v["type"], 10.5, mono=True, fill=MUTED))
            body.append(t(bx + bw / 2, by + bh / 2 + 4.5, v.get("val", ""), 13, mono=True,
                          fill=RED if kind == "dead" else INK))
            if v.get("addr"):
                body.append(t(bx + bw / 2, by + bh + 15, v["addr"], 10.5, mono=True, fill=BLUE))
            if v.get("note"):
                body.append(t(bx + bw / 2, by + bh + (30 if v.get("addr") else 15), v["note"], 10, fill=MUTED, italic=True))
    # flechas
    addrs = {str(v.get("name")): bool(v.get("addr")) for r in regions for v in r["vars"]}
    k = 0
    base0 = top + 34 + box_h + (20 if anyaddr else 6) + (15 if anynote else 0)
    for r in regions:
        for v in r["vars"]:
            if not v.get("to"):
                continue
            sx, sy, sw, sh = pos[str(v["name"])]
            tx, ty, tw, th = pos[str(v["to"])]
            k += 1
            x1 = sx + sw / 2
            x2 = tx + tw / 2 + (10 if tx > sx else -10)
            ybase = base0 + k * 14
            y1 = sy + sh + (19 if addrs[str(v["name"])] else 2)
            y2 = ty + th + (19 if addrs[str(v["to"])] else 3)
            col = VIO if v.get("kind") == "ref" else BLUE
            mk = "ahv" if v.get("kind") == "ref" else "ahb"
            body.append(f'<path d="M{x1:.1f},{y1} C{x1:.1f},{ybase} {x2:.1f},{ybase} {x2:.1f},{y2}" fill="none" stroke="{col}" stroke-width="1.8" marker-end="url(#{mk})"/>')
    if spec.get("caption"):
        body.append(t(width / 2, height - 6, spec["caption"], 11, fill=MUTED, italic=True))
    return svg_wrap(width, height, "".join(body))


# ---------------------------------------------------------------- arr
def arr(spec):
    """Arreglo unidimensional / cadena de caracteres.

    spec: {name, vals, hl:[i], hl2:[i], dim:[i], idx:true, addr:'0x1000', step:4,
           marks:{i:'etq'}, cw:48, caption, type}
    """
    vals = [str(v) for v in spec.get("vals", [])]
    cw = spec.get("cw", max(44, max([text_w(v, 13, True) + 16 for v in vals] or [44])))
    ch = 40
    name = spec.get("name", "")
    typ = spec.get("type", "")
    left = 16 + max(text_w(name, 13) if name else 0, text_w(typ, 10.5, True)) + (14 if name else 0)
    marks = {int(k): v for k, v in (spec.get("marks") or {}).items()}
    top = 14 + (34 if marks else 0)
    hl = set(spec.get("hl", []) or [])
    hl2 = set(spec.get("hl2", []) or [])
    dim = set(spec.get("dim", []) or [])
    body = []
    if name:
        body.append(t(left - 12, top + ch / 2 + 2, name, 13, "end", "700"))
    if typ:
        body.append(t(left - 12, top + ch / 2 + 16, typ, 10.5, "end", mono=True, fill=MUTED))
    for i, v in enumerate(vals):
        x = left + i * cw
        fill = HL if i in hl else (GRNL if i in hl2 else ("#f1f5f9" if i in dim else BOXF))
        body.append(f'<rect x="{x:.1f}" y="{top}" width="{cw:.1f}" height="{ch}" fill="{fill}" stroke="{INK}" stroke-width="1.4"/>')
        col = MUTED if i in dim else (RED if v in ("\\0", "'\\0'") else INK)
        body.append(t(x + cw / 2, top + ch / 2 + 4.5, v, 13, mono=True, fill=col))
        if spec.get("idx", True):
            body.append(t(x + cw / 2, top + ch + 15, f"[{i}]", 10.5, mono=True, fill=MUTED))
        if spec.get("addr"):
            a = int(str(spec["addr"]), 16) + i * int(spec.get("step", 4))
            body.append(t(x + cw / 2, top + ch + 30, hex(a), 9.5, mono=True, fill=BLUE))
        if i in marks:
            body.append(t(x + cw / 2, top - 22, marks[i], 11.5, weight="700", fill=VIO))
            body.append(f'<line x1="{x + cw / 2:.1f}" y1="{top - 17}" x2="{x + cw / 2:.1f}" y2="{top - 3}" stroke="{VIO}" stroke-width="1.6" marker-end="url(#ahv)"/>')
    width = left + len(vals) * cw + 16
    height = top + ch + (36 if spec.get("addr") else 22)
    if spec.get("caption"):
        height += 18
        body.append(t(width / 2, height - 6, spec["caption"], 11, fill=MUTED, italic=True))
    return svg_wrap(width, height, "".join(body))


# ---------------------------------------------------------------- mat
def mat(spec):
    """Matriz con índices de fila/columna. spec: {name, rows, hl:[[r,c]], hlrow, hlcol, caption, cw}"""
    rows = [[str(c) for c in r] for r in spec["rows"]]
    nr, nc = len(rows), max(len(r) for r in rows)
    cw = spec.get("cw", max(44, max(text_w(c, 13, True) + 16 for r in rows for c in r)))
    ch = 34
    left = 60
    top = 40 if spec.get("name") else 30
    hl = {tuple(x) for x in (spec.get("hl") or [])}
    hl2 = {tuple(x) for x in (spec.get("hl2") or [])}
    body = []
    if spec.get("name"):
        body.append(t(left, 14, spec["name"], 13, "start", "700"))
    for c in range(nc):
        body.append(t(left + c * cw + cw / 2, top - 6, f"[{c}]", 10.5, mono=True, fill=MUTED))
    for r in range(nr):
        body.append(t(left - 8, top + r * ch + ch / 2 + 4, f"[{r}]", 10.5, "end", mono=True, fill=MUTED))
        for c in range(nc):
            v = rows[r][c] if c < len(rows[r]) else ""
            x, y = left + c * cw, top + r * ch
            fill = BOXF
            if spec.get("hlrow") == r or spec.get("hlcol") == c:
                fill = BLUEL
            if (r, c) in hl2:
                fill = GRNL
            if (r, c) in hl:
                fill = HL
            body.append(f'<rect x="{x:.1f}" y="{y}" width="{cw:.1f}" height="{ch}" fill="{fill}" stroke="{INK}" stroke-width="1.2"/>')
            body.append(t(x + cw / 2, y + ch / 2 + 4.5, v, 13, mono=True))
    width = left + nc * cw + 16
    height = top + nr * ch + 12
    if spec.get("caption"):
        height += 20
        body.append(t(width / 2, height - 6, spec["caption"], 11, fill=MUTED, italic=True))
    return svg_wrap(width, height, "".join(body))


# ---------------------------------------------------------------- stack
def stack(spec):
    """Pila de llamadas. spec: {frames:[{name, vars:[[n,v],...], hl, note}], caption, title}
    El primer frame de la lista es el de abajo (main)."""
    frames = spec["frames"]
    fw = spec.get("w", 250)
    rowh = 20
    body = []
    y = 30
    heights = [30 + max(1, len(f.get("vars", []))) * rowh + 8 for f in frames]
    total = sum(heights) + 6 * (len(frames) - 1)
    x = 100
    cur = y
    for f, h in zip(reversed(frames), reversed(heights)):
        fill = HL if f.get("hl") else ("#f8fafc" if not f.get("done") else "#f1f5f9")
        dash = ' stroke-dasharray="5 3"' if f.get("done") else ""
        body.append(f'<rect x="{x}" y="{cur}" width="{fw}" height="{h}" rx="6" fill="{fill}" stroke="{INK}" stroke-width="1.4"{dash}/>')
        body.append(t(x + 10, cur + 18, f["name"], 12, "start", "700", mono=True))
        if f.get("note"):
            body.append(t(x + fw - 10, cur + 18, f["note"], 10.5, "end", fill=MUTED, italic=True))
        for i, (n, v) in enumerate(f.get("vars", [])):
            yy = cur + 38 + i * rowh
            body.append(t(x + 18, yy, str(n), 11.5, "start", mono=True, fill=MUTED))
            body.append(t(x + fw - 14, yy, str(v), 11.5, "end", mono=True))
        cur += h + 6
    body.append(t(x - 48, y + 12, spec.get("toplabel", "cima"), 10.5, "end", fill=VIO, weight="600"))
    body.append(f'<line x1="{x - 40}" y1="{y + 4}" x2="{x - 40}" y2="{y + total}" stroke="{VIO}" stroke-width="1.5" marker-start="url(#ahv)"/>')
    width = x + fw + 20
    height = y + total + 14
    if spec.get("title"):
        body.append(t(x + fw / 2, 16, spec["title"], 12, weight="700"))
    if spec.get("caption"):
        height += 18
        body.append(t(width / 2, height - 6, spec["caption"], 11, fill=MUTED, italic=True))
    return svg_wrap(width, height, "".join(body))


# ---------------------------------------------------------------- struct
def _struct_size(fields, depth=0):
    w = 0
    for f in fields:
        if "fields" in f:
            fw, _ = _struct_size(f["fields"], depth + 1)
            w += fw + 16
        else:
            w += max(70, text_w(f.get("val", ""), 12.5, True) + 22, text_w(f["name"], 11.5) + 18)
    return w, depth


def _struct_draw(fields, x, y, h, body, depth):
    for f in fields:
        if "fields" in f:
            fw, _ = _struct_size(f["fields"], depth + 1)
            fw += 8
            body.append(f'<rect x="{x}" y="{y}" width="{fw}" height="{h}" fill="{VIOL if depth % 2 == 0 else BLUEL}" stroke="{INK}" stroke-width="1.2"/>')
            body.append(t(x + fw / 2, y + 14, f["name"] + (f"  ({f['type']})" if f.get("type") else ""), 11, weight="700", fill=VIO))
            _struct_draw(f["fields"], x + 4, y + 22, h - 26, body, depth + 1)
            x += fw + 8
        else:
            fw = max(70, text_w(f.get("val", ""), 12.5, True) + 22, text_w(f["name"], 11.5) + 18)
            fill = HL if f.get("hl") else BOXF
            body.append(f'<rect x="{x}" y="{y}" width="{fw}" height="{h}" fill="{fill}" stroke="{INK}" stroke-width="1.2"/>')
            body.append(t(x + fw / 2, y + 14, f["name"], 11, weight="600", fill=MUTED))
            body.append(t(x + fw / 2, y + h / 2 + 12, f.get("val", ""), 12.5, mono=True))
            x += fw
    return x


def struct(spec):
    """Registro/estructura con campos anidados.
    spec: {var, type, fields:[{name,val,hl}|{name,type,fields:[...]}], caption}"""
    fields = spec["fields"]
    depth = 0

    def maxdepth(fs, d=0):
        m = d
        for f in fs:
            if "fields" in f:
                m = max(m, maxdepth(f["fields"], d + 1))
        return m
    depth = maxdepth(fields)
    h = 52 + depth * 26
    w, _ = _struct_size(fields)
    x0, y0 = 20, 44
    body = []
    title = spec.get("var", "")
    if spec.get("type"):
        title += f"  :  {spec['type']}"
    body.append(t(x0, 20, title, 13, "start", "700", mono=True))
    body.append(f'<rect x="{x0 - 6}" y="{y0 - 14}" width="{w + 12 + depth * 8}" height="{h + 20}" rx="8" fill="#f8fafc" stroke="{BLUE}" stroke-width="1.6"/>')
    _struct_draw(fields, x0, y0, h - 8, body, 0)
    width = x0 + w + depth * 8 + 30
    height = y0 + h + 14
    if spec.get("caption"):
        height += 20
        body.append(t(width / 2, height - 6, spec["caption"], 11, fill=MUTED, italic=True))
    return svg_wrap(width, height, "".join(body))


# ---------------------------------------------------------------- bars
def bars(spec):
    items = spec["items"]
    unit = spec.get("unit", "")
    mx = max(v for _, v in items)
    lw = max(text_w(l, 11.5, True) for l, _ in items) + 20
    bw = spec.get("w", 320)
    body = []
    y = 10
    for lab, v in items:
        L = bw * v / mx
        body.append(t(lw - 10, y + 13, lab, 11.5, "end", mono=True))
        body.append(f'<rect x="{lw}" y="{y}" width="{L:.1f}" height="18" rx="3" fill="{BLUE}" opacity="0.85"/>')
        body.append(t(lw + L + 6, y + 13, f"{v} {unit}", 11, "start", fill=MUTED))
        y += 26
    width = lw + bw + 80
    height = y + 6
    if spec.get("caption"):
        height += 18
        body.append(t(width / 2, height - 6, spec["caption"], 11, fill=MUTED, italic=True))
    return svg_wrap(width, height, "".join(body))


# ---------------------------------------------------------------- arrs (varios estados)
def arrs(spec):
    """Secuencia de estados de un arreglo (traza visual).
    spec: {cw, rows:[{label, vals, hl:[i], ok:[i], swap:true, note}], caption, idx}"""
    rows = spec["rows"]
    allv = [str(v) for r in rows for v in r["vals"]]
    cw = spec.get("cw", max(36, max(text_w(v, 12.5, True) + 14 for v in allv)))
    ch = 30
    lw = max(text_w(r.get("label", ""), 11) for r in rows) + 18
    n = max(len(r["vals"]) for r in rows)
    nw = max((text_w(r.get("note", ""), 10.5) for r in rows), default=0)
    top = 26 if spec.get("idx", True) else 8
    body = []
    if spec.get("idx", True):
        for i in range(n):
            body.append(t(lw + i * cw + cw / 2, 16, f"[{i}]", 10, mono=True, fill=MUTED))
    y = top
    for r in rows:
        hl = set(r.get("hl", []) or [])
        ok = set(r.get("ok", []) or [])
        body.append(t(lw - 10, y + ch / 2 + 4, r.get("label", ""), 11, "end", "600", fill=INK))
        for i, v in enumerate(r["vals"]):
            x = lw + i * cw
            fill = HL if i in hl else (GRNL if i in ok else BOXF)
            body.append(f'<rect x="{x:.1f}" y="{y}" width="{cw:.1f}" height="{ch}" fill="{fill}" stroke="{INK}" stroke-width="1.2"/>')
            body.append(t(x + cw / 2, y + ch / 2 + 4.5, v, 12.5, mono=True))
        if r.get("swap") and len(hl) == 2:
            a, b = sorted(hl)
            xa, xb = lw + a * cw + cw / 2, lw + b * cw + cw / 2
            body.append(f'<path d="M{xa:.1f},{y + ch + 2} Q{(xa + xb) / 2:.1f},{y + ch + 14} {xb:.1f},{y + ch + 2}" fill="none" stroke="{RED}" stroke-width="1.5" marker-end="url(#ahr)" marker-start="url(#ahr)"/>')
        if r.get("note"):
            body.append(t(lw + n * cw + 12, y + ch / 2 + 4, r["note"], 10.5, "start", fill=MUTED))
        y += ch + (18 if r.get("swap") else 8)
    width = lw + n * cw + 16 + (nw + 12 if nw else 0)
    height = y + 4
    if spec.get("caption"):
        height += 18
        body.append(t(width / 2, height - 6, spec["caption"], 11, fill=MUTED, italic=True))
    return svg_wrap(width, height, "".join(body))


GENS = {"mem": mem, "arr": arr, "mat": mat, "stack": stack, "struct": struct, "bars": bars, "arrs": arrs}


# ---------------------------------------------------------------- dot
DOT_PRE = """
  graph [fontname="Inter", bgcolor="transparent", pad="0.15", nodesep="0.35", ranksep="0.38", fontsize=11];
  node  [fontname="Inter", fontsize=12.5, shape=box, style="rounded,filled", fillcolor="#eff6ff", color="#2563eb", penwidth=1.3, margin="0.14,0.06", height=0.36];
  edge  [fontname="Inter", fontsize=11, color="#475569", arrowsize=0.7, penwidth=1.2, fontcolor="#334155"];
"""

MACROS = {
    "term": 'shape=box, style="rounded,filled", fillcolor="#1e293b", fontcolor="white", color="#1e293b"',
    "proc": 'shape=box, style="filled", fillcolor="#eff6ff", color="#2563eb"',
    "io":   'shape=parallelogram, style="filled", fillcolor="#ecfdf5", color="#059669", margin="0.05,0.04"',
    "dec":  'shape=diamond, style="filled", fillcolor="#fef3c7", color="#d97706", margin="0.02,0.02"',
    "sub":  'shape=box, style="filled", fillcolor="#f5f3ff", color="#7c3aed", peripheries=2',
    "pt":   'shape=point, width=0.06, height=0.06, color="#475569"',
    "note": 'shape=plaintext, style="", fontcolor="#475569", fontsize=12',
    "hl":   'shape=box, style="filled", fillcolor="#fde68a", color="#d97706"',
    "file": 'shape=note, style="filled", fillcolor="#f8fafc", color="#475569"',
    "cls":  'shape=plaintext, style=""',
}


def dot_svg(src):
    def rep(m):
        kind, nid, rest = m.group(1), m.group(2), m.group(3)
        label = ""
        if rest:
            label = rest.strip().lstrip(",").strip()
        attrs = MACROS[kind]
        if kind == "pt":
            return f'{nid} [{attrs}];'
        if label.startswith("<"):
            return f'{nid} [label={label}, {attrs}];'
        return f'{nid} [label={label}, {attrs}];'
    body = re.sub(r'@(\w+)\(\s*(\w+)\s*(?:,(.*?))?\)\s*;?\s*$', rep, src, flags=re.M)
    body = re.sub(r'"#([0-9a-fA-F])([0-9a-fA-F])([0-9a-fA-F])"', r'"#\1\1\2\2\3\3"', body)
    if not re.match(r'\s*(di)?graph', body):
        body = "digraph G {\n" + DOT_PRE + body + "\n}"
    else:
        body = re.sub(r'\{', "{\n" + DOT_PRE, body, count=1)
    p = subprocess.run(["dot", "-Tsvg"], input=body.encode(), capture_output=True)
    if p.returncode != 0:
        raise RuntimeError("dot error:\n" + p.stderr.decode() + "\n" + body)
    svg = p.stdout.decode()
    svg = svg[svg.find("<svg"):]
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    # quitar fondo blanco/transparente de graphviz
    svg = re.sub(r'<polygon fill="transparent"[^>]*/>', "", svg, count=1)
    m = re.search(r'width="([\d.]+)pt" height="([\d.]+)pt"', svg)
    if m:
        w, h = float(m.group(1)), float(m.group(2))
        svg = svg.replace(m.group(0), f'width="{w*1.333:.0f}" height="{h*1.333:.0f}"', 1)
    svg = svg.replace("<svg", '<svg class="dg"', 1)
    return svg
