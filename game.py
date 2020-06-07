# Ultimate Ninja Combat Game!!! 
# The player fights against the computer, and the winner gets bragging rights


import random, sys # random for generating random attacks
                   # sys for exiting the program when user quits.
 


def instructions(): # handles the display of instructions
    print("\nWelcome to Ultimate Gun Battle Combat!!! "
    "\nYou will be fighting against the computer, and the winner gets bragging rights. "
    "\nFor each turn you will be asked to use one of the 6 attacks below:"
    "\n(1)AK-47"
    "\n(2)AR-15"
    "\n(3)Carl Gustaf M4(Korobosta)"
    "\n(4)M16"
    "\n(5)M24 Sniper"
    "\n(6)9mm Revolver\n"
    "Choose wisely.")    

def sub(balance, bet): #updates the balace at start and subsequent subtractions

    newBalance = balance - bet
    return newBalance

def add(balace, bet): # add the balance and bet amount when the player wins
    
    newBalance = balace + bet
    return newBalance

def main():

    STARTING_BALANCE = 100
    STARTING_BET = 0

    

    print("Welcome to Ultimate Gun Battle Combat Game!!!") # Introduces the games

    while True:

        response = input("Please enter your name: ") # gets player's name

        if (response.isalpha()) == False:           # ensures the players does not submit numbers as a name
            print("\nInvalid! Please try again!\n")
            continue
        
        else:

            print("Welcome,",response)

            balance = sub(STARTING_BALANCE, STARTING_BET)

            print("\nYour current balance is ${:,.2f}".format(balance))


            rnd = 0 # initialise the rounds played at start to 0
            rbal = [] # initialised as an empty string


            while True:

                choice = input("\nPlease choose from the following menu:" # User menu
                "\n(I)nstructions"
                "\n(P)lay game"
                "\n(Q)uit game\n")

                if choice.lower() == 'i': # converts user input to lower case incase user inputs I or i
                                          
                    instructions()

                elif choice.lower() == 'p': # where the game is handled

                    while True:

                        if balance != 0: # makes sure the initial balance passes through

                            print("\nPlease enter the amount to bet. All bets must be multiples of 5.") # accepting bets entered by the user
                            bet = int(input())
                        
                            if bet%5 != 0: # making sure that bets that are not multiples of 5 are not accepted
                                print("You choose to bet ${:,.2f}".format(bet))
                                print("\nThat is not a valid amount. Your bet must be a multiple of 5, "
                                "and be within your means.")

                            elif bet%5 == 0 and bet > balance: # making sure that bets that are multiples of 5 but greater than the available balance are not accepted
                                print("You choose to bet ${:,.2f}".format(bet))
                                print("\nThat is not a valid amount. Your bet must be a multiple of 5, "
                                "and be within your means.")

                            else:
                                rnd+=1 # calculating the number of rounds played
                                rbal.append(balance) # adding the balances of each round to the rbal list
                                
                                print("You choose to bet ${:,.2f}".format(bet))

                                attacks = ["AK-47", "AR-15", "Carl Gustaf M4(Korobosta)", # store attacks in a list
                                "M16", "M24 Sniper", "9mm Revolver"]

                                while True:

                                    print("\n"+ response + ", you must choose one of the following attacks:" # get attack from user
                                    "\n(1)AK-47"
                                    "\n(2)AR-15"
                                    "\n(3)Carl Gustaf M4(Korobosta)"
                                    "\n(4)M16"
                                    "\n(5)M24 Sniper"
                                    "\n(6)9mm Revolver\n")
                                    
                                    a = int(input()) # ensure it's an integer

                                    if a < 1:  # ensure 0 and negatives are not accepted
                                        print("Invalid choice. Please try again!")
                                        continue

                                    elif a > 6: # ensure that any input greater than 6 is not accepted
                                        print("Invalid choice. Please try again!")
                                        continue

                                    else:
                                        c = random.randint(1, 6) # generate a random number between 1 and 6 both included
                                        
                                        print("\n"+ response +", you chose: {0}".format(attacks[a-1])) # Reveal player's choice
                                        print("The computer chose: {0}".format(attacks[c-1]))          # Reveal computer's choice
                                                                                                           
                                                                                                           # Compare the 2 attacks and 
                                                                                                           # announce the winner
                                        if a == 1 and c == 2:
                                            balance = sub(balance, bet)                                            
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 1 and c == 3:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 1 and c == 4:
                                            balance = add(balance, bet)                                           
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 1 and c == 5:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 1 and c == 6:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 2 and c == 1:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 2 and c == 3:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 2 and c == 4:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 2 and c == 5:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 2 and c == 6:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 3 and c == 1:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 3 and c == 2:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 3 and c == 4:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 3 and c == 5:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 3 and c == 6:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 4 and c == 1:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 4 and c == 2:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 4 and c == 3:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 4 and c == 5:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 4 and c == 6:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${0}".format(balance))
                                        elif a == 5 and c == 1:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 5 and c == 2:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 5 and c == 3:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 5 and c == 4:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 5 and c == 6:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 6 and c == 1:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 6 and c == 2:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 6 and c == 3:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 6 and c == 4:
                                            balance = sub(balance, bet)
                                            print("Unfortunately, "+response+" you lost")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == 6 and c == 5:
                                            balance = add(balance, bet)
                                            print("Congratulations, you won "+response+"!")
                                            print("\nYour current balance is ${:,.2f}".format(balance))
                                        elif a == c:
                                            print("Its a tie. No winner")
                                            print("\nYour current balance is ${:,.2f}".format(balance))

                                    break # Break from attack loop

                                break # Break from bet input loop   
                        else:
                            rbal.append(balance) # append the final balance when bal = 0
                            print("\nGoodbye "+response+". Your final balance is ${:,.2f}".format(balance)) # Print an exit message with the final balance
                            print("\nYour balance history is:") # Give player a run down of balance history
                            print("Starting balance: ${:,.2f}".format(STARTING_BALANCE)) # starting balance
                            # print(rbal)
                            for i in range(rnd): # loop for printing the balance for each round played
                                print("After round {0}: ${1:,.2f}".format(i+1, rbal[i+1]))
                            sys.exit() # exit the program

                elif choice.lower() == 'q': # When pressed gives the players a run down of his/her history before exiting
                    rbal.append(balance)
                    print("\nGoodbye "+response+". Your final balance is ${0}".format(balance))
                    print("\nYour balance history is:")
                    print("Starting balance: ${:,.2f}".format(STARTING_BALANCE))
                    # print(rbal)
                    for i in range(rnd):
                        print("After round {0}: ${1:,.2f}".format(i+1, rbal[i+1]))
                    sys.exit()

                else:
                    print("That's an invalid choice. Please try again!") # gives an error and continues back to the game menu.
                    continue   

if __name__ == "__main__":
    main()