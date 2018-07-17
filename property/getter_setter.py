#!/usr/bin/env python
# -*- coding=utf-8 -*-


class Student(object):
    __slots__ = ('_name', '_age', '_score', '_birth')

    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._score = 100
        self._birth = 1900

    def __str__(self):
        return str(self._name) + ',' + str(self._age)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must betweent 0-100')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    st = Student('Mike', 12)
    st.age = 1
    st.score = 60

    print(st)
    print(st.age)
    print(st.score)
