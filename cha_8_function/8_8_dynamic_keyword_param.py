def squsum(*param):
    sum = 0
    for i in param:
        sum += i*i
    print(sum)
print('~')
squsum(1,2,3,4,5,6)# 91
print('~' * 20)
# 可变关键字参数：
def city_temp(**param): # **param
    print(param)
    print(type(param))

city_temp(bj= '32c', xm='23c', sh='31')
#{'bj': '32c', 'xm': '23c', 'sh': '31'}
#<class 'dict'>

print('~' * 20)
# 可变关键字参数：
def city_temp(**param): # **param
    for key,value in param.items():
        print(key,':',value)

city_temp(bj= '32c', xm='23c', sh='31') 
# bj : 32c
# xm : 23c
# sh : 31
print('~' * 20)
a = {'bj': '32c', 'sh':'31c'}
city_temp(**a)
# bj : 32c
# sh : 31c
print('~' * 20)
city_temp() # empty is ok. print nothing

'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：

>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=extra['city'], job=extra['job'])
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

当然，上面复杂的调用可以用简化的写法：

>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
'''
