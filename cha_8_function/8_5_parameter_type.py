def double_skill_1_combine(skill_1,skill_2):
    return skill_1 * 2 + skill_2

# 关键字参数：arguemnts' order doesnt mmatter.
c = double_skill_1_combine(skill_2 = 2, skill_1 = 1 )
print(c)