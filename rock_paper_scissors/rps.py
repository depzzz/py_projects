from random import choice
import sys

# set up options r,p,s
options = ['rock','paper','scissors']

# gib a random value to comp
computer = choice(options)

# let the user choose how many times they wanna play
print("How many times do you want to play?")
try:
    chances = int(input())
except ValueError:
    print("Not a Number!")
    sys.exit(1)

# set scores of both player and computer to zero
pscore, cscore, ties = 0, 0, 0

# run the game while there are chances
while chances != 0:
    player = input("Rock, Paper or Scissors? ").lower()

    if player == computer:
        print(f"Tie! Computer is also {computer}")
        ties += 1
        print()
    elif player == "rock":
        if computer == "paper":
            print(f"You Lose! Computer was {computer}")
            print()
            cscore += 1
        elif computer == "scissors":
            print(f"You Win! Computer was {computer}")
            print()
            pscore += 1
    elif player == "paper":
        if computer == "rock":
            print(f"You Win! Computer is {computer}")
            print()
            pscore += 1
        elif computer == "scissors":
            print(f"You Lose! Computer was {computer}")
            print()
            cscore += 1
    elif player == "scissors":
        if computer == "rock":
            print(f"You Lose! Computer was {computer}")
            print()
            cscore += 1
        elif computer == "paper":
            print(f"You Win! Computer is {computer}")
            print()
            pscore += 1
    else:
        print("Not a valid input sussy boy.")
        print()

    computer = choice(options)
    chances -= 1

# print the scores
print()
print(f'Your Score: {pscore}')
print(f'Computer\'s Score: {cscore}')
print(f'Ties: {ties}')
print()