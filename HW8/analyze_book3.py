import random
from bisect import bisect_left

def create_freq(d):
    t = []
    freq = [0]
    i = 1
    for key in d.keys():
        t.append(key)
        freq.append(d[key]+freq[i-1])
        i += 1
    freq.remove(0)
    
    return freq,t

def choose_num(freq):
    return random.randint(1,freq[-1])

def find_index(freq,num):
    return bisect_left(freq,num)

def choose_word(word_list, i):
    return word_list[i]

def main():
    d = {'poop':17, 'merp':5, 'larp':7, 'frump':2}

    freq, word_list = create_freq(d)
    print freq
    print word_list
    num = choose_num(freq)
    print num
    i = find_index(freq,num)
    print i
    print choose_word(word_list,i)

if __name__ == '__main__':
    main()
