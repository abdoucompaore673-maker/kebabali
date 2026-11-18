# Ali Pizzeria Kebab — sito demo Premium (18/11/2026)
Modalità: rapida (demo per prospect), livello Premium da subito.
Locale: Corso Cavour 155, 47521 Cesena (FC). Tel 327 714 5213 (confermato da Abdou il 18/11; WhatsApp NON confermato, quindi niente blocco "prenota su WhatsApp"). Tutti i giorni 10–23:30. 4,7 su 55 recensioni Google. Titolare: Ali.
Fonti: scheda Google Maps (orari, menu "Ordina online" con prezzi, servizi, recensioni, foto dell'insegna rossa e bianca "Ali Pizzeria Kebab · Halal food 100% quality"). Nessun sito né social trovati.
Pubblico probabile: studenti e ragazzi, lavoratori in pausa pranzo e chi passa in centro la sera, budget basso.

## Come si lavora
- `python3 build.py [indirizzo_base]` genera index.html, privacy.html, 404.html, robots, sitemap, favicon.svg. Indirizzo base predefinito: https://ali-pizzeria-kebab.github.io (organizzazione GitHub ancora da creare).
- Dati in `dati.py`, illustrazioni SVG in `arte.py` (piatti, marchio tondo, icone, mappa), pagina e codice in `build.py`.
- og.jpg, favicon.png (versione semplice "ALI") e apple-touch-icon.png si rifanno con Playwright: script aliog.cjs e pagine ali_og.html, ali_fav.html, ali_favs.html nello scratch.
- Test dal cloud con i font veri: Anton, Instrument Sans e Caveat presi da github.com/google/fonts (clone parziale) e installati in ~/.fonts.

## Inventario
Il nome Ali, e Ali stesso citato nelle recensioni come "super simpatico" · insegna rossa e bianca · "Halal food 100% quality" · aperto 7 giorni su 7 dalle 10 alle 23:30 · Corso Cavour 155 · riso biryani e seekh kebab tra i piatti in evidenza · pizze rosse da 7 € · panino falafel e hot dog da 5 € · menù completi con patatine e lattina · "migliore kebab di Cesena, 5 anni che vengo qui".

## Idea
Su questa pagina i prezzi bassi e l'orario lungo diventano la domanda "hai fame? quanto hai in tasca?": il sito risponde con piatti veri e scontrini veri.

## Sezioni (affermazione → prova)
1. Hero rosso: stato aperto/chiuso dal vivo, "Hai fame? Da Ali c'è…" con 4 parole, vassoio che fa passare 4 piatti disegnati (panino kebab, riso biryani, pizza, seekh kebab), cartellino col prezzo vero, bollino Halal 100% che gira → menu e insegna.
2. Quanto hai in tasca? (cosa viva): cursore da 5 a 20 € e tasti rapidi; fino a 3 scontrini con piatto + contorno + bibita entro la cifra, un piatto per categoria, resto calcolato. Senza script resta la versione a 10 €. Avviso: prezzi del menu online, al banco possono cambiare.
3. Menu (34 voci) con indice fisso a sinistra e pillole su telefono; Riso Biryani "in evidenza" con prezzo al banco.
4. Recensioni su fondo rosso: titolo "Ali è super simpatico", voto 4,7, 3 recensioni vere, frasi in evidenza di Google.
5. Orari: "7 su 7", settimana con oggi evidenziato, servizi, mappa disegnata, Come arrivare.
6. Chiusura "Hai fame? Chiama Ali."

## Stile
- Palette: rosso insegna #d7262e / #b51c23, inchiostro #1a1414, carta #fff8ee, giallo patatine #ffc93c (evidenze), verde halal #1e9e5a (solo bollino e servizio halal).
- Font: Anton (titoli, come un'insegna), Instrument Sans (testo), Caveat (note a mano). Scontrini in monospazio di sistema.
- Pulsanti rettangolari con riempimento dal basso e freccia.

## Movimento
Sipario col marchio che gira (una volta per sessione), vassoio che fa scorrere i piatti con vapore, parola che cambia con WAAPI, cartellino che si gira, bollino halal che ruota, nastri incrociati, titoli parola per parola, scontrini che entrano sfalsati, numero del voto che sale, stelle a timbro, percorso tratteggiato sulla mappa, marchio della testata che gira con lo scorrimento. Tutto spento con movimento ridotto o col pulsante "Ferma le animazioni".

## Modern Web Guidance
Titoli fluidi rem+vw, text-wrap balance/pretty, font-size-adjust, barra di avanzamento con animation-timeline scroll() e script di riserva, menu del telefono come <dialog> con showModal e overscroll-behavior, accent-color/::selection/scrollbar-color, @view-transition tra le pagine, cursore con riempimento via variabile CSS.

## Lezioni
- Classi di stato con prefisso (is-sc, is-open, is-on, is-intro) per non scontrarsi con altre classi.
- Un ::after assoluto dentro un box che diventa position:static su telefono scappa dal ritaglio e allarga la pagina: il box deve restare position:relative.

## Verifica (18/11/2026)
1440 e iPhone 13: nessun errore, nessun ID doppio, niente scorrimento laterale (390 px); cursore provato a 5 € (panino falafel, hot dog) e 20 €; vassoio al tocco; menu del telefono aperto; controllo_finale pulito salvo noindex della demo.

## Da fare / da chiedere ad Ali
- Il numero ha WhatsApp? Se sì, aggiungere "Prenota/ordina su WhatsApp".
- Prezzi al banco uguali al menu online? Prezzo del riso biryani.
- Foto vere del locale e dei piatti; consegna a domicilio: con chi e dove.
- Pubblicazione: creare l'organizzazione GitHub "ali-pizzeria-kebab" solo con l'ok di Abdou.
