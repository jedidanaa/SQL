 import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Basketball Bounce Game")
screen.bgcolor("lightgreen")
screen.setup(width=600, height=600)

# Draw the basketball court outline
court = turtle.Turtle()
court.speed(0)
court.pensize(3)
court.penup()
court.goto(-250, -250)
court.pendown()
for _ in range(4):
    court.forward(500)
    court.left(90)

# Create the basketball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0, 0)

# Ball movement speed
dx = 3
dy = 2

# Move the ball
def move_ball():
    global dx, dy
    x, y = ball.position()
    ball.setx(x + dx)
    ball.sety(y + dy)

    # Bounce off walls
    if x + dx > 250 or x + dx < -250:
        dx *= -1
    if y + dy > 250 or y + dy < -250:
        dy *= -1

    screen.ontimer(move_ball, 30)

# Start moving the ball
move_ball()

screen.mainloop()
