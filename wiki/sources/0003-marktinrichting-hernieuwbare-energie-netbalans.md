---
id: 3
titel: "Met juiste marktinrichting kan hernieuwbare energie bijdragen aan netbalans"
uitgever: "ESB"
type: "analyse"
auteur: ""
datum: ""
themas: ["Marktinrichting"]
mechanismen: ["balanceringsmarkt", "curtailment"]
stakeholders: ["TenneT", "Energie-Nederland"]
scope: "NL"
toegang: "open"
url: "https://esb.nu/met-juiste-marktinrichting-kan-hernieuwbare-energie-bijdragen-aan-netbalans"
status: "verwerkt"
ingest-datum: "2026-07-03"
---

## Kernstelling
Of zon- en windproducenten kunnen bijdragen aan het herstellen van netonbalans (in plaats van er vooral de oorzaak van te zijn) hangt niet af van technologie maar van marktinrichting. Nederland heeft in theorie de juiste marktstructuur (een continue intradaymarkt), maar te weinig liquiditeit om dat voordeel in de praktijk te verzilveren.

## Belangrijkste punten / cijfers
- Wind- en zonproductie is onvoorspelbaar en kan makkelijk omlaag (curtailen) maar moeilijk omhoog worden bijgesteld — asymmetrisch aanpassingsvermogen, anders dan bv. gascentrales.
- Balans wordt in Nederland bewaakt door TenneT, via day-aheadmarkt → intradaymarkt → balanceringsmarkt (met frequentiebegrenzings-, frequentieherstel- en vervangende reserves).
- Twee marktvormen voor intraday-handel: *discreet* (veilingen op vaste tijden, o.a. Italië/Spanje) en *continu* (doorlopend handelen tot vlak voor levering, o.a. Nederland/Duitsland).
- Bij continue intradaymarkten kunnen hernieuwbare producenten balanceringsverplichtingen nakomen door tot vlak voor levering bij te handelen — zónder eigen batterij. Bij discrete markten is een batterij als buffer vrijwel noodzakelijk.
- Verwachte groei batterijcapaciteit NL: van 2 GWh (2025) naar ~10 GWh (2027) (bron: Energy Storage NL) — het artikel betoogt dat minder hiervan nodig zou zijn bij een goed werkende intradaymarkt.
- Nederland heeft al de gunstige (continue) marktvorm, maar onvoldoende liquiditeit: lastig een tegenpartij vinden vlak voor levering, hoge bid-ask spreads. Beleidsaanbeveling: liquiditeit vergroten (meer marktpartijen toelaten, transparantie, prikkels voor marktmakers) in plaats van alleen op batterijopslag te koersen.

## Mechanismen
- [[balanceringsmarkt]] — nieuw concept, aangemaakt bij deze ingest: hoe day-ahead-, intraday- en balanceringsmarkten samen netonbalans opvangen en welke rol marktstructuur (discreet vs. continu) daarin speelt.
- [[curtailment]] — genoemd als het "makkelijke" (neerwaartse) deel van het aanpassingsvermogen van zon/wind; dit artikel voegt toe dát opwaarts bijstellen veel lastiger is, wat curtailment als blinde vlek in dat concept relevant maakt.

## Frame / standpunt
Marktontwerp-frame: de energietransitie hoeft niet vooral opgelost te worden met dure, milieubelastende batterijopslag (kapitaalintensief, zeldzame aardmetalen) — een goed werkende, liquide continue intradaymarkt kan hetzelfde bereiken tegen lagere maatschappelijke kosten. Impliciet dus een frame van "goede regels/marktwerking beperken de meerkosten van de transitie", eerder dan "transitie = onvermijdelijk duurder".

## Toetsing & blinde vlekken
Dit artikel introduceert een mechanisme — marktgebaseerde balancering via (continue) intradaymarkten, als alternatief voor batterij-investeringen — dat nog niet te toetsen is aan een bestaand model: `raw/modellen/` is nog leeg (geen model van Matthijs of anderen aanwezig). Dit is zelf een blinde vlek in de opzet van deze wiki: zonder referentiemodel kan de toetsingsfunctie van `modeltoetsing.md` nog niet werken. Inhoudelijk valt op dat het artikel de *kosten* van balancering wel noemt (aanbieders verdienen eraan, veroorzakers betalen) maar niet doorrekent wat dit richting de consument/energierekening betekent — dat blijft impliciet.

## Betrokken stakeholders
- [[tennet]] — verantwoordelijk voor het handhaven van de systeembalans in Nederland; selecteert balanceringsdiensten bij onbalans.
- [[energie-nederland]] — waarschuwde (geciteerd, 2021) dat opsplitsing van biedzones tot lagere liquiditeit leidt en zo integratie van hernieuwbare bronnen bemoeilijkt.
