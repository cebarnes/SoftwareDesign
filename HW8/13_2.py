
import string
def gutenberg():
    res = []
    fin = open('fairies_short.txt')

    for line in fin:
        words = line.rsplit(' ')
        for word in words:
            word = word.strip()
            for char in word:
                if char in string.punctuation:
                    word = word.replace(char,'')
            if word =='':
                pass
            else:
                res.append(word.lower())

    return res

print gutenberg()