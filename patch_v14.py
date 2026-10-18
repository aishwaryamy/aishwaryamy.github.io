h = open("index.html").read()
old = "family=Space+Grotesk:wght@500;600;700"
assert old in h, "font link not found"
h = h.replace(old, "family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500")
open("index.html", "w").write(h)

open("styles.css", "a").write("""
/* typography: elegant serif headings + mono labels */
:root{--serif:"Instrument Serif","Times New Roman",Georgia,serif;--mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace}
h1,h2,h3,.stat b,.how-n,.pc-back h3{font-family:var(--serif);font-weight:400;letter-spacing:-.01em}
.hero h1{font-weight:400;font-size:clamp(3rem,6.4vw,5.2rem);line-height:.98;letter-spacing:-.02em}
.title{font-weight:400;font-size:clamp(2.4rem,5vw,3.6rem);line-height:1.02}
.sub{font-weight:400;font-size:1.8rem}
.role{font-family:var(--serif);font-style:italic;font-weight:400;font-size:clamp(1.6rem,3.2vw,2.3rem)}
#type{font-style:italic}
.stat b{font-size:2.6rem}
.how-card h3,.proj h3,.edu h3,.tl h3,.timeline h3{font-size:1.5rem;line-height:1.15}
.proj.big .pb h3{font-size:2rem}
.touch h2{font-weight:400;font-size:clamp(2.4rem,5.4vw,3.8rem)}
.how-n{font-style:italic;font-size:2.2rem}
.brand{font-family:var(--serif);font-weight:400;font-size:1.35rem;letter-spacing:0}
.nav nav a,.hello,.badge,.tags i,.meta,.fact span,.how-card small,.pc-hint,.pc-live,.open-now,.chat-top span,.chat-foot,.foot,.open,.stat span,.edu time,.edu .when{font-family:var(--mono)}
.nav nav a{font-size:.74rem;text-transform:uppercase;letter-spacing:.09em}
.hello{font-size:.8rem;text-transform:uppercase;letter-spacing:.16em;font-weight:500}
.badge{font-weight:500;letter-spacing:.06em;font-size:.68rem}
.tags i{font-size:.72rem;font-style:normal}
.meta{font-size:.76rem;font-weight:500}.meta span{font-weight:400}
.fact span,.how-card small,.open,.stat span{font-size:.72rem;letter-spacing:.05em}
.how-card small{text-transform:uppercase;letter-spacing:.06em}
.proj .open{font-weight:500}
@media (max-width:600px){.hero h1{font-size:clamp(2.6rem,12vw,3.4rem)}}
""")
print("patched OK")
