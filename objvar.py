#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Person:
    '''Represents a person'''

    population = 0

    def __init__(self, name):
        '''Initializes the person's data'''
        self.name = name
        print('(Initializing %s)' % self.name)

        # When this person is created,he/she
        # adds to the population
        Person.population += 1

    def __del__(self):
        '''i am dying'''
        print('%s says bye.' % self.name)

        Person.population -= 1

        if Person.population == 0:
            print('I am the last one.')
        else:
            print('There are still %d people left' % Person.population)

    def sayHi(self):
        '''Greeting by the person
        Realy,that' all it does.'''
        print('Hi,my name is %s.' % self.name)

    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print('I am the only person here')
        else:
            print('We have %d personshere' % Person.population)


swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

jason = Person('jason')
jason.sayHi()
jason.howMany()

swaroop.sayHi()
swaroop.howMany()
