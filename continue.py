i = True
while i:
    s = input('Enter something:')
    if s == 'quit':
        break
    if len(s)<5:
        continue
    print ('Input is of sufficient length')
    if len(s)>10:
        i = False
