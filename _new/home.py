import json, html, os
from common import *
IMG = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "home_img.json")))
I = I18N(); shared(I); a = I.add

# ---------- copy ----------
a("hp.nav.why", "Why it matters", "Kenapa penting", "为什么重要")
a("hp.nav.how", "How it works", "Cara ia berfungsi", "怎么运作")
a("hp.nav.diff", "Why StockLess", "Kenapa StockLess", "为什么选 StockLess")
a("hp.nav.ex", "Example", "Contoh", "示例")
a("hp.nav.faq", "FAQ", "Soalan lazim", "常见问题")
a("hp.cta", "Start with your sales data →", "Mula dengan data jualan anda →", "从您的销售数据开始 →")
a("hp.eyebrow", "Smaller restocks. Bigger possibilities.", "Stok lebih kecil. Peluang lebih besar.", "少进一点货，多一点可能。")
a("hp.h1a", "Less ", "Kurang ", "减少")
a("hp.h1b", "food waste.", "pembaziran makanan.", "食物浪费。")
a("hp.h1c", "Lower costs. Higher profits.", "Kos lebih rendah. Untung lebih tinggi.", "降低成本，提高利润。")
a("hp.lede", "Smarter restocking for small retailers. Make the most of what you stock.", "Tambah stok dengan lebih bijak untuk peruncit kecil. Manfaatkan setiap barang yang anda simpan.", "为小型零售商打造的聪明补货方式，让每一件库存都物尽其用。")
a("hp.see", "See how it works ↓", "Lihat cara ia berfungsi ↓", "看看怎么运作 ↓")
a("hp.chk1", "Runs in your browser", "Berjalan dalam pelayar anda", "在浏览器里运行")
a("hp.chk2", "No account needed", "Tiada akaun diperlukan", "不用注册账号")
a("hp.chk3", "No uploads", "Tiada muat naik", "不上传文件")
a("hp.card.k", "Purchase plan · SKU MM0001", "Pelan belian · SKU MM0001", "进货计划 · SKU MM0001")
a("hp.card.steady", "Steady seller", "Laku secara konsisten", "卖得稳定")
a("hp.card.today", "Today", "Hari ini", "今天")
a("hp.card.past", "Past 8 weeks", "8 minggu lepas", "过去 8 周")
a("hp.card.next", "Next 4 weeks", "4 minggu akan datang", "未来 4 周")
a("hp.card.pc", "Purchase check", "Semakan belian", "进货检查")
a("hp.card.ok", "This plan is within range.", "Pelan ini dalam julat jangkaan.", "这次的数量刚刚好。")
a("hp.card.bal", "Looks balanced", "Nampak seimbang", "数量刚刚好")

a("hp.big.k", "The bigger picture", "Gambaran lebih besar", "更大的图景")
a("hp.big.h", "Food waste starts with what we stock.", "Pembaziran makanan bermula dengan apa yang kita simpan.", "食物浪费，从进货就开始了。")
a("hp.big.t", "For small retailers, every restocking decision can mean the difference between selling stock and wasting it.", "Bagi peruncit kecil, setiap keputusan tambah stok boleh menentukan sama ada barang terjual atau terbuang.", "对小店来说，每一次补货决定，都可能决定货是卖出去还是被浪费。")
a("hp.st1", "of food waste generated globally in 2022, including inedible parts.", "sisa makanan dihasilkan di seluruh dunia pada 2022, termasuk bahagian yang tidak boleh dimakan.", "2022 年全球产生的食物浪费，包括不可食用部分。")
a("hp.st2", "of that food waste came from the retail sector.", "daripada sisa makanan itu datang daripada sektor runcit.", "这些食物浪费来自零售业。")
a("hp.st3", "the SDG 12.3 target year for halving per-capita food waste at retail and consumer levels.", "tahun sasaran SDG 12.3 untuk mengurangkan separuh sisa makanan per kapita di peringkat runcit dan pengguna.", "SDG 12.3 的目标年份：零售和消费环节的人均食物浪费减半。")
a("hp.src", "Sources: UNEP Food Waste Index 2024 · SDG 12.3", "Sumber: UNEP Food Waste Index 2024 · SDG 12.3", "来源：UNEP 食物浪费指数 2024 · SDG 12.3")
a("hp.case.k", "Case study", "Kajian kes", "案例")
a("hp.case.t", "saved per semester after an AI stock system cut spoilage from 20% to 8% at a Malaysian university food service.", "dijimatkan setiap semester selepas sistem stok AI mengurangkan kerosakan daripada 20% kepada 8% di sebuah perkhidmatan makanan universiti di Malaysia.", "一所马来西亚大学餐饮服务使用 AI 库存系统后，损耗从 20% 降到 8%，每学期省下这笔钱。")
a("hp.case.s", "(MSU Greenally, self-reported)", "(MSU Greenally, dilaporkan sendiri)", "（MSU Greenally，自行报告）")
a("hp.img.waste", "Discarded vegetables piled at a landfill", "Sayur-sayuran yang dibuang bertimbun di tapak pelupusan", "堆在垃圾场的废弃蔬菜")

a("hp.how.k", "How it works", "Cara ia berfungsi", "怎么运作")
a("hp.how.h1", "Four steps to a ", "Empat langkah ke arah ", "四步，")
a("hp.how.h2", "confident order", "pesanan yang yakin", "放心下单")
a("hp.s1", "Upload your sales data", "Muat naik data jualan anda", "上传销售数据")
a("hp.s1t", "Import your existing sales CSV or Excel file, or try the sample data first.", "Import fail CSV atau Excel jualan sedia ada, atau cuba data sampel dahulu.", "导入现有的 CSV 或 Excel 销售文件，也可以先试试示例数据。")
a("hp.s2", "Map your columns", "Padankan lajur anda", "匹配栏位")
a("hp.s2t", "Tell StockLess which columns hold your sale date, product and quantity.", "Beritahu StockLess lajur mana yang ada tarikh jualan, produk dan kuantiti.", "告诉 StockLess 哪些栏位是销售日期、商品和数量。")
a("hp.s3", "Check your data is ready", "Semak data anda sudah sedia", "检查数据是否就绪")
a("hp.s3t", "StockLess looks for gaps, duplicates and unusual rows before any analysis.", "StockLess mencari jurang, pendua dan baris luar biasa sebelum sebarang analisis.", "分析前，StockLess 会先找出缺漏、重复和异常的行。")
a("hp.s4", "Plan your purchases", "Rancang pembelian anda", "规划进货")
a("hp.s4t", "See the expected demand, then decide what to restock — with the reasoning shown.", "Lihat jangkaan jualan, kemudian tentukan apa yang perlu ditambah — dengan sebabnya ditunjukkan.", "先看预计销量，再决定补什么货——每一步都有理由。")

