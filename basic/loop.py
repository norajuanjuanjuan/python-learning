# -*- coding : utf-8 -*-
#for in
#高斯算出来的5050
sum=0
for x in range(101):
    sum=sum+x;
print(sum)

#计算100以内的所有奇数之和
sum=0
n=99
while n>0:
    sum=sum+n
    n = n - 2
print('奇数之和为：',sum)

#练习
L=['Bart','Lisa','Adam']
for name in L:
    print('Hello,',name)

#break
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('End')

#continue
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)		