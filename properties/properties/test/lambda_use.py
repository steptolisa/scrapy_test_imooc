# coding:utf-8
# python 3.6

__author__ = 'dht'
__creattm = '20181205'
__usefor__ = ''


add = lambda x, y: x+y
print(add(1, 2))
# 3

# map

# 我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# Iterator是惰性序列
f = map(lambda x: x**2, [1, 2, 3, 4])
print(f)
# <map object at 0x0000022E9F005B38>
print(list(f))
# [1, 4, 9, 16]

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# __doc__
# reduce

from functools import reduce

DIGITS = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8' : 8, '9' : 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def add(x, y):
    return x + y
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
print(reduce(add, [1, 3, 5, 7, 9]))
# 25

# filter

# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7])))
# [1, 3, 5, 7]

print(list(filter(lambda x:True if x % 3 == 0 else False, range(100))))
# [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

print(list(map(lambda x: 1 if x == 'a' else 2 if x == 'b' else 3, ['a', 'b', 'c'])))
# [1, 2, 3]
