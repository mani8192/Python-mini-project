# Restorent management system

print('Welcome to our restaurant 😛 :-')

# menu 
resto_menu = {
    'Burger': 49,
    'Pizza': 101,
    'Pasta': 120,
    'Sandwich': 60,
    'Fries': 70,
    'Noodles': 110,
    'Momos': 90,
    'Taco': 130,
    'Hotdog': 85,
    'Paneer Roll': 95,
    'Chicken Wrap': 150,
    'Spring Roll': 80,
    'Salad': 75,
    'Cold Coffee': 65,
    'Ice Cream': 55
}

# user input -- First food
user_choise = input('Enter your food: ')

if user_choise in resto_menu:
    print('Your order is confirmed:', user_choise)
else:
    print('Sorry! Item not available.')
    
    
# user input -- Second food
user_choise2 = input('Enter your second food: ')

for item, price in resto_menu.items():
    if user_choise2 == item:
        print('Food price :-', price)


# not complete