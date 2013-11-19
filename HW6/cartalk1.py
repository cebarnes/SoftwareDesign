def triple_double_letters():
    fin = open('words.txt')
    for word in fin:
        if check_triple(word):
            print word

def check_triple(word):
    if len(word)<6:
        return False
    for i in range(len(word)-6):
        if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
            return True

triple_double_letters()