import random
import requests
import re
import time
from os import system, name 

#declaring variables
chosen_word = "placeholder"
chosen_word_length = 1
x = 0
guess_list = []
current_state = 0
go_on = "y"
has_won = 0
words = []

#making a list off all the states off the gallow
states = ['''
  +---+
      |
      |
      |
      |
      |
=========
''','''
  +---+
  |   |
      |
      |
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
  O   |
  |   |
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
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

# define a clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#define a function that fetches a new word from the list
def get_new_word():
    global chosen_word
    global chosen_word_length
    global words

    #check if the list of words is empty, if empty get new words
    if (words == []):
        #get all the words from the site and store them in words
        response = requests.get("https://raw.githubusercontent.com/QUINT-09/first-repository/master/resources/10000_dutch_words.txt")
        words = response.content.splitlines()

    #using the lenght of the list, choose a random word and store it in chosen_word
    lenght_of_words = len(words)
    chosen_word_number = random.randint(0,lenght_of_words-1)

    #making sure it's a lowercase string
    chosen_word_nf = str.lower(str((words[chosen_word_number])))

    #format the word
    chosen_word = re.search("b\'(.*)\'",chosen_word_nf).group(1)
    #store the lenght of the word in chosen_word_lenght
    chosen_word_length = len(chosen_word)

#define a function used to split the word into l e t t e r s
def split(chosen_word): 
    return list(chosen_word)

#main loop of the game
while ( go_on == "y"):

    #set the gallow state back to the beginning
    current_state = 0

    get_new_word()

    #if the word is to short, get a new word
    while (chosen_word_length<7):
        get_new_word()
    
    #if the word contains anything else than letters, get a new word
    while (chosen_word.isalpha() != True):
        get_new_word()

    #split words into letters
    answer_list = split(chosen_word)

    #make a list with an _ for every letter (e.g.   words => _ _ _ _ _ )
    x = 0
    guess_list.clear()
    while (x < chosen_word_length):
        guess_list.append("_")
        x += 1

    #reset guess variable
    guess = "1"

    #this is the loop where the guessing takes place
    while (guess != "stop" ): 

        #print the current state of the game and ask for a guess
        clear()
        print("Typ 'stop' om te stoppen met spelen")
        print(states[current_state])
        print(' '.join(guess_list))
        print("")
        guess = input("Typ een letter: ")

        #if the input = stop, stop the game
        if (guess == "stop"):
            print("")
            print("Bedankt voor het spelen")
            time.sleep(3)
            exit(0)

        else:
            
            #check if the guess is a single letter
            if (guess.isalpha() == True and len(guess) == 1 and guess != "stop"):
                locations=[i for i in range(len(answer_list)) if answer_list[i]==guess]

                #the guess is wrong, increase the state of the gallow
                if (locations == []):
                    current_state += 1

                    #final stage of the gallow, the game is lost
                    if (current_state == 7):
                        clear()
                        #exit the guess loop
                        break
                
                #the guess was correct
                else:
                    #check where the letters are (e.g. guess==e, word==selection => [1,3])
                    for x in locations:
                        #replace the _ with the guessed letter
                        del guess_list[x]
                        guess_list.insert(x, guess)
                    
                    #if the guess list == The answer list, the game is won
                    if (answer_list == guess_list):
                        has_won = 1
                        #exit the guess loop
                        break
                        
            else:
                #intput is not a single letter, alert the player
                print ("Dat is geen letter")  
                time.sleep(3)  

    #the game was lost (we know this because of the has_won variable)
    if (has_won == 0): 
        #print some stuff
        clear()
        print(states[current_state])
        print("Jij verliest!")
        print("")
        print("Het correcte antwoord was " + chosen_word + ".")
        print("Tot nu toe had je geraden: " + (' '.join(guess_list)))
        print("")
        #ask if the player want's to play again (this works because the game loop only runs when go_on == y)
        go_on = input("Wil je nog eens spelen? (typ 'y' om nog eens te spelen) ")
    
    #the game was won
    else:
        #reset the has_won variable
        has_won = 0
        #print some stuff
        clear()
        print(states[current_state])
        print("Jij wint!")
        print("")
        print("Je hebt het woord " + chosen_word + " correct geraden.")
        print("")
        #see above
        go_on = input("Wil je nog eens spelen? (typ 'y' om nog eens te spelen) ")

#the main loop is quit, so the game is quit
print("")
print("Bedankt voor het spelen")
time.sleep(3)
exit(0)

#QUINT_09