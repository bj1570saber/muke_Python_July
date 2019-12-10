# use a dictionary as switch flow control
switcher = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday'
}

day = 0
print(switcher.get(day, 'Unknow'))

# better way for multi statements:
def get_sunday():
    return 'Sunday'

def get_monday():
    return 'Monday'

def get_tuesday():
    return 'Tuesday'

def get_default():
    return 'Unknow'

switcher = {
    0: get_sunday,
    1: get_monday,
    2: get_tuesday
}

day = 4

print(switcher.get(day, get_default)())