from human_class import Human
class Student(Human):
    def __init__(self,school,name,age):
        self.school = school
        Human.__init__(self,name, age)
        # pass 'self' to parent constructor
        
student1 = Student("Palomar", "jerry", 18)
print(student1.school)
print(student1.name) 
print(student1.age) 
