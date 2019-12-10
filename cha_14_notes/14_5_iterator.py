#iterable: list, tuple, set, dict
#iterator Object: includes __iter__(), __next__()

class BookCollection:# a iterable class
    def __init__(self):
        self.data = ['<book 1>', '<book 2>','<book 3>']
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= len(self.data):
            raise StopIteration()
        r = self.data[self.cur]
        self.cur += 1
        return r

# for loop:
books = BookCollection()
import copy
books_copy = copy.copy(books)
books_deepcopy_1 = copy.deepcopy(books)
print('First For loop:')
for book in books:
    print(book)
print('Seconde For loop:')
for book in books: # 2nd loop will not print. Not like iterable data structure.
    print(book)

print("Use copy module: ")
for book in books_copy:
    print(book)
    
print('What will happen if copy books after iterate?')
books_shallow_copy = copy.copy(books)
for book in books_shallow_copy:
    print(book)
print("It will not print, copy.copy() it's a shallow copy.")
print('~')
print('What will happen if copy.deepcopy() books after iterate?')
books_deepcopy = copy.deepcopy(books)
for book in books_deepcopy:
    print(book)
print("It will not print.")
print('What about books_deepcopy_1?')
for book in books_deepcopy_1:
    print(book)

print('~')

# iterator:
books = BookCollection()
print(next(books))
print(next(books))
print(next(books))

