# Ultimate Ninja Combat Game!!! 
# The player fights against the computer, and the winner gets bragging rights


import random, sys # random for generating random attacks
                   # sys for exiting the program when user quits.
 


def instructions(): # handles the display of instructions
    print("\nWelcome to Ultimate Ninja Battle Combat!!! "
    "\nYou will be fighting against the computer, and the winner gets bragging rights. "
    "\nFor each turn you will be asked to use one of the 6 attacks below:"
    "\n(1)Punch of Fury"
    "\n(2)Kick of Punishment"
    "\n(3)Sword of Justice"
    "\n(4)Shuriken of Vengeance"
    "\n(5)Nunchucks of Anger"
    "\n(6)Knife of Freedom \n"
    "Choose wisely.")    

def sub(balance, bet): #updates the balace at start

    newBalance = balance - bet
    return newBalance

def add(balace, bet):
    
    newBalance = balace + bet
    return newBalance

def main():

    STARTING_BALANCE = 100
    STARTING_BET = 0

    

    print("Welcome to Ultimate Ninja Combat Game!!!")

    while True:

        response = input("Please enter your name: ")

        if (response.isalpha()) == False:
            print("\nInvalid! Please try again!\n")
            continue
        
        else:

            print("Welcome,",response)

            balance = sub(STARTING_BALANCE, STARTING_BET)

            print("\nYour current balance is ${:,.2f}".format(balance))


            rnd = 0
            rbal = []


            while True:

                choice = input("\nPlease choose from the following menu:"
                "\n(I)nstructions"
                "\n(P)lay game"
                "\n(Q)uit game\n")

                if choice.lower() == 'i':
                    instructions()

                elif choice.lower() == 'p':

                    while True:

                        if balance != 0:

                            print("\nPlease enter the amount to bet. All bets must be multiples of 5.")
                            bet = int(input())
                        
                            if bet%5 != 0:
                                print("You choose to bet ${:,.2f}".format(bet))
                                print("\nThat is not a valid amount. Your bet must be a multiple of 5, "
                                "and be within your means.")

                            elif bet%5 == 0 and bet > balance:
                                print("You choose to bet ${:,.2f}".format(bet))
                                print("\nThat is not a valid amount. Your bet must be a multiple of 5, "
                                "and be within your means.")

                            else:
                                rnd+=1
                                rbal.append(balance)
                                
                                print("You choose to bet ${:,.2f}".format(bet))

                                attacks = ["Punch of Fury","Kick of Punishment", "Sword of Justice", 
                                "Shuriken of Vengeance", "Nunchucks of Anger", "Knife of Freedom"]

                                while True:

                                    print("\n"+ response + ", you must choose one of the following attacks:"
                                    "\n(1)Punch of Fury"
                                    "\n(2)Kick of Punishment"
                                    "\n(3)Sword of Justice"
                                    "\n(4)Shuriken of Vengeance"
                                    "\n(5)Nunchucks of Anger"
                                    "\n(6)Knife of Freedom")
                                    
                                    a = int(input())

                                    if a < 1:
                                        print("Invalid choice. Please try again!")
                                        continue

                                    elif a > 6:
                                        print("Invalid choice. Please try again!")
                                        continue

                                    else:
                                        c = random.randint(1, 6)
                                        
                                        print("\n"+ response +", you chose: {0:>10}".format(attacks[a-1]))
                                        print("The computer chose: {0:>15}".format(attacks[c-1]))

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

                                    break

                                break    
                        else:
                            rbal.append(balance)
                            print("\nGoodbye "+response+". Your final balance is ${:,.2f}".format(balance))
                            print("\nYour balance history is:")
                            print("Starting balance: ${:,.2f}".format(STARTING_BALANCE))
                            # print(rbal)
                            for i in range(rnd):
                                print("After round {0}: ${1:,.2f}".format(i+1, rbal[i+1]))
                            sys.exit()

                elif choice.lower() == 'q':
                    rbal.append(balance)
                    print("\nGoodbye "+response+". Your final balance is ${0}".format(balance))
                    print("\nYour balance history is:")
                    print("Starting balance: ${:,.2f}".format(STARTING_BALANCE))
                    # print(rbal)
                    for i in range(rnd):
                        print("After round {0}: ${1:,.2f}".format(i+1, rbal[i+1]))
                    sys.exit()

                else:
                    print("That's an invalid choice. Please try again!")
                    continue   

if __name__ == "__main__":
    main()