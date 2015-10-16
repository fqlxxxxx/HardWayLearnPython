#-*- coding: UTF-8 -*-


from sys import argv

script, from_file, to_file = argv

input = open(from_file)
indata = input.read()


output = open(to_file, 'w')
output.write(indata)


print "已经将两个文档合并"