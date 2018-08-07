#!/usr/bin/env python
# encoding: utf-8

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: collections_test.py
# @time: 2018/8/7 下午3:47
# @desc:
from collections import abc

my_dict ={}
print(isinstance(my_dict, abc.Mapping))