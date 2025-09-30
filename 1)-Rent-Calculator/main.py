# Rent Calculating app

# Input from user --
rent = int(input("Enter your Total House rent:-"))
food = int(input("Enter your Total food orderd :-"))
electrcity_speend = int(input("Enter your total electrcity_speend :-"))
charge_unit = int(input("Chrage per unit :-"))
person = int(input("how many person living in room :-"))

# calculate total electrcity into par charge unit 
total_bill = electrcity_speend * charge_unit

# calculate total rent --
calculate_rent = (rent + food + total_bill) 

# print all the statment--
print(f"House Rent{rent}")
print(f"Total Food Expense:")
print(f"Total electrcity bill{total_bill}")
total_rent = calculate_rent // person
print("-" * 40)  # using for line 
print(f"Total person living in the room:- {person}")
print(calculate_rent)
print(f"total-equel each person :-{total_rent}")
