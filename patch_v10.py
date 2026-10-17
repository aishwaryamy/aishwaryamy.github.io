import re
swap = {
  "#0d9488": "#4f46e5", "#0b7a70": "#4338ca", "#d9f1ed": "#e0e7ff",
  "#0b6b63": "#4338ca", "#134e4a": "#6d28d9", "#f0fdfa": "#eef2ff",
  "rgba(13,148,136": "rgba(79,70,229", "rgba(251,250,247": "rgba(252,252,255",
  "#fbfaf7": "#fcfcff", "#f2f6f4": "#f5f6fd", "#e6e3da": "#e5e7f0",
}
for fn in ["styles.css", "main.js", "index.html"]:
    t = open(fn).read()
    for a, b in swap.items():
        t = t.replace(a, b)
    t = t.replace("%230d9488", "%234f46e5")  # favicon
    if fn == "styles.css":
        t = t.replace('font-family:"Plus Jakarta Sans",Inter,system-ui,sans-serif', 'font-family:"Space Grotesk",Inter,system-ui,sans-serif')
        t += """
/* startup look: soft indigo glow + gradient role text */
.hero{background:radial-gradient(900px 480px at 88% -5%,rgba(79,70,229,.11),transparent 62%),radial-gradient(700px 420px at 0% 35%,rgba(124,58,237,.07),transparent 60%)}
#type{background:linear-gradient(90deg,#4f46e5,#7c3aed);-webkit-background-clip:text;background-clip:text;color:transparent}
.btn.primary{background:linear-gradient(135deg,#4f46e5,#6d28d9);border-color:transparent}
.btn.primary:hover{filter:brightness(1.08)}
"""
    if fn == "index.html":
        t = t.replace("family=Plus+Jakarta+Sans:wght@600;700;800", "family=Space+Grotesk:wght@500;600;700")
    open(fn, "w").write(t)
print("patched OK")
