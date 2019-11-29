from init_folder import * #this import modules in init_folder
print(allowed_import.ai_1)
#print(not_allowed_import.nai_1) # error, __init__.py does not allowed to 
# import 'not_allowed_import'


#import sys
import init_folder # this import __init__
'''
If multiple .py modules need many common import modure.
please the import moduls in __init__.py
then import __init__.py to specific modules equals to import all modules 
that __init__.py contains. save many lines of import in many module files
'''
# __init__.py also allow easy import for every modure.
print(init_folder.sys.path)