  var EV_OPEN = true, EXTRA = -1;
  function dfmt(s, long) { if (!s) return '—'; var p = s.split('-'), d = new Date(+p[0], +p[1] - 1, +p[2]); return d.toLocaleDateString(document.documentElement.lang, long ? { day: 'numeric', month: 'short', year: 'numeric' } : { day: 'numeric', month: 'short' }); }
  function plusDays(n) { var d = new Date(AD); d.setDate(d.getDate() + n); return d.toLocaleDateString(document.documentElement.lang, { day: 'numeric', month: 'short' }); }
  function obs(r) { var o = []; (r.weeks || []).forEach(function (v, i) { if (r.wkn[i] > 0) o.push(v); }); return o; }
  var VPILL = { needed: 'pill--missing', check: 'pill--review', ok: 'pill--ok', need: 'pill--muted' };
  function chartHTML(r) {
    var lo = r.low / 4, hi = r.high / 4, mx = Math.max.apply(null, r.weeks.concat([hi, 1])) * 1.25, H = 118;
    var px = function (v) { return Math.max(3, Math.round(H * v / mx)); };
    var h = '<div class="fc"><div class="fc__plot">';
    r.weeks.forEach(function (v, i) {
      var miss = !(r.wkn[i] > 0);
      h += '<div class="fc__col"><span class="fc__val">' + (miss ? '–' : Math.round(v)) + '</span><span class="fc__bar' + (miss ? ' fc__bar--miss' : '') + '" style="height:' + (miss ? 18 : px(v)) + 'px"></span></div>';
    });
    var bLo = Math.round(H * lo / mx), bHi = Math.round(H * hi / mx), mid = Math.round((bLo + bHi) / 2), wm = Math.round((r.low + r.high) / 8 * 10) / 10;
    h += '<div class="fc__future"><span class="fc__flab">' + esc(t('dz.flab')) + '</span>';
    for (var k = 0; k < 4; k++) h += '<div class="fc__fcol"><span class="fc__bl" style="bottom:' + (bHi + 4) + 'px">≈' + wm + '</span><span class="fc__band" style="bottom:' + bLo + 'px;height:' + Math.max(4, bHi - bLo) + 'px"></span><span class="fc__mid" style="bottom:' + mid + 'px"></span></div>';
    h += '</div></div><div class="fc__labels">';
    r.weeks.forEach(function (v, i) { h += '<span>' + esc(dfmt(WS[i])) + '</span>'; });
    h += '<div class="fc__flabels">' + [0, 7, 14, 21].map(function (n) { return '<span>' + esc(plusDays(n)) + '</span>'; }).join('') + '</div></div>';
    h += '<div class="fc__mlabels"><span>' + esc(t('dz.past')) + '</span><b>' + esc(fmt(t('dz.next'), { n: wm })) + '</b></div>';
    h += '<ul class="lgd"><li><i class="sw sw--obs"></i>' + esc(t('dz.lg.sold')) + '</li><li><i class="sw sw--e"></i>' + esc(t('dz.lg.fc')) + '</li><li><i class="sw sw--miss"></i>' + esc(t('dz.lg.miss')) + '</li></ul></div>';
    return h;
  }
  function verdictText(r) { var k = kind(r); return fmt(t('d.m.' + k), { a: avail(r), h: r.high, l: r.low, s: sugg(r) }); }
  function pcheckHTML(r) {
    var k = kind(r), o = r.plan || 0, tot = avail(r), max = Math.max(r.high * 1.3, tot * 1.08, 4);
    var pc = function (v) { return (100 * v / max).toFixed(2) + '%'; };
    var h = '<div class="pp2-check__head"><h3>' + esc(t('x.pc')) + '</h3><span class="num">' + esc(fmt(t('x.eq'), { s: r.stock, i: r.inc, o: o, t: tot })) + '</span></div>';
    h += '<div class="pbar" aria-hidden="true"><div class="pbar__track"><span class="pbar__seg pbar__seg--s" style="width:' + pc(r.stock) + '"></span><span class="pbar__seg pbar__seg--i" style="width:' + pc(r.inc) + '"></span><span class="pbar__seg pbar__seg--o" style="width:' + pc(o) + '"></span></div>' +
      '<span class="pbar__band" style="left:' + pc(r.low) + ';width:' + pc(r.high - r.low) + '"></span><span class="pbar__tick" style="left:' + pc(r.low) + '">' + r.low + '</span><span class="pbar__tick" style="left:' + pc(r.high) + '">' + r.high + '</span></div>';
    h += '<div class="pp2-verdict pp2-verdict--' + k + '"><b>' + esc(t('x.t.' + k)) + '</b><span>' + esc(verdictText(r)) + '</span></div>';
    return h;
  }
  function suggHTML(r) {
    var s = sugg(r), mid = Math.round((r.low + r.high) / 2);
    return '<span class="pp2-k">' + esc(t('dz.sg')) + '</span><span class="pp2-big">' + s + ' <small>' + esc(t('s4.units')) + '</small></span>' +
      '<span class="pp2-f">' + esc(fmt(t('dz.sgf'), { m: mid, s: r.stock, i: r.inc })) + '</span>' +
      '<button type="button" class="btn btn--primary btn--small" data-use="' + s + '">' + esc(fmt(t('d.use'), { n: s })) + '</button>';
  }
  function renderDetail() {
    var L = list(), r = ROWS.filter(function (x) { return x.code === sel; })[0];
    if (!r) { det.innerHTML = ''; return; }
    var idx = L.indexOf(r), k = kind(r), h = '';
    h += '<div class="pp2-head"><div><span class="pp2-k">' + esc(fmt(t('dz.product'), { i: idx + 1, n: L.length })) + '</span><h2>' + esc(r.name) + '</h2>' +
      '<span class="pp2-sub">' + esc(fmt(t('dz.sub'), { c: r.code, p: r.pack, d: r.scd ? dfmt(r.scd) + (r.age != null ? ' · ' + fmt(t('dz.f.ago'), { n: r.age }) : '') : '—' })) + '</span></div>' +
      '<div class="pp2-head__right"><span class="pill ' + VPILL[k] + ' js-vpill">' + esc(t(PILL[k][1])) + '</span>' +
      '<button type="button" class="pp2-nav" data-nav="-1" aria-label="' + esc(t('d.prev')) + '">‹</button><button type="button" class="pp2-nav" data-nav="1" aria-label="' + esc(t('d.next')) + '">›</button></div></div>';
    if (r.need) {
      h += '<div class="msg msg--need"><span class="ico">✕</span><div><b>' + esc(t('d.m.need.h')) + '</b>' + esc(t('w.' + r.why)) + '</div></div>';
      h += '<a class="btn btn--ghost" href="StockLess-Step3-Readiness.html">' + esc(t('d.fix')) + '</a>';
      det.innerHTML = h; wire(r); return;
    }
    var o = obs(r), avg = o.length ? o.reduce(function (a, b) { return a + b; }, 0) / o.length : 0;
    var cover = avg > 0 ? (r.stock / avg).toFixed(1) : '—';
    h += '<section class="pp2-ev"><div class="pp2-ev__head"><h3>' + esc(t('dz.h')) + '</h3><button type="button" class="btn--link" data-ev aria-expanded="' + EV_OPEN + '">' + esc(t(EV_OPEN ? 'dz.hide' : 'dz.show')) + '</button></div>';
    if (EV_OPEN) {
      h += '<div class="pp2-ev__body"><div class="pp2-ev__main"><p class="pp2-fc"><b>' + r.low + '–' + r.high + ' ' + esc(t('s4.units')) + '</b><span>' + esc(fmt(t('dz.fct'), { a: plusDays(0), b: plusDays(27) })) + '</span></p>' + chartHTML(r) + '</div>' +
        '<div class="pp2-facts">' +
        '<div><small>' + esc(t('dz.f.stock')) + '</small><b>' + r.stock + '</b><small>' + esc(t('tag.file')) + '</small></div>' +
        '<div><small>' + esc(t('dz.f.avg')) + '</small><b>' + avg.toFixed(1) + '</b><small>' + esc(fmt(t('dz.f.avgs'), { n: o.length })) + '</small></div>' +
        '<div><small>' + esc(t('dz.f.cover')) + '</small><b>' + cover + '</b><small>' + esc(t('dz.f.covers')) + '</small></div>' +
        '<div><small>' + esc(t('dz.f.count')) + '</small><b>' + esc(dfmt(r.scd)) + '</b><small>' + esc(r.age != null ? fmt(t('dz.f.ago'), { n: r.age }) : '') + '</small></div>' +
        '</div></div>';
    }
    h += '</section>';
    var mx = Math.max(50, r.high * 2);
    h += '<div class="pp2-two"><div class="pp2-sugg js-sugg">' + suggHTML(r) + '</div>' +
      '<div class="pp2-order"><label class="pp2-k" for="plan-in">' + esc(t('dz.yo')) + '</label>' +
      '<div class="pp2-step"><button type="button" class="pp2-sbtn" data-step="-1" aria-label="' + esc(t('dz.less')) + '">−</button><input id="plan-in" type="number" min="0" step="1" inputmode="numeric" data-q="plan" value="' + (r.plan == null ? '' : r.plan) + '" placeholder="0"><button type="button" class="pp2-sbtn" data-step="1" aria-label="' + esc(t('dz.more')) + '">+</button><span>' + esc(t('s4.units')) + '</span></div>' +
      '<input type="range" class="qf__range" min="0" max="' + mx + '" step="1" value="' + (r.plan || 0) + '" data-q="plan" aria-label="' + esc(t('dz.yo')) + '">' +
      '<div class="pp2-inc"><label for="inc-in">' + esc(t('x.inc')) + '</label><input id="inc-in" type="number" min="0" step="1" inputmode="numeric" data-q="inc" value="' + r.inc + '"><span>' + esc(t('s4.units')) + '</span></div></div></div>';
    h += '<section class="pp2-check js-pcheck">' + pcheckHTML(r) + '</section>';
    var ex;
    if (!r.expraw) ex = t('x.exp.none');
    else { var p = r.expraw.split('-'), dd = Math.round((new Date(+p[0], +p[1] - 1, +p[2]) - AD) / 864e5); ex = fmt(t(dd <= 28 ? 'x.exp.soon' : 'x.exp.ok'), { d: dfmt(r.expraw, 1), n: dd }); }
    var sq = supplierQty(r);
    var supBody = '<div class="sup__grid"><label>' + esc(t('sup.case')) + '<input type="number" min="1" data-sup="case" value="' + (r.case || '') + '"></label>' +
      '<label>' + esc(t('sup.min')) + '<input type="number" min="0" data-sup="min" value="' + (MIN[r.code] || 0) + '"></label>' +
      '<label>' + esc(t('sup.lead')) + '<input type="number" min="0" data-sup="lead" value="' + (r.lead || 0) + '"></label></div>' +
      (sq.q === 0 ? '<p>' + esc(t('sup.zero')) + '</p>' : '<p>' + esc(fmt(t('sup.q'), { q: sq.q, c: sq.k, k: sq.c, d: addDays(r.lead || 0) })) + '</p><button type="button" class="btn btn--small btn--ghost" data-use="' + sq.q + '">' + esc(fmt(t('sup.use'), { q: sq.q })) + '</button>');
    var extras = [
      { title: t('x.exp'), sum: ex, body: '<p>' + esc(t('x.exp.note')) + '</p>' },
      { title: t('sup.h'), sum: fmt(t('dz.supsum'), { s: r.supplier || '—', c: r.case || '—', d: r.lead || 0 }), body: supBody }
    ];
    h += '<div class="pp2-two pp2-extras">' + extras.map(function (x, i) {
      var open = EXTRA === i;
      return '<div class="pp2-x"><button type="button" class="pp2-x__btn" data-extra="' + i + '" aria-expanded="' + open + '"><span><b>' + esc(x.title) + '</b><small>' + esc(x.sum) + '</small></span><i aria-hidden="true">' + (open ? '−' : '+') + '</i></button>' + (open ? '<div class="pp2-x__body">' + x.body + '</div>' : '') + '</div>';
    }).join('') + '</div>';
    h += '<div class="det__foot"><button type="button" class="btn btn--primary" data-done>' + esc(t('dz.done')) + '</button></div>';
    det.innerHTML = h; wire(r);
  }
  function live(r) {
    var k = kind(r), pill = det.querySelector('.js-vpill');
    if (pill) { pill.className = 'pill ' + VPILL[k] + ' js-vpill'; pill.textContent = t(PILL[k][1]); }
    det.querySelector('.js-pcheck').innerHTML = pcheckHTML(r);
    det.querySelector('.js-sugg').innerHTML = suggHTML(r);
    det.querySelectorAll('.js-sugg [data-use]').forEach(useBtn(r));
    renderKPIs(); renderTable();
  }
  function useBtn(r) { return function (b) { b.addEventListener('click', function () { r.plan = +b.dataset.use; syncQ(r); live(r); }); }; }
  function syncQ(r) {
    det.querySelectorAll('[data-q]').forEach(function (el) { var v = r[el.dataset.q]; if (document.activeElement !== el) el.value = el.type === 'range' ? (v || 0) : (v == null ? '' : v); });
  }
  function wire(r) {
    det.querySelectorAll('[data-nav]').forEach(function (b) {
      b.addEventListener('click', function () { var L2 = list(), i = L2.indexOf(r), n = L2[(i + +b.dataset.nav + L2.length) % L2.length]; if (n) { EXTRA = -1; select(n.code); } });
    });
    var ev = det.querySelector('[data-ev]');
    if (ev) ev.addEventListener('click', function () { EV_OPEN = !EV_OPEN; renderDetail(); det.querySelector('[data-ev]').focus(); });
    det.querySelectorAll('[data-q]').forEach(function (el) {
      el.addEventListener('input', function () {
        var k = el.dataset.q, v = el.value === '' ? null : Math.max(0, Math.floor(+el.value));
        if (v != null && isNaN(v)) return;
        if (k === 'inc') r.inc = v || 0; else r.plan = v;
        syncQ(r); live(r);
      });
    });
    det.querySelectorAll('[data-step]').forEach(function (b) { b.addEventListener('click', function () { r.plan = Math.max(0, (r.plan || 0) + +b.dataset.step); syncQ(r); live(r); }); });
    det.querySelectorAll('[data-use]').forEach(useBtn(r));
    det.querySelectorAll('[data-extra]').forEach(function (b) { b.addEventListener('click', function () { var i = +b.dataset.extra; EXTRA = EXTRA === i ? -1 : i; renderDetail(); var nb = det.querySelector('[data-extra="' + i + '"]'); if (nb) nb.focus(); }); });
    det.querySelectorAll('[data-sup]').forEach(function (inpS) {
      inpS.addEventListener('change', function () {
        var v = Math.max(0, Math.floor(+inpS.value || 0));
        if (inpS.dataset.sup === 'case') r.case = Math.max(1, v); else if (inpS.dataset.sup === 'min') MIN[r.code] = v; else r.lead = v;
        renderDetail();
      });
    });
    var dn = det.querySelector('[data-done]');
    if (dn) dn.addEventListener('click', function () {
      var L2 = list(), i = L2.indexOf(r), n = L2[(i + 1) % L2.length];
      EXTRA = -1; if (n) { select(n.code); det.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });
  }
