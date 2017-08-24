#coding=utf-8

from book1 import funTest

funTest("zhangsan",18)

try:
    with open('text.txt') as file:
        contents = file.read()
        print contents
except IOError:
    print 'error'

file_name = 'programming.txt'
with open(file_name,'a') as file_obj:
    file_obj.write('I love programming!\n')
    file_obj.write('I love python!\n')