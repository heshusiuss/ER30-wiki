# Workflow – LLM-wiki energierekening (Karpathy-patroon)

Opzet voor een gedeelde kennisbank over de Nederlandse energierekening, volgens het LLM-wiki-patroon van Andrej Karpathy. De kennisbank bedient vier analytische doelen gelijkwaardig: persmonitoring, thema-agendering, blinde-vlekken-detectie, en het toetsen van observaties aan bestaande modellen van de energierekening. Volledige teksten in `raw/`, met FD/Energeia via de organisatie-licentie en — als nice-to-have — uiteindelijk voor iedereen bevraagbaar.

## Het patroon in het kort

Karpathy beschrijft (gist, april 2026) een kennisbank van drie lagen, onderhouden door een LLM in plaats van met RAG: je indexeert bronnen in een `raw/`-map en gebruikt een LLM om daaruit incrementeel een wiki te "compileren" — een verzameling .md-bestanden in een mappenstructuur. Het verschil met gewone RAG: in plaats van bij elke vraag opnieuw uit de ruwe documenten op te halen, bouwt en onderhoudt de LLM een blijvende wiki — een gestructureerde, onderling gelinkte verzameling markdown die tussen jou en de bronnen in zit. De kennis wordt één keer samengevat en daarna actueel gehouden. De drie lagen zijn ruwe bronnen (onaantastbaar), de wiki (door de LLM gegenereerde markdown), en het schema — een CLAUDE.md die de LLM vertelt hoe de wiki is gestructureerd en welke workflows te volgen.

Er zijn drie operaties: ingest (nieuwe bronnen verwerken), query (vragen stellen) en lint (gezondheidschecks). Twee navigatiebestanden helpen: index.md is de inhoudscatalogus die je bij een query als eerste leest, en log.md is een chronologisch, append-only logboek. Tooling: Obsidian als vault, Claude Code als agent dat de bron leest, wikipagina's maakt en relaties legt. Schaal: dit werkt goed tot een paar honderd documenten; voor miljoenen documenten gebruik je een echte RAG-pijplijn.

## Wat er klaarstaat

In `energiewiki.zip` zit een werkende skelet-vault:

- **`CLAUDE.md`** — het schema, toegesneden op dit domein: paginatypes, frontmatter per bron (uitgever, type, auteur, datum, thema's, mechanismen, stakeholders, scope, toegang), de ingest/query/lint-workflows, en de logboek-conventie.
- **`wiki/index.md`** — catalogus + ingest-backlog van alle 114 bronnen, gegroepeerd op toegang.
- **`wiki/taxonomie.md`** — opgeschoonde, gecontroleerde thema-woordenlijst (7 hoofdcategorieën).
- **`wiki/modeltoetsing.md`** — analytische pagina met twee functies: observaties uit bronnen toetsen aan een bestaand model, en blinde vlekken in dat model benoemen. Het model van Matthijs is het startpunt (in `raw/modellen/`); andere modellen kunnen ernaast.
- **`wiki/overview.md`**, **`wiki/log.md`**, **`wiki/playbooks.md`** (kant-en-klare prompts en Dataview-queries), plus 11 concept-stubs (mechanismen) en 10 entity-stubs (stakeholders).
- **`fetch_open_sources.py`** + `requirements.txt` — script dat ~60 open bronnen automatisch in `raw/articles/` zet.

## De vier doelen, als gelijkwaardige analytische lenzen

- **Persofficier-overleg** → overzicht per uitgever en per journalist; welke titels/auteurs pakken het thema, met welk frame.
- **Thema-agenda team** → groepeer op hoofdcategorie/thema uit de taxonomie; clusters zijn kandidaat-onderwerpen.
- **Blinde vlekken** → twee invalshoeken: thema's/stakeholders die in jullie werk leven maar nauwelijks in de pers; en omgekeerd. Graph view in Obsidian maakt dit visueel.
- **Modeltoetsing** → in `modeltoetsing.md`: passen mechanismen uit bronnen in een bestaand model (startpunt: dat van Matthijs)? Welke blinde vlekken treden op in dat model?

Zet bij elk overzicht de monitoring-kanttekening: toevallige greep, geen systematische zoektocht — geen conclusies over frequentie.

## Bronnen binnenhalen — drie tiers

**Tier 1 — script voor open bronnen (nul kliks).** `fetch_open_sources.py` haalt alles met `Open*`-toegang automatisch op. Eén commando, klaar binnen een paar minuten.

**Tier 2 — MarkDownload voor de paywall.** Browserextensie; één klik per artikel terwijl je in FD/Energeia bent ingelogd → markdown in je downloadmap → naar `raw/articles/`.

**Tier 3 — als je nul kliks wilt voor àlles.** Claude in Chrome (AI-driven browsing in je eigen sessie), knipseldienst/Nexis (gelicentieerde batch-export), of een cookies-gebaseerde uitbreiding van het script (op aanvraag).

## Toegang en delen

Organisatie-licentie maakt intern delen prima — dat haalt de scherpste rand van de gedeelde wiki af. Eén punt om los te checken bij de licentiebeheerder: of *geautomatiseerd* ophalen onder de gebruiksvoorwaarden valt — een aparte clausule van delen-binnen-de-organisatie.

## Bevraagbaar voor iedereen (later)

- **Fase 1 (nu):** jij draait Claude Code en doet ingest/query; team bladert mee in Obsidian. De wiki is een git-repo, dus delen en versiebeheer zijn gratis.
- **Fase 2 (later):** zoeklaag toevoegen zodat collega's zelf bevragen. Karpathy noemt hiervoor `qmd` (CLI + MCP-server).

## Starten

1. Pak de zip uit, open de map als Obsidian-vault, start Claude Code erin, `git init`.
2. Draai `fetch_open_sources.py` voor de ~60 open bronnen.
3. Begin met ingest van een paar artikelen (per stuk: "ingest bron NNNN volgens CLAUDE.md").
4. Wil je de modeltoetsings-lens gebruiken: zet het model van Matthijs in `raw/modellen/` en laat de agent `modeltoetsing.md` bijwerken.

Volledige stap-voor-stap staat in `README.md` in de zip.
