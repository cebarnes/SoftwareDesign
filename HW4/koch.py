from swampy.TurtleWorld import *


def koch(t,n):
    if n<3:
        fd(t,n)
        return
    m = n/3.0
    print m
    koch(t,m)
    lt(t,60)
    koch(t,m)
    rt(t,120)
    koch(t,m)
    lt(t,60)
    koch(t,m)
    

def snowflake(t,n):
    koch(t,n)
    rt(t,120)
    koch(t,n)
    rt(t,120)
    koch(t,n)
    wait_for_user()

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
snowflake(bob,333)