#_*_coding:utf-8_*_
#__author__='Nora'
#slice
L=['Nora','Sunny','Bob','Steve']
print L[0:3]
print L[:3]
print L[1:3]
print L[-1:]
print L[-2:]
print L[-2:-1]

Li = list(range(100))
print Li[:10]
print Li[-10:]
print Li[-10::2]
print Li[::5]
print L[:]

#Iterator
from collections import Iterable
print isinstance('abc',Iterable)

for i,value in enumerate(['A','B','C']):
    print (i,value)

#list generator
print [x*x for x in range(1,11)]
print [m+n for m in 'ABC' for n in 'XYZ']
import os
print [d for d in os.listdir('.')]

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k+'='+v for k,v in d.items()]

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L1 if isinstance(x,str)]