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
# name  hack_read_ini2json.py
# date: 2013AUG15
# prog: pr
# desc: end to end hack. basis of this file is found in test_factory.py
#
#       make/read ini file
#       use factory.Ini to read & decode file
#       instanciate a record.Record object
#       instanciate a record.Meta object, populate with data
#       use factory.Factory add record.Meta blocks to record.Record
#       export to string/file
#       write out as JSON
#
# use:  python hack_ini2json.py -s urls.ini -d $PATH/code/socsom/record/urls.json
#
# copy: copyright (C) 2013 Peter Renshaw
#===


import sys
import os.path
from optparse import OptionParser


import record
import factory


# --- cli interface
def main():
    """cli entry point"""
    usage = "usage: %prog [-h] -s"
    parser = OptionParser(usage)
    parser.add_option("-s", "--source", dest="source", 
                      help="read source '.ini' file")
    parser.add_option("-d", "--destination", dest="destination",
                      help="save destination filename path")
    parser.add_option("-v", "--version", dest="version", \
                      action="store_true",
                      help="current version")    
    options, args = parser.parse_args()

    if options.version:
        print("%s %s %s %s" % ("hack_ini2json", 
                               "0.0.1", 
                               "2013", 
                               "(C) Copyright Peter Renshaw"))
        sys.exit(0)
    if options.source:
        print("source <%s>" % options.source)
        if options.destination:
            print("destination <%s>" % options.destination)

            # lets rock
            pyversion = factory.hex_version()
            config = factory.hack_import_configparser(pyversion)
            ini = factory.Ini(pyversion)
            if not ini.read(config, options.source):
                print("error: factory.Ini has a problem <%s>" % ini_data)

            # extract Ini data
            ini_data = ini.all()
            if not ini_data:
                print("error: could not extract factory.Ini \
                      from <%s>" % options.source)
                sys.exit(1)

            # describe meta block
            meta_description = record.Meta('Ini2JSON',
                                           'Ini end to end testing. Ini data to JSON')

            # build container, add to factory and build then extact results
            c = record.Record(meta_description.all())
            f = factory.Factory(ini_data, meta_description, c)
            if not f.build():
                print("error: problem building factory.build")
                sys.exit(1)

            # extract data from factory
            data = f.all()
            if not data:
                print("error: problem extracting data from Factory.all")
                sys.exit(1)

            # convert python to JSON & save
            json = record.py2json(data)
            if record.save(options.destination, json):
                print("saved <%s>" % options.destination)
            else:
                print("error saving <%s>" % options.destination)
        else:
            print("error: you must supply a destination filepath")
            if options.destination:
                print("<%s>" % options.destination)
            sys.exit(1)
    else:
        parser.print_help()  


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
