class Student():
    sum = 0
    name = 'None'
    age = 0
    
    def __init__(self, name1, age1):
        self.name = name1 
        self.age = age1
        print('constructor of '+ self.name)

    @classmethod
    def plus_sum(cls):
        cls.sum += 1 
        print("Total number of students:" + str(cls.sum))
        print("cls.sum: " + str(cls.sum))# can access Class field.
        print("cls.name: " + cls.name)#this print Studnet.name; 
        # can not access object field.

    @staticmethod
    def get_sum():# no self or cls parameter
        print('Static method get_sum: ' + str(Student.sum))# access class field
        #print(self.name)# can not access object field.

student1 = Student("Jerry", 20)
student1.plus_sum()# invoke class method by object
Student.plus_sum()# invoke class  method by Class
student1.get_sum()# invoke static method by object
Student.get_sum()# invoke static method by Class

# output:
# constructor of Jerry
# Total number of students:1
# cls.sum: 1
# cls.name: None
# Total number of students:2
# cls.sum: 2
# cls.name: None
# Static method get_sum: 2
# Static method get_sum: 2