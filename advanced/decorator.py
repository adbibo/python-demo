#!/usr/bin/env python
# -*- coding=utf-8 -*-

import time

class Decorator(object):
    def __init__(self, f):
        print("inside decorator.__init__()")
        f()  # Prove that function definition has completed

    def __call__(self):
        print("inside decorator.__call__()")


@Decorator
def function():
    print("inside function()")


if __name__ == '__main__':
    print("Finished decorating function()")


def myfunc():
    print("start my func")
    time.sleep(0.6)
    print("end my func")


def addfunc(a, b):
    print("start add func")
    print("result is %d" % (a + b))
    print("end add func")


if __name__ == "__main__":
    print("my func is: ", myfunc.__name__)
    myfunc()
    print("my func is: ", addfunc.__name__)
    addfunc(1, 2)
