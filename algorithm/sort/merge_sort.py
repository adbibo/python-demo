# /usr/bin/env python
# -*- coding=utf-8 -*-

"""
归并排序

归并排序也称合并排序，是分治法的典型应用。分治思想是将每个问题分解成个个小问题，将每个小问题解决，然后合并。

具体的归并排序就是，将一组无序数按n/2递归分解成只有一个元素的子项，一个元素就是已经排好序的了。然后将这些有序的子元素进行合并。

合并的过程就是 对 两个已经排好序的子序列，先选取两个子序列中最小的元素进行比较，选取两个元素中最小的那个子序列并将其从子序列中

去掉添加到最终的结果集中，直到两个子序列归并完成。
"""

import sys


def merge(nums, first, middle, last):
    ''''' merge '''
    # 切片边界,左闭右开并且是了0为开始  
    lnums = nums[first:middle + 1]
    rnums = nums[middle + 1:last + 1]
    lnums.append(sys.maxint)
    rnums.append(sys.maxint)
    l = 0
    r = 0
    for i in range(first, last + 1):
        if lnums[l] < rnums[r]:
            nums[i] = lnums[l]
            l += 1
        else:
            nums[i] = rnums[r]
        r += 1


def merge_sort(nums, first, last):
    ''''' merge sort
    merge_sort函数中传递的是下标，不是元素个数
    '''
    if first < last:
        middle = (first + last) / 2
        merge_sort(nums, first, middle)
        merge_sort(nums, middle + 1, last)
        merge(nums, first, middle, last)


if __name__ == '__main__':
    nums = [10, 8, 4, -1, 2, 6, 7, 3]
    print 'nums is:', nums
    merge_sort(nums, 0, 7)
    print 'merge sort:', nums
