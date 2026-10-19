import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("black")

# Create a ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")

# Ball speed
ball.dx = 0.175
ball.dy = -0.175

# Function to move the ball
def move_ball():
    x = ball.xcor() + ball.dx
    y = ball.ycor() + ball.dy

    # Border collision
    if x < -290 or x > 290:
        ball.dx *= -1  # Reverse the ball direction

    if y < -290 or y > 290:
        ball.dy *= -1  # Reverse the ball direction

    ball.goto(x, y)  # Move the ball

    # Move the ball again after 10 milliseconds
    win.ontimer(move_ball, 10)

# Start moving the ball
move_ball()

# Keep the window open
turtle.done()
