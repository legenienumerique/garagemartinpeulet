"""Générateur de la maquette Garage Martin-Peulet. Usage : python build.py <dossier-du-projet>
Contenus relevés sur garagemartin-peulet.com (novembre 2026) : textes, avis contrôlés Plus que pro, logo, photos.
Une seule vraie photo (la façade) : les autres visuels sont ceux du site actuel."""
import os
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
A = 'assets/'
PH = A + 'ph/'
V = 2  # cache : incrémenter à chaque changement de CSS ou JS
TEL, TELH = '04 74 47 91 04', 'tel:0474479104'
MOB, MOBH = '06 08 92 10 48', 'tel:0608921048'
ADR = ('Route de Bourg', '01400 Neuville-les-Dames')

NAV = [('mecanique.html', 'Mécanique'), ('carrosserie.html', 'Carrosserie'), ('avis.html', 'Avis clients')]


def pill(t, href, cls='', arrow='↗'):
    return f'<a class="pill {cls}" href="{href}"><span class="r"><span>{t}</span><span>{t}</span></span><b>{arrow}</b></a>'


def tile(src, cls='', style='', alt='', par=None, lazy=True):
    p = f' data-par="{par}" style="height:118%;width:100%"' if par else ''
    return f'<figure class="tile {cls}" style="{style}"><img src="{src}" alt="{alt}"{p}{" loading=lazy" if lazy else ""}></figure>'


def logo(cls=''):
    return f'<span class="lgo {cls}" aria-hidden="true"><i><img src="{A}logo.png" alt=""></i><span><span class="wm">Garage <b>Martin-Peulet</b></span><small>Mécanique · Carrosserie</small></span></span>'


def head(title, desc, cur):
    def a(h, t, cls=''):
        return f'<a href="{h}"{" class="+cls if cls else ""}{" aria-current=page" if h == cur else ""}>{t}</a>'
    items = a('index.html', 'Accueil') + ''.join(a(h, t) for h, t in NAV) + a('rendez-vous.html', 'Rendez-vous', 'hl')
    return f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#111417">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{A}logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat+Alternates:wght@600;700;800&family=Montserrat:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}style.css?v={V}">
</head><body>
<div id="bar"></div>
<header class="top">
<a class="logo" href="index.html" aria-label="Garage Martin-Peulet, accueil">{logo()}</a>
<nav class="nav" aria-label="Navigation principale"><button class="stop" type="button" aria-label="Fermer le menu"><span>MENU</span></button>{items}</nav>
<span class="side"><a class="tel" href="{TELH}" aria-label="Appeler le {TEL}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z" fill="currentColor"/></svg><span>{TEL}</span></a></span>
<button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</header>
<main>'''


def foot():
    return f'''</main>
<footer><div class="wrap"><div class="fg">
<div>{logo('big')}<p>Garage indépendant, multimarque et multiservice à Neuville-les-Dames, dans l’Ain. Entretien, réparation, carrosserie et peinture, pour voitures, utilitaires et deux-roues.</p></div>
<div><h4 class="micro">Prestations</h4><ul><li><a href="mecanique.html">Entretien et révision</a></li><li><a href="mecanique.html#reparation">Réparation et dépannage</a></li><li><a href="carrosserie.html">Carrosserie et peinture</a></li><li><a href="carrosserie.html#pare-brise">Pare-brise</a></li><li><a href="avis.html">Avis clients</a></li></ul></div>
<div><h4 class="micro">Contact</h4><ul><li><a href="{TELH}">{TEL}</a></li><li><a href="{MOBH}">{MOB}</a></li><li><a href="rendez-vous.html">Prendre rendez-vous</a></li></ul></div>
<div><h4 class="micro">Garage</h4><ul><li>{ADR[0]}</li><li>{ADR[1]}</li><li>Ouvert du lundi au vendredi</li></ul></div>
</div></div>
<div class="fw" aria-hidden="true">GARAGE</div>
<div class="fb micro"><span class="pad">© Garage Martin-Peulet</span><span class="pad">Maquette de site · Le Génie Numérique</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="{A}main.js?v={V}"></script></body></html>'''


def cta(t='Un bruit <em>bizarre ?</em>'):
    return f'''<section class="sec cta"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.6rem">Devis gratuit · véhicule de prêt · toutes marques</span><h2 class="sp">{t}</h2>
