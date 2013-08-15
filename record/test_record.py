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


import unittest


import record


class TestRecord(unittest.TestCase):
    def setUp(self):
        self.m = record.Meta("meta test", "this is a test of meta data")
        self.r = record.Record(self.m.all())
    def tearDown(self):
        self.m = None
        self.r = None


    # init
    def test_init_ok(self):
        """initialise Record, T"""
        self.assertTrue(self.r)

    #---
    # TODO HACK ALERT, fix me
    # check for bad data input, fail requires 
    # obj.status check
    def test_init_fail(self):
        """inject non list ie: self.m instead of self.m.all()"""
        self.r = record.Record(self.m)
        self.assertFalse(self.r.status())
    # new
    def test_new(self):
        """test new ok"""
        md = record.Meta("new meta", "this a new meta")
        metadata = md.all()
        status = self.r.new(metadata)
        md = None
        self.assertTrue(status)
    # add
    def test_add_ok(self):
        """default add of record data"""
        self.assertTrue(self.r.add('a key', 'a value that I like'))
    def test_add_unique(self):
        """add data, try to add duplicate data, should fail"""
        key = 'unique'
        value = 'non unique value'
        self.assertTrue(self.r.add(key, value))
        self.assertFalse(self.r.add(key, value))
    def test_add_bulk_ok(self):
        """add list of dic(key/value) pairs"""
        self.m.add('test1','input of bulk data')
        self.m.add('test2','more input of data')
        self.m.add('test3','yet more data input')
        metadata = self.m.all()
        self.assertTrue(self.r.new(metadata))
        metadata = None
    def test_add_bulk_fail(self):
        """test empty add, should F"""
        self.assertFalse(self.r.new([]))
    def test_add_no_data_fail(self):
        """add no data, should fail"""
        self.assertFalse(self.r.add('',''))
    def test_add_no_key_yes_value_fail(self):
        """no key, yes value, F"""
        self.assertFalse(self.r.add('','value'))
    def test_add_yes_key_no_value_fail(self):
        """yes key, no value, F"""
        self.assertFalse(self.r.add('key', ''))

    # search
    def test_search_key_ok(self):
        """pass in known key, return results"""
        key = "everybodyknows"
        self.r.add(key, "this is nowhere")
        self.assertTrue(self.r.search(key))
    def test_search_empty_key_fail(self):
        """empty key for search should fail"""
        key = "everybodyknows"
        self.r.add(key, "this is nowhere")
        self.assertFalse(self.r.search(""))
    def test_search_nothing_found_fail(self):
        """valid key but nothing found, fails"""
        self.r.add("smalltown", "never put her roots down")
        key = "diner"
        self.assertFalse(self.r.search(key))
    # search item
    def test_search_item_by_key_ok(self):
        """seach by key for item, ok"""
        key = "unknownlegend"
        self.r.add(key, "unknown legend in her own time")
        result = {'value': 'unknown legend in her own time', 
                  'key': 'unknownlegend'}
        #print(self.r.search_item(key))
        self.assertEqual(self.r.search_item(key), result)
    def test_search_item_by_empty_key_fail(self):
        """search by empty key, fail"""
        key = "unknownlegend"
        self.r.add(key, "unknown legend in her own time")
        self.assertFalse(self.r.search_item(""))
    def test_search_item_by_key_no_result_fail(self):
        """search by key, not found, fail"""
        key = "unknown"
        self.r.add("unknownlegend", "unknown legend in her own time")
        self.assertFalse(self.r.search(key))
    # search value
    def test_search_value_by_key_ok(self):
        """search by key, result ok"""
        key = "unknownlegend"
        value = "unknown legend in her own time"
        self.assertTrue(self.r.add(key, value))
        self.assertEqual(value, self.r.search_value(key))
    def test_search_value_by_key_fail(self):
        """search by key, result not found, fail"""
        key = "unknownlegend"
        value = "unknown legend in her own time"
        self.assertTrue(self.r.add(key, value))
        self.assertFalse(self.r.search_value("legend"))
    def test_search_value_empty_key_fail(self):
        """search by empty key, fail"""
        key = "unknownlegend"
        value = "unknown legend in her own time"
        self.assertTrue(self.r.add(key, value))
        self.assertFalse(self.r.search_value(""))
    def test_search_value_not_found_fail(self):
        """search by key, not found, fail"""
        key = "unknownlegend"
        value = "unknown legend in her own time"
        self.assertTrue(self.r.add(key, value))
        self.assertFalse(self.r.search_value("legend"))
    # search index
    def test_search_index_by_key_ok(self):
        """search by valid key, index found, pass"""
        key = "unknownlegend"
        self.assertTrue(self.r.add(key, "unknown legend in her own time"))
        self.assertTrue(self.r.add("walkon", "I remember the good old days / stayed up all night"))
        self.assertTrue(self.r.add("winterlong", "I waited for you winterlong / you seem to be where I belong"))
        #print(self.r.search_index(key))
        self.assertTrue(self.r.search_index(key))
        self.assertEqual(3, self.r.search_index(key))
    def test_search_index_by_empty_key_fail(self):
        """search by empty key, fail"""
        key = "unknownlegend"
        self.assertTrue(self.r.add(key, "unknown legend in her own time"))
        self.assertFalse(self.r.search_index(""))
    def test_search_index_by_key_not_found_fail(self):
        """search index by key, no result, fail"""
        key = "unknown"
        self.assertTrue(self.r.add("unknownlegend", "unknown legend in her own time"))
        self.assertTrue(self.r.add("walkon", "I remember the good old days / stayed up all night"))
        self.assertTrue(self.r.add("winterlong", "I waited for you winterlong / you seem to be where I belong"))
        self.assertFalse(self.r.search_index(key))
    # all
    def test_all_ok(self):
        """return all, ok"""
        self.assertTrue(self.r.add("unknownlegend", "unknown legend in her own time"))
        self.assertTrue(self.r.add("walkon", "I remember the good old days / stayed up all night"))
        self.assertTrue(self.r.add("winterlong", "I waited for you winterlong / you seem to be where I belong"))
        self.assertTrue(self.r.all())
    def test_all_no_adds_ok(self):
        """no add's, return metadata, nothing else"""
        self.assertTrue(self.r.all())
        metadata_keys = ['title','description','created']
        for item in self.r.all():
            self.assertTrue(item['key'] in metadata_keys)


#---
# suite: allows all tests run here to be run externally at 'test_all.py'
#---
def suite():
    """tests added to run in 'test_all.py'"""
    tests = ['test_init_ok',
             'test_init_fail',
             'test_new',
             'test_add_ok',
             'test_add_unique',
             'test_add_bulk_ok',
             'test_add_bulk_fail',
             'test_add_no_data_fail',
             'test_add_no_key_yes_value_fail',
             'test_add_yes_key_no_value_fail',
             'test_search_key_ok',
             'test_search_empty_key_fail',
             'test_search_nothing_found_fail',
             'test_search_item_by_key_ok',
             'test_search_item_by_empty_key_fail',
             'test_search_item_by_key_no_result_fail',
             'test_search_value_by_key_ok',
             'test_search_value_by_key_fail',
             'test_search_value_empty_key_fail',
             'test_search_value_not_found_fail',
             'test_search_index_by_key_ok',
             'test_search_index_by_empty_key_fail',
             'test_search_index_by_key_not_found_fail',
             'test_all_ok',
             'test_all_no_adds_ok']

    return unittest.TestSuite(map(TestRecord, tests))


if __name__ == "__main__":
    suite()
    unittest.main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
