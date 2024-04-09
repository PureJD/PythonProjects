from turtle import Turtle, Screen
import random

main_loop = False 
screen = Screen()
screen.bgcolor('grey')
screen.setup(width=500, height=400)
colours = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
#Bet selection 
user_bet = screen.textinput(title= 'Make your bet', prompt='Which turtle will win? Enter a colour: red, green, blue, yellow, orange, purple ').lower()



all_turtles = []

co_ordinates = [-200, -100]
current_colour = 0 

for turtle in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colours[current_colour])
    new_turtle.goto(co_ordinates)
    co_ordinates[1] += 30
    current_colour += 1
    all_turtles.append(new_turtle)

if user_bet:
    main_loop = True

while main_loop:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            main_loop = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f'You have won. {winner} turtle has come in first!') 
            else:
                print(f'You have lost! {winner} turtle has come in first!')

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick() 