from init_folder import * #this import modules in init_folder includes __init__.py
print(allowed_import.ai_1)
# print(not_allowed_import.nai_1) # error, __init__.py does not allowed to 
# import 'not_allowed_import'

#import sys
import init_folder # this import __init__ only.
#Since __init__.py has import in line 1. Codes inside it will not run again
'''
If multiple .py modules need many common import modure.
please the import moduls in __init__.py
then import __init__.py to specific modules equals to import all modules 
that __init__.py contains. save many lines of import in many module files
'''
# __init__.py also allow easy import for every module.
print(init_folder.sys.path)