#!/usr/bin/python
# -*- coding: utf-8 -*-
# 快速排序  
'''''
划分 使满足 以A[r]为基准对数组进行一个划分，比A[r]小的放在左边，
   比A[r]大的放在右边
快速排序的分治partition过程有两种方法，
一种是上面所述的两个指针索引一前一后逐步向后扫描的方法,
另一种方法是两个指针从首位向中间扫描的方法。
'''


def sub_sort(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort1(array, low, high):
    if low < high:
        key_index = sub_sort(array, low, high)
        print array[key_index]
        print array
        quick_sort1(array, low, key_index)
        quick_sort1(array, key_index + 1, high)


def quick_sort(array):
    low = list()
    high = list()
    if len(array) <= 1:
        return array

    sentry = array.pop()
    for data in array:
        if data < sentry:
            low.append(data)
        else:
            high.append(data)

    return quick_sort(low) + [sentry] + quick_sort(high)

if __name__ == '__main__':
    src_array = [8, 10, 9, 6, 4, 16, 5, 13, 26, 18, 2, 45, 34, 23, 1, 7, 3]
    # quick_sort(src_array, 0, len(src_array) - 1)

    print quick_sort(src_array)
