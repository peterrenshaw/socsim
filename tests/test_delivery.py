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

#---
# copy: copyright (C) 2013 Peter Renshaw
#---


import os
import json
import os.path
import unittest


import socsim.tools
import socsim.factory


# get_home_path_os: from os.sys.platform()
#                   find OS name & ret path
# <http://docs.python.org/2/library/sys.html#sys.platform>
# TODO fix paths here
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


class TestIni(unittest.TestCase):
    def setUp(self):
        # os independent home dir
        self.osname = os.sys.platform
        self.home = get_home_path_os(self.osname)
        self.filepathname_fail = os.path.join(self.home,'code','socsim','record','empty.ini')
        self.filepathname = os.path.join(self.home,'code','socsim','record','urls.ini')

        # python versions
        self.pyhv = socsim.tools.hex_version()
        self.pyhv3 = "30000f0"
        self.pyhv2 = "20000f0"

        # TODO fix hard coded paths
        self.c = socsim.tools.hack_import_configparser(self.pyhv)
        self.i = socsim.factory.Ini(self.pyhv)
    def tearDown(self):
        self.i = None
        self.c = None
        self.pyhv = None
        self.filepathname = None
        self.filepathname_fail = None
        self.home = None

    # python versions
    def test_py_version3_ok(self):
        """is current python version 3? return T"""
        if self.pyhv >= self.pyhv3:
            self.assertTrue(self.i.is_py3())
        else:
            self.assertFalse(self.i.is_py3())
    def test_py_version2_ok(self):
        """is current python version 2? return T"""
        if (self.pyhv > self.pyhv2) and (self.pyhv < self.pyhv3):
            # pyv2
            self.assertTrue(self.i.is_py2())
        elif (self.pyhv >= self.pyhv3):
            # pyv3
            self.assertFalse(self.i.is_py2())
        else:
            # pyv < 2
            self.assertFalse(self.i.is_py2())
    # ini files
    def test_ini_ok(self):
        """default ini, T"""
        status = self.i.read(self.c, self.filepathname)
        self.assertTrue(status)
    def test_ini_fail(self):
        """default F with no filenamepath set"""
        status = self.i.read(self.c, "")
        self.assertFalse(status)
    # all
    def test_ini_all_ok(self):
        """are we getting something back?"""
        self.i.read(self.c, self.filepathname)
        data = self.i.all()
        self.assertTrue(data)
    def test_ini_all_fail(self):
        """no data in file, F"""
        self.i.read(self.c, self.filepathname_fail)
        data = self.i.all()
        self.assertFalse(data)


#---
# suite: allows all tests run here to be run externally at 'test_all.py'
#---
def suite():
    """tests added to run in 'test_all.py'"""
    tests = ['test_py_version3_ok',
             'test_py_version2_ok',
             'test_ini_ok',
             'test_ini_fail',
             'test_ini_all_ok',
             'test_ini_all_fail']

    return unittest.TestSuite(map(TestIni, tests))


if __name__ == "__main__":
    suite()
    unittest.main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
