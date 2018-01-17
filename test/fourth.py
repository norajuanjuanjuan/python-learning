#_*_coding:utf-8_*_
#__author__='Nora'
n1 = 255
n2 = 1000
print hex(n1)

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

print my_abs(-19)
#print my_abs('A')

import math

def move(x,y,step,angle=0):
    nx = x +step*math.cos(angle)
    ny=y+step* math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print (x,y)

def quadratic(a,b,c):
    delta=math.sqrt(b*b-4*a*c)
    x1=(-b+delta)/(2*a)
    x2=(-b-delta)/(2*a)
    return x1,x2
print (quadratic(2,3,1))
print (quadratic(1,3,-4))

def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)

args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)

def person(name, age, *args, **kw):
    print(name, age, args, kw)

person('Jack',24,city='Beijing',job='Engineer')

#recursion
#def fact(n):
    #if n==1:
        #return 1
   # return n * fact(n-1)

#print fact(5)

def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)

print fact(5)


def move(n,a,b,c):
    if n==1:
        print(a,'->',c)
        return
    move(n-1,a,c,b)
    move(1,a,b,c)
    move(n-1,b,a,c)

move(3,'a','b','c')
