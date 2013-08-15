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


import json
import os.path
import unittest


import tools
import factory
import record


class TestFactory(unittest.TestCase):
    def setUp(self):
        # os independent home dir
        self.osname = os.sys.platform
        self.home = tools.get_home_path_os(self.osname)
        self.basepath = os.path.join('code','socsim','record')
        self.filepathname_fail = os.path.join(self.home, self.basepath,'empty.ini')
        self.filepathname_titleno = os.path.join(self.home,self.basepath,'title_non.ini')
        self.filepathname = os.path.join(self.home, self.basepath,'urls.ini')

        # python versions
        self.pyhv = factory.hex_version()

        # Ini
        self.ini_title = "Urls"
        self.ini_desc = "description of URL information"
        self.c = factory.hack_import_configparser(self.pyhv)
        self.i = factory.Ini(self.pyhv)
        self.i.read(self.c, self.filepathname)
        self.data = self.i.all()

        # record obj
        self.m = record.Meta(self.ini_title, self.ini_desc)
        self.ma = self.m.all()    # Warning: must return all before injection
        self.r = record.Record(self.ma)

        # Factory
        self.f = factory.Factory(self.data, self.m, self.r)
    def tearDown(self):
        self.f = None
        self.i = None
        self.c = None
        self.data = None
        self.m = None
        self.ma = None
        self.r = None

        self.pyhv = None
        self.filepathname = None
        self.filepathname_fail = None
        self.home = None

    # init
    def test_fac_ok(self):
        """add new name & desc, return T"""
        self.assertTrue(self.f)
    # status
    def test_fac_status_ok(self):
        """default status, F"""
        status = self.f.status()
        self.assertFalse(status)
    # build
    def test_fac_build_ok(self):
        """default build, empty data, F"""
        d = []
        # T because we use default 
        status = self.f.build(d)
        self.assertTrue(status)
    def test_fac_build_meta_ok(self):
        """check build using ini file contents"""
        status = self.f.build()
        self.assertTrue(status)
    def test_fac_build_valid_ok(self):
        """build with data, T"""
        status = self.f.build()
        self.assertTrue(status)
    # all
    def test_fac_all_ok(self):
        """default, F"""
        self.f.build()
        status = self.f.all()
        self.assertTrue(status)


#---
# suite: allows all tests run here to be run externally at 'test_all.py'
#---
def suite():
    """tests added to run in 'test_all.py'"""
    tests = ['test_fac_ok',
             'test_fac_status_ok',
             'test_fac_build_ok',
             'test_fac_build_meta_ok',
             'test_fac_build_valid_ok',
             'test_fac_all_ok']

    return unittest.TestSuite(map(TestFactory, tests))


if __name__ == "__main__":
    suite()
    unittest.main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
