#>>> it = iter([1,2,3,4,5])
#>>> while True:
#...     try:
#...         x=next(it)
#...     except StopIteration:
#...         break
#... 
#>>> 
#>>> it = iter([1,2,3,4,5])
#>>> while True:
#...     try:
#...         x=next(it)
#...         print(x)
#...     except StopIteration:
#...         break
#... 
#1
#2
#3
#4
#5
#>>> f = abs
#>>> f
#<built-in function abs>
#>>> f(-10)
#10
#>>> def add(x,y,f)
#  File "<stdin>", line 1
#    def add(x,y,f)
#                 ^
#SyntaxError: invalid syntax
#>>> def add(x,y,f):
#...     return f(x)+f(y)
#... 
#>>> x=5
#>>> y=-6
#>>> f=abs
#>>> add(5,-6,abs)
#11
#>>> 
# def f(x):
#...     return x*x
#... 
#>>> r=map(f,range(1,10))
#>>> list(r)
#[1, 4, 9, 16, 25, 36, 49, 64, 81]
#>>> list(map(str,range(1,10)))
#['1', '2', '3', '4', '5', '6', '7', '8', '9']
#>>> from functools import reduce
#>>> def add(x,y):
#...     return x+y
#... 
#>>> reduce(add,for n in range(1,10))
#  File "<stdin>", line 1
#    reduce(add,for n in range(1,10))
#                 ^
#SyntaxError: invalid syntax
#>>> reduce(add,[x for x in range(1,10) if x/2 !=0 ])
#44
#>>> reduce(add,[x for x in range(1,10) if x%2 !=0])
#25
#>>> def fn(x,y):
#...     return x * 10 +y
#... 
#>>> 
#>>> reduce(fn,[1,3,5,7,9])
#13579
#>>> def nomalize(name):
#...     for char in name:
#...         name.lower()
#...     name[0].upper()
#... 
#>>> map(nomalize,['adam','LISA','barT'])
#[None, None, None]
#>>> def normalize(name):
#...     for char in name:
#...         char.lower()
#...     name[0].upper()
#...     return name
#... 
#>>> map(normalize,['adam','LISA','barT'])
#['adam', 'LISA', 'barT']
#>>> def nomalize(name):
#...     return name.capitalize()
#... 
#>>> map(normalize,['adam','LISA','barT'])
#['adam', 'LISA', 'barT']
#>>> list(map(normalize,['adam','LISA','barT']))
#['adam', 'LISA', 'barT']
#>>> print(list(map(normalize,['adam','LISA','barT'])))
#['adam', 'LISA', 'barT']
#>>> 'adam'.capitalize()
#'Adam'
#>>> def nomalize(name):
#...     return name.capitalize()
#... 
#>>> r=map(nomalize,['adam','LiSA','barT'])
#>>> print(list(r))
#['Adam', 'Lisa', 'Bart']

def f(x,y):
    return x*y+0
def prod(L):
    return reduce(f,L) 
prod([3,5,7,9])
