from math import floor, sqrt


with open('0042_words.txt','r') as f: #parsing
    content = f.read()
content = content.replace('"','')
words = content.split(',')

def value(s):
    val = ord(s) - 64
    return val

def triangle(n):
    k = n
    n = floor(sqrt(2 * n)) # if n = k(k+1) then k * k < n < k+1 * k+1, k < sqrt(n) < k+1
    if n * (n + 1) / 2 == k:
        return True
    else:
        return False
    
print(words)


val = 0
for i in words:
    sum = 0
    for j in range(len(i)):
        sum += value(i[j])
    if triangle(sum) == True:
        val += 1
print(val)


        

        




