css = r'''
/* ===== DARK THEME: mint + violet on near-black ===== */
:root{
  --bg:#05070c; --tint:#080c14; --card:#0c1119; --ink:#e9edf5; --muted:#8e98ad; --line:rgba(255,255,255,.08);
  --a:#7cf0c9; --a-d:#7cf0c9; --a-soft:rgba(124,240,201,.12); --b:#8b7bff;
  --grad:linear-gradient(100deg,#7cf0c9,#8b7bff);
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.35);
  color-scheme:dark;
}
body{background:var(--bg);color:var(--ink)}
::selection{background:rgba(139,123,255,.4)}
.comets{display:none}
#progress{background:var(--grad)}
.nav{background:rgba(5,7,12,.6)}
.nav.scrolled{box-shadow:none}
.nav-social{border-left-color:var(--line)}
.title::after{background:var(--grad)}
.dot{background:var(--a)}
.hero{background:radial-gradient(900px 520px at 85% 0%,rgba(139,123,255,.20),transparent 62%),radial-gradient(700px 420px at 0% 80%,rgba(124,240,201,.09),transparent 60%)}
#type{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.hello{color:var(--a)}
.tint{background:var(--tint)}
.btn{background:rgba(255,255,255,.04);color:var(--ink);border-color:rgba(255,255,255,.14)}
.btn:hover{background:rgba(255,255,255,.09)}
.btn.primary{background:var(--grad);color:#05070c;border-color:transparent}
.btn.primary:hover{filter:brightness(1.07);background:var(--grad)}
.btn.ghost{background:transparent}
.badge{color:var(--a);background:var(--a-soft)}
.proj:hover,.proj:focus-visible{box-shadow:0 24px 60px rgba(0,0,0,.55);border-color:rgba(124,240,201,.5)}
.proj .shot{background:#0a0f17}
.tags i,.skills i,.chip{background:rgba(255,255,255,.06);color:#cfd6e4;border-color:var(--line)}
.open{color:var(--a)}
.pl.live{background:var(--grad);color:#05070c}.pl.live:hover{filter:brightness(1.08);background:var(--grad)}
.pl.gh{background:rgba(255,255,255,.05);color:var(--ink);border-color:var(--line)}.pl.gh:hover{border-color:var(--a);color:var(--a)}
/* chat */
.chat{box-shadow:0 20px 60px rgba(0,0,0,.5);background:linear-gradient(180deg,#101826,#0c1119)}
.chat-top{background:rgba(255,255,255,.03)}
.msg.bot{background:rgba(255,255,255,.05)}
.msg.me{background:var(--grad);color:#05070c;font-weight:500}
.chips button{background:rgba(255,255,255,.04);color:var(--ink);border-color:var(--line)}
.chips button:hover{border-color:var(--a);background:var(--a-soft)}
#q{background:rgba(255,255,255,.04);color:var(--ink);border-color:var(--line)}
#q:focus{border-color:var(--a)}
.icon{background:rgba(255,255,255,.05);color:var(--ink);border-color:var(--line)}
.send{background:var(--grad);color:#05070c;border-color:transparent}
/* cards / sections that used light surfaces */
.edu,.fact,.stat,.skill,.paper,.tl-card,.card{background:linear-gradient(180deg,#101826,#0c1119);border-color:var(--line)}
.foot{background:#05070c;border-color:var(--line)}
/* modal */
.modal-bg{background:rgba(2,4,8,.7)}
.modal-card{background:#0c1119;border:1px solid var(--line)}
.modal-x{background:rgba(5,7,12,.8);color:#fff}
/* contact panel */
.touch{background:radial-gradient(600px 300px at 80% 0%,rgba(139,123,255,.35),transparent 60%),radial-gradient(500px 260px at 10% 100%,rgba(124,240,201,.18),transparent 60%),#0c1119;border:1px solid rgba(255,255,255,.1);box-shadow:0 30px 80px rgba(0,0,0,.5)}
.touch .btn.primary{background:var(--grad);color:#05070c}
.open-now i{background:#4ade80}
/* profile card */
.pc-face{border-color:rgba(255,255,255,.1);box-shadow:0 30px 70px rgba(0,0,0,.55),0 0 60px rgba(139,123,255,.18)}
.pc-hint{background:rgba(5,7,12,.7);color:#cfd6e4}
.pc-back{background:linear-gradient(160deg,#131b2b 0%,#0c1119 100%)}
.pc-av{border-color:#0c1119;box-shadow:0 8px 24px rgba(139,123,255,.35)}
.pc-quote{background:rgba(255,255,255,.05);border-color:var(--line);color:#cfd6e4}
.pc-btns a{background:var(--grad);color:#05070c}.pc-btns a:hover{filter:brightness(1.07);background:var(--grad)}
.pc-res{background:rgba(255,255,255,.05);color:var(--ink);border-color:var(--line)}.pc-res:hover{border-color:var(--a)}
.pc-handle{color:var(--a)}
/* timeline / misc accents */
.timeline::before,.tl-line{background:var(--line)}
/* background animation: network + cursor glow */
#net{position:absolute;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}
.hero .wrap{position:relative;z-index:2}
#glow{position:fixed;width:520px;height:520px;left:0;top:0;margin:-260px 0 0 -260px;border-radius:50%;pointer-events:none;z-index:0;background:radial-gradient(circle,rgba(139,123,255,.16),transparent 62%);opacity:0;transition:opacity .3s}
body.hasmouse #glow{opacity:1}
'''
open("styles.css", "a").write(css)

