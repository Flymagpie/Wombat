#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import types
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self, gender):
#         self.__gender = gender
# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')
#
# class nostu(object):
#     def get_gender(self):
#         return 'Yes,it is!'
#
# def test(Student):
#     print(Student.get_gender())
#
# test(nostu())
# print(type(bart))
#
# print(types.FunctionType == type(test))
#
# bat = Student('alpha','male')
#
# print('------------------华丽分割线-------------------')


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1




# 测试:
if Student.count != 0:
    print('测试失败1!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败2!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败3!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

print(Student.count)