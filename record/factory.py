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
# name  factory.py
# date: 2013AUG12
# prog: pr
# desc: here we marshall the data input data, 
#       then build meta blocks and wrap in record container,
#       export to meta & record.
# copy: copyright (C) 2013 Peter Renshaw
#===

import os
import sys


# --- HACK ALERT --- 
# hex_version: which version of py are we using?
def hex_version():
    """python version in hex"""
    return '%x' % sys.hexversion

# hack_import_configparser: difference called in Py2 to Py3
def hack_import_configparser(pyhv):
    """
    In version 2 upwards in python 'import ConfigParser' is used.
    In version 3 onwards, 'import configparser' is used. Sux!!!
    """
    if pyhv >= "30000f0":     # py3
        import configparser   # look at this *carefully*
        config = configparser.ConfigParser()
    elif pyhv > "20000f0":    # py2 
        import ConfigParser   # look at this *carefully*
        config = ConfigParser.ConfigParser()
    else: 
        # less than py2
        print("error: python version not able to support this code")
        print("version: <%s>" % pyhv)
        sys.exit(1)
    return config

# ATTENTION:
# need this to import dynamically depending on python version
pyhv = hex_version()
hack_import_configparser(pyhv)
# ---


import record


#---
# name: Ini
# date: 2013AUG12
# prog: pr
# desc: imports data in various ways & prepares for factory
#---
class Ini:
    def __init__(self, pyversion):
        """prepare delivery"""
        self.filepathname = ""
        self.pyver = pyversion
        self.store = []
    # --- ini file
    def read(self, config, filepathname):
        """input ini config obj to parse"""
        # need a valid filename to load
        self.filepathname = filepathname
        if self.filepathname:
            if not os.path.isfile(self.filepathname):
                #print("error: no valid filepathname <%s>" % self.filepathname)
                #sys.exit(1)
                return False
        else:
            #print("error: no filepathname found <%s>" % self.filepathname)
            #sys.exit(1)
            return False

        # setup, read ini, break down
        self.store = []
        t = []
        config.read(self.filepathname)
        sections = config.sections()

        # look thru sections, extract title, per title key & value
        for title in sections:
            t.append(dict(title=title))
            for key in config.items(title):
                t.append(dict(key=key[0], value=key[1]))
            self.store.append(t)
            t = []
        return True
    def all(self):
        """return all data in store, or F"""
        if len(self.store) > 0:
             return self.store
        else:
             return False


def main():
    pass


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
