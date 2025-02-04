#p = a+b+c = k(m^2+n^2+2mn+m^2-n^2) = 2k(m^2+2mn) = 2km(m+n)
#p must be even, each pair of (m,n,k) generates a solution
from math import ceil, gcd

def divisor(k):
    factors = [k]
    for i in range(2,ceil(k/2)+1):
        if k % i == 0:
            factors.append(i)
    return factors

def solution(k): #solve k = m(m+n)
    sol = 0
    for i in range(2, ceil(k**0.5) + 1):
        for j in range(1, i):
            if k == i * (i + j) and gcd(i, j) == 1 and not(i % 2 == 1 and j % 2 == 1):
                sol += 1

    return sol

def total(k):
    tot = 0
    for i in divisor(k):
        tot += solution(i)
    return tot

max = 0
maxsol = 3
for i in range(60, 500):
    if total(i) > maxsol:
        max = i
        maxsol = total(i)
print(max, max*2)

#ans is max*2




    