a("hp.diff.k", "Why StockLess", "Kenapa StockLess", "为什么选 StockLess")
a("hp.diff.h1", "Between a spreadsheet and an ERP, ", "Antara hamparan dan ERP, ", "介于电子表格和 ERP 之间，")
a("hp.diff.h2", "just what you need", "cukup apa yang anda perlukan", "刚好是您需要的")
a("hp.diff.t", "Most small shops plan orders in a spreadsheet or from memory. ERP systems can do more, but they cost more and take months to set up. StockLess does one job well: helping you decide how much to order.", "Kebanyakan kedai kecil merancang pesanan dalam hamparan atau ikut ingatan. Sistem ERP boleh buat lebih banyak, tetapi lebih mahal dan ambil masa berbulan untuk disediakan. StockLess buat satu kerja dengan baik: bantu anda tentukan berapa banyak nak pesan.", "大多数小店用电子表格或凭记忆来订货。ERP 功能多，但贵，而且要花好几个月来设置。StockLess 只专注做好一件事：帮您决定该进多少货。")
a("hp.c.sheet", "Spreadsheet", "Hamparan", "电子表格")
a("hp.c.sheet.t", "Flexible, but you do the maths", "Fleksibel, tetapi anda kira sendiri", "灵活，但要自己算")
a("hp.c.erp", "ERP system", "Sistem ERP", "ERP 系统")
a("hp.c.erp.t", "Powerful, but heavy for a small shop", "Hebat, tetapi berat untuk kedai kecil", "功能强，但对小店太重")
a("hp.c.sl", "StockLess", "StockLess", "StockLess")
a("hp.c.sl.t", "Focused on your next order", "Fokus pada pesanan anda yang seterusnya", "专注于您的下一次订货")
a("hp.c.best", "Built for small shops", "Dibina untuk kedai kecil", "为小店而设计")
# comparison rows: (key, en, ms, zh) then per column: (state, text_key)
ROWS_DIFF = [
  ("setup", "Set-up", "Persediaan", "上手时间"),
  ("cost", "Cost", "Kos", "费用"),
  ("forecast", "Expected demand", "Jangkaan jualan", "预计销量"),
  ("check", "Checks your order", "Semak pesanan anda", "检查您的订单"),
  ("data", "Spots data problems", "Kesan masalah data", "找出数据问题"),
  ("privacy", "Where your data goes", "Ke mana data anda pergi", "数据去哪里"),
]
for k, en, ms, zh in ROWS_DIFF: a("hp.r." + k, en, ms, zh)
CELLS = {
  "setup":    [("mid", "Minutes, but every formula is yours to build", "Beberapa minit, tetapi semua formula anda bina sendiri", "几分钟，但公式都要自己写"),
               ("no", "Weeks to months, often with a consultant", "Berminggu hingga berbulan, selalunya dengan perunding", "几周到几个月，常常要请顾问"),
               ("yes", "Minutes: use the sales export you already have", "Beberapa minit: guna eksport jualan yang sedia ada", "几分钟：直接用现有的销售导出文件")],
  "cost":     [("yes", "Free or low cost", "Percuma atau murah", "免费或便宜"),
               ("no", "Licences, set-up fees and training", "Lesen, yuran persediaan dan latihan", "授权费、设置费和培训费"),
               ("yes", "Free to use in your browser", "Percuma digunakan dalam pelayar", "在浏览器里免费使用")],
  "forecast": [("no", "Only if you build it yourself", "Hanya jika anda bina sendiri", "除非自己做"),
               ("mid", "Often an add-on module", "Selalunya modul tambahan", "通常要另买模块"),
               ("yes", "A 4-week range for every product", "Julat 4 minggu untuk setiap produk", "每个商品都有 4 周范围")],
  "check":    [("no", "No", "Tidak", "没有"),
               ("mid", "Reorder points you set by hand", "Titik pesanan semula yang anda tetapkan sendiri", "要自己设补货点"),
               ("yes", "Too much, about right or too little — with the reason", "Terlalu banyak, cukup atau terlalu sedikit — dengan sebabnya", "太多、刚好还是太少——附上理由")],
  "data":     [("no", "Errors stay hidden in cells", "Ralat tersembunyi dalam sel", "错误藏在格子里"),
               ("mid", "Strict data entry rules", "Peraturan kemasukan data yang ketat", "要严格录入数据"),
               ("yes", "Flags gaps, duplicates and odd rows in plain words", "Tandakan jurang, pendua dan baris pelik dalam bahasa mudah", "用简单的话标出缺漏、重复和异常行")],
  "privacy":  [("yes", "Stays on your computer", "Kekal dalam komputer anda", "留在您的电脑")],
}
CELLS["privacy"] += [("mid", "Stored on the vendor's servers", "Disimpan di pelayan vendor", "存在供应商的服务器"),
                     ("yes", "Never leaves your device", "Tidak pernah keluar dari peranti anda", "从不离开您的设备")]
for k, cells in CELLS.items():
    for i, (st, en, ms, zh) in enumerate(cells): a(f"hp.c.{k}.{i}", en, ms, zh)

a("hp.ex.k", "Interactive example", "Contoh interaktif", "互动示例")
a("hp.ex.h", "Try a purchase check", "Cuba semakan belian", "试试进货检查")
a("hp.ex.t", "This is a working example — drag the slider to see the purchase check update.", "Ini contoh yang berfungsi — seret peluncur untuk lihat semakan belian berubah.", "这是可操作的示例——拖动滑杆，看进货检查怎么变化。")
a("hp.ex.prod", "Kopi O Kaw 2in1 · 10 sachets", "Kopi O Kaw 2in1 · 10 sachets", "Kopi O Kaw 2in1 · 10 sachets")
a("hp.ex.dem", "Demand overview", "Gambaran jualan", "销量概览")
a("hp.ex.exp", "Expected demand (next 4 weeks)", "Jangkaan jualan (4 minggu akan datang)", "预计销量（未来 4 周）")
a("hp.units", "units", "unit", "件")
a("hp.lg.past", "Past sales", "Jualan lepas", "过去销量")
a("hp.lg.exp", "Expected demand", "Jangkaan jualan", "预计销量")
a("hp.lg.range", "Possible range", "Julat mungkin", "可能范围")
a("hp.ex.plan", "Your planned order", "Pesanan dirancang anda", "您计划的订购量")
a("hp.ex.sugg", "StockLess suggests 10", "StockLess cadangkan 10", "StockLess 建议 10")
a("hp.ex.soh", "Stock on hand", "Stok sedia ada", "现有库存")
a("hp.ex.inc", "Incoming", "Dalam perjalanan", "在途")
a("hp.ex.after", "After order", "Selepas pesanan", "订货后")
a("hp.v.ok.k", "Looks balanced", "Nampak seimbang", "数量刚刚好")
a("hp.v.ok.h", "This plan is within range.", "Pelan ini dalam julat jangkaan.", "这次的数量刚刚好。")
a("hp.v.ok.t", "You would have {n} units, within the 7–28 four-week range, so the planned order looks about right.", "Anda akan ada {n} unit, dalam julat empat minggu 7–28, jadi pesanan ini nampak sesuai.", "您会有 {n} 件，在 7–28 的四周范围内，订购量看起来刚好。")
a("hp.v.hi.k", "Overstock risk", "Risiko stok berlebihan", "可能进太多")
a("hp.v.hi.h", "This plan looks too high.", "Pesanan ini nampak terlalu banyak.", "这次进得有点多。")
a("hp.v.hi.t", "You would have {n} units, above the 7–28 four-week range. Some stock may sit unsold.", "Anda akan ada {n} unit, melebihi julat empat minggu 7–28. Sebahagian stok mungkin tidak laku.", "您会有 {n} 件，超过 7–28 的四周范围，部分库存可能卖不掉。")
a("hp.v.lo.k", "Needs review", "Perlu disemak", "要确认一下")
a("hp.v.lo.h", "This plan looks too low.", "Pesanan ini nampak terlalu sedikit.", "这次进得有点少。")
a("hp.v.lo.t", "You would have {n} units, below the 7–28 four-week range. You may run short.", "Anda akan ada {n} unit, kurang daripada julat empat minggu 7–28. Stok mungkin tidak cukup.", "您会有 {n} 件，低于 7–28 的四周范围，可能会缺货。")
a("hp.ex.note", "Illustrative product and figures · Your results depend on your own sales and stock data.", "Produk dan angka contoh · Keputusan anda bergantung pada data jualan dan stok anda sendiri.", "示例商品和数字 · 实际结果取决于您自己的销售和库存数据。")

