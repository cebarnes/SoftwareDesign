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

word = "cheer"
print rotate_word(word,7)