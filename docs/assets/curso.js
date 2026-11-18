/* Programación básica en C · curso interactivo (mapa de ruta CLT4BP)
   Sin dependencias. El progreso se guarda en localStorage (clave clt4bp-c-v1). */
(function () {
  'use strict';
  var C = window.COURSE || { temas: [], bloques: [], pasos: [] };
  var PAGE = window.PAGE || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var CIRC = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳';
  var PASOS = ['soporte', 'procedimental', 'tareas', 'protocolo', 'evaluacion'];
  var NOMBRE_PASO = { soporte: 'Información de soporte', procedimental: 'Información procedimental', tareas: 'Tareas de aprendizaje', protocolo: 'Protocolo verbal', evaluacion: 'Evaluación' };
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ------------------------------------------------------------ estado */
  var KEY = 'clt4bp-c-v1';
  var estado = null;
  function cargar() {
    if (estado) return estado;
    var s = {};
    try { s = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { s = {}; }
    s.v = 1; s.temas = s.temas || {}; s.ruta = s.ruta || {}; s.diag = s.diag || {}; s.encuesta = s.encuesta || {};
    estado = s; return s;
  }
  var tg = null;
  function guardar() { clearTimeout(tg); tg = setTimeout(guardarYa, 150); }
  function guardarYa() { clearTimeout(tg); try { localStorage.setItem(KEY, JSON.stringify(estado)); } catch (e) { /* modo privado o bloqueado */ } }
  window.addEventListener('pagehide', function () { if (estado) guardarYa(); });
  function tema(num) {
    var s = cargar();
    var t = s.temas[num] || (s.temas[num] = {});
    ['pasos', 'tareas', 'huecos', 'recall', 'resp', 'compr', 'checks', 'notas'].forEach(function (k) { if (!t[k]) t[k] = {}; });
    if (t.esfuerzo === undefined) t.esfuerzo = null;
    return t;
  }
  function infoTema(num) { for (var i = 0; i < C.temas.length; i++) if (C.temas[i].num === num) return C.temas[i]; return null; }
  function pasosHechos(num) { var t = cargar().temas[num]; if (!t || !t.pasos) return 0; return PASOS.filter(function (p) { return t.pasos[p]; }).length; }
  function contar(obj, val) { var n = 0; for (var k in obj) if (obj[k] === val) n++; return n; }
  function resumenTema(num) {
    var t = cargar().temas[num] || {}; var info = infoTema(num) || { tareas: [] };
    var r = { pasos: pasosHechos(num), tareas: 0, tareasTot: info.tareas.length, hOk: 0, hTot: 0, rOk: 0, rN: 0, cOk: 0, cN: 0, esf: t.esfuerzo || null };
    if (t.tareas) r.tareas = info.tareas.filter(function (x) { return t.tareas[x.id]; }).length;
    if (t.huecos) for (var k in t.huecos) { var h = t.huecos[k]; if (h && h.ok) { r.hOk += h.ok[0]; r.hTot += h.ok[1]; } }
    if (t.recall) { for (var j in t.recall) { r.rN++; if (t.recall[j] === 1) r.rOk++; } }
    if (t.compr) { for (var c in t.compr) { r.cN++; if (t.compr[c] === 1) r.cOk++; } }
    return r;
  }
  function estadoTema(num) { var p = pasosHechos(num); var t = cargar().temas[num]; var algo = t && (p > 0 || Object.keys(t.tareas || {}).length || Object.keys(t.recall || {}).length); return p === 5 ? 'hecho' : (algo ? 'curso' : 'nada'); }

  /* ------------------------------------------------------------ utilidades */
  function el(tag, attrs, html) {
    var e = document.createElement(tag);
    if (attrs) for (var k in attrs) { if (k === 'class') e.className = attrs[k]; else if (k === 'text') e.textContent = attrs[k]; else e.setAttribute(k, attrs[k]); }
    if (html !== undefined) e.innerHTML = html;
    return e;
  }
  function b64dec(s) { try { var b = atob(s); var bytes = new Uint8Array(b.length); for (var i = 0; i < b.length; i++) bytes[i] = b.charCodeAt(i); return new TextDecoder('utf-8').decode(bytes); } catch (e) { return ''; } }
  function b64enc(s) { var bytes = new TextEncoder().encode(s); var b = ''; for (var i = 0; i < bytes.length; i++) b += String.fromCharCode(bytes[i]); return btoa(b); }
  function norm(s) { return String(s || '').replace(/[“”]/g, '"').replace(/[‘’]/g, "'").replace(/\s+/g, ''); }
  function textoPlano(h) { var d = document.createElement('div'); d.innerHTML = h; return (d.textContent || '').trim(); }
  function copiar(txt) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(txt);
    return new Promise(function (ok, no) {
      var ta = el('textarea'); ta.value = txt; ta.style.position = 'fixed'; ta.style.opacity = '0'; document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy') ? ok() : no(); } catch (e) { no(e); } document.body.removeChild(ta);
    });
  }
  function descargar(nombre, contenido, tipo) {
    var blob = new Blob([contenido], { type: tipo });
    var a = el('a', { href: URL.createObjectURL(blob), download: nombre }); document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }
  function hoy() { var d = new Date(); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); }

  /* ------------------------------------------------------------ cabecera */
  function cabecera() {
    var btn = $('.menu-btn'), nav = $('#nav-principal');
    if (btn && nav) btn.addEventListener('click', function () { var a = nav.classList.toggle('abierto'); btn.setAttribute('aria-expanded', a ? 'true' : 'false'); });
    var tb = $('.tema-btn');
    function oscuroActual() { var d = document.documentElement.dataset.theme; if (d) return d === 'dark'; return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches; }
    function rotulo() { if (tb) $('.tema-txt', tb).textContent = oscuroActual() ? 'Modo claro' : 'Modo oscuro'; }
    if (tb) {
      rotulo();
      tb.addEventListener('click', function () {
        var nuevo = oscuroActual() ? 'light' : 'dark';
        document.documentElement.dataset.theme = nuevo;
        try { localStorage.setItem('clt4bp-tema', nuevo); } catch (e) { }
        rotulo();
      });
    }
  }

  /* ------------------------------------------------------------ código */
  function codigoActual(wrap) {
    var src = b64dec(wrap.dataset.src || '');
    if (wrap.dataset.blank) {
      var ins = $$('input.hole', wrap), i = 0;
      src = src.replace(/__(\d+|\?)__/g, function (m) { var inp = ins[i++]; var v = inp && inp.value.trim(); return v ? v : m; });
    }
    return src;
  }
  function urlCE(src, stdin, flags) {
    var opts = '-std=c17 -Wall -Wextra' + (flags ? ' ' + flags : '') + ' -lm';
    var st = { sessions: [{ id: 1, language: 'c', source: src, compilers: [], executors: [{ arguments: '', compiler: { id: 'cg142', libs: [], options: opts }, stdin: stdin || '' }] }] };
    return 'https://godbolt.org/clientstate/' + encodeURIComponent(b64enc(JSON.stringify(st)));
  }
  function animarSalida(term) {
    var pres = $$('pre', term);
    term.classList.remove('oculta');
    if (reduceMotion) return;
    pres.forEach(function (pre) {
      if (!pre.dataset.html) pre.dataset.html = pre.innerHTML;
      var lineas = pre.dataset.html.split('\n'); var n = lineas.length;
      var paso = Math.max(12, Math.min(45, 900 / n)); var k = 0;
      pre.innerHTML = '';
      (function sig() { k++; pre.innerHTML = lineas.slice(0, k).join('\n'); if (k < n) setTimeout(sig, paso); })();
    });
  }
  function herramientasCodigo() {
    $$('.codewrap[data-src]').forEach(function (wrap) {
      var modo = wrap.dataset.mode;
      var compila = modo === 'err' || modo === 'warn';
      var enSol = !!wrap.closest('details.sol');
      var salidas = $$(':scope > .term, :scope > .filebox', wrap);
      var bar = el('div', { class: 'code-tools' });
      var fig = $(':scope > figure', wrap);
      if (fig && fig.nextSibling) wrap.insertBefore(bar, fig.nextSibling); else wrap.appendChild(bar);
      if (salidas.length && !enSol && (modo === 'run' || modo === 'runs' || compila)) {
        salidas.forEach(function (s) { s.classList.add('oculta'); });
        var lbl = compila ? 'Compilar' : (modo === 'runs' ? 'Ejecutar con varios datos' : 'Ejecutar');
        var run = el('button', { class: 'ct-btn ct-run' + (compila ? ' err' : ''), type: 'button', text: lbl });
        var nota = el('span', { class: 'ct-nota', text: modo === 'err' ? '¿Qué error esperas?' : (modo === 'warn' ? '¿Qué advertencia esperas?' : 'Predice la salida antes de ejecutar.') });
        run.addEventListener('click', function () {
          salidas.forEach(function (s) { if (s.classList.contains('term')) animarSalida(s); else s.classList.remove('oculta'); });
          run.textContent = compila ? 'Compilar de nuevo' : 'Ejecutar de nuevo';
          nota.textContent = compila ? 'Mensaje real de gcc.' : 'Salida real del programa (compilado con gcc).';
        });
        bar.appendChild(run); bar.appendChild(nota);
      }
      var cp = el('button', { class: 'ct-btn', type: 'button', text: 'Copiar código' });
      cp.addEventListener('click', function () {
        copiar(codigoActual(wrap)).then(function () { cp.textContent = 'Copiado'; setTimeout(function () { cp.textContent = 'Copiar código'; }, 1600); },
          function () { cp.textContent = 'No se pudo copiar'; });
      });
      bar.appendChild(cp);
      var variosArchivos = wrap.dataset.modulos || wrap.dataset.modulo;
      if (!variosArchivos && (modo !== 'display' || wrap.dataset.blank)) {
        var ce = el('a', { class: 'ct-btn', href: '#', target: '_blank', rel: 'noopener', text: compila ? 'Corregirlo en Compiler Explorer' : 'Probar en Compiler Explorer' });
        ce.title = 'Abre el código en godbolt.org para editarlo y ejecutarlo' + (wrap.dataset.stdin ? ' (con los datos de entrada del ejemplo)' : '');
        var fijar = function () { ce.href = urlCE(codigoActual(wrap), wrap.dataset.stdin ? b64dec(wrap.dataset.stdin) : '', wrap.dataset.flags); };
        ce.addEventListener('mousedown', fijar); ce.addEventListener('focus', fijar); ce.addEventListener('click', fijar); ce.addEventListener('touchstart', fijar, { passive: true });
        bar.appendChild(ce);
      }
      if (wrap.dataset.modulos) bar.appendChild(el('span', { class: 'ct-nota', text: 'Programa de varios archivos (' + wrap.dataset.modulos + '): para probarlo, créalos en un proyecto de tu IDE o compílalos juntos en la terminal.' }));
      else if (wrap.dataset.modulo) bar.appendChild(el('span', { class: 'ct-nota', text: 'Es uno de los archivos del programa: se compila junto con los demás.' }));
      if (wrap.dataset.files) bar.appendChild(el('span', { class: 'ct-nota', text: 'Lee archivos (' + wrap.dataset.files + '): para probarlo, créalos junto al programa en tu computadora.' }));
    });
  }

  /* ------------------------------------------------------------ soluciones */
  function plegarSoluciones() {
    $$('div.sol').forEach(function (d) {
      var det = el('details', { class: 'sol' }); det.dataset.label = d.dataset.label || '';
      var sum = el('summary', { text: 'Ver solución' }); det.appendChild(sum);
      var body = el('div', { class: 'sol-b' }); while (d.firstChild) body.appendChild(d.firstChild); det.appendChild(body);
      d.parentNode.replaceChild(det, d);
    });
  }

  /* ------------------------------------------------------------ huecos */
  function respuestasHuecos(sol) {
    var out = {};
    $$('.circ', sol).forEach(function (c) {
      var n = CIRC.indexOf(c.textContent.trim()) + 1; if (n <= 0 || out[n]) return;
      var alts = [], txt = '', nd = c.nextSibling;
      while (nd && !(nd.nodeType === 1 && nd.classList.contains('circ'))) {
        if (nd.nodeType === 1 && nd.tagName === 'CODE') alts.push(nd.textContent);
        else txt += nd.textContent || '';
        nd = nd.nextSibling;
      }
      if (!alts.length) { var t = txt.replace(/[·.]\s*$/, '').replace(/^\s*/, '').trim(); if (t) alts.push(t); }
      if (alts.length) out[n] = alts;
    });
    return out;
  }
  function huecos(num) {
    var t = tema(num);
    $$('.c-tarea').forEach(function (tarea) {
      var ins = $$('input.hole[data-n]', tarea).filter(function (i) { return !i.closest('details.sol'); });
      if (!ins.length) return;
      var tid = tarea.id; var sol = $('details.sol', tarea); var resp = sol ? respuestasHuecos(sol) : {};
      var st = t.huecos[tid] || (t.huecos[tid] = { v: {} }); st.v = st.v || {};
      ins.forEach(function (inp) {
        var n = inp.dataset.n; var a = resp[n];
        if (a) { var L = Math.max.apply(null, a.map(function (x) { return x.length; })); inp.style.width = Math.min(34, Math.max(4, L + 2)) + 'ch'; }
        if (st.v[n]) inp.value = st.v[n];
        inp.addEventListener('input', function () { st.v[n] = inp.value; inp.classList.remove('ok', 'mal'); guardar(); });
      });
      var conResp = ins.filter(function (i) { return resp[i.dataset.n]; });
      if (!conResp.length) return;
      var ultimo = ins[ins.length - 1].closest('.codewrap');
      var bar = el('div', { class: 'huecos-bar' });
      var bOk = el('button', { class: 'btn btn-chico btn-primario', type: 'button', text: 'Comprobar huecos' });
      var bVer = el('button', { class: 'btn btn-chico', type: 'button', text: 'Mostrar respuestas' });
      var res = el('span', { class: 'hb-res', role: 'status', 'aria-live': 'polite' });
      bar.appendChild(bOk); bar.appendChild(bVer); bar.appendChild(res);
      ultimo.parentNode.insertBefore(bar, ultimo.nextSibling);
      function comprobar(silencioso) {
        var ok = 0;
        conResp.forEach(function (inp) {
          var bien = resp[inp.dataset.n].some(function (a) { return norm(a) === norm(inp.value); });
          inp.classList.toggle('ok', bien); inp.classList.toggle('mal', !bien && inp.value.trim() !== '');
          if (bien) ok++;
        });
        st.ok = [ok, conResp.length]; guardar();
        if (!silencioso) {
          res.className = 'hb-res ' + (ok === conResp.length ? 'ok' : 'mal');
          res.textContent = ok === conResp.length ? '¡Todos los huecos son correctos!' : ok + ' de ' + conResp.length + ' huecos correctos. Revisa los marcados en rojo.';
        }
      }
      bOk.addEventListener('click', function () { comprobar(false); });
      bVer.addEventListener('click', function () {
        conResp.forEach(function (inp) { if (!inp.classList.contains('ok')) { inp.value = resp[inp.dataset.n][0]; st.v[inp.dataset.n] = inp.value; } });
        res.className = 'hb-res'; res.textContent = 'Respuestas mostradas. Compara con lo que habías escrito y lee la explicación en la solución.';
        conResp.forEach(function (inp) { inp.classList.remove('mal'); }); guardar();
      });
      if (st.ok && Object.keys(st.v).length) comprobar(true);
    });
  }

  /* ------------------------------------------------------------ tareas y rutas */
  function rutaDe(bloque) { return cargar().ruta[bloque] || null; }
  function selectorRuta(bloque, alCambiar) {
    var cont = $('.selector-ruta'); if (!cont) return;
    function pintar() {
      var r = rutaDe(bloque); var d = cargar().diag[bloque];
      cont.innerHTML = '';
      cont.appendChild(el('span', { class: 'sr-t', text: 'Mi ruta en el bloque ' + bloque + ':' }));
      var seg = el('div', { class: 'seg', role: 'group', 'aria-label': 'Elegir ruta' });
      [['A', 'Ruta A'], ['B', 'Ruta B']].forEach(function (x) {
        var b = el('button', { type: 'button', 'data-ruta': x[0], 'aria-pressed': r === x[0] ? 'true' : 'false', text: x[1] });
        b.title = x[0] === 'A' ? 'Sin conocimientos previos: ejemplos resueltos y problemas por completar' : 'Con conocimientos previos: autoexplicación, imaginación y retos';
        b.addEventListener('click', function () { cargar().ruta[bloque] = x[0]; guardar(); pintar(); alCambiar(); });
        seg.appendChild(b);
      });
      cont.appendChild(seg);
      var nota = d ? 'Tu diagnóstico: ' + d.aciertos + ' de ' + d.total + ' (sugiere la Ruta ' + (d.aciertos / d.total >= 0.7 ? 'B' : 'A') + ').' : '';
      cont.appendChild(el('span', { class: 'sr-nota', html: nota || (r ? '' : '<a href="diagnostico.html#bloque-' + bloque + '">Haz el diagnóstico del bloque</a> para que te sugiramos una.') }));
      var temaEl = $('.tema'); if (temaEl) { if (r) temaEl.dataset.ruta = r; else delete temaEl.dataset.ruta; }
    }
    pintar();
  }
  function tareas(num, bloque) {
    var t = tema(num);
    $$('.c-tarea').forEach(function (ta) {
      var h = $('.tarea-h', ta); if (!h) return;
      var b = el('button', { class: 'tarea-hecha', type: 'button' });
      function pintar() { var si = !!t.tareas[ta.id]; b.setAttribute('aria-pressed', si ? 'true' : 'false'); b.textContent = si ? 'Hecha' : 'Marcar como hecha'; }
      b.addEventListener('click', function () { t.tareas[ta.id] = !t.tareas[ta.id]; if (!t.tareas[ta.id]) delete t.tareas[ta.id]; guardar(); pintar(); });
      pintar(); h.appendChild(b);
    });
    filtrarTareas(bloque);
  }
  function filtrarTareas(bloque) {
    var r = rutaDe(bloque);
    $$('.c-tarea').forEach(function (ta) {
      var tr = ta.dataset.ruta; var otra = r && tr && tr !== 'AB' && tr !== r;
      var aviso = $('.otra-ruta', ta); if (aviso) aviso.remove();
      ta.classList.toggle('plegada', !!otra);
      if (otra) {
        var a = el('div', { class: 'otra-ruta' }, '<span>Tarea de la Ruta ' + tr + ': está plegada porque elegiste la Ruta ' + r + '.</span>');
        var bt = el('button', { type: 'button', text: 'Mostrarla' });
        bt.addEventListener('click', function () { var p = ta.classList.toggle('plegada'); bt.textContent = p ? 'Mostrarla' : 'Plegarla'; });
        a.appendChild(bt); $('.tarea-h', ta).appendChild(a);
      }
    });
    var av = $('.aviso-ruta');
    if (av) {
      if (r) av.innerHTML = 'Estás en la <b>Ruta ' + r + '</b> de este bloque: ' + (r === 'A' ? 'empieza por el ejemplo resuelto y los problemas por completar.' : 'puedes saltar a las tareas de autoexplicación, imaginación y solución libre.') + ' Las tareas de la otra ruta aparecen plegadas; ábrelas cuando quieras.';
      else av.innerHTML = 'Aún no eliges ruta para este bloque, así que ves todas las tareas. <a href="diagnostico.html#bloque-' + bloque + '">Haz el diagnóstico</a> o elige una ruta arriba.';
    }
  }

  /* ------------------------------------------------------------ evaluación */
  function partirNumerados(h, n) {
    var s = h.trim(); if (!/^1\s/.test(s)) return null;
    var ini = [0];
    for (var i = 2; i <= n; i++) { var k = s.indexOf(' · ' + i + ' ', ini[ini.length - 1] + 1); if (k < 0) return null; ini.push(k); }
    var out = [];
    for (var j = 0; j < n; j++) { var seg = s.slice(ini[j], j + 1 < n ? ini[j + 1] : s.length); out.push(seg.replace(/^\s*·?\s*\d+\s/, '').trim().replace(/\.$/, '')); }
    return out;
  }
  function marcaBtns(cont, valor, alCambiar) {
    var box = el('div', { class: 'sol-marca' }); box.appendChild(el('span', { text: '¿Cómo te fue?' }));
    var si = el('button', { class: 'marca-btn si', type: 'button', text: 'Lo tenía bien' });
    var no = el('button', { class: 'marca-btn no', type: 'button', text: 'Me faltó algo' });
    function pintar(v) { si.setAttribute('aria-pressed', v === 1 ? 'true' : 'false'); no.setAttribute('aria-pressed', v === 0 ? 'true' : 'false'); }
    si.addEventListener('click', function () { pintar(1); alCambiar(1); });
    no.addEventListener('click', function () { pintar(0); alCambiar(0); });
    pintar(valor); box.appendChild(si); box.appendChild(no); cont.appendChild(box);
  }
  function recall(num) {
    var t = tema(num); var box = $('.c-recall'); if (!box) return;
    var ol = $(':scope > ol', box); var sol = $('details.sol[data-label^="Evaluación 5.1"]');
    if (!ol || !sol) return;
    var p = $('.sol-b > p', sol); var items = $$(':scope > li', ol);
    var resp = p ? partirNumerados(p.innerHTML, items.length) : null; if (!resp) return;
    sol.hidden = true;
    var res = el('p', { class: 'ev-res', role: 'status', 'aria-live': 'polite' }); ol.parentNode.insertBefore(res, ol);
    function total() { var r = resumenTema(num); res.innerHTML = 'Recall: ' + r.rOk + ' de ' + items.length + ' correctas <small>(' + r.rN + ' de ' + items.length + ' respondidas)</small>'; }
    items.forEach(function (li, i) {
      var k = String(i + 1); var ans = resp[i]; var ansTxt = textoPlano(ans);
      li.classList.add('r-item');
      var h = li.innerHTML;
      var mOp = /(^|\s|<br>)a\)\s/.exec(h);
      var esMC = mOp && /^[a-e]$/i.test(ansTxt);
      var esVF = /verdadero o falso/i.test(li.textContent) && /^(verdadero|falso)/i.test(ansTxt);
      if (esMC) {
        var preg = h.slice(0, mOp.index).replace(/<br>\s*$/, '');
        var resto = h.slice(mOp.index + mOp[1].length);
        var partes = resto.split(/\s*(?:·\s*)?(?=\b[b-e]\)\s)/);
        li.innerHTML = '<div class="r-q">' + preg + '</div>';
        var ul = el('ul', { class: 'r-ops' }); var fb = el('p', { class: 'r-fb', 'aria-live': 'polite' });
        partes.forEach(function (pt) {
          var m = /^([a-e])\)\s*([\s\S]*)$/.exec(pt.trim()); if (!m) return;
          var letra = m[1]; var bt = el('button', { class: 'r-op', type: 'button' }, '<b>' + letra + ')</b>' + m[2].replace(/\s*·\s*$/, ''));
          bt.addEventListener('click', function () {
            $$('.r-op', ul).forEach(function (x) { x.classList.remove('ok', 'mal'); });
            var bien = letra.toLowerCase() === ansTxt.toLowerCase();
            bt.classList.add(bien ? 'ok' : 'mal');
            if (!bien) $$('.r-op', ul).forEach(function (x) { if (x.firstChild.textContent.charAt(0) === ansTxt.toLowerCase()) x.classList.add('ok'); });
            fb.className = 'r-fb ' + (bien ? 'ok' : 'mal'); fb.textContent = bien ? 'Correcto.' : 'No es esa: la respuesta correcta es la ' + ansTxt + ').';
            t.recall[k] = bien ? 1 : 0; t.resp[k] = letra; guardar(); total();
          });
          var lii = el('li'); lii.appendChild(bt); ul.appendChild(lii);
          if (t.resp[k] === letra) setTimeout(function () { bt.click(); }, 0);
        });
        li.appendChild(ul); li.appendChild(fb);
      } else if (esVF) {
        var ul2 = el('ul', { class: 'r-ops' }); var fb2 = el('p', { class: 'r-fb', 'aria-live': 'polite' }); var exp = el('div', { class: 'r-resp', hidden: '' }, '<b>Respuesta</b>' + ans);
        ['Verdadero', 'Falso'].forEach(function (v) {
          var bt = el('button', { class: 'r-op', type: 'button', text: v });
          bt.addEventListener('click', function () {
            $$('.r-op', ul2).forEach(function (x) { x.classList.remove('ok', 'mal'); });
            var bien = ansTxt.toLowerCase().indexOf(v.toLowerCase()) === 0; bt.classList.add(bien ? 'ok' : 'mal');
            fb2.className = 'r-fb ' + (bien ? 'ok' : 'mal'); fb2.textContent = bien ? 'Correcto.' : 'No es correcto.'; exp.hidden = false;
            t.recall[k] = bien ? 1 : 0; t.resp[k] = v; guardar(); total();
          });
          var lii = el('li'); lii.appendChild(bt); ul2.appendChild(lii);
          if (t.resp[k] === v) setTimeout(function () { bt.click(); }, 0);
        });
        li.appendChild(ul2); li.appendChild(fb2); li.appendChild(exp);
      } else {
        var wrap = el('div', { class: 'r-abierta' });
        var ta = el('textarea', { class: 'resp', rows: '2', placeholder: 'Tu respuesta', 'aria-label': 'Tu respuesta a la pregunta ' + k });
        ta.value = t.resp[k] || '';
        ta.addEventListener('input', function () { t.resp[k] = ta.value; guardar(); });
        var ver = el('button', { class: 'btn btn-chico', type: 'button', text: 'Comparar con la respuesta' });
        var rr = el('div', { class: 'r-resp', hidden: '' }, '<b>Respuesta esperada</b>' + ans);
        var marcas = el('div');
        ver.addEventListener('click', function () { rr.hidden = false; ver.hidden = true; if (!marcas.firstChild) marcaBtns(marcas, t.recall[k], function (v) { t.recall[k] = v; guardar(); total(); }); });
        wrap.appendChild(ta); wrap.appendChild(ver); wrap.appendChild(rr); wrap.appendChild(marcas);
        li.appendChild(wrap);
        if (t.recall[k] !== undefined) ver.click();
      }
    });
    total();
  }
  function gruposP(cont) {
    var gs = [], cur = null;
    Array.prototype.slice.call(cont.children).forEach(function (e) {
      var s = e.firstElementChild;
      var m = e.tagName === 'P' && s && s.tagName === 'STRONG' && e.innerHTML.trim().indexOf('<strong>') === 0 && /^P(\d+)\./.exec(s.textContent.trim());
      if (m) { cur = { n: m[1], els: [e] }; gs.push(cur); } else if (cur) cur.els.push(e);
    });
    return gs;
  }
  function comprension(num) {
    var t = tema(num); var box = $('.c-compr'); var sol = $('details.sol[data-label^="Evaluación 5.2"]');
    if (!box || !sol) return;
    var gP = gruposP(box), gS = gruposP($('.sol-b', sol)); if (!gP.length || !gS.length) return;
    var res = el('p', { class: 'ev-res', role: 'status', 'aria-live': 'polite' });
    var cab = $('.caja-h', box); box.insertBefore(res, cab ? cab.nextSibling : box.firstChild);
    function total() { var r = resumenTema(num); res.innerHTML = 'Comprensión: ' + r.cOk + ' de ' + gP.length + ' problemas resueltos bien <small>(autoevaluación)</small>'; }
    gP.forEach(function (g) {
      var s = gS.filter(function (x) { return x.n === g.n; })[0]; if (!s) return;
      var det = el('details', { class: 'sol sol-p' }); det.appendChild(el('summary', { text: 'Ver solución de P' + g.n }));
      var body = el('div', { class: 'sol-b' }); s.els.forEach(function (e) { body.appendChild(e); }); det.appendChild(body);
      marcaBtns(det, t.compr[g.n], function (v) { t.compr[g.n] = v; guardar(); total(); });
      var ult = g.els[g.els.length - 1]; ult.parentNode.insertBefore(det, ult.nextSibling);
    });
    if (!$('.sol-b', sol).children.length) sol.remove(); else sol.querySelector('summary').textContent = 'Ver el resto de las soluciones';
    total();
  }
  function autorregistro(num) {
    var t = tema(num); var box = $('.c-registro'); if (!box) return;
    $$('ul.checks', box).forEach(function (ul) {
      ul.classList.add('interactiva');
      $$(':scope > li', ul).forEach(function (li, i) {
        var lab = el('label', { class: 'reg-item' }); var cb = el('input', { type: 'checkbox' }); cb.checked = !!t.checks[i];
        cb.addEventListener('change', function () { t.checks[i] = cb.checked; guardar(); });
        var sp = el('span'); sp.innerHTML = li.innerHTML; lab.appendChild(cb); lab.appendChild(sp); li.innerHTML = ''; li.appendChild(lab);
      });
    });
    $$('.escala', box).forEach(function (esc) {
      esc.classList.add('interactiva'); esc.setAttribute('role', 'group'); esc.setAttribute('aria-label', 'Esfuerzo mental invertido, de 1 a 9');
      $$(':scope > span', esc).forEach(function (sp) {
        var v = parseInt(sp.textContent, 10); var b = el('button', { type: 'button', text: String(v), 'aria-pressed': t.esfuerzo === v ? 'true' : 'false' });
        b.addEventListener('click', function () { t.esfuerzo = v; guardar(); $$('button', esc).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); });
        sp.innerHTML = ''; sp.appendChild(b);
      });
      esc.insertAdjacentHTML('afterend', '<div class="esc-ext"><span>1: muy, muy bajo</span><span>9: muy, muy alto</span></div>');
    });
  }
  function notas(num) {
    var t = tema(num);
    $$('textarea.resp').forEach(function (ta, i) {
      if (ta.closest('.r-abierta')) return;
      var k = 'n' + i; if (t.notas[k]) ta.value = t.notas[k];
      ta.addEventListener('input', function () { t.notas[k] = ta.value; guardar(); });
    });
  }

  /* ------------------------------------------------------------ paneles del tema */
  function paneles(num) {
    var t = tema(num);
    var ps = $$('.panel'); if (!ps.length) return;
    var ids = ps.map(function (p) { return p.id; });
    var enlaces = $$('.rail a[data-paso]');
    function pintarRail(actual) {
      enlaces.forEach(function (a) {
        var p = a.dataset.paso; a.classList.toggle('hecho', !!t.pasos[p]);
        if (a.classList.contains('est')) { if (p === actual) a.setAttribute('aria-current', 'step'); else a.removeAttribute('aria-current'); }
        else { if (p === actual) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current'); }
      });
    }
    function mostrar(id, desplazar, foco, sinHash) {
      if (ids.indexOf(id) < 0) id = ids[0];
      ps.forEach(function (p) { p.classList.toggle('on', p.id === id); });
      pintarRail(id);
      if (!sinHash && location.hash !== '#' + id) history.replaceState(null, '', '#' + id);
      if (desplazar) { var c = $('.tema-cuerpo'); var y = c.getBoundingClientRect().top + window.scrollY - 70; if (window.scrollY > y) window.scrollTo(0, y); }
      if (foco) { var h = $('#h-' + id); if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); } }
    }
    function desdeHash() {
      var h = decodeURIComponent(location.hash.slice(1));
      if (!h) { var pend = PASOS.filter(function (p) { return !t.pasos[p]; })[0]; mostrar(pend || 'soporte', false, false, true); return; }
      if (ids.indexOf(h) >= 0) { mostrar(h, false); return; }
      var dest = document.getElementById(h); var p = dest && dest.closest('.panel');
      if (p) { mostrar(p.id, false); history.replaceState(null, '', '#' + h); setTimeout(function () { dest.scrollIntoView({ block: 'start' }); }, 30); }
      else mostrar(ids[0], false);
    }
    $$('a[data-paso], a[data-ir]').forEach(function (a) {
      a.addEventListener('click', function (e) { var id = a.dataset.ir || a.dataset.paso; if (ids.indexOf(id) < 0) return; e.preventDefault(); mostrar(id, true, true); });
    });
    $$('.btn-hecho').forEach(function (b) {
      var p = b.dataset.paso;
      function pintar() { var si = !!t.pasos[p]; b.setAttribute('aria-pressed', si ? 'true' : 'false'); b.textContent = si ? 'Paso terminado' : 'Marcar este paso como terminado'; }
      b.addEventListener('click', function () { t.pasos[p] = !t.pasos[p]; if (!t.pasos[p]) delete t.pasos[p]; guardar(); pintar(); pintarRail($('.panel.on').id); });
      pintar();
    });
    window.addEventListener('hashchange', desdeHash);
    desdeHash();
  }

  function paginaTema() {
    var num = PAGE.num, bloque = PAGE.bloque;
    plegarSoluciones();
    herramientasCodigo();
    huecos(num);
    selectorRuta(bloque, function () { filtrarTareas(bloque); });
    tareas(num, bloque);
    recall(num);
    comprension(num);
    autorregistro(num);
    notas(num);
    paneles(num);
    var s = cargar(); s.ultimo = num; guardar();
  }

  /* ------------------------------------------------------------ mapa de ruta (portada) */
  function partir(txt, max) {
    var w = txt.split(' '), l = [], cur = '';
    w.forEach(function (p) { if ((cur + ' ' + p).trim().length > max && cur) { l.push(cur); cur = p; } else cur = (cur + ' ' + p).trim(); });
    if (cur) l.push(cur); return l.slice(0, 2);
  }
  function svgEsc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
  function estiloVia(r, via) {
    if (!r) return 'stroke:var(--r' + via.toLowerCase() + ');opacity:.55;stroke-width:5';
    return r === via ? 'stroke:var(--r' + via.toLowerCase() + ');stroke-width:7' : 'stroke:var(--station);opacity:.4;stroke-width:4';
  }
  function estacion(t, x, y, w, h) {
    var e = estadoTema(t.num);
    var fill = e === 'hecho' ? 'var(--ink)' : 'var(--surface)';
    var stroke = e === 'nada' ? 'var(--station)' : 'var(--ink)';
    var txt = e === 'hecho' ? 'var(--surface)' : (e === 'nada' ? 'var(--ink-2)' : 'var(--ink)');
    var est = e === 'hecho' ? 'terminado' : (e === 'curso' ? 'en curso' : 'sin empezar');
    return '<a href="tema-' + t.num + '.html" aria-label="Tema ' + t.num + ': ' + svgEsc(t.corto) + ' (' + est + ')">' +
      '<rect class="m-est" x="' + (x - w / 2) + '" y="' + (y - h / 2) + '" width="' + w + '" height="' + h + '" rx="' + Math.min(w, h) / 2 + '" style="fill:' + fill + ';stroke:' + stroke + ';stroke-width:3"/>' +
      '<text x="' + x + '" y="' + (y + 5) + '" text-anchor="middle" style="font-weight:800;font-size:14px;fill:' + txt + '">' + t.num + '</text>';
  }
  function diamante(b, x, y, lx, anchor) {
    var d = cargar().diag[b];
    var hecho = !!d;
    return '<a class="m-diag" href="diagnostico.html#bloque-' + b + '" aria-label="Diagnóstico del bloque ' + b + (hecho ? ' (respondido: ' + d.aciertos + ' de ' + d.total + ')' : '') + '">' +
      '<rect x="' + (x - 8) + '" y="' + (y - 8) + '" width="16" height="16" rx="2" transform="rotate(45 ' + x + ' ' + y + ')" style="fill:' + (hecho ? 'var(--ink)' : 'var(--surface)') + ';stroke:var(--ink);stroke-width:2.5"/>' +
      '<text x="' + lx + '" y="' + (y + 4) + '" text-anchor="' + anchor + '">' + (hecho ? 'Diagnóstico ' + b + ': ' + d.aciertos + '/' + d.total : 'Diagnóstico ' + b) + '</text></a>';
  }
  function rotuloRuta(b) { var r = rutaDe(b); return r ? '<tspan class="m-ruta" style="fill:var(--r' + r.toLowerCase() + ')">  Ruta ' + r + '</tspan>' : '<tspan class="m-ruta" style="fill:var(--ink-2)">  ruta por elegir</tspan>'; }
  function mapaSerpiente() {
    var W = 1000, xL = 140, xR = 860, R = 72, G = 2 * R, y0 = 92, d = 7, SW = 32, SH = 48;
    var vias = '', est = '', etiq = '';
    C.bloques.forEach(function (b, r) {
      var y = y0 + r * G, dir = r % 2 === 0 ? 1 : -1;
      var ts = b.temas.map(infoTema); var k = ts.length;
      var ruta = rutaDe(b.id);
      ['A', 'B'].forEach(function (via) {
        var sA = r % 2 === 0 ? -1 : 1; var o = d * (via === 'A' ? sA : -sA); var o2 = -o;
        var x0 = r === 0 ? 44 : (dir > 0 ? xL : xR);
        var x1 = dir > 0 ? xR : xL;
        var path = 'M' + x0 + ' ' + (y + o) + ' H' + x1;
        if (r < C.bloques.length - 1) { var rad = (G + o2 - o) / 2; path += ' A' + rad + ' ' + rad + ' 0 0 ' + (dir > 0 ? 1 : 0) + ' ' + x1 + ' ' + (y + G + o2); }
        else path += ' H' + (dir > 0 ? xR + 70 : xL - 70);
        vias += '<path d="' + path + '" fill="none" stroke-linecap="round" style="' + estiloVia(ruta, via) + '"/>';
      });
      ts.forEach(function (t, i) {
        var x = dir > 0 ? xL + i * (xR - xL) / (k - 1) : xR - i * (xR - xL) / (k - 1);
        est += estacion(t, x, y, SW, SH);
        var lineas = partir(t.corto, 16);
        est += '<text class="m-lbl" text-anchor="middle" x="' + x + '" y="' + (y + SH / 2 + 18) + '">' + lineas.map(function (l, j) { return '<tspan x="' + x + '" dy="' + (j ? 16 : 0) + '">' + svgEsc(l) + '</tspan>'; }).join('') + '</text></a>';
      });
      var lx = r === 0 ? 44 : (dir > 0 ? xL - 20 : xR + 20);
      etiq += '<text class="m-blq" x="' + lx + '" y="' + (y - 40) + '" text-anchor="' + (dir > 0 ? 'start' : 'end') + '">Bloque ' + b.id + ': ' + svgEsc(b.nombre) + rotuloRuta(b.id) + '</text>';
      if (r === 0) etiq += diamante(b.id, 76, y, 76, 'middle').replace('y="' + (y + 4) + '" text-anchor="middle"', 'y="' + (y - 18) + '" text-anchor="middle"');
      else { var prevDir = (r - 1) % 2 === 0 ? 1 : -1; var dx = prevDir > 0 ? xR + R : xL - R; var dy = y - R; etiq += diamante(b.id, dx, dy, prevDir > 0 ? dx - 18 : dx + 18, prevDir > 0 ? 'end' : 'start'); }
    });
    var H = y0 + (C.bloques.length - 1) * G + 80;
    return '<svg viewBox="0 0 ' + W + ' ' + H + '" role="group" aria-label="Mapa de ruta del curso: 17 temas en 4 bloques, con las rutas A y B">' + vias + etiq + est + '</svg>';
  }
  function mapaVertical() {
    var W = 360, x = 40, d = 6, y = 18, vias = '', cont = '';
    C.bloques.forEach(function (b) {
      var ruta = rutaDe(b.id);
      cont += '<text class="m-blq" x="12" y="' + (y + 16) + '">Bloque ' + b.id + ': ' + svgEsc(b.nombre) + '</text>';
      cont += '<text x="12" y="' + (y + 34) + '">' + rotuloRuta(b.id).replace('  ', '') + '</text>';
      y += 52; var yIni = y;
      cont += diamante(b.id, x, y + 8, x + 28, 'start'); y += 38;
      b.temas.map(infoTema).forEach(function (t) {
        cont += estacion(t, x, y + 20, 44, 30) + '<text class="m-lbl" x="' + (x + 34) + '" y="' + (y + 25) + '" style="font-size:15px">' + svgEsc(t.corto) + '</text></a>';
        y += 56;
      });
      ['A', 'B'].forEach(function (via) { var xx = via === 'A' ? x - d : x + d; vias += '<line x1="' + xx + '" y1="' + (yIni - 6) + '" x2="' + xx + '" y2="' + (y + 6) + '" stroke-linecap="round" style="' + estiloVia(ruta, via) + '"/>'; });
      y += 18;
    });
    return '<svg viewBox="0 0 ' + W + ' ' + y + '" role="group" aria-label="Mapa de ruta del curso">' + vias + cont + '</svg>';
  }
  function dibujarMapa() {
    var m = $('#mapa'); if (!m) return;
    var vertical = m.clientWidth < 680;
    m.innerHTML = vertical ? mapaVertical() : mapaSerpiente();
    m.dataset.modo = vertical ? 'v' : 'h';
  }
  function paginaInicio() {
    dibujarMapa();
    var modo = null; window.addEventListener('resize', function () { var m = $('#mapa'); var v = m.clientWidth < 680 ? 'v' : 'h'; if (v !== m.dataset.modo) dibujarMapa(); });
    $$('.fila-tema').forEach(function (f) {
      var num = f.dataset.num; var p = pasosHechos(num); var e = estadoTema(num);
      $('.ft-prog i', f).style.width = (p / 5 * 100) + '%';
      $('.ft-estado', f).textContent = e === 'hecho' ? 'Terminado' : (e === 'curso' ? p + ' de 5 pasos' : '');
      f.classList.toggle('hecho', e === 'hecho');
    });
    $$('.bloque-ruta').forEach(function (p) {
      var b = p.dataset.bloque; var r = rutaDe(b); var d = cargar().diag[b];
      p.innerHTML = (r ? 'Tu ruta: <span class="ruta r' + r.toLowerCase() + '">Ruta ' + r + '</span>' : 'Ruta por elegir') +
        (d ? '. Diagnóstico: ' + d.aciertos + ' de ' + d.total + '.' : '. <a href="diagnostico.html#bloque-' + b + '">Hacer el diagnóstico</a>');
    });
    var s = cargar(); var hayAlgo = C.temas.some(function (t) { return estadoTema(t.num) !== 'nada'; });
    if (hayAlgo) {
      var sig = C.temas.filter(function (t) { return estadoTema(t.num) !== 'hecho'; })[0];
      var acc = $('#acciones-inicio');
      if (acc) acc.innerHTML = sig ? '<a class="btn btn-primario" href="tema-' + sig.num + '.html">Continuar con el Tema ' + sig.num + ': ' + sig.corto + '</a><a class="btn" href="progreso.html">Ver mi progreso</a>'
        : '<a class="btn btn-primario" href="progreso.html">Terminaste los 17 temas: revisa tu progreso</a>';
    } else if (Object.keys(s.diag).length) {
      var acc2 = $('#acciones-inicio'); if (acc2) acc2.innerHTML = '<a class="btn btn-primario" href="tema-01.html">Empezar por el Tema 01</a><a class="btn" href="diagnostico.html">Ver el diagnóstico</a>';
    }
  }

  /* ------------------------------------------------------------ diagnóstico */
  function paginaDiagnostico() {
    var s = cargar();
    function pintarTabs() {
      $$('.diag-tab').forEach(function (a) {
        var b = a.dataset.bloque; var d = s.diag[b]; a.classList.toggle('hecho', !!d);
        var sm = $('small', a); var base = sm.dataset.base || sm.textContent; sm.dataset.base = base;
        sm.textContent = d ? base + ': ' + d.aciertos + ' de ' + d.total : base;
      });
      $$('.diag-estado').forEach(function (p) {
        var b = p.dataset.bloque; var d = s.diag[b]; var r = s.ruta[b];
        p.textContent = d ? 'Lo respondiste el ' + d.fecha + ': ' + d.aciertos + ' de ' + d.total + '.' + (r ? ' Ruta elegida: ' + r + '.' : '') : '';
      });
    }
    $$('.diag-form').forEach(function (f) {
      var b = f.dataset.bloque; var items = $$('.reactivo', f); var res = $('.diag-res', f);
      function calificar(guardarRes) {
        var faltan = items.filter(function (it) { return !$('input:checked', it); });
        items.forEach(function (it) { it.classList.remove('sin'); });
        if (faltan.length) {
          faltan.forEach(function (it) { it.classList.add('sin'); });
          res.innerHTML = '<div class="dr"><p class="dr-aviso">Te ' + (faltan.length === 1 ? 'falta 1 reactivo' : 'faltan ' + faltan.length + ' reactivos') + '. Responde todos antes de calificar.</p></div>';
          var r0 = $('input', faltan[0]); if (r0) r0.focus(); return;
        }
        var ok = 0, resp = [];
        items.forEach(function (it) {
          var sel = $('input:checked', it); var v = +sel.value; var bien = v === +it.dataset.ok; resp.push(v);
          if (bien) ok++;
          it.classList.toggle('ok', bien); it.classList.toggle('mal', !bien);
          $$('label', it).forEach(function (l, j) { l.classList.toggle('correcta', j === +it.dataset.ok); l.classList.toggle('elegida-mal', j === v && !bien); });
          $('.r-exp', it).hidden = false;
        });
        var tot = items.length, sug = ok / tot >= 0.7 ? 'B' : 'A';
        if (guardarRes) { s.diag[b] = { aciertos: ok, total: tot, fecha: hoy(), resp: resp }; guardar(); }
        res.innerHTML = '<div class="dr"><p><span class="dr-num">' + ok + ' de ' + tot + '</span> (' + Math.round(ok / tot * 100) + ' %)</p>' +
          '<p>' + (sug === 'B' ? 'Ya dominas buena parte del bloque ' + b + '. Te sugerimos la <b>Ruta B</b>: tareas de autoexplicación, imaginación, solución libre y retos.' :
            'Te conviene la <b>Ruta A</b> en el bloque ' + b + ': ejemplos resueltos y problemas por completar antes de los problemas abiertos.') + '</p>' +
          '<div class="acciones"><button class="btn btn-primario" type="button" data-usar="' + sug + '">Usar la Ruta ' + sug + ' en el bloque ' + b + '</button>' +
          '<button class="btn" type="button" data-usar="' + (sug === 'A' ? 'B' : 'A') + '">Prefiero la Ruta ' + (sug === 'A' ? 'B' : 'A') + '</button></div><p class="dr-ok" role="status"></p></div>';
        $$('[data-usar]', res).forEach(function (bt) {
          bt.addEventListener('click', function () {
            s.ruta[b] = bt.dataset.usar; guardar(); pintarTabs();
            var pr = C.bloques.filter(function (x) { return x.id === b; })[0].temas[0];
            $('.dr-ok', res).innerHTML = 'Listo: Ruta ' + bt.dataset.usar + ' en el bloque ' + b + '. <a href="tema-' + pr + '.html">Ir al Tema ' + pr + '</a>.';
          });
        });
        pintarTabs();
      }
      f.addEventListener('submit', function (e) { e.preventDefault(); calificar(true); });
      f.addEventListener('reset', function () {
        items.forEach(function (it) { it.classList.remove('ok', 'mal', 'sin'); $('.r-exp', it).hidden = true; $$('label', it).forEach(function (l) { l.classList.remove('correcta', 'elegida-mal'); }); });
        res.innerHTML = '';
      });
      var d = s.diag[b];
      if (d && d.resp && d.resp.length === items.length) {
        items.forEach(function (it, i) { var inp = $$('input', it)[d.resp[i]]; if (inp) inp.checked = true; });
        calificar(false);
      }
    });
    pintarTabs();
  }

  /* ------------------------------------------------------------ progreso */
  function grafica(cont) {
    var pts = C.temas.map(function (t) { var r = resumenTema(t.num); return { t: t, r: r }; }).filter(function (p) { return p.r.esf && p.r.rN > 0; });
    var W = 760, H = 380, m = { l: 58, r: 20, t: 18, b: 48 }, iw = W - m.l - m.r, ih = H - m.t - m.b;
    var X = function (e) { return m.l + (e - 1) / 8 * iw; }, Y = function (p) { return m.t + (1 - p) * ih; };
    var g = '';
    for (var e = 1; e <= 9; e++) g += '<line class="g-grid" x1="' + X(e) + '" x2="' + X(e) + '" y1="' + m.t + '" y2="' + (m.t + ih) + '"/><text x="' + X(e) + '" y="' + (m.t + ih + 18) + '" text-anchor="middle">' + e + '</text>';
    [0, 0.25, 0.5, 0.75, 1].forEach(function (p) { g += '<line class="g-grid" x1="' + m.l + '" x2="' + (m.l + iw) + '" y1="' + Y(p) + '" y2="' + Y(p) + '"/><text x="' + (m.l - 8) + '" y="' + (Y(p) + 4) + '" text-anchor="end">' + Math.round(p * 100) + ' %</text>'; });
    g += '<line class="g-ref" x1="' + X(5) + '" x2="' + X(5) + '" y1="' + m.t + '" y2="' + (m.t + ih) + '"/><line class="g-ref" x1="' + m.l + '" x2="' + (m.l + iw) + '" y1="' + Y(0.7) + '" y2="' + Y(0.7) + '"/>';
    g += '<text x="' + (m.l + iw / 2) + '" y="' + (H - 6) + '" text-anchor="middle">Esfuerzo mental registrado (1 = muy bajo, 9 = muy alto)</text>';
    g += '<text transform="translate(14 ' + (m.t + ih / 2) + ') rotate(-90)" text-anchor="middle">Recall test (respuestas correctas)</text>';
    if (!pts.length) g += '<text class="g-vacio" x="' + (m.l + iw / 2) + '" y="' + (m.t + ih / 2) + '" text-anchor="middle">Aparecerá un punto por tema cuando respondas su recall test y registres tu esfuerzo.</text>';
    pts.forEach(function (p) {
      var pr = p.r.rOk / 10; var cx = X(p.r.esf), cy = Y(pr);
      g += '<g><circle class="g-punto" tabindex="0" cx="' + cx + '" cy="' + cy + '" r="9" data-tip="Tema ' + p.t.num + ' (' + svgEsc(p.t.corto) + '): recall ' + p.r.rOk + '/10, esfuerzo ' + p.r.esf + '" aria-label="Tema ' + p.t.num + ': recall ' + p.r.rOk + ' de 10, esfuerzo ' + p.r.esf + '"/>' +
        '<text class="g-lbl" x="' + (cx + 13) + '" y="' + (cy + 4) + '">' + p.t.num + '</text></g>';
    });
    cont.innerHTML = '<svg viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="Gráfica de desempeño contra esfuerzo mental por tema">' + g + '</svg>';
    var tip = el('div', { class: 'g-tip', hidden: '' }); cont.appendChild(tip);
    $$('.g-punto', cont).forEach(function (c) {
      function on() { var bb = c.getBoundingClientRect(), cb = cont.getBoundingClientRect(); tip.textContent = c.dataset.tip; tip.style.left = (bb.left + bb.width / 2 - cb.left) + 'px'; tip.style.top = (bb.top - cb.top) + 'px'; tip.hidden = false; }
      function off() { tip.hidden = true; }
      c.addEventListener('mouseenter', on); c.addEventListener('focus', on); c.addEventListener('mouseleave', off); c.addEventListener('blur', off);
    });
  }
  function mediaEnc(r, a, b) { var v = r.slice(a, b).filter(function (x) { return x !== null && x !== undefined; }); return v.length ? (v.reduce(function (p, c) { return p + c; }, 0) / v.length) : null; }
  function textoEnc(e) { if (!e) return ''; var f = function (x) { return x === null ? '—' : x.toFixed(1); }; return 'Intrínseca ' + f(mediaEnc(e.r, 0, 3)) + ', extrínseca ' + f(mediaEnc(e.r, 3, 6)) + ', pertinente ' + f(mediaEnc(e.r, 6, 10)); }
  function csv() {
    var s = cargar();
    var filas = [['tema', 'titulo', 'bloque', 'ruta', 'pasos_terminados', 'tareas_hechas', 'tareas_total', 'huecos_correctos', 'huecos_comprobados', 'recall_correctas', 'recall_respondidas', 'comprension_bien', 'comprension_evaluada', 'esfuerzo_mental']];
    C.temas.forEach(function (t) { var r = resumenTema(t.num); filas.push([t.num, t.corto, t.bloque, s.ruta[t.bloque] || '', r.pasos, r.tareas, r.tareasTot, r.hOk, r.hTot, r.rOk, r.rN, r.cOk, r.cN, r.esf || '']); });
    filas.push([]);
    filas.push(['bloque', 'diagnostico_aciertos', 'diagnostico_total', 'carga_intrinseca', 'carga_extrinseca', 'carga_pertinente']);
    C.bloques.forEach(function (b) { var d = s.diag[b.id] || {}; var e = s.encuesta[b.id]; var m = function (a, z) { var x = e ? mediaEnc(e.r, a, z) : null; return x === null ? '' : x.toFixed(2); }; filas.push([b.id, d.aciertos !== undefined ? d.aciertos : '', d.total || '', m(0, 3), m(3, 6), m(6, 10)]); });
    return '﻿' + filas.map(function (f) { return f.map(function (c) { c = String(c); return /[",\n]/.test(c) ? '"' + c.replace(/"/g, '""') + '"' : c; }).join(','); }).join('\r\n');
  }
  function paginaProgreso() {
    var s = cargar();
    var res = C.temas.map(function (t) { return { t: t, r: resumenTema(t.num) }; });
    var terminados = res.filter(function (x) { return x.r.pasos === 5; }).length;
    var pasos = res.reduce(function (a, x) { return a + x.r.pasos; }, 0);
    var tareasH = res.reduce(function (a, x) { return a + x.r.tareas; }, 0), tareasT = res.reduce(function (a, x) { return a + x.r.tareasTot; }, 0);
    var rOk = res.reduce(function (a, x) { return a + x.r.rOk; }, 0), rN = res.reduce(function (a, x) { return a + x.r.rN; }, 0);
    var rs = $('#prog-resumen');
    if (rs) rs.innerHTML = '<div class="pr-dato"><b>' + terminados + ' de 17</b><span>temas terminados (' + pasos + ' de 85 pasos)</span></div>' +
      '<div class="pr-dato"><b>' + tareasH + ' de ' + tareasT + '</b><span>tareas marcadas como hechas</span></div>' +
      '<div class="pr-dato"><b>' + (rN ? Math.round(rOk / rN * 100) + ' %' : 'Sin datos') + '</b><span>aciertos en los recall tests (' + rN + ' preguntas respondidas)</span></div>' +
      '<div class="pr-dato"><b>' + Object.keys(s.diag).length + ' de 4</b><span>diagnósticos de bloque respondidos</span></div>';
    var tb = $('#prog-tabla tbody');
    if (tb) tb.innerHTML = res.map(function (x) {
      var t = x.t, r = x.r, ru = s.ruta[t.bloque];
      var dots = PASOS.map(function (p) { var tt = s.temas[t.num]; return '<i class="' + ((tt && tt.pasos && tt.pasos[p]) ? 'si' : '') + '" style="--c:var(--' + { soporte: 'sop', procedimental: 'pro', tareas: 'tar', protocolo: 'pv', evaluacion: 'ev' }[p] + ')" title="' + NOMBRE_PASO[p] + '"></i>'; }).join('');
      return '<tr><td class="pt-t"><a href="tema-' + t.num + '.html">' + t.num + '. ' + t.corto + '</a></td><td>' + (ru ? '<span class="ruta r' + ru.toLowerCase() + '">' + ru + '</span>' : '—') + '</td>' +
        '<td><span class="pasos5" aria-label="' + r.pasos + ' de 5 pasos">' + dots + '</span></td><td>' + r.tareas + ' / ' + r.tareasTot + '</td><td>' + (r.hTot ? r.hOk + ' / ' + r.hTot : '—') + '</td>' +
        '<td>' + (r.rN ? r.rOk + ' / 10' + (r.rN < 10 ? ' <small>(' + r.rN + ' resp.)</small>' : '') : '—') + '</td><td>' + (r.cN ? r.cOk + ' / 4' : '—') + '</td><td>' + (r.esf || '—') + '</td></tr>';
    }).join('');
    var g = $('#grafica'); if (g) grafica(g);
    $$('.enc-form').forEach(function (f) {
      var b = f.dataset.bloque; var e = s.encuesta[b]; var out = $('.enc-res[data-bloque="' + b + '"]');
      if (e) { e.r.forEach(function (v, i) { if (v === null) return; var inp = $('input[name="e' + b + '-' + (i + 1) + '"][value="' + v + '"]', f); if (inp) inp.checked = true; }); out.textContent = textoEnc(e); }
      f.addEventListener('submit', function (ev) {
        ev.preventDefault();
        var r = []; for (var i = 1; i <= 10; i++) { var c = $('input[name="e' + b + '-' + i + '"]:checked', f); r.push(c ? +c.value : null); }
        s.encuesta[b] = { r: r, fecha: hoy() }; guardar(); out.textContent = textoEnc(s.encuesta[b]);
        var falt = r.filter(function (x) { return x === null; }).length;
        $('.enc-ok', f).textContent = 'Guardado.' + (falt ? ' Quedaron ' + falt + ' enunciados sin responder.' : '');
      });
    });
    var msg = $('.datos-msg');
    var bj = $('#exp-json'); if (bj) bj.addEventListener('click', function () { var o = JSON.parse(JSON.stringify(s)); o.exportado = new Date().toISOString(); o.curso = 'Programación básica en C (CLT4BP)'; descargar('progreso-c-clt4bp-' + hoy() + '.json', JSON.stringify(o, null, 2), 'application/json'); });
    var bc = $('#exp-csv'); if (bc) bc.addEventListener('click', function () { descargar('resumen-c-clt4bp-' + hoy() + '.csv', csv(), 'text/csv;charset=utf-8'); });
    var bi = $('#imp-json'); if (bi) bi.addEventListener('change', function () {
      var f = bi.files[0]; if (!f) return; var rd = new FileReader();
      rd.onload = function () {
        try { var o = JSON.parse(rd.result); if (!o || typeof o !== 'object' || !o.temas) throw new Error('formato');
          if (!confirm('Esto reemplaza el progreso guardado en este navegador por el del archivo. ¿Continuar?')) return;
          delete o.exportado; estado = o; guardarYa(); location.reload();
        } catch (e) { msg.textContent = 'El archivo no es un progreso válido de este curso.'; }
      };
      rd.readAsText(f);
    });
    var bb = $('#borrar'); if (bb) bb.addEventListener('click', function () {
      if (!confirm('Se borrará todo tu progreso de este navegador (pasos, tareas, respuestas, diagnósticos y encuestas). No se puede deshacer. ¿Borrar?')) return;
      try { localStorage.removeItem(KEY); } catch (e) { } estado = null; location.reload();
    });
  }

  /* ------------------------------------------------------------ glosario */
  function paginaGlosario() {
    var q = $('#g-q'), sel = $('#g-tema'), n = $('#g-n'); var filas = $$('.glos-todo tbody tr');
    function filtrar() {
      var t = (q.value || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').trim(); var tm = sel.value; var k = 0;
      filas.forEach(function (f) {
        var txt = f.dataset.q.normalize('NFD').replace(/[̀-ͯ]/g, '');
        var ok = (!t || txt.indexOf(t) >= 0) && (!tm || (' ' + f.dataset.temas + ' ').indexOf(' ' + tm + ' ') >= 0);
        f.hidden = !ok; if (ok) k++;
      });
      n.textContent = k === filas.length ? '' : k + (k === 1 ? ' término' : ' términos');
    }
    q.addEventListener('input', filtrar); sel.addEventListener('change', filtrar);
    var h = new URLSearchParams(location.search).get('q'); if (h) { q.value = h; filtrar(); }
  }

  /* ------------------------------------------------------------ arranque */
  cabecera();
  if (PAGE.tipo === 'tema') paginaTema();
  else if (PAGE.tipo === 'inicio') paginaInicio();
  else if (PAGE.tipo === 'diagnostico') paginaDiagnostico();
  else if (PAGE.tipo === 'progreso') paginaProgreso();
  else if (PAGE.tipo === 'glosario') paginaGlosario();
  else if (PAGE.tipo === 'guia') { plegarSoluciones(); herramientasCodigo(); }
})();
