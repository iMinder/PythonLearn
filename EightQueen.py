#!/usr/bin/python2
#  -*- coding: utf-8 -*-
__author__ = 'jackie'
import random

def conflict (state, nextX):
    nextY = len(state)
    for i in range(nextY):
        # 如果新的皇后和之前的同在一列或者对角线上，就返回True
        if abs(nextX - state[i]) in (0, nextY - i):
            return True
    return False

# def queen(num, state):
#     if len(state) == num - 1:
#         for pos in range(num):
#             if not conflict(state, pos):
#                 yield  pos

# 升级完整版
def queen(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queen(num, state + (pos, )):
                    yield (pos, ) + result

print (list(queen(8)))
def prettyprint(solution):
    def line(pos, length = len(solution)):
        return '. ' * (pos) + 'x ' + '. ' * (length - pos  - 1)
    for pos in solution:
        print line(pos)

prettyprint(random.choice(list(queen(8))))
