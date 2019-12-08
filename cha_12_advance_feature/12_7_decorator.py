import time

def f1():
    print('This is f1')

def f2():
    print('This is f2')

# The unix time stamp is a way to track time as a running total of seconds. 
# This count starts at the Unix Epoch on January 1st, 1970 at UTC. 
t1 = time.time()
f1()
print('Time consume: %f seconds' %(time.time() - t1)) # print out running time of a function.
# 修改是封闭的，扩展是开放的
print('~')

def print_current_time(func): # 业务需要每个function都需要打印时间
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)