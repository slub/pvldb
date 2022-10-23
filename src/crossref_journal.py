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
import logging
from datetime import timedelta
from timeit import default_timer as timer

from . import crossref, openalex, opencitations, utils


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logging.captureWarnings(True)   # due to works(warn=True)
logger = logging.getLogger("src.crossref_journal")


def outpath(issn, pattern):
    return "data/crossref_works_filter-issn-{0}{1}.json".format(issn, pattern)


def outpath_csv(issn, pattern):
    return "data/crossref_works_filter-issn-{0}{1}.csv".format(issn, pattern)


def main(issn):
    start = timer()
    doi_list, reference_doi_list = works_main(issn, return_dois=True)
    citation_main(issn, doi_list=doi_list)
    reference_main(issn, doi_list=reference_doi_list)
    end = timer()
    logger.info("All done!")
    logger.info("Took {0} (h:m:s)".format(timedelta(seconds=end - start)))


def works_main(issn, return_dois=False):
    logger.info("Fetch works of journal with ISSN %s!" % issn)
    works = crossref.get_works_from_journal(issn)
    if not os.path.exists("data"):
        os.makedirs("data")
    utils.store_json(works, outpath(issn, "_works"))
    year_types = crossref.get_types_per_year(works)
    utils.store_json_pretty(year_types, outpath(issn, "_year-types"))
    issn_list = crossref.get_issns(works)
    utils.store_json_pretty(issn_list, outpath(issn, "_issns"))
    prefix_list = crossref.get_prefixes(works)
    utils.store_json_pretty(prefix_list, outpath(issn, "_prefixes"))
    member_list = crossref.get_members(works)
    utils.store_json_pretty(member_list, outpath(issn, "_members"))
    doi_list = crossref.get_dois(works)
    utils.store_json_pretty(doi_list, outpath(issn, "_dois"))
    issue_doi_list = crossref.get_dois_of_issues(works)
    utils.store_json_pretty(issue_doi_list, outpath(issn, "_dois-issue"))
    article_doi_list = crossref.get_dois_of_articles(works)
    utils.store_json_pretty(article_doi_list, outpath(issn, "_dois-article"))
    reference_dois = crossref.get_dois_from_works_references(works)
    utils.store_json_pretty(reference_dois, outpath(issn, "_reference"))
    reference_count = {doi: len(reference_dois[doi] or [])
                       for doi in reference_dois}
    reference_count = dict(sorted(reference_count.items(),
                                  key=lambda item: item[1], reverse=True))
    utils.store_json_pretty(reference_count, outpath(issn, "_count-reference"))
    reference_doi_list = list(set([ref_doi for doi in reference_dois
                                   for ref_doi in reference_dois[doi] or []]))
    reference_doi_list.sort()
    utils.store_json_pretty(reference_doi_list, outpath(issn, "_dois-reference"))
    if return_dois:
        return doi_list, reference_doi_list


def reference_main(issn, doi_list=None):
    if doi_list is None:
        doi_list = utils.read_json(outpath(issn, "_dois-reference"))
        if doi_list is None:
            return
    logger.info("Fetch works cited in works of journal with ISSN %s!" % issn)
    reference_works = crossref.get_works(doi_list)
    utils.store_json(reference_works, outpath(issn, "_works-reference"))
    reference_issns = crossref.get_issns_from_works(reference_works)
    utils.store_json_pretty(reference_issns, outpath(issn, "_works-reference_issns"))
    reference_issn_stats = crossref.get_issns_stats(reference_works)
    utils.store_json_pretty(reference_issn_stats,
                            outpath(issn, "_count-issns-reference"))
    logger.info("Fetch venues cited in works of journal with ISSN %s!" % issn)
    reference_issn_stats_enriched = openalex.oa_venue_enrichment(reference_issn_stats)
    utils.store_csv(reference_issn_stats_enriched, outpath_csv(issn, "_count-issns-reference"))
    reference_issn_list = crossref.get_issns(reference_works)
    utils.store_json_pretty(reference_issn_list, outpath(issn, "_issns-reference"))
    reference_year_types = crossref.get_types_per_year(reference_works)
    utils.store_json_pretty(reference_year_types,
                            outpath(issn, "_year-types-reference"))


def citation_main(issn, doi_list=None):
    if doi_list is None:
        doi_list = utils.read_json(outpath(issn, "_dois"))
        if doi_list is None:
            return
    citation_dois = opencitations.fetch_citations(doi_list)
    utils.store_json_pretty(citation_dois, outpath(issn, "_citation"))
    citation_count = {doi: len(citation_dois[doi] or [])
                      for doi in citation_dois}
    citation_count = dict(sorted(citation_count.items(),
                                 key=lambda item: item[1], reverse=True))
    utils.store_json_pretty(citation_count, outpath(issn, "_count-citation"))
    citation_doi_list = list(set([cit_doi for doi in citation_dois
                                  for cit_doi in citation_dois[doi] or []]))
    citation_doi_list.sort()
    utils.store_json_pretty(citation_doi_list, outpath(issn, "_dois-citation"))
    logger.info("Fetch works citing works of journal with ISSN %s!" % issn)
    citation_works = crossref.get_works(citation_doi_list)
    utils.store_json(citation_works, outpath(issn, "_works-citation"))
    citation_issns = crossref.get_issns_from_works(citation_works)
    utils.store_json_pretty(citation_issns, outpath(issn, "_works-citation_issns"))
    citation_issn_stats = crossref.get_issns_stats(citation_works)
    utils.store_json_pretty(citation_issn_stats,
                            outpath(issn, "_count-issns-citation"))
    logger.info("Fetch venues citing works of journal with ISSN %s!" % issn)
    citation_issn_stats_enriched = openalex.oa_venue_enrichment(citation_issn_stats)
    utils.store_csv(citation_issn_stats_enriched, outpath_csv(issn, "_count-issns-citation"))
    citation_issn_list = crossref.get_issns(citation_works)
    utils.store_json_pretty(citation_issn_list, outpath(issn, "_issns-citation"))
    citation_year_types = crossref.get_types_per_year(citation_works)
    utils.store_json_pretty(citation_year_types,
                            outpath(issn, "_year-types-citation"))
