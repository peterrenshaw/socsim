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
# name  hack_read_ini.py
# date: 2013AUG10
# prog: pr
# desc: input data from sources, process it
#       output the raw data
#     
#       NO TESTING YET
#
# todo: build meta and record blocks
# copy: copyright (C) 2013 Peter Renshaw
#===


import sys
import os.path
from optparse import OptionParser


# --- HACK ALERT ---
# * get python version in hex
# - python:  20703c2
# - python3: 30203f0
def hex_version():
    """python version in hex"""
    return '%x' % sys.hexversion

# --- HACK ALERT ---
# code changes in python3 for configparser
# <http://docs.python.org/2/library/configparser.html#module-ConfigParser>
#
if hex_version() < '30203f0':
    # py 2
    import ConfigParser
    config = ConfigParser.ConfigParser()
else:
    # py 3
    import configparser
    config = configparser.ConfigParser()


import record


# display all raw data
def display_all(sections, conf, version):
    """display all sections and key,value pair per section"""
    count = 0
    for title in sections:
        print("%s %s" % (count, title)) # title == sections[count]

        # --- HACK ALERT ---
        # works in py vers < 3
        if version < '30203f0':
            for key in conf.items(title):
                print("\t%s=%s" % (key[0], key[1]))
        else:
        # works in py ver >= 3 
            for key in conf[title]:
                print("\t%s=%s" % (key, conf[title][key]))
        count += 1


# --- cli interface
def main():
    """cli entry point"""
    usage = "usage: %prog [v] -s"
    parser = OptionParser(usage)
    parser.add_option("-s", "--source", dest="source", 
                      help="source directory of file")
    parser.add_option("-v", "--version", dest="version", \
                      action="store_true",
                      help="current version")    
    options, args = parser.parse_args()

    if options.version:
        print("%s v%s %s %s" % ('hack_read_ini', '0.0.1', '2013AUG11', '(C) 2013'))
        sys.exit(0)
    elif options.source:
        if os.path.isfile(options.source):
            #config = configparser.ConfigParser()
            config.read(options.source)
            sections = config.sections()

            display_all(sections, config, hex_version())
        else:
            print("error: problem with the filepath")
            print("\t<%s>" % options.source)
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
