# 9 + 8 + ... + 1 = 0 mod 3, so we start from 1 to 8

# 8!, 7!, .. is small enough for us to brute force all

import itertools, sympy

digits = '1234567' #tried 8, no prime

pandigital = [int(''.join(p)) for p in itertools.permutations(digits)]

prime = []

for i in pandigital:
    if sympy.isprime(i) == True:
        prime.append(i)
    
print(max(prime))