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
        if score_p < 0:
            return "score can not be negtive."
        self.score = score_p
        print(self.name + '\'s score: ' + str(self.score))

    def do_homework(self):
        self.do_eng_homework#内部调用
        print(self.name +" is doing homework.")
    
    def do_eng_homework(self):
        print(self.name +" is doing homework.")

student1 = Student("Jerry", 20)
student1.do_homework()#外部调用
result =student1.marking(59)
if result is not None:
    print(result)
result =student1.marking(-1)
if result is not None:
    print(result)
# output:
# constructor of Jerry
# Jerry is doing homework.
# Jerry's score: 59
# score can not be negtive.