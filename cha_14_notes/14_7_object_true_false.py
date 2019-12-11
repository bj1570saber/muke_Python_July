class Test():
    pass

test = Test()
if test: # True
    print('S')

print('Test_2:~~~')

class Test_2():
    def __len__(self):
        return 0 # if programer does not rewrite this function.
                 # default return greater than 0 integer -> True.

test_2 = Test_2()
if test_2: # False
    print('S')
else:
    print('F')

print('Test_3():~~~')
class Test_3():
    def __bool__(self): # if programer does not rewrite this function.
        return False    # default return True.

test_3 = Test_3()
if test_3: # False
    print('S')
else:
    print('F')

print(bool(None))
print(bool([]))
print(bool(test))#True
print(bool(test_2))
print(bool(test_3))

