'''
\n :next line
\' :'
\t :
\r :
'''
print('Hello\tWorld.') #Hello   World.
print('This is Hello\rWorld.') #World.s Hello
print('Hello\\nWorld.')# Hello\nWorld.
print('~'*20)
# Raw string print:
print('Hello\\nWorld.')# Hello\nWorld.
print(r'Hello\nWorld.') # Hello\nWorld.   raw make \ escape charactor invalid.
print(R'C:\Hello\nWorld.') # C:\Hello\nWorld.  raw make \ escape charactor invalid.
#causion:
#print(r'Let's go.') # there are 3 ' raw string does not works.


