def is_even(n):
    if n%2:
        return False
    else:
        return True

def is_odd(n):
    return n%2 != 0

def is_divisible(n,m):
    return n%m == 0

print is_even(2)
print is_odd(7)
print is_divisible(12,4)