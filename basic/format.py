#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('ABC'.encode('ascii'),
'中文'.encode('utf-8'),
b'ABC'.decode('ascii'),
len('ABC'),
len('中文'),
len('中文'.encode('utf-8')))
print('中文测试正常')

# 格式化
print('%2d-%02d' % (3,1))
print('%.2f' % 3.1415926)
print('growth rate is %d %%' % 7)
s1=72
s2=85
r=((85-72)/72)*100
print('%.1f %%' % r)