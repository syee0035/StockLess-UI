# Step 3: Products / Rows tabs (the "underlying numbers" moved to the top, simplified).
a("vt.label", "Readiness view", "Paparan kesediaan", "检查结果视图")
a("vt.prod", "Products", "Produk", "商品")
a("vt.rows", "Rows in your file", "Baris dalam fail anda", "文件里的行")
a("rw.head", "of {t} rows will be used", "daripada {t} baris akan digunakan", "行会被使用，共 {t} 行")
a("rw.safe", "Your file isn't changed", "Fail anda tidak diubah", "原始文件不会被更改")
a("rw.used", "Used in the plan", "Digunakan dalam pelan", "用于计划")
a("rw.out", "Left out", "Diketepikan", "没用上")
a("rw.tidy", "Tidied for you (still used)", "Dikemas untuk anda (masih digunakan)", "已帮您整理（仍会使用）")
a("rw.why", "Why {n} rows were left out", "Kenapa {n} baris diketepikan", "为什么有 {n} 行没用上")
a("rw.todo", "What to do", "Apa yang perlu dibuat", "该怎么做")
a("rw.fixn", "Fix {n} rows in your file", "Baiki {n} baris dalam fail anda", "在文件里修改这 {n} 行")
a("rw.fix1", "Fix 1 row in your file", "Baiki 1 baris dalam fail anda", "在文件里修改这 1 行")
a("rw.nothing", "Nothing to fix", "Tiada apa perlu dibaiki", "不用修改")
a("rw.rows", "Rows", "Baris", "行")
a("rw.cont", "Or continue now — these rows are simply left out of the plan.", "Atau teruskan sekarang — baris ini cuma tak dikira dalam pelan.", "也可以现在继续，这些行只是不会算进计划里。")
a("rw.show", "Show these rows in “What we found” ↓", "Lihat baris ini dalam “Apa yang kami jumpa” ↓", "在「我们发现的情况」里查看这些行 ↓")
a("rw.r.date", "Dates we couldn't read", "Tarikh yang tak dapat dibaca", "看不懂的日期")
a("rw.r.qty", "Quantity isn't a number", "Kuantiti bukan nombor", "数量不是数字")
a("rw.r.noprod", "No product code", "Tiada kod produk", "没有商品代码")
a("rw.r.dup", "Repeated rows (latest kept)", "Baris berulang (yang terbaru disimpan)", "重复的行（保留最新一行）")
a("rw.r.other", "Other reasons", "Sebab lain", "其他原因")
a("rw.a.date", "Write each date as day/month/year (for example 15/09/2026), then upload the file again.", "Tulis setiap tarikh sebagai hari/bulan/tahun (contoh 15/09/2026), kemudian muat naik fail semula.", "把日期写成 日/月/年（例如 15/09/2026），再重新上传文件。")
a("rw.a.qty", "Type the number of units sold, for example 3 instead of a word.", "Taip bilangan unit dijual, contohnya 3 dan bukan perkataan.", "填上卖出的件数，例如写 3，而不是文字。")
a("rw.a.noprod", "Add the product code so we know what was sold.", "Tambah kod produk supaya kami tahu apa yang dijual.", "补上商品代码，我们才知道卖的是什么。")
a("rw.a.dup", "These were exact repeats. We kept the latest copy so sales aren't counted twice.", "Ini baris yang sama sepenuhnya. Kami simpan salinan terbaru supaya jualan tak dikira dua kali.", "这些是完全一样的行。我们保留了最新一行，销量不会重复计算。")
a("rw.a.other", "Download the problem list to see these rows.", "Muat turun senarai masalah untuk lihat baris ini.", "下载问题清单查看这些行。")
a("dd.h2", "See every finding as a table", "Lihat semua dapatan dalam jadual", "用表格查看全部检查结果")

