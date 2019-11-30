import sys,c7
print('~'*20)
print(dir(sys)) # dir() retrieves variables list from parameter module.
print('~'*20)
print("\nc7.py: "+ str(dir(c7)))

# How to use __name__
if __name__ =='__main__':#!!!!!!
    print('This is an app.'+ __name__) 
    # This line will not print, if another .py file  import this module.
else:
    print("This is a module." + __name__)

#python code can run like this(from outside of package): 
# python3 -m packageName.filename #run as module file
# python3 packageName\fileName.py #run as program.

'''
A module allows you to logically organize your Python code. 
Grouping related code into a module makes the code easier to understand and use.
Simply, a module is a file consisting of Python code. 
A module can define functions, classes, variables, runnable code.
'''