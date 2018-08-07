#!/usr/bin/env python
# encoding: utf-8

# @author: yinhaochuan
# @contact: yinhaochuan@100tal.com
# @file: array_test.py
# @time: 2018/8/7 下午2:02
# @desc:

from array import array
from random import random

# array write to file
floats = array('d', (random() for _ in range(10 ** 7)))
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

# array read from file
floats2 = array('d')
fp = open('floats.bin', 'wb')
floats2.fromfile(fp, 10**7)
fp.close()

