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
#
# use: python hack_blocks.py -t "Testing" 
#                            -d "A test after I've changed the source tree" 
#                            -s $HOME/block.json
#
# copy: copyright (C) 2013 Peter Renshaw
#===


import sys
from optparse import OptionParser


import socsim.record


def main():
    usage = "usage: %prog [v] -t -d"
    parser = OptionParser(usage)
    parser.add_option("-t", "--title", dest="title", 
                      help="metadata title information")
    parser.add_option("-d", "--description", dest="description", 
                      help="metadata description information")
    parser.add_option("-s", "--save", dest="save", 
                      help="convert to json, save to file")
    parser.add_option("-v", "--version", dest="version", \
                      action="store_true",
                      help="current version")    
    options, args = parser.parse_args()


    if options.version:
        print("%s v%s %s %s" % ('blocks', '0.0.1', '2013AUG09', '(C) 2013'))
        sys.exit(0)
    elif options.title and options.description:
        mvp = socsim.record.Meta('Victorian Police', 'Information related to Victorian Police')
        mvp.add('phone','000')
        mvp.add('web', 'http://vicpolice.gov.au/')
        mvp.add('contact', 'title, firstname, lastname')

        mcfa = socsim.record.Meta("Country Fire Authority", "Information related to CFA")
        mcfa.add('phone','000')
        mcfa.add('www', 'http://cfa.vic.gov.au')
        mcfa.add('contact', 'title, lastname, firtname')

        md = socsim.record.Meta("Emergency services", "List of emergencey services information")

        me = socsim.record.Record(md.all())
        me.add('vicpolice', mvp.all())
        me.add('cfa', mcfa.all())

        if options.save: 
            json = socsim.record.py2json(me.all())
            if socsim.record.save(options.save, json):
                print("save %s" % options.save)
            else:
                print("error saving %s" % options.save)
                sys.exit(1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
