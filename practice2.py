#!/usr/bin/python
# -*- coding: UTF-8 -*- 

#
# L = ['Hello', 'World', 18, 'Apple', None]
# print([s.lower() for s in L if isinstance(s , str)])

# -----------------------------------------生成器作业：杨辉三角（作弊）---------------------------------------
#
# def triangles(max):
#     n = 1
#     L = [1]
#     while n <= max:
#         yield L
#         L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]
#         n = n + 1
#     return 'done'
#
# for i in triangles(10):
#     print(i)

# -----------------------------------------生成器作业：杨辉三角（作弊）---------------------------------------

# from functools import reduce
#
# def accumulate(start,end,handle,sign):
#     t=map(lambda x:handle(x),range(start,end+1))
#     return  reduce(lambda x,y:eval('%s%s%s' %(x,sign,y)),t)
#
# def add(start,end,handle):
#     return accumulate(start,end,handle,'+')
#
# def product(start,end,handle):
#     return accumulate(start,end,handle,'*')
#
# def handle(n):
#     return n**3
#
# print(add(1,5,handle))


# -------------------------------------------map/reduce函数--------------------------------------

#使用map将字符串首字母大写其他字母小写
#
# def normalize(name):
#     return name[:1].upper() + name[1:].lower()
#
# L1 = ['adam', 'LISA', 'barT', 'wombat']
# L2 = list(map(normalize, L1))
# print(L2)
#
#
# #利用reduce求积
# from functools import reduce
#
# def prod(L):
#     def multiply(x, y):
#         return x * y
#     return reduce(multiply, L)
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
#
# # 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# from functools import reduce
# import math
#
# def str2float(s):
#     n = 0
#     for i in s:
#         if i == '.':
#             break
#         n += 1
#     s = s.replace('.', '')
#
#     def fn(x, y):
#         return x * 10 + y
#
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
#     return reduce(fn, map(char2num, s))/pow(10, n)
#
# print('str2float(\'123.456\') =', str2float('123.456'))

#-------------------------------------------filter------------------------------------------

#使用filter过滤掉非回数，留下回数

def is_palindrome(n):
    pass



# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))

