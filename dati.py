# Dati di Ali pizzeria kebab Cesena, presi il 18/11/2026 dalla scheda Google Maps
# (orari, menu online con prezzi, voto, recensioni, servizi) e dalle foto dell'insegna
# ("Ali Pizzeria Kebab · Halal food 100% quality", insegna rossa e bianca con i pannelli del menu).
# Nessun sito, nessun social trovato. Titolare: Ali (citato nelle recensioni).
NOME = "Ali pizzeria kebab Cesena"
INSEGNA = "Ali Pizzeria Kebab"
INDIRIZZO = "Corso Cavour 155"
CAP_CITTA = "47521 Cesena (FC)"
LAT, LNG = 44.1436722, 12.250861
TEL = ("327 714 5213", "+393277145213")  # cellulare: WhatsApp da confermare
MAPS = "https://www.google.com/maps/search/?api=1&query=Ali+pizzeria+kebab+Cesena%2C+Corso+Cavour+155%2C+47521+Cesena+FC"
RECENSIONI_URL = "https://www.google.com/maps/place/Ali+pizzeria+kebab+Cesena/@44.1436722,12.250861,17z/data=!4m8!3m7!1s0x132ca504febf8b4b:0x7bf1cf079693afb3!8m2!3d44.1436722!4d12.250861!9m1!1b1"
GOOGLE_VOTO, GOOGLE_N = "4,7", 55
# lun=0 ... dom=6. Google Maps 18/11/2026: tutti i giorni 10-23:30
ORARI = {d: [("10:00", "23:30")] for d in range(7)}
GIORNI = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
SERVIZI = ["Aperto tutti i giorni", "Halal 100%", "Consumazione sul posto", "Asporto", "Consegna a domicilio", "Ordine online"]

# Menu: prezzi del menu "Ordina online" della scheda Google. Al banco possono differire: da confermare con Ali.
MENU = [
 ("kebab", "Kebab", "Halal, come dice l'insegna.", [
   ("Panino Kebab", "Fette sottili di carne arrostita sullo spiedo verticale, nel pane pita con verdure e salse", "7,00"),
   ("Piadina Kebab", "", "8,09"),
   ("Piatto Kebab", "", "10,00"),
   ("Piatto Riso Kebab", "", "10,00"),
   ("Seekh Kebab", "", "9,09"),
   ("Panino Falafel", "", "5,00")]),
 ("menu", "Menù completi", "Con patatine e una lattina a scelta.", [
   ("Menù Panino Kebab", "Con patatine fritte e bibita in lattina a scelta", "11,00"),
   ("Menù Piadina Kebab", "Con patatine fritte e bibita in lattina a scelta", "12,00"),
   ("Menù Chicken Burger", "Con bibita in lattina a scelta", "12,00")]),
 ("pizze", "Pizze rosse", "", [
   ("Salsiccia dolce", "Pomodoro, mozzarella e salsiccia dolce", "7,00"),
   ("Margherita", "Pomodoro e mozzarella", "7,50"),
   ("Wurstel", "Pomodoro, mozzarella e wurstel", "8,00"),
   ("Salamino piccante", "Pomodoro, mozzarella e salamino piccante", "8,00"),
   ("Tonno e cipolla", "Pomodoro, mozzarella, tonno e cipolla", "8,00"),
   ("Pizza con patatine", "Pomodoro, mozzarella e patatine fritte", "9,00"),
   ("Pizza Kebab", "Pomodoro, mozzarella e carne kebab", "14,00")]),
 ("panini", "Burger e hot dog", "", [
   ("Hamburger", "", "5,50"), ("Chicken Burger", "", "5,50"), ("Chicken Cheese", "", "6,00"),
   ("Cheeseburger", "", "6,90"), ("Hot Dog", "", "5,00")]),
 ("fritti", "Fritti", "", [
   ("Patatine fritte", "", "4,00"), ("Onion rings", "", "4,00"), ("Crocchette di patate", "", "5,00"),
   ("Mozzarella sticks", "", "5,00"), ("Alette di pollo", "", "7,00")]),
 ("bevande", "Bevande", "", [
   ("Acqua naturale 50 cl", "", "2,00"), ("Acqua frizzante 50 cl", "", "2,00"),
   ("Lattina 33 cl", "Coca-Cola, Coca-Cola Zero, Fanta, Sprite", "3,00"), ("Tè alla pesca 50 cl", "", "3,00"),
   ("Bottiglia 45-50 cl", "Coca-Cola, Coca-Cola Zero, Fanta, Sprite", "4,00"), ("Succo di mango", "", "4,00"),
   ("Bottiglia 1,5 l", "Coca-Cola, Fanta", "4,50")]),
]
# piatto in evidenza su Google senza prezzo online
EVIDENZA = ["Riso Biryani", "Hot Dog"]

# Recensioni Google vere (estratti fedeli), 18/11/2026. Nome abbreviato.
RECENSIONI = [
 ("Marco C.", "4 mesi fa", "Migliore kebab di Cesena, 5 anni che vengo qui e mi ritengo pienamente soddisfatto."),
 ("Sara A.", "un anno fa", "Il miglior kebab che abbia mai mangiato in vita mia, leggero ma gustoso. Il personale è carino e gentile."),
 ("Stefania B.", "1 mese fa", "Il personale molto simpatico e disponibile, servizio ottimo, miglior kebab che io abbia mai mangiato."),
]
FRASI = ["Ingredienti freschi e saporiti", "Ali è super simpatico e molto gentile.", "Molto buono, servizio bravissimo."]
