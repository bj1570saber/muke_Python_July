print('%02d-%02d' % (3, 1))# 03-01
print('%2d-%2.2d' % (3, 1))# 3-01
print('%09.2f' % 3.1415926)#000003.14

addr = '123@163.com121212122'
print(addr.strip('12')) 

dict = {'Name': 'Zara', 'Age': 7}
print( "Value : %s" %  dict.setdefault('Age', None))
print ("Value : %s" %  dict.setdefault('Sex', None))
print(dict.get('Name')+' love Python')
print(dict)