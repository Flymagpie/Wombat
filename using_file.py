#!/usr/bin/python
# -*- coding: UTF-8 -*-


poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python
'''

f = open('poem.txt', 'w')  # open fo 'w'riting
f.write(poem)  # write text to file
f.close()  # close the file


f = open('poem.txt')
# if no mode is specified,'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0:  # Zero length indicatesEOF
        break
    print(line, end='')
    # Notice comma to avoid automatic newline added by Python
f.close()  # close the file
