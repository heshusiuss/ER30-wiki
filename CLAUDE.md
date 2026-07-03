# CLAUDE.md — schema voor de LLM-wiki "Energierekening"

Dit bestand vertelt je (de LLM-agent) hoe deze wiki is opgebouwd en welke werkwijze je volgt bij **ingest**, **query** en **lint**. Volg dit strikt; wijk alleen af in overleg met de beheerder en werk de wijziging hierin bij.

## Doel

Een meegroeiende kennisbank over de Nederlandse energierekening: welke mechanismen, stakeholders, frames en discussies in de pers terugkomen. De kennisbank bedient meerdere analytische doelen, gelijkwaardig:

- **persmonitoring** — welke media en journalisten, welke frames;
- **thema-agendering** voor het team;
- **blinde-vlekken-detectie** — wat valt op, wat ontbreekt;
- **modeltoetsing** — observaties uit bronnen toetsen aan bestaande modellen van de energierekening (zoals dat van Matthijs), en blinde vlekken in die modellen vinden.

**Geen conclusies over frequentie of representativiteit.** Het bronmateriaal is een toevallige greep, geen systematische zoektocht. Label analyses als *monitoring/signalering*, niet als onderzoek. Zet die kanttekening expliciet in elk overzichtsantwoord.

## Drie lagen (Karpathy-patroon)

- `raw/` — **onaantastbaar**. Bronteksten zoals binnengehaald (artikelen als markdown, rapporten als pdf, modellen). Jij leest hieruit, je wijzigt hier nooit iets.
- `wiki/` — **van jou**. Alle gegenereerde markdown: bronpagina's, entiteiten, concepten, overzicht, index, log, en analytische pagina's zoals modeltoetsing. Jij maakt en onderhoudt deze volledig.
- `CLAUDE.md` (dit bestand) — de afspraken.

## Mappen en naamgeving

```
raw/articles/      bronartikelen (markdown), 1 bestand per artikel
raw/reports/       rapporten/pdf's (PBL, TNO, ACM, ...)
raw/modellen/      modellen/schema's waaraan we observaties toetsen (Matthijs en evt. anderen)
raw/assets/        afbeeldingen
wiki/sources/      1 samenvattingspagina per bron — bestandsnaam: NNNN-korte-slug.md
wiki/entities/     1 pagina per stakeholder — slug.md (bv. acm.md, tno.md)
wiki/concepts/     1 pagina per mechanisme/concept — slug.md (bv. netcongestie.md)
wiki/overview.md   lopende synthese
wiki/modeltoetsing.md  analytische pagina voor de modeltoetsings-lens
wiki/index.md      catalogus van álle pagina's (lees dit eerst bij een query)
wiki/log.md        chronologisch logboek (append-only)
wiki/taxonomie.md  gecontroleerde thema-woordenlijst
wiki/playbooks.md  kant-en-klare prompts en queries
```

## Frontmatter voor bronpagina's (`wiki/sources/`)

Elke bronpagina begint met deze YAML. Vul niets in dat niet in de bron staat; laat onbekend leeg.

```yaml
---
id: 6
titel: "..."
uitgever: "Energeia"          # bv. Energeia, BNR, NOS, Trouw, PBL
type: "nieuws"                # nieuws | opinie | analyse | rapport | commercieel | uitleg
auteur: ""                    # journalist, indien bekend
datum: ""                     # YYYY-MM-DD publicatiedatum
themas: ["..."]               # ALLEEN labels uit taxonomie.md
mechanismen: ["..."]          # verwijst naar concepts/
stakeholders: ["ACM"]         # verwijst naar entities/
scope: "NL"                   # NL | regionaal | EU | buitenland
toegang: "betaalmuur"         # open | betaalmuur | deels | archief
url: ""
status: "verwerkt"            # te-doen | verwerkt
ingest-datum: "YYYY-MM-DD"
---
```

