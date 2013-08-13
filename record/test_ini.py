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


import factory


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
        self.basepath = os.path.join('code','socsim','record')
        self.filepathname_fail = os.path.join(self.home, self.basepath,'empty.ini')
        self.filepathname_titleno = os.path.join(self.home,self.basepath,'title_non.ini')
        self.filepathname = os.path.join(self.home, self.basepath,'urls.ini')

        # python versions
        self.pyhv = factory.hex_version()
        self.pyhv3 = "30000f0"
        self.pyhv2 = "20000f0"

        self.c = factory.hack_import_configparser(self.pyhv)
        self.i = factory.Ini(self.pyhv)
    def tearDown(self):
        self.i = None
        self.c = None
        self.pyhv = None
        self.filepathname = None
        self.filepathname_fail = None
        self.home = None

    # ini files
    def test_ini_ok(self):
        """default ini, T"""
        status = factory.Ini(self.pyhv)
        self.assertTrue(status)
    def test_ini_fail(self):
        """default F with no filenamepath set"""
        status = self.i.read(self.c, "")
        self.assertFalse(status)
    # read
    def test_ini_read_ok(self):
        """default read, T"""
        status = self.i.read(self.c, self.filepathname)
        self.assertTrue(status)
    def test_ini_read_fail(self):
        """read bad ini file, F"""
        status = self.i.read(self.c, self.filepathname_titleno)
        self.assertFalse(status)
    def test_ini_read_unicode(self):
        """
        urls.ini contains unicode mixed with ascii. is there 
        a specific test to look out for?
        """
        status = self.i.read(self.c, self.filepathname)
        self.assertTrue(status)
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
    tests = ['test_ini_ok',
             'test_ini_fail',
             'test_ini_read_ok',
             'test_ini_read_fail',
             'test_ini_read_unicode',
             'test_ini_all_ok',
             'test_ini_all_fail']

    return unittest.TestSuite(map(TestIni, tests))


if __name__ == "__main__":
    suite()
    unittest.main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
