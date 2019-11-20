import c7
'''
# c7.py output:
name: c7
package: not belong to any package.
doc: No documentation.
file: /Volumes/Jetdrive_BZ/Study/Python/Learning_notes/Muke_July/cha_6_7_flow_control_N_loop/c7.py
'''
print('~' * 20)
print("7_12 codes: ")
print('\nname: '+ (__name__ or 'print name error.'))
print('package: '+(__package__ or 'not belong to any package.')) 
print('doc: '+ (__doc__ or 'No documentation.'))
print('file: '+ (__file__ or 'No file path.'))
'''
# 7_12 output:
name: __main__
package: not belong to any package.
doc: No documentation.
file: 7_12_difference_main_import.py #! this output will change 
                                        if run same python files from different
                                        directory, such upper level. It will be
                                        'new\7_12_difference_main_import.py'
'''
