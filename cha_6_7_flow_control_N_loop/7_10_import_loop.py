#Comment import Errors:
'''
Avoid :
p1.py-
from p2 import p2 
p1 = 'p1'


p2.py-
from p1 import p1
p2 = 'p2'

This cause a loop import.
'''

'''
Avoid :
p1.py-
from p2 import p2 
p1 = 'p1'

p2.py-
from p3 import p3
p2 = 'p2'

p3.py-
from p1 import p1
p3 = 'p3'

This cause a loop import.
'''

'''
p1.py-
import p2

p2.py-
p2 = 'p2'
print(p2)

When run python p1.py
Python will run codes in p2.py
'''