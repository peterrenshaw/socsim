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
import collections


#import socsim.tools


# ATTENTION:
# need this to import dynamically, depending on python version
#pyhv = socsim.tools.hex_version()
#socsim.tools.hack_import_configparser(pyhv)
# ---


#---
# name: Ini
# date: 2013AUG12
# prog: pr
# desc: imports data in various ways & prepares for factory
# note:
#       * extracting Ini titles have to be added as something like
#         
#         ini.Title    --->    Key = 'TITLE', value = ini.Title
#           
#         This helps later on in factory.Factory.build() where you have
#         to translate python data structure with KEY/VALUE pairs. If you 
#         use this consistantly, search is seamless and translation to 
#         record.Meta and insertion into record.Record via record.Record.add
#         runs smoothly.
#---
class Ini:
    def __init__(self, py_version):
        """prepare delivery"""
        self.filepathname = ""
        self.pyver = py_version
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
        try:
            config.read(self.filepathname)    # TODO handling here for bad input
            sections = config.sections()
        except:
            #print("error: we have an error <%s>" % config)
            #print("\tfile = <%s>" % self.filepathname)
            #sys.exit(1)
            return False
        if sections: # look thru sections, extract title, per title key & value
            for title in sections:
                t.append(dict(key='title', value=title))       # IMPORTANT see note (*)
                for key in config.items(title):
                    t.append(dict(key=key[0], value=key[1]))
                self.store.append(t)
                t = []
            return True
        else:
            # print("error: no sections found in <%s>" % (self.filepathname))
            # sys.exit(1)
            return False
    def all(self):
        """return all data in store, or F"""
        if len(self.store) > 0:
             return self.store
        else:
             return False

#---
# name: Factory
# date: 2013AUG13
# prog: pr
# desc: from py objects, convert this data into record.Meta
#       and add them to record.Record as a container. Depending
#       on status, build & spit out the results at all() call.
#       Able to obtain statitic breakdown of objects.
#---
class Factory:
    def __init__(self, data, meta, record):
        """initialise, read to start"""
        self.data = data
        self.store = []
        self.__status = False
        self.__meta = meta
        self.__record = record
    def status(self):
        """current status of build"""
        return self.__status
    def __data_check(self, data):
        """check data for problems"""
        if data:                                            # data found?
            if len(data) > 0:                               # len > 0?
                if isinstance(data, collections.Iterable):  # itterable?
                    self.data = data
                    return True
        return False
    def __get_all_byname(self, data, key):
        """generalised search for key/value pairs in list"""
        for item in data:
            if item['key'] == key:
                return item
        return False
    def __get_value_byname(self, data, key):
        """
        convenience function for __get_all_byname,
        return 'value' of result
        """
        data = self.__get_all_byname(data, key)
        if data:
            return data['value']
        else:
            return False
    def build(self, data=""):
        """
        itterate thru data and build record.Meta, update
        stats, record.Record.add()
        """
        if data: 
            self.data = data
        if not self.__data_check(self.data):
            return False

        for data in self.data:
            title = self.__get_value_byname(data, 'title')
            description = self.__get_value_byname(data, 'description')
            self.__meta.new(title, description)

            for item in data:
                if 'key' in item and 'value' in item:
                    self.__meta.add(item['key'], item['value'])
                    
            self.__record.add(title, self.__meta.all())
        self.__status = True
        return True
    def all(self):
        """return built container record.Record"""
        return self.__record.all()


def main():
    pass

if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
