from pronounce import*

def make_words_dict():
    d = {}
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word]=word
    return d

def homophone(a,b,pro):
    if a not in pro or b not in pro:
        return False
    
    return pro[a]==pro[b]

def check(word_dict,word,pro):
    word1 = word[1:]
    if word1 not in word_dict:
        return False
    if not homophone(word,word1,pro):
        return False

    word2 = word[0]+word[2:]
    if word2 not in word_dict:
        return False
    if not homophone(word,word2,pro):
        return False

    return True

if __name__ == '__main__':
    pro = read_dictionary('c06d.txt')
    word_dict = make_words_dict()

    for word in word_dict:
        if check(word_dict,word,pro):
            print word, word[1:], word[0]+word[2:]