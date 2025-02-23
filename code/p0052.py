# notice that 142857 is a solution (1/7)

# x < 10^ ceil(log x) / 6

from itertools import permutations

def check(n):
    for i in range(10**n, round(10**(n+1)/6)):
        s = 0
        permutation = tuple((''.join(p) for p in permutations(str(i))))
        for j in range(1,7):
            s += str(i * j) in permutation
            if s == 6:
                return i
            
for i in range(1,6):
    print(check(i))
            

