import turtle

def drawsquare(dot):
	for i in range(1,3):
		dot.forward(99)
		dot.right(30)
		dot.forward(99)
		dot.right(120)
		dot.forward(99)
		dot.right(30)
		dot.forward(99)

def draw():
	window = turtle.Screen()
	window.bgcolor("red")

	robot = turtle.Turtle()
	robot.color("blue")
	robot.speed(0)
	for i in range (1,35):
		drawsquare(robot)
		robot.right(10)

	window.exitonclick()

draw()
