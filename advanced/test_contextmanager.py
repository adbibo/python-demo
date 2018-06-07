#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""

"""

import time
from contextlib import contextmanager


class demo(object):
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_ty, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))


@contextmanager
def file_open(path):
    try:
        f_obj = open(path, "w")
        yield f_obj
    except OSError:
        print("We had an error!")
    finally:
        print("Closing file")
        f_obj.close()


"""
contextlib.closing(thing)
contextlib.suppress(*exceptions)
contextlib.redirect_stdout/redirect_stderr for python 3.4 & 3.5
contextlib.ExitStack
"""

if __name__ == '__main__':

    with demo('counting'):
        n = 10000000
        while n > 0:
            n -= 1
