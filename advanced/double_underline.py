#!/usr/bin/env python
# -*- coding-=utf-8 -*-


class Test(object):
    def __init__(self, start=0, step=1):
        print("Call function  __init__")
        self.start = start
        self.step = step
        self.myData = {}

    def __getitem__(self, item):
        print("Call function __getitem__")
        try:
            return self.myData[item]
        except KeyError:
            return self.start + item * self.step

    def __setitem__(self, key, value):
        print("Call function __setitem__")
        self.myData[key] = value

    def __len__(self):
        print("Call function __len__")
        return len(self.myData) + 1

    def __delitem__(self, key):
        print("Call function __delitem__")
        del self.myData[key]


if __name__ == "__main__":
    s = Test(1, 2)
    print(s)
    print(s[3])
    s[3] = 100
    print(s[3])

    print(len(s))
    del s[3]
    print(s[3])



