import random

def histogram(t):
    d = {}
    for c in t:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def choose_from_hist(hist):
    t = []
    for key in hist.keys():
        for i in range(hist[key]):
            t.append(key)
    return random.choice(t)

if __name__ == '__main__':
    t1 = [5,5,7,3,4,5,6,7,8,2,3,4,1,3,6,7,8,9,2,0]
    d1 = histogram(t1)
    print choose_from_hist(d1)
