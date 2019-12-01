class Student():
    name = 'None'
    age = 0
    # 'self' represent specific object. Not Class.
    def __init__(self,name, age):
        self.name = name 
        self.age = age 
        print('constructor of '+ self.name)
        print(name)
        print(age)
        
        #self must be in every funcation's first parameter.
    def do_homework(self):
        print(self.name +" is doing homework.")
student1 = Student("Jerry", 20) #self = student1
student2 = Student("Tom", 21) #self = student2
student1.do_homework()
student2.do_homework()

