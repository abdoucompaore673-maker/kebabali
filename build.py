# Genera il sito di Ali pizzeria kebab Cesena: python3 build.py [indirizzo_base]
import os, sys, json, html, datetime
from dati import *
from arte import HERO_SVG, MAPPA, roundel, ico

DIR = os.path.dirname(os.path.abspath(__file__))
BASE = (sys.argv[1] if len(sys.argv) > 1 else "https://ali-pizzeria-kebab.github.io").rstrip("/")
e = lambda s: html.escape(str(s), quote=True)
EXT = 'target="_blank" rel="noopener noreferrer"'
ARR = '<svg class="ar" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'

def btn(t, href, kind="red", extra="", ico=True):
    return f'<a class="btn btn-{kind}" href="{href}"{extra}><span>{e(t)}</span>{ARR if ico else ""}</a>'

ORARI_JS = json.dumps({k: v for k, v in ORARI.items()})
TEL_CALL = "tel:" + TEL[1]
ORA = "10–23:30"

# ---------- testa ----------
FONTS = ["https://fonts.googleapis.com/css2?family=Anton&family=Instrument+Sans:wght@400;500;600;700&family=Caveat:wght@700&display=swap"]
SCHEMA = json.dumps({
    "@context": "https://schema.org", "@type": "Restaurant", "name": NOME, "url": BASE + "/", "image": BASE + "/og.jpg",
    "telephone": TEL[1], "servesCuisine": ["Kebab", "Pizza", "Halal"], "priceRange": "€",
    "address": {"@type": "PostalAddress", "streetAddress": INDIRIZZO, "postalCode": "47521", "addressLocality": "Cesena", "addressRegion": "FC", "addressCountry": "IT"},
    "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:00", "closes": "23:30"}],
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": GOOGLE_VOTO.replace(",", "."), "reviewCount": GOOGLE_N}}, ensure_ascii=False)

