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
# name: record.py
# date: 2013AUG09
# prog: pr
# desc: tools to build, manipulate python data
#       convert data to json, save
#       read, convert json to python
# copy: copyright (C) 2013 Peter Renshaw
#===


import json
import time
import os.path


#--- tools ---
# TODO not tested
#
def save(filepathname, data):
    """save a file to filesystem"""
    filepath = os.path.dirname(filepathname)
    filename = os.path.basename(filepathname)
    if data:
        if filename:
            if os.path.isdir(filepath):
                with open(filepathname, 'w') as f:
                    f.write(data)
                return True
    return False
def load(filepathname):
    """load a file"""
    if filepathname: 
        if os.path.isfile(filepathname):
            data = ""
            with open(filepathname, 'r') as f:
                data = f.read()
            f.close()
            return data
    return False
def convert(data, to_json=True):
    """conversion from py<==>json"""
    if data:
        if to_json:
            return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            return json.loads(data)
    return False
def json2py(data):
    """convert json data to python structure"""
    return convert(data, to_json=False)
def py2json(data):
    """convert python structure to json"""
    return convert(data)
#--- tools ---


#---
# name: Meta
# date: 2013AUG09
# prog: pr
# desc: creates expandable metadata description
#---
class Meta:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.store = []
        self.__add_default()
    def new(self, title, description):
        if title != "" and description != "": 
            self.store = []
            self.title = title
            self.description = description
            self.__add_default()
            return True
        else:
            return False
    def search(self, key):
        """search for (key) name in store, found is T, non, F"""
        if key:
            for item in self.store:
                if item['key'] == key: 
                    return True
        return False
    def add(self, name, value):
        """convenience method for private ___add_data"""
        n = name.replace(' ','-') # do not allow spaces in key
        return self.__add_data(dict(key=n, value=value))
    def __add_data(self, data):
        """
        add a new meta name and value pair
        no dupes allowed,
        unique key names enforced
        """
        if 'key' in data.keys():
            if not self.search(data['key']):
                self.store.append(data)
                return True
        return False
    def __add_default(self):
        """private, adds all metadata to store"""
        self.add('title', self.title)
        self.add('description', self.description)
        # uppercase, want Aug as AUG
        self.add('created', time.strftime("%Y%b%d%H%M.%S").upper())
    def all(self):
        """if something in store, return else False"""
        if self.store:
            return self.store
        else:
            return False


#---
# name: Record
# date: 2013AUG09
# prog: pr
# desc: creates expandable record of key/value pairs with metadata
#---
class Record:
    def __init__(self, meta):
        """init the object, meta contains metadata"""
        self.store = []
        self.name = ""
        self.value = ""
        self.removed = False # future removal flag
        self.__add_bulk_data(meta)
    def new(self, meta):
        """clear obj, add new meta"""
        self.store = []
        self.name = ""
        self.value = ""
        return self.__add_bulk_data(meta)
    # --- add ---
    def add(self, name, value):
        """add a single name/value pair"""
        if name and value:
            n = name.replace(' ','-')  # do not allow spaces in key
            # key as unique name, value as data, deleted flag for removal
            return self.__add_data(dict(key=n, value=value,
                                        deleted=self.removed))
        else:
            return False
    def __add_bulk_data(self, data):
        """data input as list of key/values"""
        if data:
            for d in data:
                if not self.__add_data(d):
                    return False
            return True
        return False
    def __add_data(self, data):
        """add data to store, no duplicate keys"""
        if 'key' and 'value' in data.keys():
            if not self.search(data['key']):
                self.store.append(data)
                return True
        return False
    # --- search ---
    # TODO not tested
    #
    def __search_all(self, key, get_index=False, get_item=False):
        """find if key in store[name], T/F, opt return index or item"""
        if key:
            count = 0
            for item in self.store:
                if item['key'] == key:
                    if get_item: # return {'key':'foo','value':'bar'}
                       return item
                    elif get_index:
                       return count # return index of item
                    else: 
                       return True
                count += 1
        return False
    def search(self, key):
        """convenience method to find key in store, T/F"""
        return self.__search_all(key)
    def search_item(self, key):
        """search by key on key/value pair ret {'key':'foo','value':'bar'}"""
        return self.__search_all(key, get_index=False, get_item=True)
    def search_value(self, key):
        """search by key, ret value, else F"""
        item = self.search_item(key)
        if item: return item['value']
        else: return False
    def search_index(self, key):
        """search by key, return count index or F"""
        return self.__search_all(key, get_index=True, get_item=False)
    # --- get ---
    def all(self):
        """return all in store as py stucture"""
        if self.store:
            return self.store
        else:
            return False


def main():
    pass

if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
