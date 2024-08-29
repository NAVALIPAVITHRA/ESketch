from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()
screen.title("ESKetchPy")
def mov_forwards():
    tim.forward(20)
def mov_backwards():
    tim.backward(20)
def turn_left():
   new =  tim.heading()+10
   tim.setheading(new)
def turn_right():
    new= tim.heading()-10
    tim.setheading(new)
def clear():
    tim.clear()

def home():
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(mov_forwards,"Up")
screen.onkey(mov_backwards,"Down")
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")
screen.onkey(clear,"c")
screen.onkey(home,"h")









screen.exitonclick()













