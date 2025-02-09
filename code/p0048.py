def ModularExponentiation(base, exponent, mod):
    result = 1
    base = base % mod

    while exponent > 0:
      
        if exponent % 2 == 1:
            result = (result * base) % mod

        base = (base * base) % mod

        exponent = exponent // 2

    return result

s = 0 
for i in range(1,1001):
    s += ModularExponentiation(i, i, 10**10)
    s = s % 10**10
print(s)


print(str(sum(x**x for x in range(1,1001)))[-10:]) # it works LMAO