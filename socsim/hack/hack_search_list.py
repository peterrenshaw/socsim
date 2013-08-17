#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


def get(data, key):
    """
    search for key in list of dictionsary with
    key/value pairs
    """
    for item in data:
        if 'key' in item:
            if item['key'] == key:
                return item
    return False


def main():
  data = [{'value': 'hackernews', 'key': 'TITLE'}, 
  {'value': 'news.ycombinator.com/?users=bootload', 'key': 'url'}, 
  {'value': 'bootload', 'key': 'user'},
  {'value': 'entreprenerial/technical reading, forum', 'key': 'function'},
  {'value': '2006', 'key': 'started'}, 
  {'value': '2012', 'key': 'ended'}, 
  {'value': 'dead', 'key': 'status'}, 
  {'value': 'hacker news and information', 'key': 'description'}]

  print(get(data, 'TITLE'))
  print(get(data, 'description'))
  print(get(data, 'url'))
  print(get(data, 'status')) 
        
if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
