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


