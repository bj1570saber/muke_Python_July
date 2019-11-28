print('-1:%s ' %(type(-1)))
n = 2
print('n:%s ' %(type(n)))
m = 3.14
print('m:%s ' %(type(m)))
print('1.111111111111111111111111111111111111:%s ' %(type(1.111111111111111111111111111111111111)))
print('1+1 = %d :%s' %(1+1,type(1+1)))
print('1+1.0 = %.2f :%s' %(1+1.0,type(1+1.0)))
print('1*1 = %d :%s' %(1*1,type(1*1)))
print('1*1.0 = %f :%s' %(1*1.0,type(1*1.0)))
print('~'*20)
print('3/2 = %f :%s' %(3/2, type(3/2))) # 3/2 = 1.000000:<type 'int'>
print('3/1 = %d :%s' %(3/1, type(3/1))) # 3/1 = 3:<type 'int'>
print('1/2 = %d :%s' %(1/2, type(1/2))) # 1/2 = 0:<type 'int'>
print('~'*20)
# / operator output: float
print('3.0/2 = %f :%s' %(3.0/2, type(3.0/2))) # 3.0/2 = 1.500000:<type 'float'>
print('3.0/1 = %f :%s' %(3.0/1, type(3.0/1))) # 3.0/1 = 3.000000:<type 'float'>
print('1.0/2 = %f :%s' %(1.0/2, type(1.0/2))) # 1.0/2 = 0.500000:<type 'float'>
print('~'* 20)
# // operator output: int
print('1//1 = %d :%s' %(1//1, type(1//1))) # 1//1 = 1:<type 'int'>
print('3//2 = %f :%s' %(3//2, type(3//2))) # 3//2 = 1.000000:<type 'int'>
print('1//2 = %d :%s' %(1//2, type(1//2))) # 1//2 = 0:<type 'int'>

