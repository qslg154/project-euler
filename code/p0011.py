def parse(n): 
    l = []
    for i in range(n):
        l.append(list(map(int,input().split(' '))))
    return l
                 
def iterate(l, n):
    value = []
    for i in range(n - 3):
        for j in range(n - 3): #row, column
            row = 1
            column = 1
            diag1 = 1
            diag2 = 1
            for k in range(4):
                row *= l[i][j+k]
                column *= l[i+k][j]
                diag1 *= l[i+k][j+k]
                diag2 *= l[i+3-k][j+k]
            value.extend((row, column, diag1, diag2))
    return max(value)

print(iterate(parse(20), 20))

                

