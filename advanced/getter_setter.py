#!/usr/bin/env python
# -*- coding=utf-8 -*-


class Student(object):
    __slots__ = ('name', 'age', '__score', '_birth')

    def __str__(self):
        return str(self.name) + ',' + str(self.age)

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must betweent 0-100')
        self.__score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


if __name__ == '__main__':
    st = Student()
    st.name = 'll'
    st.age = 1
    st.score = 60

    print(st)
