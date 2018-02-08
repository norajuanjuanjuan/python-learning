# _*_coding:utf-8_*_
# __author__='Nora'
# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != j) and (i != k) and (j != k):
#                 print i, j, k
# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
# 　　　于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
# 　　　成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
# 　　　40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
# 　　　100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# bonus1 = 100000 * 0.1
# bonus2 = bonus1 + 100000 * 0.075
# bonus4 = bonus2 + 200000 * 0.05
# bonus6 = bonus4 + 200000 * 0.03
# bonus10 = bonus6 + 400000 * 0.015
# i = int(raw_input('input gain:\n'))
# if i <= 100000:
#     bonus = i * 0.1
# # elif 100000 < i <= 200000:
# elif i <= 200000:
#     bonus = bonus1 + (i - 100000) * 0.075
# # elif 200000 < i <= 400000:
# elif i <= 400000:
#     bonus = bonus2 + (i - 200000) * 0.05
# # elif 400000 < i <= 600000:
# elif i <= 600000:
#     bonus = bonus4 + (i - 400000) * 0.03
# # elif 600000 < i <= 1000000:
# elif i <= 1000000:
#     bonus = bonus6 + (i - 600000) * 0.015
# # elif i > 1000000:
# else:
#     bonus = bonus10 + (i - 1000000) * 0.01
# print 'bonus = ', bonus

# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# import math
# for i in range(100000):
#     x = int(math.sqrt(i+100))
#     y = int(math.sqrt(i+268))
#     if(x*x == i + 100) and (y * y == i + 268):
#         print i

# # 题目：输入某年某月某日，判断这一天是这一年的第几天？
# year = int(raw_input('year : \n'))
# month = int(raw_input('month : \n'))
# day = int(raw_input('day : \n'))
# # sum days each first day of month
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# sum = 0
# if 0 <= month <= 12:
#     sum = months[month-1]
# else:
#     print "data error!"
# sum += day
# leap = 0
# if(leap % 400 ==0) and (leap % 4 == 0) and (leap % 100 != 0):
#     leap = 1
# if(leap == 1) and (month == 2):
#     sum += 1
# print "it is the %d th day of year %d" % (sum , year)

# # 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# # the solution below is awesome
# l = []
# for i in range(3):
#     x = int(raw_input("integer: \n"))
#     l.append(x)
# l.sort()
# print l

# # 题目：用*号输出字母C的图案。
# print 'Hello Python world!\n'
# print '*' * 10
# for i in range(5):
#     print '*        '
# print '*' * 10

# # 题目：输出特殊图案，请在c环境中运行，看一看，Very Beautiful!
# a = 176
# b = 219
# print chr(b),chr(a),chr(a),chr(a),chr(b)
# print chr(a),chr(b),chr(a),chr(b),chr(a)
# print chr(a),chr(a),chr(b),chr(a),chr(a)
# print chr(a),chr(b),chr(a),chr(b),chr(a)
# print chr(b),chr(a),chr(a),chr(a),chr(b)
#
# 题目：输出9*9口诀。
# for i in range(1, 10):
#     for j in range(1,10):
#         if (j <= i):
#             result = i * j
#             print ('%d * %d = %d ' % (i, j, result)),
#     print ""
# python 2.7 print last comma can cause non \r\n


# # 题目：要求输出国际象棋棋盘。
# # import sys
# for i in range(8):
#     for j in range(8):
#         if(i+j) % 2==0:
#             print('W'),
#             # print(),
#         else:
#             print(' '),
#     print ''
#
# # 打印楼梯，同时在楼梯上方打印两个笑脸。
# import sys
# sys.stdout.write(chr(1))
# sys.stdout.write(chr(1))
# print ''
#
# for i in range(1,11):
#     for j in range(1,i):
#         sys.stdout.write(chr(219))
#         sys.stdout.write(chr(219))
#     print ''

# import sys
# import time
# for i in xrange(10):
#     for ch in '-\\|/':
#         print '%-20s%s\r' % ('waiting..',ch)
#         sys.stdout.flush()
#         time.sleep(0.2)

#


