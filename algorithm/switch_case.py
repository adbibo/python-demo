#!/usr/bin/env python
# -*- coding=utf -*-

values = {
    'a': lambda x: x * 5,
    'b': lambda x: x + 7,
    'c': lambda x: x - 2
}

print values['a'](10)


# values = {
#            value1: do_some_stuff1,
#            value2: do_some_stuff2,
#            ...
#            valueN: do_some_stuffN,
#          }
# values.get(var, do_default_stuff)()


# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class Switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


# The following example is pretty much the exact use-case of a dictionary,
# but is included for its simplicity. Note that you can include statements
# in each suite.
v = 'ten'
for case in Switch(v):
    if case('one'):
        print 1
        break
    if case('two'):
        print 2
        break
    if case('ten'):
        print 10
        break
    if case('eleven'):
        print 11
        break
    if case():  # default, could also just omit condition or 'if True'
        print "something else!"
        # No need to break here, it'll stop anyway
