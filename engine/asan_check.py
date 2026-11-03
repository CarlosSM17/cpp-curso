import re, sys, subprocess, tempfile, os, shlex
sys.path.insert(0, 'engine')
from render import FENCE, parse_attrs
src = open(sys.argv[1]).read()
files = {}
for m in FENCE.finditer(src):
    lang, info, code = m.group(1), m.group(2), m.group(3)
    a = parse_attrs(info)
    if lang == 'txt' and 'file' in a:
        files[a['file']] = code + '\n'
    if lang != 'cpp' or not ('run' in a or 'runs' in a): continue
    code = "\n".join(re.sub(r"\s*//>.*$", "", l) for l in code.split("\n"))
    d = tempfile.mkdtemp()
    open(d+'/m.cpp','w').write(code)
    for fn, ct in files.items():
        open(os.path.join(d, fn), 'w').write(ct)
    r = subprocess.run(['g++','-std=c++20','-g','-fsanitize=address,undefined','-o',d+'/p',d+'/m.cpp'],capture_output=True,text=True)
    if r.returncode: print('COMPILE FAIL', a.get('title')); continue
    stdin = (a.get('stdin') or (a.get('runs','').split('|')[0])).replace('\\n','\n') + '\n'
    try:
        rr = subprocess.run([d+'/p'], input=stdin, capture_output=True, text=True, timeout=20, cwd=d)
    except subprocess.TimeoutExpired:
        print('TIMEOUT  ', a.get('title')); continue
    bad = 'ERROR: AddressSanitizer' in rr.stderr or 'LeakSanitizer' in rr.stderr or 'runtime error' in rr.stderr
    print(('PROBLEMA ' if bad else 'ok       ') + str(a.get('title')), ([l for l in rr.stderr.split('\n') if 'runtime error' in l or 'ERROR' in l or 'Sanitizer' in l][:1] if bad else ''))