Daaronder, in proza en in **eigen woorden** (geen letterlijke overname, zie Auteursrecht):
1. **Kernstelling** (1–2 zinnen).
2. **Belangrijkste punten / cijfers**.
3. **Genoemde mechanismen** met `[[wikilink]]` naar de concept-pagina('s).
4. **Frame/standpunt** (bv. "transitie maakt energie duurder" vs "kosten dalen").
5. **Toetsing & blinde vlekken** — passen de genoemde mechanismen in modellen die we toetsen? Wat valt op of ontbreekt? (Voedt `modeltoetsing.md`.)
6. **Links** naar betrokken `[[entities]]`.

## Gecontroleerde thema-woordenlijst

Gebruik uitsluitend de labels uit `wiki/taxonomie.md`. Kom je een thema tegen dat er niet in staat, voeg het niet zomaar toe: stel het voor aan de beheerder en werk daarna `taxonomie.md` bij.

## Stakeholders (entities)

Begin met o.a.: ACM, Consumentenbond, TNO, PBL, netbeheerders (TenneT, Enexis, ...), energieleveranciers (Eneco, Vattenfall, ...), warmtebedrijven, ministerie/politiek (Tweede Kamer, minister), Noodfonds Energie. Maak een entity-pagina aan zodra een stakeholder in ≥1 bron voorkomt; verzamel daarop wat de bronnen over die partij zeggen, met `[[wikilinks]]`.

## Modeltoetsing (analytische lens)

`wiki/modeltoetsing.md` is een analytische pagina, geen organisatiecentrum. Twee functies: (a) **toetsen** of mechanismen uit bronnen plaatsbaar zijn in een bestaand model; (b) **blinde vlekken** benoemen — in bronnen of in het model. Het model van Matthijs (in `raw/modellen/`) is het startpunt; meer modellen kunnen ernaast. Bij ingest werk je deze pagina alleen bij waar het meerwaarde heeft.

## Operaties

**Ingest.** Beheerder zet een bron in `raw/`. Jij: (1) lees de bron; (2) bespreek kort de kernpunten; (3) maak `wiki/sources/NNNN-slug.md` met frontmatter + samenvatting in eigen woorden; (4) maak/again update betrokken `concepts/` en `entities/`; (5) werk waar relevant `modeltoetsing.md` en `overview.md` bij; (6) werk `index.md` bij; (7) voeg een regel toe aan `log.md`. Eén bron raakt typisch 5–15 pagina's. Ingest één bron tegelijk, tenzij de beheerder om een batch vraagt.

**Query.** Lees eerst `index.md`, bepaal de relevante pagina's, lees die, en synthetiseer met bronverwijzing (`[[source]]`). Goede antwoorden sla je terug op als wiki-pagina. Zet bij overzichten de monitoring-kanttekening.

**Lint.** Periodieke gezondheidscheck: tegenstrijdigheden tussen pagina's, verouderde claims, weespagina's zonder inkomende links, mechanismen die wel genoemd maar geen eigen concept-pagina hebben, ontbrekende kruisverwijzingen, en gaten in `modeltoetsing.md`. Rapporteer en stel vervolgvragen/bronnen voor.

## Logboek-conventie

Append-only. Begin elke regel met een vast prefix zodat het met `grep` te lezen is:
`## [YYYY-MM-DD] ingest | Titel` — of `query` / `lint` in plaats van `ingest`.

## Auteursrecht & toegang

- In `raw/` staat volledige brontekst; in `wiki/` staan **samenvattingen in eigen woorden**, nooit letterlijk overgenomen alinea's. Citeer hooguit een korte kernzin als de exacte formulering ertoe doet.
- Toegang en distributie van betaalde bronnen volgt de licentievoorwaarden van de organisatie. Bij twijfel: afstemmen met de licentiebeheerder.

## Bevraagbaar voor iedereen (later)

Fase 1: de beheerder draait de agent; team bladert in Obsidian (graph view voor de blinde-vlekken-blik). Fase 2 (nice-to-have): wiki als git-repo delen en een zoeklaag toevoegen (bv. `qmd` met MCP-server), zodat collega's zelf bevragen. Niet nodig voor de eerste implementatie.