_out_total = TOT - USED
_date_rows = sorted(i["row"] for i in ISS if i["type"] in ("date", "future"))
_qty_rows = sorted(i["row"] for i in ISS if i["type"] == "qty")
_id_rows = sorted(i["row"] for i in ISS if i["type"] == "noprod")
_dup_rows = sorted(r for d in DUPS for r in d["drop"])
_ex = lambda t: next((i["found"] for i in ISS if i["type"] in t), "")
_R = [("date", _date_rows, "date", _ex(("date", "future")), True),
      ("qty", _qty_rows, "qty", _ex(("qty",)), True),
      ("noprod", _id_rows, "noprod", "", True),
      ("dup", _dup_rows, "tidy", "", False)]
_R = [r for r in _R if r[1]]
_other = _out_total - sum(len(r[1]) for r in _R)
if _other > 0:
    _R.append(("other", [], "", "", False))
_mx = max([len(r[1]) for r in _R] + [_other, 1])

def _fmt_rows(rows):
    s = ", ".join(f"{r:,}" for r in rows[:4])
    return s + ("…" if len(rows) > 4 else "")

_reasons = ""
for _k, (_key, _rows, _grp, _obs, _fix) in enumerate(_R):
    _n = len(_rows) if _key != "other" else _other
    _w = round(100 * _n / _mx)
    _on = " is-on" if _k == 0 else ""
    _sel = "true" if _k == 0 else "false"
    _lab = I.s("rw.r." + _key)
    _reasons += (f'<button type="button" role="radio" aria-checked="{_sel}" class="rw-reason{_on}" data-n="{_n}" data-key="{_key}" data-group="{_grp}" data-fix="{1 if _fix else 0}" data-rows="{_fmt_rows(_rows)}" data-obs="{html.escape(_obs)}">'
                 f'<span class="rw-reason__l" data-i18n="rw.r.{_key}">{_lab}</span><span class="rw-meter" aria-hidden="true"><span style="width:{_w}%"></span></span><b class="num">{_n}</b></button>')

_whytxt = I.s("rw.why").replace("{n}", str(_out_total))
_headtxt = I.s("rw.head").replace("{t}", f"{TOT:,}")
rows_panel = f'''<div class="rw">
  <div class="rw__head"><p class="rw__headline"><b class="num">{USED:,}</b> <span class="rw-tpl" data-tpl="rw.head" data-t="{TOT:,}">{_headtxt}</span></p><span class="rw__safe">✓ <span data-i18n="rw.safe">{I.s("rw.safe")}</span></span></div>
  <div class="rw__bar" role="img" aria-label="{USED:,} / {TOT:,}"><span class="rw__used" style="flex-grow:{USED}"></span><span class="rw__out" style="flex-grow:{_out_total}"></span></div>
  <ul class="rw__legend"><li><i class="rw-key rw-key--used"></i><span data-i18n="rw.used">{I.s("rw.used")}</span> · <b class="num">{USED:,}</b></li><li><i class="rw-key rw-key--out"></i><span data-i18n="rw.out">{I.s("rw.out")}</span> · <b class="num">{_out_total}</b></li><li><i class="rw-key rw-key--tidy"></i><span data-i18n="rw.tidy">{I.s("rw.tidy")}</span> · <b class="num">{len(TIDY)}</b></li></ul>
  <div class="rw__grid">
    <div class="rw__reasons"><h3 class="rw-h rw-tpl" data-tpl="rw.why" data-n="{_out_total}">{_whytxt}</h3><div role="radiogroup" class="rw__list" aria-label="{_whytxt}">{_reasons}</div></div>
    <div class="rw__todo" aria-live="polite"><h3 class="rw-h" data-i18n="rw.todo">{I.s("rw.todo")}</h3><b class="rw__title"></b><p class="rw__advice"></p><p class="rw__where"></p><p class="rw__note" data-i18n="rw.cont">{I.s("rw.cont")}</p><button type="button" class="rw__show" data-i18n="rw.show">{I.s("rw.show")}</button></div>
  </div>
</div>'''

_ptab = deep[deep.index('<div class="card ptab">'):deep.rindex('</div></details>')]
deep2 = f'<details class="deep"><summary data-i18n="dd.h2">{I.s("dd.h2")}</summary><div class="deep__in">{_ptab}</div></details>'
main = main.replace(deep, deep2)

