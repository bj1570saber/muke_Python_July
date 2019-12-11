print('Test_4:~~~')
class Test_4():
    pass
    # def __len__(self):
    #     return 0 # if programer does not rewrite this function.
                 # len(Test_4()) will not work:

#print(len(Test_4)) # TypeError: object of type 'type' has no len() 

print('Test_5:~~~')
class Test_5():
    def __bool__(self): # this function has priority to return T/F
        return False 
    def __len__(self):
        return True
test_5 = Test_5()
if test_5:
    print('True')
else:
    print('False')