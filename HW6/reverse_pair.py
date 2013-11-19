from inlist import*

def reverse_pair(word_list,word):
    rev_word = word[::-1]
    return in_bisect(word_list,rev_word)


    for word in fin:
        if word[::-1] in d.keys():
            rev_words.append(word)
    return rev_words

def make_word_list():
    stuff = list(open('words.txt'))
    fin = map(str.strip, stuff)
    return fin

if __name__ == '__main__':
    word_list = make_word_list()

    for word in word_list:
        if reverse_pair(word_list,word):
            print word, word[::-1]
