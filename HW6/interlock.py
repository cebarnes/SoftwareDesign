from inlist import*

def interlock(word_list,word):
    evens = word[::2]
    odds = word[1::2]

    return in_bisect(word_list, evens) and in_bisect(word_list,odds)

def make_word_list():
    stuff = list(open('words.txt'))
    fin = map(str.strip, stuff)
    return fin

if __name__ == '__main__':
    word_list = make_word_list()

    for word in word_list:
        if interlock(word_list,word):
            print word, word[::2],word[1::2]

