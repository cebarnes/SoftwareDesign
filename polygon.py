from swampy.TurtleWorld import *

def polygon(t, length, n):
	for i in range(n):
		fd(t, length)
		lt(t,360/n)
	print t
	wait_for_user()

def circle(t,r):
	
world = TurtleWorld()
bob = Turtle()

polygon(bob,50,4)