import random, sys

choice = random.randint(1,20)
play = True

while play:
    for i in range(5):
        try:
            user = int(input("Enter a Number between 1 to 20: "))
        except ValueError:
            print("Invalid Integer!")
            sys.exit(1)
        if user > 0 and user < 20:
            if user == choice:
                print("You Won!")
                break
            if user > choice:
                print("Too High")
            if user < choice:
                print("Too Low")
        else:
            print("Invalid Range")

    again = input("Out of Attempts! Play again? y/n: ")
    if again.lower() in ("y","yes"):
        play = True
    else:
        play = False

print("Thanks for Playing!")