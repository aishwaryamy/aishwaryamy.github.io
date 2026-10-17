m = open("main.js").read()
m = m.replace("img/rentguard.svg", "img/rentguard.jpg").replace("img/contact-enrichment.svg", "img/contact-enrichment.jpg")
old = '<span class="open">View details</span></div>`;'
new = '<div class="pf"><span class="open">View details</span><span class="plinks">${p.links.map(([l, u, pr]) => pr ? `<a class="pl live" href="${u}" target="_blank" rel="noopener">Live demo</a>` : `<a class="pl gh" href="${u}" target="_blank" rel="noopener" aria-label="GitHub repo" title="GitHub"><svg viewBox="0 0 16 16" width="18" height="18" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38v-1.33c-2.23.48-2.7-1.07-2.7-1.07-.36-.92-.89-1.17-.89-1.17-.73-.5.06-.49.06-.49.8.06 1.23.83 1.23.83.72 1.22 1.88.87 2.33.66.07-.52.28-.87.5-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.83-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.6 7.6 0 0 1 4 0c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48v2.2c0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg></a>`).join("")}</span></div></div>`;'
assert old in m, "card line not found"
m = m.replace(old, new)
m = m.replace('const card = e.target.closest(".proj"); if (card)', 'const card = e.target.closest(".proj"); if (card && !e.target.closest(".plinks"))')
open("main.js", "w").write(m)
open("styles.css", "a").write('\n.pf{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:14px}\n.pf .open{margin-top:0}\n.plinks{display:flex;align-items:center;gap:8px}\n.pl{display:inline-flex;align-items:center;justify-content:center;border-radius:999px;font-weight:600;font-size:.82rem;transition:.2s}\n.pl.live{background:var(--a);color:#fff;padding:6px 14px}.pl.live:hover{background:var(--a-d)}\n.pl.gh{width:34px;height:34px;border:1px solid var(--line);color:var(--ink,#1f2937);background:#fff}.pl.gh:hover{border-color:var(--a);color:var(--a-d)}\n')
print("patched OK")
