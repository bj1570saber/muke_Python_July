
class Student():
    # class fields
    sum = 0
    name='null'
    age = 1
    # functions
    def __init__(self, name, age): # 'self' can be any words such as 'this'
        self.name = name # object field 'self.name'
        self.age = age # object field 'self.age'
        print('constructor of '+ self.name)
        # return None # only return None (default or explicit).

    def introduce(self):
        print('name: ' + self.name)
        print('age: '+ str(self.age))
    
    def do_homework(self):
        print("do_homework")

#test:
student1 = Student("Jerry", 2)
print(student1.name)
student1.introduce()
student1.do_homework()

# a = student1.__init__("Tom", 2)#return default None to a
# print(type(a))# <class 'NoneType'>
# print(a)# None
