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
# name  socsim.py
# date: 2013AUG15
# prog: pr
# desc: place holder file
# copy: copyright (C) 2013 Peter Renshaw
#===


from optparse import OptionParser


# --- cli interface
def main():
    """cli entry point"""
    usage = "usage: %prog [-h] -s"
    parser = OptionParser(usage)
    parser.add_option("-v", "--version", dest="version", \
                      action="store_true",
                      help="current version")    
    options, args = parser.parse_args()

    if options.version:
        print("%s %s %s %s" % ("socsim", 
                               "0.0.1", 
                               "2013", 
                               "(C) Copyright Peter Renshaw"))
        sys.exit(0)
    else:
        parser.print_help()  


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
