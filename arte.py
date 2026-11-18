# Illustrazioni SVG del sito di Ali: piatti veri del menu su un vassoio che gira.

def _st(xs, y):
    return ''.join(f'<path class="stm" style="--i:{i}" d="M{x} {y} c-12 -18 12 -30 0 -48 s12 -30 0 -48"/>' for i, x in enumerate(xs))

DEFS = '''<defs>
<radialGradient id="pl" cx=".5" cy=".42" r=".6"><stop offset="0" stop-color="#ffffff"/><stop offset=".8" stop-color="#f1ece4"/><stop offset="1" stop-color="#d9d1c5"/></radialGradient>
<linearGradient id="pita" x1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1cf8c"/><stop offset="1" stop-color="#cf9a4e"/></linearGradient>
<linearGradient id="crust" x1="0" x2="1"><stop offset="0" stop-color="#d9913f"/><stop offset=".5" stop-color="#f2bb6a"/><stop offset="1" stop-color="#c47c2e"/></linearGradient>
<linearGradient id="seekh" x1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5552a"/><stop offset="1" stop-color="#6a2f12"/></linearGradient>
<pattern id="rice" width="16" height="10" patternUnits="userSpaceOnUse"><rect width="16" height="10" fill="#f6d36a"/><ellipse cx="4" cy="3" rx="3.2" ry="1.1" fill="#fff6dc"/><ellipse cx="12" cy="7" rx="3.2" ry="1.1" fill="#fff3d0" transform="rotate(20 12 7)"/><ellipse cx="9" cy="2" rx="2.6" ry="1" fill="#e9a93a" transform="rotate(-25 9 2)"/></pattern>
</defs>'''

PLATE = '<ellipse cx="260" cy="330" rx="220" ry="86" fill="#000" opacity=".22" transform="translate(0 18)"/><ellipse cx="260" cy="330" rx="220" ry="86" fill="url(#pl)"/><ellipse cx="260" cy="326" rx="168" ry="62" fill="none" stroke="#e2d9cc" stroke-width="3"/>'

PANINO = f'''<g class="dish d-panino">
 <path d="M120 330 Q150 214 260 206 Q370 214 400 330 Q260 372 120 330 Z" fill="url(#pita)"/>
 <path d="M150 318 Q170 250 260 244 Q350 250 370 318 Q260 340 150 318 Z" fill="#7a3b18"/>
 <path d="M168 300 q24 -18 46 -4 q22 -18 46 -2 q24 -16 46 0 q20 -14 40 4" fill="none" stroke="#b5672e" stroke-width="7" stroke-linecap="round"/>
 <path d="M160 312 q20 -12 40 0 t40 0 t40 0 t40 0 t40 0" fill="none" stroke="#7cb342" stroke-width="9" stroke-linecap="round"/>
 {''.join(f'<circle cx="{190+i*36}" cy="{282+(i%2)*10}" r="9" fill="#d9412b"/>' for i in range(5))}
 <path d="M178 270 q40 -18 80 -6 q40 -14 84 4" fill="none" stroke="#f7f2e6" stroke-width="6" stroke-linecap="round"/>
 <path d="M190 262 q30 -10 60 0" fill="none" stroke="#d9412b" stroke-width="4" stroke-linecap="round"/>
 <path d="M120 330 Q260 372 400 330 L404 344 Q260 388 116 344 Z" fill="#fff" opacity=".9"/>
 <path d="M150 340 Q260 368 370 340" stroke="#d7262e" stroke-width="4" fill="none" stroke-dasharray="14 10"/>
 {_st([220, 260, 300], 210)}
</g>'''

BIRYANI = f'''<g class="dish d-biryani">
 <path d="M140 326 Q160 220 262 214 Q368 220 384 326 Q262 360 140 326 Z" fill="url(#rice)"/>
 <path d="M150 318 Q172 236 262 230 Q352 236 372 318" fill="none" stroke="#fff6dc" stroke-width="3" opacity=".7"/>
 {''.join(f'<path d="M{180+ (i*41)%170} {250+ (i*23)%60} q8 -6 16 0" fill="none" stroke="#9c4e8e" stroke-width="4" stroke-linecap="round"/>' for i in range(7))}
 {''.join(f'<circle cx="{170+ (i*53)%190}" cy="{256+ (i*31)%60}" r="3" fill="#3f7d2a"/>' for i in range(12))}
 <g transform="translate(330 318)"><path d="M0 0 a26 26 0 0 1 52 0 Z" fill="#f2d43a"/><path d="M6 0 a20 20 0 0 1 40 0" fill="none" stroke="#fff7b0" stroke-width="3"/></g>
 <g transform="translate(150 318)">{''.join(f'<rect x="{i*12}" y="{-8-(i%2)*6}" width="10" height="22" rx="3" fill="#7cb342" transform="rotate({-20+i*8})"/>' for i in range(4))}</g>
 {_st([220, 262, 304], 214)}
</g>'''

PIZZA = f'''<g class="dish d-pizza">
 <ellipse cx="260" cy="318" rx="170" ry="66" fill="url(#crust)"/>
 <ellipse cx="260" cy="314" rx="148" ry="54" fill="#d9412b"/>
 {''.join(f'<ellipse cx="{170+ (i*47)%180}" cy="{292+ (i*19)%44}" rx="{18+(i%3)*4}" ry="{9+(i%2)*3}" fill="#fff4dc"/>' for i in range(11))}
 {''.join(f'<ellipse cx="{176+ (i*61)%170}" cy="{298+ (i*29)%36}" rx="10" ry="5" fill="#9b2f1c"/>' for i in range(7))}
 {''.join(f'<path d="M{190+ (i*53)%150} {300+ (i*13)%30} l6 -4" stroke="#3f7d2a" stroke-width="4" stroke-linecap="round"/>' for i in range(6))}
 <path d="M260 314 L420 318 A170 66 0 0 1 380 360 Z" fill="#000" opacity=".08"/>
 {_st([210, 260, 310], 262)}
</g>'''

