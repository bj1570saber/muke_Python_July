def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2

damages = damage(3,6)#<class 'tuple'>
print(type(damages))
print(damages[0], damages[1])
# 9 22
# 9 22

# A better way to print:
skill_1_damage, skill_2_damage = damage(3,6)#序列解包 sequence unpacking
print(skill_1_damage, skill_2_damage)# more meaningful than index print.
