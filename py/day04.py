#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test module'

__author__ = 'wfeng'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        # print(args)
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

hello = greeting('wfeng')
# print(hello)

# print(sys.path)


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()

print(bart.score)
# print(bart._Student__name) #不建议的做法