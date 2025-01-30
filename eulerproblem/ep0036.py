from math import ceil, log2
import time

start = time.time()
digits = ['0','1']

def adding(precessor, lastopp):
    temp = digits[:]
    if lastopp == True:
        temp.pop(0)
    current = []
    if precessor == []:
            current = temp[:]
    else:
        for i in precessor:
            for j in temp:
                current.append(j + i)
    return current

def bingen(n):
    binary = []
    for i in range(n):
        binary = adding(binary, True if i == n-1 else False)
    return binary

def palindrome(n): #generate base 2 pali up to n
    pali = ['1']
    even = 1
    odd = 1
    for i in range(2,n+1):
        if i % 2 == 0:
            for j in bingen(even):
                pali.append(j+j[::-1])
            even += 1
        if i % 2 == 1:
            for j in bingen(odd):
                for k in digits:
                    pali.append(j+k+j[::-1])
            odd += 1
    return pali

def baseconv(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[::-1][i]) * (2 ** i)
    return sum

def bothbase(n): # n = max num
    k = ceil(log2(n))
    totest = list(map(baseconv,palindrome(k)))
    bothbase = []

    for i in totest:
        if str(i) == str(i)[::-1] and i <= n:
            bothbase.append(i)
    return bothbase

print(sum(bothbase(1000000)))
end = time.time()
print(end - start)


           




