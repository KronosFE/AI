# -*- coding: utf-8 -*-
"""
Kronos AI · ML · Quantum Library — static-site generator (build_ai.py).
Generator-driven like the Technical Library: content_*.py modules register pages;
this engine renders them on-brand (dark navy), with SEO/AI metadata, seamless R2
clips, and interactive quantum-circuit / Bloch / matrix / truth-table widgets.

Rebuild:  python3 build_ai.py
Extend:   drop a content_<name>.py exposing register(add) -> appends page dicts.

RULES (enforced by verify()): no economics ($/LCOE/valuation), honest gates kept,
function-first naming, frozen canon only.
"""
import os, re, json, html, importlib, glob, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://kronosfusionenergy.com"
BASE = SITE + "/ai"
CLIPS_BASE = "https://pub-6f4141e515994eaf98b678a16ccbf603.r2.dev/"
BUILD_DATE = "2026-08-15"

# ---- frozen canon (PUBLIC, no economics) ------------------------------------
F = {
    "control_layers": 8,            # Kronos AI control stack layers
    "reflex_latency": "microsecond",# L1 deterministic reflex
    "surrogate_speedup": "10^6-10^9",# surrogate vs first-principles (order-of-magnitude)
    "twin": "predictive digital twin",
    "he3_qc": "helium-3 dilution refrigeration reaches millikelvin for superconducting & spin qubits",
    "q_sci": "3.424", "p_fus": "88.7 MW", "f_n": "5.44%",
}

# ---- categories (id -> (title, blurb)) --------------------------------------
# Ordered as the founder's narrative arc:
# AI → logic/future-logic → fusion codes → AI algorithms → machine learning
# → control brain → digital twins (both machines) → the quantum computer.
CATS = {
 # 1. AI — the intelligence layer
 "foundations":        ("AI & Foundations", "What the intelligence layer is, and the math and information theory under it."),
 # 2. Logic → future logic
 "logic-gates":        ("Classical Logic Gates", "AND, OR, NOT, XOR — the classical logic the quantum gates generalize."),
 "digital-logic":      ("Digital Logic & Circuits", "Adders, multiplexers, flip-flops, registers — logic assembled into computers."),
 "number-systems":     ("Number Systems & Information", "Binary, floating point, encoding, and information theory."),
 "complexity-theory":  ("Complexity & Computation", "What is computable, and how hard — P, NP, and the limits of algorithms."),
 "quantum-gates":      ("Quantum Logic Gates", "Future logic: every gate, its matrix, circuit symbol, table, and an interactive circuit."),
 # 3. Fusion codes — the real Kronos code
 "fusion-codes":       ("Fusion Codes", "The real Kronos simulation and control code — solvers, surrogates, and the plasma-control loop."),
 # 4. AI algorithms
 "ai-algorithms":      ("AI Algorithms", "Search, optimization, and planning algorithms behind intelligent systems."),
 "quantum-algorithms": ("Quantum Algorithms", "Gate-level walkthroughs — Grover, Shor, QFT, phase estimation, VQE, QAOA and more."),
 # 5. Machine learning
 "machine-learning":   ("Machine Learning", "Architectures, training, and the theory behind them."),
 "neural-architectures": ("Neural Architectures", "MLPs to transformers, GNNs, and diffusion models."),
 "reinforcement-learning": ("Reinforcement Learning", "Value, policy, and actor-critic methods for control."),
 # 6. The control brain
 "control-theory":     ("Control Theory", "PID, LQR, MPC, Kalman filtering, and state-space control."),
 "plasma-control":     ("AI Plasma Control", "How the Kronos control stack holds a fusion plasma in real time."),
 "surrogates-uq":      ("Surrogates & Uncertainty", "Fast surrogate models, uncertainty quantification, and validation."),
 # 7. Digital twins — BOTH machines
 "digital-twins":      ("3D Model & Digital Twin", "The interactive 3D model of both machines today — the seed that evolves into a live predictive digital twin of the breeder (Hyperion) and the burner (Aegis / MetroVolt)."),
 # 8. The quantum computer
 "quantum-foundations":("Quantum Foundations", "Qubits, superposition, entanglement, measurement, and the no-cloning theorem."),
 "quantum-simulation": ("Quantum Simulation", "Hamiltonian simulation, Trotterization, and simulating plasma & materials."),
 "quantum-error-correction": ("Quantum Error Correction", "Stabilizer codes, surface codes, syndromes, and fault tolerance."),
 "he3-quantum":        ("Helium-3 for Quantum Computing", "Dilution refrigeration, qubit modalities, and the isotope-demand case."),
 "hpc-compute":        ("HPC & Compute", "The compute substrate behind simulation and training."),
 "security-privacy":   ("Security & Safety-Critical Computing", "Cybersecurity, OT/ICS security, and post-quantum cryptography for a fusion plant."),
 "visualization":      ("Visualization & Interfaces", "Scientific visualization, dashboards, and the human interfaces to the machine."),
 # applied
 "applications":       ("Applications", "What all this computing does for Kronos — design, control, operations, and the isotope-and-quantum flywheel."),
 "worked-examples":    ("Worked Examples", "End-to-end, step-by-step examples with code — from a Bell state to solving Grad-Shafranov."),
 # reference
 "glossary":           ("Glossary", "Concise definitions across AI, ML, and quantum computing."),
}
CAT_ORDER = list(CATS.keys())

