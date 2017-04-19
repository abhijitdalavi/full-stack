import turtle

def draw_square(new_turtle):
    for i in range(1,5):
        new_turtle.forward(100)
        new_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("dark grey")
    #Chet the turtle and his attributes
    chet = turtle.Turtle()
    chet.shape("turtle")
    chet.color("yellow")
    chet.speed(5)
    #Chet is gonna draw us a lot of squares
    for i in range(1,36):
        draw_square(chet)
        chet.right(10)
    #Aerie, Chet's girlfriend, draws us a circle
    aerie = turtle.Turtle()
    aerie.shape("arrow")
    aerie.color("red")
    aerie.circle(100)
    #now billy is going to draw us a triangle
    billy = turtle.Turtle()
    billy.shape("circle")
    billy.color("green")
    for i in range(1,4):
        billy.forward(100)
        billy.left(120)
    #close the window when we click it
    window.exitonclick()

draw_art()
