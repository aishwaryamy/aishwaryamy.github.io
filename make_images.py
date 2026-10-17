"""Generates realistic browser-window mockups of each project's main page into ./img/."""
import os
os.makedirs("img", exist_ok=True)
F = "font-family='-apple-system,Segoe UI,Helvetica,Arial,sans-serif'"

def T(x, y, s, size=13, w=400, fill="#1f2937", anchor="start"):
    s = s.replace("&", "&amp;")
    return f"<text x='{x}' y='{y}' font-size='{size}' font-weight='{w}' fill='{fill}' text-anchor='{anchor}' {F}>{s}</text>"
def R(x, y, w, h, fill="#fff", rx=8, stroke="", sw=1):
    st = f" stroke='{stroke}' stroke-width='{sw}'" if stroke else ""
    return f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='{rx}' fill='{fill}'{st}/>"
def L(x, y, w, fill="#e5e7eb", h=7):
    return R(x, y, w, h, fill, h / 2)
def chip(x, y, s, bg, fg, w=None):
    w = w or (len(s) * 6.6 + 18)
    return R(x, y, w, 20, bg, 10) + T(x + w / 2, y + 14, s, 11, 600, fg, "middle")
def dot(x, y, r, fill):
    return f"<circle cx='{x}' cy='{y}' r='{r}' fill='{fill}'/>"

def browser(name, url, body, page="#f8fafc", chrome="#e5e7eb"):
    svg = f"""<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 450'>
<rect width='800' height='450' fill='{page}'/>
<rect width='800' height='34' fill='{chrome}'/>{dot(18,17,5,'#ef4444')}{dot(35,17,5,'#f59e0b')}{dot(52,17,5,'#22c55e')}
{R(150, 7, 500, 20, '#fff', 10)}{T(400, 21, url, 11, 500, '#6b7280', 'middle')}
<g transform='translate(0,34)'>{body}</g></svg>"""
    open(f"img/{name}.svg", "w").write(svg)

# ---------- RentGuard ----------
b = R(0, 0, 800, 46, "#fff") + R(0, 45, 800, 1, "#e5e7eb")
b += T(30, 29, "🛡️ RentGuard", 17, 800, "#0f766e") + T(770, 28, "NYC building safety", 12, 500, "#6b7280", "end")
b += T(400, 108, "Know your building before you sign.", 31, 800, "#0f172a", "middle")
b += T(400, 138, "Live HPD violations and 311 complaints, explained in plain English.", 14, 400, "#64748b", "middle")
b += R(150, 162, 500, 46, "#fff", 12, "#cbd5e1") + T(172, 190, "Enter an NYC address, e.g. 350 5th Ave, Manhattan", 14, 400, "#94a3b8")
b += R(662, 162, 0, 0) + R(520, 168, 122, 34, "#0d9488", 9) + T(581, 190, "Check building", 13, 700, "#fff", "middle")
for i, (t, s, col) in enumerate([("HPD violations", "Open and closed, by severity", "#fee2e2"), ("311 complaints", "Heat, noise, pests and more", "#fef3c7"), ("Ask a question", "Answers cite the records", "#ccfbf1")]):
    x = 60 + i * 235
    b += R(x, 245, 215, 140, "#fff", 14, "#e5e7eb") + dot(x + 30, 278, 14, col) + T(x + 54, 283, t, 14, 700, "#0f172a")
    b += T(x + 20, 318, s, 12, 400, "#64748b") + L(x + 20, 336, 150) + L(x + 20, 354, 110)
browser("rentguard", "rentguard.streamlit.app", b)

# ---------- Contact enrichment (matches the real dark split-screen layout) ----------
b = R(0, 0, 800, 416, "#0a0a0f")
b += R(0, 0, 330, 416, "#0f0f14") + R(329, 0, 1, 416, "#232327") + T(20, 30, "AI Contact Enrichment Agent", 13, 700, "#e2e8f0")
b += R(20, 50, 240, 34, "#1e1e28", 12) + T(34, 72, "Enrich Sarah Chen at Acme", 12, 500, "#e2e8f0")
b += R(20, 100, 290, 98, "#18181f", 12, "#232327") + L(34, 118, 240, "#2a2a35", 7) + L(34, 136, 258, "#2a2a35", 7) + L(34, 154, 200, "#2a2a35", 7) + chip(34, 170, "web_search", "#232336", "#a5b4fc", 80) + chip(122, 170, "company_intel", "#232336", "#a5b4fc", 96)
b += R(20, 360, 290, 38, "#18181f", 10, "#232327") + T(36, 383, "Message the agent…", 12, 400, "#62748e")
b += T(354, 30, "AI Agent Output", 13, 700, "#e2e8f0") + chip(704, 15, "Step 3 / 4", "#232336", "#a5b4fc", 76)
for i, (t, done) in enumerate([("Find contact", True), ("Research", True), ("Score fit", True), ("Draft email", False)]):
    x = 354 + i * 108
    b += R(x, 50, 100, 26, "#18181f", 8, "#232327") + dot(x + 14, 63, 5, "#22c55e" if done else "#6366f1") + T(x + 26, 67, t, 10, 600, "#cbd5e1")
