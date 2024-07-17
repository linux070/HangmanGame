# `````` Building a Hangman game project ```````
import random 
import os
import hangman_art
hangman_image = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''
print(hangman_image)
# ````` making use of the hangman_words list `````
import hangman_words
hangman_words.word_list
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
# print(f"Pfft, the answer is : {chosen_word}") ------ this is just a demo to make sure you're on the right track.
lives = 6 # ---- just to know this is part of hangman pictures code.

display = []  #  ----- Creating blank spaces to fill in the words 
for letter in range(word_length) :
    display += "_" 

end_game = False
while not end_game:
# ````` checking the guessed letter `````    
    guess = input("Guess a letter :").lower()
    os.system('cls')  #--------- this is to clear the screen to avoid confusion after a user input.
    if guess in display:
        print(f"You've guessed {guess}")

    for position in range(word_length) :
        letter = chosen_word[position]
        if letter == guess :
          display[position] = letter 
    if guess not in chosen_word: # ----- checking if a certain word isn't in the available provided words.
            print(f"You guessed {guess}, that's not in the you lose a life.")
            lives -= 1
            if lives == 0:
              end_game = True    
              print("You lose")  

# join all the elements together.
    print(f"{' ' .join(display)}")

    if "_" not in display:
        end_game = True
        print("You win.")  
    print(hangman_art.stages[lives])    


# ````` linuxmode `````