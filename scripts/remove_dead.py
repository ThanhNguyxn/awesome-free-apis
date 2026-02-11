#!/usr/bin/env python3
"""Remove known dead links from README.md."""

import re
import sys

reconfigure_stdout = getattr(sys.stdout, "reconfigure", None)
if callable(reconfigure_stdout):
    reconfigure_stdout(encoding="utf-8", errors="replace")

DEAD_URLS = [
    "http://18f.github.io/API-All-the-X/",
    "http://data.deutschebahn.com/dataset/api-fahrplan",
    "http://opendata.praha.eu/en",
    "http://ratings.food.gov.uk/open-data/en-GB",
    "https://0x.org/api",
    "https://aninditabasu.github.io/indica/html/rv.html",
    "https://aninditabasu.github.io/indica/html/vs.html",
    "https://api.gitguardian.com/doc",
    "https://bittrex.github.io/api/v3",
    "https://bybit-exchange.github.io/docs/linear/#t-introduction",
    "https://circleci.com/docs/api/v1-reference/",
    "https://cloudflare-quic.com/b/",
    "http://data.gov.sg/developer",
    "https://data.rijksmuseum.nl/object-metadata/api/",
    "https://dev.blablacar.com",
    "https://developers.revolt.chat/api/",
    "https://developers.sendinblue.com/docs",
    "https://docs.alchemy.com/alchemy/",
    "https://docs.aylien.com/textapi/#getting-started",
    "https://github.com/melpon/wandbox/blob/master/kennel2/API.rst",
    "https://coinlib.io/apidocs",
    "https://crafatar.com",
    "https://api.mangadex.org/docs.html",
    "https://data.gov.sg/developer",
    "https://docs.sportmonks.com/cricket/",
    "https://duply.co/docs#getting-started-api",
    "https://geodata.gov.hk/gs/",
    "https://github.com/Dehash-lt/api",
    "https://github.com/FayasNoushad/Short-Link-API",
    "https://github.com/GurbaniNow/api",
    "https://github.com/Jaagrav/CodeX",
    "https://localbitcoins.com/api-docs/",
    "https://owlbot.info/",
    "https://owo.vc/api",
    "https://quoteclear.web.app/",
    "https://random-words-api.vercel.app/word",
    "https://shrtlnk.dev/developer",
    "https://sportdataapi.com",
    "https://tyk.io/open-source/",
    "https://uselection.togatech.org/api/",
    "https://www.cloverly.com/carbon-offset-documentation",
    "https://www.hpb.health.gov.lk/en/api-documentation",
    "https://www.machinetutors.com/portfolio/MT_api.html",
    "https://www.saidit.net/dev/api",
    "https://www.tcgdex.net/docs",
    "https://www.usa.gov/developer",
    "https://www.yelp.com/developers/documentation/v3",
]

readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

removed = 0
new_lines = []
for line in lines:
    skip = False
    for url in DEAD_URLS:
        if url in line and line.strip().startswith("|"):
            skip = True
            removed += 1
            print(f"  Removed: {url}")
            break
    if not skip:
        new_lines.append(line)

with open(readme_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

total = len(re.findall(r"\|\s*\*\*[^|]+\*\*\s*\|", "".join(new_lines)))
print(f"\nRemoved {removed} dead links. Total APIs now: {total}")
