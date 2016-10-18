# -*- coding: utf-8 -*- 
'''
age=6
if age>=18:
	print('adult')
elif age>=6:
    print('teenager')
else:
    print('kid')

s=input('birth:')
birth=int(s)
if birth<2000:
    print('00前')
else:
    print('00后')
'''

# 练习
# -*- coding: utf-8 -*-
h=input("height is:")
height=float(h)
w=input("weight is:")
weight=float(w)
bmi=weight/(height**2)
if bmi < 18.5:
    print('Too lenient')
elif 18.5 <= bmi <25:
    print('normal')
elif 25 <= bmi <28:
    print('overweight')
elif 28 <= bmi <32:
    print('fat')
else:
    print('Severe obesity')