'''
https://www.liaoxuefeng.com/wiki/1016959663602400/1017063826246112
同一个变量可以反复赋值，而且可以是不同类型的变量，这种变量本身类型不固定的语言称之为动态语言，
与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。
例如Java是静态语言.

a = 'ABC' 时，Python解释器干了两件事情：
1.在内存中创建了一个'ABC'的字符串；
2.在内存中创建了一个名为a的变量，并把它指向'ABC'。

也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，
例如下面的代码：
'''
a = 'ABC'
b = a
a = 'XYZ'
print(b)#ABC

