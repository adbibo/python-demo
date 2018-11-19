<<<<<<< HEAD:advanced/advanced.py
#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: advanced.py
# @time: 2018/7/2 下午3:17


class Student(object):
    """
    双下划线：双下划线开头的命名形式在 Python 的类成员中使用表示名字改编 (Name Mangling)，即如果有一 Test 类里有一成员 __x，
        那么 dir(Test) 时会看到 _Test__x 而非 __x。这是为了避免该成员的名称与子类中的名称冲突。但要注意这要求该名称末尾没有下划线。
        双下划线开头双下划线结尾的是一些 Python 的“魔术”对象，如类成员的 __init__、__del__、__add__、__getitem__ 等，
        以及全局的 __file__、__name__ 等。 Python 官方推荐永远不要将这样的命名方式应用于自己的变量或函数，而是按照文档说明来使用。

    单下划线：这个被常用于模块中，在一个模块中以单下划线开头的变量和函数被默认当作内部函数；
        在 Python 的官方推荐的代码样式中，还有一种单下划线结尾的样式，这在解析时并没有特别的含义，但通常用于和 Python 关键词区分开来，
        比如如果我们需要一个变量叫做 class，但 class 是 Python 的关键词，就可以以单下划线结尾写作 class_。

    """
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
    # st.age = 1
    st.score = 60
    print(st)
=======
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
>>>>>>> 0ab40c3f9c9be3ec741ec9c719b7f1a74f460d05:advanced/getter_setter.py
