#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
from .crossref_journal import reference_main


def main():
    reference_main("2150-8097")


if __name__ == '__main__':
    main()