# ---- design -----------------------------------------------------------------
STYLE = """
:root{--bg:#232C39;--panel:#28323f;--text:#E7EBF2;--mut:#8FA0B8;--gold:#D4AD5C;--gold2:#E2C57E;
--line:rgba(231,235,242,.11);--line2:rgba(231,235,242,.2);--good:#7FB08A;--warn:#D4A05C;
--serif:"Newsreader",Charter,Georgia,serif;--sans:"Space Grotesk",system-ui,-apple-system,Arial,sans-serif;--mono:"Space Mono",ui-monospace,Menlo,monospace}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font:16.5px/1.72 var(--sans);-webkit-font-smoothing:antialiased}
a{color:var(--gold);text-decoration:none}p a,li a{border-bottom:1px solid rgba(212,173,92,.32)}a:hover{color:var(--gold2)}
.sitebar{background:#1d2530;display:flex;flex-wrap:wrap;gap:8px 18px;align-items:center;justify-content:space-between;padding:11px 22px;position:sticky;top:0;z-index:20;border-bottom:1px solid var(--line)}
.sitebar a{color:#e8ebef;font-size:13px}.sitebar .sb-home{font-weight:700;letter-spacing:.11em;color:#fff;font-size:12.5px}
.sitebar .sb-links{display:flex;flex-wrap:wrap;gap:15px}.sitebar a:hover{color:var(--gold)}
.wrap{max-width:860px;margin:0 auto;padding:0 24px}
.page{padding:22px 0 72px}
.layout{display:grid;grid-template-columns:250px 1fr;gap:34px;max-width:1240px;margin:0 auto;padding:0 24px}
.side{border-right:1px solid var(--line);padding:24px 18px 60px 0;position:sticky;top:52px;height:calc(100vh - 52px);overflow-y:auto;font-size:13.5px}
.side a{display:block;text-decoration:none}
.side .sbtitle{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);padding:0 0 10px;border-bottom:1px solid var(--line2);margin-bottom:4px}
.side .sec{color:#c3cddb;font-size:13px;padding:6px 0;border-bottom:1px solid var(--line)}
.side .sec .cn{float:right;color:var(--mut);font-family:var(--mono);font-size:10px}
.side .sec:hover{color:#fff}.side .sec.on{color:var(--gold);font-weight:600}
.side .pg{color:var(--mut);font-size:12.5px;padding:3px 0 3px 12px;border-left:1px solid var(--line);margin-left:2px}
.side .pg:hover{color:var(--gold)}
.main{padding:26px 0 70px;min-width:0}
.crumb{font-family:var(--mono);color:var(--mut);font-size:12px;margin:12px 0 18px}
.kicker{font-family:var(--mono);color:var(--gold);font-size:11px;letter-spacing:.18em;text-transform:uppercase}
h1{font-family:var(--serif);font-weight:500;font-size:clamp(2rem,4.2vw,2.7rem);line-height:1.1;margin:.4rem 0 0;letter-spacing:-.015em}
h2{font-family:var(--serif);font-weight:500;font-size:1.5rem;margin:2.4rem 0 .7rem}
h3{font-size:1.05rem;margin:1.6rem 0 .5rem;color:var(--gold2)}
.lede{font-family:var(--serif);font-style:italic;font-size:1.3rem;line-height:1.5;color:#C4CEDC;margin:1rem 0 0}
p{margin:0 0 1.05rem}ul,ol{padding-left:1.15rem}li{margin:.34rem 0}
.kf{margin:1.7rem 0;border-top:1px solid var(--line)}
.kf .row{display:grid;grid-template-columns:minmax(130px,32%) 1fr;gap:16px;padding:10px 0;border-bottom:1px solid var(--line)}
.kf dt{font-family:var(--mono);font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:var(--mut)}
.kf dd{margin:0;font-size:15px}
.gate{margin:1.8rem 0;padding:1px 0 1px 20px;border-left:2px solid var(--gold);color:#C4CEDC;font-size:15px}
.gate b{display:block;font-family:var(--mono);font-weight:400;font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin-bottom:5px}
.related{margin:3rem 0 0;padding-top:1.4rem;border-top:1px solid var(--line2)}
.related h3{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--mut);margin:0 0 .3rem}
.related a{display:inline-block;margin:5px 14px 5px 0;color:var(--text)}
footer{border-top:1px solid var(--line);margin-top:3rem}
footer .wrap{padding:24px;color:var(--mut);font-size:12.5px;line-height:1.7}
/* code */
pre{background:#171e28;border:1px solid var(--line);border-left:3px solid var(--gold);border-radius:6px;padding:15px 17px;overflow-x:auto;font:13px/1.6 var(--mono);color:#d7deea;position:relative}
pre .cp{position:absolute;top:7px;right:9px;font-size:10px;color:var(--mut);cursor:pointer;font-family:var(--mono)}
code{font-family:var(--mono);font-size:.92em;color:var(--gold2)}
.lang{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut);margin:0 0 4px}
/* matrix */
.matrix{display:inline-grid;gap:2px 14px;background:linear-gradient(#0000,#0000) padding-box;border-left:2px solid var(--gold2);border-right:2px solid var(--gold2);padding:8px 14px;margin:12px 0;font-family:var(--mono);font-size:14px;text-align:center;vertical-align:middle}
.mxt{font-family:var(--mono);color:var(--gold);font-size:12px;margin:12px 0 2px}
/* truth table */
table.tt{border-collapse:collapse;margin:14px 0;font-family:var(--mono);font-size:13px}
table.tt th{color:var(--gold);font-weight:400;text-align:left;border-bottom:1px solid var(--line2);padding:6px 16px 6px 0}
table.tt td{padding:5px 16px 5px 0;border-bottom:1px solid var(--line);color:#cdd6e2}
/* circuit */
.circuit{margin:16px 0;padding:14px;background:#1b232e;border:1px solid var(--line);border-radius:8px;overflow-x:auto}
.circuit svg{display:block}
.qwire{stroke:#5b6a80;stroke-width:2}
.gbox{fill:#2c3745;stroke:var(--gold);stroke-width:1.5;rx:4}
.glabel{fill:var(--gold2);font-family:'Space Mono',monospace;font-size:15px;font-weight:700;text-anchor:middle;dominant-baseline:central}
.qlabel{fill:var(--mut);font-family:'Space Mono',monospace;font-size:12px;dominant-baseline:central}
.ctrl{fill:var(--gold)}.cline{stroke:var(--gold);stroke-width:2}
.chip{display:inline-block;font-family:var(--mono);font-size:11px;color:var(--mut);border:1px solid var(--line2);border-radius:20px;padding:2px 10px;margin:2px 4px 2px 0}
/* bloch */
.bloch{margin:12px 0}
/* seamless clip */
.clip{margin:26px 0 30px}
.clip video{width:100%;height:auto;display:block;border:0;border-radius:0;box-shadow:none;background:transparent;
-webkit-mask-image:radial-gradient(140% 132% at 50% 47%,#000 74%,transparent 100%);mask-image:radial-gradient(140% 132% at 50% 47%,#000 74%,transparent 100%)}
.clip figcaption{font-family:var(--serif);font-style:italic;color:var(--mut);font-size:.9rem;margin-top:.5rem;text-align:center;opacity:.85}
/* index */
.hero{padding:46px 0 10px;border-bottom:1px solid var(--line)}
.catgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin:26px 0}
.catcard{display:block;background:var(--panel);border:1px solid var(--line);border-top:2px solid var(--gold);border-radius:8px;padding:16px 18px;color:var(--text)}
.catcard:hover{border-color:var(--gold)}.catcard .ct{font-family:var(--mono);font-size:10px;letter-spacing:.12em;color:var(--gold);text-transform:uppercase}
.catcard h3{margin:.3rem 0 .3rem;color:var(--text)}.catcard p{color:var(--mut);font-size:13.5px;margin:0}
.catcard .n{font-family:var(--mono);font-size:11px;color:var(--mut);margin-top:8px}
@media(max-width:820px){.layout{grid-template-columns:1fr}.side{display:none}}
"""

