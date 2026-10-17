h = open("index.html").read()
s = h.index('<!-- CONTACT -->'); e = h.index("</section>", s) + len("</section>")
new = '''<!-- CONTACT -->
<section id="contact" class="section">
  <div class="wrap">
    <div class="touch reveal">
      <span class="open-now"><i></i>Open to AI / ML Engineer roles</span>
      <h2>Let's build something<br>worth shipping.</h2>
      <p>Hiring for an ML or AI engineering role, or have a problem worth solving with LLM agents? My inbox is open.</p>
      <div class="touch-actions">
        <a class="btn primary big" href="mailto:aishwaryamy20@gmail.com">Say hello</a>
        <button class="btn big" id="copyMail" type="button">aishwaryamy20@gmail.com <span id="copyTag">Copy</span></button>
      </div>
      <div class="touch-links">
        <a href="https://linkedin.com/in/aishwaryamy" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4V21H3zM9.5 9.75h3.8v1.6h.05c.53-1 1.82-2 3.75-2 4 0 4.75 2.63 4.75 6.05V21h-4v-4.9c0-1.17-.02-2.67-1.63-2.67-1.63 0-1.88 1.27-1.88 2.58V21h-4z"/></svg>LinkedIn</a>
        <a href="https://github.com/aishwaryamy" target="_blank" rel="noopener"><svg viewBox="0 0 16 16" width="18" height="18" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38v-1.33c-2.23.48-2.7-1.07-2.7-1.07-.36-.92-.89-1.17-.89-1.17-.73-.5.06-.49.06-.49.8.06 1.23.83 1.23.83.72 1.22 1.88.87 2.33.66.07-.52.28-.87.5-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.83-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.6 7.6 0 0 1 4 0c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48v2.2c0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>GitHub</a>
        <a href="AishwaryaMY_resume.pdf" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></svg>Resume</a>
        <span><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>New York, NY</span>
      </div>
    </div>
  </div>
</section>'''
open("index.html", "w").write(h[:s] + new + h[e:])

c = open("styles.css").read()
c += """
/* contact touch */
.touch{position:relative;overflow:hidden;text-align:center;padding:64px 28px;border-radius:28px;color:#fff;background:linear-gradient(135deg,#0d9488 0%,#0b6b63 60%,#134e4a 100%);box-shadow:0 30px 60px rgba(13,148,136,.25)}
.touch::before,.touch::after{content:"";position:absolute;border-radius:50%;border:1px solid rgba(255,255,255,.14);pointer-events:none}
.touch::before{width:520px;height:520px;right:-160px;top:-220px}.touch::after{width:360px;height:360px;left:-120px;bottom:-190px}
.touch>*{position:relative}
.open-now{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.25);padding:6px 14px;border-radius:999px;font-size:.84rem;font-weight:600}
.open-now i{width:8px;height:8px;border-radius:50%;background:#4ade80;box-shadow:0 0 0 0 rgba(74,222,128,.7);animation:ping 2s infinite}
@keyframes ping{70%{box-shadow:0 0 0 9px rgba(74,222,128,0)}100%{box-shadow:0 0 0 0 rgba(74,222,128,0)}}
.touch h2{font-size:clamp(2rem,4.6vw,3.2rem);line-height:1.1;margin:22px 0 14px;letter-spacing:-.02em;color:#fff}
.touch p{max-width:560px;margin:0 auto;opacity:.9;font-size:1.05rem}
.touch-actions{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:30px}
.touch .btn.big{padding:14px 26px;font-size:1rem}
.touch .btn.primary{background:#fff;color:#0b6b63;border-color:#fff}.touch .btn.primary:hover{background:#f0fdfa}
.touch .btn:not(.primary){background:rgba(255,255,255,.12);color:#fff;border:1px solid rgba(255,255,255,.35)}
.touch .btn:not(.primary):hover{background:rgba(255,255,255,.22)}
.touch .btn span{margin-left:10px;font-size:.78rem;background:rgba(255,255,255,.2);padding:2px 10px;border-radius:999px}
.touch-links{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-top:34px}
.touch-links a,.touch-links span{display:inline-flex;align-items:center;gap:8px;padding:9px 16px;border-radius:999px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:#fff;font-weight:600;font-size:.9rem;transition:.2s}
.touch-links a:hover{background:rgba(255,255,255,.22);transform:translateY(-2px)}
@media (max-width:600px){.touch{padding:44px 20px}}
"""
open("styles.css", "w").write(c)

m = open("main.js").read()
m += """
/* copy email */
(() => {
  const b = document.getElementById("copyMail"); if (!b) return;
  b.addEventListener("click", async () => {
    const t = document.getElementById("copyTag");
    try { await navigator.clipboard.writeText("aishwaryamy20@gmail.com"); t.textContent = "Copied!"; }
    catch (e) { location.href = "mailto:aishwaryamy20@gmail.com"; }
    setTimeout(() => (t.textContent = "Copy"), 1800);
  });
})();
"""
open("main.js", "w").write(m)
print("patched OK")
