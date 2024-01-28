from random import randint
import json

def load_scores(filename='scores.json'):
    try:
        with open(filename, 'r') as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = {}
    return scores

def save_scores(scores, filename='scores.json'):
    with open(filename, 'w') as file:
        json.dump(scores, file)

def update_scores(player, score, scores):
    if player in scores:
        scores[player] += score
    else:
        scores[player] = score

def input_player_name():
    return input('Please enter player name: ')

def input_from_user():
    range_to = input('This program will set a value, and it is up to you to guess that value. Enter the upper limit for the range (a positive integer): ')
    if range_to.isdigit():
        print(f'Thank you, now let me think... I have selected a number between 1 and {range_to}.')
        return int(range_to)
    else:
        print('You did not enter a valid number.')
        return input_from_user()

def correct_answer(random_number):
    attempts_count = 1
    while True:
        user_guess = input('What is your guess?: ')
        if int(user_guess) == random_number:
            print(f'Congratulations! You guessed the correct number in {attempts_count} tries.')
            return attempts_count
        else:
            print('Nope')
            attempts_count += 1

scores = load_scores()
print(f'The current HIGHSCORES for this are {scores}, however as you choose your own difficulty, take this with a pinch of salt')

player_name = input_player_name()

while True:
    range_limit = input_from_user()
    random_number = randint(1, range_limit)

    current_score = correct_answer(random_number)
    update_scores(player_name, current_score, scores)
    
    save_scores(scores)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break

