# Bibliometric Analysis of PVLDB

Powered by [actions](https://github.com/herreio/pvldb/actions) workflow. See [build](https://herreio.github.io/pvldb/) for results. The build files can be found on the [gh-pages](https://github.com/herreio/pvldb/tree/gh-pages) branch.

## Development

### Requirements

- Unix-like OS
- R (tested with Version 4.2)
- Python (tested with Version 3.10)

### Set up

#### Repository

```sh
git clone git@github.com:herreio/pvldb.git
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

### Create build

```sh
utils/crossref
utils/render
```
