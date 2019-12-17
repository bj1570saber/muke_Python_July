print("Let's go.")#Let's go.
# or
print('Let\'s go.')#Let's go.
print('I\'m \"OK\"')#I'm "OK"
print('''
Hello
World
''')

print("""
I
am
Jerry
""")

print('hello \
world.')# output: hello world. Above line can not comment or any space. 
# " \ + returnKey " allow the code to be continue in next line

print(1+2\
    +3)#6  #returnKey, no space after it.

#print raw string: with - r
print(r'I like \n')#I like \n

#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('Age: %s. Gender: %s' % (25, True))# Age: 25. Gender: True

#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print('growth rate: %d %%' % 7)# growth rate: 7 %

# format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}
#'Hello, 小明, 成绩提升了 17.1%'
print('Hello,{0},成绩提升了 {1:.1f}%'.format('小明',17.111))