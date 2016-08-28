#Uses a function for each shape and in the square function uses a loop
import turtle

def draw_turtle():
	window = turtle.Screen()
	window.bgcolor("red")
	
	draw_square()
	draw_circle()
	draw_triangle()
	
	window.exitonclick()
	
def draw_square():
	
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(6)
	
	for i in range(5):
		brad.forward(100)
		brad.right(90)
		
def draw_circle():

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(6)
	
	brad.circle(100)
	
def draw_triangle():
	
	triangle = turtle.Turtle()
	triangle.shape("turtle")
	triangle.color("black")
	triangle.speed(6)
	
	triangle.left(90)
	triangle.forward(200)
	triangle.right(135)
	triangle.forward(150)
	triangle.right(90)
	triangle.forward(135)
		

draw_turtle()

	