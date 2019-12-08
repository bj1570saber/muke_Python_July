origin = 0
def factory(pos):
    def go(step):
        nonlocal pos # explicit declare
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go

tourist = factory(origin)
print(tourist(2))
print(tourist.__closure__[0].cell_contents)
print(tourist(3))
print(tourist.__closure__[0].cell_contents)
print(tourist(5))
print(tourist.__closure__[0].cell_contents)
print(origin)

# this is a functional programming example.
# closure memorize the last time saved value of 'pos'.
# function never change origin's value.