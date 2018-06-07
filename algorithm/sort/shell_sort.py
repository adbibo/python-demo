#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
希尔排序，也称递减增量排序算法,希尔排序是非稳定排序算法。该方法又称缩小增量排序，因DL．Shell于1959年提出而得名。

先取一个小于n的整数d1作为第一个增量，把文件的全部记录分成d1个组。所有距离为d1的倍数的记录放在同一个组中。先在各组内进行排序；

然后，取第二个增量d2
"""


def shell_sort(a):
    ''''' shell排序 '''
    a_len = len(a)
    gap = a_len / 2  # 增量  
    while gap > 0:
        for i in range(a_len):  # 对同一个组进行选择排序 
            m = i
            j = i + 1
            while j < a_len:
                if a[j] < a[m]:
                    m = j
                    j += gap  # j增加gap  
            if m != i:
                a[m], a[i] = a[i], a[m]
        gap /= 2


if __name__ == '__main__':
    A = [10, -3, 5, 7, 1, 3, 7]
    print 'Before sort:', A
    shell_sort(A)
    print 'After sort:', A
