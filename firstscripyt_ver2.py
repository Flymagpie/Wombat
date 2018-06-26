#!/usr/bin/python
#-*- coding: UTF-8 -*-
import os
import time

#1. 需要备份的文件和目录由一个列表指定
source = ['/Users/timi/PycharmProjects/practice','/Users/timi/wish/sku']


#2. 备份应该保存在主备份目录中
target_dir = '/Users/timi/PycharmProjects/back_up/'  #这是备份保存的目录


#3. 文件备份成一个zip文件
#4. 主目录下的子目录名称是当前的日期
today = target_dir + time.strftime('%y%m%d')
#zip文件名是当前时间
now = time.strftime('%h%m%s')
#让用户输入个备注写入文件名
comment = input('Enter a comment -->')
if len(comment) == 0:  #检查一下输入了没
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '(' + \
             comment.replace(' ','_') + ')' + '.zip'


#如果没有子目录则创建之
if not os.path.exists(today):
    os.mkdir(today)  #创建目录
    print('Successfully created directory',today)


#5. 我们使用标准的zip命令，它通常默认地随Linux/Unix发行版提供，把文件放在一个zip文档里
zip_command = "zip -qr '%s' %s"%(target,' '.join(source))

#执行备份
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')
