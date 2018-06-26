#!/usr/bin/python
#-*- coding: UTF-8 -*- 
import os
import time

#1. 需要备份的文件和目录由一个列表指定
source = ['/Users/timi/PycharmProjects/practice','/Users/timi/wish/sku']


#2. 备份应该保存在主备份目录中
target_dir = '/Users/timi/PycharmProjects/back_up/'  #这是备份保存的目录


#3. 文件备份成一个zip文件
#4. zip存在的名称是当前的日期和时间
target = target_dir + time.strftime('%y%m%d%h%m%s') + '.zip'


#5. 我们使用标准的zip命令，它通常默认地随Linux/Unix发行版提供，把文件放在一个zip文档里
zip_command = "zip -qr '%s' %s"%(target,' '.join(source))

#执行备份
if os.system(zip_command) == 0:
    print('备份成功',target)
else:
    print('备份失败')
