#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
 @author 
 @create 2017-03-17 下午10:06
"""

import heapq


# 堆排序
# 第一种实现
def Heapify(a, start, end):
    left = 0
    right = 0
    maxv = 0
    left = start * 2
    right = start * 2 + 1
    while left <= end:
        maxv = left
        if right <= end:
            if a[left] < a[right]:
                maxv = right
            else:
                maxv = left
        if a[start] < a[maxv]:
            a[maxv], a[start] = a[start], a[maxv]
            start = maxv
        else:
            break
        left = start * 2
        right = start * 2 + 1


def BuildHeap(a):
    size = len(a)
    i = (size - 1) // 2;
    while i >= 0:
        Heapify(a, i, size - 1)
        i = i - 1


def HeapSort(a):
    BuildHeap(a)
    print 'first before sorted:', a
    i = len(a) - 1

    while i >= 0:
        a[0], a[i] = a[i], a[0]
        Heapify(a, 0, i - 1)
        i = i - 1


a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
HeapSort(a)
print 'first after sorted', a


# 第二种实现
def buildHeap(a, size):
    for j in range(size / 2 - 1, -1, -1):
        adjustHeap(a, j, size)


def adjustHeap(a, i, size):
    lchild = 2 * i  # i的左孩子节点序号
    rchild = 2 * i + 1  # i的右孩子节点序号
    maxIndex = i
    if i < size / 2:
        if lchild <= size and a[lchild] > a[maxIndex]:
            maxIndex = lchild
        if rchild <= size and a[rchild] > a[maxIndex]:
            maxIndex = rchild
        if maxIndex != i:
            a[i], a[maxIndex] = a[maxIndex], a[i]
            adjustHeap(a, maxIndex, size)


if __name__ == "__main__":
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    b = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    buildHeap(a, len(a))
    print '-------------------------------------------------'
    print 'second before sorted', a
    i = len(a) - 1
    while i >= 0:
        a[0], a[i] = a[i], a[0]
        buildHeap(a, i)
        i = i - 1
    print 'second after sorted', a

    # python自带函数实现
    heapq.heapify(b)
    heap = []
    while b:
        heap.append(heapq.heappop(b))
    b[:] = heap
    print '-------------------------------------------------'
    print 'sdk sorted', b
