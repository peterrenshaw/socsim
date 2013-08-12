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


import sys

# --- HACK ALERT --- 
# hex_version: which version of py are we using?
def hex_version():
    """python version in hex"""
    return '%x' % sys.hexversion
if hex_version() < '30203f0':
    # py 2
    import ConfigParser
    config = ConfigParser.ConfigParser()
else:
    # py 3
    import configparser
    config = configparser.ConfigParser()
# ---


import record


#---
# name: Delivery
# date: 2013AUG12
# prog: pr
# desc: imports data in various ways & prepares for factory
#---
class Delivery:
    def __init__(self, pyversion, filepathname=""):
        """prepare delivery"""
        self.filepathname = filepathname
        self.pyver = pyversion
        self.store = []
        
    # TODO fix this for exact hex
    def is_py3(self):
        """borked: check exact hex version"""
        return self.pyver >= '30000f0'
    def is_py2(self):
        """borked: find the exact hex version"""
        return self.pyver < '30000f0' and self.pyver >= '20703c2'
    # --- ini file
    def ini(self, config, filepathname=""):
        """input ini config obj to parse"""
        # need a valid filename to load
        if filepathname:
            if os.path.isfile(filepathname):
                self.filepathname = filepathname
            else:
                return False
        if not self.filepathname:
            return False

        # read ini, break down
        data = []
        config.read(self.filepathname)
        sections = config.sections()

        # look thru sections, extract
        for atitle in sections:
            d = dict(title=atitle)

            # check python version
            if self.__is_py3():
                for akey in config.items(title):
                    d = d + dict(key=akey, value=config[title][key])
                data.append(d)
            elif self.__is_py2():
                for akey in config[atitle]:
                    d = d + dict(key=akey, value=config[atitle][akey])
                data.append(d)
            else:
                # problem, die
                return False
        # update the store
        self.store.append(data)
        return True
    def all(self):
        """return all data in store, or F"""
        if len(self.store) > 0:
             return self.data
        else:
             return False



def main():
    pass


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
