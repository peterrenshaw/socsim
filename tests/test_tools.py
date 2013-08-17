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


import socsim.tools


class TestTools(unittest.TestCase):
    def setUp(self):
        self.my_py = ['1','2','3']
        self.my_json = """[
    "1",
    "2",
    "3"
]"""
    def tearDown(self):
        self.my_py = None
        self.my_json = None

    # py2json
    def test_py2json_ok(self):
        """input python, get out json"""
        json = socsim.tools.py2json(self.my_py)
        self.assertTrue(json)
        self.assertEqual(json, self.my_json)
    def test_py2json_empty_arg_fail(self):
        """empty arg should return F"""
        self.assertFalse(socsim.tools.py2json(""))
    # json2py
    def test_json2py_ok(self):
        """input json, get out python"""
        py = socsim.tools.json2py(self.my_json)
        self.assertTrue(py)
        self.assertEqual(py, self.my_py)
    def test_json2py_empyt_arg_fail(self):
        """empty arg should return F"""
        self.assertFalse(socsim.tools.json2py(""))
    # convert
    def test_convert_empty_arg_fail(self):
        """empty arg should fail"""
        self.assertFalse(socsim.tools.convert(""))
    # save
    def test_save_empty_path_arg_fail(self):
        """empty arg/s for read, F"""
        self.assertFalse(socsim.tools.save("","data"))
    def test_save_empty_data_arg_fail(self):
        """empty data arg, F"""
        fp = os.path.join("")
        self.assertFalse(socsim.tools.save(fp, ""))
    # read
    def test_read_empty_fpn_arg_fail(self):
        """empty filepathname, F"""
        self.assertFalse(socsim.tools.load(""))


#---
# suite: allows all tests run here to be run externally at 'test_all.py'
#---
def suite():
    """tests added to run in 'test_all.py'"""
    tests = ['test_py2json_ok',
             'test_py2json_empty_arg_fail',
             'test_json2py_ok',
             'test_json2py_empyt_arg_fail',
             'test_convert_empty_arg_fail',
             'test_save_empty_path_arg_fail',
             'test_save_empty_data_arg_fail',
             'test_read_empty_fpn_arg_fail']

    return unittest.TestSuite(map(TestTools, tests))


if __name__ == "__main__":
    suite()
    unittest.main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
