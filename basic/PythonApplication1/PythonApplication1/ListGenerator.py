#>>> list(range(1,11))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#>>> L=[]
#>>> for x in range(1,11):
#...     L.append(x*x)
#... 
#>>> L
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#>>> [x*x for x in range(1,11)]
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#>>> [x*x for x in range(1,11) if x%2==0]
#[4, 16, 36, 64, 100]
#>>> [m+n for m in 'ABC' for n in 'XYZ']
#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
#>>> import os
#>>> [d for d in os.listdir('.')]
#['Iteration.py', 'ListGenerator.py', 'PythonApplication1.py', 'PythonApplication1.pyproj']
#>>> d ={'x'£º'A','y':'B','z':'C'}
#  File "<stdin>", line 1
#    d ={'x'???'A','y':'B','z':'C'}
#           ^
#SyntaxError: invalid syntax
#>>> d={'x':'A','y':'B'}
#>>> [k+'='+v for k£¬v in d.items()]
#  File "<stdin>", line 1
#    [k+'='+v for k???v in d.items()]
#                  ^
#SyntaxError: invalid syntax
#>>> [k+'='+v for k,v in d.items()]
#['y=B', 'x=A']
#>>>  L = ['Hello', 'World', 'IBM', 'Apple']
#  File "<stdin>", line 1
#    L = ['Hello', 'World', 'IBM', 'Apple']
#    ^
#IndentationError: unexpected indent
#>>> L = ['Hello', 'World', 'IBM', 'Apple']
#>>> [s.lower() for s in L]
#['hello', 'world', 'ibm', 'apple']
#>>> L=['Hello', 'World', 18, 'Apple', None]
#>>> [s.lower() for s in L if isinstance(s,str)]
#['hello', 'world', 'apple']
#>>> L1=[]
#>>> for n in L:
#...     if isinstance(n,str)==True:
#...         m=n.lower()
#...         L1.append(m)
#...     else:
#...         L1.append(n)
#...    
#>>> L1
#['hello', 'world', 18, 'apple', None]
##>>> 