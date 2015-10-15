
#-*- coding: UTF-8 -*-


from sys import argv #导入

script, filename = argv #解包

txt = open(filename) #打开指定文件

print "Here's you file %r:" % filename #打印引导句，引用一个变量
print txt.read() #读打开的文件并打印出来

print "Type the filename again:"  # 打印引导句
file_again = raw_input(">") #输入文件名

txt_again = open(file_again) #打开输入的文件

print txt_again.read()  #读打开的文件并打开


close(txt)
close(txt_again)