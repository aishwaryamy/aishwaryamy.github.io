h = open("index.html").read()
old = "family=Instrument+Serif:ital@0;1"
assert old in h, "font link not found (did the serif patch run?)"
h = h.replace(old, "family=Space+Grotesk:wght@500;600;700")
open("index.html", "w").write(h)

open("styles.css", "a").write("""
/* bold geometric headings (Space Grotesk), mono labels, Inter body */
:root{--serif:"Space Grotesk",Inter,system-ui,sans-serif}
h1,h2,h3,.stat b,.how-n,.pc-back h3{font-weight:600;letter-spacing:-.025em}
.hero h1{font-weight:700;font-size:clamp(2.6rem,5.6vw,4.4rem);line-height:1.04;letter-spacing:-.03em}
.title{font-weight:700;font-size:clamp(2rem,4.4vw,3rem);line-height:1.08}
.sub{font-weight:600;font-size:1.5rem}
.role{font-style:normal;font-weight:600;font-size:clamp(1.3rem,2.6vw,1.9rem)}
#type{font-style:normal}
.stat b{font-size:2.1rem;font-weight:700}
.how-card h3,.proj h3,.edu h3,.tl h3,.timeline h3{font-size:1.25rem;font-weight:600;line-height:1.25}
.proj.big .pb h3{font-size:1.6rem}
.touch h2{font-weight:700;font-size:clamp(2.2rem,5vw,3.4rem);line-height:1.08}
.how-n{font-style:normal;font-size:1.8rem;font-weight:700}
.brand{font-weight:700;font-size:1.15rem}
@media (max-width:600px){.hero h1{font-size:clamp(2.4rem,11vw,3rem)}}
""")
print("patched OK")
