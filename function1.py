def printMax(a,b):
    if a>b:
        print (a,'is maximum')
    elif a<b:
        print (b,'is maximum')
    else:
        print ('holy same!')

x = eval(input('plz enter a number:'))
y = eval(input('plz enter another number:'))
print (x)
print (type (x))
print (y)
print (type (y))
printMax(x,y)
