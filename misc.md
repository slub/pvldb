---
title: "PVLDB"
author: "Donatus Herre (SLUB Dresden)"
subtitle: "Bibliometric Analysis"
pagetitle: "PVLDB :: Bibliometric Analysis :: Outtakes"
author-meta: "SLUB Dresden"
date: "2022-10-18"
lang: "en-US"
output:
  html_document:
    toc: true
    toc_depth: 3
    toc_float:
      collapsed: false
      smooth_scroll: false
    mathjax: null
    includes:
      after_body: assets/html/target.html
    keep_md: true
---





Branches: [main](https://github.com/slub/pvldb/tree/main) / [gh-pages](https://github.com/slub/pvldb/tree/gh-pages)

# Count Data



## Works



![](/home/runner/work/pvldb/pvldb/public/misc_files/figure-html/journalsdb-works-count-plot-1.png)<!-- -->







![](/home/runner/work/pvldb/pvldb/public/misc_files/figure-html/scival-works-count-plot-1.png)<!-- -->

## Citations







![](/home/runner/work/pvldb/pvldb/public/misc_files/figure-html/scival-citations-count-plot-1.png)<!-- -->

# Raw Data

- JournalsDB (last update: 2022-10-17)
  - [journals](./data/journalsdb_journals_2150-8097.json) (`2150-8097`) [JSON, 3.96 KB]

# Data Sources

- [Crossref API](https://api.crossref.org)
  - prefixes
    - [10.1145](https://api.crossref.org/prefixes/10.1145?mailto=bibliometrie@slub-dresden.de)
  - works
    - [filter=issn:2150-8097,has-abstract:true](https://api.crossref.org/works?filter=issn:2150-8097,has-abstract:true&mailto=bibliometrie@slub-dresden.de)
    - [filter=issn:2150-8097,has-references:true](https://api.crossref.org/works?filter=issn:2150-8097,has-references:true&mailto=bibliometrie@slub-dresden.de)
    - [filter=issn:2150-8097&facet=type-name:*](https://api.crossref.org/works?filter=issn:2150-8097&facet=type-name:*&rows=0&mailto=bibliometrie@slub-dresden.de)
    - [filter=issn:2150-8097,type:journal-article](https://api.crossref.org/works?filter=issn:2150-8097,type:journal-article&mailto=bibliometrie@slub-dresden.de)
    - [filter=issn:2150-8097,type:journal-article,has-references:true](https://api.crossref.org/works?filter=issn:2150-8097,type:journal-article,has-references:true&mailto=bibliometrie@slub-dresden.de)
- [Crossref Event Data API](https://www.eventdata.crossref.org/)
  - events
    - [obj-id.prefix=10.14778](https://api.eventdata.crossref.org/v1/events?obj-id.prefix=10.14778&mailto=bibliometrie@slub-dresden.de)
    - [subj-id.prefix=10.14778](https://api.eventdata.crossref.org/v1/events?subj-id.prefix=10.14778&mailto=bibliometrie@slub-dresden.de)
- [ISSN Portal LD Service](https://www.issn.org/understanding-the-issn/assignment-rules/issn-linked-data-application-profile/)
  - resource/ISSN
    - [2150-8097](https://portal.issn.org/resource/ISSN/2150-8097?format=json)
  - resource/ISSN-L
    - [2150-8097](https://portal.issn.org/resource/ISSN-L/2150-8097?format=json)
- [JournalsDB API](https://api.journalsdb.org/apidocs/)
  - journals
    - [2150-8097](https://api.journalsdb.org/journals/2150-8097)
- [Wikidata](https://www.wikidata.org/wiki/Wikidata:Data_access)
  - Linked Data Interface
    - [Q27722874](https://www.wikidata.org/wiki/Special:EntityData/Q27722874.json)
- [SLUB LOD API](https://data.slub-dresden.de/)
  - resource
    - [591517426](https://data.slub-dresden.de/resources/591517426)
  - source/kxp-de14
    - [591517426](https://data.slub-dresden.de/source/kxp-de14/591517426)

# Usage Terms

[![Creative Commons License](https://mirrors.creativecommons.org/presskit/buttons/80x15/svg/by.svg)](http://creativecommons.org/licenses/by/4.0/) This [document](#) is licensed under a [Creative Commons Attribution 4.0 International License](./LICENSE.txt).  
[![Public Domain Dedication](https://mirrors.creativecommons.org/presskit/buttons/80x15/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/) The [raw data](#raw-data) is made available under the [CC0 1.0 Universal Public Domain Dedication](./data/LICENSE.txt).
