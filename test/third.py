# _*_coding:utf-8_*_
# __author__='Nora'
classmates = ['Nora', 'Mike', 'Mark']
print len(classmates)
print classmates[0]
print classmates[len(classmates) - 1]
classmates.append('Adam')
print classmates[len(classmates) - 1]
classmates.insert(3, 'Harry')
print classmates[3]
classmates.pop(3)
print classmates[len(classmates) - 1]
classmates.pop()
classmates[len(classmates) - 1]

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print L[0][0]
print L[1][1]
print L[2][2]

height = 1.52
weight = 52
BMI = weight / (height * height)
if 18.5 >= BMI:
    print 'too light'
elif 18.5 < BMI and 25 >= BMI:
    print 'normal'
elif 25 < BMI and 28 >= BMI:
    print 'too heavy'
elif 28 < BMI and 32 >= BMI:
    print 'fat'
elif 32 < BMI:
    print 'heavily fat'

for li in L:
    print li

sum = 0
for x in list(range(101)):
    sum = sum + x
print sum

sum2=0
n=99
while n>0:
    sum2=sum2+n
    n=n-2
print sum2

myList=['Bart','Lisa','Adam']
for li in myList:
    print 'Hello %s !' % li

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']
d['Michael']=80
print d['Michael']

print 'Nora' in d
print d.get('Nora')

print d['Bob']
d.pop('Bob')
print d

s=set([1,2,3,1,3,4])
print s

a=['a','c','d','b']
print a
a.sort()
print a

s=set((1,3))
print s

#s=set(([1,4],[2,3]))
#print s