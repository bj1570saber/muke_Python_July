# Count travel distance:
origin = 0
def go(step):
    new_pos = origin + step
    # if function has local variable origin, it will not search 'origin' in outer scope.
    # origin = new_pos #In a function, any = sign's left side variable is a local variable.
    return new_pos

print(go(2))
print(go(3))
print(go(6))
print('~')
# second try:
origin = 0
def go(step):
    global origin
    new_pos = origin + step
    origin = new_pos 
    return new_pos

print(go(2))
print(go(3))
print(go(6))
print('~')

# Third try:

# def update():
#     x = 0
#     def increace(n):
#         x = x + n
#         return x
#     return increace

# f = update()
# print(f(1))
# print(f(3))
# print(f(5))
# print(f(7))

