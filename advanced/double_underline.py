#!/usr/bin/env python
# -*- coding-=utf-8 -*-

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: double_underline.py
# @time: 2018/7/17 下午4:09
# @desc: python内置的一些双下划线函数的重载


class Test(object):
    # 初始化 构造函数
    def __init__(self, start=0, step=1):
<<<<<<< HEAD
        print("Call function  __init__")
=======
        print("Call  function  __init__")
>>>>>>> 0ab40c3f9c9be3ec741ec9c719b7f1a74f460d05
        self.start = start
        self.step = step
        self.data = {}

<<<<<<< HEAD
    def __getitem__(self, item):
=======
    # 获取关键字对应的值
    def __getitem__(self, key):
>>>>>>> 0ab40c3f9c9be3ec741ec9c719b7f1a74f460d05
        print("Call function __getitem__")
        try:
            return self.data[key]
        except KeyError:
            return self.start + key * self.step

    # 插入k-v对
    def __setitem__(self, key, value):
        print("Call function __setitem__")
<<<<<<< HEAD
        self.myData[key] = value

    def __len__(self):
        print("Call function __len__")
        return len(self.myData) + 1
=======
        self.data[key] = value
    
    # len函数重载
    def __len__(self):
        print("Call function __len__")
        return len(self.data) + 1
>>>>>>> 0ab40c3f9c9be3ec741ec9c719b7f1a74f460d05

    # 删除指定关键字
    def __delitem__(self, key):
        print("Call function __delitem__")
<<<<<<< HEAD
        del self.myData[key]
=======
        del self.data[key]
>>>>>>> 0ab40c3f9c9be3ec741ec9c719b7f1a74f460d05


if __name__ == "__main__":
    #  初始化
    s = Test(1, 2)
    print(s)
<<<<<<< HEAD
    print(s[3])
    s[3] = 100
    print(s[3])

    print(len(s))
=======
    # 调用__getitem__
    print(s[3])
    # 调用__setitem__
    s[3] = 100
    print(s[3])
    # 调用__len__
    print(len(s))
    # 调用__delitem__
>>>>>>> 0ab40c3f9c9be3ec741ec9c719b7f1a74f460d05
    del s[3]
    print(s[3])



