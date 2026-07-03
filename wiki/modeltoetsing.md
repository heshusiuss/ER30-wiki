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
| [[netcongestie]] | _(vul bij ingest)_ | _?_ | _?_ |
| [[netkosten-transporttarieven]] | | _?_ | _?_ |
| [[salderen]] | | _?_ | _?_ |
| [[terugleververgoeding]] | | _?_ | _?_ |
| [[dynamische-prijzen]] | | _?_ | _?_ |
| [[energiebelasting]] | | _?_ | _?_ |
| [[ets2-beprijzing]] | | _?_ | _?_ |
| [[warmtenet-tarieven]] | | _?_ | _?_ |
| [[curtailment]] | | _?_ | _?_ |
| [[energiearmoede]] | | _?_ | _?_ |
| [[leveringszekerheid]] | | _?_ | _?_ |

_(Voeg rijen toe naarmate nieuwe mechanismen uit bronnen komen.)_

## 2. Blinde vlekken

### A. In bronnen, niet in het model
_(mechanismen die bronnen noemen maar die in het getoetste model geen plek lijken te hebben — vul aan tijdens ingest/lint)_

### B. In het model, niet in bronnen
_(modelonderdelen die in géén verwerkte bron voorkomen — vul aan tijdens lint)_

## Openstaande vragen
- **Geen model aanwezig.** `raw/modellen/` is nog leeg — het model van Matthijs (of een ander model) moet nog aangeleverd worden voor de toetsingsfunctie (kolom 1) daadwerkelijk kan werken. Tot die tijd loggen we hier alleen welke mechanismen uit bronnen komen.
- _(tegenstrijdigheden tussen bronnen, kandidaten voor gerichte search, vervolgvragen)_
