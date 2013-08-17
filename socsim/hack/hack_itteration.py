#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~

import collections

class Hello:
    def __init__(self, message, count):
        self.i = count
        self.message = message
    def count(self):
        return self.i
    def world(self):
        return "%s" % (self.count() * self.message)

def main():
    hw = Hello('World', 4)
    m = hw.world()
    print(m)

    #print(dir(hw))
    try:
        for item in hw.count():
            print(item)
    except TypeError:
        print("%s not iterable" % hw.count())

    if isinstance(hw.count(), collections.Iterable):
        print('iterable')
    else:
        print('not iterable')
        
if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
