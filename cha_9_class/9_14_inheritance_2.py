from human_class import Human
class Student(Human):
    def __init__(self,school,name,age):
        self.school = school
        Human.__init__(self,name, age)# should use super.
        # explicit pass 'self' to parent constructor,
        # when a function called by class name.
    
    def do_homework(self):
        print("doing_homework.")

student1 = Student("Palomar", "jerry", 18)
print(student1.school)
print(student1.name) 
print(student1.age) 
#This is a demo of class name call function must pass a object.
Student.do_homework(student1)# doing_homework.
Student.do_homework('')#pass a empty string: doing_homework. 
# Best way:
student1.do_homework()# doing_homework.
# All in all, Python is flexibility
