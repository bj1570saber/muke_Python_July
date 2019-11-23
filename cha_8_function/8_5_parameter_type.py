def double_skill_1_combine(skill_1,skill_2):
    return skill_1 * 2 + skill_2

# 1.必须参数：
print(double_skill_1_combine(1,2))

# 2.关键字参数：arguemnts' order doesnt mmatter.
d = double_skill_1_combine(skill_2 = 2, skill_1 = 1 )
print(d)

# 3. 默认参数
def print_student_files(name,gender,age,city):
    print("My name is " + name)
    print("I am " + str(age) + " years old.")
    print("I'm "+ gender)
    print("I live in " + city)

print_student_files("Jerry", "male", 28, "SD")
