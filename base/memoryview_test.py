#!/usr/bin/env python
# encoding: utf-8

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: memoryview_test.py
# @time: 2018/8/7 下午2:44
# @desc:

from array import array

numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(numbers)
print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())
print(numbers)