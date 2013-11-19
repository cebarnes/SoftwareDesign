from inlist import * 

def make_word_list():
    stuff = list(open('words.txt'))
    fin = map(str.strip, stuff)
    return fin

def find_children(word_list,word):
    children = []
    for i in range(len(word)):
        child = word[:i]+word[i+1:]
        if in_bisect(word_list,child):
            children.append(child)
    return children

memo = {}
memo[''] = ['']

def reducible(word_list,word):
    if word in memo:
        return memo[word]

    res = []
    for child in find_children(word_list,word):
        t = reducible(word_list,child)
        if t:
            res.append(child)

    memo[word] = res
    return res

def all_reducible(word_list):
    res = []
    for word in word_list:
        t = reducible(word_list,word)
        if t != []:
            res.append(word)
    return res 

def print_trail(word_list,word):
    if len(word)==1:
        print word
        return
    print word,
    t = reducible(word_list,word)
    print_trail(word_list,t[0])

def find_longest(word_list):
    reducibles = all_reducible(word_list)
    longest = []
    for word in reducibles:
        longest.append((len(word),word))
    longest.sort(reverse=True)

    for length,word in longest[:5]:
        print '\n'
        print_trail(word_list,word)
    print '\n'
        

if __name__ == '__main__':
    word_list = make_word_list()
    find_longest(word_list)

