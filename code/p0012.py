def parse(n):
    a = 0
    for i in range(n):
        a += int(input()[0:20])
    print(str(a)[0:10])

parse(int(input()))
        