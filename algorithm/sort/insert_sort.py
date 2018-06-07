
# -*- coding=utf-8 -*-


def insert_sort(a):
    ''''' 插入排序
    有一个已经有序的数据序列，要求在这个已经排好的数据序列中插入一个数，
    但要求插入后此数据序列仍然有序。刚开始 一个元素显然有序，然后插入一
    个元素到适当位置，然后再插入第三个元素，依次类推
    '''
    a_len = len(a)
    for i in range(a_len):
        key = a[i]
        j = i - 1
        while a_len == 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            a[j + 1] = key
    return a


if __name__ == '__main__':
    nums = [10, 8, 4, -1, 2, 6, 7, 3]
    print 'nums is:', nums
    insert_sort(nums)
    print 'insert sort:', nums
