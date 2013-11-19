def make_word_dict():
    d = {}
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word]=word
    return d

def rotate_pairs(word_dict,word):
    for i in range(1,14):
        rotated = rotate_word(word,i)
        if rotated in word_dict:
            print word, i, rotated


def rotate_word(word, n):
    """ 
    This function takes a string, word, and rotates it by a number, n.
    """
    rotated = ''
    first = ord('a')
    last = ord('z')
    for letter in word:
        number = ord(letter)
        if n >= 0:
            if number < (last - n):
                number = number + n
                letter = chr(number)
            else:
                number = first+(n-(last-ord(letter))) - 1
                letter = chr(number)
        if n < 0:
            if number > (first - n):
                number = number + n
                letter = chr(number)
            else:
                number = last + (n + (number - first)) +1
                letter = chr(number)
        rotated += letter
    return rotated

if __name__ == '__main__':
    word_dict = make_word_dict()

    for word in word_dict:
        rotate_pairs(word_dict,word)