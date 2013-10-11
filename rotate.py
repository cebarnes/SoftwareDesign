def rotate_word(word, rot):
    """ 
    This function takes a string, word, and rotates it by a number, rot.
    """
    first = ord('a')
    last = ord('z')
    for letter in word:
        number = ord(letter)
        if rot >= 0:
            if number < (last - rot):
                number = number + rot
                letter = chr(number)
            else:
                number = first+(rot-(last-ord(letter))) - 1
                letter = chr(number)
        if rot < 0:
            if number > (first - rot):
                number = number + rot
                letter = chr(number)
            else:
                number = last + (rot + (number - first)) +1
                letter = chr(number)
        print letter,

word = "cheer"
rotate_word(word,7)