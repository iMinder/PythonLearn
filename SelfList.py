# -*- coding:utf-8 -*-
__author__ = 'jackie'

def checkIndex(key):
    """

    Is the given key an acceptable index?

    To be acceptable, the key should be a non-negative integer. If it
    is not an integer, a TypeError is raised; if it is negative, an
    IndexError is raised (since the sequence is of infinite length).
    """
    if not isinstance(key,(int, long)) : raise TypeError
    if key < 0 : raise IndexError

class ArithmeticSequence:
    def __init__(self, start = 0, step = 1):
        """
        初始化算术队列
        :param start: 序列中的第一个值
        :param step: 相邻之间的差别
        :return:
        """
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        """
        从队列中获取一个值
        :param key:
        :return:
        """
        checkIndex(key)

        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        """
        设置序列中的一个对象的值
        :param key:
        :param value:
        :return:
        """
        checkIndex(key)
        self.changed[key] = value


s = ArithmeticSequence(1,2)
print s[4]
s[4] = 2
print s[4]
print s[5]
s[-10]