#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


import unittest


import record


class TestRecord(unittest.TestCase):
    def setUp(self):
        self.m = record.Meta("meta test", "this is a test of meta data")
        self.r = record.Record(self.m.all())
    def tearDown(self):
        self.m = None
        self.r = None


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



#---
# suite: allows all tests run here to be run externally at 'test_all.py'
#---
def suite():
    """tests added to run in 'test_all.py'"""
    tests = ['test_new',
             'test_add_ok',
             'test_add_unique',
             'test_add_bulk_ok',
             'test_add_bulk_fail',
             'test_add_no_data_fail',
             'test_add_no_key_yes_value_fail',
             'test_add_yes_key_no_value_fail']

    return unittest.TestSuite(map(TestRecord, tests))


if __name__ == "__main__":
    suite()
    unittest.main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
