import turtle

s = turtle.Screen()
t = turtle.Turtle()
s.title("Happy New Year 2022!")
s.setup(width=1000, height=700)
turtle.bgcolor("black")
t.speed("fastest")


t.up()

t.lt(90)
t.fd(100)
t.rt(90)

t.down()

for i in range(100):
    t.color("red")
    t.fd(100)
    t.back(100)
    t.rt(5)

t.up()

t.fd(120)

t.down()

for i in range(100):
    t.color("orange")
    t.fd(100)
    t.back(100)
    t.rt(5)

t.up()

t.back(200)

t.down()

for i in range(100):
    t.color("blue")
    t.fd(100)
    t.back(100)
    t.rt(5)

t.up()

t.rt(120)
t.fd(180)
t.down()

for i in range(100):
    t.color("yellow")
    t.fd(100)
    t.back(100)
    t.rt(5)

t.up()

t.fd(80)
t.lt(5)
t.down()

for i in range(100):
    t.color("green")
    t.fd(100)
    t.back(100)
    t.rt(5)

t.up()

t.lt(90)

t.fd(300)

t.down()

for i in range(100):
    t.color("purple")
    t.fd(100)
    t.back(100)
    t.rt(5)

t.up()

t.lt(10)

t.fd(100)

t.rt(90)

t.down()

for i in range(100):
    t.color("cyan")
    t.fd(100)
    t.back(100)
    t.rt(5)

t.up()

t.color('white')
style = ('Courier', 20, 'normal')
t.write('Happy New Year 2022!', font=style, align='center')
t.hideturtle()


while True:
    s.update()