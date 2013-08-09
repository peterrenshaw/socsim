#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


import json
import os.path
import unittest


import record


class TestMeta(unittest.TestCase):
    def setUp(self):
        self.title = "a title"
        self.description = "a rather boring descripotion"
        self.source = os.path.join("e:","code","records")
        self.m = record.Meta(self.title, self.description)
        
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
             'test_all_key_ok']

    return unittest.TestSuite(map(TestMeta, tests))


if __name__ == "__main__":
    suite()
    unittest.main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
