#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


import unittest


import record
import test_meta
import test_record

#---
# suite: allows all tests run here to be run externally at 'test_all.py'
#---
def main():
    """tests added to run in 'test_all.py'"""
    # add all new test suites per test module here
    suite_meta = test_meta.suite()
    suite_record = test_record.suite()

    # add the suite to be tested here
    alltests = unittest.TestSuite((suite_meta, 
                                   suite_record)) 
    # run the suite
    runner = unittest.TextTestRunner()
    runner.run(alltests)


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab