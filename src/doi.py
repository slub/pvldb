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
import requests


def tracker(doi):
    doi_url = "https://doi.org/%s" % doi
    response = requests.get(doi_url, allow_redirects=False)
    if response.status_code == 301 and "Location" in response.headers:
        location = response.headers["Location"]
        if location.startswith("https://doi.org/"):
            return location.replace("https://doi.org/", "")
