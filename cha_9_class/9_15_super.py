from human_class import Human
class Student(Human):
    def __init__(self,school,name,age):
        self.school = school
        #Human.__init__(self,name, age)# should use super.
        super(Student, self).__init__(name,age)
        
    # function overriding
    def do_homework(self):
        super(Student, self).do_homework()# call parent function.
        print("doing_homework.")

student1 = Student("Palomar", "jerry", 18)
student1.do_homework()# doing_homework.
# output:
# Human doing homework.
# doing_homework.
