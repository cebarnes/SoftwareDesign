from swampy.TurtleWorld import *

def star(t,length):
    for i in range(5):
        fd(t,length)
        lt(t,72)
        fd(t,length)
        rt(t,144)
    wait_for_user()

world = TurtleWorld()
bob = Turtle()
star(bob,50)

