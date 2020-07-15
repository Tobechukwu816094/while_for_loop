"""
5) Create the following lists using a for loop.
  (a) A list consisting of the integers 0 through 49
  (b) A list containing the squares of the integers 1 through 50.

"""
integers = []
squares_integers = []
for i in range(0 , 49):
    add = integers.append(i)
print(integers)
for x in range(1 , 50):
    square = x**2
    add = squares_integers.append(square)
print(squares_integers )



