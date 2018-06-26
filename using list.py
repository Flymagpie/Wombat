#this is my shoppinglist
shoplist = ['apple','mango','carrot','banana']

print ('i have',len(shoplist),'items to purchase.')

print ('These items are:',end='')#Notice the comma at end of the line
for item in shoplist:
    print (item,end=' ')

print ('\nl also have to buy rice.')
shoplist.append('rice')
print ('My shopping list is now',shoplist)

print ('I will sort my list now')
shoplist.sort()
print ('Sorted shopping list is',shoplist)

print ('the first item i will buy is',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print ('i bought the',olditem)
print ('My shopping list is now',shoplist)
