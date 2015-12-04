#!/usr/bin/env python3
__author__ = "hero24"
# python 3.5 brings in a new operator @
# its a matrix multuplier, and has no use in
# python standard library.
# note this shows how to implement and use new operator not, 
# how to implement proper matrixes, for sake of easy implementation
# my matrixes will be built using lists of equal length (2)
class Matrix:
    def __init__(self,lst):
        # initialise matrix in form of:
        # eg.:[[1,2],[2,3],[3,4]]
        # note that each matrix can have only 2 values
        self.lst = lst

    def __str__(self):
        # string value of the object, this is here only
        # for printing purpouses.
        return str(self.lst)

    def __matmul__(self,other):
        # new python operator can be 'overwitten' like
        # any other operator in python, by defining a 'magic method'
        # for it.
        # it can be defined using __matmul__ or __rmatmul__
        lst = []
        for i,k in other.lst:
            for j,l in self.lst:
                lst += [[i*j,k*l]]
            return Matrix(lst)

    def __imatmul__(self,other):
        # together with @ operator, a @= has also been brought in,
        # and is defined using __imatul__
        lst = []
        for i,k in other.lst:
            for j,l in self.lst:
                lst += [[i*j,k*l]]
            return Matrix(lst)

a = Matrix([[1,2],[3,4],[5,6]])
b = Matrix([[7,8],[9,10],[11,12]])
c = a @ b
print(c)
b @= c
print(b)