SCRIPT = r"""
<script>
// copy code
document.querySelectorAll('pre').forEach(function(p){var b=document.createElement('span');b.className='cp';b.textContent='copy';
b.onclick=function(){navigator.clipboard.writeText(p.querySelector('code').innerText);b.textContent='copied';setTimeout(function(){b.textContent='copy';},1200);};p.appendChild(b);});
// interactive circuit: read JSON from data-spec, draw SVG
function drawCircuit(el){
 var spec; try{spec=JSON.parse(el.getAttribute('data-spec'));}catch(e){return;}
 var q=spec.qubits||1, cols=spec.cols||[], W=70, H=54, x0=54, y0=26;
 var w=x0+Math.max(cols.length,1)*W+24, h=y0+q*H+10;
 var s='<svg viewBox="0 0 '+w+' '+h+'" width="'+w+'" height="'+h+'" xmlns="http://www.w3.org/2000/svg">';
 for(var i=0;i<q;i++){var y=y0+i*H;s+='<text class="qlabel" x="6" y="'+y+'">q'+i+'</text>';
   s+='<line class="qwire" x1="40" y1="'+y+'" x2="'+(w-8)+'" y2="'+y+'"/>';}
 cols.forEach(function(col,ci){var cx=x0+ci*W+W/2;
   col.forEach(function(g){
     if(g.c!=null){ // controlled
       var yc=y0+g.c*H, yt=y0+g.t*H;
       s+='<line class="cline" x1="'+cx+'" y1="'+yc+'" x2="'+cx+'" y2="'+yt+'"/>';
       s+='<circle class="ctrl" cx="'+cx+'" cy="'+yc+'" r="5"/>';
       if(g.g==='X'||g.g==='+'){s+='<circle cx="'+cx+'" cy="'+yt+'" r="13" fill="#2c3745" stroke="var(--gold)" stroke-width="1.5"/><line class="cline" x1="'+(cx-13)+'" y1="'+yt+'" x2="'+(cx+13)+'" y2="'+yt+'"/><line class="cline" x1="'+cx+'" y1="'+(yt-13)+'" x2="'+cx+'" y2="'+(yt+13)+'"/>';}
       else{s+='<rect class="gbox" x="'+(cx-16)+'" y="'+(yt-16)+'" width="32" height="32" rx="4"/><text class="glabel" x="'+cx+'" y="'+yt+'">'+g.g+'</text>';}
     } else {var y=y0+g.t*H; s+='<rect class="gbox" x="'+(cx-16)+'" y="'+(y-16)+'" width="32" height="32" rx="4"/><text class="glabel" x="'+cx+'" y="'+y+'">'+g.g+'</text>';}
   });});
 s+='</svg>'; el.innerHTML=s;
}
document.querySelectorAll('.circuit[data-spec]').forEach(drawCircuit);
// lazy clips
var io=new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target;if(e.isIntersecting){if(!v.src&&v.dataset.src){v.src=v.dataset.src;v.addEventListener('canplay',function(){v.play().catch(function(){});},{once:true});}v.play&&v.play().catch(function(){});}else{v.pause&&v.pause();}});},{rootMargin:'300px'});
document.querySelectorAll('.clip video').forEach(function(v){io.observe(v);});
</script>
"""

