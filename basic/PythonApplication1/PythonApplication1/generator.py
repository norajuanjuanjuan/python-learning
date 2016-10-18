#>>> g=(x*x for x in range(10))
#>>> g
#<generator object <genexpr> at 0x023D7BC0>
#>>> next(g)
#0
#>>> next(g)
#1
#>>> next(g)
#4
#>>> next(g)
#9
#>>> next(g)
#16
#>>> next(g)
#25
#>>> next(g)
#36
#>>> next(g)
#49
#>>> next(g)
#64
#>>> next(g)
#81
#>>> next(g)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#StopIteration
#>>> g=(x*x for x in range(10))
#>>> for n in g:
#...     print(n)
#... 
#0
#1
#4
#9
#16
#25
#36
#49
#64
#81

#>>> def fib(max):
#...     n,a,b=0,0,1
#...     while n<max:
#...         yield b
#...         a,b=b,a+b
#...         n=n+1
#... 
#>>> f=fib(6)
##>>> f
#<generator object fib at 0x023ED800>
#>>> for n in f:
#...     print n
#... 
#1
#1
#2
#3
#5
#8


#>>> def triangles():
#...     L = [1]
#...     while True:
#...         yield L
#...         L.append(0);
#...         L = [L[i-1] + L[i] for i in range(len(L))]
#... 
#>>> t=triangles()
#>>> t
#<generator object triangles at 0x02375080>
#>>> for n in t:
#...     print(t)
#...     n=n+1
#...     if n == 10:
#...         break
#... 
#<generator object triangles at 0x02375080>
#Traceback (most recent call last):
#  File "<stdin>", line 3, in <module>
#TypeError: can only concatenate list (not "int") to list
#>>> n=0
#>>> for t in triangles():
#...     print(t)
#...     n=n+1
#...     if n == 10:
#...         break
#... 
#[1]
#[1, 1]
#[1, 2, 1]
#[1, 3, 3, 1]
#[1, 4, 6, 4, 1]
#[1, 5, 10, 10, 5, 1]
#[1, 6, 15, 20, 15, 6, 1]
#[1, 7, 21, 35, 35, 21, 7, 1]
#[1, 8, 28, 56, 70, 56, 28, 8, 1]
#[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
#>>> 
