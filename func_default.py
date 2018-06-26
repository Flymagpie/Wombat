#!/Library/Frameworks/Python.framework/Versions/3.6/python
#Filename:func_default.py

def say(message,times=1,times2=3,ti2=2):
    print (message*times*times2*ti2)
say('hello',2,2)

def func(a,b=5,c=10):
    print ('a is',a,'b is',b,'c is',c)

func(3,7)
func(25,c=24)
func(c=50,a=100)

print ('--------------Parting line-------------------')
def maximum(x,y):
    if x > y:
        return x
    elif y > x:
        return y
    

print (maximum(3,5))

print ('--------------Parting line-------------------')

def printMax(x,y):
    '''Prints the maximum of two numbers
    The tow values must be integers.'''
    x = int(x) #convert to integers,if possible
    y = int(y)

    if x > y:
        print (x,'is maximum')
    else:
        print (y,'is maximum')

printMax(3,5)
print (printMax.__doc__)
help(printMax)






