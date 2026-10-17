/* Portfolio interactions. No dependencies. */
(() => {
  "use strict";

  // ---- Settings ---------------------------------------------------------
  // Leave empty to use the free built-in answerer (works offline, no cost).
  // After deploying the worker, paste its URL here, e.g.
  // "https://portfolio-agent.YOURNAME.workers.dev"
  const AGENT_URL = "";

  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));

  // ---- Typewriter -------------------------------------------------------
  const phrases = ["Machine Learning Engineer", "LLM & Agent Builder", "RAG Pipeline Engineer", "AI Product Builder"];
  const typeEl = $("#type");
  if (typeEl) {
    if (reduce) typeEl.textContent = phrases[0];
    else {
      let p = 0, c = 0, del = false;
      const tick = () => {
        const full = phrases[p];
        c += del ? -1 : 1;
        typeEl.textContent = full.slice(0, c);
        let wait = del ? 30 : 70;
        if (!del && c === full.length) { del = true; wait = 1800; }
        else if (del && c === 0) { del = false; p = (p + 1) % phrases.length; wait = 350; }
        setTimeout(tick, wait);
      };
      setTimeout(tick, 700);
    }
  }

  // ---- Reveal on scroll -------------------------------------------------
  $$(".stats,.skill-grid,.proj-grid,.facts,.papers,.edu-grid").forEach((g) =>
    [...g.children].forEach((el, i) => el.style.setProperty("--d", i * 80 + "ms")));
  const io = new IntersectionObserver((es) => es.forEach((e) => {
    if (e.isIntersecting) {
      e.target.classList.add("in");
      if (e.target.matches(".stat")) countUp($("b", e.target));
      io.unobserve(e.target);
    }
  }), { threshold: 0.15, rootMargin: "0px 0px -6% 0px" });
  $$(".reveal").forEach((el) => io.observe(el));

  function countUp(el) {
    if (!el || el.dataset.done) return;
    el.dataset.done = 1;
    const end = parseFloat(el.dataset.count), dec = +(el.dataset.dec || 0);
    const suf = el.dataset.suffix || "";
    const fmt = (v) => v.toLocaleString("en-US", { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suf;
    if (reduce) { el.textContent = fmt(end); return; }
    const t0 = performance.now(), dur = 1400;
    const step = (t) => {
      const k = clamp((t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = fmt(end * e);
      if (k < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }

  // ---- Scroll progress, nav, timeline ----------------------------------
  const progress = $("#progress"), nav = $("#nav");
  const timeline = $("#timeline"), lineFill = $("#lineFill");
  let ticking = false;
  function onScroll() {
    const max = document.documentElement.scrollHeight - innerHeight;
    progress.style.transform = `scaleX(${max > 0 ? scrollY / max : 0})`;
    nav.classList.toggle("scrolled", scrollY > 20);
    if (timeline) {
      const r = timeline.getBoundingClientRect();
      lineFill.style.transform = `scaleY(${clamp((innerHeight * 0.65 - r.top) / r.height)})`;
    }
    ticking = false;
  }
  addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  addEventListener("resize", onScroll);
  onScroll();

  const links = $$(".nav nav a");
  const sio = new IntersectionObserver((es) => es.forEach((e) => {
    if (e.isIntersecting) links.forEach((a) => a.classList.toggle("active", a.getAttribute("href") === "#" + e.target.id));
  }), { rootMargin: "-45% 0px -50% 0px" });
  ["about", "ask", "skills", "experience", "projects", "contact"].forEach((id) => { const s = document.getElementById(id); if (s) sio.observe(s); });

  $("#yr").textContent = new Date().getFullYear();

  // ---- Contact form: opens the visitor's email app -----------------------
  const cf = $("#contactForm");
  if (cf) cf.addEventListener("submit", (e) => {
    e.preventDefault();
    const f = new FormData(cf);
    const body = `${f.get("message")}\n\n${f.get("name")} (${f.get("email")})`;
    location.href = "mailto:aishwaryamy20@gmail.com?subject=" + encodeURIComponent("Portfolio message from " + f.get("name")) + "&body=" + encodeURIComponent(body);
  });

  // ---- "Ask my AI" ------------------------------------------------------
  const log = $("#log"), form = $("#askForm"), input = $("#q"), micBtn = $("#mic");
  const speakBox = $("#speak"), history = [];
  let kb = [];
  fetch("knowledge.json").then((r) => r.json()).then((d) => { kb = d; }).catch(() => {});

  function add(text, who) {
    const d = document.createElement("div");
    d.className = "msg " + who; d.textContent = text;
    log.appendChild(d); log.scrollTop = log.scrollHeight; return d;
  }
  const STOP = new Set("a an the is are was were be to of in on at for and or her his she he it this that what whats who how do does did tell me about can you your please any with from".split(" "));
  const tok = (s) => s.toLowerCase().replace(/[^a-z0-9+#\- ]/g, " ").split(/\s+/).filter((w) => w.length > 1 && !STOP.has(w));

  // Free, offline answerer: keyword match over knowledge.json
  function localAnswer(q) {
    const words = tok(q);
    if (!words.length) return "Ask me about her projects, experience, skills, or the roles she's looking for.";
    if (/^(hi|hello|hey)\b/i.test(q.trim()) && words.length <= 1)
      return "Hi! Ask me about Aishwarya's projects, experience, skills, or what roles she's looking for.";
    const scored = kb.map((e) => {
      let s = 0; const body = e.text.toLowerCase();
      for (const w of words) {
        if (e.tags.includes(w)) s += 4;
        else if (e.tags.some((t) => t.startsWith(w) && w.length > 3)) s += 2;
        if (body.includes(w)) s += 1;
      }
      return { e, s };
    }).sort((a, b) => b.s - a.s);
    if (!scored.length || scored[0].s < 3)
      return "I don't have that in her resume or projects, so I won't guess. You can email her at aishwaryamy20@gmail.com, or ask me about her projects, experience or skills.";
    const out = [scored[0].e.text];
    if (scored[1] && scored[1].s >= scored[0].s * 0.8 && scored[1].s >= 6) out.push(scored[1].e.text);
    return out.join("\n\n");
  }

  async function answer(q) {
    if (AGENT_URL) {
      try {
        const r = await fetch(AGENT_URL, {
          method: "POST", headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ question: q, history: history.slice(-6) }),
        });
        if (r.ok) { const j = await r.json(); if (j.answer) return j.answer; }
        if (r.status === 429) return "I'm getting a lot of questions right now. Please try again in a minute, or email her directly.";
      } catch (_) { /* fall through to the free answerer */ }
    }
    return localAnswer(q);
  }

  async function ask(q) {
    q = q.trim(); if (!q) return;
    add(q, "me"); input.value = "";
    const t = add("Thinking…", "bot typing");
    const a = await answer(q);
    t.remove(); add(a, "bot");
    history.push({ role: "user", content: q }, { role: "assistant", content: a });
    if (speakBox.checked && "speechSynthesis" in window) {
      speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(a); u.rate = 1.02; speechSynthesis.speak(u);
    }
  }
  form.addEventListener("submit", (e) => { e.preventDefault(); ask(input.value); });
  $("#chips").addEventListener("click", (e) => { if (e.target.matches("button")) ask(e.target.textContent); });

  // Voice input (free, uses the browser's built-in speech recognition)
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) { micBtn.style.display = "none"; $("#voiceNote").textContent = "Voice input isn't supported in this browser; typing works everywhere."; }
  else {
    const rec = new SR(); rec.lang = "en-US"; rec.interimResults = false; rec.maxAlternatives = 1;
    let on = false;
    micBtn.addEventListener("click", () => {
      if (on) { rec.stop(); return; }
      try { speechSynthesis.cancel(); rec.start(); } catch (_) {}
    });
    rec.onstart = () => { on = true; micBtn.classList.add("rec"); input.placeholder = "Listening…"; };
    rec.onend = () => { on = false; micBtn.classList.remove("rec"); input.placeholder = "Ask a question…"; };
    rec.onerror = () => { add("I couldn't hear that. Check that the microphone is allowed, or type your question.", "bot"); };
    rec.onresult = (e) => { const t = e.results[0][0].transcript; input.value = t; ask(t); };
  }

  // exposed for tests
  window.__portfolio = { localAnswer, setKb: (k) => { kb = k; } };
})();
