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
