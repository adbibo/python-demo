#!/usr/bin/env python
# -*- coding=utf-8 -*-


def select_sort(a):
    ''''' 选择排序  
    每一趟从待排序的数据元素中选出最小（或最大）的一个元素，
    顺序放在已排好序的数列的最后，直到全部待排序的数据元素排完。
    选择排序是不稳定的排序方法。
    '''
    a_len = len(a)
    for i in range(a_len):  # 在0-n-1上依次选择相应大小的元素  
        min_index = i  # 记录最小元素的下标  
        for j in range(i + 1, a_len):  # 查找最小值  
            if a[j] < a[min_index]:
                min_index = j
        if min_index != i:  # 找到最小元素进行交换  
            a[i], a[min_index] = a[min_index], a[i]


if __name__ == '__main__':
    A = [10, -3, 5, 7, 1, 3, 7]
    print 'Before sort:', A
    select_sort(A)
    print 'After sort:', A
