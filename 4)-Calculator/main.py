# simple calculator in python --

# opretor --
print('''
      addition : +
      subtraction : -
      multiply : *
      division : /
      moduler : **
      ''')

# get two number from user :-
num1 = int(input("Enter a first number :-"))
num2 = int(input("Enter a second number :-"))
symbol = input('Enter a opreator :-')

# condition :-
if symbol == '+':
    print(num1 + num2)
    
elif symbol == '-':
    print(num1 - num2)
    
elif symbol == '*':
    print(num1 * num2)

elif symbol == '/':
    print(num1 / num2)

elif symbol == '**':
    print(num1 ** num2)
    
else:
    print('invalid syntax -')