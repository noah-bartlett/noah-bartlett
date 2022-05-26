import turtle
import winsound

#Main window, this draws the window that the game is played in
wn = turtle.Screen()
wn.title('Pong by ME')
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#creates the score variables
score_a = 0
score_b = 0

#this is the creation and behavior of paddle a, it is drawn with turtle and the speed is the refresh rate, not movement
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B, same as paddle a but on the other side of the screen.
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball, also created in turtle. dx and dy are the speed that the ball moves at, this needs to be set on a computer basis.
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.dx = 0.1
ball.dy = 0.1

# Pen, writes the scoreboard also through turtle. sets the font, size and location.
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align = "center", font = ("Courier", 24, "normal"))

#Functions, the program can call these to do things
def paddle_a_up(): #this will move the first paddle up when the function is called.
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down(): #this will move that paddle down when the fuction is called.
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard bindings, this tells the computer what keys do what when pressed.
#wn.listen tells the computer to look out for the keys to be pressed
#wn.onkeypress defines the key bindings. this uses the format of a function and a string
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    wn.update()

    #move the ball according to the ball.dx and ball.dy parameters
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #check the borders, this will make the ball bounce and play a sound if it hits a border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #these two blocks define the edge of the screen on the x coordinate. resets the ball to center and updates the score
    #if the ball goes past.
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player 1: {score_a}  Player 2: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player 1: {score_a}  Player 2: {score_b}", align="center", font=("Courier", 24, "normal"))

    #check the paddles/players. this will make the ball bounce and play a sound for the paddles.
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() > paddle_a.ycor() - 40 and ball.ycor() < paddle_a.ycor() + 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

#All done!!
#ideas, add a win con, if score_a > 5 print a message
#make the ball more dynamic by changing dx and dy over time