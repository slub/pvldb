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
import time
import tqdm
import logging
import requests


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("src.opencitations")


def citations_url(doi):
    return "https://w3id.org/oc/index/coci/api/v1/citations/%s" % doi


def citations_count_url(doi):
    return "https://w3id.org/oc/index/coci/api/v1/citation-count/%s" % doi


def oc_request(url, repeat=0):
    headers = None
    if "OPENCITATIONS_ACCESS_TOKEN" in os.environ:
        headers = {"Authorization": os.environ["OPENCITATIONS_ACCESS_TOKEN"]}
    else:
        logger.warning("Unable to find access token for OpenCitations!")
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        logger.error("Request to URL %s failed!" % url)
        logger.error("Exception of type %s was thrown." % e.__class__.__name__)
        if repeat < 3:
            repeat += 1
            time.sleep(1.1)
            return oc_request(url, repeat=repeat)
        return None
    if response.status_code == 200:
        return response.json()
    else:
        logger.error("Request to URL %s failed!" % url)
        logger.error("HTTP status code was %s." % response.status_code)
        if repeat < 3:
            repeat += 1
            time.sleep(1.1)
            return oc_request(url, repeat=repeat)
        return None


def citations_request(doi):
    url = citations_url(doi)
    return oc_request(url)


def citations_count_request(doi):
    url = citations_count_url(doi)
    response = oc_request(url)
    if isinstance(response, list) and len(response) > 0:
        if isinstance(response[0], dict) and "count" in response[0]:
            return int(response[0]["count"])


def fetch_citations(dois):
    mapping = {}
    for doi in tqdm.tqdm(dois):
        citations = citations_request(doi)
        if isinstance(citations, list):
            mapping[doi] = []
            for citation in citations:
                if isinstance(citation, dict) and "citing" in citation and citation["citing"]:
                    mapping[doi].append(citation["citing"])
        else:
            mapping[doi] = None
        time.sleep(0.55)
    for doi in mapping.keys():
        if isinstance(mapping[doi], list):
            mapping[doi].sort()
    mapping = dict(sorted(mapping.items()))
    return mapping


def fetch_citations_count(dois):
    mapping = {}
    for doi in tqdm.tqdm(dois):
        citation_count = citations_count_request(doi)
        if isinstance(citation_count, int):
            mapping[doi] = citation_count
        else:
            mapping[doi] = 0
        time.sleep(0.55)
    mapping = dict(sorted(mapping.items()))
    return mapping
