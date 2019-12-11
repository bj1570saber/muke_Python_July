print('Test_4:~~~')
class Test_4():
    pass
    # def __len__(self):
    #     return 0 # if programer does not rewrite this function.
                 # len(Test_4()) will not work:

#print(len(Test_4)) # TypeError: object of type 'type' has no len() 

print('Test_5:__bool__() priority')
class Test_5():
    def __bool__(self): # this function has priority to return T/F
        print('bool called.')
        return False 

    def __len__(self):
        print('len called.')
        return True
test_5 = Test_5()
if test_5:
    print('True')
else:
    print('False')
# bool called.
# False


print('Test_6: __bool__() return type')
class Test_6():
    def __bool__(self): # this function has priority to return T/F
        return 0 
    def __len__(self):
        return True
test_6 = Test_6()
# if test_6:#TypeError: __bool__ should return bool, returned int
#     print('True')
# else:
#     print('False')