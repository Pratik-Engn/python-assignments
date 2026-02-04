#asking name of the user and giving a output
name1=input("enter your name")
print(f"Hello {name1}!")
#die role problem
import random
print("welcome to the game of dice role")
Die1=(1,2,3,4,5,6)
choice=input("enter 'Play' to start and 'quit' to end the game")
if choice=="Play":
    roll = random.choice(Die1)
    print("You rolled a ",roll)

elif choice=="Quit":
    print("Thank you for playing")

else: print ("The desired input is invalid")

#dictionaries operation
user={"name":"Pratik","age":22,"city":"Bangal"}
user.pop("city")
print (f'Here is it',name[1])