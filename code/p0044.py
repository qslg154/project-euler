pentagon = set((3*i - 1)*(i)/2 for i in range(1, 2501))

#brute force through the list of generated pentagon number, I don't like this question

for i in pentagon:
    for j in pentagon:
        if i + j in pentagon:
            if i - j in pentagon:
                print(i - j)