SEEKH = f'''<g class="dish d-seekh">
 {''.join(f'<g transform="rotate({-8+i*6} 260 300)"><rect x="128" y="{280+i*20}" width="264" height="22" rx="11" fill="url(#seekh)"/>{"".join(f"<path d=\"M{150+j*34} {284+i*20} l8 14\" stroke=\"#3d1606\" stroke-width=\"3\" opacity=\".6\"/>" for j in range(7))}<rect x="140" y="{283+i*20}" width="80" height="5" rx="2" fill="#c7743c" opacity=".7"/></g>' for i in range(3))}
 {''.join(f'<ellipse cx="{170+i*56}" cy="346" rx="20" ry="9" fill="none" stroke="#c68ab7" stroke-width="5"/>' for i in range(4))}
 <g transform="translate(372 328)"><path d="M0 0 a22 22 0 0 1 44 0 Z" fill="#f2d43a"/></g>
 {_st([210, 260, 310], 258)}
</g>'''

HERO_SVG = f'<svg class="scene" viewBox="0 0 520 460" role="img" aria-label="I piatti di Ali sul vassoio">{DEFS}<g class="tray">{PLATE}</g>{PANINO}{BIRYANI}{PIZZA}{SEEKH}</svg>'

def roundel(cls="mk", uid="m"):
    return f'''<svg class="{cls}" viewBox="0 0 120 120" aria-hidden="true">
 <defs><path id="{uid}c" d="M60 60 m-40 0 a40 40 0 1 1 80 0 a40 40 0 1 1 -80 0"/></defs>
 <circle cx="60" cy="60" r="58" fill="#d7262e"/><circle cx="60" cy="60" r="52" fill="none" stroke="#fff" stroke-width="2"/>
 <g class="mk-ring"><text font-family="Anton,Impact,Arial Narrow,sans-serif" font-size="11" fill="#fff"><textPath href="#{uid}c" textLength="240" lengthAdjust="spacing">ALI · PIZZERIA KEBAB · HALAL ·</textPath></text></g>
 <circle cx="60" cy="60" r="29" fill="#b51c23"/><text x="60" y="71" text-anchor="middle" font-family="Anton,Impact,Arial Narrow,sans-serif" font-size="30" fill="#fff" letter-spacing="1">ALI</text>
</svg>'''

ICO = {
 'kebab': '<path d="M32 4 V60"/><path d="M20 12 H44 L40 50 H24 Z"/><path d="M21.5 24 H42.5 M22.5 37 H41.5"/><path d="M26 56 h12"/>',
 'menu': '<rect x="8" y="22" width="22" height="30" rx="3"/><path d="M36 22 h20 l-3 30 h-14 Z"/><path d="M44 14 l4 8"/>',
 'pizze': '<path d="M32 8 L56 52 Q32 60 8 52 Z"/><circle cx="30" cy="34" r="4"/><circle cx="38" cy="46" r="3"/><circle cx="24" cy="48" r="3"/>',
 'panini': '<path d="M8 30 Q8 14 32 13 Q56 14 56 30 Z"/><path d="M6 36 h52"/><path d="M8 42 Q8 50 16 50 H48 Q56 50 56 42"/>',
 'fritti': '<path d="M14 26 h36 l-5 28 h-26 Z"/><path d="M20 26 l-3 -16 M28 26 l-1 -18 M36 26 l1 -17 M44 26 l3 -15"/>',
 'bevande': '<path d="M18 10 H46 L42 54 H22 Z"/><path d="M20 24 H44"/><path d="M28 6 l4 18"/>',
}
def ico(k):
    return f'<svg class="ci" viewBox="0 0 64 64" aria-hidden="true">{ICO[k]}</svg>'

MAPPA = '''<svg class="map" viewBox="0 0 520 380" role="img" aria-label="Mappa: Corso Cavour 155, Cesena">
 <rect width="520" height="380" fill="#f3ebde"/>
 <path class="rd rd-s" d="M0 90 C 120 110 300 70 520 120"/>
 <path class="rd rd-s" d="M80 380 C 120 260 140 160 150 0 M380 380 C 360 280 380 180 420 0"/>
 <path class="rd" d="M40 0 C 160 120 300 220 520 330"/>
 <text x="300" y="214" transform="rotate(30 300 214)" class="mt">Corso Cavour</text>
 <path class="route" d="M470 312 C 400 282 330 246 262 206"/>
 <g class="pin" transform="translate(250 196)"><circle class="pulse" r="18" fill="#d7262e" opacity=".35"/><path d="M0 0 C -14 -16 -14 -36 0 -40 C 14 -36 14 -16 0 0 Z" fill="#d7262e"/><circle cx="0" cy="-26" r="6" fill="#fff"/></g>
 <g transform="translate(276 120)"><rect width="150" height="40" rx="8" fill="#1a1414"/><text x="12" y="17" class="mt mt-w">Ali pizzeria kebab</text><text x="12" y="32" class="mt mt-w2">Corso Cavour 155</text></g>
</svg>'''
