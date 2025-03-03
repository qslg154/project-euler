def eval(a, b):
    n = a**b
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

def main():
    max = -1
    for i in range(99, 81, -1):
        for j in range(99, 81, -1):
            a = eval(i, j)
            if a >= max:
                max = a
    print(max)

if __name__ == '__main__':
    main()