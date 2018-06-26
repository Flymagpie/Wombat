# ab is short for address book
ab = {'Swaroop':'swaroopch@byteofpython.info',
      'larry':'larry@wall.org',
      'Matsumoto':'matz@ruby-lang.org',
      'Spammer':'spammer@hotmail.com'
    }

print ("Swaroop's address is %s" % ab['Swaroop'])

# adding a key/value pair
ab['Guido'] = 'guido@python.org'

# deleting a key/value pair
del ab['Spammer']

print('\nThere are %d contacts in the address-book \n' %len(ab))
for name,address in ab.items():
    print('Contact %s at %s' % (name, address))

if 'Guido' in ab:  # OR ab.has_key('Guido')
    print("\nGuido's address is %s" % ab['Guido'])
