import turtle

may = turtle
may.shape('turtle')
may.color('red')
may.pensize(12)
may.speed(20)

for i in range(3):
    may.left(60)
    may.forward(300)
    may.right(120)
    may.forward(300)
    may.left(180)
    may.forward(150)
    may.right (120)
    may.forward(80)
    may.left(180)
    may.forward(300)
    may.pensize(10)
    may.left(180)
    may.forward(30)
    may.right(90)
    may.circle(110)
    may.right(150)

may.hideturtle()


input()