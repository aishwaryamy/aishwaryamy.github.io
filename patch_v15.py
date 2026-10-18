import re
m = open("main.js").read()

# 1) remove the old comet block (if present) and the hero network block (if present)
i = m.find("/* ---- comets")
if i != -1:
    j = m.find("\n})();", i)
    m = m[:i] + m[j + len("\n})();"):]
i = m.find("/* ---- dark theme background animation")
if i != -1:
    j = m.find("\n})();", i)
    m = m[:i] + m[j + len("\n})();"):]

# 2) new block: cursor glow + comets across the whole page, always behind content
m += r'''
/* ---- background: cursor glow + mint/violet comets (behind all content) ---- */
(() => {
  const glow = document.createElement("div"); glow.id = "glow"; glow.setAttribute("aria-hidden", "true"); document.body.appendChild(glow);
  addEventListener("pointermove", (e) => { glow.style.transform = `translate(${e.clientX}px,${e.clientY}px)`; document.body.classList.add("hasmouse"); }, { passive: true });
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const cv = document.createElement("canvas"); cv.className = "comets"; cv.setAttribute("aria-hidden", "true"); document.body.appendChild(cv);
  const ctx = cv.getContext("2d"); let W, H;
  const size = () => { const dpr = Math.min(devicePixelRatio || 1, 2); W = innerWidth; H = innerHeight; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); };
  size(); addEventListener("resize", size);
  const ANG = 1.05, dx = Math.cos(ANG), dy = Math.sin(ANG), N = innerWidth < 700 ? 6 : 11;
  const COL = ["124,240,201", "139,123,255"];
  const make = (first) => ({ x: Math.random() * (W + 300) - 200, y: first ? Math.random() * H : -Math.random() * 240 - 40, v: 1.4 + Math.random() * 2.2, len: 90 + Math.random() * 150, a: 0.28 + Math.random() * 0.32, c: COL[Math.random() < 0.55 ? 0 : 1] });
  const items = Array.from({ length: N }, () => make(true));
  (function tick() {
    ctx.clearRect(0, 0, W, H);
    for (const c of items) {
      c.x += dx * c.v; c.y += dy * c.v;
      if (c.y - c.len * dy > H || c.x - c.len * dx > W + 100) Object.assign(c, make(false));
      const tx = c.x - dx * c.len, ty = c.y - dy * c.len, g = ctx.createLinearGradient(tx, ty, c.x, c.y);
      g.addColorStop(0, `rgba(${c.c},0)`); g.addColorStop(1, `rgba(${c.c},${c.a})`);
      ctx.strokeStyle = g; ctx.lineWidth = 1.6; ctx.lineCap = "round";
      ctx.beginPath(); ctx.moveTo(tx, ty); ctx.lineTo(c.x, c.y); ctx.stroke();
      ctx.fillStyle = `rgba(${c.c},${Math.min(c.a + 0.25, 0.85)})`; ctx.beginPath(); ctx.arc(c.x, c.y, 1.9, 0, 6.283); ctx.fill();
    }
    requestAnimationFrame(tick);
  })();
})();
'''
open("main.js", "w").write(m)

open("styles.css", "a").write("""
/* comets everywhere, always behind text and cards */
#net{display:none}
.comets{display:block;position:fixed;inset:0;width:100vw;height:100vh;pointer-events:none;z-index:-1}
.tint,.foot{background:transparent}
.ask{background:transparent}
""")
print("patched OK")
