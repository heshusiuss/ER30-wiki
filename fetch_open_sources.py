#!/usr/bin/env python3
"""
fetch_open_sources.py — bulk-haalt open bronnen uit de corpus-Excel
                       en zet ze als markdown in raw/articles/.

Gebruik (vanuit de vault-map):
    pip install -r requirements.txt
    python fetch_open_sources.py ../Corpus_energierekening_opgeschoond.xlsx

Wat het doet
------------
- Leest het tabblad 'Corpus'.
- Pakt alleen rijen met toegang 'Open*' (open, open (deels), open (instantie),
  open (commercieel)). Voeg --include-partial toe om ook 'Deels betaalmuur' te
  proberen — een deel werkt zonder login.
- Haalt elke URL op met een nette User-Agent en 2 sec rate-limit.
- Extraheert de hoofdtekst met trafilatura (sterk in NL) naar markdown.
- Schrijft NNNN-slug.md in raw/articles/, met titel + bron + url in de header.
- Slaat over wat al bestaat (idempotent — gewoon opnieuw draaien is veilig).
- Eindigt met een rapport: geslaagd / overgeslagen / mislukt-met-reden.

Wat het NIET doet
-----------------
- FD, Energeia, NRC, archive.is: die laat het script staan. Pak die met
  MarkDownload (één klik per artikel, terwijl je ingelogd bent), of vraag
  me om een cookies-gebaseerde variant.
"""
import sys
import time
import argparse
import pathlib
import pandas as pd
import requests
import trafilatura
from slugify import slugify

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def fetch_one(url: str) -> str | None:
    """Haal URL op en geef schone markdown terug, of None bij mislukken."""
    r = requests.get(url, headers={"User-Agent": UA}, timeout=20)
    r.raise_for_status()
    md = trafilatura.extract(
        r.text,
        include_links=False,
        include_images=False,
        favor_recall=True,
        output_format="markdown",
    )
    return md if md and len(md) >= 200 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("excel", help="pad naar Corpus_energierekening_opgeschoond.xlsx")
    ap.add_argument("--out", default="raw/articles", help="uitvoermap")
    ap.add_argument("--include-partial", action="store_true",
                    help="ook 'Deels betaalmuur' proberen (kan deels lukken)")
    ap.add_argument("--delay", type=float, default=2.0,
                    help="seconden tussen requests (default 2)")
    args = ap.parse_args()

    df = pd.read_excel(args.excel, sheet_name="Corpus")
    mask = df["Toegang"].astype(str).str.startswith("Open")
    if args.include_partial:
        mask |= df["Toegang"].astype(str).str.startswith("Deels")
    df = df[mask & df["URL"].astype(str).str.startswith("http")]
    print(f"Te proberen: {len(df)} bronnen")

    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    ok = skipped = 0
    failed: list[tuple[int, str, str]] = []
    for _, row in df.iterrows():
        nr = int(row["ID"])
        title = str(row["Titel"]).strip()
        slug = (slugify(title) or "artikel")[:60]
        path = out_dir / f"{nr:04d}-{slug}.md"
        if path.exists():
            skipped += 1
            continue
        url = row["URL"]
        try:
            md = fetch_one(url)
            if md is None:
                failed.append((nr, url, "extractie leeg / te kort (waarschijnlijk paywall of JS-rendered)"))
                continue
            header = (f"# {title}\n\n"
                      f"_Bron: {row['Bron (uitgever)']} · {url}_\n\n"
                      "---\n\n")
            path.write_text(header + md, encoding="utf-8")
            ok += 1
            print(f"  + {nr:04d}  {row['Bron (uitgever)']}")
        except Exception as e:
            failed.append((nr, url, type(e).__name__ + ": " + str(e)[:80]))
        time.sleep(args.delay)

    print(f"\nKlaar. {ok} opgehaald · {skipped} al aanwezig · {len(failed)} mislukt.")
    if failed:
        print("\nMislukt (pak deze met MarkDownload of vraag de cookies-variant):")
        for nr, url, reason in failed:
            print(f"  {nr:04d}  {reason}\n         {url}")


if __name__ == "__main__":
    main()
