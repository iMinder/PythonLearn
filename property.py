# -*- coding:utf-8 -*-
__author__ = 'jackie'

__metaclass__ = type

# 1.第一个版本
# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#     def setSize(self, size):
#         self.width = size
#         self.height = size
#     def getSize(self):
#         return self.width, self.height
#     size = property(getSize, setSize)

# 2.第二个版本

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self, key, value):
        if key == 'size':
            self.width = value
            self.height = value
        else:
            self.__dict__[key] = value
    def __getattr__(self, key):
        if key == 'size':
            return self.width, self.height
        else:
            raise AttributeError


r = Rectangle()
r.size = 100
print r.size

