def make_word_dict():
    t = {}
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        key = tuple(sorted(tuple(word)))
        if key in t:
            pass
        else:
            t[key] = []
    return t

def make_word_list():
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        t.append(word)
    return t


def assign_words_to_letters(word_list,letters):
    d = letters
    for word in word_list:
        t = tuple(sorted(tuple(word)))
        d[t].append(word)
    return d

def anagram_sets(d):
    anagrams = {}
    for key in d.keys():
        if len(d[key])>1:
            anagrams[key]=d[key]
        else:
            pass
    return anagrams

def largest_sets(anagrams):
    gram = []
    for val in anagrams.values():
        gram.append((len(val),val))
    gram.sort(reverse=True)

    sort_gram = []
    for length,value in gram:
        sort_gram.append(value)
    return sort_gram

def maxLen(t):
    lengths = []
    for value in t:
        lengths.append(len(value))
    biggest = max(lengths)
    return biggest

def largest_bingo(anagrams):
    gram = []
    for val in anagrams.values():
        gram.append((len(val),val))
    gram.sort(reverse=True)

    sort_gram = []
    largest_bingo = []
    for length,value in gram:
        sort_gram.append(value)
    for value in sort_gram:
        if len(value)==maxLen(sort_gram):
            largest_bingo.append(value)
    t = largest_bingo[0]
    letters = tuple(t[0])
    return sorted(letters)

def bingo(anagrams):
    bingo = {}
    for key in anagrams.keys():
        if len(key)==8:
            bingo[key] = anagrams[key]
    return bingo


if __name__ == '__main__':
    letters = make_word_dict()
    word_list = make_word_list()
    anagrams = assign_words_to_letters(word_list,letters)
    grams = anagram_sets(anagrams)
    bing = bingo(grams)
    
    
    print largest_bingo(bing)