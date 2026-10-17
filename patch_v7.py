LI = '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4V21H3zM9.5 9.75h3.8v1.6h.05c.53-1 1.82-2 3.75-2 4 0 4.75 2.63 4.75 6.05V21h-4v-4.9c0-1.17-.02-2.67-1.63-2.67-1.63 0-1.88 1.27-1.88 2.58V21h-4z"/></svg>'
GH = '<svg viewBox="0 0 16 16" width="18" height="18" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38v-1.33c-2.23.48-2.7-1.07-2.7-1.07-.36-.92-.89-1.17-.89-1.17-.73-.5.06-.49.06-.49.8.06 1.23.83 1.23.83.72 1.22 1.88.87 2.33.66.07-.52.28-.87.5-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.83-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.6 7.6 0 0 1 4 0c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48v2.2c0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>'
DOC = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></svg>'
L1 = "https://linkedin.com/in/aishwaryamy"; L2 = "https://github.com/aishwaryamy"
h = open("index.html").read()

# 1) top nav icons
nav_end = '    <a href="#contact">Contact</a>\n  </nav>\n'
assert nav_end in h, "nav not found"
h = h.replace(nav_end, nav_end + f'  <div class="nav-social"><a href="{L1}" target="_blank" rel="noopener" aria-label="LinkedIn" title="LinkedIn">{LI}</a><a href="{L2}" target="_blank" rel="noopener" aria-label="GitHub" title="GitHub">{GH}</a></div>\n', 1)

# 2) flip profile card instead of the round photo
s = h.index('<div class="hero-photo rise"'); e = h.index("</section>", s)
card = f'''<div class="hero-photo rise pcard" style="--d:250ms" tabindex="0" aria-label="Profile card, hover or tap to flip">
      <div class="pc-inner">
        <div class="pc-face pc-front">
          <img src="profile.jpg" alt="Aishwarya Mandya Yogananda">
          <div class="pc-cap">
            <span class="pc-live"><i></i>Open to roles</span>
            <b>Aishwarya M. Y.</b>
            <small>ML / AI Engineer · New York</small>
          </div>
          <span class="pc-hint">Hover to flip</span>
        </div>
        <div class="pc-face pc-back">
          <div class="pc-av"><img src="profile.jpg" alt=""></div>
          <h3>Aishwarya</h3>
          <p class="pc-handle">@aishwaryamy</p>
          <p class="pc-quote">Making AI answers you can actually trust, and having fun shipping them.</p>
          <div class="pc-btns">
            <a href="{L1}" target="_blank" rel="noopener">{LI}LinkedIn</a>
            <a href="{L2}" target="_blank" rel="noopener">{GH}GitHub</a>
          </div>
          <a class="pc-res" href="AishwaryaMY_resume.pdf" target="_blank" rel="noopener">{DOC}Resume</a>
        </div>
      </div>
    </div>
  </div>
'''
h = h[:s] + card + h[e:]
open("index.html", "w").write(h)

open("styles.css", "a").write("""
/* nav social */
.nav nav{margin-left:auto}
.nav-social{display:flex;gap:4px;margin-left:12px;padding-left:12px;border-left:1px solid var(--line)}
.nav-social a{display:inline-flex;width:34px;height:34px;align-items:center;justify-content:center;border-radius:50%;color:var(--muted);transition:.2s}
.nav-social a:hover{color:var(--a-d);background:var(--a-soft)}
/* flip profile card */
.hero-photo.pcard{width:min(330px,78vw);aspect-ratio:3/4;perspective:1200px;outline:none}
.pc-inner{position:absolute;inset:0;transform-style:preserve-3d;transition:transform .8s cubic-bezier(.2,.7,.2,1)}
.pcard:hover .pc-inner,.pcard:focus-within .pc-inner,.pcard.flip .pc-inner{transform:rotateY(180deg)}
.pc-face{position:absolute;inset:0;border-radius:26px;overflow:hidden;backface-visibility:hidden;-webkit-backface-visibility:hidden;border:1px solid var(--line);box-shadow:0 30px 60px rgba(13,148,136,.2)}
.pc-front{background:var(--a-soft)}
.pc-front>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 25%}
.pc-cap{position:absolute;left:12px;right:12px;bottom:12px;background:rgba(255,255,255,.88);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.7);border-radius:18px;padding:14px 16px;display:grid;gap:2px}
.pc-cap b{font-size:1.12rem}.pc-cap small{color:var(--muted)}
.pc-live{display:inline-flex;align-items:center;gap:7px;font-size:.74rem;font-weight:700;color:var(--a-d);text-transform:uppercase;letter-spacing:.08em}
.pc-live i{width:8px;height:8px;border-radius:50%;background:#22c55e;box-shadow:0 0 0 0 rgba(34,197,94,.6);animation:ping2 2s infinite}
@keyframes ping2{70%{box-shadow:0 0 0 8px rgba(34,197,94,0)}100%{box-shadow:0 0 0 0 rgba(34,197,94,0)}}
.pc-hint{position:absolute;top:14px;right:14px;font-size:.72rem;font-weight:600;background:rgba(255,255,255,.85);padding:4px 10px;border-radius:999px;color:var(--muted)}
.pc-back{transform:rotateY(180deg);background:linear-gradient(160deg,#fff 0%,var(--tint,#f2f6f4) 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:24px;gap:6px}
.pc-av{width:92px;height:92px;border-radius:50%;overflow:hidden;border:3px solid #fff;box-shadow:0 8px 24px rgba(13,148,136,.3)}
.pc-av img{width:100%;height:100%;object-fit:cover;object-position:50% 25%}
.pc-back h3{font-size:1.5rem;margin-top:8px}
.pc-handle{color:var(--a-d);font-weight:600;font-size:.92rem}
.pc-quote{background:#fff;border:1px solid var(--line);border-radius:14px;padding:12px 14px;font-size:.9rem;color:var(--muted);margin:8px 0 6px}
.pc-btns{display:flex;gap:8px;width:100%}
.pc-btns a,.pc-res{display:inline-flex;align-items:center;justify-content:center;gap:7px;font-weight:600;font-size:.88rem;border-radius:999px;padding:10px 12px;transition:.2s}
.pc-btns a{flex:1;background:var(--a);color:#fff}.pc-btns a:hover{background:var(--a-d)}
.pc-res{border:1px solid var(--line);background:#fff;color:var(--ink,#1f2937);width:100%;margin-top:2px}.pc-res:hover{border-color:var(--a)}
@media (max-width:900px){.hero-photo.pcard{width:min(290px,76vw)}}
@media (prefers-reduced-motion:reduce){.pc-inner{transition:none}}
""")

m = open("main.js").read()
m += """
/* tap to flip the profile card (touch devices) */
(() => {
  const c = document.querySelector(".pcard"); if (!c) return;
  c.addEventListener("click", (e) => { if (e.target.closest("a")) return; c.classList.toggle("flip"); });
})();
"""
open("main.js", "w").write(m)
print("patched OK")
