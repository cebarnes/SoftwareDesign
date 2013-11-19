def has_palindrome(number,start,length):
    """
    Takes an integer and checks to see if it has a palindrome
    """
    word = str(number)[start:start+length]
    return word[::-1]==word

def check_i(i):
    return (has_palindrome(i,2,4) and
        has_palindrome(i+1,1,5) and
        has_palindrome(i+2,1,4) and
        has_palindrome(i+3,0,6))

def check_all_numbers():
    answers = []
    i = 100000
    while i<=999999:
        if check_i(i):
            answers.append(i)
        i = i+1
    return answers

print check_all_numbers()


