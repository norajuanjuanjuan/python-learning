# _*_coding:utf-8_*_
# __author__='Nora'
a = 100
if (100 <= a):
    print (a)
else:
    print (-a)
print(True and False)

a = "ABC"
b = a
a = "XYZ"
print(b)

print (9/3)
print (9//3)

my = ord('刘')
print my
print chr(66)

print (len('ABC'))

print len('中文'.encode('utf-8'))

print 'Hello,%s' % "world"

print '%d-%02d' % (3,1)
print '%.2f' % 3.1415

print 'growth rate: %d %%' %7

s1=72
s2=85
r=(s2-s1)/(s1*1.0)
print 'Growth rate is %.1f %%' % r