#!/usr/bin/env python
# encoding: utf-8

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: registration.py
# @time: 2018/8/7 下午4:11
# @desc:

registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry -> ', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
