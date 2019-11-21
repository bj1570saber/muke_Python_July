from package2.package4.m2 import m #this is absolute import. 
# main.py can not use relative import: .package2.package4.m2
print(m)
'''
Relative import: . same level; ..parent level; ...grand parent level; ......
It find out the __name__ as a start point to find the file need to be import.
However, main.py is special. When ran the program, main.py's __name__ will be 
change to __main__ which relative import can not locate this file.

Only way to use relative import in main.py: cd to main.py's parent level and 
python -m parentFolder.main   this will run main.py as a module. 
'''

# main.py is entry of the program. All module same level 
# with main.py can not be import by module in packages.
# It's out of top level package.
# Example: In this program, package1, package2 and package3
# are top level packages. Any packages need to be import,
# put them in lower level than main.py