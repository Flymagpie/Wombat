number = 59
guess = int(input('来来来，输个数（100以内）： '))
#guess = str(eval(input('Enter an integer : ')))

if guess == number:
    print ('Comgratulations,you guessed it!')
elif guess>number:
    print ('No,it is a little higher than that')
else:
    print ("No, it's a little lower than that")
print ('Done')
