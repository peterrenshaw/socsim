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


import socsim.record


class TestMeta(unittest.TestCase):
    def setUp(self):
        self.title = "a title"
        self.description = "a rather boring descripotion"
        self.source = os.path.join("e:","code","records")
        self.m = socsim.record.Meta(self.title, self.description)
        
    def tearDown(self):
        self.m = None
        self.name = None
        self.description = None
        self.source = None

    # new
    def test_new_ok(self):
        """ add new name & desc, return T"""
        status = self.m.new('name-of-value', 'a description of value name')
        self.assertTrue(status)
    # add
    def test_add_ok(self):
        """add new name & desc, check values ok"""
        name = "name"
        description = "description"
        self.assertTrue(self.m.add(name, description))
    def test_add_no_duplicates(self):
        """can you add a duplicate key to the record?"""
        name = 'name20'
        value = "some crappy value"
        status1 = self.m.add(name, value)
        status2 = self.m.add(name, value)
        self.assertNotEqual(status1, status2)
    def test_add_no_spaces_key(self):
        title = "a bloody disgrace of a title"
        title_replace = title.replace(' ','-')
        self.m.add(title, 'a bloody disgrace of a  value')
        self.assertTrue(self.m.search(title_replace))
        self.assertFalse(self.m.search(title))
    # search
    def test_search_ok(self):
        self.m.add('name0', 'a value0')
        status = self.m.search('name0')
        self.assertTrue(status)
    def test_search_fail(self):
        self.m.add('name1', 'value1')
        status = self.m.search('name10')
        self.assertFalse(status)
    # all
    def test_all_key_ok(self):
        """something added, return all, test all keys are present"""
        self.m.add('name2', 'value2')

        title = self.m.search('title')
        description = self.m.search('description')
        created = self.m.search('created')
        name2 = self.m.search('name2')
        
        status = title and description and created and name2
        self.assertTrue(status)
    def test_all_key_no_add_ok(self):
        """add nothing, still get Meta default"""
        self.assertTrue(self.m.all())
        metadata_keys = ['title','description','created']
        for item in self.m.all():
            self.assertTrue(item['key'] in metadata_keys)

#---
# suite: allows all tests run here to be run externally at 'test_all.py'
#---
def suite():
    """tests added to run in 'test_all.py'"""
    tests = ['test_new_ok', 
             'test_add_ok',
             'test_add_no_duplicates',
             'test_add_no_spaces_key',
             'test_search_ok',
             'test_search_fail',
             'test_all_key_ok',
             'test_all_key_no_add_ok']

    return unittest.TestSuite(map(TestMeta, tests))


if __name__ == "__main__":
    suite()
    unittest.main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
