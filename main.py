from turtle import *
import random
screen=Screen()
screen.setup(500,400)
screen.listen()
user=screen.textinput("Turtle Race Game","Choose a Colour: ")
colors = ["red","green","blue","purple","yellow","black"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles=[]
for turtle_player in range(0, 6):
    sam=Turtle()
    sam.shape("turtle")
    sam.penup()
    sam.color(colors[turtle_player])
    sam.goto(x=-230,y=y_positions[turtle_player])
    all_turtles.append(sam)
if user:
    is_race=True
while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race=False

            winning_color=turtle.pencolor()
            if winning_color==user:
                print(f"You've won! The {winning_color} Turtle is the Winner!")
            else:
                print(f"You've lost! The {winning_color} Turtle is the Winner!")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()