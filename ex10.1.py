#-*- coding: UTF-8 -*-

#区分格式符%r和%s的区别，%r显示输入的内容，%s显示应该看到的内容，比如应该换行\n。

a = "my name is %r."
b = 'my name is %s.'


print a % "my\neric"
print b % "my\neric"