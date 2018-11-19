#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: decorator.py
# @time: 2018/7/17 下午4:09
# @desc: 装饰器
# @url: http://python.jobbole.com/81683/


# 定义一个装饰器
class decorator(object):
    def __init__(self, f):
        print("inside decorator.__init__()")
        f()  # Prove that function definition has completed

    def __call__(self):
        print("inside decorator.__call__()")


@decorator
def test_function():
    print("inside function()")


if __name__ == '__main__':
    print("Finished decorating function()")


