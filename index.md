---
title: "PVLDB"
author: "Donatus Herre"
subtitle: "Bibliometric Analysis"
pagetitle: "PVLDB :: Bibliometric Analysis"
author-meta: "SLUB Dresden"
date: "2022-10-11"
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



![](/home/runner/work/pvldb/pvldb/public/index_files/figure-html/crossref-works-count-plot-1.png)<!-- -->



![](/home/runner/work/pvldb/pvldb/public/index_files/figure-html/journalsdb-works-count-plot-1.png)<!-- -->



![](/home/runner/work/pvldb/pvldb/public/index_files/figure-html/openalex-works-count-plot-1.png)<!-- -->

## Citations



![](/home/runner/work/pvldb/pvldb/public/index_files/figure-html/openalex-citations-count-plot-1.png)<!-- -->



![](/home/runner/work/pvldb/pvldb/public/index_files/figure-html/jcr-citations-count-plot-1.png)<!-- -->

# Raw Data

- Crossref
  - [works](./data/crossref_works_filter-issn-2150-8097.json) (`filter=issn:2150-8097`) [JSON, 29.05 MB]
    - [prefixes](./data/crossref_works_filter-issn-2150-8097_prefixes.json) [JSON, 16 B]
    - [dois](./data/crossref_works_filter-issn-2150-8097_dois.json) [JSON, 103.08 KB]
    - [dois-article](./data/crossref_works_filter-issn-2150-8097_dois-article.json) [JSON, 100.42 KB]
    - [reference](./data/crossref_works_filter-issn-2150-8097_reference.json) [JSON, 2.01 MB]
    - [year-types](./data/crossref_works_filter-issn-2150-8097_year-types.json) [JSON, 79.79 KB]

# Data Sources

- [Crossref API](https://api.crossref.org)
  - members
    - [320](https://api.crossref.org/members/320?mailto=bibliometrie@slub-dresden.de)
    - [5777](https://api.crossref.org/members/5777?mailto=bibliometrie@slub-dresden.de)
  - prefixes
    - [10.1145](https://api.crossref.org/prefixes/10.1145?mailto=bibliometrie@slub-dresden.de)
    - [10.14778](https://api.crossref.org/prefixes/10.14778?mailto=bibliometrie@slub-dresden.de)
  - journals
    - [2150-8097](https://api.crossref.org/journals/2150-8097?mailto=bibliometrie@slub-dresden.de)
  - works
    - [filter=issn:2150-8097](https://api.crossref.org/works?filter=issn:2150-8097&mailto=bibliometrie@slub-dresden.de)
    - [filter=issn:2150-8097,has-abstract:true](https://api.crossref.org/works?filter=issn:2150-8097,has-abstract:true&mailto=bibliometrie@slub-dresden.de)
    - [filter=issn:2150-8097,has-references:true](https://api.crossref.org/works?filter=issn:2150-8097,has-references:true&mailto=bibliometrie@slub-dresden.de)
    - [filter=issn:2150-8097&facet=type-name:*](https://api.crossref.org/works?filter=issn:2150-8097&facet=type-name:*&rows=0&mailto=bibliometrie@slub-dresden.de)
    - [filter=issn:2150-8097,type:journal-article](https://api.crossref.org/works?filter=issn:2150-8097,type:journal-article&mailto=bibliometrie@slub-dresden.de)
    - [filter=issn:2150-8097,type:journal-article,has-references:true](https://api.crossref.org/works?filter=issn:2150-8097,type:journal-article,has-references:true&mailto=bibliometrie@slub-dresden.de)
- [Crossref Event Data API](https://www.eventdata.crossref.org/)
  - events
    - [obj-id.prefix=10.14778](https://api.eventdata.crossref.org/v1/events?obj-id.prefix=10.14778&mailto=bibliometrie@slub-dresden.de)
- [ISSN Portal LD Service](https://www.issn.org/understanding-the-issn/assignment-rules/issn-linked-data-application-profile/)
  - resource/ISSN
    - [2150-8097](https://portal.issn.org/resource/ISSN/2150-8097?format=json)
  - resource/ISSN-L
    - [2150-8097](https://portal.issn.org/resource/ISSN-L/2150-8097?format=json)
- [JournalsDB API](https://api.journalsdb.org/apidocs/)
  - journals
    - [2150-8097](https://api.journalsdb.org/journals/2150-8097)
- [OpenAlex API](https://docs.openalex.org/api)
  - venues
    - [V4210226185](https://api.openalex.org/journals/V4210226185?mailto=bibliometrie@slub-dresden.de) / [issn:2150-8097](https://api.openalex.org/journals/issn:2150-8097?mailto=bibliometrie@slub-dresden.de)
  - works
    - [filter=host_venue.id:V4210226185](https://api.openalex.org/works?filter=host_venue.id:V4210226185&mailto=bibliometrie@slub-dresden.de)
    - [filter=host_venue.id:V4210226185&group_by=type](https://api.openalex.org/works?filter=host_venue.id:V4210226185&group_by=type&mailto=bibliometrie@slub-dresden.de)
    - [filter=host_venue.id:V4210226185&group_by=publication_year](https://api.openalex.org/works?filter=host_venue.id:V4210226185&group_by=publication_year&mailto=bibliometrie@slub-dresden.de)
- [OpenCitations API](https://opencitations.net/index/coci/api/v1) (COCI)
  - citations
  - citation-count
- [Wikidata](https://www.wikidata.org/wiki/Wikidata:Data_access)
  - Linked Data Interface
    - [Q27722874](https://www.wikidata.org/wiki/Special:EntityData/Q27722874.json)

# Content Access

- VLDB Endowment
  - [PVLDB (Proceedings of the VLDB Endowment)](https://vldb.org/pvldb/)
- ACM DL > Collections > Hosted Content
    - [Proceedings of the VLDB Endowment](https://dl.acm.org/journal/pvldb)
- DBLP > Journals
    - [Proceedings of the VLDB Endowment](https://dblp.org/db/journals/pvldb/)

# Usage Terms

[![Creative Commons License](https://mirrors.creativecommons.org/presskit/buttons/80x15/svg/by.svg)](http://creativecommons.org/licenses/by/4.0/) This [report](#) is licensed under a [Creative Commons Attribution 4.0 International License](./LICENSE.txt).  
[![Public Domain Dedication](https://mirrors.creativecommons.org/presskit/buttons/80x15/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/) The [raw data](#raw-data) is made available under the [CC0 1.0 Universal Public Domain Dedication](./data/LICENSE.txt).
