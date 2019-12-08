list_x =[1,2,3,4,5,6,7,8]

def square(x):
    return x * x

map_y = map(square, list_x)
print(map_y) #<map object at 0x10f452bb0>
print(list(map_y))#[1, 4, 9, 16, 25, 36, 49, 64]

r = map(lambda x: x*x ,list_x)
print(list(r))#[1, 4, 9, 16, 25, 36, 49, 64]

# two parameters example:
list_x =[1,2,3,4,5,6,7,8]
list_y =[1,2,3,4,5,6,7,8]
r = map(lambda x,y: x*y ,list_x, list_y)
print(list(r))#[1, 4, 9, 16, 25, 36, 49, 64]

# three and many more:
list_x =[1,2,3,4,5,6,7,8]
list_y =[1,2,3,4,5,6,7,8]
list_z =[1,2,3,4,5]    # not enough parameters
r = map(lambda x,y,z: x*y+z ,list_x, list_y, list_z)
print(list(r))#[2, 6, 12, 20, 30] # lack of result.