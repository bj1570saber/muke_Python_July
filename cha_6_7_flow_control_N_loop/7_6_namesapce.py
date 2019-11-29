import c7
import new.c1 as c1

# namespace: the module's path.
# 'Python package' must includes a __init__.py files. It can be empty or not. 
# import __init__.py : just need to import the package name.

print(c7.c)
#print(new.c1.c) # longer typing version when just import "new"
print(c1.c)# shorter module path name use keyword 'as' (line 2)