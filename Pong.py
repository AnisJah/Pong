import turtle


#window
win = turtle.Screen()
win.setup(width=800, height=600)
win.bgcolor("black")
win.title("Ping Pong")
win.tracer(0)

#player 1
player1 = turtle.Turtle()
player1.speed (0)
player1.shape("square")
player1.shapesize(stretch_wid=5,stretch_len=1)
player1.color("white")
player1.penup()
player1.goto(-350,0)
player1score = 0

#player 2
player2 = turtle.Turtle()
player2.speed (0)
player2.shape("square")
player2.shapesize(stretch_wid=5,stretch_len=1)
player2.color("white")
player2.penup()
player2.goto(350,0)
player2score = 0

#ball
ball = turtle.Turtle()
ball.speed (0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

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

#score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(0,250)
score.hideturtle()


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
        player1score += 1
    if (ball.xcor()<=-390):
        ball.goto(0,0)
        ball.dx*=-1
        player2score += 1
    if((ball.xcor()<-340)and(ball.ycor()<player1.ycor()+15)and(ball.ycor()>player1.ycor()-15)):
        ball.setx(-340)
        ball.dx*=-1
    if((ball.xcor()>340)and(ball.ycor()<player2.ycor()+15)and(ball.ycor()>player2.ycor()-15)):
        ball.setx(340)
        ball.dx*=-1
    score.clear()    
    score.write("{}-{}".format(player1score, player2score),  align="center", font=("Courier",22,"normal"))
   # if player1score==5:
        #player1wins
    #if player2score==5:
        #player2wins