def head(title, desc, url):
    fl = ''.join(f'<link rel="stylesheet" href="{u}" media="print" onload="this.media=\'all\'"><noscript><link rel="stylesheet" href="{u}"></noscript>' for u in FONTS)
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><meta name="robots" content="noindex,nofollow">
<link rel="canonical" href="{url}"><meta name="theme-color" content="#1a1414">
<meta property="og:type" content="website"><meta property="og:locale" content="it_IT"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="icon" href="favicon.png" sizes="32x32"><link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>{fl}
<script>document.documentElement.classList.add('js')</script>'''

CSS = r'''
:root{--ink:#1a1414;--ink2:rgba(26,20,20,.74);--mute:rgba(26,20,20,.58);--ink3:#2a2121;--paper:#fff8ee;--cream:#fff1dc;--white:#fff;
--red:#d7262e;--red2:#b51c23;--yel:#ffc93c;--grn:#1e9e5a;--wt2:rgba(255,248,238,.8);--line:rgba(26,20,20,.12);--lined:rgba(255,248,238,.16);
--fd:"Anton","Arial Narrow","Roboto Condensed",Impact,sans-serif;--fb:"Instrument Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--fh:"Caveat","Comic Sans MS",cursive;
--ease:cubic-bezier(.23,1,.32,1);--ease-io:cubic-bezier(.77,0,.175,1);--s1:8px;--s2:16px;--s3:24px;--s4:32px;--s6:48px;--s8:64px;--s12:96px;--r:8px}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:84px;scrollbar-color:var(--red) var(--ink);color-scheme:light}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--paper);color:var(--ink);font:400 1rem/1.6 var(--fb);overflow-x:clip;font-size-adjust:from-font;accent-color:var(--red)}
::selection{background:var(--yel);color:var(--ink)}
@view-transition{navigation:auto}
@media (prefers-reduced-motion:reduce){@view-transition{navigation:none}}
img,svg{display:block;max-width:100%}
a{color:inherit}
h1,h2,h3{font-family:var(--fd);font-weight:400;line-height:.95;letter-spacing:.01em;margin:0;text-transform:uppercase;text-wrap:balance}
h2{font-size:clamp(2.6rem,1.6rem + 4.2vw,5.4rem)}
p{margin:0;text-wrap:pretty}
.wrap{width:min(1240px,100% - 40px);margin-inline:auto}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.skip{position:absolute;left:12px;top:-60px;z-index:200;background:var(--red);color:#fff;padding:12px 16px;border-radius:var(--r);font-weight:600}.skip:focus{top:12px}
:focus-visible{outline:3px solid var(--yel);outline-offset:3px;border-radius:4px}
.kick{font:600 .8rem/1 var(--fb);letter-spacing:.16em;text-transform:uppercase;display:flex;align-items:center;gap:10px}
.kick::before{content:"";width:22px;height:2px;background:currentColor}
.note{font:700 1.5rem/1.05 var(--fh);color:var(--yel)}
/* pulsanti */
.btn{position:relative;display:inline-flex;align-items:center;justify-content:center;gap:12px;min-height:54px;padding:0 24px;border-radius:var(--r);font:700 .92rem/1 var(--fb);letter-spacing:.06em;text-transform:uppercase;text-decoration:none;overflow:hidden;isolation:isolate;transition:transform .16s var(--ease);-webkit-tap-highlight-color:transparent;font-variant-numeric:tabular-nums}
.btn::before{content:"";position:absolute;inset:0;z-index:-1;transform:translateY(101%);transition:transform .38s var(--ease)}
.btn:hover::before{transform:none}.btn:active{transform:scale(.97)}
.btn .ar{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;transition:transform .3s var(--ease)}.btn:hover .ar{transform:translateX(4px)}
.btn-red{background:var(--red);color:#fff}.btn-red::before{background:var(--red2)}
.btn-yel{background:var(--yel);color:var(--ink)}.btn-yel::before{background:#ffd666}
.btn-white{background:#fff;color:var(--ink)}.btn-white::before{background:var(--cream)}
.btn-ink{background:var(--ink);color:#fff}.btn-ink::before{background:var(--ink3)}
@media (hover:none){.btn:hover::before{transform:translateY(101%)}.btn:hover .ar{transform:none}}
/* barra info e testata */
.info{background:#0f0b0b;color:var(--wt2);font-size:.82rem}
.info .wrap{display:flex;justify-content:space-between;gap:16px;min-height:38px;align-items:center}
.st{display:inline-flex;align-items:center;gap:8px}.dot{width:8px;height:8px;border-radius:50%;background:#8a7f78;flex:none}
.is-open .dot{background:#4fd67e;box-shadow:0 0 0 0 rgba(79,214,126,.6);animation:pulse 2s infinite}
@keyframes pulse{70%{box-shadow:0 0 0 8px rgba(79,214,126,0)}100%{box-shadow:0 0 0 0 rgba(79,214,126,0)}}
.info a{text-decoration:none;font-variant-numeric:tabular-nums}.info .mid{opacity:.8}
@media (max-width:760px){.info .mid{display:none}}
@media (max-width:520px){.hdr .brand small{display:none}.hdr .brand b{font-size:1.45rem}}
.hdr{position:sticky;top:0;z-index:50;background:rgba(26,20,20,.93);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);color:#fff;border-bottom:1px solid var(--lined);transition:box-shadow .3s}
.hdr.is-sc{box-shadow:0 10px 30px rgba(0,0,0,.35)}
.hdr .wrap{display:flex;align-items:center;gap:24px;min-height:72px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;margin-right:auto}
.brand .mk{width:50px;height:50px;flex:none}
.brand .mk-ring{transform-origin:60px 60px}
.brand b{display:block;font:400 1.55rem/.9 var(--fd);letter-spacing:.03em;text-transform:uppercase}
.brand b em{font-style:normal;color:var(--yel)}
.brand small{display:block;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;opacity:.72;margin-top:5px}
.nav{display:flex;gap:22px}.nav a{text-decoration:none;font-weight:500;font-size:.95rem;position:relative;padding:6px 0}
.nav a::after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;background:var(--yel);transform:scaleX(0);transform-origin:right;transition:transform .3s var(--ease)}
.nav a:hover::after{transform:scaleX(1);transform-origin:left}
.hdr .btn{min-height:46px;padding:0 18px}
.mnu{display:none;width:48px;height:48px;border-radius:10px;border:1.5px solid var(--lined);background:transparent;cursor:pointer;position:relative;padding:0;flex:none}
.mnu span{position:absolute;left:13px;right:13px;height:2.5px;border-radius:2px;background:#fff}.mnu span:nth-child(1){top:18px}.mnu span:nth-child(2){top:27px;right:19px}
@media (max-width:1060px){.nav{display:none}.mnu{display:block}.hdr .btn{display:none}}
.prog{position:fixed;left:0;top:0;height:3px;width:100%;z-index:60;background:var(--yel);transform-origin:0 50%;transform:scaleX(0);pointer-events:none}
@keyframes pgw{to{transform:scaleX(1)}}
@supports (animation-timeline:scroll()){html.sda .prog{animation:pgw linear both;animation-timeline:scroll(root block)}}
/* menu del telefono */
.mpanel{position:fixed;inset:0;z-index:90;background:var(--red);color:#fff;display:flex;flex-direction:column;justify-content:space-between;padding:calc(var(--cy,20px) + 76px) 24px calc(28px + env(safe-area-inset-bottom));clip-path:circle(0 at var(--ox,90%) var(--oy,40px));transition:clip-path .55s var(--ease-io);overflow-y:auto;margin:0;border:0;width:auto;height:auto;max-width:none;max-height:none;overscroll-behavior:contain}
.mpanel:not([open]){display:none}.mpanel::backdrop{background:transparent;overflow:hidden;overscroll-behavior:contain}
.mpanel.is-on{clip-path:circle(150% at var(--ox,90%) var(--oy,40px))}
.mclose{position:absolute;left:var(--cx,auto);top:var(--cy,20px);width:48px;height:48px;border-radius:10px;border:1.5px solid rgba(255,255,255,.4);background:transparent;cursor:pointer;padding:0}
.mclose span{position:absolute;left:12px;right:12px;top:22.75px;height:2.5px;background:#fff;border-radius:2px}.mclose span:first-child{transform:rotate(45deg)}.mclose span:last-child{transform:rotate(-45deg)}
.mlinks{display:flex;flex-direction:column}
.mlinks a{display:flex;align-items:baseline;gap:14px;font:400 clamp(2.4rem,1.6rem + 6vw,3.6rem)/1.02 var(--fd);text-transform:uppercase;text-decoration:none;padding:8px 0;opacity:0;transform:translateY(18px);transition:opacity .4s,transform .5s var(--ease)}
.mlinks a i{font:600 .78rem/1 var(--fb);font-style:normal;color:var(--yel);letter-spacing:.12em}
.mpanel.is-on .mlinks a{opacity:1;transform:none;transition-delay:.15s}
.mpanel.is-on .mlinks a:nth-child(2){transition-delay:.2s}.mpanel.is-on .mlinks a:nth-child(3){transition-delay:.25s}.mpanel.is-on .mlinks a:nth-child(4){transition-delay:.3s}.mpanel.is-on .mlinks a:nth-child(5){transition-delay:.35s}
.mfoot{display:grid;gap:8px;margin-top:var(--s4);color:var(--wt2)}.mtel{font:400 2.2rem/1 var(--fd);color:var(--yel);text-decoration:none;padding:6px 0;font-variant-numeric:tabular-nums}
/* hero */
.hero{background:var(--red);color:#fff;position:relative;overflow:hidden;min-height:calc(100svh - 110px);display:flex;align-items:center}
.hero::before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,transparent 0 46px,rgba(255,255,255,.05) 46px 92px);pointer-events:none}
.hero::after{content:"";position:absolute;right:-10%;top:-30%;width:70%;aspect-ratio:1;border-radius:50%;background:radial-gradient(closest-side,rgba(255,201,60,.28),transparent);pointer-events:none}
.hero-in{display:grid;grid-template-columns:1.05fr 1fr;gap:var(--s4);align-items:center;padding-block:var(--s8);position:relative;z-index:1}
.hstat{display:inline-flex;align-items:center;gap:12px;padding:10px 18px 10px 14px;border-radius:999px;background:rgba(26,20,20,.82);font-weight:600;font-size:1.02rem;font-variant-numeric:tabular-nums}
.hstat .dot{width:12px;height:12px}
.hero h1{font-size:clamp(3.2rem,1.9rem + 5.4vw,7.2rem);margin:var(--s3) 0 var(--s3)}
.hero h1 .l1{display:block;color:#fff}
.rot{display:block;color:var(--yel);height:1.02em;overflow:hidden;position:relative;white-space:nowrap}
.rot i{display:block;font-style:normal;position:absolute;left:0;top:0}
.hero .sub{font-size:clamp(1.05rem,.98rem + .35vw,1.22rem);color:var(--wt2);max-width:46ch}
.hero .sub b{color:#fff;font-weight:600}
.hero .cta{display:flex;flex-wrap:wrap;gap:14px;margin-top:var(--s4)}
.proof{display:flex;flex-wrap:wrap;gap:8px 22px;margin-top:var(--s4);font-size:.92rem;color:var(--wt2);align-items:center}
.proof .stars{color:var(--yel);letter-spacing:2px}.proof b{color:#fff}
.stage{position:relative;aspect-ratio:520/460;max-width:580px;justify-self:center;width:100%;cursor:pointer;-webkit-tap-highlight-color:transparent}
.scene{width:100%;height:100%;overflow:visible}
.tray{transform-box:view-box;transform-origin:260px 330px}
.dish{opacity:0;transform-box:view-box;transform-origin:260px 330px;transform:translateX(90px) rotate(10deg);transition:opacity .4s var(--ease),transform .7s var(--ease)}
.dish.on{opacity:1;transform:none}.dish.out{opacity:0;transform:translateX(-90px) rotate(-10deg)}
.stm{fill:none;stroke:rgba(255,255,255,.5);stroke-width:5;stroke-linecap:round;stroke-dasharray:40 140;animation:stm 3.4s linear infinite;animation-delay:calc(var(--i)*-1.1s)}
@keyframes stm{from{stroke-dashoffset:180;opacity:0}20%{opacity:1}to{stroke-dashoffset:0;opacity:0}}
.ptag{position:absolute;left:4%;top:8%;background:var(--yel);color:var(--ink);border-radius:10px;padding:10px 14px 12px;transform:rotate(-5deg);box-shadow:0 14px 30px -14px rgba(0,0,0,.55);min-width:150px;transition:transform .3s var(--ease)}
.ptag small{display:block;font:600 .72rem/1 var(--fb);letter-spacing:.12em;text-transform:uppercase;opacity:.75}
.ptag b{display:block;font:400 1.6rem/1.05 var(--fd);text-transform:uppercase;margin-top:6px}
.ptag span{display:block;font-weight:700;font-variant-numeric:tabular-nums;margin-top:2px}
.ptag.flip{animation:flip .5s var(--ease)}@keyframes flip{from{transform:rotate(-5deg) translateY(-10px) scale(.95);opacity:.2}}
.halal{position:absolute;right:2%;top:2%;width:clamp(96px,10vw,128px);aspect-ratio:1}.hring{transform-box:view-box;transform-origin:60px 60px;animation:spin 18s linear infinite}
.halal text{font:600 10.5px var(--fb);letter-spacing:.14em;fill:#fff}
@keyframes spin{to{transform:rotate(360deg)}}
.hn{position:absolute;font:700 1.55rem/1 var(--fh);color:var(--yel);display:flex;gap:8px;align-items:flex-start;pointer-events:none}
.hn svg{width:64px;height:42px;fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round}
.hn-1{left:-8%;bottom:4%;transform:rotate(-6deg)}
@media (max-width:1180px){.hn{display:none}}
@media (max-width:900px){.hero{min-height:0}.hero-in{grid-template-columns:1fr;padding-block:var(--s4) var(--s6)}.stage{max-width:420px}.hero h1{margin-top:var(--s2)}}
@media (max-width:600px){.stage{max-width:340px;margin-top:-4px}.ptag{min-width:0;padding:8px 12px 10px;left:0;top:4%}.ptag b{font-size:1.25rem}.halal{width:84px;right:0;top:0}}
/* nastri */
.tapes{position:relative;height:150px;overflow:hidden;background:var(--paper)}
.tape{position:absolute;left:-4%;right:-4%;top:50%;overflow:hidden;border-block:2px solid var(--ink)}
.tape .row{display:flex;width:max-content;animation:tape 38s linear infinite}
.tape span{font:400 1.65rem/1 var(--fd);text-transform:uppercase;letter-spacing:.04em;padding:14px 0;white-space:nowrap}
.tape span i{font-style:normal;margin:0 22px}
.t1{background:var(--ink);color:var(--yel);transform:translateY(-50%) rotate(-3deg);z-index:2}.t2{background:var(--grn);color:#fff;transform:translateY(-50%) rotate(2.5deg)}
.t2 .row{animation-direction:reverse}
@keyframes tape{to{transform:translateX(-50%)}}
/* sezioni */
.sec{padding-block:clamp(80px,6vw + 40px,150px)}
.sec-h{display:grid;grid-template-columns:1.2fr 1fr;gap:var(--s4);align-items:end;margin-bottom:var(--s8)}
.sec-h p.lead{color:var(--ink2);font-size:1.1rem;max-width:44ch}
.sec .kick{color:var(--red2);margin-bottom:var(--s2)}
@media (max-width:860px){.sec-h{grid-template-columns:1fr;margin-bottom:var(--s6)}}
/* quanto hai in tasca */
.budget{background:var(--paper)}
.budget h2 em{font-style:normal;color:var(--red)}
.bgrid{display:grid;grid-template-columns:.9fr 1.3fr;gap:var(--s6);align-items:start}
.bctl{position:sticky;top:100px;background:var(--ink);color:#fff;border-radius:18px;padding:var(--s4);overflow:hidden;isolation:isolate}
.bctl::after{content:"";position:absolute;right:-70px;top:-70px;width:200px;height:200px;border-radius:50%;background:var(--red);z-index:-1;opacity:.85}
.bctl label{display:block;font-weight:600;color:var(--wt2);margin-bottom:6px}
.bout{display:block;font:400 clamp(5rem,3.6rem + 5vw,8rem)/.9 var(--fd);color:var(--yel);font-variant-numeric:tabular-nums}
.bout small{font-size:.45em;color:#fff;margin-left:6px}
.brange{width:100%;margin:var(--s3) 0 6px;height:44px;-webkit-appearance:none;appearance:none;background:transparent;cursor:pointer;touch-action:pan-y}
.brange::-webkit-slider-runnable-track{height:10px;border-radius:999px;background:linear-gradient(90deg,var(--yel) var(--p,33%),rgba(255,255,255,.18) var(--p,33%))}
.brange::-moz-range-track{height:10px;border-radius:999px;background:rgba(255,255,255,.18)}.brange::-moz-range-progress{height:10px;border-radius:999px;background:var(--yel)}
.brange::-webkit-slider-thumb{-webkit-appearance:none;width:34px;height:34px;border-radius:50%;background:#fff;border:6px solid var(--red);margin-top:-12px;box-shadow:0 6px 16px rgba(0,0,0,.4);transition:transform .16s var(--ease)}
.brange::-moz-range-thumb{width:22px;height:22px;border-radius:50%;background:#fff;border:6px solid var(--red)}
.brange:active::-webkit-slider-thumb{transform:scale(1.12)}
.bscale{display:flex;justify-content:space-between;font-size:.85rem;color:var(--wt2);font-variant-numeric:tabular-nums}
.bquick{display:flex;flex-wrap:wrap;gap:8px;margin-top:var(--s3)}
.bquick button{min-height:44px;min-width:56px;padding:0 14px;border-radius:999px;border:1.5px solid var(--lined);background:transparent;color:#fff;font:600 .95rem/1 var(--fb);cursor:pointer;font-variant-numeric:tabular-nums;transition:background .2s,color .2s,transform .16s var(--ease)}
.bquick button:active{transform:scale(.97)}.bquick button[aria-pressed="true"]{background:var(--yel);color:var(--ink);border-color:var(--yel)}
.bnote{font-size:.85rem;color:var(--wt2);margin-top:var(--s3);max-width:40ch}
.bres{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:18px;align-items:start}
.rc{background:#fff;border-radius:6px;padding:20px 20px 28px;font:500 .95rem/1.5 ui-monospace,"SF Mono",Menlo,Consolas,monospace;color:#2a2020;box-shadow:0 22px 40px -26px rgba(60,20,10,.55);position:relative;
 -webkit-mask:radial-gradient(circle at 8px 100%,transparent 7px,#000 7.5px) 0 0/16px 100% repeat-x;mask:radial-gradient(circle at 8px 100%,transparent 7px,#000 7.5px) 0 0/16px 100% repeat-x;transform:rotate(var(--rt,0deg))}
.rc.new{animation:rcin .5s var(--ease) both;animation-delay:var(--d,0s)}@keyframes rcin{from{opacity:0;transform:translateY(16px) rotate(var(--rt,0deg))}}
.rc .tag{display:inline-block;font:600 .72rem/1 var(--fb);letter-spacing:.12em;text-transform:uppercase;background:var(--red);color:#fff;padding:6px 9px;border-radius:999px;margin-bottom:12px}
.rc h3{font:400 1.25rem/1 var(--fd);letter-spacing:.06em;text-align:center}
.rc .rsub{text-align:center;font-size:.74rem;opacity:.65;margin:4px 0 12px}
.rl{display:flex;justify-content:space-between;gap:12px;font-variant-numeric:tabular-nums}
.rl span:first-child{min-width:0}
.rdiv{border-top:2px dashed rgba(42,32,32,.32);margin:10px 0}
.rtot{font-weight:700;font-size:1.08rem}
.rleft{margin-top:8px;color:var(--grn);font-weight:700}
.rnone{grid-column:1/-1;background:#fff;border-radius:12px;padding:var(--s4);color:var(--ink2)}
.bcta{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-top:var(--s4)}
.bcta p{color:var(--mute);font-size:.9rem;max-width:40ch}
@media (max-width:960px){.bgrid{grid-template-columns:1fr}.bctl{position:relative;top:auto}}
/* menu */
.menu{background:#fff}
.mlayout{display:grid;grid-template-columns:240px 1fr;gap:var(--s6);align-items:start}
.midx{position:sticky;top:100px;display:grid;gap:2px}
.midx a{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:10px 14px;border-radius:8px;text-decoration:none;font-weight:500;color:var(--ink2);transition:background .2s,color .2s}
.midx a small{font-variant-numeric:tabular-nums;color:var(--mute);font-size:.8rem}
.midx a:hover{background:rgba(26,20,20,.05)}
.midx a.on{background:var(--red);color:#fff}.midx a.on small{color:var(--yel)}
.mcat{margin-bottom:var(--s8);scroll-margin-top:100px}
html.mtabs .mcat:not(.on){display:none}html.mtabs .mcat{margin-bottom:var(--s3);min-height:340px}
.mnext{display:none}html.mtabs .mnext{display:inline-flex;align-items:center;gap:10px;margin-top:var(--s4);padding:14px 18px;border-radius:var(--r);background:var(--ink);color:#fff;text-decoration:none;font-weight:600;transition:transform .16s var(--ease)}
.mnext .ar{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;transition:transform .3s var(--ease)}.mnext:hover .ar{transform:translateX(4px)}.mnext:active{transform:scale(.97)}
.mcat-h{display:flex;align-items:center;gap:16px;margin-bottom:var(--s3);padding-bottom:var(--s2);border-bottom:2px solid var(--ink)}
.mcat-h h3{font-size:clamp(2rem,1.5rem + 2vw,3rem)}
.mcat-h p{margin-left:auto;font:700 1.35rem/1 var(--fh);color:var(--red2);text-align:right}
.ci{width:46px;height:46px;flex:none;fill:none;stroke:var(--red);stroke-width:3;stroke-linecap:round;stroke-linejoin:round}
.items{display:grid;grid-template-columns:1fr 1fr;gap:6px 48px}
.item{padding:12px 0;border-bottom:1px solid var(--line)}
.item .top{display:flex;align-items:baseline;gap:10px}
.item b{font-weight:600;font-size:1.05rem}
.item .dots{flex:1;border-bottom:2px dotted rgba(26,20,20,.3);transform:translateY(-4px);min-width:16px}
.item .pr{font-weight:600;font-variant-numeric:tabular-nums;white-space:nowrap}
.item p{font-size:.9rem;color:var(--mute);margin-top:2px;max-width:46ch}
.item.ev b::after{content:"in evidenza";margin-left:8px;font:600 .66rem/1 var(--fb);letter-spacing:.1em;text-transform:uppercase;background:var(--yel);color:var(--ink);padding:4px 7px;border-radius:999px;vertical-align:3px}
.mnote{font-size:.88rem;color:var(--mute);margin-top:var(--s2)}
.mpills{display:none}
@media (max-width:960px){.mlayout{grid-template-columns:1fr}.midx{display:none}
 .mpills{display:flex;position:sticky;top:72px;z-index:20;gap:8px;overflow-x:auto;padding:12px 20px;margin:0 -20px var(--s4);background:rgba(255,255,255,.94);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);scrollbar-width:none;scroll-snap-type:x proximity}
 .mpills::-webkit-scrollbar{display:none}
 .mpills a{flex:none;scroll-snap-align:start;padding:10px 14px;border-radius:999px;border:1.5px solid var(--line);text-decoration:none;font-weight:500;font-size:.92rem;white-space:nowrap}
 .mpills a.on{background:var(--red);color:#fff;border-color:var(--red)}}
@media (max-width:700px){.items{grid-template-columns:1fr}.mcat-h p{display:none}}
/* ali e recensioni */
.rec{background:var(--red);color:#fff;position:relative;overflow:hidden}
.rec .kick{color:var(--yel)}.rec .sec-h p.lead{color:var(--wt2)}
.rec h2 em{font-style:normal;color:var(--yel)}
.rgrid{display:grid;grid-template-columns:320px 1fr;gap:var(--s6);align-items:start}
.score{position:sticky;top:110px;background:var(--ink);color:#fff;border-radius:16px;padding:var(--s4);text-align:center}
.score b{display:block;font:400 clamp(5.5rem,4rem + 5vw,8rem)/.85 var(--fd);color:var(--yel);font-variant-numeric:tabular-nums}
.score .stars{display:flex;justify-content:center;gap:6px;margin:16px 0 10px}
.score .stars i{width:26px;height:26px;background:var(--yel);clip-path:polygon(50% 0,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%);transform:scale(0);transition:transform .45s var(--ease)}
.score .stars i:last-child{background:linear-gradient(90deg,var(--yel) 70%,rgba(255,255,255,.25) 70%)}
.score.in .stars i{transform:none}.score.in .stars i:nth-child(2){transition-delay:.08s}.score.in .stars i:nth-child(3){transition-delay:.16s}.score.in .stars i:nth-child(4){transition-delay:.24s}.score.in .stars i:nth-child(5){transition-delay:.32s}
.score p{color:var(--wt2)}.score a{color:#fff}
.rcards{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.rv{background:#fff;color:var(--ink);border-radius:14px;padding:22px;margin:0;transition:transform .3s var(--ease),box-shadow .3s}
.rv:first-child{grid-column:1/-1}.rv:first-child blockquote{font:400 clamp(1.6rem,1.2rem + 1.4vw,2.3rem)/1.08 var(--fd);text-transform:uppercase}
.rv:hover{transform:translateY(-4px);box-shadow:0 18px 30px -22px rgba(0,0,0,.6)}
.rv-top{display:flex;align-items:center;gap:12px;margin-bottom:10px}
.av{width:40px;height:40px;border-radius:50%;background:var(--red);color:#fff;display:grid;place-items:center;font:400 1.2rem/1 var(--fd)}
.rv-top small{color:var(--mute);display:block;font-size:.8rem}
.rv blockquote{margin:0;font-size:1.03rem}
.frasi{display:flex;flex-wrap:wrap;gap:10px;margin-top:var(--s4)}
.frasi span{background:rgba(26,20,20,.28);border:1px solid rgba(255,255,255,.22);border-radius:999px;padding:9px 14px;font-size:.92rem}
.frasi span::before{content:"“";color:var(--yel);font-weight:700;margin-right:2px}.frasi span::after{content:"”";color:var(--yel);font-weight:700}
@media (max-width:900px){.rgrid{grid-template-columns:1fr}.score{position:static}.rcards{grid-template-columns:1fr}}
/* orari */
.visit{background:var(--paper)}
.vgrid{display:grid;grid-template-columns:1fr 1.1fr;gap:var(--s6);align-items:start}
.big7{display:flex;align-items:baseline;gap:14px;margin-top:var(--s3);flex-wrap:wrap}
.big7 b{font:400 clamp(3.6rem,2.6rem + 4vw,6rem)/.9 var(--fd);color:var(--red);font-variant-numeric:tabular-nums}
.big7 span{font-weight:600;color:var(--ink2);max-width:22ch}
.week{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin-top:var(--s4);list-style:none;padding:0}
.week li{background:#fff;border:1.5px solid var(--line);border-radius:10px;padding:12px 4px;text-align:center;font-size:.8rem;line-height:1.25;font-variant-numeric:tabular-nums}
.week li b{display:block;font:400 1.15rem/1 var(--fd);text-transform:uppercase;margin-bottom:4px}
.week li.today{background:var(--ink);color:#fff;border-color:var(--ink)}
.week li.today b{color:var(--yel)}
.now{display:inline-flex;align-items:center;gap:10px;margin-top:var(--s3);font-weight:600;padding:10px 14px;border-radius:999px;background:rgba(26,20,20,.06)}
.svc{display:flex;flex-wrap:wrap;gap:8px;margin-top:var(--s4);list-style:none;padding:0}
.svc li{padding:8px 12px;border-radius:999px;background:var(--cream);font-size:.88rem;font-weight:500}
.svc li:nth-child(2){background:var(--grn);color:#fff}
.addr{font:400 clamp(2rem,1.5rem + 2vw,3rem)/.98 var(--fd);text-transform:uppercase;margin:var(--s2) 0}
.mapbox{border-radius:16px;overflow:hidden;border:2px solid var(--ink);margin-top:var(--s3)}
.map{width:100%;height:auto}.map .rd{fill:none;stroke:#fff;stroke-width:16;stroke-linecap:round}.map .rd-s{stroke-width:10}
.map .mt{font:600 13px var(--fb);fill:#6b5d52}.map .mt-w{fill:#fff;font-size:12.5px;font-weight:600}.map .mt-w2{fill:var(--yel);font-size:11px}
.map .route{fill:none;stroke:var(--red);stroke-width:4;stroke-dasharray:6 8;stroke-linecap:round}
.mapbox.in .route{animation:route 1.6s linear infinite}@keyframes route{to{stroke-dashoffset:-28}}
.pulse{transform-box:fill-box;transform-origin:center;animation:pp 2s ease-out infinite}@keyframes pp{from{transform:scale(.4);opacity:.6}to{transform:scale(1.8);opacity:0}}
.vbtns{display:flex;gap:12px;flex-wrap:wrap;margin-top:var(--s3)}
@media (max-width:900px){.vgrid{grid-template-columns:1fr}}
@media (max-width:520px){.week{grid-template-columns:repeat(4,1fr)}}
/* chiusura e piede */
.final{background:var(--ink);color:#fff;text-align:center;overflow:hidden;position:relative;padding-block:clamp(90px,8vw + 40px,170px)}
.final h2{font-size:clamp(4rem,2rem + 11vw,12rem);line-height:.88}
.final h2 .o{color:transparent;-webkit-text-stroke:2px var(--yel)}
.final p{color:var(--wt2);margin:var(--s3) auto 0;max-width:40ch;font-size:1.1rem}
.final .cta{display:flex;justify-content:center;gap:14px;flex-wrap:wrap;margin-top:var(--s4)}
.foot{background:#0f0b0b;color:var(--wt2);padding:var(--s8) 0 calc(var(--s4) + 80px);font-size:.95rem}
.fgrid{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:var(--s4)}
.foot .brand{color:#fff;margin:0}
.foot .fh{font:400 1.1rem/1 var(--fd);text-transform:uppercase;letter-spacing:.06em;color:#fff;margin:0 0 12px}
.foot a{text-decoration:none}.foot a:hover{color:var(--yel)}
.foot p+p{margin-top:6px}
.fbot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:var(--s6);padding-top:var(--s3);border-top:1px solid var(--lined);font-size:.85rem}
#calm{background:none;border:1px solid var(--lined);color:var(--wt2);border-radius:999px;padding:8px 14px;cursor:pointer;font:inherit;min-height:40px}
@media (max-width:860px){.fgrid{grid-template-columns:1fr 1fr}}
@media (min-width:861px){.foot{padding-bottom:var(--s4)}}
/* barra in basso sul telefono */
.mbar{position:fixed;left:12px;right:12px;bottom:calc(12px + env(safe-area-inset-bottom));z-index:40;display:none;gap:10px;transform:translateY(140%);transition:transform .4s var(--ease)}
.mbar.on{transform:none}.mbar .btn{flex:1 1 0;min-width:0;min-height:52px;padding:0 10px;letter-spacing:.02em;font-size:.84rem;gap:8px;white-space:nowrap;box-shadow:0 12px 26px -12px rgba(0,0,0,.6)}.mbar .btn-ink{border:1px solid var(--lined)}.mbar .ar{display:none}
@media (max-width:860px){.mbar{display:flex}}
/* sipario */
.intro{display:none}
html.is-intro .intro{display:grid;place-items:center;position:fixed;inset:0;z-index:300;background:var(--red);animation:introOut .6s var(--ease-io) 1.15s forwards}
.intro .mk{width:116px;height:116px;animation:introIn .7s var(--ease) both}
.intro .mk-ring{transform-origin:60px 60px;animation:spin 2.4s linear infinite}
@keyframes introIn{from{transform:scale(.9) rotate(-20deg);opacity:0}}
@keyframes introOut{to{clip-path:inset(0 0 100% 0)}}
/* comparse */
.js [data-r]{opacity:0;transform:translateY(24px);transition:opacity .7s var(--ease),transform .8s var(--ease);transition-delay:var(--d,0s)}
.js [data-r].in{opacity:1;transform:none}
.js h2[data-r]{opacity:1;transform:none}
.js h2[data-r] .w{display:inline-block;transform:translateY(105%);transition:transform .8s var(--ease);transition-delay:calc(var(--wi)*.05s)}
.js h2[data-r] .wl{display:inline-block;overflow:hidden;vertical-align:top;padding-bottom:.06em;margin-bottom:-.06em}
.js h2[data-r].in .w{transform:none}
.grain{position:fixed;inset:0;pointer-events:none;z-index:70;opacity:.05;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
@media (hover:none){.grain{display:none}}
/* calma e movimento ridotto */
html.calm *,html.calm *::before,html.calm *::after{animation:none!important;transition-duration:.01ms!important}
html.calm [data-r],html.calm h2[data-r] .w{opacity:1!important;transform:none!important}
html.calm .mlinks a{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition-duration:.01ms!important}.js [data-r],.js h2[data-r] .w{opacity:1!important;transform:none!important}.mlinks a{opacity:1!important;transform:none!important}}
'''

JS = r'''
(function(){
 var html=document.documentElement,reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
 function run(f){try{f()}catch(err){console.error(err)}}
 function calm(){return reduced||html.classList.contains('calm')}
 try{if(localStorage.getItem('ali-calm')==='1')html.classList.add('calm')}catch(e){}
 var ORARI=%%ORARI%%,GIORNI=%%GIORNI%%;
 function roma(){var p=new Intl.DateTimeFormat('it-IT',{timeZone:'Europe/Rome',weekday:'short',hour:'2-digit',minute:'2-digit',hour12:false}).formatToParts(new Date()),o={};p.forEach(function(x){o[x.type]=x.value});
  var wd={'lun':0,'mar':1,'mer':2,'gio':3,'ven':4,'sab':5,'dom':6}[o.weekday.replace('.','').slice(0,3).toLowerCase()];return {d:wd,m:(+o.hour%24)*60+(+o.minute)}}
 function mins(s){var a=s.split(':');return +a[0]*60+(+a[1])}
 function stato(){var t=roma(),sl=ORARI[t.d]||[];for(var i=0;i<sl.length;i++){if(t.m>=mins(sl[i][0])&&t.m<mins(sl[i][1])){var left=mins(sl[i][1])-t.m;return {open:true,txt:left<=45?'Aperto ancora per '+left+' minuti · chiude alle '+sl[i][1]:'Aperto ora · chiude alle '+sl[i][1],d:t.d}}}
  for(var j=0;j<sl.length;j++){if(t.m<mins(sl[j][0]))return {open:false,txt:'Chiuso ora · apre alle '+sl[j][0],d:t.d}}
  for(var k=1;k<8;k++){var dd=(t.d+k)%7,s2=ORARI[dd]||[];if(s2.length)return {open:false,txt:'Chiuso ora · riapre '+(k===1?'domani':GIORNI[dd].toLowerCase())+' alle '+s2[0][0],d:t.d}}
  return {open:false,txt:'',d:t.d}}
 run(function(){var s=stato();[].forEach.call(document.querySelectorAll('[data-stato]'),function(el){el.classList.toggle('is-open',s.open);var t=el.querySelector('.t');if(t&&s.txt)t.textContent=s.txt});
  var li=document.querySelector('.week li[data-d="'+s.d+'"]');if(li){li.classList.add('today');li.setAttribute('aria-current','date')}});

 // testata, barra di avanzamento, barra del telefono, marchio che gira
 run(function(){var h=document.querySelector('.hdr'),bar=document.querySelector('.mbar'),hero=document.querySelector('.hero'),ring=document.querySelector('.hdr .mk-ring'),pg=document.querySelector('.prog'),tk=false;
  var sda=!reduced&&window.CSS&&CSS.supports&&CSS.supports('animation-timeline: scroll()');if(sda){html.classList.add('sda');pg=null}
  function u(){tk=false;var y=scrollY,mx=document.documentElement.scrollHeight-innerHeight;if(pg)pg.style.transform='scaleX('+(mx>0?Math.min(1,y/mx):0).toFixed(4)+')';
   h.classList.toggle('is-sc',y>8);if(bar)bar.classList.toggle('on',y>hero.offsetHeight*.6);if(ring&&!calm())ring.setAttribute('transform','rotate('+(y*.2%360).toFixed(1)+' 60 60)')}
  addEventListener('scroll',function(){if(!tk){tk=true;requestAnimationFrame(u)}},{passive:true});u()});

 // il vassoio: parola che cambia, piatto che passa, cartellino del prezzo
 run(function(){var rot=document.querySelector('.rot'),W=%%ROT%%,T=%%TAGS%%,S=['panino','biryani','pizza','seekh'],i=0,svg=document.querySelector('.scene'),stage=document.querySelector('.stage'),tag=document.querySelector('.ptag');if(!rot||!svg)return;
  var dishes=S.map(function(n){return svg.querySelector('.d-'+n)});dishes[0].classList.add('on');
  function show(n,prev){dishes.forEach(function(s,k){s.classList.remove('out');s.classList.toggle('on',k===n)});if(prev!=null&&!calm()){var o=dishes[prev];o.classList.add('out');setTimeout(function(){o.classList.remove('out')},700)}
   if(tag){tag.querySelector('b').textContent=T[n][0];tag.querySelector('span').textContent=T[n][1];if(!calm()){tag.classList.remove('flip');void tag.offsetWidth;tag.classList.add('flip')}}}
  function next(){var prev=i;i=(i+1)%W.length;var old=[].slice.call(rot.querySelectorAll('i'));old.forEach(function(o,k){if(k<old.length-1){o.remove();return}
    if(o.animate&&!calm())o.animate([{transform:'none',opacity:1},{transform:'translateY(-100%)',opacity:0}],{duration:420,easing:'cubic-bezier(.77,0,.175,1)',fill:'forwards'}).onfinish=function(){o.remove()};else o.remove()});
   if(window.__fitRot)window.__fitRot();var n=document.createElement('i');n.textContent=W[i];rot.appendChild(n);
   if(n.animate&&!calm())n.animate([{transform:'translateY(100%)',opacity:0},{transform:'none',opacity:1}],{duration:520,easing:'cubic-bezier(.23,1,.32,1)'});
   rot.setAttribute('aria-label',W[i]);show(i,prev)}
  setInterval(function(){if(document.hidden||calm())return;next()},3400);
  stage.addEventListener('click',next);stage.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();next()}});
  if(calm()&&svg.pauseAnimations)svg.pauseAnimations()});

 // la parola che cambia sta sempre in una riga
 run(function(){var rot=document.querySelector('.rot');if(!rot)return;var W=%%ROT%%;function fit(){rot.style.fontSize='';var cs=getComputedStyle(rot),m=document.createElement('span');m.style.cssText='position:absolute;visibility:hidden;white-space:nowrap;text-transform:uppercase';m.style.fontFamily=cs.fontFamily;m.style.fontWeight=cs.fontWeight;m.style.fontSize=cs.fontSize;m.style.letterSpacing=cs.letterSpacing;document.body.appendChild(m);
  var w=0;W.forEach(function(t){m.textContent=t;w=Math.max(w,m.getBoundingClientRect().width)});m.remove();var av=rot.parentNode.getBoundingClientRect().width;if(w>av){rot.style.fontSize=(parseFloat(cs.fontSize)*av/w*.98)+'px'}}
  window.__fitRot=fit;fit();if(document.fonts){document.fonts.ready.then(fit);document.fonts.addEventListener&&document.fonts.addEventListener('loadingdone',fit)}addEventListener('resize',fit)});

 // titoli parola per parola
 run(function(){[].forEach.call(document.querySelectorAll('h2[data-r]'),function(h){var k=0;function walk(n){[].slice.call(n.childNodes).forEach(function(c){if(c.nodeType===3){var f=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(function(w){if(!w)return;if(/^\s+$/.test(w)){f.appendChild(document.createTextNode(w));return}var o=document.createElement('span');o.className='wl';var x=document.createElement('span');x.className='w';x.style.setProperty('--wi',k++);x.textContent=w;o.appendChild(x);f.appendChild(o)});c.replaceWith(f)}else if(c.nodeType===1&&c.tagName!=='BR')walk(c)})}walk(h)})});

 // comparse
 run(function(){var els=[].slice.call(document.querySelectorAll('[data-r],.score,.mapbox'));if(!('IntersectionObserver' in window)){els.forEach(function(x){x.classList.add('in')});return}
  var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{rootMargin:'0px 0px -8% 0px'});els.forEach(function(x){io.observe(x)})});

 // quanto hai in tasca
 run(function(){var r=document.getElementById('brange'),out=document.getElementById('bout'),box=document.getElementById('bres');if(!r||!box)return;var M=%%MAINS%%,SD=%%SIDES%%,DR=%%DRINKS%%,LB=%%LABELS%%,last='',tm;
  function eur(c){return (c/100).toFixed(2).replace('.',',')+' €'}
  function esc(s){return s.replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function combos(B){var all=[];M.forEach(function(m){if(m.p>B)return;if(m.c==='menu'){all.push({c:m.c,it:[m],t:m.p,sc:m.p+90});return}var best=null;
    [null].concat(SD).forEach(function(s){[null].concat(DR).forEach(function(d){var t=m.p+(s?s.p:0)+(d?d.p:0);if(t>B)return;var sc=t+(d?60:0)+(s?30:0);if(!best||sc>best.sc)best={c:m.c,it:[m,s,d].filter(Boolean),t:t,sc:sc}})});all.push(best)});
   all.sort(function(a,b){return b.sc-a.sc||b.t-a.t});var pick=[],cats={};all.forEach(function(x){if(pick.length<3&&!cats[x.c]){cats[x.c]=1;pick.push(x)}});all.forEach(function(x){if(pick.length<3&&pick.indexOf(x)<0&&!pick.some(function(p){return p.it[0].n===x.it[0].n}))pick.push(x)});return pick}
  function draw(){var B=+r.value*100;out.innerHTML=r.value+'<small>€</small>';r.style.setProperty('--p',((r.value-r.min)/(r.max-r.min)*100)+'%');
   [].forEach.call(document.querySelectorAll('.bquick button'),function(b){b.setAttribute('aria-pressed',b.dataset.v===r.value?'true':'false')});
   var cs=combos(B),key=cs.map(function(c){return c.it.map(function(x){return x.n}).join('+')}).join('|');if(key===last)return;last=key;
   if(!cs.length){box.innerHTML='<p class="rnone">Con '+r.value+' euro non c\'è ancora un piatto nel menu online: alza un po\' il cursore.</p>';return}
   box.innerHTML=cs.map(function(c,k){var h='<article class="rc'+(calm()?'':' new')+'" style="--d:'+(k*.07)+'s;--rt:'+[-1.2,.8,-.4][k]+'deg"><span class="tag">'+LB[c.c]+'</span><h3>ALI PIZZERIA KEBAB</h3><p class="rsub">Corso Cavour 155 · Cesena</p>';
    c.it.forEach(function(x){h+='<div class="rl"><span>1 × '+esc(x.n)+'</span><span>'+eur(x.p)+'</span></div>'});
    if(c.c==='menu')h+='<div class="rl" style="opacity:.65;font-size:.85rem"><span>  '+esc(c.it[0].d)+'</span><span></span></div>';
    h+='<div class="rdiv"></div><div class="rl rtot"><span>TOTALE</span><span>'+eur(c.t)+'</span></div>';var left=B-c.t;h+='<p class="rleft">'+(left>0?'Ti avanzano '+eur(left):'Spesi giusti giusti')+'</p></article>';return h}).join('')}
  r.addEventListener('input',draw);
  [].forEach.call(document.querySelectorAll('.bquick button'),function(b){b.addEventListener('click',function(){r.value=b.dataset.v;draw()})});
  draw()});

 // menu a schede: l'indice resta a sinistra, a destra solo la categoria scelta
 run(function(){var cats=[].slice.call(document.querySelectorAll('.mcat'));if(!cats.length)return;var links=[].slice.call(document.querySelectorAll('.midx a,.mpills a,.mnext')),pills=document.querySelector('.mpills'),box=document.querySelector('.mlayout');
  html.classList.add('mtabs');
  function show(id,scroll){var c=document.getElementById(id);if(!c)return;cats.forEach(function(x){var on=x===c;x.classList.toggle('on',on);x.hidden=!on});
   [].forEach.call(document.querySelectorAll('.midx a,.mpills a'),function(a){var on=a.getAttribute('href')==='#'+id;a.classList.toggle('on',on);if(on)a.setAttribute('aria-current','true');else a.removeAttribute('aria-current');if(on&&a.parentNode===pills)pills.scrollTo({left:a.offsetLeft-20,behavior:calm()?'auto':'smooth'})});
   if(!calm()&&c.animate)c.animate([{opacity:0,transform:'translateY(14px)'},{opacity:1,transform:'none'}],{duration:320,easing:'cubic-bezier(.23,1,.32,1)'});
   if(scroll){var mob=window.matchMedia('(max-width:960px)').matches,top=(mob?pills:box).getBoundingClientRect().top;if(top<0||top>innerHeight*.6){var y=scrollY+box.getBoundingClientRect().top-(mob?150:96);scrollTo({top:y,behavior:calm()?'auto':'smooth'})}}}
  window.__menuShow=show;
  links.forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();show(a.getAttribute('href').slice(1),true)})});
  show(cats[0].id,false)});

 // numero del voto
 run(function(){var b=document.querySelector('.score b');if(!b||calm()||!('IntersectionObserver' in window))return;var end=+b.dataset.v,io=new IntersectionObserver(function(es){if(!es[0].isIntersecting)return;io.disconnect();var t0=performance.now();
  (function st(t){var k=Math.min(1,(t-t0)/1100),e=1-Math.pow(1-k,3);b.textContent=(end*e).toFixed(1).replace('.',',');if(k<1)requestAnimationFrame(st)})(t0)});b.textContent='0,0';io.observe(b)});

 // menu del telefono
 run(function(){var b=document.querySelector('.mnu'),p=document.getElementById('mpanel');if(!b||!p)return;var x=p.querySelector('.mclose'),nat=typeof p.showModal==='function';
  function open(){if(p.open)return;var r=b.getBoundingClientRect();p.style.setProperty('--ox',(r.left+r.width/2)+'px');p.style.setProperty('--oy',(r.top+r.height/2)+'px');p.style.setProperty('--cx',r.left+'px');p.style.setProperty('--cy',r.top+'px');
   if(nat)p.showModal();else p.setAttribute('open','');b.setAttribute('aria-expanded','true');requestAnimationFrame(function(){requestAnimationFrame(function(){p.classList.add('is-on')})});x.focus()}
  function close(back){if(!p.open)return;p.classList.remove('is-on');b.setAttribute('aria-expanded','false');setTimeout(function(){if(!p.classList.contains('is-on')){if(nat)p.close();else p.removeAttribute('open');if(back)b.focus()}},calm()?0:560)}
  b.addEventListener('click',open);x.addEventListener('click',function(){close(true)});p.addEventListener('cancel',function(e){e.preventDefault();close(true)});
  [].forEach.call(p.querySelectorAll('.mlinks a'),function(a){a.addEventListener('click',function(){close(false)})});
  if(!nat)document.addEventListener('keydown',function(e){if(e.key==='Escape'&&p.open)close(true)});
  matchMedia('(min-width:1061px)').addEventListener&&matchMedia('(min-width:1061px)').addEventListener('change',function(m){if(m.matches&&p.open)close(false)})});

 // ferma le animazioni
 run(function(){var c=document.getElementById('calm');if(!c)return;function s(){var on=html.classList.contains('calm');c.setAttribute('aria-pressed',on);c.textContent=on?'Riattiva le animazioni':'Ferma le animazioni';var sv=document.querySelector('.scene');if(sv&&sv.pauseAnimations){on?sv.pauseAnimations():sv.unpauseAnimations()}}
  s();c.addEventListener('click',function(){html.classList.toggle('calm');try{localStorage.setItem('ali-calm',html.classList.contains('calm')?'1':'0')}catch(e){}s()})});
})();
'''

# ---------- contenuti ----------
cents = lambda p: int(round(float(p.replace(",", ".")) * 100))
CAT = {k: items for k, t, s, items in MENU}
ROT = ["un panino kebab", "il riso biryani", "una pizza", "un seekh kebab"]
PI = {n: p for k, t, s, items in MENU for n, d, p in items}
TAGS = [["Panino Kebab", PI["Panino Kebab"] + " €"], ["Riso Biryani", "prezzo al banco"], ["Pizza rossa", "da " + min(CAT["pizze"], key=lambda x: cents(x[2]))[2] + " €"], ["Seekh Kebab", PI["Seekh Kebab"] + " €"]]

# per "quanto hai in tasca": piatti, contorni e bibite del menu online
MAINS = [{"n": n, "p": cents(p), "c": k, "d": d} for k in ("kebab", "menu", "pizze", "panini") for n, d, p in CAT[k]]
SIDES = [{"n": n, "p": cents(p)} for n, d, p in CAT["fritti"] if n in ("Patatine fritte", "Onion rings", "Crocchette di patate", "Mozzarella sticks")]
DRINKS = [{"n": n, "p": cents(p)} for n, d, p in CAT["bevande"] if n in ("Acqua naturale 50 cl", "Lattina 33 cl")]
LABELS = {"kebab": "Kebab", "menu": "Menù completo", "pizze": "Pizza", "panini": "Burger e hot dog"}

def combos(B):
    allc = []
    for m in MAINS:
        if m["p"] > B: continue
        if m["c"] == "menu":
            allc.append({"c": m["c"], "it": [m], "t": m["p"], "sc": m["p"] + 90}); continue
        best = None
        for s in [None] + SIDES:
            for d in [None] + DRINKS:
                t = m["p"] + (s["p"] if s else 0) + (d["p"] if d else 0)
                if t > B: continue
                sc = t + (60 if d else 0) + (30 if s else 0)
                if not best or sc > best["sc"]:
                    best = {"c": m["c"], "it": [x for x in (m, s, d) if x], "t": t, "sc": sc}
        allc.append(best)
    allc.sort(key=lambda x: (-x["sc"], -x["t"]))
    pick, cats = [], set()
    for x in allc:
        if len(pick) < 3 and x["c"] not in cats: cats.add(x["c"]); pick.append(x)
    for x in allc:
        if len(pick) < 3 and x not in pick and not any(p["it"][0]["n"] == x["it"][0]["n"] for p in pick): pick.append(x)
    return pick

eu = lambda c: f"{c/100:.2f}".replace(".", ",") + " €"
def rcard(c, k, B):
    h = f'<article class="rc" style="--rt:{[-1.2, .8, -.4][k]}deg"><span class="tag">{LABELS[c["c"]]}</span><h3>ALI PIZZERIA KEBAB</h3><p class="rsub">Corso Cavour 155 · Cesena</p>'
    h += ''.join(f'<div class="rl"><span>1 × {e(x["n"])}</span><span>{eu(x["p"])}</span></div>' for x in c["it"])
    if c["c"] == "menu": h += f'<div class="rl" style="opacity:.65;font-size:.85rem"><span>  {e(c["it"][0]["d"])}</span><span></span></div>'
    left = B - c["t"]
    return h + f'<div class="rdiv"></div><div class="rl rtot"><span>TOTALE</span><span>{eu(c["t"])}</span></div><p class="rleft">{"Ti avanzano " + eu(left) if left > 0 else "Spesi giusti giusti"}</p></article>'
BRES0 = ''.join(rcard(c, k, 1000) for k, c in enumerate(combos(1000)))
QUICK = ''.join(f'<button type="button" data-v="{v}" aria-pressed="{"true" if v == 10 else "false"}">{v} €</button>' for v in (5, 7, 10, 12, 15, 20))

def mitem(n, d, p):
    return f'<div class="item"><div class="top"><b>{e(n)}</b><span class="dots"></span><span class="pr">{e(p)} €</span></div>{f"<p>{e(d)}</p>" if d else ""}</div>'
EVID = '<div class="item ev"><div class="top"><b>Riso Biryani</b><span class="dots"></span><span class="pr">al banco</span></div><p>Tra i piatti in evidenza sulla scheda Google: il prezzo non è nel menu online, chiedilo ad Ali.</p></div>'
NEXT = {MENU[i][0]: f'<a class="mnext" href="#m-{MENU[(i+1)%len(MENU)][0]}">Poi: {e(MENU[(i+1)%len(MENU)][1])} {ARR}</a>' for i in range(len(MENU))}
MENU_HTML = ''.join(f'''<div class="mcat" id="m-{k}"><div class="mcat-h">{ico(k)}<h3>{e(t)}</h3>{f"<p>{e(s)}</p>" if s else ""}</div><div class="items">{"".join(mitem(*it) for it in items)}{EVID if k == "kebab" else ""}</div>{NEXT[k]}</div>''' for k, t, s, items in MENU)
MIDX = ''.join(f'<a href="#m-{k}"><span>{e(t)}</span><small>{len(items) + (1 if k == "kebab" else 0)}</small></a>' for k, t, s, items in MENU)
MPILLS = ''.join(f'<a href="#m-{k}">{e(t)}</a>' for k, t, s, items in MENU)
NVOCI = sum(len(m[3]) for m in MENU) + 1

RECS = ''.join(f'<figure class="rv" data-r style="--d:{i*0.06:.2f}s"><div class="rv-top"><span class="av" aria-hidden="true">{e(n[0])}</span><div><b>{e(n)}</b><small>Google · {e(q)}</small></div></div><blockquote><p>{e(t)}</p></blockquote></figure>' for i, (n, q, t) in enumerate(RECENSIONI))
FR = ''.join(f'<span>{e(f.rstrip("."))}</span>' for f in FRASI)

GG = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"]
WEEK = ''.join(f'<li data-d="{d}"><b>{GG[d]}</b>{ORARI[d][0][0]}<br>{ORARI[d][0][1]}</li>' for d in range(7))
SVC = ''.join(f'<li>{e(s)}</li>' for s in SERVIZI)
TAPE1 = ''.join(f'<span>{w}<i>✶</i></span>' for w in ["Halal food 100%", "Aperto tutti i giorni", "10–23:30", "Corso Cavour 155", "Riso biryani", "Seekh kebab", "Pizza", "Asporto"] * 2)
TAPE2 = ''.join(f'<span>{w}<i>●</i></span>' for w in ["Panino kebab", "Piadina kebab", "Falafel", "Chicken burger", "Hot dog", "Alette di pollo", "Patatine"] * 2)
NOTE_ARROW = '<svg viewBox="0 0 64 42"><path d="M60 6 C 42 4 24 14 12 34"/><path d="M24 32 L12 34 L10 22"/></svg>'
HALAL = '''<svg class="halal" viewBox="0 0 120 120" aria-hidden="true"><defs><path id="hl" d="M60 60 m-44 0 a44 44 0 1 1 88 0 a44 44 0 1 1 -88 0"/></defs>
<circle cx="60" cy="60" r="58" fill="#1e9e5a"/><circle cx="60" cy="60" r="34" fill="none" stroke="#fff" stroke-width="1.5" stroke-dasharray="3 4"/>
<g class="hring"><text><textPath href="#hl" textLength="270" lengthAdjust="spacing">HALAL FOOD · 100% QUALITY ·</textPath></text></g>
<text x="60" y="58" text-anchor="middle" style="font:400 22px Anton,Impact,sans-serif;letter-spacing:.02em">100%</text><text x="60" y="76" text-anchor="middle" style="font:600 10px 'Instrument Sans',sans-serif;letter-spacing:.2em">HALAL</text></svg>'''

NAV = [("budget", "Quanto hai?"), ("menu", "Menu"), ("recensioni", "Recensioni"), ("orari", "Orari e dove")]
NAVH = ''.join(f'<a href="#{k}">{t}</a>' for k, t in NAV)
MNAV = ''.join(f'<a href="#{k}"><i>{i+1:02d}</i>{t}</a>' for i, (k, t) in enumerate(NAV))

TITLE = "Ali Pizzeria Kebab · Kebab halal e pizza in Corso Cavour, Cesena"
DESC = f"Kebab halal, riso biryani, seekh kebab, pizze e burger in Corso Cavour 155 a Cesena. Aperto tutti i giorni dalle 10 alle 23:30. {GOOGLE_VOTO} su Google."

INTRO_JS = "<script>try{if(!sessionStorage.getItem('ali-intro')&&!matchMedia('(prefers-reduced-motion: reduce)').matches&&localStorage.getItem('ali-calm')!=='1'){document.documentElement.classList.add('is-intro');sessionStorage.setItem('ali-intro','1');setTimeout(function(){document.documentElement.classList.remove('is-intro')},1900)}}catch(e){}</script>"

def brand(uid="hb"):
    return f'<a class="brand" href="./#top" aria-label="{NOME}, torna su">{roundel("mk", uid)}<span><b>Ali <em>Pizzeria Kebab</em></b><small>Halal 100% · Corso Cavour · Cesena</small></span></a>'

index = head(TITLE, DESC, BASE + "/") + f'''<script type="application/ld+json">{SCHEMA}</script>{INTRO_JS}<style>{CSS}</style></head>
<body>
<a class="skip" href="#main">Vai al contenuto</a>
<div class="intro" aria-hidden="true">{roundel("mk", "ib")}</div>
<div class="prog" aria-hidden="true"></div><div class="grain" aria-hidden="true"></div>
<div class="info"><div class="wrap"><span class="st" data-stato><i class="dot"></i><span class="t">Aperto tutti i giorni {ORA}</span></span><span class="mid">{e(INDIRIZZO)}, Cesena · halal 100%</span><a href="{TEL_CALL}">{TEL[0]}</a></div></div>
<header class="hdr"><div class="wrap">{brand()}
 <nav class="nav" aria-label="Sezioni">{NAVH}</nav>
 {btn("Chiama", TEL_CALL)}
 <button type="button" class="mnu" aria-expanded="false" aria-controls="mpanel"><span></span><span></span><b class="sr">Apri il menu</b></button>
</div></header>
<dialog class="mpanel" id="mpanel" aria-label="Menu">
 <button type="button" class="mclose" aria-label="Chiudi il menu"><span></span><span></span></button>
 <nav class="mlinks" aria-label="Menu del telefono">{MNAV}</nav>
 <div class="mfoot"><a class="mtel" href="{TEL_CALL}">{TEL[0]}</a><p class="st" data-stato><i class="dot"></i><span class="t">Aperto tutti i giorni {ORA}</span></p><p>{e(INDIRIZZO)}, Cesena</p></div>
</dialog>
<main id="main">
<section class="hero" id="top" aria-labelledby="h1">
 <div class="wrap hero-in">
  <div>
   <p class="hstat" data-stato><i class="dot"></i><span class="t">Aperto tutti i giorni {ORA}</span></p>
   <h1 id="h1"><span class="l1">Hai fame? Da Ali c'è</span> <span class="rot" aria-live="off"><i>{ROT[0]}</i></span></h1>
   <p class="sub">Kebab halal, riso biryani, pizze e burger in Corso Cavour 155. <b>Aperto tutti i giorni, dalle 10 di mattina alle 23:30.</b></p>
   <div class="cta">{btn("Chiama · " + TEL[0], TEL_CALL, "yel")}{btn("Guarda il menu", "#menu", "white")}</div>
   <p class="proof"><span><span class="stars" aria-hidden="true">★★★★★</span> <b>{GOOGLE_VOTO}</b> su Google · {GOOGLE_N} recensioni</span><span>Asporto e consegna</span></p>
  </div>
  <div class="stage" role="button" tabindex="0" aria-label="Cambia piatto">
   {HERO_SVG}
   <p class="ptag" aria-live="polite"><small>Sul vassoio</small><b>{TAGS[0][0]}</b><span>{TAGS[0][1]}</span></p>
   {HALAL}
   <p class="hn hn-1" aria-hidden="true">tocca il vassoio!{NOTE_ARROW}</p>
  </div>
 </div>
</section>
<div class="tapes" aria-hidden="true"><div class="tape t2"><div class="row">{TAPE2}</div></div><div class="tape t1"><div class="row">{TAPE1}</div></div></div>

<section class="sec budget" id="budget" aria-labelledby="bud-t">
 <div class="wrap">
  <div class="sec-h"><div><p class="kick">Quanto hai in tasca?</p><h2 id="bud-t" data-r>Dimmi quanto hai,<br>ti dico <em>cosa mangi</em></h2></div>
   <p class="lead" data-r style="--d:.1s">Sposta il cursore: il conto lo fa il sito con i prezzi del menu di Ali, dal panino falafel da 5 euro al menù completo con patatine e lattina.</p></div>
  <div class="bgrid">
   <div class="bctl" data-r>
    <label for="brange">In tasca ho</label>
    <output class="bout" id="bout" for="brange">10<small>€</small></output>
    <input class="brange" type="range" id="brange" min="5" max="20" step="1" value="10">
    <div class="bscale"><span>5 €</span><span>20 €</span></div>
    <div class="bquick" role="group" aria-label="Importi veloci">{QUICK}</div>
    <p class="bnote">Prezzi del menu “Ordina online” sulla scheda Google di Ali. Al banco possono cambiare: chiedi conferma quando ordini.</p>
   </div>
   <div>
    <div class="bres" id="bres" aria-live="polite">{BRES0}</div>
    <div class="bcta">{btn("Chiama e ordina", TEL_CALL)}<p>Ordini al telefono e passi a ritirare, oppure ti siedi e lo mangi lì.</p></div>
   </div>
  </div>
 </div>
</section>

<section class="sec menu" id="menu" aria-labelledby="menu-t">
 <div class="wrap">
  <div class="sec-h"><div><p class="kick">Il menu</p><h2 id="menu-t" data-r>Dal kebab<br>alla pizza</h2></div>
   <p class="lead" data-r style="--d:.1s">{NVOCI} voci: kebab halal, menù completi, pizze rosse, burger, fritti e bevande. Si mangia lì, si porta via o si fa portare.</p></div>
  <nav class="mpills" aria-label="Categorie del menu">{MPILLS}</nav>
  <div class="mlayout">
   <nav class="midx" aria-label="Categorie del menu">{MIDX}</nav>
   <div>{MENU_HTML}<p class="mnote">Prezzi in euro presi dal menu “Ordina online” della scheda Google. Per allergeni, disponibilità e prezzi al banco chiedi ad Ali.</p></div>
  </div>
 </div>
</section>

<section class="sec rec" id="recensioni" aria-labelledby="rec-t">
 <div class="wrap">
  <div class="sec-h"><div><p class="kick">Recensioni Google</p><h2 id="rec-t" data-r>“Ali è super<br><em>simpatico”</em></h2></div><p class="lead" data-r style="--d:.1s">Lo scrivono i clienti su Google, insieme a un'altra frase che torna spesso: il miglior kebab che abbiano mai mangiato. Marco ci viene da cinque anni.</p></div>
  <div class="rgrid">
   <div class="score"><b data-v="{GOOGLE_VOTO.replace(',', '.')}">{GOOGLE_VOTO}</b><div class="stars" aria-label="{GOOGLE_VOTO} stelle su 5"><i></i><i></i><i></i><i></i><i></i></div><p>su {GOOGLE_N} recensioni Google</p><p style="margin-top:14px"><a href="{RECENSIONI_URL}" {EXT}>Leggile tutte →</a></p></div>
   <div><div class="rcards">{RECS}</div><div class="frasi" data-r>{FR}</div></div>
  </div>
 </div>
</section>

<section class="sec visit" id="orari" aria-labelledby="orari-t">
 <div class="wrap vgrid">
  <div>
   <p class="kick">Orari e dove</p>
   <h2 id="orari-t" data-r>Sempre aperto,<br>anche la domenica</h2>
   <div class="big7"><b>7 su 7</b><span>dalle 10 di mattina alle 23:30, tutti i giorni della settimana</span></div>
   <ul class="week" aria-label="Orari della settimana">{WEEK}</ul>
   <p class="now" data-stato><i class="dot"></i><span class="t">Aperto tutti i giorni {ORA}</span></p>
   <ul class="svc">{SVC}</ul>
  </div>
  <div>
   <p class="addr">{e(INDIRIZZO)}<br>{e(CAP_CITTA)}</p>
   <p style="color:var(--ink2)">L'insegna è rossa e bianca, con scritto “Halal food 100% quality”.</p>
   <div class="mapbox">{MAPPA}</div>
   <div class="vbtns">{btn("Come arrivare", MAPS, "ink", " " + EXT)}{btn("Chiama " + TEL[0], TEL_CALL)}</div>
  </div>
 </div>
</section>

<section class="final" aria-labelledby="fin-t">
 <div class="wrap"><h2 id="fin-t" data-r>Hai fame?<br><span class="o">Chiama Ali.</span></h2>
  <p data-r style="--d:.1s">Ordini al telefono e passi a ritirare, oppure ti siedi e lo mangi caldo. Tutti i giorni dalle 10 alle 23:30.</p>
  <div class="cta" data-r style="--d:.16s">{btn("Chiama · " + TEL[0], TEL_CALL)}{btn("Come arrivare", MAPS, "white", " " + EXT)}</div></div>
</section>
</main>
<footer class="foot"><div class="wrap">
 <div class="fgrid">
  <div>{brand("fb")}<p style="margin-top:14px;max-width:30ch">Kebab halal, pizza e burger in Corso Cavour a Cesena.</p></div>
  <div><p class="fh">Contatti</p><p><a href="{TEL_CALL}">{TEL[0]}</a></p><p><a href="{MAPS}" {EXT}>Google Maps</a></p></div>
  <div><p class="fh">Orari</p><p>Tutti i giorni</p><p>{ORA}</p></div>
  <div><p class="fh">Dove</p><p>{e(INDIRIZZO)}<br>{e(CAP_CITTA)}</p><p><a href="{MAPS}" {EXT}>Come arrivare →</a></p></div>
 </div>
 <div class="fbot"><span>© {datetime.date.today().year} {NOME} · <a href="privacy.html">Privacy</a></span><button type="button" id="calm" aria-pressed="false">Ferma le animazioni</button></div>
</div></footer>
<div class="mbar">{btn("Chiama", TEL_CALL)}{btn("Come arrivare", MAPS, "ink", " " + EXT)}</div>
<script>{JS}</script>
</body></html>'''

subs = {"%%ORARI%%": ORARI_JS, "%%GIORNI%%": json.dumps(GIORNI, ensure_ascii=False), "%%ROT%%": json.dumps(ROT, ensure_ascii=False),
        "%%TAGS%%": json.dumps(TAGS, ensure_ascii=False), "%%MAINS%%": json.dumps(MAINS, ensure_ascii=False), "%%SIDES%%": json.dumps(SIDES, ensure_ascii=False),
        "%%DRINKS%%": json.dumps(DRINKS, ensure_ascii=False), "%%LABELS%%": json.dumps(LABELS, ensure_ascii=False)}
for k, v in subs.items(): index = index.replace(k, v)
assert "%%" not in index

simple_css = CSS + '.pv{padding-block:var(--s12)}.pv .wrap{max-width:760px}.pv h1{font-size:clamp(3rem,2rem + 4vw,5rem);margin-bottom:var(--s4)}.pv h2{font-size:1.8rem;margin:var(--s4) 0 var(--s2)}.pv p{color:var(--ink2)}'
def simple(title, desc, url, body):
    return head(title, desc, url) + f'<style>{simple_css}</style></head><body><header class="hdr is-sc"><div class="wrap">{brand()}{btn("Torna al sito", "./", "white")}</div></header><main class="pv"><div class="wrap">{body}</div></main><footer class="foot"><div class="wrap"><div class="fbot" style="margin:0;border:0"><span>© {datetime.date.today().year} {NOME} · {e(INDIRIZZO)}, Cesena · {TEL[0]}</span></div></div></footer></body></html>'

privacy = simple("Privacy · Ali Pizzeria Kebab, Corso Cavour Cesena", "Informativa privacy del sito di Ali Pizzeria Kebab, Corso Cavour 155 a Cesena: nessun cookie di profilazione, nessun modulo, nessun dato raccolto.", BASE + "/privacy.html",
 f'''<h1>Privacy</h1><p>Questo sito presenta {NOME}, {e(INDIRIZZO)}, {e(CAP_CITTA)}.</p>
<h2>Dati raccolti</h2><p>Il sito non ha moduli e non raccoglie dati personali. Il calcolo della sezione "Quanto hai in tasca?" avviene nel tuo browser: nessun dato viene inviato. Quando chiami, la telefonata parte dal tuo telefono.</p>
<h2>Cookie</h2><p>Il sito non usa cookie di profilazione né statistiche. I caratteri sono caricati da Google Fonts. Il link "Come arrivare" apre Google Maps, e da quel momento valgono le regole di Google.</p>
<h2>Contatti</h2><p>Per qualsiasi domanda: {TEL[0]}.</p>''')
p404 = simple("Pagina non trovata · Ali Pizzeria Kebab", "La pagina che cercavi sul sito di Ali Pizzeria Kebab non c'è. Torna alla home o chiama per ordinare in Corso Cavour a Cesena.", BASE + "/404.html",
 f'<h1>Questa pagina se l\'è mangiata qualcuno.</h1><p>La pagina che cercavi non c\'è più. Torna alla home o chiama Ali per ordinare.</p><p style="margin-top:24px;display:flex;gap:16px;flex-wrap:wrap">{btn("Torna al sito", "./", "ink")}{btn("Chiama " + TEL[0], TEL_CALL)}</p>')

for n, c in (("index.html", index), ("privacy.html", privacy), ("404.html", p404)):
    open(os.path.join(DIR, n), "w", encoding="utf-8").write(c)
open(os.path.join(DIR, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
open(os.path.join(DIR, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{BASE}/</loc></url><url><loc>{BASE}/privacy.html</loc></url></urlset>\n')
open(os.path.join(DIR, "favicon.svg"), "w").write('<svg xmlns="http://www.w3.org/2000/svg"' + roundel("f", "fv")[4:])
print("ok", len(index), [[x["n"] for x in c["it"]] for c in combos(500)], [[x["n"] for x in c["it"]] for c in combos(2000)])