a("hp.get.k", "What you get at the end", "Apa yang anda dapat", "最后您会得到")
a("hp.get.h1", "Everything you need to ", "Semua yang anda perlukan untuk ", "做决定需要的，")
a("hp.get.h2", "decide with confidence", "membuat keputusan dengan yakin", "一应俱全")
a("hp.g1", "Weekly sales for the selected product", "Jualan mingguan untuk produk yang dipilih", "所选商品的每周销量")
a("hp.g2", "Your recent average (last 8 complete weeks)", "Purata terkini anda (8 minggu penuh terakhir)", "最近平均（最近 8 个完整周）")
a("hp.g3", "How long your current stock will last", "Berapa lama stok semasa anda akan bertahan", "现有库存能撑多久")
a("hp.g4", "A four-week demand range (low–high)", "Julat jualan empat minggu (rendah–tinggi)", "四周销量范围（低–高）")
a("hp.g5", "A verdict: too much, about right, or too little", "Keputusan: terlalu banyak, cukup, atau terlalu sedikit", "结论：太多、刚好或太少")
a("hp.pv.k", "Privacy", "Privasi", "隐私")
a("hp.pv.h", "Your figures stay on your computer", "Angka anda kekal dalam komputer anda", "您的数字留在您的电脑里")
a("hp.pv.t", "StockLess runs entirely in your browser. No file is ever uploaded to a server, and no account is needed. Your sales data never leaves your device.", "StockLess berjalan sepenuhnya dalam pelayar anda. Tiada fail dimuat naik ke pelayan, dan tiada akaun diperlukan. Data jualan anda tidak pernah keluar dari peranti anda.", "StockLess 完全在您的浏览器中运行，不会把文件上传到服务器，也不需要账号。您的销售数据从不离开您的设备。")
a("hp.pv.c3", "No tracking", "Tiada penjejakan", "不追踪")

a("hp.band.k", "A smarter way to restock", "Cara lebih bijak untuk tambah stok", "更聪明的补货方式")
a("hp.band.h1", "Keep less in stock, ", "Simpan stok lebih sedikit, ", "少囤点货，")
a("hp.band.h2", "unlock more possibilities.", "buka lebih banyak peluang.", "多一点可能。")
a("hp.band.cta", "Start with your sales data →", "Mula dengan data jualan anda →", "从您的销售数据开始 →")
a("hp.band.t", "Use your own CSV or Excel file, or explore an example file.", "Guna fail CSV atau Excel anda sendiri, atau terokai fail contoh.", "用您自己的 CSV 或 Excel 文件，或先看看示例文件。")
a("hp.img.produce", "Fresh fruit and vegetables on a shop shelf", "Buah-buahan dan sayur segar di rak kedai", "货架上的新鲜蔬果")

a("hp.sdg.n", "Responsible consumption and production", "Penggunaan dan pengeluaran yang bertanggungjawab", "负责任的消费和生产")
a("hp.sdg.cap", "A shared goal. An everyday action.", "Matlamat bersama. Tindakan setiap hari.", "共同的目标，日常的行动。")
a("hp.sdg.k", "Good for your shop. Better for the planet.", "Baik untuk kedai anda. Lebih baik untuk bumi.", "对小店好，对地球更好。")
a("hp.sdg.h", "Small decisions. Less waste.", "Keputusan kecil. Kurang pembaziran.", "小决定，少浪费。")
a("hp.sdg.t1", "Smarter restocking decisions can help small retailers save money while preventing food from becoming waste.", "Keputusan tambah stok yang lebih bijak boleh membantu peruncit kecil menjimatkan wang sambil mengelakkan makanan daripada terbuang.", "更聪明的补货决定，能帮小店省钱，也能避免食物被浪费。")
a("hp.sdg.t2", "Every restocking decision matters. StockLess uses your existing sales data to help you identify unnecessary orders and potential excess stock. Less stock sitting on shelves can mean less food going to waste.", "Setiap keputusan tambah stok penting. StockLess menggunakan data jualan sedia ada untuk membantu anda mengenal pasti pesanan yang tidak perlu dan stok yang mungkin berlebihan. Kurang stok terbiar di rak boleh bermakna kurang makanan terbuang.", "每一次补货决定都很重要。StockLess 用您现有的销售数据，帮您找出不必要的订单和可能多出的库存。架上积压的货少了，被浪费的食物也会少。")
a("hp.sdg.link", "Read about SDG 12 ↗", "Baca tentang SDG 12 ↗", "了解 SDG 12 ↗")
a("hp.lm.k", "Learn more", "Ketahui lebih lanjut", "了解更多")
a("hp.lm.h", "Learn more about StockLess", "Ketahui lebih lanjut tentang StockLess", "进一步了解 StockLess")
a("hp.lm.t", "Find answers to common questions about how StockLess works and how it can help your business.", "Cari jawapan kepada soalan lazim tentang cara StockLess berfungsi dan bagaimana ia boleh membantu perniagaan anda.", "关于 StockLess 怎么运作、能怎样帮到您的生意，常见问题都在这里。")
FAQ = [
  ("🌱", "How does StockLess work?", "Bagaimana StockLess berfungsi?", "StockLess 是怎么运作的？",
   "Upload your sales export, confirm which columns are which, and StockLess checks the data. It then works out a four-week demand range for each product and checks the order you plan to place against it.",
   "Muat naik eksport jualan anda, sahkan lajur yang betul, dan StockLess akan menyemak data. Kemudian ia mengira julat jualan empat minggu untuk setiap produk dan menyemak pesanan yang anda rancang.",
   "上传销售导出文件，确认各栏位对应什么，StockLess 就会检查数据。接着为每个商品算出四周销量范围，并用它来检查您打算下的订单。"),
  ("📄", "What data do I need?", "Data apa yang saya perlukan?", "我需要什么数据？",
   "Three columns are enough to start: sale date, product (a code, or name + pack size) and quantity sold. Stock on hand, stock count date, planned orders, incoming stock and expiry dates unlock more checks.",
   "Tiga lajur sudah cukup untuk bermula: tarikh jualan, produk (kod, atau nama + saiz pek) dan kuantiti terjual. Stok sedia ada, tarikh kiraan stok, pesanan dirancang, stok dalam perjalanan dan tarikh luput membuka lebih banyak semakan.",
   "有三个栏位就能开始：销售日期、商品（代码，或名称 + 包装规格）和销售数量。加上现有库存、盘点日期、计划订单、在途库存和有效期，就能做更多检查。"),
  ("🛒", "How are purchase recommendations made?", "Bagaimana cadangan belian dibuat?", "进货建议是怎么来的？",
   "StockLess uses your last eight complete weeks of sales to set a four-week range. The suggested restock is the middle of that range, minus the stock you have and the stock already on its way.",
   "StockLess guna jualan lapan minggu penuh terakhir untuk menetapkan julat empat minggu. Cadangan tambah stok ialah titik tengah julat itu, tolak stok yang ada dan stok yang sedang dalam perjalanan.",
   "StockLess 用最近八个完整周的销量算出四周范围。建议进货量 = 范围中间值 − 现有库存 − 在途库存。"),
  ("♻️", "How does StockLess help reduce food waste?", "Bagaimana StockLess membantu mengurangkan pembaziran makanan?", "StockLess 怎样帮助减少食物浪费？",
   "Most retail food waste starts with ordering more than will sell. By flagging orders above the expected range before you place them, StockLess helps you avoid stock that may expire on the shelf.",
   "Kebanyakan pembaziran makanan runcit bermula dengan memesan lebih daripada yang akan terjual. Dengan menandakan pesanan yang melebihi julat jangkaan sebelum anda membuatnya, StockLess membantu anda elak stok yang mungkin luput di rak.",
   "零售食物浪费大多源于进货超过能卖出的量。StockLess 会在您下单前标出超出预计范围的订单，帮您避免货品在架上过期。"),
]
for i, (ic, en, ms, zh, aen, ams, azh) in enumerate(FAQ):
    a(f"hp.q{i}", en, ms, zh); a(f"hp.a{i}", aen, ams, azh)
