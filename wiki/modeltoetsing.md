# modeltoetsing.md — observaties toetsen + blinde vlekken vinden

Deze pagina dient twee functies, allebei analytisch:

1. **Toetsing van observaties** — kunnen mechanismen die in verwerkte bronnen voorkomen geplaatst worden in een bestaand model van de energierekening?
2. **Blinde vlekken** — wat zit in de bronnen maar niet in het model, en omgekeerd?

Startpunt is het model/schema; zet dat in `raw/modellen/`. Andere modellen kunnen ernaast gelegd worden (extra kolommen in de tabel hieronder).

> Monitoring-kanttekening: dit is een toevallige greep bronnen, geen systematische meting. Gebruik dit voor signalering — niet voor uitspraken over hoe vaak iets speelt.

## 1. Toetsing van observaties

Onderhoud per mechanisme uit de bronnen: welke bronnen het noemen, waar het in het getoetste model zit, en of de plaatsing klopt.

| Mechanisme (concept) | Bronnen | Onderdeel in model | Past |
|---|---|---|---|
| [[balanceringsmarkt]] | [[0003-marktinrichting-hernieuwbare-energie-netbalans]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[netcongestie]] | [[0020-nederland-loopt-achter-vormgeven-nieuwe-energiemarkt]], [[0058-richt-beleid-efficient-gebruik-schaarse-energie]], [[0034-acm-akkoord-nettarieven-2027-2031]], [[0035-nettarieven-tijdsafhankelijk-piekmomenten]], [[0098-kosten-stroomnet-verdrievoudigen-2040]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[netkosten-transporttarieven]] | [[0034-acm-akkoord-nettarieven-2027-2031]], [[0035-nettarieven-tijdsafhankelijk-piekmomenten]], [[0098-kosten-stroomnet-verdrievoudigen-2040]], [[0029-acm-energierekening-stijgt-beter-contract]], [[0096-energienota-omhoog-door-dure-aanleg-stroomnet-op-zee-zo-comp]], [[0036-people-like-cheap-energy-the-bagel-shop-saving-money-and-emi]], [[0018-wonen-wordt-betaalbaarder-maar-energierekening-omhoog-dit-verandert-er-dit-jaar]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[salderen]] | [[0088-betalen-voor-terugleveren-stroom-verleden-tijd-tweede-kamer-]], [[0018-wonen-wordt-betaalbaarder-maar-energierekening-omhoog-dit-verandert-er-dit-jaar]], [[0052-huishoudens-betalen-in-2026-minder-voor-gas-en-elektra-door-dalende-leveringskosten]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[terugleververgoeding]] | [[0088-betalen-voor-terugleveren-stroom-verleden-tijd-tweede-kamer-]], [[0018-wonen-wordt-betaalbaarder-maar-energierekening-omhoog-dit-verandert-er-dit-jaar]], [[0052-huishoudens-betalen-in-2026-minder-voor-gas-en-elektra-door-dalende-leveringskosten]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[dynamische-prijzen]] | [[0020-nederland-loopt-achter-vormgeven-nieuwe-energiemarkt]], [[0035-nettarieven-tijdsafhankelijk-piekmomenten]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[energiebelasting]] | [[0020-nederland-loopt-achter-vormgeven-nieuwe-energiemarkt]], [[0046-analyse-beprijzing-broeikasgasemissies-nederland]], [[0018-wonen-wordt-betaalbaarder-maar-energierekening-omhoog-dit-verandert-er-dit-jaar]], [[0052-huishoudens-betalen-in-2026-minder-voor-gas-en-elektra-door-dalende-leveringskosten]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[ets2-beprijzing]] | [[0046-analyse-beprijzing-broeikasgasemissies-nederland]], [[0029-acm-energierekening-stijgt-beter-contract]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[warmtenet-tarieven]] | [[0004-de-sluitpost-van-het-warmtenet-moet-niet-de-bewoner-zijn]], [[0050-mogelijk-meer-betalen-bij-zuinig-gebruik-warmtenet]], [[0090-over-vijf-jaar-is-het-warmtenet-het-goedkoopst-maar-corporaties-twijfelen-nog]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[curtailment]] | [[0003-marktinrichting-hernieuwbare-energie-netbalans]], [[0020-nederland-loopt-achter-vormgeven-nieuwe-energiemarkt]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[energiearmoede]] | [[0098-kosten-stroomnet-verdrievoudigen-2040]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[leveringszekerheid]] | [[0020-nederland-loopt-achter-vormgeven-nieuwe-energiemarkt]], [[0074-vk-carbon-budget-delivery-plan]], [[0087-vk-warmtepompen-koeling-weer]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[capaciteitsmarkt]] | [[0020-nederland-loopt-achter-vormgeven-nieuwe-energiemarkt]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[co2-beprijzingstekort]] | [[0046-analyse-beprijzing-broeikasgasemissies-nederland]], [[0058-richt-beleid-efficient-gebruik-schaarse-energie]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[schaarste-allocatie-duurzame-energie]] | [[0058-richt-beleid-efficient-gebruik-schaarse-energie]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[energiecontracten]] | [[0029-acm-energierekening-stijgt-beter-contract]], [[0033-acm-energierekening-stijgt-bespaar-overstappen-gaslicht]], [[0039-eneco-happypower-loyaliteitsprogramma]], [[0040-overstapkosten-opzegtermijn-boetevrij]], [[0089-vk-groene-energiecontracten-afname]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[warmtepompen-verwarmingstransitie]] | [[0054-duitsland-verwarmingswet-terugdraaien]], [[0074-vk-carbon-budget-delivery-plan]], [[0087-vk-warmtepompen-koeling-weer]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[energiearmoede]] | [[0098-kosten-stroomnet-verdrievoudigen-2040]], [[0081-compensatie-hoge-energieprijzen-regeling-voor-huishoudens-me]], [[0102-aanvraag-noodfonds-energie-te-lastig-voor-veel-bredanaars-he]], [[0077-helft-nederlanders-vreest-hoge-kosten-door-energietransitie]], [[0106-noodfonds-energie-gesloten-210000-aanvragen-in-een-week]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[lokale-compensatie-energie-infrastructuur]] | [[0047-zeeuws-vlaanderen-eist-miljarden-als-kerncentrales-daar-worden-gebouwd]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[energielabel]] | [[0067-vereniging-eigen-huis-verbeteren-energielabel-voor-huiseigen]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[toegankelijkheid-regelingen]] | [[0102-aanvraag-noodfonds-energie-te-lastig-voor-veel-bredanaars-he]], [[0081-compensatie-hoge-energieprijzen-regeling-voor-huishoudens-me]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |
| [[macro-effecten-elektriciteitsprijzen]] | [[0021-effecten-elektriciteitsprijzen]] | _nog niet te toetsen — geen model aanwezig_ | _?_ |

_(Voeg rijen toe naarmate nieuwe mechanismen uit bronnen komen.)_

## 2. Blinde vlekken

### A. In bronnen, niet in het model
_(mechanismen die bronnen noemen maar die in het getoetste model geen plek lijken te hebben — vul aan tijdens ingest/lint)_
- Industriepolitieke allocatie van schaarse duurzame energie ([[schaarste-allocatie-duurzame-energie]]) — een keuze over *wie* toegang krijgt tot schaarse energie, los van marktprijs; onduidelijk of dit type mechanisme in een marktinrichtings-/netbalansmodel als dat van Matthijs een plek heeft.
- Aansluitkosten-financiering van warmtenetten ([[warmtenet-tarieven]], via [[0004-de-sluitpost-van-het-warmtenet-moet-niet-de-bewoner-zijn]]) — de Bijdrage AansluitKosten (BAK) en het "vollooprisico" zijn warmtenet-specifieke financieringsmechanismen zonder duidelijk equivalent in de tot nu toe verwerkte bronnen over elektriciteits-netkosten; onduidelijk of een marktinrichtings-/netbalansmodel dit warmte-specifieke vraagstuk meeneemt.
- Contractkeuze/leveranciersgedrag ([[energiecontracten]]) — prijsverschillen tussen contracten, opzegvoorwaarden en loyaliteitsprogramma's zijn een consumentengedrag-/marktwerkingsmechanisme dat losstaat van productie-, net- of beprijzingsmodellen; waarschijnlijk geen onderdeel van een marktinrichtings-/netbalansmodel als dat van Matthijs, maar wel relevant voor de energierekening zelf.
- Koelvraag/airconditioning ([[leveringszekerheid]], via [[0087-vk-warmtepompen-koeling-weer]]) — een in de NL-bronnen tot nu toe volledig afwezige vraagfactor; onduidelijk of een NL-gericht model deze factor al meeneemt.
- Uitvoeringsdetails van compensatieregelingen ([[energiearmoede]], via [[0081-compensatie-hoge-energieprijzen-regeling-voor-huishoudens-me]]) — of een huishouden steun krijgt hangt af van aansluitingstype (individueel vs. blok); dit soort uitvoeringstechnisch onderscheid past waarschijnlijk niet in een marktinrichtings-/netbalansmodel, maar is wel bepalend voor wie de energierekening daadwerkelijk kan betalen.
- Onderscheid terugleverkosten vs. terugleververgoeding ([[terugleververgoeding]], via [[0088-betalen-voor-terugleveren-stroom-verleden-tijd-tweede-kamer-]]) — publiek (zie reacties onder de bron) worden beide vaak door elkaar gehaald; een begrijpelijkheidsvraagstuk dat los staat van marktwerking maar wel de framing van "oneerlijke kosten" voedt.
- Uitvoeringstoegankelijkheid van regelingen ([[toegankelijkheid-regelingen]], via [[0102-aanvraag-noodfonds-energie-te-lastig-voor-veel-bredanaars-he]] en [[0081-compensatie-hoge-energieprijzen-regeling-voor-huishoudens-me]]) — of een huishouden een compensatieregeling daadwerkelijk verzilvert, hangt af van aanvraagprocedure, digitale vaardigheid, taal en aansluitingstype; dit uitvoeringsniveau ontbreekt structureel in marktinrichtings-/prijsmodellen.
- Energielabel als financieel instrument ([[energielabel]], via [[0067-vereniging-eigen-huis-verbeteren-energielabel-voor-huiseigen]]) — het label werkt door in woningwaarde en hypotheekvoorwaarden, een indirecte route naar woonlasten die los staat van het directe energieverbruik en tot nu toe in geen ander model-thema is ondergebracht.
- Macro-economische terugkoppeling van elektriciteitsprijzen ([[macro-effecten-elektriciteitsprijzen]], via [[0021-effecten-elektriciteitsprijzen]]) — effecten op inflatie, werkloosheid en industriële productie liggen op een ander schaalniveau dan de huishoudrekening; onduidelijk of een marktinrichtings-/netbalansmodel dit soort brede economische terugkoppeling meeneemt.

### B. In het model, niet in bronnen
_(modelonderdelen die in géén verwerkte bron voorkomen — vul aan tijdens lint)_

## Openstaande vragen
- **Geen model aanwezig.** `raw/modellen/` is nog leeg — het model van Matthijs (of een ander model) moet nog aangeleverd worden voor de toetsingsfunctie (kolom 1) daadwerkelijk kan werken. Tot die tijd loggen we hier alleen welke mechanismen uit bronnen komen.
- _(tegenstrijdigheden tussen bronnen, kandidaten voor gerichte search, vervolgvragen)_
