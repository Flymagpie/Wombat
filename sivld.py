#!/usr/bin/python
# -*- coding: UTF-8 -*- 


def checkio(number):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    if (number % 3) and (number % 5) == True:
        return 'Fizz Buzz'
    elif number % 3 == 0:
        print ("Fizz, %d is divisible by 3", number)
    elif number % 5 == 0:
        print ("Buzz, %d is divisible by 5", number)
    else:
        print ("%d, %d is not divisible by 3 or 5", number, number)
    #replace this for solution
    return str(number)

#Some hints:
#Convert a number in the string with str(n)

#These "asserts" using only for self-checking and not necessary for auto-testing
checkio(15)
checkio(6)
checkio(10)
checkio(7)
