#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
 @author 
 @create 2017-03-17 下午2:45
"""
# input: [('uid1', 'A1'), ('uid2', 'A1'), ('uid3', 'A1'), ('uid1', 'A2'), ('uid2', 'A3'), ('uid3', 'A2')]
# output: [('A1', 3), ('A2', 2), ('A3', 1)]

from collections import Counter
from itertools import groupby


def func(t):
    return sorted([(article, times) for article, times in Counter([book[1] for book in t]).items()],
                  key=lambda x: x[1], reverse=True)


def func2(t):
    return sorted([(key, len(list(key_list))) for key, key_list in groupby([book[1] for book in t])], key=lambda x: x[1],
                  reverse=True)


t = [('uid1', 'A1'), ('uid2', 'A1'), ('uid3', 'A1'), ('uid1', 'A2'), ('uid2', 'A3'), ('uid3', 'A2')]
print func2(t)

print groupby([book[1] for book in t])

for key, key_list in groupby([book[1] for book in t]):
    print key, list(key_list)
