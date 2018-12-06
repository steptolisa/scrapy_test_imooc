# coding:utf-8
# python 3.6

__author__ = 'dht'
__creattm = ''
__usefor__ = ''


s = '2000001299000000012016120220180104020181129182324'

print(len(s))

t = '20180101'
import datetime

tdate = datetime.datetime.strptime(t, '%Y%m%d').date()
print(tdate)

print(datetime.datetime.now())
print(type(datetime.datetime.now()))

import time

# t1 = time.time()
t1 = time.mktime(time.localtime())
print(t1)
print(type(t1))

import time

dt = "2016-05-05 20:28:54"

#转换成时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
timestamp = time.mktime(timeArray)

print(timestamp)

x = (1, 2)

# tuple.__add__(tuple)
# (1) is not a tuple but (1,) is a tuple
z = x.__add__((3,))
print(z)
