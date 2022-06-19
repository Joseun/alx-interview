In mathematics, Pascal's triangle is a triangular array of the binomial coefficients that arise in probability theory, combinatorics, and algebra. In much of the Western world, it is named after the French mathematician Blaise Pascal, although other mathematicians studied it centuries before him in India,[1] Persia,[2] China, Germany, and Italy.[3]

The entries of Pascal's triangle are conventionally enumerated starting with row {\displaystyle n=0}n=0 at the top (the 0th row) and column {\displaystyle k=0}k=0 at the left (the 0th column). The triangle may be constructed in the following manner: in row 0 and column 0, the entry is 1. The subsequent entries are constructed by adding the entry above and to the left with the entry above and to the right, treating blank entries as 0. For example, in row 1 and column 0, the entry is 1 (the sum of the blank entry 0 in row 0 and column −1, and the entry 1 in row 0

Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer