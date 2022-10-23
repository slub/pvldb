"""
slub/pvldb -- Bibliometric Analysis of PVLDB
Copyright (c) 2022 SLUB Dresden

This file is part of slub/pvldb.

slub/pvldb is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

slub/pvldb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with slub/pvldb. If not, see <https://www.gnu.org/licenses/>.
"""
import os
import tqdm
import logging
from habanero import Crossref
from tqdm.contrib.logging import logging_redirect_tqdm

from .doi import tracker as doi_tracker


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logging.captureWarnings(True)   # due to works(warn=True)
logger = logging.getLogger("src.crossref")


def get_client(mailto=None):
    if mailto is None:
        if "CROSSREF_MAILTO" in os.environ:
            mailto = os.environ["CROSSREF_MAILTO"]
        else:
            logger.warning("Unable to enter Crossref's polite pool!")
    return Crossref(mailto=mailto)


def get_works_from_journal(issn, mailto=None):
    cr = get_client(mailto=mailto)
    works = []
    response = cr.works(filter={"issn": issn},
                        cursor="*", cursor_max=100000, sort="indexed",
                        order="desc", limit=100, progress_bar=True)
    for batch in response:
        if "status" in batch and batch["status"] == "ok":
            for item in batch["message"]["items"]:
                works.append(item)
    return works


def get_works(dois, mailto=None):
    cr = get_client(mailto=mailto)
    works = []
    with logging_redirect_tqdm():
        for doi in tqdm.tqdm(dois):
            response = cr.works(ids=[doi], warn=True)
            if isinstance(response, dict) and "status" in response \
                    and response["status"] == "ok":
                works.append(response["message"])
            elif response is None:
                new_doi = doi_tracker(doi)
                if new_doi is not None:
                    msg = "Change of DOI {0} to new DOI {1} detected!".format(
                        doi, new_doi)
                    logger.info(msg)
                    response = cr.works(ids=[new_doi], warn=True)
                    if isinstance(response, dict) and "status" in response \
                            and response["status"] == "ok":
                        works.append(response["message"])
    return works


def get_dois(works):
    dois = [item["DOI"] for item in works]
    dois = list(set(dois))
    dois.sort()
    return dois


def get_prefixes(works):
    prefixes = [item["prefix"] for item in works]
    prefixes = list(set(prefixes))
    prefixes.sort()
    return prefixes


def get_members(works):
    members = [item["member"] for item in works]
    members = list(set(members))
    members.sort()
    return members


def get_issns(works):
    issns = [issn for item in works if "ISSN" in item for issn in item["ISSN"]]
    issns = list(set(issns))
    issns.sort()
    return issns


def get_dois_of_articles(works):
    dois = [item["DOI"] for item in works if item["type"] == "journal-article"]
    dois.sort()
    return dois


def get_dois_of_issues(works):
    dois = [item["DOI"] for item in works if item["type"] == "journal-issue"]
    dois.sort()
    return dois


def get_dois_from_works_references(works):
    mapping = {}
    for item in works:
        doi = item["DOI"]
        mapping[doi] = []
        if "reference" in item:
            for ref in item["reference"]:
                if "DOI" in ref:
                    mapping[doi].append(ref["DOI"])
        else:
            mapping[doi] = None
    mapping = dict(sorted(mapping.items()))
    return mapping


def get_issns_from_works(works):
    mapping = {}
    for item in works:
        doi = item["DOI"]
        issns = list(set(item["ISSN"])) if "ISSN" in item else None
        mapping[doi] = issns
    mapping = dict(sorted(mapping.items()))
    return mapping


def get_issns_stats(works):
    issns = []
    for item in works:
        if "ISSN" in item:
            issns.extend(list(set(item["ISSN"])))
    stats = {}
    for value in list(set(issns)):
        stats[value] = issns.count(value)
    stats = dict(sorted(stats.items(), key=lambda item: item[1], reverse=True))
    return stats


def get_types_per_year(works):
    mapping = {}
    for item in works:
        year = 1970
        if "published" in item:
            if "date-parts" in item["published"]:
                if len(item["published"]["date-parts"]) > 0:
                    if len(item["published"]["date-parts"][0]) > 0:
                        year = item["published"]["date-parts"][0][0]
        if year > 1970:
            if year in mapping:
                mapping[year].append(item["type"])
            else:
                mapping[year] = [item["type"]]
    for year in mapping.keys():
        mapping[year].sort()
    mapping = dict(sorted(mapping.items()))
    return mapping
