#!/usr/bin/env python
# -*- coding=utf-8 -*-


class Celsius(object):
    def __init__(self, value=0.0):
        print 'Celsius.__init__'
        self.value = float(value)

    def __get__(self, instance, owner):
        print 'Celsius.__get__'
        return self.value

    def __set__(self, instance, value):
        print 'Celsius.__set__'
        self.value = float(value)


class Temperature(object):
    celsius = Celsius()


if __name__ == '__main__':
    temp = Temperature()
    print temp.celsius
    temp.celsius = 1
    print temp.celsius
