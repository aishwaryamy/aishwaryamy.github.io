h = open("index.html").read()
s = h.index('<div class="pc-cap">'); e = h.index("</div>", s) + len("</div>")
h = h[:s] + '<div class="pc-cap"><i></i>Open to roles · New York</div>' + h[e:]
open("index.html", "w").write(h)
open("styles.css", "a").write("""
/* simpler front caption: one clean pill */
.pc-cap{left:14px;right:auto;bottom:14px;display:inline-flex;align-items:center;gap:9px;padding:9px 16px;border-radius:999px;font-size:.84rem;font-weight:600;color:var(--ink,#1f2937)}
.pc-cap i{width:8px;height:8px;border-radius:50%;background:#22c55e;box-shadow:0 0 0 0 rgba(34,197,94,.6);animation:ping2 2s infinite}
""")
print("patched OK")
