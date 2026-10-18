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

  // ---- Projects: cards + detail pop-up ----------------------------------
  // To use a real screenshot instead of an illustration, drop it in img/ and
  // change the `img` value below (for example "img/rentguard.png").
  const PROJECTS = [
    { id: "rentguard", big: true, badge: "NYC · Public data", title: "RentGuard", img: "img/rentguard.jpg",
      blurb: "Type any NYC address and see that building's live HPD violations and 311 complaints in plain English, with answers grounded only in the building's own records.",
      tags: ["Python", "Streamlit", "OpenAI", "NYC Open Data", "Guardrails"],
      sections: [
        ["The problem", "Renters can't easily see a building's history before signing a lease. The data exists, but it is scattered across city systems and written for agencies, not tenants."],
        ["What it does", ["Resolves any NYC address to its building (BBL) with NYC Planning Labs Geosearch.", "Pulls live HPD violations and 311 complaints from NYC Open Data and explains them in plain English.", "Lets you ask questions answered only from that building's records, with citations.", "Declines legal conclusions and never calls a building safe."]],
        ["The bug I'm proudest of finding", "While testing, a Jersey City address resolved to a Brooklyn building, because NYC's geocoder always returns its closest guess. I built a verification layer that refuses out-of-NYC input and checks house number, street, borough and ZIP before showing any report. It is covered by 32 offline tests, and I wrote it up in the README."]],
      links: [["Live demo", "https://rentguard-fwpwhgu6y7iwhzbozcefml.streamlit.app/", true], ["View code", "https://github.com/aishwaryamy/RentGuard"]] },
    { id: "enrichment", big: true, badge: "Agentic AI · B2B", title: "AI Contact Enrichment Agent", img: "img/contact-enrichment.jpg",
      blurb: "A conversational agent that turns any B2B prospect into a research brief in about 45 seconds: live company intel, buying signals, ICP scoring and a personalized outreach draft.",
      tags: ["Next.js", "TypeScript", "GPT-4o", "Supabase", "Vercel"],
      sections: [
        ["The problem", "Researching a prospect before outreach is slow and repetitive: company news, hiring and funding signals, fit with the ideal customer profile, then writing something personal."],
        ["What it does", ["Chat with the agent about any prospect or company.", "Gathers live company intelligence and buying signals.", "Scores the prospect against an ideal customer profile (ICP).", "Drafts personalized outreach with GPT-4o, in about 45 seconds end to end."]]],
      links: [["Live demo", "https://ai-enrichment-agent.vercel.app/", true], ["View code", "https://github.com/aishwaryamy/ai-enrichment-agent"]] },
    { id: "nexthire", badge: "Job search · Agentic", title: "NextHire AI", img: "img/nexthire.svg",
      blurb: "An AI job-search copilot with a Kanban tracker, resume and cover letter tailoring, contact finding and STAR-scored interview prep.",
      tags: ["FastAPI", "React", "LangGraph", "GPT-4o", "Docker"],
      sections: [["What it does", ["Tracks applications on a Kanban board.", "Tailors your resume and writes cover letters for each role.", "Finds contacts to reach out to.", "Runs mock interviews and scores answers with the STAR method."]]],
      links: [["Live demo", "https://nexthire-46nl.onrender.com", true], ["View code", "https://github.com/aishwaryamy/nexthire"]] },
    { id: "incident", badge: "Agents · RAG", title: "AI Incident Response Agent", img: "img/incident-response.svg",
      blurb: "A LangGraph and RAG pipeline that helps investigate engineering incidents, with caching, retrieval, authentication and observability built in.",
      tags: ["LangGraph", "RAG", "FastAPI", "pgvector", "Redis", "Docker"],
      sections: [["What it does", ["Investigates incidents with a LangGraph agent over retrieved runbooks and history.", "pgvector retrieval with Redis caching for fast repeat lookups.", "JWT authentication and observability for production use."]]],
      links: [["View code", "https://github.com/aishwaryamy/AI-Incident-Response-Agent"]] },
    { id: "audit", badge: "RAG · Evaluation", title: "Audit Readiness AI", img: "img/audit-readiness.svg",
      blurb: "A RAG compliance assistant over SOC 2 documents that compares retrieval methods, with a reported 60% reduction in audit effort.",
      tags: ["LangChain", "RAG", "OpenAI API", "FastAPI", "Docker"],
      sections: [["What it does", ["Answers audit-readiness questions from SOC 2 documents.", "Compares retrieval approaches so the best one is chosen by measurement, not guesswork.", "Reported 60% reduction in audit effort."]]],
      links: [["View code", "https://github.com/aishwaryamy/auditreadinessai"]] },
    { id: "quantamind", badge: "Fine-tuning · Legal AI", title: "Quantamind Legal AI Agent", img: "img/quantamind.svg",
      blurb: "An offline agent for legal contract analysis. LoRA fine-tuning reached 92.5% accuracy versus 85.3% for prompt engineering on the CUAD benchmark.",
      tags: ["Mistral 7B", "LoRA", "FAISS", "RAG", "Docker"],
      sections: [["What it does", ["Analyzes contracts fully offline using Mistral 7B, FAISS and RAG.", "Benchmarks LoRA fine-tuning (92.5%) against few-shot prompt engineering (85.3%) on the CUAD dataset."]]],
      links: [["View code", "https://github.com/aishwaryamy/quantamind-legal-ai-agent"]] },
    { id: "opspilot", badge: "AI SaaS · Full-stack", title: "OpsPilot", img: "img/opspilot.svg",
      blurb: "A full-stack AI agent SaaS with chat and tool calling, document ingestion, vector retrieval, user memory and a multi-panel interface.",
      tags: ["Next.js", "FastAPI", "pgvector", "Redis", "OpenAI"],
      sections: [["What it does", ["Chat with tool calling to run tasks.", "Document ingestion with vector retrieval.", "Per-user memory and a multi-panel UI."]]],
      links: [["View code", "https://github.com/aishwaryamy/opspilot"]] },
    { id: "gtm", badge: "Sales · Automation", title: "AI GTM Copilot", img: "img/gtm-copilot.svg",
      blurb: "An LLM assistant that automates lead qualification, account research and outreach for 1K+ leads per day through MCP workflows.",
      tags: ["OpenAI API", "MCP", "Streamlit", "SQLite", "Pandas"],
      sections: [["What it does", ["Qualifies leads and researches accounts automatically.", "Generates outreach, handling 1K+ leads per day.", "Uses MCP-based workflows to connect tools."]]],
      links: [["Live demo", "https://ai-gtm-copilot.streamlit.app/", true], ["View code", "https://github.com/aishwaryamy/ai-gtm-copilot"]] },
  ];
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const featuredEl = $("#featured"), gridEl = $("#projGrid");
  PROJECTS.forEach((p) => {
    const a = document.createElement("article");
    a.className = "proj reveal" + (p.big ? " big" : "");
    a.tabIndex = 0; a.setAttribute("role", "button"); a.dataset.p = p.id;
    a.setAttribute("aria-label", "Open details for " + p.title);
    a.innerHTML = `<div class="shot"><img src="${p.img}" alt="" loading="lazy"></div><div class="pb"><span class="badge">${esc(p.badge)}</span><h3>${esc(p.title)}</h3><p>${esc(p.blurb)}</p><div class="tags">${p.tags.slice(0, 4).map((t) => `<i>${esc(t)}</i>`).join("")}</div><div class="pf"><span class="open">View details</span><span class="plinks">${p.links.map(([l, u, pr]) => pr ? `<a class="pl live" href="${u}" target="_blank" rel="noopener">Live demo</a>` : `<a class="pl gh" href="${u}" target="_blank" rel="noopener" aria-label="GitHub repo" title="GitHub"><svg viewBox="0 0 16 16" width="18" height="18" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38v-1.33c-2.23.48-2.7-1.07-2.7-1.07-.36-.92-.89-1.17-.89-1.17-.73-.5.06-.49.06-.49.8.06 1.23.83 1.23.83.72 1.22 1.88.87 2.33.66.07-.52.28-.87.5-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.83-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.6 7.6 0 0 1 4 0c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48v2.2c0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg></a>`).join("")}</span></div></div>`;
    (p.big ? featuredEl : gridEl).appendChild(a);
  });
  const modal = $("#modal");
  let lastFocus = null;
  function openProject(id) {
    const p = PROJECTS.find((x) => x.id === id); if (!p) return;
    lastFocus = document.activeElement;
    $("#mImg").src = p.img; $("#mBadge").textContent = p.badge; $("#mTitle").textContent = p.title; $("#mLead").textContent = p.blurb;
    $("#mSections").innerHTML = p.sections.map(([h, b]) => `<div class="m-sec"><h4>${esc(h)}</h4>${Array.isArray(b) ? "<ul>" + b.map((x) => `<li>${esc(x)}</li>`).join("") + "</ul>" : `<p>${esc(b)}</p>`}</div>`).join("");
    $("#mTags").innerHTML = p.tags.map((t) => `<i>${esc(t)}</i>`).join("");
    $("#mLinks").innerHTML = p.links.map(([l, u, primary]) => `<a class="btn sm${primary ? " primary" : ""}" href="${u}" target="_blank" rel="noopener">${esc(l)}</a>`).join("");
    modal.hidden = false; document.body.classList.add("lock"); $(".modal-x").focus();
  }
  function closeModal() { modal.hidden = true; document.body.classList.remove("lock"); if (lastFocus) lastFocus.focus(); }
  document.addEventListener("click", (e) => {
    const card = e.target.closest(".proj"); if (card && !e.target.closest(".plinks")) openProject(card.dataset.p);
    if (e.target.closest("[data-close]")) closeModal();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !modal.hidden) closeModal();
    if ((e.key === "Enter" || e.key === " ") && e.target.matches(".proj")) { e.preventDefault(); openProject(e.target.dataset.p); }
  });

  // ---- Reveal on scroll -------------------------------------------------
  $$(".stats,.skill-grid,.proj-grid,.feature-row,.facts,.papers,.edu-grid").forEach((g) =>
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

/* tap to flip the profile card (touch devices) */
(() => {
  const c = document.querySelector(".pcard"); if (!c) return;
  c.addEventListener("click", (e) => { if (e.target.closest("a")) return; c.classList.toggle("flip"); });
})();



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