a("hp.lm.still", "Still have questions?", "Masih ada soalan?", "还有疑问？")
a("hp.lm.all", "View all FAQs →", "Lihat semua soalan lazim →", "查看全部常见问题 →")
a("hp.lm.less", "Close all FAQs ↑", "Tutup semua soalan lazim ↑", "收起全部常见问题 ↑")
a("hp.foot", "Supports UN SDG 12.3: halving food waste at retail by 2030.", "Menyokong SDG 12.3 PBB: mengurangkan separuh pembaziran makanan runcit menjelang 2030.", "支持联合国 SDG 12.3：在 2030 年前将零售环节的食物浪费减半。")
a("hp.top", "Back to top ↑", "Kembali ke atas ↑", "回到顶部 ↑")

T = I.t
STEP1 = "StockLess-Step1-Upload.html"

def ic(path, size=18):
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'
CHECK = '<span class="hp-tick" aria-hidden="true">' + ic('<path d="m5 12 4 4L19 6"/>', 13) + '</span>'

# Mini chart (hero card + example) — past 8 weeks + forecast fan
PAST = [5, 7, 5, 6, 3, 5, 2, 3]
def line_chart(w, h, big=False):
    l, r, t, b = (34 if big else 10), w - 10, 18, h - (26 if big else 18)
    today = l + (r - l) * 0.66
    mx = 9
    y = lambda v: b - v / mx * (b - t)
    xs = [l + i * (today - l) / 7 for i in range(8)]
    pts = " ".join(f"{x:.1f},{y(v):.1f}" for x, v in zip(xs, PAST))
    s = f'<svg viewBox="0 0 {w} {h}" class="hp-chart" aria-hidden="true">'
    if big:
        for v in (0, 4, 8):
            s += f'<line x1="{l}" x2="{r}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke="#E8EEEC"/><text x="{l-8}" y="{y(v)+4:.1f}" text-anchor="end" class="hp-ax">{v}</text>'
    lo, hi, mid = 1.75, 7, 4.4
    s += f'<path d="M{today:.1f},{y(PAST[-1]):.1f} C{today+(r-today)*.3:.1f},{y(PAST[-1]):.1f} {today+(r-today)*.7:.1f},{y(hi):.1f} {r},{y(hi):.1f} L{r},{y(lo):.1f} C{today+(r-today)*.7:.1f},{y(lo):.1f} {today+(r-today)*.3:.1f},{y(PAST[-1]):.1f} {today:.1f},{y(PAST[-1]):.1f}Z" fill="rgba(22,125,116,.16)"/>'
    s += f'<line x1="{today:.1f}" x2="{r}" y1="{y(PAST[-1]):.1f}" y2="{y(mid):.1f}" stroke="#167D74" stroke-width="2" stroke-dasharray="6 5"/>'
    s += f'<line x1="{today:.1f}" x2="{today:.1f}" y1="{t-6}" y2="{b}" stroke="#B8C8C4" stroke-dasharray="3 4"/>'
    s += f'<polyline points="{pts}" fill="none" stroke="#16313B" stroke-width="{2.5 if big else 2}" stroke-linejoin="round" stroke-linecap="round"/>'
    s += '</svg>'
    return s

hero_card = f'''<div class="hp-card-wrap"><div class="hp-card">
  <div class="hp-card__top"><div><span class="hp-k">{I.s("hp.card.k")}</span><b class="hp-card__name">Kopi O Kaw 2in1 · 10 sachets</b></div><span class="hp-pill">{T("hp.card.steady")}</span></div>
  <div class="hp-card__chart"><span class="hp-card__today" data-i18n="hp.card.today">Today</span>{line_chart(300, 90)}<div class="hp-card__axis">{T("hp.card.past")}{T("hp.card.next")}</div></div>
  <div class="hp-card__check"><div><span class="hp-k2">{T("hp.card.pc")}</span><b>{T("hp.card.ok")}</b></div><span class="hp-dot">{T("hp.card.bal")}</span></div>
</div></div>'''

def stat(svg, num, key):
    return f'<div class="hp-stat"><span class="hp-stat__ic" aria-hidden="true">{ic(svg, 16)}</span><b>{num}</b><p data-i18n="{key}">{I.s(key)}</p></div>'
stats = (stat('<path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13"/>', "1.05B t", "hp.st1") +
         stat('<path d="M3 9h18l-1-5H4zM5 9v11h14V9M9 20v-6h6v6"/>', "12%", "hp.st2") +
         stat('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>', "2030", "hp.st3"))

steps = ""
plants = ["🌱", "🌿", "🪴", "🌳"]
files = ["StockLess-Step1-Upload.html", "StockLess-Step2-Mapping.html", "StockLess-Step3-Readiness.html", "StockLess-Step4-Purchases.html"]
for i in range(4):
    steps += f'<a class="hp-step" href="{files[i]}"><span class="hp-step__n">{i+1}</span><span class="hp-step__plant" aria-hidden="true">{plants[i]}</span><b data-i18n="hp.s{i+1}">{I.s(f"hp.s{i+1}")}</b><p data-i18n="hp.s{i+1}t">{I.s(f"hp.s{i+1}t")}</p></a>'

MARK = {"yes": ('hp-m--yes', ic('<path d="m5 12 4 4L19 6"/>', 14)),
        "mid": ('hp-m--mid', ic('<path d="M6 12h12"/>', 14)),
        "no": ('hp-m--no', ic('<path d="m7 7 10 10M17 7 7 17"/>', 14))}
cols = [("sheet", ic('<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M4 9h16M4 15h16M10 3v18"/>', 20)),
        ("erp", ic('<rect x="3" y="4" width="18" height="6" rx="1"/><rect x="3" y="14" width="18" height="6" rx="1"/><path d="M7 7h.01M7 17h.01"/>', 20)),
        ("sl", ic('<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10Z"/><path d="M2 21c0-3 1.9-5.4 5.1-6"/>', 20))]
diff = ""
for ci, (c, svg) in enumerate(cols):
    hl = " hp-col--sl" if c == "sl" else ""
    badge = f'<span class="hp-col__badge">{T("hp.c.best")}</span>' if c == "sl" else ""
    rows = ""
    for k, *_ in ROWS_DIFF:
        st = CELLS[k][ci][0]; cls, mk = MARK[st]
        rows += f'<li><span class="hp-m {cls}" aria-hidden="true">{mk}</span><span><small data-i18n="hp.r.{k}">{I.s("hp.r."+k)}</small><span data-i18n="hp.c.{k}.{ci}">{I.s(f"hp.c.{k}.{ci}")}</span></span></li>'
    diff += f'<article class="hp-col{hl}">{badge}<div class="hp-col__head"><span class="hp-col__ic">{svg}</span><div><h3 data-i18n="hp.c.{c}">{I.s("hp.c."+c)}</h3><p data-i18n="hp.c.{c}.t">{I.s("hp.c."+c+".t")}</p></div></div><ul>{rows}</ul></article>'

faq = ""
for i, (icn, *_r) in enumerate(FAQ):
    faq += f'<details class="hp-faq"><summary><span class="hp-faq__ic" aria-hidden="true">{icn}</span><span data-i18n="hp.q{i}">{I.s(f"hp.q{i}")}</span><span class="hp-faq__leaf" aria-hidden="true"></span></summary><p data-i18n="hp.a{i}">{I.s(f"hp.a{i}")}</p></details>'

