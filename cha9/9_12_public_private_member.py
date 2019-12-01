class Student():
    sum = 0
    #name = 'None'
    #age = 0
    
    def __init__(self, name_p, age_p):
        self.name = name_p 
        self.age = age_p
        self.score = 0
        print('constructor of '+ self.name)

    def marking(self, score_p):
        self.score = score_p
        print(self.name + '\'s score: ' + str(self.score))

    def do_homework(self):
        self.do_eng_homework#内部调用
        print(self.name +" is doing homework.")
    
    def do_eng_homework(self):
        print(self.name +" is doing homework.")

student1 = Student("Jerry", 20)
student1.do_homework()#外部调用
student1.marking(59)
# output:



    # @classmethod
    # def plus_sum(cls):
    #     cls.sum += 1 
    #     print("Total number of students:" + str(cls.sum))
    #     print("cls.sum: " + str(cls.sum))# can access Class field.
    #     print("cls.name: " + cls.name)#this print Studnet.name; 
        # can not access object field.

    #staticmethod can be replace by classmethod. 
    # It's similar to object function and class function,
    # but lack of parameter(cls, self)

    # If a method not relate to class and object, 
    # can as a static method, lack of Object Oriented Programming.

    # @staticmethod
    # def get_sum():# no self or cls parameter
    #     print('Static method get_sum: ' + str(Student.sum))# access class field
    #     #print(self.name)# can not access object field.

# student1 = Student("Jerry", 20)
# student1.plus_sum()# invoke class method by object
# Student.plus_sum()# invoke class  method by Class
# student1.get_sum()# invoke static method by object
# Student.get_sum()# invoke static method by Class

# # output:
# constructor of Jerry
# Total number of students:1
# cls.sum: 1
# cls.name: None
# Total number of students:2
# cls.sum: 2
# cls.name: None
# Static method get_sum: 2
# Static method get_sum: 2