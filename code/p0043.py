#we construct from d_8 d_9 d_10
import time

start = time.time()  

def pandigitCheck(n):
    a = [int(i) for i in str(n)]
    a.sort()
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return False
    return True

def multCheck(n, s):
    if n % s == 0:
        return True
    return False

def nextnum(n) -> list: # nextnum gives successor, string
    digits = ['0','1','2','3','4','5','6','7','8','9']
    l = []
    for i in digits:
        if i not in list(str(n)):
            l.append(i + str(n))

    return l 
           

init = [i for i in range(100, 999)]

num = [str(i) for i in init if pandigitCheck(i) == True and i % 17 == 0]

prime = [13,11,7,5,3,2,1]
m = 0


for i in prime:
    l = num.copy()
    for j in l:
        for k in nextnum(j): # nextnum gives successor
            if multCheck(int(k[0:3]), i) == True: 
                num.append(k)
        num.remove(j)
print(num)

print(sum([int(i) for i in num]))

end = time.time()

print(end-start)