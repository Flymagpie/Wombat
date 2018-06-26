#!/usr/bin/python
# -*- coding: UTF-8 -*- 


from tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色
root.title('Wish Calculater')
root.geometry('640x480')
#                                 # 创建两个列表
# li     = ['C','python','php','html','SQL','java']
# movie  = ['CSS','jQuery','Bootstrap']
# listb  = Listbox(root)          #  创建两个列表组件
# listb2 = Listbox(root)
# for item in li:                 # 第一个小部件插入数据
#     listb.insert(0,item)
#
# for item in movie:              # 第二个小部件插入数据
#     listb2.insert(0,item)

#核心计算函数
def calcsales():
    p = float(price.get())
    w = float(weight.get())
    c = float(cost.get())
    sales['text'] =  float('%.2f' % (p*6.35*0.85*0.95))
    shipping['text'] = float('%.2f' % (w*0.09))
    profit['text'] = float('%.2f' % ((p*6.35*0.85*0.95)-(w*0.09)-c))

#定义一些组件

l1 = Label(text='输入售价$：')
price = Entry()


l2 = Label(text='输入成本￥：')
cost = Entry()

l3 = Label(text='输入重量g：')
weight = Entry()

l4 = Label(text='销售额')
sales = Label(text='--')

l5 = Label(text='运费')
shipping = Label(text='--')

l6 = Label(text='利润估算')
profit = Label(text='--')

b = Button(text="计算", command=calcsales)





# listb.pack()                    # 将小部件放置到主窗口中
# listb2.pack()

#下面把组件丢进去
l1.pack()
price.pack()

l2.pack()
cost.pack()

l3.pack()
weight.pack()



b.pack()


l4.pack()
sales.pack()

l5.pack()
shipping.pack()

l6.pack()
profit.pack()

root.mainloop()    # 进入消息循环