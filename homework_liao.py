#!/usr/bin/python
# -*- coding: UTF-8 -*- 

# ----------------------字符串的练习题----------------------
#
# s1 = 72
# s2 = 85
#
# r = (s2 - s1) / s1 * 100
# print('小明的成绩较去年提升了%.1f%%' % r)
#
# -----------------------list&tuple------------------------
#
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Lisa:
# print(L[-1][-1])


#-----------------------条件判断-----------------------------
#
# height = float(input('输一下你的身高（M）:'))
# weight = float(input('请输入你的体重（KG）:'))
# bmi = weight/(height**2)
#
# if bmi < 18.5:
#     print('你的BMI值为%.1f,瘦死了！' % bmi)
# elif bmi < 25:
#     print('你的BMI值为%.1f,完美！' % bmi)
# elif bmi < 28:
#     print('你的BMI值为%.1f,有点肥！' % bmi)
# elif bmi < 32:
#     print('你的BMI值为%.1f,死胖子一个！' % bmi)
# else:
#     print('你的BMI值为%.1f,肥成狗了，别活了！' % bmi)
#
#-------------------------循环------------------------------
#
# L = ['Bart', 'Lisa', 'Adam']
#
# for name in L:
#     print('Hello,%s' % name)
#
#-----------------------使用dict和set-----------------------
#
# d = {'jason': 94 , 'amy': 95 , 'adm': 99 , (1,2,3): 100 , (1,[2,3]): 110}
#
# print(d[(1,2,3)])
# print(d['amy'])
# print(d[(1,[2,3])])


# ------------------------函数=============================
#
# n1 = 255
# n2 = 1000
#
# print(hex(n1),hex(n2))
#
# # abs()
# import math
#
# # 求一元二次方程的根
# def quadratic(a , b , c):
#     if a == 0:
#         return 'a不能为0'
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         return '无解'
#     if delta >= 0:
#         return ((-b+(math.sqrt(delta))) / (2 * a)) , ((-b-(math.sqrt(delta))) / (2 * a))
#
# print(quadratic(2, 3, 1))
# print(quadratic(1, 3, -4))
#
#-----------------------------递归函数-----------------------------

#
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
#
# print(fact(1000))

# 尾递归优化
#
# def fact(n):
#     return fact_iter(n, 1)
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
#
# print(fact(5))

# 汉诺塔递归
#
# B=[]  #设置操作过程列表
#
#
# def move(n, a, b, c):
#     if n==1:
#         step=a+str(n)+'-->'+c+str(n)  #一个圆盘需要从A到C操作步骤
#         B.append(step) #向列表中添加操作步骤
#         return
#     move(n-1,a,c,b)  #将A柱的n-1个盘移到B柱
#     step=a+str(n)+'-->'+c+str(n)  #将A柱的第n个盘移到C柱操作步骤
#     B.append(step)  #向列表中添加操作步骤
#     move(n-1,b,a,c)  #将过渡柱子B上n-1个圆盘移动到目标柱子C
#
#
# move(int(input('请输入盘子数：')),'A','B','C')  #输入盘子数
# print('共需操作'+str(len(B))+'次','操作过程为:\n',B)  #打印操作数和操作步骤

# --------------------------------切片-----------------------------
#
# L=list(range(10))
# L[::2]=[-i for i in L[::2]]
# print(L,"with len=",len(L))

L = list(range(100))

print(L[::-5])
print(L[-1])