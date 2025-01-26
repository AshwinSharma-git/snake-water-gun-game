# 1 for snake , -1 for water , 0 for gun 
import random

computer = random.choice([-1, 1, 0])
youstr = input("enter ur choice: ")
youDict = {"s": 1,"w": -1,"g": 0}
reverseDict = {1: "snake",-1: "water",0: "gun"}

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you):
    print("its a tie sharma ji")

else:
    if(computer == -1 and you == 1):
        print("you win! sharma ji")

    elif(computer == -1 and you == 0):
        print("opps you lose! bhai")

    elif(computer == 1 and you == -1):
        print("opps you lose! bhai")

    elif(computer == 1 and you == 0):
        print("you win! sharma ji")

    elif(computer == 0 and you == -1):
        print("you win! sharma ji")

    elif(computer == 0 and you == 1):
        print("oops you lose! bhai")

    else:
        print("something went wrong") 