lang = ('<label class="lang"><span class="sr-only">Language</span><select aria-label="Language">'
        '<option value="en" lang="en">English</option><option value="ms" lang="ms">Bahasa Melayu</option><option value="zh" lang="zh-Hans">中文</option></select></label>')

body = f'''
<header class="topbar">{LOGO}<span class="topbar__spacer"></span>
  <nav class="hp-nav" aria-label="Sections"><a href="#why">{T("hp.nav.why")}</a><a href="#how">{T("hp.nav.how")}</a><a href="#diff">{T("hp.nav.diff")}</a><a href="#example">{T("hp.nav.ex")}</a><a href="#faq">{T("hp.nav.faq")}</a></nav>
  {lang}
  <a class="btn btn--primary hp-topcta" href="{STEP1}">{T("hp.cta")}</a>
</header>
<main id="top">
<section class="hp-hero"><div class="wrap hp-hero__in">
  <div class="hp-hero__text">
    <p class="hp-eyebrow"><span aria-hidden="true">🌱</span> {T("hp.eyebrow")}</p>
    <h1>{T("hp.h1a")}<em data-i18n="hp.h1b">food waste.</em><br>{T("hp.h1c")}</h1>
    <p class="hp-lede">{T("hp.lede")}</p>
    <div class="hp-ctas"><a class="btn btn--primary hp-bigbtn" href="{STEP1}">{T("hp.cta")}</a><a class="hp-link" href="#how">{T("hp.see")}</a></div>
    <ul class="hp-checks"><li>{CHECK}{T("hp.chk1")}</li><li>{CHECK}{T("hp.chk2")}</li><li>{CHECK}{T("hp.chk3")}</li></ul>
  </div>
  {hero_card}
</div></section>

<section class="hp-big" id="why"><div class="wrap hp-big__in">
  <div>
    <p class="hp-k3">{T("hp.big.k")}</p>
    <h2>{T("hp.big.h")}</h2>
    <p class="hp-p">{T("hp.big.t")}</p>
    <div class="hp-stats">{stats}</div>
    <p class="hp-src">{T("hp.src")}</p>
  </div>
  <div class="hp-big__media">
    <img src="{IMG['waste']}" alt="{I.s('hp.img.waste')}" data-i18n-alt="hp.img.waste" width="900" height="600">
    <div class="hp-case"><span class="hp-case__k" data-i18n="hp.case.k">Case study</span><p><b>RM10,000</b> <span data-i18n="hp.case.t">{I.s("hp.case.t")}</span> <small data-i18n="hp.case.s">{I.s("hp.case.s")}</small></p></div>
  </div>
</div></section>

<section class="hp-how" id="how"><div class="wrap">
  <p class="hp-k3 hp-center">{T("hp.how.k")}</p>
  <h2 class="hp-center">{T("hp.how.h1")}<em data-i18n="hp.how.h2">confident order</em></h2>
  <div class="hp-steps">{steps}</div>
</div></section>

<section class="hp-diff" id="diff"><div class="wrap">
  <p class="hp-k3">{T("hp.diff.k")}</p>
  <h2>{T("hp.diff.h1")}<em data-i18n="hp.diff.h2">just what you need</em></h2>
  <p class="hp-p hp-diff__t">{T("hp.diff.t")}</p>
  <div class="hp-cols">{diff}</div>
</div></section>

<section class="hp-ex" id="example"><div class="wrap">
  <div class="hp-ex__head"><div><p class="hp-k3">{T("hp.ex.k")}</p><h2>{T("hp.ex.h")}</h2></div><p class="hp-ex__t">{T("hp.ex.t")}</p></div>
  <div class="hp-ex__grid">
    <div class="hp-panel">
      <div class="hp-ex__top"><div><span class="hp-k">Kopi O Kaw 2in1 · 10 sachets</span><b>{T("hp.ex.dem")}</b></div><div class="hp-ex__range"><small>{T("hp.ex.exp")}</small><b>7–28 <span data-i18n="hp.units">units</span></b></div></div>
      {line_chart(420, 170, True)}
      <div class="hp-ex__axis"><span>W1</span><span>W8 · <span data-i18n="hp.card.today">Today</span></span><span>F4</span></div>
      <ul class="hp-legend"><li><i class="hp-sw hp-sw--line"></i>{T("hp.lg.past")}</li><li><i class="hp-sw hp-sw--dash"></i>{T("hp.lg.exp")}</li><li><i class="hp-sw hp-sw--fan"></i>{T("hp.lg.range")}</li></ul>
    </div>
    <div class="hp-ex__side">
      <div class="hp-panel">
        <div class="hp-plan"><label for="hp-plan">{T("hp.ex.plan")}</label><b><span id="hp-plan-n">9</span> <small data-i18n="hp.units">units</small></b></div>
        <input id="hp-plan" type="range" min="0" max="40" value="9" class="hp-range">
        <div class="hp-scale"><span>0 <span data-i18n="hp.units">units</span></span><span>{T("hp.ex.sugg")}</span><span>40 <span data-i18n="hp.units">units</span></span></div>
        <div class="hp-nums"><div><small>{T("hp.ex.soh")}</small><b>7</b></div><div><small>{T("hp.ex.inc")}</small><b>2</b></div><div><small>{T("hp.ex.after")}</small><b id="hp-after">18</b></div></div>
      </div>
      <div class="hp-verdict" id="hp-verdict" aria-live="polite"><span class="hp-dot" id="hp-vk" data-i18n="hp.v.ok.k">Looks balanced</span><b id="hp-vh" data-i18n="hp.v.ok.h">This plan is within range.</b><p id="hp-vt"></p></div>
    </div>
  </div>
  <p class="hp-src">{T("hp.ex.note")}</p>
</div></section>

<section class="hp-get"><div class="wrap hp-get__in">
  <div>
    <p class="hp-k3">{T("hp.get.k")}</p>
    <h2>{T("hp.get.h1")}<em data-i18n="hp.get.h2">decide with confidence</em></h2>
    <ul class="hp-list">{"".join(f'<li>{CHECK}<span data-i18n="hp.g{i}">{I.s(f"hp.g{i}")}</span></li>' for i in range(1, 6))}</ul>
  </div>
  <div class="hp-priv">
    <span class="hp-priv__ic" aria-hidden="true">{ic('<rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>', 22)}</span>
    <p class="hp-k3">{T("hp.pv.k")}</p>
    <h3>{T("hp.pv.h")}</h3>
    <p class="hp-p">{T("hp.pv.t")}</p>
    <div class="hp-chips"><span data-i18n="hp.chk3">No uploads</span><span data-i18n="hp.chk2">No account needed</span><span data-i18n="hp.pv.c3">No tracking</span></div>
  </div>
</div></section>

<section class="wrap"><div class="hp-band">
  <div class="hp-band__text">
    <p class="hp-k3 hp-k3--light"><span aria-hidden="true">🌳</span> {T("hp.band.k")}</p>
    <h2>{T("hp.band.h1")}<em data-i18n="hp.band.h2">unlock more possibilities.</em></h2>
    <a class="hp-band__btn" href="{STEP1}">{T("hp.band.cta")}</a>
    <p>{T("hp.band.t")}</p>
  </div>
  <img src="{IMG['produce']}" alt="{I.s('hp.img.produce')}" data-i18n-alt="hp.img.produce" width="900" height="600">
</div></section>

<section class="wrap hp-sdg"><div class="hp-sdg__card">
  <div class="hp-sdg__top"><b>12</b><span data-i18n="hp.sdg.n">Responsible consumption and production</span></div>
  <svg viewBox="0 0 140 100" class="hp-sdg__icon" aria-hidden="true"><path d="M70 50C82 34 95 27 108 33C123 40 123 60 108 67C95 73 82 66 70 50C58 34 45 27 32 33C17 40 17 60 32 67C40 71 49 70 56 64" fill="none" stroke="#fff" stroke-width="11" stroke-linecap="round"/><path d="M47 58L60 60L56 73" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <p class="hp-sdg__cap" data-i18n="hp.sdg.cap">A shared goal. An everyday action.</p>
</div><div class="hp-sdg__text">
  <p class="hp-k3">{T("hp.sdg.k")}</p>
  <h2>{T("hp.sdg.h")}</h2>
  <p class="hp-sdg__lead">{T("hp.sdg.t1")}</p>
  <p class="hp-p">{T("hp.sdg.t2")}</p>
  <a class="hp-link" href="https://sdgs.un.org/goals/goal12" target="_blank" rel="noopener">{T("hp.sdg.link")}</a>
</div></section>

<section class="hp-lm" id="faq"><div class="wrap">
  <p class="hp-k3">{T("hp.lm.k")}</p>
  <h2>{T("hp.lm.h")}</h2>
  <p class="hp-p hp-lm__t">{T("hp.lm.t")}</p>
  <div class="hp-faqs">{faq}</div>
  <div class="hp-lm__foot"><b>{T("hp.lm.still")}</b><button type="button" class="hp-link" id="hp-all" aria-expanded="false" data-i18n="hp.lm.all">View all FAQs →</button></div>
</div></section>
</main>
<footer class="hp-foot"><div class="wrap hp-foot__in">{LOGO}<p>{T("hp.foot")}</p><a class="hp-link" href="#top">{T("hp.top")}</a></div></footer>
'''

