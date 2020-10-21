import turtle


t = turtle.Turtle()
draw = turtle.Turtle()
screen = turtle.Screen()

t.shape("turtle")
t.speed(0)
# t.getscreen()
screen.bgcolor("white")
t.color("white")
t.penup()
t.goto(-300,-300)
# draw.goto(-300,-305)
# screen.screensize(1024,480)


def turn_left():
    t.left(2)
def turn_right():
    t.right(2)
def turn_forward():
    t.forward(2)
def turn_backward():
    t.backward(2)
def fire():  #발사 함수
    ang = t.heading()
    while t.ycor() > 0:
        t.forward(15)
        t.right(5)

    # d = t.distance(target, 0)
    # t.sety(random.randint(10, 100))
    # if d < 25:
    #     t.color("blue")
    #     t.write("Good!", False, "center", ("", 15))
    # else:
    #     t.color("red")
    #     t.write("Bad!", False, "center", ("", 15))
    t.color("black")
    t.goto(-200, 10)
    t.setheading(ang)
t.goto(-300, 0)
t.down()
t.goto(300, 0)

screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(turn_forward,"Up")
screen.onkeypress(turn_forward,"Down")
screen.onkeypress(fire, "space")

dir("str")
screen.listen()
screen.mainloop()



