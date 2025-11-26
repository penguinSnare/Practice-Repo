#
# A python program that simulates a slot machine.
# Having the following items... '🍒',' 🍇', '🍉', '7️⃣'.

import random

# Creates the function
def play():
    # the initial list
    symbols = ['🍒',' 🍇', '🍉', '7️⃣']
    # This boolean basically instructs python to keep running the program indefinetly, therefore
    # the need for a 'break' is needed within per user input within a conditional statement.
    while True:
        results = random.choices(symbols, k=3) #prints 3 random results
        pretty_results = '|'.join(results) #puts the results b/w pipes
        print(pretty_results) # printsd the results for the user.

        if results == ['7️⃣', '7️⃣', '7️⃣']: # The main checker for desired results
            print("Jackpot! 💰")
            break #What will ultimately break the infinite loop we created with the boolean.
        else:
            print("Will roll again!")

    user_cont = input("Wanna play again?: ") # Variable whether to end or continue
    print("Press 'Y' to continue or 'N' to not play again.")
    if user_cont == 'N': # Ends the program for good with a message
        print("Thanks for playing.") 
    elif user_cont == 'Y':
        play() # Restarts the program from the top
    else: # Ends the program for good with a message incase of any weird input.
        print("Weird input, terminating program.")

play()

# Resources:
#https://stackoverflow.com/questions/62992294/how-to-print-out-the-list-items-horizontally