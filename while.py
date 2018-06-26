from random import randint

number = randint(1,100)
guess = 0
while number != guess:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print ('Comgratulations,you guessed it!It is %d!'%guess)
        #running = False# this causes the while loop to stop
    elif guess < number:
        print ('No,%d is lower than that number'%guess)
    else:
        print ("No, %d is higher than that number"%guess)
else:
    print ('The while loop is over.')# Do anything else you want to do herent
print ('Done')