b += R(354, 92, 424, 96, "#18181f", 12, "#232327") + dot(382, 120, 16, "#2f2f42") + T(408, 117, "Sarah Chen", 14, 700, "#f1f5f9") + T(408, 135, "VP of Sales · Acme", 11, 400, "#62748e")
b += chip(654, 106, "ICP fit: strong", "#12301f", "#4ade80", 108) + L(370, 158, 380, "#2a2a35", 7) + L(370, 172, 300, "#2a2a35", 7)
b += R(354, 202, 206, 94, "#18181f", 12, "#232327") + T(370, 226, "Buying signals", 12, 700, "#a5b4fc") + chip(370, 238, "Hiring SDRs", "#232336", "#c7d2fe") + chip(468, 238, "New funding", "#232336", "#c7d2fe") + chip(370, 264, "Stack change", "#232336", "#c7d2fe", 90)
b += R(572, 202, 206, 94, "#18181f", 12, "#232327") + T(588, 226, "ICP score", 12, 700, "#a5b4fc") + R(588, 242, 170, 10, "#2a2a35", 5) + R(588, 242, 138, 10, "#6366f1", 5) + L(588, 266, 150, "#2a2a35", 6) + L(588, 280, 110, "#2a2a35", 6)
b += R(354, 310, 424, 88, "#18181f", 12, "#232327") + T(370, 334, "Personalized outreach", 12, 700, "#a5b4fc") + L(370, 348, 390, "#2a2a35", 7) + L(370, 364, 360, "#2a2a35", 7) + L(370, 380, 280, "#2a2a35", 7)
browser("contact-enrichment", "ai-enrichment-agent.vercel.app", b, "#0a0a0f", "#1c1c24")

# ---------- NextHire ----------
b = R(0, 0, 800, 50, "#fff") + R(0, 49, 800, 1, "#e5e7eb") + T(30, 31, "NextHire", 17, 800, "#4338ca")
for i, t in enumerate(["Tracker", "Resume", "Cover letters", "Interview prep"]):
    b += T(190 + i * 110, 31, t, 13, 700 if i == 0 else 500, "#4338ca" if i == 0 else "#6b7280")
b += R(190, 44, 52, 3, "#4338ca", 2)
cols = [("Saved", "#e0e7ff", ["ML Engineer", "AI Engineer"]), ("Applied", "#fef3c7", ["Applied ML Engineer", "Data Scientist"]), ("Interview", "#dcfce7", ["AI Engineer", "ML Platform"]), ("Offer", "#fce7f3", ["Research Engineer"])]
for i, (t, col, jobs) in enumerate(cols):
    x = 30 + i * 187
    b += R(x, 72, 172, 320, "#f1f5f9", 12) + chip(x + 12, 84, t, col, "#312e81", 70)
    for j, role in enumerate(jobs):
        y = 118 + j * 92
        b += R(x + 10, y, 152, 80, "#fff", 10, "#e5e7eb") + dot(x + 28, y + 22, 9, "#c7d2fe") + T(x + 44, y + 26, role, 11, 700, "#1e1b4b")
        b += L(x + 22, y + 46, 100) + L(x + 22, y + 60, 70)
browser("nexthire", "nexthire.onrender.com", b)

# ---------- Incident response ----------
b = R(0, 0, 800, 416, "#0b1220") + R(0, 0, 210, 416, "#0f172a") + T(20, 34, "Incident Response", 14, 800, "#f8fafc")
for i, (s, col) in enumerate([("Checkout latency spike", "#ef4444"), ("Queue backlog growing", "#f59e0b"), ("Cache hit rate drop", "#f59e0b"), ("Cert expiry warning", "#22c55e")]):
    y = 62 + i * 58
    b += R(12, y, 186, 48, "#1e293b" if i == 0 else "#0f172a", 8) + dot(28, y + 24, 5, col) + T(42, y + 21, s, 11, 600, "#e2e8f0") + L(42, y + 31, 90, "#334155", 5)
