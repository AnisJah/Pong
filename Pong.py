import turtle


#window
win = turtle.Screen()
win.setup(width=800, height=600)
win.bgcolor("black")
win.title("Ping Pong Thing Ding Dong Chink")
win.tracer(0)

#player 1
player1 = turtle.Turtle()
player1.speed (0)
player1.shape("square")
player1.shapesize(stretch_wid=5,stretch_len=1)
player1.color("white")
player1.penup()
player1.goto(-350,0)

#player 2
player2 = turtle.Turtle()
player2.speed (0)
player2.shape("square")
player2.shapesize(stretch_wid=5,stretch_len=1)
player2.color("white")
player2.penup()
player2.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed (0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3

#movement
def player1up():
   y = player1.ycor()
   y+= 15
   player1.sety(y)

def player1down():
   y = player1.ycor()
   y-= 15
   player1.sety(y)

def player2up():
   y = player2.ycor()
   y+= 15
   player2.sety(y)

def player2down():
   y = player2.ycor()
   y-= 15
   player2.sety(y)

#Keyboard
win.listen()
win.onkeypress(player1up,"w")
win.onkeypress(player1down,"s")
win.onkeypress(player2up,"Up")
win.onkeypress(player2down,"Down")

while True:
    win.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if (ball.ycor()>=290):
        ball.sety(290)
        ball.dy *=-1
    if (ball.ycor()<=-290):
        ball.sety(-290)
        ball.dy *=-1
    if (ball.xcor()>=390):
        ball.goto(0,0)
        ball.dx*=-1
    if (ball.xcor()<=-390):
        ball.goto(0,0)
        ball.dx*=-1
    if((ball.xcor()<-345)and(ball.ycor()<player1.ycor()+40)and(ball.ycor()>player1.ycor()+40)):
        ball.setx(345)
        ball.dx*=-1