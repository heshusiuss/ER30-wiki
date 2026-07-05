# log.md — chronologisch logboek (append-only)

Elke regel begint met `## [YYYY-MM-DD] <operatie> | <titel>`. Zo werkt:
`grep "^## \[" wiki/log.md | tail -5` voor de laatste 5 acties.

## [2026-06-08] setup | Wiki opgezet volgens Karpathy-patroon; backlog van 114 bronnen in index.md; taxonomie en model-matthijs gescaffold
## [2026-06-08] setup | 11 concept-stubs + 10 entity-stubs aangemaakt en gekoppeld; playbooks.md toegevoegd; index bijgewerkt
## [2026-06-08] setup | fetch_open_sources.py + requirements.txt toegevoegd; README bijgewerkt met drie-tiers bulk-aanpak

## [2026-06-08] refactor | wiki gedecentraliseerd; model-matthijs.md → modeltoetsing.md (analytische lens i.p.v. organisatiecentrum); raw/schema-matthijs → raw/modellen; CLAUDE.md en README herschreven

## [2026-07-03] setup | omgeving + 23/52 open bronnen opgehaald via fetch_open_sources.py (rest geblokkeerd door BNR-botdetectie); eerste git-commit van het skelet
## [2026-07-03] ingest | Bron 3 (ESB, marktinrichting/netbalans) verwerkt; nieuw concept [[balanceringsmarkt]] aangemaakt, [[curtailment]] aangevuld, entity [[energie-nederland]] aangemaakt, [[tennet]] aangevuld, modeltoetsing.md + overview.md bijgewerkt. Blinde vlek genoteerd: raw/modellen/ is nog leeg, toetsingsfunctie kan nog niet echt werken.
## [2026-07-05] ingest | Cluster Marktinrichting afgerond: bron 20 (ESB, marktordening NL vs. DE/VK), bron 46 (PBL, CO2-beprijzing 2024) en bron 58 (ESB, schaarste-allocatie duurzame energie) verwerkt. Nieuwe concepten [[capaciteitsmarkt]], [[co2-beprijzingstekort]], [[schaarste-allocatie-duurzame-energie]]; [[curtailment]], [[dynamische-prijzen]], [[leveringszekerheid]], [[netcongestie]], [[ets2-beprijzing]], [[energiebelasting]] aangevuld; entities [[pbl]], [[tno]], [[tennet]], [[ministerie-politiek]] aangevuld. modeltoetsing.md (nieuwe rijen + blinde vlek industriepolitieke allocatie) en overview.md (twee hoofdlijnen, spanning compensatie-vs-schaarste-sturing) bijgewerkt.
