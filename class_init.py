#!/usr/bin/python
#-*- coding: UTF-8 -*-
class Person:
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print('Hello,my name is',self.name)

p = Person('Swaroop')
p.sayHi()

Person('Jason').sayHi() #let me try this

p.sayHi()

s = Person('slash')

s.sayHi()