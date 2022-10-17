# Bibliometric Analysis of PVLDB

*Under Construction*

Powered by [actions](https://github.com/slub/pvldb/actions) workflow. See [report](https://slub.github.io/pvldb/) for results. The report files can be found on the [gh-pages](https://github.com/slub/pvldb/tree/gh-pages) branch.

## Development

### Requirements

- Unix-like OS (tested on Ubuntu 20.04)
- Git (tested with version 2.37)
- cURL (tested with version 7.68)
- gzip (tested with version 1.10)
- jq (tested with version 1.6)
- R (tested with version 4.2)
- Python (tested with version 3.10)

### Set up

#### Repository

```sh
git clone git@github.com:slub/pvldb.git
cd pvldb
```

#### Python

```sh
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

#### R

```sh
Rscript renv/activate.R
Rscript -e "renv::restore()"
```

#### Environment

```sh
export CROSSREF_MAILTO="humans@institution.org"
export OPENALEX_MAILTO="humans@institution.org"
export OPENCITATIONS_ACCESS_TOKEN="YOUR_OC_ACCESS_TOKEN"
```

For further details, see the documentation of the [Crossref polite pool](https://github.com/CrossRef/rest-api-doc#good-manners--more-reliable-service), the [OpenAlex polite pool](https://docs.openalex.org/api#the-polite-pool) and the [OpenCitations access token](https://opencitations.net/accesstoken).

### Retrieve data

```sh
utils/crossref
utils/crossrefgz
utils/urlrequest
```

### Create report

```sh
utils/data2public
utils/render
utils/license
```

### Browse results

```sh
cd public
python3 -m http.server
```

Go to http://127.0.0.1:8000 ...

## Meta

- License: [GPL3](./LICENSE)
- Copyright Holder: [SLUB Dresden](https://www.slub-dresden.de)
- Author + Maintainer: [Donatus Herre](https://orcid.org/0000-0003-4335-2535)
- Bug Tracker: [GitHub](https://github.com/slub/pvldb/issues)
- Contact: [bibliometrie@slub-dresden.de](mailto:bibliometrie@slub-dresden.de)
