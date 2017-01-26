import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    chet = turtle.Turtle()
    count = 0
    while (count < 4):
        chet.forward(100)
        chet.right(90)
        count = count + 1

    window.exitonclick()

draw_square()
