import random
import time

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  
player_cards = []
dealer_cards = []
game_over = False

def game_start():
    global player_cards, dealer_cards  
    player_cards = []
    dealer_cards = []
    for _ in range(2):  
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    print(f'You have drawn the two cards: {player_cards}')
    print(f'The dealer has drawn the card: {dealer_cards[0]}')  

def hit():
    global game_over  
    player_cards.append(random.choice(cards))
    print('You have pulled a...')
    time.sleep(1)
    print(player_cards[-1])
    if sum(player_cards) > 21 and 11 in player_cards: 
        player_cards[player_cards.index(11)] = 1  
    if sum(player_cards) == 21:
        print('BLACKJACK, You WIN!')
        game_over = True
    elif sum(player_cards) > 21:
        lose()

def stick():
    global game_over  
    while sum(dealer_cards) < 17:  
        dealer_cards.append(random.choice(cards))
        print(f'The dealer has pulled the card {dealer_cards[-1]}')
        if sum(dealer_cards) > 21:
            win()
            return
    if sum(dealer_cards) >= sum(player_cards):  
        lose()
    else:
        win()

def win():
    global game_over  
    print(f'The Dealer has gone bust with the cards of {dealer_cards} with a total of {sum(dealer_cards)}!')
    time.sleep(1)
    print('Congratulations, you win!')
    game_over = True

def lose():
    global game_over  
    print(f'You have lost, your cards {player_cards} have exceeded 21 with a total of {sum(player_cards)} or you have been outplayed by the dealer')
    game_over = True

print('Welcome to Blackjack')
game_start()

while not game_over:
    print(f'Your current hand: {player_cards}, total: {sum(player_cards)}')
    print(f'Dealer\'s visible card: {dealer_cards[0]}')
    user_choice = input('What next? Do you want to "hit" or to "stick"? ').lower()
    if user_choice == 'hit':
        hit()
    elif user_choice == 'stick':
        stick()
    else:
        print('Please type either "hit" or "stick".')

if game_over:  
    print('Game over. Type "restart" to play again or "exit" to quit.')
    user_choice = input().lower()
    if user_choice == 'restart':
        game_over = False
        game_start()
    else:
        print('Thanks for playing!')

        
    