_s = main.index('<div class="stats">')
_e = main.index('<div class="s3">')
_prod = main[_s:_e]
_tabs = f'''<div class="vtabs" role="tablist" aria-label="{I.s("vt.label")}">
  <button type="button" role="tab" id="vt-prod" class="vtab" aria-selected="true" aria-controls="vp-prod"><span aria-hidden="true">🛒</span> <span data-i18n="vt.prod">{I.s("vt.prod")}</span> <span class="vtab__n num">{len(P)}</span></button>
  <button type="button" role="tab" id="vt-rows" class="vtab" aria-selected="false" aria-controls="vp-rows" tabindex="-1"><span aria-hidden="true">📄</span> <span data-i18n="vt.rows">{I.s("vt.rows")}</span> <span class="vtab__n num">{TOT:,}</span></button>
</div>
<div id="vp-prod" role="tabpanel" aria-labelledby="vt-prod">{_prod}</div>
<div id="vp-rows" role="tabpanel" aria-labelledby="vt-rows" class="card rw-card" hidden>{rows_panel}</div>
'''
main = main[:_s] + _tabs + main[_e:]

main += r'''
<style>
.vtabs{display:flex;gap:6px;padding:6px;margin-bottom:18px;border-radius:16px;background:var(--band);border:1px solid var(--line-soft)}
.vtab{flex:1;display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;border:0;border-radius:12px;background:transparent;cursor:pointer;font-family:var(--display);font-weight:700;font-size:16px;color:var(--muted);transition:background-color .2s,color .2s,box-shadow .2s}
.vtab:hover{color:var(--ink)}
.vtab[aria-selected="true"]{background:#fff;color:var(--teal-deep);box-shadow:0 4px 12px rgba(22,49,59,.10)}
.vtab__n{flex:none;white-space:nowrap;padding:2px 9px;border-radius:999px;background:#DCE8E4;font-size:12px;color:var(--muted)}
.vtab[aria-selected="true"] .vtab__n{background:var(--teal-deep);color:#fff}
.rw-card{margin-bottom:20px}
.rw{display:flex;flex-direction:column;gap:14px;padding:22px 24px}
.rw__head{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap}
.rw__headline{margin:0;font-size:18px;color:var(--muted)}
.rw__headline b{font-family:var(--display)!important;font-weight:800!important;font-size:34px;line-height:1;color:var(--teal-deep)}
.rw__safe{padding:6px 12px;border-radius:999px;background:var(--teal-tint);font-family:var(--display);font-weight:700;font-size:13px;color:var(--teal-deep)}
.rw__bar{display:flex;height:22px;border-radius:11px;overflow:hidden;background:var(--line-soft)}
.rw__used{background:var(--teal)}.rw__out{min-width:18px;background:var(--amber-strong)}
.rw__legend{display:flex;flex-wrap:wrap;gap:6px 20px;margin:0;padding:0;list-style:none;font-size:14px;color:var(--muted)}
.rw__legend li{display:inline-flex;align-items:center;gap:6px}
.rw-key{width:12px;height:12px;border-radius:3px;box-sizing:border-box}
.rw-key--used{background:var(--teal)}.rw-key--out{background:var(--amber-strong)}.rw-key--tidy{border:2px solid var(--teal)}
.rw__grid{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:16px}
h3.rw-h{margin:0 0 6px;font-family:var(--display);font-weight:800;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.rw__todo h3.rw-h{color:var(--teal-deep)}
.rw__reasons{padding:16px;border-radius:16px;background:#F7FAF9}
.rw-reason{display:flex;align-items:center;gap:12px;width:100%;padding:10px 12px;border:1px solid transparent;border-radius:10px;background:transparent;cursor:pointer;text-align:left;font:inherit;color:var(--ink)}
.rw-reason:hover{background:#fff;border-color:var(--line)}
.rw-reason.is-on{background:#fff;border-color:var(--mint);box-shadow:0 2px 8px rgba(22,49,59,.06)}
.rw-reason__l{flex:1;font-family:var(--display);font-weight:700;font-size:15px}
.rw-meter{width:120px;height:8px;border-radius:4px;background:var(--line-soft);overflow:hidden}
.rw-meter span{display:block;height:100%;border-radius:4px;background:var(--amber-strong)}
.rw-reason b{width:32px;text-align:right}
.rw__todo{display:flex;flex-direction:column;gap:8px;padding:16px 18px;border-radius:16px;border:1.5px solid #CFE4DE;background:#F3FAF7}
.rw__title{font-family:var(--display);font-size:18px}
.rw__todo p{margin:0;font-size:15px;line-height:1.5;color:var(--ink-2)}
.rw__where code{font-family:var(--data);font-size:13px;padding:1px 6px;border-radius:4px;background:#EEF3F1}
.rw__todo .rw__note{color:var(--muted);font-size:14px}
.rw__show{align-self:flex-start;margin-top:auto;padding:4px 0;border:0;background:none;cursor:pointer;font-family:var(--display);font-weight:700;font-size:14px;color:var(--teal-deep)}
.rw__show:hover{text-decoration:underline}
@media(max-width:760px){.vtab{font-size:14px;min-height:44px;gap:6px;padding:4px 6px;line-height:1.2}.vtab>span[aria-hidden]{display:none}.rw{padding:16px}.rw__grid{grid-template-columns:minmax(0,1fr)}.rw-meter{width:64px}.rw__headline b{font-size:28px}}
</style>
<script>
(function () {
  var tabs = [document.getElementById('vt-prod'), document.getElementById('vt-rows')];
  var panels = { 'vt-prod': document.getElementById('vp-prod'), 'vt-rows': document.getElementById('vp-rows') };
  function show(tab, focus) {
    tabs.forEach(function (b) { var on = b === tab; b.setAttribute('aria-selected', on); b.tabIndex = on ? 0 : -1; panels[b.id].hidden = !on; });
    if (focus) tab.focus();
  }
  tabs.forEach(function (b, i) {
    b.addEventListener('click', function () { show(b); });
    b.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); show(tabs[1 - i], true); } });
  });
  var reasons = Array.prototype.slice.call(document.querySelectorAll('.rw-reason'));
  var cur = reasons[0];
  function tt(k) { return (window.t && window.t(k)) || k; }
  function render() {
    document.querySelectorAll('.rw-tpl').forEach(function (el) {
      var s = tt(el.getAttribute('data-tpl')).replace('{t}', el.getAttribute('data-t') || '').replace('{n}', el.getAttribute('data-n') || '');
      el.textContent = s; if (el.tagName === 'H3') el.parentNode.querySelector('.rw__list').setAttribute('aria-label', s);
    });
    if (!cur) return;
    var n = +cur.getAttribute('data-n'), key = cur.getAttribute('data-key'), fix = cur.getAttribute('data-fix') === '1';
    document.querySelector('.rw__title').textContent = !fix ? tt('rw.nothing') : n === 1 ? tt('rw.fix1') : tt('rw.fixn').replace('{n}', n);
    document.querySelector('.rw__advice').textContent = tt('rw.a.' + key);
    var where = document.querySelector('.rw__where'), rows = cur.getAttribute('data-rows'), obs = cur.getAttribute('data-obs');
    where.innerHTML = '';
    if (rows) { where.appendChild(document.createTextNode(tt('rw.rows') + ' ' + rows)); if (obs) { where.appendChild(document.createTextNode(' · ')); var c = document.createElement('code'); c.textContent = obs; where.appendChild(c); } }
    document.querySelector('.rw__show').hidden = !cur.getAttribute('data-group');
  }
  reasons.forEach(function (b) { b.addEventListener('click', function () {
    cur = b; reasons.forEach(function (r) { var on = r === b; r.classList.toggle('is-on', on); r.setAttribute('aria-checked', on); }); render();
  }); });
  document.querySelector('.rw__show').addEventListener('click', function () {
    var g = document.querySelector('.wf__g[data-g="' + cur.getAttribute('data-group') + '"]');
    if (!g) return; g.open = true; g.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
  document.addEventListener('langchange', render);
  window.addEventListener('DOMContentLoaded', render); render();
})();
</script>'''
