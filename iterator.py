#!/usr/bin/python2
#  -*- coding: utf-8 -*-
__author__ = 'jackie'

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


fibs = Fibs()
for f in fibs:
    if f > 1000:
        print f
        break

# 内建类型本身支持获得迭代器

it = iter([1,2,3])
print it.next()
print it.next()

# 生成器, 使用yield，函数会被冻结在那里直到下次调用，会从冻结的那里继续执行
# 1. 处理两层迭代
# def flatten(nested):
#     for sublist in nested:
#         for element in sublist:
#             yield element


# 2. 处理任意层迭代
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield  element
    except TypeError:
        yield nested

nested = [[1,2], [3, 4], [5]]

for num in flatten(nested):
    print num
nested = [[[1], 2], [3,4],[5,[6,7] ,8]]

print list(flatten(nested))
# 生成器推导式，返回的是一个生成器
g = ((i + 2) ** i for i in range(2, 27))
for value in g:
    print value

# 可以和列表推导式进行对比下
print [i * i for i in range(10) if i % 3 == 0]

# 生成器方法

def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new

r = repeater(12)
print r.next()
print r.send("hello")
print r.next()
print r.next()