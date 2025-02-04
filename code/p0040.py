def eval(length) -> int: # 1 * (10 - 1 + 1) + 2 * (100 - 10)
    sum = 0

    for i in range(1, length + 1):
        sum += (i) * (10 ** i - 10 ** (i-1))
    return sum 

def digit(n):
    k = 0
    while True:
        if eval(k) >= n:
            break
        k += 1
    return k - 1

def returnNumber(n) -> int:
    prevDigit = digit(n)
    if prevDigit == 0:
        return n
    k = n - eval(prevDigit) #so we start counting at n+1 digit number
    residue = k % (prevDigit + 1)
    number = 10 ** prevDigit + (k - residue) / (prevDigit + 1)

    return int(str(number)[residue-1])

product = 1
for i in range(0,7):
    product *= returnNumber(10 ** i)

print(product)






