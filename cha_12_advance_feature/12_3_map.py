list_x =[1,2,3,4,5,6,7,8]

def square(x):
    return x * x

map_y = map(square, list_x)
print(map_y) #<map object at 0x10f452bb0>
print(list(map_y))#[1, 4, 9, 16, 25, 36, 49, 64]