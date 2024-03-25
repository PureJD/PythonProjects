from random import Random

nouns = {1: 'cats', 2: 'dogs', 3: 'birds', 4: 'fish', 5: 'mice', 6: 'rabbits', 7: 'hamsters', 8: 'horses', 9: 'snakes', 10: 'lizards'}
adjectives = {1: 'happy', 2: 'sad', 3: 'angry', 4: 'excited', 5: 'bored', 6: 'tired', 7: 'hungry', 8: 'thirsty', 9: 'scared', 10: 'brave'}
ing_adjectives = {1: 'running', 2: 'jumping', 3: 'swimming', 4: 'flying', 5: 'crawling', 6: 'hopping', 7: 'galloping', 8: 'slithering', 9: 'climbing', 10: 'sneaking'}
name = input('Enter your name: ')

def band_name(name):
    while True:
        random = Random()
        random_noun = random.randint(1, 10)
        random_adjective = random.randint(1, 10)
        random_ing_adjective = random.randint(1, 10)
        print(f'{name} and the {adjectives[random_adjective]} {ing_adjectives[random_ing_adjective]} {nouns[random_noun]}')
        choice = input('Please type 1 to generate another band name or 2 to exit:' )
        if choice == '1':
            continue
        elif choice == '2':
            break
        else:
            print('Invalid input. Please type 1 to generate another band name or 2 to exit:')
            continue
print(band_name(name))
