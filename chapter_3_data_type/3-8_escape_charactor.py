'''
\n :next line
\' :'
\t :
\r :
'''
print('Hello\tWorld.') 
print('Hello\rWorld.') #????
print('Hello\\nWorld.')
# Raw string print:
print('Hello\\nWorld.')
print(r'Hello\nWorld.') # raw make \ escape charactor invalid.
print(R'C:\Hello\nWorld.') # raw make \ escape charactor invalid.
#causion:
#print(r'Let's go.') # raw string does not works.


