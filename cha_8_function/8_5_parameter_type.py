def double_skill_1_combine(skill_1,skill_2):
    return skill_1 * 2 + skill_2

# 1.必须参数：
print(double_skill_1_combine(1,2))# 4

# 2.关键字参数 keyword parameter：arguemnts' order doesnt mmatter.
d = double_skill_1_combine(skill_2 = 2, skill_1 = 1 )
print(d)# 4

# 3. 默认参数 default argument
def print_student_files(name,gender = "male", age = 20, city = "SD"):
    print("My name is " + name)
    print("I am " + str(age) + " years old.")
    print("I'm "+ gender)
    print("I live in " + city)

print_student_files("Jerry", "male", 28, "SD")
print('~'*20)
print_student_files("Tom")
#other fields will be fill up with default value.
print('~'*20)
print_student_files("Jeremy", "female", 25)
# name argument must pass in since no default value. 
# All arguments need to be in order.
print('~'*20)
# if some default arguments need to be pass in as keyword parameter. 
print_student_files("Larry",age = 30)
# default arguments must pass in after regular arguemnts.
'''
My name is Jerry
I am 28 years old.
I'm male
I live in SD
~~~~~~~~~~~~~~~~~~~~
My name is Tom
I am 20 years old.
I'm male
I live in SD
~~~~~~~~~~~~~~~~~~~~
My name is Jeremy
I am 25 years old.
I'm female
I live in SD
~~~~~~~~~~~~~~~~~~~~
My name is Larry
I am 30 years old.
I'm male
I live in SD
'''
# error: Non-default argument follows default argument.
'''
def func(name, gender = 'male', age):# default value must be specified here
    print(name + gender + str(age))
'''