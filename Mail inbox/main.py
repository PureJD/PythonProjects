#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Mail Merge Project Start/Input/Names/invited_names.txt', 'r') as file:
    names = file.read()
collection_of_names = list(names.split())


with open('Mail Merge Project Start/Input/Letters/starting_letter.txt', 'r') as file:
    letter = file.read()


for i in collection_of_names:
    new_letter = letter.replace('[name]', i)
    with open(f'Mail Merge Project Start/Output/ReadyToSend/{i}.txt', 'w')as file:
        file.write(new_letter)



  



