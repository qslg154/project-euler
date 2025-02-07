from eulib import triangle
from math import ceil, sqrt


def hexangon(n): # (2k-1)^2 < (2k-1)(2k) = 2n < 4k^2
    k = ceil(sqrt(2*n)) # get 2k
    return n == (k - 1)*(k) / 2 and k % 2 == 0 # prevent k being odd

pentagon = [i*(3*i-1) / 2 for i in range(100000)]

solution = []

for i in pentagon:
    if triangle(i) and hexangon(i):
        solution.append(i)
        print(i)





