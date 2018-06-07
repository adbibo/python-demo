#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 判断数字是不是回文


def is_palindrome(n):
    n = str(n)
    m = n[::-1]
    return n == m


print is_palindrome('aba')

print is_palindrome(123432)
