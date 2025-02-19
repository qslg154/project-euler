from sympy import primerange, isprime
from math import ceil

primes = primerange(10000,10000000)

def round_up_to_nth_digit(number, n):
    factor = 10 ** (n - 1)
    return ceil(number / factor) * factor
def replacement_count(p, diff):
    k = round_up_to_nth_digit(p, len(str(diff)) + 1)
    s = 0
    while p < k:
        s += isprime(p)
        p += diff
    return s

def diff(n):
    diff = []
    for i in range(0,10):
        pivot = '0'
        for j in str(n)[-2::-1]:
            if j == str(i):
                pivot = '1' + pivot
            else:
                pivot = '0' + pivot
        diff.append(int(pivot)) if int(pivot) != 0 else None
    return diff

def main():    
    for i in primes:
        for j in diff(i):
            if replacement_count(i, j) == 8:
                print(i)
                return i
    
if __name__ == '__main__':
    main()
  




 
