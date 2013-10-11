import math

def complex_mag(c):
    mag = math.hypot(c.real, c.imag)
    return mag

def complex_angle(c):
    angle = math.atan2(c.real, c.imag)
    return angle

c = complex(3, 4)
a =complex_mag(c)
b =complex_angle(c)

def signal_noise(signal, noise):
    noise = 10 * math.log10(float(signal) / noise)
    return noise

x = signal_noise(2, 1)

def binomial_coef(n, k):
    num = math.factorial(n)
    denom = math.factorial(k) * math.factorial(n-k)
    return num / denom

y = binomial_coef(10, 3)

def factorial_length(n):
    return len(str(math.factorial(n)))

def factorial_length2(n):
    return (n * math.log(n) - n) / math.log(10)

z = factorial_length(100)
w = factorial_length2(100)

print 'complex magnitude is ' ,a
print 'complex angle is ' ,b
print x
print y
print z
print w