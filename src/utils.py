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
import csv
import json


def store_csv(obj, path):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(obj)


def store_json(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f)


def store_json_pretty(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)


def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
