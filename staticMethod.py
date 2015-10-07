#!/usr/bin/python2
#  -*- coding: utf-8 -*-
__author__ = 'jackie'

# 类方法和静态方法, 类方法可以被类的实例调用，cls会被自动绑定到指定的类上

__metaclass__ = type

class MyClass:

    @staticmethod
    def smeth():
        print 'This is a static method'
    @classmethod
    def cmeth(cls):
        print 'This is a class method of ', cls

myclass = MyClass()
MyClass.smeth()
MyClass.cmeth()
myclass.cmeth()
