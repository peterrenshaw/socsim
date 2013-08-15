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


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