NAV = ('<nav class="sitebar"><a class="sb-home" href="%s/">KRONOS &middot; FUSION ENERGY</a>'
 '<span class="sb-links"><a href="%s/">Home</a><a href="%s/learn/">Learn</a>'
 '<a href="%s/technical/">Technical</a><a href="%s/ai/">AI&nbsp;&middot;&nbsp;Quantum</a>'
 '<a href="%s/whitepapers">Whitepapers</a><a href="%s/publications">Publications</a>'
 '<a href="%s/3D_Model">3D&nbsp;Model</a></span></nav>') % ((SITE,)*8)

FOOTER = ('<footer><div class="wrap">&copy; 2026 Kronos Fusion Energy, Inc. &middot; Los Angeles, California &middot; '
 '<a href="%s">kronosfusionenergy.com</a> &middot; AI &middot; ML &middot; Quantum Library &middot; '
 'content CC BY 4.0 &middot; code Apache-2.0 &middot; Correspondence: p.ford@kronosfusionenergy.com<br>'
 'Educational reference. Design figures are computed, reproducible targets — not measurements. Nothing here is an offer of securities.</div></footer>') % SITE

# ---- rendering helpers ------------------------------------------------------
def esc(s): return html.escape(str(s))

def render_matrix(title, rows):
    cols = len(rows[0])
    cells = "".join(f'<span style="grid-column:{c+1};grid-row:{r+1}">{esc(v)}</span>'
                    for r,row in enumerate(rows) for c,v in enumerate(row))
    t = f'<div class="mxt">{esc(title)}</div>' if title else ""
    return f'{t}<div class="matrix" style="grid-template-columns:repeat({cols},auto)">{cells}</div>'

