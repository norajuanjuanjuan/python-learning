# -*- coding : utf-8 -*-
'''
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

#定义函数
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#调用函数	
p = (int)(input('please enter an interger:'))
print(my_abs(p))		

#返回多个值 其实就是一个tuple
import math
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x,y = move(75,75,60,math.pi / 6)
print(x,y)

#练习
def quadratic():
    a = (int)(input('please input a :'))
    if a==0:
        raise TypeError('bad operand',a)
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand',a)    
    b = (int)(input('please input b :'))
    if not isinstance(b,(int,float)):
        raise TypeError('bad operand',b)
    c = (int)(input('please input c :'))
    if not isinstance(c,(int,float)):
        raise TypeError('bad operand',c)
    Delta = b**2-4*a*c
    if Delta < 0:
        return print('此方程无实数解')
    elif Delta == 0:
        x1=(-b+math.sqrt(Delta))/(2*a)    
        return print('此方程只有一个解，\n x1=',x1)
    else:
        x1=(-b+math.sqrt(Delta))/(2*a) 
        x2=(b+math.sqrt(Delta))/(2*a)
        return print('此方程有两个解，\n x1=',x1,',x2=',x2)

quadratic()
'''
#函数的参数 没跑出结果；默认参数需指向不可变对象
def cal(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

cal(5,3)

#可变参数    