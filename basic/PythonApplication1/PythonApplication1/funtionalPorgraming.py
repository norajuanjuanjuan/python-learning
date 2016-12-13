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

# prime number
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)

for n in primes():
    if n<1000:
        print(n)
    else:
        break

def is_odd(n):
    return n % 2==1

list(filter(is_odd,range(1,15)))

def not_empty(s):
    return s and s.strip()
list(filter(not_empty,['A',' ','B','C ',None,'     ']))


#circuit number
def is_palindrome(n):
    return int(str(n)[::-1])==n
output = filter(is_palindrome,range(1,1000))
print(list(output))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower
L2=sorted(L,key=by_name)

def by_score(t):
    return t[1]

def count():
    fs=[]
    for i in range(1,4):
        fs.append(lambda i=i:i*i)
    return fs


# decorator
#>>> import functools
#>>> def log(func):
#...     @functools.wraps(func)
#...     def wrapper(*args,**kw):
#...         print('call %s ():' % func.__name__)
#...         return func(*args,**kw)
#...     return wrapper
#... 
#>>> @log
#... def now():
#...     print('2016-11-21')
#... 
#>>> now()
#call now ():
#2016-11-21
#>>> now.__name__
#'now'
#>>> 

#log with or without parameter in one function

#import functools
#>>> def log(text):
#...     def decorate(func):
#...         @functools.wraps(func)
#...         def wrapper(*args, **kw):
#...             output = text and ('%s %s()' % (text, func.__name__)) or ('call %s()' % func.__name__)
#...             print(output)
#...             return func(*args, **kw)
#...         return wrapper
#...     if hasattr(text,'__call__'):
#...         func = text
#...         text = None
#...         return decorate(func)
#...     else:
#...         return decorate
#... 
#>>> @log
#... def now():
#...     print('2016-11-21')
#... 
#>>> now()
#call now()
#2016-11-21
#>>> @log('execute')
#... def future():
#...     print('2016-11-22')
#... 
#>>> future()
#execute future()
#2016-11-22