page_css = r'''
html{scroll-behavior:smooth}
body{background:#fff}
.topbar{position:sticky;top:0;z-index:40}
.hp-nav{display:flex;gap:4px;margin-right:8px}
.hp-nav a{padding:8px 10px;border-radius:8px;font-family:var(--display);font-weight:700;font-size:var(--text-description);color:var(--ink);text-decoration:none}
.hp-nav a:hover{background:var(--teal-tint)}
.hp-topcta{min-height:40px;padding:0 16px;font-size:var(--text-description)}
.hp-k,.hp-k2{display:block;font-family:var(--display);font-weight:800;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.hp-k2{text-transform:none;letter-spacing:0;font-weight:400;font-family:var(--body);font-size:12px}
.hp-k3{margin:0 0 10px;font-family:var(--display);font-weight:800;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--teal-deep)}
.hp-k3--light{color:#CFEDE6}
.hp-center{text-align:center}
.hp-p{margin:0;font-size:var(--text-body);line-height:1.6;color:var(--muted)}
.hp-src{margin:18px 0 0;font-size:12px;color:var(--muted-2)}
h2{margin:0 0 12px;font-family:var(--display);font-size:34px;line-height:1.15;font-weight:700;letter-spacing:-.4px;color:var(--ink)}
h2 em,.hp-hero h1 em{font-style:normal;color:var(--teal)}
.hp-hero{background:#EEF6F2;border-bottom:1px solid #E1EEE8}
.hp-hero__in{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:48px;align-items:center;padding-top:72px;padding-bottom:72px}
.hp-eyebrow{margin:0 0 14px;font-family:var(--display);font-weight:800;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--teal-deep)}
.hp-hero h1{margin:0;font-family:var(--display);font-size:56px;line-height:1.05;letter-spacing:-1.2px;font-weight:700;color:var(--ink)}
.hp-hero h1 em{color:#9A6A1E}
.hp-lede{margin:22px 0 0;max-width:46ch;font-size:18px;line-height:1.6;color:var(--muted)}
.hp-ctas{display:flex;flex-wrap:wrap;align-items:center;gap:20px;margin-top:28px}
.hp-bigbtn{min-height:50px;padding:0 22px;font-size:16px;box-shadow:0 10px 24px rgba(17,101,94,.22)}
.hp-link{border:0;background:none;padding:0;font-family:var(--display);font-weight:700;font-size:var(--text-description);color:var(--teal-deep);text-decoration:none;cursor:pointer}
.hp-link:hover{text-decoration:underline}
.hp-checks{display:flex;flex-wrap:wrap;gap:10px 22px;margin:28px 0 0;padding:18px 0 0;list-style:none;border-top:1px solid #D6E8DF;font-size:var(--text-description);color:var(--ink-2)}
.hp-checks li{display:flex;align-items:center;gap:8px}
.hp-tick{flex:none;display:grid;place-items:center;width:20px;height:20px;border-radius:6px;background:var(--teal-deep);color:#fff}
.hp-card-wrap{padding:22px;border-radius:28px;background:#DCEDE6;border:1px solid #CFE4DE}
.hp-card{padding:20px;border-radius:20px;background:#fff;box-shadow:0 18px 40px rgba(22,49,59,.10)}
.hp-card__top{display:flex;justify-content:space-between;align-items:flex-start;gap:10px}
.hp-card__name{display:block;margin-top:4px;font-family:var(--display);font-size:17px}
.hp-pill{padding:4px 10px;border-radius:999px;background:var(--teal-tint);font-family:var(--display);font-weight:700;font-size:12px;color:var(--teal-deep);white-space:nowrap}
.hp-card__chart{position:relative;margin:12px 0 8px}
.hp-card__today{position:absolute;left:64%;top:0;font-size:10px;color:var(--muted)}
.hp-chart{display:block;width:100%;height:auto}
.hp-ax{font-family:var(--data);font-size:11px;fill:var(--muted)}
.hp-card__axis{display:flex;justify-content:space-around;font-size:10px;color:var(--muted)}
.hp-card__check{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:14px 16px;border-radius:14px;border:1.5px solid #9ED3C7;background:#F3FAF7}
.hp-card__check b{display:block;margin-top:2px;font-family:var(--display);font-size:15px}
.hp-dot{display:inline-flex;align-items:center;gap:6px;font-family:var(--display);font-weight:700;font-size:12px;color:var(--teal-deep);white-space:nowrap}
.hp-dot::before{content:"";width:8px;height:8px;border-radius:50%;background:currentColor}
.hp-big{background:#FDFCF6;border-bottom:1px solid #EFEBDD}
.hp-big__in{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:48px;align-items:start;padding-top:72px;padding-bottom:72px}
.hp-stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:28px}
.hp-stat{padding:18px;border-radius:16px;background:#fff;border:1px solid #EFD9A6}
.hp-stat__ic{display:grid;place-items:center;width:32px;height:32px;border-radius:9px;background:var(--amber-tint);color:var(--amber)}
.hp-stat b{display:block;margin-top:14px;font-family:var(--display);font-size:26px;font-weight:800}
.hp-stat p{margin:6px 0 0;font-size:13px;line-height:1.5;color:var(--muted)}
.hp-big__media img{display:block;width:100%;height:300px;object-fit:cover;border-radius:16px}
.hp-case{display:flex;gap:16px;margin-top:12px;padding:16px 18px;border-radius:14px;background:#fff;border:1px solid var(--line)}
.hp-case__k{flex:none;font-family:var(--display);font-weight:800;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--amber)}
.hp-case p{margin:0;font-size:13px;line-height:1.55;color:var(--ink-2)}
.hp-case small{color:var(--muted-2)}
.hp-how{padding:72px 0}
.hp-steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:34px}
.hp-step{position:relative;display:flex;flex-direction:column;gap:8px;padding:20px;border-radius:18px;background:#F2F8F5;border:1px solid #DDEBE5;color:var(--ink);text-decoration:none;transition:transform .2s,box-shadow .2s}
.hp-step:hover{transform:translateY(-2px);box-shadow:var(--shadow-card)}
.hp-step__n{display:grid;place-items:center;width:36px;height:36px;border-radius:50%;background:var(--teal-deep);color:#fff;font-family:var(--display);font-weight:800}
.hp-step__plant{position:absolute;top:20px;right:20px;font-size:22px}
.hp-step b{margin-top:10px;font-family:var(--display);font-size:16px}
.hp-step p{margin:0;font-size:13px;line-height:1.55;color:var(--muted)}
.hp-diff{padding:72px 0;background:#F7FAF8;border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft)}
.hp-diff__t{max-width:70ch}
.hp-cols{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:30px;align-items:stretch}
.hp-col{position:relative;padding:22px;border-radius:20px;background:#fff;border:1px solid var(--line)}
.hp-col--sl{border:2px solid var(--teal-deep);box-shadow:0 16px 36px rgba(17,101,94,.12)}
.hp-col__badge{position:absolute;top:-12px;right:18px;padding:4px 10px;border-radius:999px;background:var(--teal-deep);color:#fff;font-family:var(--display);font-weight:800;font-size:11px;letter-spacing:.06em;text-transform:uppercase}
.hp-col__head{display:flex;align-items:center;gap:12px;padding-bottom:14px;border-bottom:1px solid var(--line-soft)}
.hp-col__ic{flex:none;display:grid;place-items:center;width:42px;height:42px;border-radius:12px;background:var(--line-soft);color:var(--ink-2)}
.hp-col--sl .hp-col__ic{background:var(--teal-tint);color:var(--teal-deep)}
.hp-col h3{margin:0;font-family:var(--display);font-size:18px}
.hp-col__head p{margin:2px 0 0;font-size:13px;color:var(--muted)}
.hp-col ul{display:flex;flex-direction:column;gap:12px;margin:14px 0 0;padding:0;list-style:none}
.hp-col li{display:flex;gap:10px;align-items:flex-start;font-size:14px;line-height:1.45;color:var(--ink-2)}
.hp-col li small{display:block;font-family:var(--display);font-weight:800;font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.hp-m{flex:none;display:grid;place-items:center;width:22px;height:22px;margin-top:2px;border-radius:50%}
.hp-m--yes{background:var(--teal-tint);color:var(--teal-deep)}
.hp-m--mid{background:var(--amber-tint);color:var(--amber)}
.hp-m--no{background:var(--red-tint);color:var(--red)}
.hp-ex{padding:72px 0;background:#EEF6F2}
.hp-ex__head{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;margin-bottom:24px}
.hp-ex__head h2{margin:0}
.hp-ex__t{max-width:38ch;margin:0;font-size:13px;color:var(--muted)}
.hp-ex__grid{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:16px;align-items:start}
.hp-panel{padding:20px;border-radius:18px;background:#fff;border:1px solid var(--line)}
.hp-ex__top{display:flex;justify-content:space-between;gap:12px;margin-bottom:10px}
.hp-ex__top b{display:block;margin-top:4px;font-family:var(--display);font-size:17px}
.hp-ex__range{text-align:right}
.hp-ex__range small{display:block;font-size:12px;color:var(--teal-deep)}
.hp-ex__range b{font-family:var(--display);font-size:26px;color:var(--teal-deep)}
.hp-ex__range b span{font-size:14px}
.hp-ex__axis{display:flex;justify-content:space-between;padding:0 4px 0 34px;font-family:var(--data);font-size:11px;color:var(--muted)}
.hp-legend{display:flex;flex-wrap:wrap;gap:6px 18px;margin:14px 0 0;padding:0;list-style:none;font-size:12px;color:var(--muted)}
.hp-legend li{display:flex;align-items:center;gap:6px}
.hp-sw{display:inline-block;width:16px;height:3px;background:#16313B}
.hp-sw--dash{background:repeating-linear-gradient(90deg,#167D74 0 4px,transparent 4px 7px)}
.hp-sw--fan{height:10px;border-radius:3px;background:rgba(22,125,116,.2)}
.hp-ex__side{display:flex;flex-direction:column;gap:16px}
.hp-plan{display:flex;justify-content:space-between;align-items:baseline}
.hp-plan label{font-family:var(--display);font-weight:700;font-size:15px}
.hp-plan b{font-family:var(--display);font-size:24px}
.hp-plan small{font-size:13px;color:var(--muted)}
.hp-range{width:100%;margin:14px 0 6px;accent-color:var(--teal-deep);min-height:28px}
.hp-scale{display:flex;justify-content:space-between;padding-bottom:14px;border-bottom:1px solid var(--line-soft);font-size:11px;color:var(--muted)}
.hp-nums{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:14px}
.hp-nums small{display:block;font-size:12px;color:var(--muted)}
.hp-nums b{font-family:var(--data);font-size:16px}
.hp-verdict{display:flex;flex-direction:column;gap:6px;padding:20px;border-radius:18px;border:1.5px solid #9ED3C7;background:#E2F1EC}
.hp-verdict b{font-family:var(--display);font-size:19px}
.hp-verdict p{margin:0;font-size:14px;line-height:1.55;color:var(--ink-2)}
.hp-verdict.is-hi{background:var(--amber-tint);border-color:#F1DDB4}.hp-verdict.is-hi .hp-dot{color:var(--amber)}
.hp-verdict.is-lo{background:var(--red-tint);border-color:#F0CACA}.hp-verdict.is-lo .hp-dot{color:var(--red)}
.hp-get{padding:72px 0}
.hp-get__in{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:48px;align-items:start}
.hp-list{display:flex;flex-direction:column;gap:10px;margin:22px 0 0;padding:0;list-style:none}
.hp-list li{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:12px;border:1px solid var(--line);font-size:14px;color:var(--ink-2)}
.hp-priv{padding:28px;border-radius:22px;background:#F2F8F5;border:1px solid #DDEBE5}
.hp-priv__ic{display:grid;place-items:center;width:44px;height:44px;margin-bottom:16px;border-radius:12px;background:var(--teal-deep);color:#fff}
.hp-priv h3{margin:0 0 12px;font-family:var(--display);font-size:22px}
.hp-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
.hp-chips span{padding:7px 12px;border-radius:999px;background:#fff;border:1px solid var(--line);font-family:var(--display);font-weight:700;font-size:12px;color:var(--teal-deep)}
.hp-band{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);overflow:hidden;border-radius:22px;background:var(--teal-deep);margin-bottom:72px}
.hp-band__text{padding:48px 40px;color:#fff;align-self:center}
.hp-band h2{color:#fff}.hp-band h2 em{color:#F6D58C}
.hp-band__btn{display:inline-flex;align-items:center;min-height:46px;padding:0 18px;border-radius:10px;background:#fff;color:var(--teal-deep);font-family:var(--display);font-weight:700;text-decoration:none}
.hp-band__text p:last-child{margin:14px 0 0;font-size:13px;color:#CFEDE6}
.hp-band img{display:block;width:100%;height:100%;min-height:300px;object-fit:cover}
.hp-lm{position:relative;padding:72px 0 56px;background:linear-gradient(180deg,#FCFDF9 0%,#EEF6EE 45%,#C9E5D0 100%);overflow:hidden}
.hp-lm::before{content:"";position:absolute;left:-10%;right:-10%;top:90px;height:260px;border-radius:50%;background:rgba(201,229,208,.45);pointer-events:none}
.hp-lm .wrap{position:relative}
.hp-lm h2{font-size:40px}
.hp-lm__t{max-width:52ch;font-size:18px}
.hp-faqs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:30px;align-items:start}
.hp-faq{border-radius:20px;background:rgba(233,243,239,.92);border:1px solid #DCEAE4}
.hp-faq summary{position:relative;display:flex;align-items:center;gap:14px;min-height:92px;padding:16px 56px 16px 22px;cursor:pointer;list-style:none;font-family:var(--display);font-weight:700;font-size:18px;color:var(--ink)}
.hp-faq summary::-webkit-details-marker{display:none}
.hp-faq__ic{font-size:24px}
.hp-faq__leaf{position:absolute;right:20px;bottom:18px;width:16px;height:16px;border-radius:0 100% 0 100%;background:#8FD2C8;transform:rotate(-10deg);transition:transform .2s}
.hp-faq[open] .hp-faq__leaf{transform:rotate(80deg)}
.hp-faq p{margin:0;padding:0 22px 20px 60px;font-size:15px;line-height:1.6;color:var(--ink-2)}
.hp-lm__foot{display:flex;justify-content:space-between;align-items:center;margin-top:28px;padding-top:22px;border-top:1px solid rgba(22,49,59,.1)}
.hp-lm__foot b{font-family:var(--display)}
.hp-lm__foot .hp-link{font-size:15px}
.hp-foot{border-top:1px solid var(--line-soft)}
.hp-foot__in{display:flex;justify-content:space-between;align-items:center;gap:16px;padding-top:18px;padding-bottom:18px}
.hp-foot__in p{margin:0;font-size:12px;color:var(--muted)}
.hp-foot .brand__logo{height:26px!important}
.hp-sdg{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:48px;align-items:center;margin-bottom:72px}
.hp-sdg__card{position:relative;display:flex;flex-direction:column;justify-content:space-between;min-height:340px;padding:24px;border-radius:22px;background:#BF8B2E;color:#fff}
.hp-sdg__top{display:flex;align-items:flex-start;gap:14px}
.hp-sdg__top b{font-family:var(--display);font-size:56px;line-height:.9;font-weight:800}
.hp-sdg__top span{max-width:22ch;font-family:var(--display);font-weight:800;font-size:12px;letter-spacing:.1em;text-transform:uppercase;line-height:1.35}
.hp-sdg__icon{display:block;width:62%;max-width:280px;margin:18px auto}
.hp-sdg__cap{margin:0;font-family:var(--display);font-weight:700;font-size:15px}
.hp-sdg__lead{margin:0 0 12px;font-size:18px;line-height:1.55;color:var(--ink)}
.hp-sdg__text .hp-p{margin-bottom:16px}
@media(max-width:960px){.hp-sdg{grid-template-columns:minmax(0,1fr);gap:24px}.hp-sdg__card{min-height:280px}}
@media(max-width:1100px){.hp-nav{display:none}}
@media(max-width:960px){
  .hp-hero__in,.hp-big__in,.hp-get__in,.hp-ex__grid,.hp-band{grid-template-columns:minmax(0,1fr)}
  .hp-steps{grid-template-columns:repeat(2,minmax(0,1fr))}
  .hp-cols{grid-template-columns:minmax(0,1fr)}
  .hp-col--sl{order:-1}
  .hp-ex__head{flex-direction:column;align-items:flex-start}
}
@media(max-width:700px){
  .hp-topcta{display:none}
  .hp-hero h1{font-size:38px}
  h2,.hp-lm h2{font-size:28px}
  .hp-hero__in,.hp-big__in{padding-top:44px;padding-bottom:44px}
  .hp-stats{grid-template-columns:minmax(0,1fr)}
  .hp-steps,.hp-faqs{grid-template-columns:minmax(0,1fr)}
  .hp-how,.hp-diff,.hp-ex,.hp-get,.hp-lm{padding-top:48px;padding-bottom:48px}
  .hp-band__text{padding:32px 24px}
  .hp-faq summary{min-height:72px;font-size:16px}
  .hp-faq p{padding-left:22px}
  .hp-foot__in{flex-direction:column;align-items:flex-start}
  .hp-case{flex-direction:column;gap:6px}
}
'''

