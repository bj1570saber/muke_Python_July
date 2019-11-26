def demo():
    global c
    c = 2
# outside local scope visit c must make it as a global variable.
demo() # Must call this function, and run the definition in side the funcions
print(c)