b += T(240, 34, "Checkout latency spike", 17, 800, "#f8fafc") + chip(240, 46, "SEV-2 · investigating", "#7f1d1d", "#fecaca", 132)
b += R(240, 84, 540, 130, "#111827", 12, "#1f2937")
b += "<polyline points='256,190 320,184 380,188 440,176 480,120 510,200 570,186 640,190 700,182 760,184' fill='none' stroke='#38bdf8' stroke-width='3' stroke-linejoin='round'/>" + dot(480, 120, 6, "#ef4444")
b += T(240, 238, "Agent timeline", 12, 700, "#94a3b8")
for i, s in enumerate(["Pulled related runbooks (RAG)", "Queried recent deploys and logs", "Ranked likely root causes", "Drafted summary for on-call"]):
    y = 254 + i * 38
    b += dot(252, y + 10, 9, "#22c55e" if i < 3 else "#38bdf8") + T(270, y + 15, s, 13, 500, "#e2e8f0") + (R(251, y + 20, 2, 18, "#334155", 1) if i < 3 else "")
b += R(560, 254, 220, 140, "#111827", 12, "#1f2937") + T(574, 276, "Likely cause", 11, 700, "#94a3b8") + L(574, 290, 180, "#334155") + L(574, 306, 150, "#334155") + L(574, 322, 170, "#334155") + chip(574, 346, "pgvector", "#0c4a6e", "#bae6fd") + chip(640, 346, "Redis cache", "#0c4a6e", "#bae6fd")
browser("incident-response", "incident-agent.internal", b, "#0b1220", "#1f2937")

# ---------- Audit readiness ----------
b = R(0, 0, 800, 46, "#fff") + R(0, 45, 800, 1, "#e5e7eb") + T(30, 29, "Audit Readiness AI", 16, 800, "#075985") + chip(650, 13, "SOC 2 Type II", "#e0f2fe", "#075985", 100)
b += R(30, 66, 470, 330, "#fff", 14, "#e5e7eb")
b += R(150, 82, 330, 34, "#0ea5e9", 12) + T(166, 104, "Do we enforce MFA for production access?", 12, 500, "#fff")
b += T(52, 150, "Answer", 11, 700, "#0369a1") + L(52, 162, 400, "#cbd5e1", 8) + L(52, 180, 420, "#cbd5e1", 8) + L(52, 198, 310, "#cbd5e1", 8)
b += chip(52, 220, "CC6.1 Logical access", "#e0f2fe", "#075985", 140) + chip(200, 220, "Access policy v3", "#e0f2fe", "#075985", 118)
b += T(52, 268, "Retrieval comparison", 11, 700, "#0369a1")
for i, (n, wd) in enumerate([("Keyword", 120), ("Dense", 190), ("Hybrid", 250)]):
    y = 280 + i * 30
    b += T(52, y + 15, n, 12, 500, "#475569") + R(124, y + 4, 300, 10, "#e0f2fe", 5) + R(124, y + 4, wd, 10, "#0ea5e9" if i == 2 else "#7dd3fc", 5)
b += R(520, 66, 250, 330, "#fff", 14, "#e5e7eb") + T(538, 92, "Sources", 13, 700, "#0f172a")
for i, s in enumerate(["Access control policy", "Change management", "Incident response plan", "Vendor risk review"]):
    y = 108 + i * 68
    b += R(534, y, 222, 56, "#f0f9ff", 10) + dot(554, y + 28, 10, "#bae6fd") + T(574, y + 25, s, 12, 600, "#0c4a6e") + L(574, y + 35, 100, "#bae6fd", 5)
browser("audit-readiness", "audit-readiness.app", b, "#f0f9ff")

# ---------- Quantamind ----------
b = R(0, 0, 800, 46, "#fff") + R(0, 45, 800, 1, "#e5e7eb") + T(30, 29, "Quantamind", 16, 800, "#6b21a8") + chip(660, 13, "Runs offline", "#f3e8ff", "#6b21a8", 90) + dot(646, 23, 4, "#22c55e")
b += R(30, 64, 450, 332, "#fff", 12, "#e5e7eb") + T(50, 92, "Master Services Agreement", 14, 700, "#1f2937")
ys = [108, 124, 140]
for y in ys: b += L(50, y, 400, "#e5e7eb", 7)
b += R(44, 156, 422, 44, "#fef08a", 6) + L(54, 166, 380, "#a16207", 6) + L(54, 182, 300, "#ca8a04", 6)
for y in [214, 230, 246]: b += L(50, y, 400, "#e5e7eb", 7)
b += R(44, 262, 422, 30, "#fecaca", 6) + L(54, 272, 340, "#b91c1c", 6)
for y in [306, 322, 338, 354]: b += L(50, y, 380, "#e5e7eb", 7)
b += R(500, 64, 270, 332, "#faf5ff", 12, "#e9d5ff") + T(518, 90, "Extracted clauses", 13, 700, "#6b21a8")
for i, (n, r, bg, fg) in enumerate([("Termination", "Low", "#dcfce7", "#166534"), ("Liability cap", "High", "#fee2e2", "#991b1b"), ("Governing law", "Low", "#dcfce7", "#166534"), ("Indemnification", "Medium", "#fef3c7", "#92400e")]):
    y = 106 + i * 56
    b += R(514, y, 242, 46, "#fff", 10, "#e9d5ff") + T(530, y + 27, n, 12, 600, "#3b0764") + chip(690, y + 13, r, bg, fg, 56)
