print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist  #这只是另一个名称指向了同一个对象

del shoplist[0]

print('shoplist is',shoplist)
print('mylist is',mylist)
#标记出来shoplist和mylist都输出了相同的列表
#apple确认了他们指向同样的对象

print('Copy by making a full slice')
mylist = shoplist[:]  #make a copy by doing a full slice
del mylist[0]  #remove first item

print('shoplist is',shoplist)
print('mylist is',mylist)
#notice that now the two lists are differen