class Student():
    __sum = 0
    __name = 'None'
    __age = 0
    __score = 0
    def __init__(self, name_p, age_p):
        self.__name = name_p 
        self.__age = age_p
        self.__score = 0
        print('constructor of '+ self.__name)

    def marking(self, score_p):
        if score_p < 0:
            print("score can not be negtive.")
            return
        self.__score = score_p
        print(self.__name + '\'s score: ' + str(self.__score))

    def do_homework(self):
        # self.name not self.__name
        print(self.__name + " finish his/her homework.")
        self.marking(100)#内部调用

student1 = Student("Jerry", 20)
# following line creat and assign a value to 
# a new (private?) variable of student1.
# this is dynamic programming language feature.
student1.__name = 'feng' # It is just created.
# this is not Student class private variable.
print(student1.__name)# output: feng
print(student1.__dict__)#{'_Student__name': 'Jerry', 
# '_Student__age': 20, '_Student__score': 0, '__name': 'feng'}
# private __name -> change name to _Student__name

student1.do_homework()#外部调用 Jerry finish his/her homework.
student1.marking(59)# Jerry's score: 59
student1.marking(-1)#score can not be negtive.
print('~'*20)

# for example: following direct to access object none exist private variable:
student2 = Student('Tom', 21)
# print(student2.__name)# AttributeError: 
#'Student' object has no attribute '__name'

# output:
# constructor of Jerry
# feng
# {'_Student__name': 'Jerry', '_Student__age': 20, '_Student__score': 0, '__name': 'feng'}
# Jerry finish his/her homework.
# Jerry's score: 100
# Jerry's score: 59
# score can not be negtive.
# ~~~~~~~~~~~~~~~~~~~~
# constructor of Tom