def render_truth(headers, rows):
    h = "".join(f"<th>{esc(x)}</th>" for x in headers)
    b = "".join("<tr>"+"".join(f"<td>{esc(c)}</td>" for c in r)+"</tr>" for r in rows)
    return f'<table class="tt"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'

def render_circuit(spec):
    return f'<div class="circuit" data-spec=\'{json.dumps(spec)}\'></div>'

def render_code(lang, code):
    return f'<div class="lang">{esc(lang)}</div><pre><code>{esc(code)}</code></pre>'

def render_clip(clip):
    cap = "Kronos motion — " + re.sub(r"^[a-z]+[0-9]*-","",re.sub(r"\.mp4$","",clip)).replace("-"," ")
    return (f'<figure class="clip"><video autoplay muted loop playsinline preload="none" '
            f'aria-label="{esc(cap)}"><source data-src="{CLIPS_BASE}{clip}" type="video/mp4"></video>'
            f'<figcaption>{esc(cap)}</figcaption></figure>')

def render_body(body):
    out=[]
    for item in body:
        if not (isinstance(item,(list,tuple)) and len(item)>=2): continue
        kind,val=item[0],item[1]
        if kind=="h2": out.append(f"<h2>{esc(val)}</h2>")
        elif kind=="h3": out.append(f"<h3>{esc(val)}</h3>")
        elif kind=="p": out.append(f"<p>{val}</p>")
        elif kind=="html": out.append(val)
        elif kind=="ul": out.append("<ul>"+"".join(f"<li>{x}</li>" for x in val)+"</ul>")
        elif kind=="code": out.append(render_code(*val))
        elif kind=="matrix": out.append(render_matrix(*val))
        elif kind=="truth": out.append(render_truth(*val))
        elif kind=="circuit": out.append(render_circuit(val))
        elif kind=="clip": out.append(render_clip(val))
    return "\n".join(out)

def jsonld(p):
    typ = p.get("seo_type","TechArticle")
    d = {"@context":"https://schema.org","@type":typ,
         "name" if typ=="DefinedTerm" else "headline": p["title"],
         "description": p["lede"], "url": f'{BASE}/{p["slug"]}.html',
         "publisher":{"@type":"Organization","name":"Kronos Fusion Energy"}}
    if typ=="DefinedTerm":
        d["inDefinedTermSet"]={"@type":"DefinedTermSet","name":"Kronos AI · Quantum Library","url":BASE}
    return '<script type="application/ld+json">'+json.dumps(d)+'</script>'

