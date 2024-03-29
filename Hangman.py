import random 

logo = '''\033[92m 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)
words = ['uninterested','fretful','savory','hulking','kill','elegant','hop','things','women','spill','lunch','tart','floor','abaft','acid','angle','longterm','representative','descriptive','noiseless','uptight','pointless','observation','crime','paste','deliver','snail','greet','reach','visitor','analyze','sisters','enter','unhealthy','button','trousers','horses','fool','weary','fit','happen','seal','desk','advertisement','longing','hellish','massive','cub', 'sausage', 'floppy']
word_choice = list(words[random.randint(0,49)])
word_string = ['_' for _ in range(len(word_choice))]
print(word_string)
lives = 6

while True:
    if lives == 0:
         print('You lose')
         break
    if '_' in word_string:
        user_guess = input('Choose a letter: ').lower()
        if user_guess not in word_choice:
             lives -= 1
             print('\033[92mI am afraid that is not correct...')
             print(stages[lives])
        else:
            for i in word_choice:
                    index = word_choice.index(i)
                    if user_guess == i:
                        word_string[index] = i
                        word_choice[index] = 0
                
        print(word_string)             
    else:
        print('Congratulations you win!')
        break
        

             
        
  
   
    
    
    
    
    
    
    
    
    
    
   
