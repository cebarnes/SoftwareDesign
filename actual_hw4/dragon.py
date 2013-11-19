from swampy.TurtleWorld import *

def dragon(t,n):
    m = n/
    dragon(t,m)
    lt(t,90)
    dragon(t,m)
    rt(t,90)
    dragon(t,m)
    lt(t,90)
    dragon(t,m)
    rt(t,90)
    dragon(t,m)

world = TurtleWorld()
bob = Turtle()
bob.delay = .01

dragon(bob,100)