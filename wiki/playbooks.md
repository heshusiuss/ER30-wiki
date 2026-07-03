# playbooks.md — kant-en-klare prompts & queries

Plak de prompts in Claude Code; plak de Dataview-blokken in een Obsidian-notitie (plugin Dataview vereist). Zet bij elk overzicht de monitoring-kanttekening: toevallige greep bronnen, geen systematische zoektocht.

## Ingest

> Ik heb bron **NNNN** in `raw/articles/` gezet. Ingest hem volgens `CLAUDE.md`: maak de bronpagina met frontmatter, update betrokken concepts/ en entities/, werk `index.md` (en waar relevant `overview.md` en `modeltoetsing.md`) bij, en log het. Vat samen in eigen woorden.

Batch:
> Ingest alle nieuwe bestanden in `raw/articles/` één voor één volgens `CLAUDE.md`. Geef daarna een korte lijst van welke mechanismen nieuw bijkwamen.

## 1. Persofficier — media & journalisten

> Geef op basis van de verwerkte bronnen een overzicht per uitgever en per journalist: wie schrijft over welk thema en met welk frame. Markeer waar de exacte formulering opvalt.

```dataview
TABLE uitgever, auteur, themas, type
FROM "wiki/sources"
WHERE status = "verwerkt"
SORT uitgever ASC
```

## 2. Modeltoetsing — observaties toetsen + blinde vlekken

> Loop `modeltoetsing.md` na: welke mechanismen uit bronnen zijn (nog) niet plaatsbaar in het getoetste model (blinde vlek A), en welke modelonderdelen komen in geen enkele bron voor (blinde vlek B)? Werk beide secties bij.

```dataview
TABLE length(rows) AS aantal-bronnen
FROM "wiki/sources"
WHERE status = "verwerkt"
FLATTEN mechanismen AS m
GROUP BY m
SORT aantal-bronnen DESC
```

## 3. Thema-agenda team

> Groepeer de verwerkte bronnen op thema (taxonomie). Welke clusters zijn groot of opvallend, en welke lenen zich als onderwerp voor de voorraadagenda van het team?

```dataview
TABLE length(rows) AS aantal
FROM "wiki/sources"
WHERE status = "verwerkt"
FLATTEN themas AS t
GROUP BY t
SORT aantal DESC
```

## 4. Blinde vlekken

> Vergelijk de stakeholders en mechanismen die in onze bronnen voorkomen met wat je zou verwachten rond de energierekening. Wat ontbreekt opvallend? Stel 3–5 gerichte searches voor om die gaten te dichten.

Visueel: open de **graph view** in Obsidian — kleine of losstaande knopen bij `concepts/` en `entities/` zijn kandidaat-blinde-vlekken.

## Lint

> Doe een lint-pass volgens `CLAUDE.md`: tegenstrijdigheden tussen pagina's, verouderde claims, weespagina's, genoemde-maar-paginaloze mechanismen, ontbrekende kruisverwijzingen, en gaten in `modeltoetsing.md`. Geef een lijstje met voorgestelde acties.
