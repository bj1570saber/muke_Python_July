from human_class import Human
class Student(Human):
    # No constructor is OK, just call parent's constructor.
    def do_homework(self):
        print(self.__name + " finish his/her homework.")

student1 = Student("Jerry", 19)
print(Student.sum) # reference ancestor's sum variable.