js = r'''
/* ---- dark theme background animation: network + cursor glow ---- */
(() => {
  const hero = document.querySelector(".hero"); if (!hero) return;
  const glow = document.createElement("div"); glow.id = "glow"; glow.setAttribute("aria-hidden", "true"); document.body.appendChild(glow);
  const cv = document.createElement("canvas"); cv.id = "net"; cv.setAttribute("aria-hidden", "true"); hero.insertBefore(cv, hero.firstChild);
  hero.style.position = "relative"; hero.style.overflow = "hidden";
  const ctx = cv.getContext("2d"); let W = 0, H = 0, nodes = [], mouse = { x: -999, y: -999 }, vis = true;
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const size = () => {
    const dpr = Math.min(devicePixelRatio || 1, 2); W = cv.clientWidth; H = cv.clientHeight;
    cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const n = Math.max(28, Math.min(85, Math.round(W * H / 16000)));
    nodes = Array.from({ length: n }, () => ({ x: Math.random() * W, y: Math.random() * H, vx: (Math.random() - .5) * .35, vy: (Math.random() - .5) * .35, r: Math.random() * 1.6 + .6 }));
  };
  size(); addEventListener("resize", size);
  new IntersectionObserver((e) => { vis = e[0].isIntersecting; }).observe(hero);
  addEventListener("pointermove", (e) => {
    const b = cv.getBoundingClientRect(); mouse.x = e.clientX - b.left; mouse.y = e.clientY - b.top;
    glow.style.transform = `translate(${e.clientX}px,${e.clientY}px)`; document.body.classList.add("hasmouse");
  }, { passive: true });
  (function tick() {
    if (vis) {
      ctx.clearRect(0, 0, W, H);
      for (const n of nodes) {
        if (!reduce) { n.x += n.vx; n.y += n.vy; }
        if (n.x < 0 || n.x > W) n.vx *= -1; if (n.y < 0 || n.y > H) n.vy *= -1;
        const dx = n.x - mouse.x, dy = n.y - mouse.y, d = Math.hypot(dx, dy);
        if (d < 140 && d > 0) { n.x += dx / d * .9; n.y += dy / d * .9; }
      }
      for (let i = 0; i < nodes.length; i++) {
        const a = nodes[i];
        for (let j = i + 1; j < nodes.length; j++) {
          const b = nodes[j], d = Math.hypot(a.x - b.x, a.y - b.y);
          if (d < 130) { ctx.strokeStyle = `rgba(124,240,201,${(1 - d / 130) * .26})`; ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke(); }
        }
        ctx.fillStyle = "rgba(139,123,255,.75)"; ctx.beginPath(); ctx.arc(a.x, a.y, a.r, 0, 6.283); ctx.fill();
      }
    }
    requestAnimationFrame(tick);
  })();
})();
'''
open("main.js", "a").write(js)
print("patched OK")
