#!/usr/bin/env python
# encoding: utf-8

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: dis_test.py
# @time: 2018/8/7 下午5:57
# @desc:

from dis import dis

b = 3
def f1(a):
    print(a)
    global b
    print(b)
    b=6
print(dis(f1))