def page_html(p, sidebar):
    facts = ""
    if p.get("facts"):
        rows="".join(f'<div class="row"><dt>{esc(k)}</dt><dd>{v}</dd></div>' for k,v in p["facts"])
        facts=f'<dl class="kf">{rows}</dl>'
    gate = f'<div class="gate"><b>Honest gate</b>{p["gate"]}</div>' if p.get("gate") else ""
    rel=""
    if p.get("related"):
        rel='<div class="related"><h3>Related</h3>'+"".join(f'<a href="./{h}.html">{esc(l)} &rarr;</a>' for h,l in p["related"])+'</div>'
    catname = CATS[p["cat"]][0]
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
      f'<meta name="viewport" content="width=device-width,initial-scale=1">'
      f'<title>{esc(p["title"])} · Kronos AI · Quantum</title>'
      f'<meta name="description" content="{esc(p["lede"])}">'
      f'<link rel="canonical" href="{BASE}/{p["slug"]}.html">'
      f'<meta name="robots" content="index,follow,max-image-preview:large">'
      f'<meta property="og:title" content="{esc(p["title"])}"><meta property="og:type" content="article">'
      f'<meta property="og:description" content="{esc(p["lede"])}">'
      f'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
      f'<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Space+Grotesk:wght@400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">'
      f'{jsonld(p)}<style>{STYLE}</style></head><body>{NAV}'
      f'<div class="layout"><aside class="side">{sidebar}</aside><main class="main">'
      f'<div class="crumb"><a href="./index.html">Computing Library</a> &rsaquo; {esc(catname)}</div>'
      f'<div class="kicker">{esc(catname)}</div><h1>{esc(p["title"])}</h1>'
      f'<p class="lede">{esc(p["lede"])}</p>{facts}{render_body(p["body"])}{gate}{rel}'
      f'</main></div>{FOOTER}{SCRIPT}</body></html>')

def sidebar_for(pages, active_cat):
    # section list for the whole library; the ACTIVE section's pages expand beneath it
    by={}
    for p in pages: by.setdefault(p["cat"],[]).append(p)
    out=['<a class="sbtitle" href="./index.html">Computing Library</a>']
    for c in CAT_ORDER:
        ps=by.get(c)
        if not ps: continue
        first=sorted(ps,key=lambda x:x["title"])[0]["slug"]
        on=" on" if c==active_cat else ""
        out.append(f'<a class="sec{on}" href="./{first}.html">{esc(CATS[c][0])}<span class="cn">{len(ps)}</span></a>')
        if c==active_cat:
            for p in sorted(ps,key=lambda x:x["title"]):
                out.append(f'<a class="pg" href="./{p["slug"]}.html">{esc(p["title"])}</a>')
    return "".join(out)

# ---- collect content --------------------------------------------------------
def collect():
    pages=[]
    seen=set()
    for mod in sorted(glob.glob(os.path.join(HERE,"content_*.py"))):
        name=os.path.splitext(os.path.basename(mod))[0]
        m=importlib.import_module(name)
        def add(p):
            if not p.get("slug") or not p.get("title") or not p.get("cat"): return
            if p["slug"] in seen: return             # skip dup slugs (multi-agent safety)
            if len(p.get("body",[]))<2: return       # skip thin pages
            c=p["cat"]
            if c not in CATS:                        # auto-register categories from any wave
                CATS[c]=(c.replace("-"," ").title(),"")
                CAT_ORDER.append(c)
            seen.add(p["slug"]); pages.append(p)
        m.register(add, F)
    return pages

def verify(pages):
    bad=[]
    econ=re.compile(r"\$[0-9]|\bLCOE\b|\bvaluation\b|\bEBITDA\b|per MWh|/MWh|\bcapex\b", re.I)
    for p in pages:
        blob=p["title"]+p["lede"]+json.dumps(p["body"])
        if econ.search(blob): bad.append(("economics",p["slug"]))
        if len(p["body"])<2: bad.append(("thin",p["slug"]))
    return bad

def inject_clips(pages):
    """Attach a seamless, topic-matched R2 clip (from the 506-clip library) to each
    non-glossary page that doesn't already have one. Keyword match on title+lede+category."""
    smp=os.path.join(HERE,"..","_clip_slug_map.json")
    if not os.path.exists(smp): return 0
    try: slugs=sorted(set(json.load(open(smp,encoding="utf-8")).values()))
    except Exception: return 0
    def toks(s): return set(w for w in re.split(r"[^a-z0-9]+",s.lower()) if len(w)>=4)
    idx={c:toks(re.sub(r"^[a-z]+[0-9]*-","",re.sub(r"\.mp4$","",c)).replace("-"," ")) for c in slugs}
    n=0
    for p in pages:
        if p.get("cat")=="glossary": continue
        if any(isinstance(b,(list,tuple)) and b and b[0]=="clip" for b in p["body"]): continue
        pt=toks(p["title"]+" "+p.get("lede","")+" "+CATS.get(p["cat"],("",""))[0])
        best,bs=None,0
        for c,ct in idx.items():
            sc=len(pt&ct)
            if sc>bs: best,bs=c,sc
        if best and bs>=1:
            body=p["body"]; pos=min(3,len(body))
            body.insert(pos,("clip",best)); n+=1
    return n

