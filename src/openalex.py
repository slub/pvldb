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
from diophila import OpenAlex


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("src.openalex")


def oa_venue(issn, mailto=None):
    if mailto is None:
        if "OPENALEX_MAILTO" in os.environ:
            mailto = os.environ["OPENALEX_MAILTO"]
        else:
            logger.warning("Unable to enter OpenAlex's polite pool!")
    openalex = OpenAlex(email=mailto)
    try:
        return openalex.get_single_venue(issn, id_type="issn")
    except Exception as e:
        logger.error("Request of venue with ISSN %s from OpenAlex failed!" % issn)
        logger.error("Exception of type %s was thrown." % e.__class__.__name__)


def oa_venue_title(issn, mailto=None):
    venue = oa_venue(issn, mailto=mailto)
    if isinstance(venue, dict):
        vid = venue["id"] if "id" in venue else ""
        issnl = venue["issn_l"] if "issn_l" in venue else ""
        dname = venue["display_name"] if "display_name" in venue else ""
        return vid, dname, issnl


def oa_venue_enrichment(issn_stats, mailto=None):
    result = []
    tracker = {}
    for k in tqdm.tqdm(issn_stats):
        venue = oa_venue_title(k, mailto=mailto)
        if isinstance(venue, tuple):
            if venue[0] in tracker:
                if issn_stats[k] <= issn_stats[tracker[venue[0]]]:
                    continue
            tracker[venue[0]] = k
            row = [venue[0], venue[1], venue[2], issn_stats[k]]
            result.append(row)
        else:
            result.append(["", "", k, issn_stats[k]])
    result.sort(key=lambda x: x[3], reverse=True)
    result.insert(0, ["id", "display_name", "issn_l", "count"])
    return result
