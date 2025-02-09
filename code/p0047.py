from math import ceil, sqrt

def factor(n): #can be optimized for breaking after k distinct prime factors are obtained
    factor = []
    for i in range(2, max(3, ceil(sqrt(n)))):
        while n % i == 0:
            factor.append(i)
            n = n / i
    if not(n == 1):
        factor.append(n)
    return factor 

def countDistinct(l):
    return len(set(l))

def consectutivePrimeFactor(n): # n is length of required consectutive number of n distinct factor
    i = 2
    while True:
        i += 1
        if countDistinct(factor(i)) == n:
            s = True
            for j in range(i, i + n):
                if countDistinct(factor(j)) != n:
                    s = False
            if s:
                return i
            
print(consectutivePrimeFactor(4))

                
                

    

