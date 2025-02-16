# c <= 500

for i in range(500, 0, -1):
    for j in range(i - 1, 0, -1):
        if i**2 == j**2 + (1000 - i - j)**2:
            print(i * j * (1000 - i - j))
