import os

to_do_list = {}
list_item_number = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_to_list():
    global list_item_number
    addition = input("What would you like to add to the list?: ")
    to_do_list[list_item_number] = addition
    list_item_number += 1
    print(f'Your current list is: {to_do_list}')

def delete_from_list():
    print(f'Your current list is: {to_do_list}')
    while True:
        delete_selection = input('Which number from the list do you wish to delete?: ')
        if not delete_selection.isdigit():
            print('Please select a number')
            continue
        elif int(delete_selection) not in to_do_list:
            print('Please select a number from the list')
            continue
        else:
            break
    del to_do_list[int(delete_selection)]
    print('Entry Deleted')

def view_entire_list():
    for value in to_do_list.values():
        print(value)

def menu_choice():
    while True:
        number_choice = input('''Please select what you would like to do:
                            1. Add item to list
                            2. Delete item from list
                            3. View entire list
                            4. Exit
                            : ''')
        if not number_choice.isdigit():
            print('Please select a number')
            continue
        elif int(number_choice) not in range(1,5):
            print('Please select a number between 1 and 4 only')
            continue
        else:
            break
    return int(number_choice)

print('Welcome to ToDoList, a program that will create a to do list for you')
while True:
    choice = menu_choice()
    clear_screen()
    if choice == 1:
        add_to_list()
    elif choice == 2:
        delete_from_list()
    elif choice == 3:
        view_entire_list()
    elif choice == 4:
        break
print('Thank you for using ToDoList')

  