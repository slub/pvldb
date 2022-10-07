# Bibliometric Analysis of PVLDB

See [build](https://herreio.github.io/pvldb/) for results.

## Development

### Requirements

- \*nix OS
- R (tested with Version 4.2)
- Python (tested with Version 3.10)

### Set up

```sh
Rscript renv/activate.R
Rscript -e "renv::restore()"
```

### Create build

```sh
utils/crossref
utils/render
```