<div class="row rv">{pill('Prendre rendez-vous', 'rendez-vous.html', 'blue')}{pill(TEL, TELH, 'ghost')}</div></div></section>'''


def pagehead(crumb, h1, lead, img, img2=None, extra=''):
    t2 = tile(img2, 'small', lazy=False) if img2 else ''
    return f'''<section class="ph"><div class="wrap"><div class="crumb micro"><a href="index.html">Accueil</a> / {crumb}</div><h1 class="sp">{h1}</h1><p class="lead rv">{lead}</p>{extra}</div>{tile(img, lazy=False)}{t2}</section>'''


def faq(its):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in its) + '</div>'


# avis contrôlés Plus que pro, publiés sur le site du garage
AVIS = [('Dorian T.', 'Neuville-les-Dames', 'Vidange, Honda Jazz', 'Je n’ai pas eu de devis préalable mais le montant de la facture était correct pour la prestation. Jamais de mauvaise surprise.', '03/2025', '4,8'),
        ('Mélanie V.', 'Neuville-les-Dames', 'Vidange, bougies, injecteur, Renault Clio', 'Toujours satisfaite des prestations fournies et de l’accueil.', '03/2025', '5'),
        ('Marie-Claude E.', 'Neuville-les-Dames', 'Kit distribution, Renault Clio', 'L’équipe du garage est toujours très réactive à nos demandes, très arrangeante, disponible et compétente.', '03/2025', '4,8'),
        ('Marie C.', 'Châtillon-sur-Chalaronne', 'Kit distribution, Peugeot 208', 'Je suis très satisfaite des réparations et suivis effectués sur ma voiture. Je recommande ce garage.', '01/2025', '4,8'),
        ('Vincent B.', 'Chanoz-Châtenay', 'Vidange, freins, pneus hiver', 'Travail bien effectué, équipe à l’écoute de nos besoins avec de bons conseils. Nos 2 voitures sont très bien suivies et entretenues ici.', '12/2024', '4,6'),
        ('John C.', 'Condeissiat', 'Vidange, support moteur', 'Mécanicien passionné, très pro, à l’écoute du client. Je recommande les yeux fermés.', '12/2024', '5')]


def avis_cards(items):
    return '<div class="rcs">' + ''.join(f'<blockquote class="rc rv"><span class="micro mute">{v} · {d}</span><p>« {t} »</p><footer><b>{n}</b><span>{p}</span><i>{s}/5</i></footer></blockquote>' for n, v, p, t, d, s in items) + '</div>'


def service(file, title, desc, crumb, h1, lead, img, img2, intro_h, intro_p, checks, faqs, more=''):
    extra = f'<div class="row rv" style="display:flex;gap:10px;flex-wrap:wrap;margin-top:2.2rem">{pill("Prendre rendez-vous", "rendez-vous.html", "blue")}{pill(TEL, TELH, "ghost")}</div>'
    cl = ''.join(f'<li><span><b>{a}</b> {b}</span></li>' for a, b in checks)
    return head(title, desc, file) + pagehead(crumb, h1, lead, img, img2, extra) + f'''