js = r'''
(function () {
  var r = document.getElementById('hp-plan'), n = document.getElementById('hp-plan-n'), after = document.getElementById('hp-after');
  var box = document.getElementById('hp-verdict'), vk = document.getElementById('hp-vk'), vh = document.getElementById('hp-vh'), vt = document.getElementById('hp-vt');
  function upd() {
    var o = +r.value, tot = 7 + 2 + o, k = tot > 28 ? 'hi' : tot < 7 ? 'lo' : 'ok';
    n.textContent = o; after.textContent = tot;
    box.className = 'hp-verdict' + (k === 'ok' ? '' : ' is-' + k);
    vk.setAttribute('data-i18n', 'hp.v.' + k + '.k'); vh.setAttribute('data-i18n', 'hp.v.' + k + '.h');
    vk.textContent = t('hp.v.' + k + '.k'); vh.textContent = t('hp.v.' + k + '.h');
    vt.textContent = t('hp.v.' + k + '.t').replace('{n}', tot);
  }
  r.addEventListener('input', upd); document.addEventListener('langchange', upd);
  var all = document.getElementById('hp-all');
  all.addEventListener('click', function () {
    var open = all.getAttribute('aria-expanded') !== 'true';
    document.querySelectorAll('.hp-faq').forEach(function (d) { d.open = open; });
    all.setAttribute('aria-expanded', String(open));
    all.setAttribute('data-i18n', open ? 'hp.lm.less' : 'hp.lm.all'); all.textContent = t(open ? 'hp.lm.less' : 'hp.lm.all');
  });
  function alts() { document.querySelectorAll('[data-i18n-alt]').forEach(function (el) { el.setAttribute('alt', t(el.getAttribute('data-i18n-alt'))); }); }
  document.addEventListener('langchange', alts);
  upd();
})();
'''

out = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>StockLess | Less food waste. Smarter restocking.</title>
<meta name="description" content="Smarter restocking for small retailers. Reduce excess stock, control costs, and help prevent food waste.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=Inter:wght@400;600;700&family=Noto+Sans+SC:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}{page_css}
h1,h2,h3,h4,th,label,legend,summary,dt,b,strong,.btn{{font-family:var(--display);font-weight:700}}
p,li,dd,td,small,input,select,textarea{{font-family:var(--body)}}
html[lang^="zh"] h1,html[lang^="zh"] h2,html[lang^="zh"] h3,html[lang^="zh"] b,html[lang^="zh"] strong,html[lang^="zh"] label,html[lang^="zh"] .btn,html[lang^="zh"] summary{{font-family:var(--display),"Noto Sans SC",sans-serif}}
</style></head>
<body>{body}
<script>
(function () {{
  var D = {I.js()};
  var HL = {{ en: 'en', ms: 'ms', zh: 'zh-Hans' }};
  var sel = document.querySelector('.lang select');
  window.t = function (k) {{ var l = sel.value; return (D[l] && D[l][k]) || D.en[k] || k; }};
  function apply(l) {{
    document.documentElement.lang = HL[l] || 'en';
    document.querySelectorAll('[data-i18n]').forEach(function (el) {{ var v = D[l][el.getAttribute('data-i18n')]; if (v) el.textContent = v; }});
    document.dispatchEvent(new CustomEvent('langchange', {{ detail: l }}));
  }}
  var saved = 'en'; try {{ saved = localStorage.getItem('stockless.lang') || 'en'; }} catch (e) {{}}
  if (!D[saved]) saved = 'en';
  sel.value = saved;
  sel.addEventListener('change', function () {{ try {{ localStorage.setItem('stockless.lang', sel.value); }} catch (e) {{}} apply(sel.value); }});
  window.addEventListener('DOMContentLoaded', function () {{ apply(sel.value); }});
}})();
</script>
<script>{js}</script>
</body></html>'''
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", "StockLess-Homepage.html"), "w").write(out)
print("home", len(out))
