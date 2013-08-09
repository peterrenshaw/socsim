#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


import sys
from optparse import OptionParser


import record


def main():
    usage = "usage: %prog [v] -t -d"
    parser = OptionParser(usage)
    parser.add_option("-t", "--title", dest="title", 
                      help="metadata title information")
    parser.add_option("-d", "--description", dest="description", 
                      help="metadata description information")
    parser.add_option("-s", "--save", dest="save", 
                      help="convert to json, save to file")
    parser.add_option("-v", "--version", dest="version", \
                      action="store_true",
                      help="current version")    
    options, args = parser.parse_args()


    if options.version:
        print("%s v%s %s %s" % ('smem-url', '0.0.1', '2013AUG09', '(C) 2013'))
        sys.exit(0)
    elif options.title and options.description:
        description = record.Meta("bigblock", "This is block is combined with A, B, C")
        
        meta_a = record.Meta("A", "This is the A meta block")
        meta_a.add("colour", "red")
        meta_a.add("size", 2)
        meta_a.add("weight", 10)
        meta_a.add("format", "2x2")
        
        meta_b = record.Meta("B", "This is the B meta block")
        meta_b.add("colour", "yellow")
        meta_b.add("size", 4)
        meta_b.add("weight", 20)
        meta_b.add("format", "2x4")        

        meta_c = record.Meta("C", "This is the C meta block")
        meta_c = record.Meta("C", "This is the C meta block")
        meta_c.add("colour", "blue")
        meta_c.add("size", 1)
        meta_c.add("weight", 10)
        meta_c.add("format", "1x1")

        blocks = record.Record(description.all())
        blocks.add('A', meta_a.all())
        blocks.add('B', meta_b.all())
        blocks.add('C', meta_c.all())

        if options.save: 
            json = record.py2json(blocks.all())
            if record.save(options.save, json):
                print("save %s" % options.save)
            else:
                print("error saving %s" % options.save)
                sys.exit(1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
