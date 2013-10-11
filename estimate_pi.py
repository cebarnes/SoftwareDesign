from math import *

def estimate_pi():
    epsilon = 0
    k = 0
    stuff = 1

    while stuff > 1e-15:
         stuff =(factorial(4.0*k)*(1103.0+26390.0*k))/((factorial(k)**4.0)*(396**(4.0*k))) 
         epsilon = epsilon + stuff
         k = k+1

    pii = 1.0/((2.0*sqrt(2.0)/(9801.0))*epsilon)
    return pii

print 'pi estimation =', estimate_pi()
print 'math.pi =', pi