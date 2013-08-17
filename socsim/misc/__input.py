#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~

"""
    This file is part of SOCSIM.

    SOCSIM is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    SOCSIM is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with SOCSIM.  If not, see <http://www.gnu.org/licenses/>.
"""

#===
# name  input.py
# date: 2013AUG10
# prog: pr
# desc: input data from ini, export to meta & record
# copy: copyright (C) 2013 Peter Renshaw
#===


import configparser


import record


# ---
# read file
# generate data
# build meta
# 
# build temp record of meta
# save to file
# ---

# * extact
# - sections
# - key, values

# * organise 
# - meta
# - others

class ini:
    def __init__(self, data, config):
        self.data = data
        self.store = []
        self.c = config
    def extract(self):
        """extract info from ini data"""
        if data:
            self.c.read_string(self.data)
            return True
        return False
    def build(self):
        """build up store"""
        if self.meta():
           if self.sections():
               return True
        return False
    def meta(self):
        """parse meta section"""
        if 'meta' in self.c['section']:
            meta = self.c['section']['meta']
            self.__add(meta)
            return True
        return False
    def section(self, name):
        """parse info section by name"""
        print(name)
   def  sections(self):
        """extract all sections"""
        for section in self.c.sections():
            self.section(section)
    def all(self):
        """return all sections in store"""
        return self.store


def main():
    pass


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
