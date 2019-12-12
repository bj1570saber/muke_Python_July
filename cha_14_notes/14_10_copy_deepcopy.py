import copy
origin = [1, 2, [3, 4]]
copy_1 = copy.copy(origin)
copy_2 = copy.deepcopy(origin)
origin[0] = 9
print(copy_1[0]) #1 shallow copy will copy elements,
print(copy_2[0]) #1

origin[2][0] = 6
print(copy_1[2][0]) #6 shallow copy will not copy subset data structure.
print(copy_2[2][0]) #3 deepcopy copy every elements includes subset.