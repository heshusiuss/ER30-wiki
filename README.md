# LLM-wiki Energierekening — setup

Een meegroeiende kennisbank volgens het patroon van Andrej Karpathy (immutable `raw/` → door de LLM onderhouden `wiki/` → `CLAUDE.md` als schema). De kennisbank bedient meerdere doelen: persmonitoring, thema-agendering voor het team, blinde-vlekken-detectie, en het toetsen van observaties aan bestaande modellen van de energierekening (zoals dat van Matthijs).

## Eenmalige setup

1. **Obsidian** installeren en deze map als *vault* openen (Obsidian = je leesvenster; de graph view toont meteen welke mechanismen veel/weinig verbindingen hebben — handig voor de blinde-vlekken-lens).
2. **Claude Code** in deze map starten (terminal: `claude` in de vaultmap). Claude Code = de agent die `wiki/` schrijft. `CLAUDE.md` wordt automatisch ingelezen.
3. **git init** in deze map → versiegeschiedenis en delen met het team voor niets.
4. **Obsidian Web Clipper** (browserextensie) installeren; opslaglocatie op `raw/articles/`. Of gebruik de fetcher (zie hieronder) voor de open bronnen.
5. Optioneel: plugin **Dataview** (rapporten over de frontmatter) en, later, een zoeklaag zoals `qmd`.

## Wat er klaarstaat

- `CLAUDE.md` — de afspraken (paginatypes, frontmatter, ingest/query/lint).
- `wiki/index.md` — catalogus + **ingest-backlog van 114 bronnen** uit de oorspronkelijke lijst, gegroepeerd op toegang.
- `wiki/taxonomie.md` — gecontroleerde thema-woordenlijst (7 hoofdcategorieën).
- `wiki/overview.md`, `wiki/log.md` — lopende synthese en logboek.
- `wiki/modeltoetsing.md` — analytische pagina met twee functies: observaties uit bronnen toetsen aan een model, en blinde vlekken in dat model benoemen. Het model van Matthijs is het startpunt.
- `wiki/playbooks.md` — kant-en-klare prompts en Dataview-queries voor de vier doelen.
- 11 concept-stubs (mechanismen) en 10 entity-stubs (stakeholders) in `wiki/concepts/` en `wiki/entities/`, plus templates en één voorbeeld in `wiki/sources/`.

## Zo werk je

1. Pak een bron uit de backlog in `index.md`, haal de tekst in `raw/articles/` (handmatig via MarkDownload, of via het fetch-script voor de open bronnen — zie volgende kop), en zeg tegen Claude Code:

   > *Ik heb bron NNNN in raw/articles/ gezet. Ingest hem volgens CLAUDE.md.*

   De agent maakt de bronpagina, update concepten/entiteiten, werkt `overview.md` en (waar relevant) `modeltoetsing.md` bij, en logt.

2. **Bevragen:** stel je vraag; de agent leest eerst `index.md` en synthetiseert met bronverwijzing. Goede antwoorden laat je terugschrijven als wiki-pagina.

3. **Lint** af en toe: *Doe een lint-pass volgens CLAUDE.md* → tegenstrijdigheden, weespagina's, lege secties.

4. **Wil je de modeltoetsings-lens gebruiken**: zet het model van Matthijs (of een ander model) in `raw/modellen/`, en vraag Claude Code de tabel in `modeltoetsing.md` bij te werken op basis van wat er al verwerkt is.

## Bronnen binnenhalen — drie paden

Je hoeft die 114 artikelen niet handmatig te clippen.

**Tier 1 — script voor open bronnen (nul kliks).** `fetch_open_sources.py` (in deze map) haalt alles met `Open*`-toegang automatisch op naar `raw/articles/`:

```
pip install -r requirements.txt
python fetch_open_sources.py ../Corpus_energierekening_opgeschoond.xlsx
```

Idempotent — opnieuw draaien is veilig. Met `--include-partial` ook deels-betaalde bronnen meenemen.

**Tier 2 — MarkDownload voor de paywall (één klik per artikel).** Browserextensie; werkt terwijl je in FD/Energeia bent ingelogd → schone markdown in je downloadmap → naar `raw/articles/`.

**Tier 3 — volledig geautomatiseerd, als je dat wilt.**
- **Claude in Chrome** (browsing-agent) draait in je eigen ingelogde browser en kan een URL-lijst afwerken.
- **Knipseldienst / Nexis Uni / LexisNexis** als je organisatie er toegang toe heeft — gelicentieerde fulltext-aggregatie met batch-export.
- **Cookies-gebaseerde uitbreiding** van het script (op aanvraag).

## Toegang / auteursrecht

De organisatie-licentie maakt intern delen prima. Eén punt om los te checken bij de licentiebeheerder: of *geautomatiseerd* artikelen ophalen onder de gebruiksvoorwaarden valt — dat is een aparte clausule van delen-binnen-de-organisatie. Meestal is een redelijke hoeveelheid voor interne analyse oké. (Geen juridisch advies.)

## Schaal

Dit patroon werkt prettig tot ~enkele honderden bronnen. Daarboven: overstappen op echte RAG met embeddings/vector-database.
