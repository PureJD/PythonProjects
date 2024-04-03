import time 
import os

#This dictionary has been left in the main file for the sake of reduing amount of files within the repository.
#ordiarily this would be stored in an addictional file and imported. 
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

Menu_art = '''______________________________
|                            |
|     Coffee Menu            |
|                            |
|   1. Espresso    - $1.50   |
|                            |
|   2. Latte       - $2.50   |
|                            |
|   3. Cappuccino  - $3.00   |
|                            |
|____________________________|'''
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

change = round(0, 2)


def clearingline():
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console 


def loading_spin():
    elements = ['|', '/', '-', '\\', '|',  '|', '\\', '-', '/', '|']
    for i in elements: 
        print(i, end='\r')
        time.sleep(0.2) # 0.2 seconds
        
            
def shutting_down():
    clearingline()
    print('*beep* *beep* SHUTDOWN PROCEDURE INITIATED')
    loading_spin()
    quit()
    

def print_report():
    clearingline()
    print('CHECKING CURRENT LEVELS')
    loading_spin()
    print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')


def resource_checker(user_choice):
    for ingredient, required_amount in MENU[user_choice]["ingredients"].items():
        if resources[ingredient] <= required_amount:
            print(f" Sorry, there is not enough {ingredient} for that order.")
            return 0
    return 1


def money_checker(user_choice, total):
    global change
    drink_cost = MENU[user_choice]["cost"]  
    if total < drink_cost:
        print(" Oh, I am sorry but it seems you have not inserted enough money to purchase this item. Money refunded.")
        print(" Please select another item or add additional coins.")
        return 0
    else:
        change = round(total - drink_cost, 2)  
        return 1
    
    
while True:
    print(Menu_art)
    user_choice = input(' What would you like? ').lower()
    if user_choice == 'off':
        shutting_down()
    elif user_choice == 'report':
        print_report()
        continue
    elif user_choice not in MENU:
        print(' please could you choose an item from the menu')
        continue
    stock = resource_checker(user_choice)
    if stock == 0:
        continue
    quarters = float(input(' please insert coins Quarters: ')) * 0.25
    dimes = float(input(' please insert coins Dimes: ')) * 0.1
    nickles = float(input(' please insert coins Nickles: ')) * 0.05
    pennies = float(input(' please insert coins pennies: ')) * 0.01
    total = round(quarters + dimes + nickles + pennies, 2)
    sufficent_money = money_checker(user_choice, total)
    if sufficent_money == 0:
        continue
    if change > 0:
        print(f' Please take your ${change} in change')
    time.sleep(1)
    resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]  
    resources["water"] -= MENU[user_choice]["ingredients"]["water"]  
    resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"] 
    resources["money"] = MENU[user_choice]["cost"]
    clearingline()
    loading_spin()
    print(f' Here is your {user_choice} ☕️, enjoy!')
    time.sleep(2)
    print(' NEXT CUSTOMER PLEASE!')
    

    
    
    
     
    
    




    