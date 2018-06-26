#! /usr/bin/python
# Filename:using_sys.py

import sys
import copy

print ('THe command line arguments are:')
for i in sys.argv:
    print (i)
for m in sys.path:
    print (m)

print ('\n\nThePYTHONPATH is',sys.path,'\n')


x = 5
y = 'dfsf'
print (type (y))
print (type (x))

y = copy.copy(x)
print (x,y)

print (type (y))
print (type (x))


