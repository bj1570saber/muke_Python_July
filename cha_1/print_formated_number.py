print('100 + 200 = ',100+200)

print('%02d-%02d' % (3, 1))# 03-01
print('%2d-%2.2d' % (3, 1))# 3-01
print('%07.2f' % 3.1415926)#0003.14  total length-> 7 including '.'

addr = '123@163.com121212122'
print(addr.strip('123'))#@163.com front and end letter can not be 1 or 2 or 3 

dict = {'Name': 'Zara', 'Age': 7}
print( "Value : %s" %  dict.setdefault('Age', None))#Value : 7
print ("Value : %s" %  dict.setdefault('Sex', None))#Value : None
print(dict.get('Name')+' love Python')#Zara love Python
print(dict)#{'Name': 'Zara', 'Age': 7, 'Sex': None}