b += T(518, 350, "LoRA fine-tuned · Mistral 7B", 11, 600, "#7e22ce") + T(518, 368, "Local retrieval with FAISS", 11, 400, "#6b7280")
browser("quantamind", "localhost:8501", b, "#faf5ff")

# ---------- OpsPilot ----------
b = R(0, 0, 800, 416, "#fff") + R(0, 0, 190, 416, "#fdf2f8") + T(20, 32, "OpsPilot", 17, 800, "#9d174d")
for i, s in enumerate(["New chat", "Documents", "Memory", "Tools", "Settings"]):
    y = 56 + i * 40
    b += R(12, y, 166, 32, "#fbcfe8" if i == 0 else "#fdf2f8", 8) + T(28, y + 21, s, 12, 600, "#831843")
b += R(210, 20, 380, 38, "#fce7f3", 16) + T(226, 44, "Summarize the Q3 onboarding doc", 12, 500, "#831843")
b += R(210, 76, 360, 26, "#fdf2f8", 13, "#fbcfe8") + T(226, 94, "🔧 search_documents · 3 results", 11, 600, "#be185d")
b += R(210, 114, 380, 120, "#f8fafc", 14, "#e5e7eb") + L(228, 134, 330, "#cbd5e1", 8) + L(228, 154, 340, "#cbd5e1", 8) + L(228, 174, 300, "#cbd5e1", 8) + L(228, 194, 250, "#cbd5e1", 8)
b += R(210, 358, 380, 38, "#fff", 19, "#fbcfe8") + T(230, 382, "Message OpsPilot…", 12, 400, "#9ca3af") + R(542, 364, 40, 26, "#db2777", 13)
b += R(608, 20, 172, 376, "#fff", 12, "#fbcfe8") + T(624, 46, "Sources", 12, 700, "#9d174d")
for i in range(3):
    y = 60 + i * 76
    b += R(620, y, 148, 64, "#fdf2f8", 10) + T(632, y + 24, ["Onboarding.pdf", "Policy.docx", "Notes.md"][i], 11, 600, "#831843") + L(632, y + 36, 100, "#fbcfe8", 5)
b += chip(624, 300, "Memory on", "#fce7f3", "#be185d", 74)
browser("opspilot", "opspilot.app", b, "#fff")

# ---------- GTM copilot ----------
b = R(0, 0, 800, 416, "#fff") + R(0, 0, 200, 416, "#f6f8fa") + T(20, 34, "AI GTM Copilot", 15, 800, "#166534")
b += T(20, 74, "Filters", 12, 700, "#6b7280")
for i, s in enumerate(["Industry", "Company size", "Region"]):
    y = 88 + i * 52
    b += T(20, y + 10, s, 11, 500, "#6b7280") + R(20, y + 16, 160, 24, "#fff", 6, "#d1d5db")
b += T(224, 40, "Lead qualification", 20, 800, "#111827") + T(224, 62, "Research accounts and draft outreach with MCP workflows", 12, 400, "#6b7280")
b += R(224, 82, 556, 30, "#f6f8fa", 6)
for x, t in [(238, "Company"), (410, "Score"), (520, "Status"), (640, "Next step")]:
    b += T(x, 102, t, 11, 700, "#6b7280")
rows = [("Northwind Labs", 230, "Qualified", "#dcfce7", "#166534"), ("Globex Systems", 160, "Researching", "#fef3c7", "#92400e"), ("Initech Cloud", 200, "Qualified", "#dcfce7", "#166534"), ("Umbrella Data", 90, "New", "#e0e7ff", "#3730a3"), ("Hooli Analytics", 140, "Researching", "#fef3c7", "#92400e")]
for i, (n, sc, st, bg, fg) in enumerate(rows):
    y = 122 + i * 48
    b += R(224, y + 40, 556, 1, "#eef0f2") + dot(246, y + 18, 11, "#bbf7d0") + T(266, y + 23, n, 13, 600, "#111827")
    b += R(410, y + 13, 80, 8, "#e5e7eb", 4) + R(410, y + 13, sc * 80 / 230, 8, "#22c55e", 4) + chip(520, y + 8, st, bg, fg, 90) + L(640, y + 17, 100, "#e5e7eb")
b += R(224, 370, 556, 32, "#f0fdf4", 8, "#bbf7d0") + T(240, 391, "Draft outreach ready for Northwind Labs", 12, 600, "#166534")
browser("gtm-copilot", "ai-gtm-copilot.streamlit.app", b, "#fff")
print("wrote", len([f for f in os.listdir("img") if f.endswith(".svg")]), "images")
