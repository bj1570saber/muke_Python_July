'''
ASCII, abbreviated from American Standard Code for Information Interchange
Unicode is a computing industry standard for the consistent encoding, 
                                representation, and handling of text
UTF-8 is a variable width character encoding

Hard drive save file as UTF-8, internet transfer UTF-8 coding save memory.
program displays(browser) or generates unicode.

对于单个字符的编码，Python提供了
ord()函数获取字符的整数表示;
chr()函数把编码转换为对应的字符;
'''
print(ord('A')) # 65
print(chr(65)) # A
print(chr(25991)) # 文
print('\u4e2d\u6587') # 中文
print('~')

'''
由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
如果要在网络上传输，或者保存到磁盘上，就需要把str变为以'字节'为单位的 bytes
Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，
但bytes的每个字符都只占用一个字节。
'''
x = b'ABC'
print(x)#b'ABC'
#以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：


print('Hello '+'World.')#Hello World.
print('Hello '* 3)#Hello Hello Hello
print('\nHello.'[0])
print('\nHello.'[1])#H
print('\nHello.'[2])#e
print('\nHello.'[3])#l
print('~~~')# () ????
print(type('Hello'))
print('\nHello.'[-1])#.
print('\nHello.'[-2])#o
print('\nHello.'[-3])#l
print('~~~~~')

print('Hello World\n'[1:3]) #el
print('Hello World\n'[0:-3])#Hello Wor
print('Hello World'[6:100]) #World
print('Hello World'[6:])    #World
print('Hello World'[-5:])   #World
print('Hello'[:-2])#Hel
print('Hello'[:-7])#
print('~~~~~~~~')

#以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
print('ABC'.encode('ascii'))# b'ABC'
print('中文'.encode('utf-8'))# b'\xe4\xb8\xad\xe6\x96\x87'
# print('中文'.encode('ascii')) # Error since ascii does not include chinese.
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

#要把bytes变为str，就需要用decode()方法：
print(b'ABC'.decode('ascii'))#ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))# 中文

#Calculate length of string:
print(len('ABC'))# 3

#Calculate length of byte:
print(len(b'ABC')) # 3
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))# 6
print(len('中文'.encode('utf-8')))# 6
# Conclude: 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

print(b'ABC'.decode('utf-8'))
'''
在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8
编码对str和bytes进行转换。由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的
时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按
UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出
可能会有乱码。
必须并且要确保文本编辑器正在使用UTF-8 without BOM编码:
'''



