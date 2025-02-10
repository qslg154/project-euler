from sympy import primerange, isprime
from itertools import permutations

primes = set(primerange(1000, 10000))
permPrimes = []


def findProgreesion(arr):
    n = len(arr)
    result = []
    
    for i in range(n):
        for j in range(i + 1, n):
            diff = arr[j] - arr[i]
            third_term = arr[j] + diff
            
            if third_term in arr[j + 1:]:
                result.append((arr[i], arr[j], third_term))
    
    return result



for i in primes:
    permutes = set(int(''.join(p)) for p in permutations(str(i)))
  
    prime_permutes = set(p for p in permutes if p in primes)
    
    l = sorted(prime_permutes)
    
    if len(prime_permutes) >= 3 and l not in permPrimes:
        permPrimes.append(l)

for i in permPrimes:
    a = findProgreesion(i)
    if a:
        for tuples in a:
            print(''.join(str(i) for i in tuples))
