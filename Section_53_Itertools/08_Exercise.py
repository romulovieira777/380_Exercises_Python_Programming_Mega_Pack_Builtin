"""
Exercise No. 08

Using the built-in itertools module and the product class create an iterator that allows it to iterate through all
fields of the chessboard and assign to the chessboard variable.

In response, print chessboard variable to the console as shown below.

Tip:

    #>>> help(itertools.product)

    Help on class product in module itertools:

    class product(builtins.object)
     |  product(*iterables, repeat=1) --> product object
     |
     |  Cartesian product of input iterables.  Equivalent to nested for-loops.
     |
     |  For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).
     |  The leftmost iterators are in the outermost for-loop, so the output tuples
     |  cycle in a manner similar to an odometer (with the rightmost element changing
     |  on every iteration).
     |
     |  To compute the product of an iterable with itself, specify the number
     |  of repetitions with the optional repeat keyword argument. For example,
     |  product(A, repeat=4) means the same as product(A, A, A, A).
     |
     |  product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)
     |  product((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ...

Expected result:

['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4',
 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8',
 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4',
 'H5', 'H6', 'H7', 'H8']
"""
import itertools

# Solution I
chessboard = []

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for letter, number in itertools.product(letters, numbers):
    chessboard.append(f'{letter}{number}')

print(chessboard)


# Solution II
letters = list('ABCDEFGH')
numbers = [str(i) for i in range(1, 9)]
chessboard = itertools.product(letters, numbers)
chessboard = [''.join(fields) for fields in chessboard]

print(chessboard)
