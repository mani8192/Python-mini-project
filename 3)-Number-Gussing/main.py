# number gussing game --

# 1 --module import 
import random

# get number -
computer_time = random.randint(1,10)
user_time = int(input("Guess your number :-"))

# condition --
if computer_time > user_time:
    print('Computer Won :-' , user_time)
    print('Computer number' , computer_time)

elif computer_time == user_time:
    print('Game drw :-',user_time)
    print('Computer number' , computer_time)
    
    
elif computer_time < user_time:
    print('You won game :-' , user_time)
    print('Computer number' , computer_time)
    
# check invalid input
elif user_time > 1 or user_time < 10:
    print('Invlid number:-')