import json
h = open("index.html").read()
assert "<!-- ASK MY AI -->" in h, "marker not found"
section = '''<!-- HOW I WORK -->
<section id="how" class="section">
  <div class="wrap">
    <h2 class="title reveal">How I work</h2>
    <p class="lede reveal">The habits I bring to every ML and AI project, and where you can see them in my work.</p>
    <div class="how-grid">
      <article class="how-card reveal"><span class="how-n">01</span><h3>Find the real problem</h3><p>Before I pick a model, I work out what decision the output feeds and where the data really comes from. Most failures start with solving the wrong thing.</p><small>Seen in: data-quality pipelines at Manifoldz</small></article>
      <article class="how-card reveal"><span class="how-n">02</span><h3>Ground every answer</h3><p>An answer should trace back to a source record. I use retrieval, citations and guardrails so a system says "I don't know" instead of guessing.</p><small>Seen in: RentGuard, Audit Readiness AI</small></article>
      <article class="how-card reveal"><span class="how-n">03</span><h3>Measure, don't assume</h3><p>I compare approaches on a benchmark before choosing one, then keep the numbers so the choice can be defended later.</p><small>Seen in: Quantamind, 92.5% with LoRA vs 85.3% with prompting</small></article>
      <article class="how-card reveal"><span class="how-n">04</span><h3>Break it, then ship it</h3><p>Real data is messy, so I hunt for the edge cases on purpose. Fix the failure, add a test, and only then call it done.</p><small>Seen in: RentGuard's address check and its offline tests</small></article>
    </div>
  </div>
</section>

'''
h = h.replace("<!-- ASK MY AI -->", section + "<!-- ASK MY AI -->", 1)
open("index.html", "w").write(h)

open("styles.css", "a").write("""
/* how I work */
.how-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.how-card{position:relative;background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:26px 22px 22px;box-shadow:var(--shadow);transition:transform .3s,border-color .3s;display:flex;flex-direction:column;gap:10px}
.how-card:hover{transform:translateY(-6px);border-color:var(--a)}
.how-n{font-family:"Space Grotesk",Inter,sans-serif;font-weight:700;font-size:1.9rem;line-height:1;background:linear-gradient(100deg,var(--a),var(--b,var(--a-d)));-webkit-background-clip:text;background-clip:text;color:transparent}
.how-card h3{font-size:1.15rem;line-height:1.25}
.how-card p{color:var(--muted);font-size:.95rem;line-height:1.6}
.how-card small{margin-top:auto;padding-top:12px;border-top:1px dashed var(--line);color:var(--a-d);font-size:.8rem;font-weight:600}
@media (max-width:1000px){.how-grid{grid-template-columns:1fr 1fr}}
@media (max-width:600px){.how-grid{grid-template-columns:1fr}}
""")

entry = {"id": "approach", "title": "How she works",
  "tags": ["approach", "process", "work", "method", "philosophy", "style", "principles", "how", "values", "habits", "trust", "testing", "measure"],
  "text": "Her approach has four habits. 1) Find the real problem first: work out what decision the output feeds and where the data comes from. 2) Ground every answer in source records, with retrieval, citations and guardrails, so a system says it doesn't know instead of guessing (RentGuard, Audit Readiness AI). 3) Measure instead of assuming: compare approaches on a benchmark before choosing, for example Quantamind reached 92.5% with LoRA versus 85.3% with prompt engineering. 4) Break it, then ship it: hunt for edge cases, fix the failure and add a test, like the RentGuard address check that caught a Jersey City address resolving to a Brooklyn building."}
for fn in ["knowledge.json", "worker/knowledge.json"]:
    try:
        kb = json.load(open(fn))
    except FileNotFoundError:
        continue
    for k in kb:  # "work" now means "how she works"; keep it from hijacking other answers
        if k["id"] in ("roles", "projects-overview") and "work" in k["tags"]:
            k["tags"].remove("work")
    if not any(k["id"] == "approach" for k in kb):
        kb.append(entry)
        json.dump(kb, open(fn, "w"), indent=1, ensure_ascii=False)
print("patched OK")
