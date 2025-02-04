num = []

for i in range(9001,10000):
    digitset = {10}
    k = str(i)+str(2*i)
    for j in range(9):
        digitset.add(str(k)[j]) if str(k)[j] != '0' else None
    if len(digitset) == 10:
        num.append(int(k))

print(max(num))
