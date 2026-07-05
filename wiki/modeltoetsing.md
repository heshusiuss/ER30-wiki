# modeltoetsing.md — observaties toetsen + blinde vlekken vinden

Deze pagina dient twee functies, allebei analytisch:

1. **Toetsing van observaties** — kunnen mechanismen die in verwerkte bronnen voorkomen geplaatst worden in een bestaand model van de energierekening?
2. **Blinde vlekken** — wat zit in de bronnen maar niet in het model, en omgekeerd?

Startpunt is het model/schema van Matthijs; zet dat in `raw/modellen/`. Andere modellen kunnen ernaast gelegd worden (extra kolommen in de tabel hieronder).

> Monitoring-kanttekening: dit is een toevallige greep bronnen, geen systematische meting. Gebruik dit voor signalering — niet voor uitspraken over hoe vaak iets speelt.

## 1. Toetsing van observaties

Onderhoud per mechanisme uit de bronnen: welke bronnen het noemen, waar het in het getoetste model zit, en of de plaatsing klopt.

| Mechanisme (concept) | Bronnen | Onderdeel in model | Past |
|---|---|---|---|
| [[balanceringsmarkt]] | [[0003-marktinrichting-hernieuwbare-energie-netbalans]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[netcongestie]] | [[0020-nederland-loopt-achter-vormgeven-nieuwe-energiemarkt]], [[0058-richt-beleid-efficient-gebruik-schaarse-energie]], [[0034-acm-akkoord-nettarieven-2027-2031]], [[0035-nettarieven-tijdsafhankelijk-piekmomenten]], [[0098-kosten-stroomnet-verdrievoudigen-2040]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[netkosten-transporttarieven]] | [[0034-acm-akkoord-nettarieven-2027-2031]], [[0035-nettarieven-tijdsafhankelijk-piekmomenten]], [[0098-kosten-stroomnet-verdrievoudigen-2040]], [[0029-acm-energierekening-stijgt-beter-contract]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[salderen]] | | _?_ | _?_ |
| [[terugleververgoeding]] | | _?_ | _?_ |
| [[dynamische-prijzen]] | [[0020-nederland-loopt-achter-vormgeven-nieuwe-energiemarkt]], [[0035-nettarieven-tijdsafhankelijk-piekmomenten]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[energiebelasting]] | [[0020-nederland-loopt-achter-vormgeven-nieuwe-energiemarkt]], [[0046-analyse-beprijzing-broeikasgasemissies-nederland]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[ets2-beprijzing]] | [[0046-analyse-beprijzing-broeikasgasemissies-nederland]], [[0029-acm-energierekening-stijgt-beter-contract]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[warmtenet-tarieven]] | | _?_ | _?_ |
| [[curtailment]] | [[0003-marktinrichting-hernieuwbare-energie-netbalans]], [[0020-nederland-loopt-achter-vormgeven-nieuwe-energiemarkt]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[energiearmoede]] | [[0098-kosten-stroomnet-verdrievoudigen-2040]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[leveringszekerheid]] | [[0020-nederland-loopt-achter-vormgeven-nieuwe-energiemarkt]], [[0074-vk-carbon-budget-delivery-plan]], [[0087-vk-warmtepompen-koeling-weer]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[capaciteitsmarkt]] | [[0020-nederland-loopt-achter-vormgeven-nieuwe-energiemarkt]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[co2-beprijzingstekort]] | [[0046-analyse-beprijzing-broeikasgasemissies-nederland]], [[0058-richt-beleid-efficient-gebruik-schaarse-energie]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[schaarste-allocatie-duurzame-energie]] | [[0058-richt-beleid-efficient-gebruik-schaarse-energie]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[energiecontracten]] | [[0029-acm-energierekening-stijgt-beter-contract]], [[0033-acm-energierekening-stijgt-bespaar-overstappen-gaslicht]], [[0039-eneco-happypower-loyaliteitsprogramma]], [[0040-overstapkosten-opzegtermijn-boetevrij]], [[0089-vk-groene-energiecontracten-afname]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[warmtepompen-verwarmingstransitie]] | [[0054-duitsland-verwarmingswet-terugdraaien]], [[0074-vk-carbon-budget-delivery-plan]], [[0087-vk-warmtepompen-koeling-weer]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |

_(Voeg rijen toe naarmate nieuwe mechanismen uit bronnen komen.)_

## 2. Blinde vlekken

### A. In bronnen, niet in het model
_(mechanismen die bronnen noemen maar die in het getoetste model geen plek lijken te hebben — vul aan tijdens ingest/lint)_
- Industriepolitieke allocatie van schaarse duurzame energie ([[schaarste-allocatie-duurzame-energie]]) — een keuze over *wie* toegang krijgt tot schaarse energie, los van marktprijs; onduidelijk of dit type mechanisme in een marktinrichtings-/netbalansmodel als dat van Matthijs een plek heeft.
- Contractkeuze/leveranciersgedrag ([[energiecontracten]]) — prijsverschillen tussen contracten, opzegvoorwaarden en loyaliteitsprogramma's zijn een consumentengedrag-/marktwerkingsmechanisme dat losstaat van productie-, net- of beprijzingsmodellen; waarschijnlijk geen onderdeel van een marktinrichtings-/netbalansmodel als dat van Matthijs, maar wel relevant voor de energierekening zelf.
- Koelvraag/airconditioning ([[leveringszekerheid]], via [[0087-vk-warmtepompen-koeling-weer]]) — een in de NL-bronnen tot nu toe volledig afwezige vraagfactor; onduidelijk of een NL-gericht model deze factor al meeneemt.

### B. In het model, niet in bronnen
_(modelonderdelen die in géén verwerkte bron voorkomen — vul aan tijdens lint)_

## Openstaande vragen
- **Geen model aanwezig.** `raw/modellen/` is nog leeg — het model van Matthijs (of een ander model) moet nog aangeleverd worden voor de toetsingsfunctie (kolom 1) daadwerkelijk kan werken. Tot die tijd loggen we hier alleen welke mechanismen uit bronnen komen.
- _(tegenstrijdigheden tussen bronnen, kandidaten voor gerichte search, vervolgvragen)_
