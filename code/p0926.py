from eulib import exp_by_squaring
from sympy import primerange
from math import floor, ceil
from collections import Counter

def compress_list(input_list):
    # Count the occurrences of each element in the list
    counter = Counter(input_list)
    
    # Create the output list
    output_list = [[item, count] for item, count in counter.items()]
    
    return output_list


def prime_fact_factorial(n):
    fact = []
    for i in primerange(1, n+1):
        t = i
        s = 0
        while True:
            if t >= n:
                break
            s += floor(n / t)
            t *= i
        fact.append(s)
    return fact

#with open('0926_primes.txt', 'w') as file:
    for line in prime_fact_factorial(10000000):
        file.write(f'{line}\n')

with open('0926_primes.txt', 'r') as file:
    primes = []
    for line in file:
        primes.append(int(line))

def post_red_count(n, k): # counts the number of element > 0 in list [fl(n/n), .... , fl(n/1)] - k, fl denotes the floor function
    return floor(n / k)

def reduction(l, step): 
    s = 1
    for i in range(len(l)):
        count = post_red_count(l[i][0], step)
        s *= exp_by_squaring(count + 1, l[i][1], 10**9 + 7) # choosing from {0, ... ,count}, so + 1
    return ([pair for pair in l if pair[0] > step], s - 1)

roundness = 0
primelist = compress_list(primes) # [exponent of prime p, number of primes that has the exponent]

step = 1
print(primelist)
while True:
    (a, b) = reduction(primelist, step)
    roundness += b
    roundness = roundness % (10**9 +7)
    primelist = a
    step += 1
    if a == []:
        break
print(roundness)


        


