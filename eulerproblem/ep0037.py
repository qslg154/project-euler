import sympy, time

start = time.time()

head = ['2','5','3','7']

mid = ['1','3','5','7','9']

end = ['3','7']

def adding(l):
    successor=[]
    for i in l:
        for j in mid:
            successor.append(i+j)
    return successor

def addingend(l):
    successor=[]
    for i in l:
        for j in end:
            successor.append(i+j)
    return successor


def generator(n): #generate the possible candidate
    candidate = head[:]
    if n > 2:
        for i in range(n-2):
            candidate=adding(candidate)[:]
    candidate=addingend(candidate)[:]
    return list(map(int,candidate))

prime = []
n = 2

while len(prime) < 11:
    for i in generator(n):
        if sympy.isprime(i) == True:
            Flag = True
            while Flag == True:
                for j in range(1,n):
                    if sympy.isprime(int(str(i)[0:j])) == False:
                        Flag = False
                        break
                    if sympy.isprime(int(str(i)[j:n])) == False:
                        Flag = False
                        break
                if Flag == True:
                    prime.append(i)
                    break
    n += 1
print(prime)
print(sum(prime))

end = time.time()
print(end - start)
            

    

    
    

