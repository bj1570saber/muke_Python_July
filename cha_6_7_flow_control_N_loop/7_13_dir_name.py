import sys,c7
print(dir(sys)) # dir() retrieves variables list from parameter module.
print("\nc7.py: "+ str(dir(c7)))

# How to use __name__
if __name__ =='__main__':
    print('This is an app.') # This line will not print, if another .py file import this module.
print("This is a module.")