import random

your_wins = 0 
computer_wins = 0

options = ['rock', 'paper', 'scissors']
user_wins = 0
computer_wins = 0

while True:
    user_pick = input("Enter You Selection rock/paper/scissors/ q to Quit: ")

    if user_pick =='q':
        print('You Quit the Game')
        break

    if user_pick not in options:
        continue

    random_selection = random.randint(0,2)

    computer_pick = options[random_selection]

    ##user winning comditions

    if user_pick == 'rock' and computer_pick == 'scissors':
        print("You Won!")
        user_wins+=1
        continue

    elif user_pick == 'paper' and computer_pick == 'rock':
        print("You Won!")
        user_wins+=1
        continue

    elif user_pick == 'scissors' and computer_pick == 'paper':
        user_wins+=1
        continue
    
    else:
        print("Computer Won!")
        computer_wins+=1
        continue
    
print("You Won total: ", user_wins, "times")
print("Computer Won total: ", computer_wins, "times" )

if user_wins > computer_wins:
    print("You Are The Winner!")
else:
    print("Computer is the Winner!")

