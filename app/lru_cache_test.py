#!/usr/bin/env python
# encoding: utf-8

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: lru_cache_test.py
# @time: 2018/8/8 下午2:19
# @desc:

from functools import lru_cache
from timer import clock_new

@lru_cache()
@clock_new
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print(fibonacci(6))

