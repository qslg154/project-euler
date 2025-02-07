from math import sqrt, floor

def triangle(n): #triangle check
    k = n
    n = floor(sqrt(2 * n)) # if n = k(k+1) then k * k < n < k+1 * k+1, k < sqrt(n) < k+1
    if n * (n + 1) / 2 == k:
        return True
    else:
        return False