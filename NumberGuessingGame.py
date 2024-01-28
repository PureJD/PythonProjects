from random import randint

def player_name():
    return input('Please enter playername: ')

def input_from_user():
    range_to = input('This program will set a value and it is up to you to guess that value. The program will select a number from the number 1 up until the number: ')
    if range_to.isdigit():
        print(f'Thank you, now let me think...I have selected a number beteen 1 and {range_to} ')
    else:
        print('You do not seem to have entere a vaid number')
        input_from_user()
    return range_to

def correct_answer():
    attempts_count = 1
    while True:
        user_guess = input('What is your guess?: ')
        if int(user_guess) == random_number:
            print('Wow, what are the odds? Whatever they were you have beaten them. Congratulations')
            print(f'That has taken you {attempts_count} tries. Do you think you can beat your previous score?')
            return attempts_count
        else:
            print('Nope')
            attempts_count += 1
            continue
        

player_user_name = player_name()
scoreboard = {}

while True:
    user_input = input_from_user()
    random_number = randint(1, int(user_input))
    previous_score  = correct_answer()
    statistics = 'A number between 1 and' + user_input


#The plan for this program is you lose your place next time is to: create new function new game plus which will let users play again but also record username, difficulty and score in the dictionary. The main game loop needs to be adjusted.