<section class="sec"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Nos prestations</span><h2 class="sp">{intro_h}</h2><p class="lead rv" style="margin-top:1.4rem">{intro_p}</p></div><ul class="checks rv">{cl}</ul></div></section>{more}
<section class="sec" style="padding-top:0"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Questions fréquentes</span><h2 class="sp">On vous <em>répond</em></h2></div><div class="rv">{faq(faqs)}</div></div></section>''' + cta() + foot()


FAQ_PRET = ('Proposez-vous un véhicule de prêt ?', 'Oui, pendant l’immobilisation de votre voiture, pour vos trajets du quotidien.')
FAQ_MARQUES = ('Travaillez-vous sur toutes les marques ?', 'Oui. Garage indépendant, nous travaillons avec toutes les marques et tous les modèles, voitures et utilitaires.')
FAQ_DEVIS = ('Le devis est-il gratuit ?', f'Oui. Appelez le {TEL} ou prenez rendez-vous en ligne pour un chiffrage précis.')


def pages():
    P = {}
    hero_tiles = [('t1', 'facade'), ('t2', 'sous-caisse'), ('t3', 'peinture'), ('t4', 'moteur'), ('t5', 'pare-brise'), ('t6', 'polissage'), ('t7', 'phare')]
    ht = ''.join(f'<figure class="tile {c}"><div class="fl"><div class="in"><img src="{PH}{f}.webp" alt=""></div></div></figure>' for c, f in hero_tiles)
    stack = ''.join(tile(f'{PH}{f}.webp') for f in ['moteur', 'sous-caisse', 'phare', 'peinture', 'polissage', 'pare-brise', 'facade'])
    items = [('mecanique.html', '01', 'Entretien', 'Révision, vidange, filtres, freins, climatisation, batterie.', 'sous-caisse'),
             ('mecanique.html#reparation', '02', 'Réparation', 'Moteur, embrayage, distribution, échappement, électricité.', 'moteur'),
             ('carrosserie.html', '03', 'Carrosserie', 'Débosselage, passage au marbre, peinture, motos comprises.', 'peinture'),
             ('carrosserie.html#pare-brise', '04', 'Pare-brise', 'Réparation d’impact par résine ou remplacement du vitrage.', 'pare-brise'),
             ('mecanique.html#pneus', '05', 'Pneus', 'Été, hiver, quatre saisons, équilibrage systématique.', 'phare')]
    pl = ''.join(f'<a href="{h}"><span class="micro mute">{n}</span><span class="nm">{t}</span><span class="d">{d}<b>Toutes marques</b></span></a>' for h, n, t, d, _ in items)
    prev = ''.join(tile(f'{PH}{it[4]}.webp', 'on' if i == 0 else '') for i, it in enumerate(items))
    steps = [('Vous réservez', 'En ligne ou par téléphone, le créneau qui vous arrange.'),
             ('On diagnostique', 'Un chiffrage précis avant toute intervention.'),
             ('Véhicule de prêt', 'Pour continuer à rouler pendant les travaux.'),
             ('Vous repartez', 'Travail soigné, facture sans mauvaise surprise.')]
    st = ''.join(f'<div class="stp"><div class="n">{i + 1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    mq = ''.join(f'<span>{x}</span>' for x in ['Vidange', 'Freins', 'Distribution', 'Pneus', 'Carrosserie', 'Peinture', 'Pare-brise', 'Climatisation'] * 2)

    P['index.html'] = head('Garage Martin-Peulet — Mécanique et carrosserie à Neuville-les-Dames (Ain)', 'Garage Martin-Peulet à Neuville-les-Dames : entretien, réparation, carrosserie, peinture, pare-brise et pneus, toutes marques. Véhicule de prêt, devis gratuit. 4,8/5 sur 6 avis contrôlés.', 'index.html') + f'''
<section class="hero">
<div class="cap micro c1"><b>Toutes marques</b>garage indépendant</div>
<div class="cap micro c2"><b>Mécanique et carrosserie</b>sous le même toit</div>
<div class="cap micro c3"><b>4,8 / 5</b>6 avis contrôlés</div>
<div class="go">{pill('Prendre rendez-vous', 'rendez-vous.html')}</div>
{ht}
<p class="para">L’entretien et la réparation de votre véhicule, à côté de chez vous.</p>
<h1 class="word">MARTIN-PEULET</h1>
<div class="scrollhint micro"><i></i>Défiler</div>
</section>

<div class="mq" aria-hidden="true"><div>{mq}</div></div>

<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Neuville-les-Dames, dans l’Ain</span><h2 class="sp">Le meilleur <em>rapport qualité-prix</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Garage multimarque et multiservice : quelle que soit votre panne, nous sommes en mesure de la résoudre. Et nos carrossiers remettent à neuf la tôle de tout type de véhicule.</p>
<ul class="checks rv" style="margin-bottom:2rem"><li><span><b>La satisfaction client</b>, pour une relation de confiance.</span></li><li><span><b>La polyvalence</b> de nos équipes.</span></li><li><span><b>La qualité</b> dans chaque prestation.</span></li></ul>{pill('Nos prestations', 'mecanique.html', 'blue')}</div>{tile(PH + 'facade.webp', '', par=8, alt='La façade du garage Martin-Peulet')}</div></section>

<section class="story"><span class="micro mute m3">L’atelier</span>
<h2><span class="w">Faites</span> <span class="w">rouler</span> <span class="w">vos</span> <span class="w"><em>mécaniques</em></span></h2>
<div class="stack">{stack}</div>
<p class="micro mute m1">Mécaniciens, carrossiers et peintres, sous le même toit.</p><span class="micro mute m2">Toutes marques</span></section>

