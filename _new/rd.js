  function tag(k) { return '<span class="tagx tagx--' + k + '">' + esc(t('tag.' + k)) + '</span>'; }
  function dfmt(s, long) { if (!s) return '—'; var p = s.split('-'), d = new Date(+p[0], +p[1] - 1, +p[2]); return d.toLocaleDateString(document.documentElement.lang, long ? { day: 'numeric', month: 'short', year: 'numeric' } : { day: 'numeric', month: 'short' }); }
  function obs(r) { var o = []; (r.weeks || []).forEach(function (v, i) { if (r.wkn[i] > 0) o.push(v); }); return o; }
  function icoCls(k) { return k === 'ok' ? '' : k === 'check' ? 'ico--amber' : 'ico--red'; }
  function chart(r) {
    var W = 520, H = 190, P = { l: 34, r: 10, t: 16, b: 30 }, n = r.weeks.length;
    var lo = r.low / 4, hi = r.high / 4, mx = Math.max.apply(null, r.weeks.concat([hi, 1])) * 1.2;
    var cw = (W - P.l - P.r) / n, y = function (v) { return P.t + (H - P.t - P.b) * (1 - v / mx); };
    var s = '<svg class="evchart" viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="' + esc(t('x.ev.h')) + '">';
    [0, mx / 2, mx].forEach(function (v) { s += '<line x1="' + P.l + '" x2="' + (W - P.r) + '" y1="' + y(v) + '" y2="' + y(v) + '" class="evchart__grid"/><text x="' + (P.l - 6) + '" y="' + (y(v) + 4) + '" text-anchor="end" class="evchart__ax">' + Math.round(v) + '</text>'; });
    s += '<rect x="' + P.l + '" y="' + y(hi) + '" width="' + (W - P.l - P.r) + '" height="' + Math.max(2, y(lo) - y(hi)) + '" class="evchart__band"/>';
    r.weeks.forEach(function (v, i) {
      var x = P.l + i * cw + cw * 0.2, w = cw * 0.6, miss = !(r.wkn[i] > 0);
      if (miss) s += '<rect x="' + x + '" y="' + (y(0) - 18) + '" width="' + w + '" height="18" rx="3" class="evchart__miss"/>';
      else s += '<rect x="' + x + '" y="' + y(v) + '" width="' + w + '" height="' + Math.max(1.5, y(0) - y(v)) + '" rx="3" class="evchart__bar"/><text x="' + (x + w / 2) + '" y="' + (y(v) - 4) + '" text-anchor="middle" class="evchart__val">' + Math.round(v) + '</text>';
      s += '<text x="' + (x + w / 2) + '" y="' + (H - 10) + '" text-anchor="middle" class="evchart__ax">' + esc(dfmt(WS[i])) + '</text>';
    });
    return s + '</svg>';
  }
  function slider(id, key, val, max) {
    var lab = t(key === 'plan' ? 'x.po' : 'x.inc');
    return '<div class="qf"><div class="qf__top"><label for="' + id + '">' + esc(lab) + '</label>' + tag('you') + '</div>' +
      '<input type="range" class="qf__range" min="0" max="' + max + '" step="1" value="' + (val || 0) + '" data-q="' + key + '" aria-label="' + esc(lab) + '">' +
      '<div class="qf__row"><input id="' + id + '" type="number" min="0" step="1" inputmode="numeric" data-q="' + key + '" value="' + (val == null ? '' : val) + '" placeholder="0" aria-label="' + esc(t(key === 'plan' ? 'x.po.ex' : 'x.inc.ex')) + '"><span>' + esc(t('s4.units')) + '</span><button type="button" class="btn btn--small btn--ghost" data-clear="' + key + '">' + esc(t('x.clear')) + '</button></div></div>';
  }
  function verdictHTML(r) {
    var k = kind(r), s = sugg(r), mid = Math.round((r.low + r.high) / 2);
    return '<div class="verdict verdict--' + k + '"><div class="verdict__h"><span class="ico ' + icoCls(k) + '">' + (k === 'ok' ? '✓' : '!') + '</span><b>' + esc(t('v.' + k)) + '</b></div>' +
      '<div class="verdict__est"><small>' + esc(t('x.est')) + '</small>' + tag('sl') + '</div><div class="verdict__num"><b class="num">' + s + '</b> ' + esc(t('s4.units')) + '</div>' +
      '<p>' + esc(t('x.est.t')) + '</p><p class="verdict__f">' + esc(t('x.formula')) + '<br><span class="num">' + mid + ' − ' + r.stock + ' − ' + r.inc + ' = ' + s + '</span></p>' +
      (r.plan !== s ? '<button type="button" class="btn btn--small btn--primary" data-use="' + s + '">' + esc(fmt(t('d.use'), { n: s })) + '</button>' : '') + '</div>';
  }
  function pcheckHTML(r) {
    var k = kind(r), o = r.plan || 0, tot = avail(r), max = Math.max(r.high * 1.3, tot * 1.08, 4);
    var pc = function (v) { return (100 * v / max).toFixed(2) + '%'; };
    var h = '<p class="pcheck__eq num">' + esc(fmt(t('x.eq'), { s: r.stock, i: r.inc, o: o, t: tot })) + '</p>';
    h += '<div class="pbar" aria-hidden="true"><div class="pbar__track"><span class="pbar__seg pbar__seg--s" style="width:' + pc(r.stock) + '"></span><span class="pbar__seg pbar__seg--i" style="width:' + pc(r.inc) + '"></span><span class="pbar__seg pbar__seg--o" style="width:' + pc(o) + '"></span></div>' +
      '<span class="pbar__band" style="left:' + pc(r.low) + ';width:' + pc(r.high - r.low) + '"></span><span class="pbar__tick" style="left:' + pc(r.low) + '">' + r.low + '</span><span class="pbar__tick" style="left:' + pc(r.high) + '">' + r.high + '</span></div>';
    h += '<ul class="lgd"><li><i class="sw sw--s"></i>' + esc(t('x.lg.s')) + '</li><li><i class="sw sw--i"></i>' + esc(t('x.lg.i')) + '</li><li><i class="sw sw--o"></i>' + esc(t('x.lg.o')) + '</li><li><i class="sw sw--e"></i>' + esc(t('x.lg.e')) + ' ' + r.low + '–' + r.high + '</li></ul>';
    h += '<div class="msg msg--' + k + '"><span class="ico ' + icoCls(k) + '">' + (k === 'ok' ? '✓' : '!') + '</span><div><b>' + esc(t('x.t.' + k)) + '</b>' + esc(fmt(t('d.m.' + k), { a: tot, h: r.high, l: r.low, s: sugg(r) })) + '</div></div>';
    return h;
  }
  function renderDetail() {
    var L = list(), r = ROWS.filter(function (x) { return x.code === sel; })[0];
    if (!r) { det.innerHTML = ''; return; }
    var idx = L.indexOf(r), h = '';
    h += '<div class="det__bar"><span>' + (idx > -1 ? esc(fmt(t('x.product'), { i: idx + 1, n: L.length })) : '') + '</span><div class="det__nav"><button type="button" data-nav="-1" aria-label="' + esc(t('d.prev')) + '">‹</button><button type="button" data-nav="1" aria-label="' + esc(t('d.next')) + '">›</button></div></div>';
    var sp = { ready: 'pill--ok', review: 'pill--review', missing: 'pill--missing' }[r.status] || 'pill--muted';
    h += '<div class="det__head"><div><small class="det__eyebrow">' + esc(fmt(t('x.eyebrow'), { c: r.code })) + '</small><h2>' + esc(r.name) + '</h2><small class="num">' + esc(r.pack) + '</small>' +
      '<p class="det__meta">' + (r.stock == null ? '' : '<b class="num">' + r.stock + '</b> ' + esc(t('s4.units')) + ' · ') + (r.scd ? esc(fmt(t('x.counted'), { d: dfmt(r.scd) })) + (r.age != null ? ' · ' + esc(fmt(t('x.daysold'), { n: r.age })) : '') + ' ' : '') + tag('file') + '</p></div>' +
      '<span class="pill ' + sp + '">' + esc(t('st3.' + r.status)) + '</span></div>';
    if (r.need) {
      h += '<div class="msg msg--need"><span class="ico">✕</span><div><b>' + esc(t('d.m.need.h')) + '</b>' + esc(t('w.' + r.why)) + '</div></div>';
      h += '<a class="btn btn--ghost" href="StockLess-Step3-Readiness.html">' + esc(t('d.fix')) + '</a>';
      det.innerHTML = h; wire(r); return;
    }
    var mx = Math.max(50, r.high * 2);
    h += '<div class="js-verdict">' + verdictHTML(r) + '</div>';
    h += '<section class="det__sec"><small class="det__k">' + esc(t('x.yp')) + '</small><h3>' + esc(t('x.yp.h')) + '</h3><p class="det__t">' + esc(t('x.yp.t')) + '</p>' +
      slider('plan-in', 'plan', r.plan, mx) + slider('inc-in', 'inc', r.inc, mx) + '<p class="det__hint">' + esc(t('x.slide')) + ' ' + esc(t('x.zero')) + '</p><p class="det__hint">' + esc(t('x.mark')) + '</p></section>';
    h += '<section class="det__sec pcheck"><h3>' + esc(t('x.pc')) + '</h3><div class="js-pcheck">' + pcheckHTML(r) + '</div>' +
      '<details class="why"><summary>' + esc(t('x.why')) + '</summary><p>' + esc(fmt(t('x.why.t'), { l: r.low, h: r.high })) + '</p></details></section>';
    var ex;
    if (!r.expraw) ex = t('x.exp.none');
    else { var p = r.expraw.split('-'), dd = Math.round((new Date(+p[0], +p[1] - 1, +p[2]) - AD) / 864e5); ex = fmt(t(dd <= 28 ? 'x.exp.soon' : 'x.exp.ok'), { d: dfmt(r.expraw, 1), n: dd }); }
    h += '<section class="det__sec"><h3>' + esc(t('x.exp')) + '</h3><p class="det__exp">⌛ ' + esc(ex) + ' ' + (r.expraw ? tag('file') : '') + '</p><p class="det__hint">' + esc(t('x.exp.note')) + '</p></section>';
    var o = obs(r), avg = o.length ? o.reduce(function (a, b) { return a + b; }, 0) / o.length : 0, steady = o.length >= 6 && o.every(function (v) { return v > 0; });
    var cover = avg > 0 ? (r.stock / avg).toFixed(1) : null;
    var last = WS[WS.length - 1].split('-'), endD = new Date(+last[0], +last[1] - 1, +last[2] + 6);
    var endS = endD.getFullYear() + '-' + String(endD.getMonth() + 1).padStart(2, '0') + '-' + String(endD.getDate()).padStart(2, '0');
    h += '<details class="det__sec ev"><summary>' + esc(t('x.ev')) + '</summary><div class="evcard"><div class="evcard__top"><div><small class="det__k">' + esc(t('x.ev.k')) + '</small><h3>' + esc(t('x.ev.h')) + '</h3><p class="det__t">' + esc(t('x.ev.t')) + '</p></div>' +
      '<span class="pill ' + (steady ? 'pill--ok' : 'pill--muted') + '">' + esc(t(steady ? 'x.steady' : 'x.occ')) + '</span></div>' +
      '<div class="evcard__exp"><small>' + esc(t('x.ev.exp')) + '</small><b class="num">' + r.low + '–' + r.high + '</b><small>' + esc(t('x.ev.total')) + '</small>' + tag('sl') + '</div>' + chart(r) +
      '<ul class="lgd"><li><i class="sw sw--obs"></i>' + esc(t('x.lg.obs')) + '</li><li><i class="sw sw--e"></i>' + esc(t('x.lg.exw')) + ' ' + (r.low / 4).toFixed(1) + '–' + (r.high / 4).toFixed(1) + '</li><li><i class="sw sw--miss"></i>' + esc(t('x.miss')) + '</li></ul>' +
      '<p class="det__hint">' + esc(fmt(t('x.range'), { n: o.length, a: dfmt(WS[0], 1), b: dfmt(endS, 1) })) + '</p>' +
      '<div class="evtiles"><div><small>' + esc(t('x.cs')) + '</small><b class="num">' + r.stock + '</b></div><div><small>' + esc(t('x.scd')) + '</small><b class="num">' + esc(dfmt(r.scd)) + '</b></div>' +
      '<div><small>' + esc(t('x.avg')) + '</small><b class="num">' + avg.toFixed(1) + '</b></div><div><small>' + esc(t('x.cover')) + '</small><b class="num">' + (cover == null ? '—' : esc(fmt(t('x.weeks'), { n: cover }))) + '</b></div></div></div></details>';
    var sq = supplierQty(r);
    h += '<div class="sup"><div class="sup__h">' + esc(t('sup.h')) + '<small>' + esc(fmt(t('sup.from'), { s: r.supplier || '—' })) + '</small></div>' +
      '<div class="sup__grid"><label>' + esc(t('sup.case')) + '<input type="number" min="1" data-sup="case" value="' + (r.case || '') + '"></label>' +
      '<label>' + esc(t('sup.min')) + '<input type="number" min="0" data-sup="min" value="' + (MIN[r.code] || 0) + '"></label>' +
      '<label>' + esc(t('sup.lead')) + '<input type="number" min="0" data-sup="lead" value="' + (r.lead || 0) + '"></label></div>';
    h += sq.q === 0 ? '<p>' + esc(t('sup.zero')) + '</p>' : '<p>' + esc(fmt(t('sup.q'), { q: sq.q, c: sq.k, k: sq.c, d: addDays(r.lead || 0) })) + '</p><button type="button" class="btn btn--small btn--ghost" data-use="' + sq.q + '">' + esc(fmt(t('sup.use'), { q: sq.q })) + '</button>';
    h += '</div><div class="det__foot"><button type="button" class="btn btn--primary" data-done>' + esc(t('x.done')) + '</button></div>';
    det.innerHTML = h; wire(r);
  }
  function live(r) {
    det.querySelector('.js-verdict').innerHTML = verdictHTML(r);
    det.querySelector('.js-pcheck').innerHTML = pcheckHTML(r);
    det.querySelectorAll('.js-verdict [data-use]').forEach(useBtn(r));
    renderKPIs(); renderTable();
  }
  function useBtn(r) { return function (b) { b.addEventListener('click', function () { r.plan = +b.dataset.use; syncQ(r); live(r); }); }; }
  function syncQ(r) {
    det.querySelectorAll('[data-q]').forEach(function (el) { var v = r[el.dataset.q]; if (document.activeElement !== el) el.value = el.type === 'range' ? (v || 0) : (v == null ? '' : v); });
  }
  function wire(r) {
    det.querySelectorAll('[data-nav]').forEach(function (b) {
      b.addEventListener('click', function () { var L2 = list(), i = L2.indexOf(r), n = L2[(i + +b.dataset.nav + L2.length) % L2.length]; if (n) select(n.code); });
    });
    det.querySelectorAll('[data-q]').forEach(function (el) {
      el.addEventListener('input', function () {
        var k = el.dataset.q, v = el.value === '' ? null : Math.max(0, Math.floor(+el.value));
        if (v != null && isNaN(v)) return;
        if (k === 'inc') r.inc = v || 0; else r.plan = v;
        syncQ(r); live(r);
      });
    });
    det.querySelectorAll('[data-clear]').forEach(function (b) { b.addEventListener('click', function () { if (b.dataset.clear === 'inc') r.inc = 0; else r.plan = null; syncQ(r); live(r); }); });
    det.querySelectorAll('.sup [data-use]').forEach(useBtn(r));
    det.querySelectorAll('[data-sup]').forEach(function (inpS) {
      inpS.addEventListener('change', function () {
        var v = Math.max(0, Math.floor(+inpS.value || 0));
        if (inpS.dataset.sup === 'case') r.case = Math.max(1, v); else if (inpS.dataset.sup === 'min') MIN[r.code] = v; else r.lead = v;
        renderDetail();
      });
    });
    var dn = det.querySelector('[data-done]');
    if (dn) dn.addEventListener('click', function () {
      var L2 = list(), i = L2.indexOf(r), n = L2[i + 1];
      if (n) { select(n.code); det.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
      else document.querySelector('.tbl').scrollIntoView({ behavior: 'smooth' });
    });
  }
