---
title: "PVLDB"
subtitle: "Bibliometric Analysis"
pagetitle: "PVLDB :: Bibliometric Analysis"
date: "2022-10-08"
lang: "en-US"
output:
  html_document:
    mathjax: null
    includes:
      after_body: assets/html/target.html
    keep_md: true
---





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
    - [dois](./data/crossref_works_filter-issn-2150-8097_dois.json) [JSON, 103.08 KB]
    - [reference-dois](./data/crossref_works_filter-issn-2150-8097_reference-dois.json) [JSON, 2.01 MB]
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
