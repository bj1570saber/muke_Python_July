class Test():
    pass

test = Test()
if test: # True
    print('S')

class Test_2():
    def __len__(self):
        return 0

test_2 = Test_2()
if test_2: # False
    print('S')
else:
    print('F')

print('~')
print(bool(None))
print(bool([]))
print(bool(test))
print(bool(test_2))
