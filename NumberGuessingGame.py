from random import randint

def input_from_user():
    range_to = input('This program will set a value and it is up to you to guess that value. The program will select a number from the number 1 up until the number: ')
    if range_to.isdigit():
        print(f'Thank you, now let me think...I have selected a number beteen 1 and {range_to} ')
    else:
        print('You do not seem to have entere a vaid number')
        input_from_user()
    return range_to

def correct_answer():
    user_guess = input('What is your guess?: ')
    if int(user_guess) == random_number:
        print('Wow, what are the odds? Whatever they were you have beaten them. Congratulations')
    else:
        print('Noope')
        correct_answer()

user_input = input_from_user()
random_number = randint(1, int(user_input))
print(random_number)
correct_answer()