def build():
    pages=collect()
    bad=verify(pages)
    ninj=inject_clips(pages)
    print(f"  clips injected on {ninj} pages")
    if bad:
        print("VERIFY FAILED:",bad[:10]);
    sbcache={}
    for p in pages:
        c=p["cat"]
        if c not in sbcache: sbcache[c]=sidebar_for(pages,c)
        open(os.path.join(HERE,p["slug"]+".html"),"w",encoding="utf-8").write(page_html(p,sbcache[c]))
    build_index(pages); build_llms(pages); build_sitemap(pages)
    open(os.path.join(HERE,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    print(f"AI·Quantum Library: {len(pages)} pages across {len({p['cat'] for p in pages})} categories -> ai/")
    return pages

def build_index(pages):
    cards=""
    for c in CAT_ORDER:
        ps=[p for p in pages if p["cat"]==c]
        if not ps: continue
        t,blurb=CATS[c]
        first=sorted(ps,key=lambda x:x["title"])[0]["slug"]
        cards+=(f'<a class="catcard" href="./{first}.html"><div class="ct">{esc(c.replace("-"," "))}</div>'
                f'<h3>{esc(t)}</h3><p>{esc(blurb)}</p><div class="n">{len(ps)} pages &rarr;</div></a>')
    total=len(pages)
    html_out=(f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
      f'<meta name="viewport" content="width=device-width,initial-scale=1">'
      f'<title>AI · ML · Quantum Library · Kronos Fusion Energy</title>'
      f'<meta name="description" content="The Kronos AI, machine-learning and quantum-computing library — {total} pages on the algorithms, logic gates, control stack, and helium-3 quantum-computing case, with interactive circuits.">'
      f'<link rel="canonical" href="{BASE}/"><meta name="robots" content="index,follow,max-image-preview:large">'
      f'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
      f'<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Space+Grotesk:wght@400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">'
      f'<style>{STYLE}</style></head><body>{NAV}'
      f'<div class="wrap"><header class="hero"><div class="kicker">AI · ML · Quantum</div>'
      f'<h1>The intelligence layer of a fusion company.</h1>'
      f'<p class="lede">{total} pages on the algorithms, machine learning, and quantum computing behind Kronos — '
      f'every quantum logic gate with an interactive circuit, the AI control stack that holds the plasma, '
      f'the surrogate models and digital twin, and the helium-3 case for quantum computing. Open, on the record.</p></header>'
      f'{render_clip("f5-quantum-verdict.mp4")}'
      f'<div class="catgrid">{cards}</div></div>{FOOTER}{SCRIPT}</body></html>')
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(html_out)

def build_llms(pages):
    lines=["## Kronos — AI · ML · Quantum Library (open, CC BY 4.0)",
           "Reference on the algorithms, machine learning, quantum logic gates and quantum computing behind Kronos Fusion Energy, plus the helium-3 quantum-computing case. Design figures are computed and reproducible; no economics.",""]
    for c in CAT_ORDER:
        ps=[p for p in pages if p["cat"]==c]
        if not ps: continue
        lines.append(f"### {CATS[c][0]}")
        for p in sorted(ps,key=lambda x:x["title"]):
            lines.append(f"- [{p['title']}]({BASE}/{p['slug']}.html): {p['lede']}")
        lines.append("")
    open(os.path.join(HERE,"llms.txt"),"w",encoding="utf-8").write("\n".join(lines))

def build_sitemap(pages):
    urls=[f"{BASE}/"]+[f"{BASE}/{p['slug']}.html" for p in pages]
    body="".join(f"<url><loc>{u}</loc><lastmod>{BUILD_DATE}</lastmod></url>" for u in urls)
    open(os.path.join(HERE,"sitemap.xml"),"w",encoding="utf-8").write(
      f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>')

if __name__=="__main__":
    build()
