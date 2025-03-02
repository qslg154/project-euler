from collections import Counter



with open('code/0054_poker.txt') as f:
    mylist = [line.rstrip('\n') for line in f]

def format(l):
    s = l.split(' ')
    s1 = s[0:5]
    s2 = s[5:10]
    return s1, s2

hands = []
for i in mylist:
    temp = format(i)
    hands.append(temp)


conversionhigh = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


def flush(l):
    s = []
    for i in l:
        s.append(i[1])
    s = set(s)
    if len(s) == 1:
        return True, handsort(l)[4]
    return False, None

def handsort(l): #return 'value' of cards
    s = []
    for i in l:
        try:
            x = conversionhigh.get(i[0])
            s.append(int(x))
        except:
            s.append(int(i[0]))
    s = sorted(s)
    return tuple(s)

def straight(l):

    s = handsort(l)

    # check
    flag = True
    for j in range(len(s) - 1):
        if s[j] + 1 != s[j + 1]:
            flag = False
    
    if s == (2, 3, 4, 5, 14):
        flag = True

    return flag, s[0]


# the following takes 'counter'

def counter(l):
    count = Counter(l)
    s = [[item, count] for item, count in count.items() ]
    return s

def quads(l): 
    for i in l:
        if i[1] == 4:
            return True, i[0]
    return False, 0
        
def trips(l):
    for i in l:
        if i[1] == 3:
            return True, i[0]
    return False, 0
        

def fh(l):
    s = trips(l)
    if s[0]:
        for i in l:
            if i[1] == 2:
                return True, trips(l)[1]
    return False, 0
    
            
def pair(l):
    pp = -1
    s = sorted(list(map(lambda x: x[0], l)) ,reverse=True)
    if len(l) == 4:
        for i in l:
            if i[1] == 2:
                pp = i[0]
                s.remove(pp)
                s = sorted(s, reverse=True)
                s = [pp] + s
                return True, tuple(s)
    return False, 0

            
def twopair(l):
    if len(l) != 3 or trips(l)[0] == True:
        return False, 0
    
    s = []
    hc = -1
    for i in l:
        if i[1] == 2:
            s.append(i[0])
        else:
            hc = i[0]
    s = sorted(s, reverse=True)
    s.append(hc)
    return True, tuple(s)

def eval(l): # hc = 0, p = 1, 2p = 2, set = 3, straight = 4, flush = 5, fh = 6, quad = 7, sf = 8
    # flush/straight block
    if flush(l)[0]:
        if straight(l)[0]:
            return 8, (straight(l)[1])
        else:
            return 5, (flush(l)[1])
    if straight(l)[0]:
        return 4, (straight(l)[1])

    #counter block
    count = counter(handsort(l))

    if quads(count)[0]:
        return 7, (quads(count)[1])
    if fh(count)[0]:
        return 6, (fh(count)[1])
    if trips(count)[0]:
        return 3, (trips(count)[1])
    if twopair(count)[0]:
        return 2, (twopair(count)[1])
    if pair(count)[0]:
        return 1, (pair(count)[1])
    
    return 0, sorted(handsort(l), reverse=True)

def proc(l):
    a = [None, None]
    a[0] = eval(l[0])
    a[1] = eval(l[1])
    return a



def main():   
    value = list(map(proc, hands))
    wins = 0

    for i in value:
        left = i[0]
        right = i[1]
        if left[0] > right[0]:
            wins += 1
        elif left[0] == right[0]:
            for j in range(5):
                if left[1][j] > right[1][j]:
                    wins += 1
                    break
                elif left[1][j] < right[1][j]:
                    break
    print(wins)

if __name__ == '__main__':
    main()


    


    
            




        




            


    
