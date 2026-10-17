js = r'''
/* ---- comets: soft teal shooting stars in the background ---- */
(() => {
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const cv = document.createElement("canvas"); cv.className = "comets"; cv.setAttribute("aria-hidden", "true");
  document.body.appendChild(cv);
  const ctx = cv.getContext("2d"); let W, H, dpr;
  const size = () => { dpr = Math.min(devicePixelRatio || 1, 2); W = innerWidth; H = innerHeight; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); };
  size(); addEventListener("resize", size);
  const ANG = 1.05, dx = Math.cos(ANG), dy = Math.sin(ANG);
  const N = W < 700 ? 5 : 9;
  const make = (first) => ({ x: Math.random() * (W + 300) - 200, y: first ? Math.random() * H : -Math.random() * 200 - 40, v: 1.6 + Math.random() * 2.2, len: 90 + Math.random() * 130, a: 0.25 + Math.random() * 0.3 });
  const items = Array.from({ length: N }, () => make(true));
  (function tick() {
    ctx.clearRect(0, 0, W, H);
    for (const c of items) {
      c.x += dx * c.v; c.y += dy * c.v;
      if (c.y - c.len * dy > H || c.x - c.len * dx > W + 100) Object.assign(c, make(false));
      const tx = c.x - dx * c.len, ty = c.y - dy * c.len;
      const g = ctx.createLinearGradient(tx, ty, c.x, c.y);
      g.addColorStop(0, "rgba(13,148,136,0)"); g.addColorStop(1, "rgba(13,148,136," + c.a + ")");
      ctx.strokeStyle = g; ctx.lineWidth = 1.6; ctx.lineCap = "round";
      ctx.beginPath(); ctx.moveTo(tx, ty); ctx.lineTo(c.x, c.y); ctx.stroke();
      ctx.fillStyle = "rgba(13,148,136," + Math.min(c.a + 0.2, 0.7) + ")";
      ctx.beginPath(); ctx.arc(c.x, c.y, 1.8, 0, 6.283); ctx.fill();
    }
    requestAnimationFrame(tick);
  })();
})();
'''
open("main.js", "a").write(js)
open("styles.css", "a").write("\n.comets{position:fixed;inset:0;width:100vw;height:100vh;pointer-events:none;z-index:2}\n")
print("patched OK")
