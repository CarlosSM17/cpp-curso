"""Ejecuta los programas `run` de un tema con AddressSanitizer y UBSan.

Uso: python3 engine/asan_check.py temas/15_memoria_dinamica.md
"""
import re, sys, subprocess, tempfile, os, shlex
sys.path.insert(0, 'engine')
from render import FENCE, parse_attrs
src = open(sys.argv[1]).read()
files = {}
limpiar = lambda c: "\n".join(re.sub(r"\s*//>.*$", "", l) for l in c.split("\n"))
futuros = [(m.start(), parse_attrs(m.group(2)).get('file'), limpiar(m.group(3)) + '\n')
           for m in FENCE.finditer(src) if m.group(1) == 'c' and parse_attrs(m.group(2)).get('file')]
for m in FENCE.finditer(src):
    lang, info, code = m.group(1), m.group(2), m.group(3)
    a = parse_attrs(info)
    if lang == 'txt' and 'file' in a:
        files[a['file']] = code + '\n'
    if lang == 'c':
        code = limpiar(code)
        if 'file' in a:                      # archivo de un programa de varios archivos
            files[a['file']] = code + '\n'
    if lang != 'c' or not ('run' in a or 'runs' in a): continue
    link = a.get('link', '').split()
    archivos = dict(files)
    for n in link:                           # módulo definido más adelante (columna de al lado)
        if n not in archivos:
            archivos[n] = next((c for pos, nm, c in futuros if nm == n and pos > m.start()), '')
    d = tempfile.mkdtemp()
    open(d+'/m.c','w').write(code)
    for fn, ct in archivos.items():
        open(os.path.join(d, fn), 'w').write(ct)
    r = subprocess.run([os.environ.get('CC', 'gcc'),'-std=c17','-g','-fsanitize=address,undefined','-o',d+'/p',d+'/m.c',*[os.path.join(d, n) for n in link],'-lm'],capture_output=True,text=True)
    if r.returncode: print('COMPILE FAIL', a.get('title')); continue
    stdin = (a.get('stdin') or (a.get('runs','').split('|')[0])).replace('\\n','\n') + '\n'
    try:
        rr = subprocess.run([d+'/p'], input=stdin, capture_output=True, text=True, timeout=20, cwd=d)
    except subprocess.TimeoutExpired:
        print('TIMEOUT  ', a.get('title')); continue
    bad = 'ERROR: AddressSanitizer' in rr.stderr or 'LeakSanitizer' in rr.stderr or 'runtime error' in rr.stderr
    print(('PROBLEMA ' if bad else 'ok       ') + str(a.get('title') or a.get('file')), ([l for l in rr.stderr.split('\n') if 'runtime error' in l or 'ERROR' in l or 'Sanitizer' in l][:1] if bad else ''))
