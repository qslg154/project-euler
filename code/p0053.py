# note that nCr = nCn-r

def count(n):
    s = 1
    for i in range(1, n + 1):
        s *= (n + 1 - i) / i
        if s >= 1000000: # nCi to nC(n-i)
            return n - i - i + 1 
    return 0    
sum = 0 
for i in range(1, 101):
    sum += count(i)
print(sum)
    
