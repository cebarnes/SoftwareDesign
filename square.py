from swampy.TurtleWorld import *

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)
	print t
	wait_for_user()

world = TurtleWorld()
bob = Turtle()

square(bob,50)