from sympy import primerange, isprime

#for i in primerange(1, 1000000):
#    s += i
#    if s > 1000000:
#        print(i)
#        break
# 3943

primes = list(primerange(1,3944))

def max_chain(n): # n is initial prime
    k = 0
    s = 0
    for i in primes:
        if i == n:
            break
        k += 1
    for i in range(k, len(primes)):
        s += primes[i]
        if s > 1000000:
            break

    for j in range(1,len(primes)+1):
        s -= primes[-j]
        if isprime(s):
            return len(primes) - j - k, s
    return -1, -1

max = -1
for i in primes:
    l = max_chain(i)
    if l[0] > max:
        max = l[0]
        t = l[1]    
print(max, t)
    


   