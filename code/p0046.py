from sympy import isprime
from math import ceil, sqrt

def check(k):    # n < sqrt(k/2) < n + 1
    s = 0
    for i in range(ceil(sqrt(k/2))):
        s += isprime(k - 2*i**2)
    return s
    

for i in range(27, 100000000, 2):
    if not(check(i)):
        print(i)



