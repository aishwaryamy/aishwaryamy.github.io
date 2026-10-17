import json, re
# ---- index.html: simple education cards, clean hero background ----
h = open("index.html").read()
s = h.index('<h3 class="sub edu-h reveal">Education</h3>')
e = h.index("</section>", s)
h = h[:s] + '''<h3 class="sub edu-h reveal">Education</h3>
    <div class="edu-grid">
      <div class="edu reveal"><div class="edu-top"><h3>Master's</h3><time>2024 – 2026</time></div><p class="school">Binghamton University, State University of New York</p><p class="prog">M.S. in Computer Science</p><p class="when">New York, USA</p></div>
      <div class="edu reveal"><div class="edu-top"><h3>Bachelor's</h3><time>2020 – 2024</time></div><p class="school">Visvesvaraya Technological University</p><p class="prog">B.E. in Information Science &amp; Engineering</p><p class="when">Bengaluru, India</p></div>
    </div>
  </div>
''' + h[e:]
h = h.replace('<div class="blob b1" aria-hidden="true"></div><div class="blob b2" aria-hidden="true"></div>\n', '')
open("index.html", "w").write(h)

# ---- styles.css ----
c = open("styles.css").read()
a = c.index(".edu-h{"); b = c.index("/* projects */")
c = c[:a] + '''.edu-h{margin-top:46px}
.edu-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:6px;max-width:980px}
.edu{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:24px;box-shadow:var(--shadow)}
.edu-top{display:flex;justify-content:space-between;align-items:baseline;gap:12px}
.edu-top h3{font-size:1.35rem}.edu-top time{color:var(--muted);font-size:.9rem;white-space:nowrap}
.edu .school{color:var(--muted);margin-top:4px}
.edu .prog{font-weight:600;margin-top:14px}
.edu .when{color:var(--muted);font-size:.92rem}

''' + c[b:]
c = c.replace("animation:spin 40s linear infinite", "").replace("border:2px dashed rgba(13,148,136,.45)", "border:2px solid rgba(13,148,136,.22)")
open("styles.css", "w").write(c)

# ---- main.js: live demo for the Contact Enrichment Agent ----
j = open("main.js").read()
old = 'links: [["View code", "https://github.com/aishwaryamy/ai-enrichment-agent"]]'
if old in j:
    j = j.replace(old, 'links: [["Live demo", "https://ai-enrichment-agent.vercel.app/", true], ["View code", "https://github.com/aishwaryamy/ai-enrichment-agent"]]')
open("main.js", "w").write(j)

# ---- knowledge.json: add the live link ----
kb = json.load(open("knowledge.json"))
for k in kb:
    if k["id"] == "p-enrich" and "ai-enrichment-agent.vercel.app" not in k["text"]:
        k["text"] = k["text"].replace("Code: https://", "Live demo: https://ai-enrichment-agent.vercel.app/ Code: https://")
json.dump(kb, open("knowledge.json", "w"), indent=1, ensure_ascii=False)
print("patched OK")
