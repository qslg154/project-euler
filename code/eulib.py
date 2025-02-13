from math import sqrt, floor

def triangle(n): #triangle check
    k = n
    n = floor(sqrt(2 * n)) # if n = k(k+1) then k * k < n < k+1 * k+1, k < sqrt(n) < k+1
    if n * (n + 1) / 2 == k:
        return True
    else:
        return False
        
def exp_by_squaring(x, n, mod):
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    base = x % mod
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        n = n // 2
    return result