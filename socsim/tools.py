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
# name  tools.py
# date: 2013AUG15
# prog: pr
# desc: tools file
# copy: copyright (C) 2013 Peter Renshaw
#===


import sys
import json
import os.path


#---
# get_home_path_os: from os.sys.platform()
#                   find OS name & ret path
# <http://docs.python.org/2/library/sys.html#sys.platform>
# TODO fix paths here
#---
def get_home_path_os(name):
    if name.lower() == 'linux2':
        home = '/home/pr'  # linux
    elif name.lower() == 'win32':
        home = 'e:\\'      # windows
    elif name.lower() == 'darwin':
        home = False
    else:
        home = False       # everything else fails (for the moment)
    return home


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
        print("error: python version not able to support configparser :(")
        print("version: <%s>" % pyhv)
        sys.exit(1)
    return config

#--- tools ---
# some testing
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



# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
