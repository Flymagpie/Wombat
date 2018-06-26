def func():
    x = 2
    b = 555
    print ('x is',x,b)
    x= 54
    print ('Changed local x to',x)
    b = 33
    
    if __name__ == '__main__':
        print ('x is still',x,b)

