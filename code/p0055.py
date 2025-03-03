def islychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return True
    return False

def main():
    s = 0
    for i in range(10001):
        s += not(islychrel(i))
    print(s)

if __name__ == '__main__':
    main()
