class Student(object):
    def __init__(self, name,score):
        self.__name=name
        self.__score=score

    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))
    
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name=name

    def set_score(self,score):
        self.__score=score

#>>> s1=Student('Nora',87)
#>>> s1.print_score()
#Nora:87
#>>> s1.get_name()
#'Nora'
#>>> s1.get_score()
#87
#>>> s1.__name='noras'
#>>> s1.__name
#'noras'
#>>> s1.get_name()
#'Nora'
#>>> s1._Student__name
#'Nora'


class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')

class Cat(Animal):
    def run(self):
        print('Cat is running')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly')

def run_twice(Animal):
    Animal.run()

#>>> animal=Animal()
#>>> dog=Dog()
#>>> cat=Cat()
#>>> tortoise=Tortoise()
#>>> run_twice(animal)
#Animal is running
#>>> run_twice(dog)
#Dog is running
#>>> run_twice(cat)
#Cat is running
#>>> run_twice(tortoise)
#Tortoise is running slowly

class Timer(object):
    def run(self):
        print('Starting ......')
#>>> run_twice(Timer())
#Starting ......


#>>> type(123)==type(456)
#True
#>>> type(dog)
#<class '__main__.Dog'>
#>>> def fn():
#...     pass
#... 
#>>> type(fn)==types.FunctionType
#True

#>>> class MyObject(object):
#...     def __init__(self):
#...         self.x=9
#...     def power(self):
#...         return self.x*self.x
#... 
#>>> obj=MyObject()
#>>> hasattr(obj,'x')
#True
#>>> hasattr(obj,'y')
#False
#>>> setattr(obj,'y',19)
#>>> getattr(obj,'y')
#19
#>>> fn=getattr(obj,'power')
#>>> fn()
#81