<section class="sec" id="services"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Nos prestations</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,4rem)">De quoi a besoin <em>votre voiture ?</em></h2>
<div class="plist">{pl}</div></div><div class="prev">{prev}</div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Plus que pro</span><h2 class="sp">Ils nous <em>font confiance</em></h2>
<div class="cnt rv"><div><b data-to="4.8">0</b><span>sur 5, note moyenne des avis contrôlés</span></div><div><b data-to="6">0</b><span>avis clients vérifiés, avec pièce justificative</span></div><div><b data-to="1">0</b><span>garage, entre Bourg-en-Bresse et Châtillon-sur-Chalaronne</span></div></div>
<div style="margin-top:clamp(2rem,4vw,3rem)">{avis_cards(AVIS[:3])}</div><div class="row rv" style="margin-top:2rem">{pill('Tous les avis', 'avis.html')}</div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Sans voiture ? Jamais.</span><h2 class="sp">Un véhicule <em>de prêt</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Nous savons à quel point une voiture est indispensable au quotidien. Pendant l’immobilisation de la vôtre, nous vous en prêtons une. Remorquage et gardiennage aux horaires d’ouverture.</p>{pill('Prendre rendez-vous', 'rendez-vous.html', 'blue')}</div>{tile(PH + 'phare.webp', '', par=8, alt='Avant d’une voiture après un choc')}</div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Comment ça marche</span><h2 class="sp">Simple <em>comme un plein</em></h2><div class="steps">{st}</div></div></section>
{cta()}''' + foot()

    rep = f'''
<section class="sec" id="reparation" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Réparation et dépannage</span><h2 class="sp">Tous les organes <em>du véhicule</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Freins, échappement, transmission, suspensions, refroidissement, électricité, direction, climatisation, moteur… Nos fournisseurs de confiance nous livrent vite les pièces manquantes. Besoin d’une dépanneuse ? Nous assurons le remorquage aux horaires d’ouverture, puis le gardiennage.</p></div>{tile(PH + 'moteur.webp', '', par=8, alt='Mécanicien penché sur un moteur')}</div></section>
<section class="sec" id="pneus" style="padding-top:0"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Pneus et contrôle technique</span><h2 class="sp">Prêt pour <em>la route</em></h2></div>
<ul class="checks rv"><li><span><b>Pneus été, hiver, quatre saisons</b>, jantes, équilibrage systématique.</span></li><li><span><b>Large gamme</b>, pour tous les budgets.</span></li><li><span><b>Prévisite du contrôle technique</b> : on corrige avant, pour éviter la contre-visite.</span></li></ul></div></section>'''
    P['mecanique.html'] = service('mecanique.html', 'Mécanique auto à Neuville-les-Dames — Garage Martin-Peulet', 'Entretien, révision, vidange, freins, distribution, pneus, prévisite du contrôle technique, dépannage et véhicule de prêt. Garage Martin-Peulet, Neuville-les-Dames (Ain).',
        'Mécanique', 'Faites rouler <em>vos mécaniques</em>', 'Un travail soigné, dans le respect de votre budget, autour de Bourg-en-Bresse.', PH + 'sous-caisse.webp', PH + 'moteur.webp',
        'L’entretien <em>régulier</em>', 'Pour limiter les pannes, une révision est recommandée tous les 15 000 km ou tous les deux ans. Un carnet d’entretien à jour est le meilleur moyen d’anticiper.',
        [('Vidange', 'et remplacement des filtres : huile, air, carburant, particules.'), ('Freins', ': plaquettes, disques, liquide.'), ('Courroie de distribution', 'et niveaux.'), ('Climatisation', ': recharge du gaz.'), ('Batterie, bougies, essuie-glaces.', '')],
        [FAQ_MARQUES, ('À quelle fréquence faire la révision ?', 'Tous les 15 000 km ou tous les deux ans, selon les recommandations.'), FAQ_PRET, FAQ_DEVIS], rep)

    pb = f'''
