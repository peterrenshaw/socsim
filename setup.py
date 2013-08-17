#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~
import os
from setuptools import setup, find_packages
from setuptools import setup


from socsim import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name = "socsim",
      version = __version__,
      description = 'social media simulation tools',
      long_description=read('README'),
      license = 'GNU GPL 3.0',
      author = "Peter Renshaw",
      author_email = "goonmail@netspace.net.au",
      url = 'https://github.com/peterrenshaw/socsim',
      packages = find_packages(),
      keywords = ['message','testing','human','response'],
      zip_safe = True)

# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
