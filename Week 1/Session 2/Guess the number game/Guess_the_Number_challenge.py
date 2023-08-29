import random

def new_game():
    print("----------------------------------------------------------------")
    print("Welcome to the guess the number game!")
    
    unknown = int(random.randint(0,20))
    #print(unknown)
    test = False
    tries = 2
    guess = int (input("Enter your guess :"))
    while (test == False or tries != 0):
        if guess == unknown:
            test = True
            print (f"CONGRATS! You WON!!!! The number is {unknown}")
            break
        elif tries != 0:
            tries -= 1
            if guess < unknown:
                print ("HINT : the number is higher than your guess!")
            else:
                print ("HINT : the number is lower than your guess!")
            guess = int (input("Guess again :"))
        else:
            print (f"OOPS you're out of tries! The number is {unknown}")
            break
    again = int (input ("Press 1 to play again ! Press 0 to exit!  "))
    if again == 1:
        new_game()
    elif again == 0:
        quit()
    else:
        print ("OOPS wrong entry game will end!")        

new_game()