<section class="sec" id="marbre" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Après un accident</span><h2 class="sp">Le passage <em>au marbre</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Notre marbre, une plateforme en acier, stabilise tout type de véhicule. Nos outils de mesure révèlent les déformations ; tirants et leviers redressent le châssis jusqu’à son alignement d’origine.</p></div>{tile(PH + 'peinture.webp', '', par=8, alt='Peintre en cabine de peinture')}</div></section>
<section class="sec" id="pare-brise" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Pare-brise</span><h2 class="sp">Un impact ? <em>On s’en occupe</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Les petits impacts se réparent par injection d’une résine spéciale. Au-delà de la taille d’une pièce de monnaie, ou en cas de fissure, nous remplaçons le vitrage : pare-brise, vitre latérale ou de coffre.</p></div>{tile(PH + 'pare-brise.webp', '', par=8, alt='Remplacement d’un pare-brise')}</div></section>'''
    P['carrosserie.html'] = service('carrosserie.html', 'Carrosserie et peinture à Neuville-les-Dames — Garage Martin-Peulet', 'Débosselage, passage au marbre, peinture voitures et motos, remplacement de pare-brise, remise à neuf de l’habitacle. Garage Martin-Peulet, Neuville-les-Dames (Ain).',
        'Carrosserie', 'Nous réparons <em>tous vos accrocs</em>', 'De la micro-rayure au pare-choc arraché, toutes marques, tous types de véhicules.', PH + 'peinture.webp', PH + 'polissage.webp',
        'Carrosserie <em>et peinture</em>', 'Préparation, ponçage, apprêt, peinture au pistolet, puis polissage pour la brillance. Les motos aussi : du ponçage au lustrage des plus petits détails.',
        [('Redressage', ', soudure, remplacement des éléments abîmés.'), ('Débosselage sans peinture', 'pour les petits impacts.'), ('Peinture', 'voitures et deux-roues.'), ('Habitacle', ': sièges, volant, ciel de toit, tapis.')],
        [('Peignez-vous aussi les motos ?', 'Oui. Nos équipes sont formées à la mise en peinture des deux-roues.'), FAQ_MARQUES, FAQ_PRET, FAQ_DEVIS], pb)

    P['avis.html'] = head('Avis clients — Garage Martin-Peulet, Neuville-les-Dames', 'Avis clients contrôlés du garage Martin-Peulet : 4,8/5 sur 6 avis vérifiés par Plus que pro.', 'avis.html') + pagehead('Avis clients', 'Ils en <em>parlent</em>', '6 avis contrôlés par Plus que pro, avec pièce justificative. Note moyenne : 4,8 sur 5.', PH + 'facade.webp') + f'''
<section class="sec"><div class="wrap">{avis_cards(AVIS)}<p class="note" style="margin-top:2rem">Avis publiés sur le site actuel du garage (Plus que pro), reproduits tels quels.</p></div></section>''' + cta() + foot()

    cr = ''.join(f'<button type="button"{" class=on" if i == 0 else ""}>{h}</button>' for i, h in enumerate(['8 h 00', '9 h 00', '10 h 00', '11 h 00', '14 h 00', '15 h 00', '16 h 00', '17 h 00']))
    P['rendez-vous.html'] = head('Prendre rendez-vous — Garage Martin-Peulet', f'Prenez rendez-vous au garage Martin-Peulet, {ADR[0]}, {ADR[1]} : entretien, réparation, carrosserie, pneus. {TEL}.', 'rendez-vous.html') + pagehead('Rendez-vous', 'Votre créneau, <em>en ligne</em>', 'Choisissez la prestation, le jour et l’heure. Nous vous confirmons le rendez-vous.', PH + 'facade.webp') + f'''
<section class="sec" id="rdv"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Coordonnées</span><h2 class="sp">Ou <em>un appel</em></h2>
<div class="contactline rv" style="margin-top:2rem"><a href="{TELH}">{TEL}</a></div>
<p class="lead rv" style="margin-top:1.6rem"><a href="{MOBH}">{MOB}</a><br>{ADR[0]}<br>{ADR[1]}</p>
<div class="hor rv"><span><b>Du lundi au vendredi</b></span><span class="micro">Horaires précis à confirmer avec le garage</span></div></div>
<form class="f calc rv" id="resa"><div class="fld"><label for="pr">Prestation</label><select id="pr"><option>Révision et vidange</option><option>Freins</option><option>Pneus</option><option>Distribution</option><option>Diagnostic panne</option><option>Carrosserie et peinture</option><option>Pare-brise</option><option>Prévisite contrôle technique</option></select></div>
<div class="r2"><div class="fld"><label for="rd">Jour</label><input id="rd" type="date" required></div><div class="fld"><label for="im">Véhicule</label><input id="im" placeholder="Marque, modèle"></div></div>
<div class="fld"><label>Créneau</label><div class="cov cr">{cr}</div></div>
<div class="r2"><div class="fld"><label for="rn">Nom</label><input id="rn" required></div><div class="fld"><label for="rt">Téléphone</label><input id="rt" type="tel" required></div></div>
<label class="chk"><input type="checkbox" id="pret"> J’ai besoin d’un véhicule de prêt</label>
<button class="pill blue" type="submit" style="justify-self:start"><span class="r"><span>Réserver</span><span>Réserver</span></span><b>↗</b></button><div class="ok">Merci ! (Maquette : aucun rendez-vous n’est envoyé.)</div></form></div></section>''' + foot()
    return P


for k, v in pages().items():
    open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
print('ok')
