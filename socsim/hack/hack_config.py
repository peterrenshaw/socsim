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
# name  hack_config.py
# date: 2013AUG10
# prog: pr
# desc: input data from sources, process it
#       output the raw data
#       first hack
#
# use:  python hack_config.py -s urls.ini
#
# todo: build meta and record blocks
# copy: copyright (C) 2013 Peter Renshaw
#===


import sys
from optparse import OptionParser


import socsim.tools


# find index from section name in sections
def search_by_name(name, sections):
    count = 0
    for section in sections:
        if name == section:
            return count
        count = count + 1
    return False

def d_all(sections, config):
    if sections: # look thru sections, extract title, per title key & value
        for title in sections:
            print("title = '%s'" % title)
            for key in config.items(title):
                print("\tkey='%s'\tvalue='%s'" % (key[0], key[1]))
        return True
    return False 

# --- cli interface
def main():
    """cli entry point"""
    usage = "usage: %prog [-h] -s"
    parser = OptionParser(usage)
    parser.add_option("-s", "--source", dest="source", 
                      help="read source '.ini' file")
    parser.add_option("-v", "--version", dest="version", \
                      action="store_true",
                      help="current version")    
    options, args = parser.parse_args()

    if options.version:
        print("%s %s %s %s" % ("hack_config", 
                               "0.0.1", 
                               "2013", 
                               "(C) Copyright Peter Renshaw"))
        sys.exit(0)
    if options.source:
        print("source <%s>" % options.source)

        # ---
        # ATTENTION:
        # need this to import dynamically, depending on python version
        pyversion = socsim.tools.hex_version()
        config = socsim.tools.hack_import_configparser(pyversion)
        # ---
        
        # lets rock
        try:
            config.read(options.source)    # TODO handling here for bad input
            sections = config.sections()
        except:
            print("error: problem with <%s>" % config)
            print("\tfile = <%s>" % options.source)
            sys.exit(1)

        d_all(sections, config)

    else:
        parser.print_help()  

if __name__ == "__main__":
    main()
