#  rock-parper-scissor Game --

# module
import random

# game choise
game_point = ["rock" , "paper" , "scissor"]

# input --
com_choise = random.choice(game_point)
user_choise = input("Enter a your choise :-").lower()

print(f"user choise - {user_choise} , computer choise is - {com_choise}")


# condition statment--

# game tai
if com_choise == user_choise:
    print("both choise same:- Game tai👍" )

elif user_choise == "rock":
    if com_choise == "paper":
        print("computer win")
    else:
        print("you win")

elif user_choise == "paper":
    if com_choise == "scissor":
        print("computer win") 
    else:
        print("you win")
        
elif user_choise == "scissor":
    if com_choise == "rock":
        print("computer win")
        
    else:
        print("you win")
        
# greting
print("Thanku play again😊")
        
        
     