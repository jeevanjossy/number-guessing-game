# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 11:38:24 2023

@author: Jossy
"""

while True:
    print(' ')
    print("---------------------------------------------")
    print("~~~~~ # THE ULTIMATE NUMBER - GUESSER # ~~~~~")   
    print("---------------------------------------------")
    print("Welcome to the Number - Guesser Game!")
    print("_____________________________________________")
    print("Option 1: One Player")
    print("Option 2: Two Player")
    print("_____________________________________________")
    print("A number have been selected between 1 and 20.")
    print("Can you guess it!?")
    print("Guess it in least attempts to gain max(10) points!")
    print("_____________________________________________")
    opt=int(input("Select the option No."))
    print("_____________________________________________")
    
    
    if opt==1:
        import random
        number = random.randint(1, 20)
        
        
        attempts = 0
        points = 11
        while True:
            
            guess = int(input("Enter your guess: "))
            attempts += 1
            points -= 1
            
            if guess == number:
                print("Congrats! You guessed the number in",attempts,"attempts.")
                print("Your total points is :-",points)
                print("_______________________________________________")
                break
            
            elif abs(guess - number) == 1:         #abs(mod||) : source= google.
                    print("Very close! Try again.")
            elif abs(guess - number) <= 2:
                    print("Close! Try again.")
            elif guess < number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
                
    if opt==2:
        
        import random
        number = random.randint(1, 20)
        
        
        attempts = 0
        points1 = 11
        while True:
            
            guess = int(input("Player 1 enter your guess: "))
            attempts += 1
            points1 -= 1
            
            if guess == number:
                print("Congrats! You guessed the number in",attempts,"attempts.")
                print("Player 1 your total points is :-",points1)
                print("_______________________________________________")
                break
            
            elif abs(guess - number) == 1:         #abs(mod||) : source= google.
                    print("Very close! Try again.")
            elif abs(guess - number) <= 2:
                    print("Close! Try again.")
            elif guess < number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
                
        import random
        number = random.randint(1, 20)
        
        
        attempts = 0
        points2 = 11
        while True:
            
            guess = int(input("Player 2 enter your guess: "))
            attempts += 1
            points2 -= 1
            
            if guess == number:
                print("Congrats! You guessed the number in",attempts,"attempts.")
                print("Player 2 your total points is :-",points2)
                print("_______________________________________________")
                break
            
            elif abs(guess - number) == 1:         #abs(mod||) : source= google.
                    print("Very close! Try again.")
            elif abs(guess - number) <= 2:
                    print("Close! Try again.")
            elif guess < number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        
        if points1 > points2:
            print("Player 1 won the game with",(points1 - points2),"points.!")
            print("Congratulations Player 1!")
        elif points2 > points1:
            print("Player 2 won the game with",(points2 - points1),"points.!")
            print("Congratulations Player 2!")
        elif points1==points2:
            print("It was an Insane match!")
            print("Both the players have tied the game!!")
    print("______________________________________________________________________")
    w=int(input('To exit the program press 3 and to continue press 1 and enter:- '))
    if w==3:
        break         
        
            
        

