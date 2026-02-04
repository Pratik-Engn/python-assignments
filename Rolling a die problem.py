import random
print("welcome to the game of dicing")
die1= [1,2,3,4,5,6]
while True:
    choice = input("start the role")
    if choice == "start":
        random.shuffle(die1)
        print("Dice roll:", die1[0])

    elif choice== "quit":
        break
    else:
        print("enter valid choice")
print("have a nice day thank you for the game")
