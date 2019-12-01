class Student():
    __sum = 0
    __name = 'None'
    __age = 0
    __score = 0
    def __init__(self, name_p, age_p):
        self.name = name_p 
        self.age = age_p
        self.score = 0
        print('constructor of '+ self.name)

    def marking(self, score_p):
        if score_p < 0:
            print("score can not be negtive.")
            return
        self.score = score_p
        print(self.name + '\'s score: ' + str(self.score))

    def do_homework(self):
        # self.name not self.__name
        print(self.name + " finish his/her homework.")
        self.marking(100)#内部调用

student1 = Student("Jerry", 20)

student1.do_homework()#外部调用
student1.marking(59)
student1.marking(-1)
# following line creat and assign a value to 
# a new private variable of student1.
# this is dynamic programming language feature.
student1.__new_score = -1 # is not access private variable.
print(student1.__new_score)

# for example: following direct to access object none exist private variable:
student2 = Student('Tom', 21)
#print(student2.__new_score_2)# AttributeError: 
#'Student' object has no attribute '__new_score_2'

# output:
# constructor of Jerry
# Jerry is doing homework.
# Jerry's score: 59
# score can not be negtive.